# -*- coding: utf-8 -*-
import re
import redis
import scrapy
from scrapy.http.request.form import FormRequest
from scrapy.utils.project import get_project_settings

class RettyTargetUrlSpider(scrapy.Spider):
    start_urls = ['http://retty.me/']
    redis_db = redis.StrictRedis(host=get_project_settings().get("REDIS_HOST"),
                                 port=get_project_settings().get("REDIS_PORT"), db=0)

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'target_url.selenium_middleware.SeleniumMiddleware': 200,
        },
    }
    name = "retty_target_urls"
    redis_key_kuchikomi = "retty_kuchikomi"
    redis_key_facility = "retty_facility"

    # analyze
    def parse(self, response):
        for sel_region in response.css('ul.area-selector__areas li'):
            prefecture = sel_region.css('a::attr("data-area")').extract_first()
            target_url = sel_region.css('a::attr("href")').extract_first()
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_prefecture)

    def parse_prefecture(self, response):
        for sel_prefecture in response.css('.truncatable-contents  ul.truncatable-contents__content:first-child li'):
            prefecture_area = sel_prefecture.css('a::attr("href")').re_first('ARE(\d+)')
            target_url = sel_prefecture.css('a::attr("href")').extract_first()
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_prefecture_sub_area)

    def parse_prefecture_sub_area(self, response):
        for sel_prefecture_area in response.css('.truncatable-contents  ul.truncatable-contents__content:first-child li'):
            prefecture_sub_area_url = sel_prefecture_area.css('a::attr("href")').extract_first()
            if prefecture_sub_area_url is not None:
                target_url = prefecture_sub_area_url
                yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_prefecture_area_restaurant)

    def parse_prefecture_area_restaurant(self, response):
        number_of_pages = response.css('li.pager__item:last-child::text').extract_first()
        if number_of_pages is not None:
            target_url = response.url # first page
            for page in range(2, int(number_of_pages) + 1):
                target_url = response.url + "page-{}/".format(str(page))
                yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_restaurant_url)

    def parse_restaurant_url(self, response):
        url_list = dict()
        count = 1
        for sel_restaurant_list in response.css('ul.restaurant-list li.restaurants__item'):
            restaurant_url = sel_restaurant_list.css('.restaurant__detail a::attr("href")').extract_first()
            restaurant_id = re.search('(?<=/)(\d+)', restaurant_url).group()

            url_json = '{"url":"' + str(restaurant_url) + '", "restaurant_id": "' + str(restaurant_id) + '"}'
            url_json_kuchikomi = '{"url":"' + str(restaurant_url+'reports/') + '", "restaurant_id": "' + str(restaurant_id) + '"}'

            self.redis_db.rpush(self.redis_key_facility, url_json)
            self.redis_db.rpush(self.redis_key_kuchikomi, url_json_kuchikomi)

            url_list[count] = url_json
            count += 1

        print(url_list)

        yield url_list
