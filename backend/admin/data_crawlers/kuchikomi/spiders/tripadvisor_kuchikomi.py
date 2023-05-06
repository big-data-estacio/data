# -*- coding: utf-8 -*-
import re
import time
from time import strftime

from kuchikomi.items.tripadvisor_items import KuchikomiTripAdvisorItem
from scrapy.http.request.form import FormRequest
from scrapy_redis.spiders import RedisSpider


class TripAdvisorRestaurantKuchikomiSpider(RedisSpider):
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES"  : {
            'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
            'kuchikomi.proxy_middlewares.ProxyMiddleware': 1,
        },
        "DOWNLOAD_DELAY"          : .5,
        "RANDOMIZE_DOWNLOAD_DELAY": True
    }

    # start_urls = ['https://www.tripadvisor.jp/Restaurant_Review-g1066451-d6692412/?_type=json&start=0']
    domain_name = 'https://www.tripadvisor.jp'
    COOKIES_ENABLED = True
    COOKIES_DEBUG = True
    handle_httpstatus_list = [400, 403, 404]

    name = "tripadvisor_kuchikomi"
    redis_key = "tripadvisor_kuchikomi"
    g_cd = '1066451'
    d_cd = '6692412'

    # analyze
    def parse(self, response):
        temp_all = response.headers.getlist('Set-Cookie')
        cookie_ta_session = ''
        for cookie in temp_all:
            if "TASession" in str(cookie):
                temp = cookie
                temp = temp.decode('utf-8')
                temp = temp.replace('TRA.true', 'TRA.false')
                match = re.search('TASession=(.*?)Domain=', temp)
                cookie_ta_session = match.groups()[0]
                cookie_ta_session = cookie_ta_session.replace('ja', 'ALL')

        yield FormRequest(
            response.url,
            method='GET',
            headers={
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Content-Type'   : 'text/html; charset=UTF-8',
                'User-Agent'     : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                   '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            },
            meta=response.meta,
            cookies={'TASession': cookie_ta_session, 'TALanguage': 'ALL'},
            callback=self.parse_review_list)

    # analyze
    def parse_review_list(self, response):
        for counter, sel in enumerate(response.xpath('.//*[@class="reviewSelector"]')):
            target_url = self.domain_name + sel.css('.quote a::attr("href")').extract_first()
            review_id = sel.css('::attr(data-reviewid)').extract_first()
            facility_id = re.search('(?<=d)(\d+)', response.url).group()
            area_id = re.search('(?<=g)(\d+)', response.url).group()
            response.meta.update(
                {"area_id": area_id, "facility_id": facility_id, "url": response.url, "review_id": str(review_id)})
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_detail)

    def parse_detail(self, response):
        # Save all item to items
        items = {}
        review_id = response.meta['review_id']
        for counter, sel in enumerate(response.xpath('.//*[@id="review_' + review_id + '"]')):
            item = KuchikomiTripAdvisorItem()
            # Set default value
            item['area_id'] = response.meta['area_id']
            item['facility_id'] = response.meta['facility_id']
            item['get_url'] = response.url

            item['review_id'] = sel.css('::attr(data-reviewid)').get(default='null').strip()
            item['title'] = sel.css('span.noQuotes::text').get(default='null').strip()

            post_date_temp = sel.css('span.ratingDate::attr(title)').get(default='null').strip()
            if post_date_temp is not 'null':
                post_date_temp = time.strptime(post_date_temp, "%Y年%m月%d日")
                item['post_date'] = strftime("%Y-%m-%d", post_date_temp)

            stay_date_temp = sel.css('div.prw_reviews_stay_date_hsx::text').get(default='null').strip()
            if stay_date_temp is not 'null':
                stay_date_temp = time.strptime(stay_date_temp, "%Y年%m月")
                item['stay_time'] = strftime("%Y-%m", stay_date_temp)

            for sel_m_info in sel.css('div.member_info'):
                item['post_area'] = sel_m_info.css('div.location span::text').get(default='null')
                item['reviewer_name'] = sel_m_info.css('div.username span::text').get(default='null').strip()
                class_name = sel_m_info.css('div.memberBadgingNoText span.ui_icon::attr("class")').extract()
                budge_text = sel_m_info.css('div.memberBadgingNoText span.badgetext::text').extract()
                for index, ui_class in enumerate(class_name):
                    if 'pencil-paper' in ui_class:
                        item['number_of_posts'] = budge_text[index]
                    if 'thumbs-up-fill' in ui_class:
                        item['number_of_likes'] = budge_text[index]

            comment = sel.css('div.entry p::text').extract()
            item['review'] = re.sub(r'\s+', '', ''.join(comment)) if len(comment) > 0 else 'null'

            temp = sel.css('div.reviewItemInline span::attr(class)').get(default='null').strip()
            if temp is not 'null':
                match = re.search('(?<=bubble_)(\d+)', temp)
                if match:
                    total_score = match.group()
                    item['total_score'] = str(int(total_score)/10)

            for sel_scores in sel.css('div.rating-list ul.recommend-column li.recommend-answer'):
                score = sel_scores.css('div.ui_bubble_rating::attr("class")').re_first('\d+')
                score = str(int(score) / 10)
                score_name = sel_scores.css('div.recommend-description::text').get(default='null').strip()
                if '食事' in score_name:
                    item['food_score'] = score
                elif '雰囲気' in score_name:
                    item['atmosphere_score'] = score
                elif '価格' in score_name:
                    item['price_score'] = score
                elif 'サービス' in score_name:
                    item['service_score'] = score

            post_useful = sel.css('.numHelp::text').get(default='null').strip()
            item['post_useful'] = post_useful.strip() if post_useful is not None else 'null'

            items[counter] = item

        yield items
