# -*- coding: utf-8 -*-
import re
import scrapy
import redis
from scrapy.http.request.form import FormRequest
from scrapy.utils.project import get_project_settings


class TabelogTargetUrlSpider(scrapy.Spider):
    start_urls = ['https://tabelog.com']
    redis_db = redis.StrictRedis(host=get_project_settings().get("REDIS_HOST"),
                                 port=get_project_settings().get("REDIS_PORT"), db=0)

    name = "tabelog_target_urls"
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
        for sel_region in response.css('.rsttop-search__pref-container dd ul li'):
            prefecture = sel_region.css('a::attr("href")').extract_first()
            target_url = response.url + prefecture
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_prefecture)

    def parse_prefecture(self, response):
        for sel_prefecture in response.css('#tabs-panel-balloon-pref-area .list-balloon__list ul li'):
            prefecture_area = sel_prefecture.css('a::attr("href")').extract_first()
            target_url = prefecture_area
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_prefecture_sub_area)

    def parse_prefecture_sub_area(self, response):
        for sel_prefecture_area in response.css('#tabs-panel-balloon-pref-area .list-balloon__list ul li'):
            prefecture_sub_area = sel_prefecture_area.css('a::attr("href")').extract_first()
            if prefecture_sub_area is not None:
                target_url = prefecture_sub_area
                yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_prefecture_sub_area_filter)

    def parse_prefecture_sub_area_filter(self, response):
        # price range
        for i in range(12):
            lst_cost = str(i+1) if i < 11 else str(i)
            # day filter
            for day_wise in [1]:
                filter_data = {'LstCos': str(i), 'LstCosT': lst_cost, 'RdoCosTp': str(day_wise)}
                target_url = response.url+'rstLst/'
                yield FormRequest(target_url, method='GET', formdata=filter_data, meta=response.meta, callback=self.parse_restaurant_url)

    # def parse_prefecture_area_restaurant(self, response):
    #     total_kuchikomi = response.css('span:last-child.c-page-count__num>strong::text').extract_first()
    #     logging.info("kuchikomi:%s->%s" % (total_kuchikomi, response.url))
        # if total_kuchikomi:
        #     number_of_pages = ceil(int(total_kuchikomi) / 20)
        #     for page in range(1, number_of_pages + 1):
        #         target_url = response.url + "{}/".format(str(page))
        #         yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_restaurant_url, dont_filter=False)

    def parse_restaurant_url(self, response):
        url_list = dict()
        count = 1
        for sel_restaurant_list in response.css('ul.rstlist-info li.list-rst'):
            restaurant_url = sel_restaurant_list.css('li.list-rst::attr("data-detail-url")').extract_first()
            restaurant_id = re.search('(?<=/)(\d+)', restaurant_url).group()

            url_json = '{"url":"' + str(restaurant_url) + '", "restaurant_id": "'+ str(restaurant_id) + '"}'
            url_json_kuchikomi = '{"url":"' + str(restaurant_url+'dtlrvwlst') + '", "restaurant_id": "'+ str(restaurant_id) + '"}'

            self.redis_db.rpush(self.redis_key_facility, url_json)
            self.redis_db.rpush(self.redis_key_kuchikomi, url_json_kuchikomi)
            self.redis_db.rpush(self.redis_key_user, url_json_kuchikomi)

            url_list[count] = url_json
            count += 1

        yield url_list

        next_page = response.css('li.c-pagination__item a[rel$="next"]::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_restaurant_url)
