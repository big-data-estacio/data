# -*- coding: utf-8 -*-
import re
from math import ceil
from scrapy_redis.spiders import RedisSpider
from scrapy.http.request.form import FormRequest
from kuchikomi.items.retty_items import KuchikomiRettyItem


class RettyKuchikomiSpider(RedisSpider):
    name = "retty_kuchikomi"
    redis_key = "retty_kuchikomi"
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES"  : {
            'kuchikomi.selenium_middleware.SeleniumMiddleware': 200,
        },
    }

    # analyze
    def parse(self, response):
        total_kuchikomi = response.css('p.restaurant-detail__listing-info::text').re_first('(?<=全)(\d+)')
        if total_kuchikomi is not None:
            number_of_pages = ceil(int(total_kuchikomi) / 20)
            for page in range(1, int(number_of_pages+1)):
                target_url = response.url + "page-{}/" .format(str(page))
                yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_detail)

    def parse_detail(self, response):
        items = dict()
        counter = 1
        for sel_response in response.css('ul.restaurant-report-list > li'):
            item = KuchikomiRettyItem()
            item['restaurant_id'] = re.search('(?<=/)(\d+)', response.url).group()
            item['customer_name'] = sel_response.css('p.scored-reporter__name::text').get()
            score_class = sel_response.css('i.report-score::attr("class")').get()
            score_class = score_class.replace('--middle', '')
            item['overall_score'] = re.findall('--(\w+)', score_class)[0]

            tags = sel_response.css('div.restaurant-report__tags > ul > li a::text').getall()
            item['tags'] = ';'.join(tags) if len(tags) > 0 else 'null'

            review = sel_response.css('p.restaurant-report__text span::text').getall()
            item['review_comment'] = re.sub(r'\s+', '', ''.join(review))

            item['review_date'] = sel_response.css('time.restaurant-report__date span::text').get()
            item['num_of_likes'] = sel_response.css('button.report-reaction__button--like + span::text').get()
            item['num_of_interested'] = sel_response.css('button.report-reaction__button--wannago + span::text').get()

            item['kuchikomi_url'] = sel_response.css('.restaurant-report__link::attr("href")').get()
            item['kuchikomi_id'] = re.findall("(?<=/)(\d+)", item['kuchikomi_url'])[1]

            items[counter] = item
            counter = counter+1
        yield items
