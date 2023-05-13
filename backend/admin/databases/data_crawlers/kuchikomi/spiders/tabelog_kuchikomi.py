# -*- coding: utf-8 -*-
import re
import json
from math import ceil
from scrapy_redis.spiders import RedisSpider
from scrapy.http.request.form import FormRequest
from kuchikomi.items.tabelog_items import KuchikomiTabelogItem


class TabelogKuchikomiSpider(RedisSpider):
    domain_name = 'https://tabelog.com'

    name = "tabelog_kuchikomi"
    redis_key = "tabelog_kuchikomi"
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "kuchikomi.header_middleware.HeaderMiddleware": 1,
            # 'kuchikomi.proxy_middlewares.ProxyMiddleware' : 2,
        },
        "DOWNLOAD_DELAY"          : .5,
        "RANDOMIZE_DOWNLOAD_DELAY": True
    }

    # analyze
    def parse(self, response):
        total_kuchikomi = response.css('span:last-child.c-page-count__num>strong::text').extract_first()
        number_of_pages = ceil(int(total_kuchikomi) / 20)
        for page in range(1, int(number_of_pages+1)):
            target_url = response.url + "?PG=" + str(page)
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_detail)

    def parse_detail(self, response):
        for sel_response in response.css('div > div.rvw-item'):
            comment_url = sel_response.css('p.rvw-item__title a::attr("href")').extract_first()
            if comment_url is not None:
                target_url = self.domain_name + str(comment_url)
                yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_comment)

    def parse_comment(self, response):
        items = dict()
        counter = 1
        for sel_response in response.css('div > div.rvw-item'):
            item = KuchikomiTabelogItem()
            item['get_url'] = response.url
            item['hotel_id'] = re.search(r'[0-9]+(?=/dtlrvwlst)', response.url).group()

            for sel_data in sel_response.css('div.rvw-item__rvwr-data'):
                item['customer_id'] = sel_data.css("p.rvw-item__rvwr-name a::attr('href')").re_first('rvwr/([0-9A-Za-z]+)/')
                item['customer_name'] = sel_data.css("p.rvw-item__rvwr-name a > span > span::text").extract_first()

            for sel_info in sel_response.css('div.rvw-item__rvw-info'):
                for sel in sel_info.css("ul.rvw-item__ratings > li"):
                    list_class = sel.css('li::attr("class")').extract_first()
                    if 'rvw-item__ratings-item' in list_class:
                        check_class = sel.css(".c-rating > span::attr('class')").extract_first()
                        if 'dinner' in check_class:
                            item['night_total_rating'] = sel.css("b.c-rating__val::text").extract_first()
                            item['night_culinary_rating'] = sel.css("li:nth-child(1) strong::text").extract_first()
                            item['night_service_rating'] = sel.css("li:nth-child(2) strong::text").extract_first()
                            item['night_atmosphere_rating'] = sel.css("li:nth-child(3) strong::text").extract_first()
                            item['night_cp_rating'] = sel.css("li:nth-child(4) strong::text").extract_first()
                            item['night_drink_rating'] = sel.css("li:nth-child(5) strong::text").extract_first()
                        elif 'lunch' in check_class:
                            item['day_total_rating'] = sel.css("b.c-rating__val::text").extract_first()
                            item['day_culinary_rating'] = sel.css("li:nth-child(1) strong::text").extract_first()
                            item['day_service_rating'] = sel.css("li:nth-child(2) strong::text").extract_first()
                            item['day_atmosphere_rating'] = sel.css("li:nth-child(3) strong::text").extract_first()
                            item['day_cp_rating'] = sel.css("li:nth-child(4) strong::text").extract_first()
                            item['day_drink_rating'] = sel.css("li:nth-child(5) strong::text").extract_first()
                    if 'otherdata' in list_class:
                        food_time_class = sel.css(".c-rating > span::attr('class')").extract()
                        food_time_amount = sel.css('strong.rvw-item__usedprice-price::text').extract()
                        for index, time_class in enumerate(food_time_class):
                            if 'dinner' in time_class:
                                item['night_amount'] = food_time_amount[index]
                            if 'lunch' in time_class:
                                item['day_amount'] = food_time_amount[index]

            for index,sel_contents in enumerate(sel_response.css('div.rvw-item__review-contents-wrap .rvw-item__review-contents')):
                if index == 0:
                    item['kuchikomi_id'] = sel_contents.css('div.rvw-item__review-contents::attr("id")').extract_first()
                    item['review_date'] = sel_contents.css('div.rvw-item__single-date p::text').re_first(r'\S+')
                    item['review_title'] = self.format_list(sel_contents.css('p.rvw-item__title strong::text').get(default='null').strip())
                    item['review_comment'] = self.format_list(sel_contents.css('div.rvw-item__rvw-comment p::text').extract())
                    review_liked_filter = sel_contents.css('div.rvw-item__contents-footer div.js-like-source::text').extract_first()
                    item['review_liked'] = json.loads(review_liked_filter)['count']

            items[counter] = item
            counter = counter+1
        yield items

    @staticmethod
    def format_list(text_list):
        formatted_text = re.sub(r'\s+', '', ''.join(text_list)) if len(text_list) > 0 else 'null'
        return formatted_text if formatted_text.strip() else 'null'
