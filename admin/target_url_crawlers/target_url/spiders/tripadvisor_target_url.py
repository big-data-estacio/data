import re
import scrapy
import redis
from scrapy.utils.project import get_project_settings


class TripadvisorTargetUrlSpider(scrapy.Spider):
    level_code = "294232"
    base_url = "https://www.tripadvisor.jp"
    start_urls = ["https://www.tripadvisor.jp/Restaurants-g294232-Japan.html"]
    redis_db = redis.StrictRedis(host=get_project_settings().get("REDIS_HOST"),
                                 port=get_project_settings().get("REDIS_PORT"), db=0)

    name = "tripadvisor_target_urls"
    redis_key_kuchikomi = "tripadvisor_kuchikomi"
    redis_key_facility = "tripadvisor_facility"

    def parse(self, response):
        data_offset = 0
        urls = []

        # pagination
        page_number = response.css('div.pageNumbers a:last-child::attr(data-page-number)').extract_first()
        total_page = int(page_number) + 1
        for i in range(1, total_page):
            if i == 1:
                for sel in response.css('div.geo_wrap'):
                    detail_url = sel.css('a::attr(href)').extract_first()
                    detail_url = self.base_url + detail_url
                    yield scrapy.Request(detail_url, callback=self.paginate_restaurant_page, meta=response.meta,
                                         dont_filter=True)
            else:
                data_offset += 20
                page_url = self.get_pagination_url(self.level_code, data_offset)
                urls.append(page_url)

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_page, meta=response.meta, dont_filter=True)

    def parse_page(self, response):
        d_urls = []
        for sel in response.css('ul.geoList li'):
            detail_url = sel.css('a::attr(href)').extract_first()
            detail_url = self.base_url + detail_url
            d_urls.append(detail_url)
        for url in d_urls:
            yield scrapy.Request(url, callback=self.paginate_restaurant_page, meta=response.meta, dont_filter=True)

    def get_pagination_url(self, site_code, data_offset):
        return self.base_url + '/Restaurants-g' + str(site_code) + '-oa' + str(data_offset) + '-Japan.html'

    def paginate_restaurant_page(self, response):
        data_offset = 0
        urls = []
        # pagination
        page_number = response.css('div.pageNumbers a:last-child::attr(data-page-number)').extract_first()
        area_code = re.search('(?<=g)(\d+)', response.url).group()
        total_page = int(page_number) + 1
        for i in range(1, total_page):
            data_offset += 30 if i > 1 else 0
            page_url = self.get_pagination_url(area_code, data_offset)
            urls.append(page_url)

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_restaurant_url, meta=response.meta, dont_filter=True)

    def parse_restaurant_url(self, response):
        url_list = dict()
        count = 1

        for restaurant_sel in response.css('#EATERY_LIST_CONTENTS div.title '):
            restaurant_url = restaurant_sel.css('a::attr("href")').extract_first()
            if restaurant_url is not None:
                restaurant_id = re.search('(?<=d)(\d+)', restaurant_url).group()

                url_json = '{"url":"' + self.base_url + str(restaurant_url) + '", "restaurant_id": "' + str(restaurant_id) + '"}'

                self.redis_db.rpush(self.redis_key_facility, url_json)
                self.redis_db.rpush(self.redis_key_kuchikomi, url_json)

                url_list[count] = url_json
                count += 1

            yield url_list
