# -*- coding: utf-8 -*-
import re
import time, logging
import redis
import scrapy
from math import ceil
from time import strftime
from scrapy.http.request.form import FormRequest
from scrapy.utils.project import get_project_settings


class TabelogTargetUrlSpider(scrapy.Spider):
    start_urls = ['https://tabelog.com/sitemap/']
    domain = 'https://tabelog.com'
    redis_db = redis.StrictRedis(host=get_project_settings().get("REDIS_HOST"),
                                 port=get_project_settings().get("REDIS_PORT"), db=0)

    name = "tabelog_target_urls_via_sitemap"
    redis_key_user = "tabelog_user"
    redis_key_kuchikomi = "tabelog_kuchikomi"
    redis_key_facility = "tabelog_facility"

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
           "target_url.header_middleware.HeaderMiddleware": 1,
        },
        "DOWNLOAD_DELAY"          : .5,
        "RANDOMIZE_DOWNLOAD_DELAY": True
    }

    # analyze
    def parse(self, response):
        for sel_region in response.css('.prefarea ul li'):
            prefecture = sel_region.css('a::attr("href")').extract_first()
            target_url = self.domain + str(prefecture)
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_prefecture_area)

    def parse_prefecture_area(self, response):
        for sel_prefecture in response.css('#arealst_sitemap ul li'):
            prefecture_area = sel_prefecture.css('a::attr("href")').extract_first()
            target_url = prefecture_area
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_area_sub_area)

    def parse_area_sub_area(self, response):
        for sel_prefecture_area in response.css('#arealst_sitemap ul li a'):
            prefecture_sub_area = sel_prefecture_area.css('a::attr("href")').extract_first()
            if prefecture_sub_area is not None:
                target_url = prefecture_sub_area
                yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_restaurant)

    def parse_restaurant(self, response):
        url_list = dict()
        count = 1
        for sel_restaurant_list in response.css('#rstlst_sitemap div.list .item'):
            restaurant_url = sel_restaurant_list.css('div.rstname a::attr("href")').extract_first()
            restaurant_id = re.search('(?<=/)(\d+)', restaurant_url).group()
            restaurant_url = self.domain + restaurant_url

            url_json = '{"url":"' + str(restaurant_url) + '", "restaurant_id": "'+ str(restaurant_id) + '"}'
            url_json_kuchikomi = '{"url":"' + str(restaurant_url+'dtlrvwlst') + '", "restaurant_id": "'+ str(restaurant_id) + '"}'

            self.redis_db.rpush(self.redis_key_facility, url_json)
            self.redis_db.rpush(self.redis_key_kuchikomi, url_json_kuchikomi)
            self.redis_db.rpush(self.redis_key_user, url_json_kuchikomi)

            url_list[count] = url_json
            count += 1

        yield url_list
