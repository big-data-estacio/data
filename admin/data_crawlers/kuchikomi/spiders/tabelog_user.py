# -*- coding: utf-8 -*-
import re
from math import ceil
from scrapy_redis.spiders import RedisSpider
from scrapy.http.request.form import FormRequest
from kuchikomi.items.tabelog_items import UserTabelogItem
from scrapy.utils.project import get_project_settings


class TabelogUserSpider(RedisSpider):
    domain_name = 'https://tabelog.com'

    name = "tabelog_user"
    redis_key = "tabelog_user"
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "kuchikomi.header_middleware.HeaderMiddleware": 1,
            # 'kuchikomi.proxy_middlewares.ProxyMiddleware': 2,
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
        items = dict()
        counter = 1
        for sel_response in response.css('div > div.rvw-item'):
            item = UserTabelogItem()
            item['get_url'] = self.domain_name + sel_response.css('div::attr("data-detail-url")').extract_first()
            item['hotel_id'] = re.search(r'[0-9]+(?=/dtlrvwlst)', response.url).group()
            item['kuchikomi_id'] = re.search(r'(?<=dtlrvwlst/)([0-9A-Za-z]+)', item['get_url']).group()

            for sel_data in sel_response.css('div.rvw-item__rvwr-data'):
                item['customer_id'] = sel_data.css("p.rvw-item__rvwr-name a::attr('href')").re_first('rvwr/([0-9A-Za-z]+)/')
                item['customer_name'] = sel_data.css("p.rvw-item__rvwr-name a > span > span::text").extract_first()

            for sel_info in sel_response.css('div.rvw-item__rvw-info'):
                number_of_visit = sel_info.css("div.rvw-item__visit-count span::text").extract()
                item['number_of_visit'] = ''.join(number_of_visit)
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

            items[counter] = item
            counter = counter+1
        yield items
