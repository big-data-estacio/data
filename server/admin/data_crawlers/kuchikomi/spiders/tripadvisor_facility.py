# -*- coding: utf-8 -*-
import base64
import json
import re, scrapy

from bs4 import BeautifulSoup
from kuchikomi.items.tripadvisor_items import FacilityTripAdvisorItem
from scrapy.http.request.form import FormRequest
from scrapy_redis.spiders import RedisSpider


class TripAdvisorFacilitySpider(RedisSpider):
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES"  : {
            'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
        },
        "DOWNLOAD_DELAY"          : .5,
        "RANDOMIZE_DOWNLOAD_DELAY": True
    }

    COOKIES_ENABLED = True
    COOKIES_DEBUG = True
    handle_httpstatus_list = [400, 403, 404]

    name = "tripadvisor_facility"
    redis_key = "tripadvisor_facility"

    # analyze
    def parse(self, response):
        temp_all = response.headers.getlist('Set-Cookie')
        cookie_TASession = ''
        for cookie in temp_all:
            if "TASession" in str(cookie):
                temp = cookie
                temp = temp.decode('utf-8')
                temp = temp.replace('TRA.true', 'TRA.false')
                match = re.search('TASession=(.*?)Domain=', temp)
                cookie_TASession = match.groups()[0]
                cookie_TASession = cookie_TASession.replace('ja', 'ALL')

        yield FormRequest(response.url,
                          method='GET',
                          headers={'Accept-Encoding': 'gzip, deflate, sdch',
                                   'Content-Type'   : 'text/html; charset=UTF-8',
                                   'User-Agent'     : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                                      '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                                   },
                          meta=response.meta,
                          cookies={'TASession': cookie_TASession, 'TALanguage': 'ALL'},
                          callback=self.parse_details)

    def parse_details(self, response):
        items = dict()
        counter = 1

        item = FacilityTripAdvisorItem()
        item['get_url'] = response.url
        item['url_area'] = re.findall(r'(?<=Reviews-)\w+-(\w+)', response.url)[0]
        item['area_id'] = area_id = re.search(r'(?<=g)(\d+)', response.url).group()
        item['facility_id'] = re.search(r'(?<=d)(\d+)', response.url).group()

        area = response.css('ul.breadcrumbs li [itemprop="title"]::text').extract()
        item['store_name'] = response.css('li.breadcrumb:last-child ::text').extract_first()
        area.append(item['store_name']) if item['store_name'] is not None else area
        item['area'] = ';'.join(area)

        overall_rating = response.css('div.ratingContainer span.ui_bubble_rating::attr(class)').re_first('bubble_(\d+)')
        item['overall_rating'] = str(int(overall_rating) / 10) if overall_rating is not None else 'null'
        review_count = response.css('span.reviewCount::text').re_first('\d+')
        item['number_of_reviews'] = str(review_count) if review_count is not None else 'null'

        rank = response.css('.header_popularity  ::text').extract()
        item['rank'] = ''.join(rank) if len(rank) > 0 else 'null'
        text_list = response.css('.header_links ::text').getall()
        cooking_genres = []
        for txt in text_list:
            text = txt.strip().replace(',','')
            if '￥' in text:
                item['price_range'] = text
            elif text:
                cooking_genres.append(text)
        item['cooking_genres'] = ', '.join(cooking_genres) if len(cooking_genres) > 0 else 'null'

        item['street_address'] = self.format_list((response.css('div.address span.detail ::text').extract()))
        item['phone_number'] = response.css('div.phone span.detail ::text').get(default='null').strip()
        item['number_of_photos'] = response.css('.mosaic_photos span.details ::text').re_first('\d+', default='null')
        item['award'] = self.format_list(response.css('div[class^="restaurants-detail-overview-cards-RatingsOverviewCard__award"] ::text').getall())

        for sel in response.css(
                'div[class^="restaurants-detail-overview-cards-RatingsOverviewCard__ratingQuestionRow--"] '):
            score_name = sel.css('::text').get(default='null').strip()
            score = sel.css('.ui_bubble_rating::attr("class")').re_first('\d+')
            score = str(int(score) / 10)
            if '食事' in score_name:
                item['food_score'] = score
            elif '雰囲気' in score_name:
                item['atmosphere_score'] = score
            elif '価格' in score_name:
                item['price_score'] = score
            elif 'サービス' in score_name:
                item['service_score'] = score

        script_basic_info = response.css('script[type="application/ld+json"]::text').get(default='null').strip()
        basic_info = json.loads(script_basic_info)

        class_category = response.css(
            'div[class^="restaurants-detail-overview-cards-DetailsSectionOverviewCard__categoryTitle"]::text').extract()
        class_text = response.css(
            'div[class^="restaurants-detail-overview-cards-DetailsSectionOverviewCard__tagText"]::text').extract()
        for index, cls in enumerate(class_category):
            if '料理' in cls:
                item['cuisine'] = class_text[index]
            elif '食事の時間帯' in cls:
                item['meal_hours'] = class_text[index]
            elif '食材別のメニュー' in cls:
                item['menu'] = class_text[index]
            elif '機能' in cls:
                item['function'] = class_text[index]

        item['location'] = response.css(
            'div[class^="restaurants-detail-overview-cards-LocationOverviewCard__addressLink"] :first-child::text').get(
            default="null")
        nearest_area = response.css(
            'span[class^="restaurants-detail-overview-cards-LocationOverviewCard__"] div ::text').getall()
        item['nearest_area'] = re.sub(r'\s+', ' ', ' '.join(nearest_area)) if len(nearest_area) > 0 else 'null'

        official_site = response.css(
            'div[class^="restaurants-detail-overview-cards-LocationOverviewCard__contactRow"] div::attr("data-encoded-url")').get()
        if official_site is not None:
            decoded_url = base64.b64decode(official_site)
            item['official_site'] = re.findall('_(.*?)_', BeautifulSoup(decoded_url, 'html.parser').text)[0]

        business_hours = response.css('span[class^="public-location-hours-LocationHours__hoursOpenerText"] span::text').getall()
        item['business_hours'] = self.format_list(business_hours)

        for sel in response.css('.collapsible div[data-name="ta_rating"] div.item'):
            label = sel.css('label::text').get()
            score = sel.css('span.row_num::text').get()
            if 'とても良い' in label:
                item['very_good_score'] = score
            elif 'とても悪い' in label:
                item['very_bad_score'] = score
            elif '良い' in label:
                item['good_score'] = score
            elif '普通' in label:
                item['average_score'] = score
            elif '悪い' in label:
                item['bad_score'] = score

        item['reviews_in_english'] = response.css('.collapsible div[data-tracker="英語"] .count::text').re_first('\d+', default=0)
        item['reviews_in_japanese'] = response.css('.collapsible div[data-tracker="日本語"] .count::text').re_first('\d+', default=0)

        items[counter] = item
        yield items

    @staticmethod
    def format_list(text_list):
        formatted_text = re.sub(r'\s+', '', ''.join(text_list)) if len(text_list) > 0 else 'null'
        return formatted_text
