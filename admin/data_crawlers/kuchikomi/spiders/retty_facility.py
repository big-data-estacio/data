# -*- coding: utf-8 -*-
import re, scrapy
from scrapy_redis.spiders import RedisSpider
from kuchikomi.items.retty_items import FacilityRettyItem


class RettyFacilitySpider(RedisSpider):

    name = "retty_facility"
    redis_key = "retty_facility"
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'kuchikomi.selenium_middleware.SeleniumMiddleware': 200,
            # 'kuchikomi.windows_selenium_middleware.SeleniumMiddleware': 200,
        },
    }

    # analyze
    def parse(self, response):
        items = dict()
        counter = 1
        item = FacilityRettyItem()
        item['restaurant_id'] = re.search('(?<=/)(\d+)', response.url).group()
        item['get_url'] = response.url
        item['url_pre'] = re.search('PRE(\d+)', response.url).group()
        item['url_area'] = re.search('ARE(\d+)', response.url).group()
        item['url_sub'] = re.search('SUB(\d+)', response.url).group()

        area_list = response.css('.restaurant-detail li.breadcrumb__item a span::text').extract()
        item['area'] = ''.join(area_list[1:])

        item['store_name'] = response.css('.restaurant-summary__display-name::text').get(default='null').strip()
        item['store_kana_name'] = response.css('.restaurant-summary__kana-name::text').get(default='null')

        info_label_list = response.css('.information-list dt.information-list__label span::text').getall()
        for index, dd in enumerate(response.css('.information-list dd.information-list__description')):
            if 'ジャンル' in info_label_list[index]:
                item['genre'] = ';'.join(dd.css('::text').getall())
            elif '定休日' in info_label_list[index]:
                item['regular_holiday'] = re.sub(r'\s+', ' ', (' '.join(dd.css(' ::text').getall())).strip())

        item['num_of_interested'] = response.css('button.wannago-button span:last-child::text').get(
            default='null').strip()
        store_popularity = len(response.css('.popularity.restaurant-summary__popularity-label svg').getall())
        item['store_popularity'] = 'null' if store_popularity == 0 else store_popularity

        item['description'] = self.format_list(response.css('.restaurant-description__body ::text').getall())
        item['description_title'] = response.css('.restaurant-description__catchcopy::text').get(
            default='null').strip()

        item['recommended_rate'] = response.css('.recommendation-rate__title::text').re_first('(\d+)%')
        item['num_of_persons_went'] = response.css('.recommendation-rate__body div:first-child>dd::text').re_first(
            '(\d+)人')
        recommended_text_list = response.css('.recommendation-rate__body dl dt::text').getall()
        recommended_text_score = response.css('.recommendation-rate__body dl dd::text').getall()
        for index, type in enumerate(recommended_text_list):
            if 'Excellent' in type:
                item['recommended_rate_excellent'] = recommended_text_score[index]
            elif 'Good' in type:
                item['recommended_rate_good'] = recommended_text_score[index]
            elif 'Average' in type:
                item['recommended_rate_average'] = recommended_text_score[index]
        item['recommended_num_of_people'] = response.css('.restaurant-summary__recommend-text strong::text').get(
            default='null').strip()

        item['number_of_photo'] = response.css(
            '.restaurant-detail__navigation li:nth-child(2) span::text').re_first('(?<=写真\()(\d+)')
        item['number_of_reviews'] = response.css(
            '.restaurant-detail__navigation li:nth-child(3) span::text').re_first('(?<=口コミ\()(\d+)')
        item['reviews_for_lunch'] = response.css(
            '.restaurant-detail__navigation li:nth-child(3) li:first-child> a::text').re_first('(?<=ランチ\()(\d+)')
        item['reviews_for_dinner'] = response.css(
            '.restaurant-detail__navigation li:nth-child(3) li:last-child> a::text').re_first('(?<=ディナー\()(\d+)')

        nearest_station = response.css('.information-list__item:nth-child(2)')
        if '最寄駅' in nearest_station.css('dt ::text').get(default='null').strip():
            item['nearest_station'] = nearest_station.css('dd ::text').get(default='null').strip()

        info_title_list = response.css('.restaurant-info-table dt::text').getall()
        for index, dd in enumerate(response.css('.restaurant-info-table dd')):
            if 'ジャンル' in info_title_list[index]:
                item['genre_info'] = ';'.join(dd.css('ul li::text').getall())
            elif '営業時間' in info_title_list[index]:
                item['business_hours'] = re.sub(r'\s+', ' ', (' '.join(dd.css('time pre::text').getall())).strip())
            elif '定休日' in info_title_list[index]:
                item['regular_holiday_info'] = re.sub(r'\s+', ' ', (' '.join(dd.css('time pre::text').getall())).strip())
            elif 'カード' in info_title_list[index]:
                payment_card = dd.css('strong::text').get(default='null').strip()
                item['payment_card'] = payment_card + ';'.join(dd.css('ul.credit-card-list li::text').getall())
            elif 'ランチ' in info_title_list[index]:
                item['lunch_budget'] = dd.css('dd::text').get(default="null").strip()
            elif 'ディナー' in info_title_list[index]:
                item['dinner_budget'] = dd.css('dd::text').get(default="null").strip()
            elif '住所' in info_title_list[index]:
                item['street_address'] = dd.css('a::text').get(default="null").strip()
            elif 'アクセス' in info_title_list[index]:
                item['access'] = self.format_list(response.css('pre span::text').getall())
            elif '店名' in info_title_list[index]:
                store_name = dd.css('dd ruby span::text').get(default='').strip()
                store_kana = dd.css('dd ruby rt::text').get(default='').strip()
                item['store'] = ';'.join([store_name, store_kana])
            elif '予約・問い合わせ' in info_title_list[index]:
                item['reservation_inquiry'] = dd.css('dd::text').get(default="null").strip()
            elif '電話番号' in info_title_list[index]:
                item['phone_number'] = dd.css('dd::text').get(default="null").strip()
            elif 'お店のホームページ' in info_title_list[index]:
                item['home_page'] = dd.css('dd li a::attr("href")').get(default="null")
            elif '備考' in info_title_list[index]:
                item['remarks'] = self.format_list(dd.css('dd span ::text').getall())
            elif 'FacebookのURL' in info_title_list[index]:
                item['facebook_url'] = dd.css('dd a::attr("href")').get(default="null")
            elif 'オンライン予約' in info_title_list[index]:
                item['online_booking'] = dd.css('dd a::attr("text")').get(default="null").strip()
            elif '宴会収容人数' in info_title_list[index]:
                item['banquet_capacity'] = dd.css('dd::text').re_first('(\d+)人')
            elif 'ウェディング・二次会対応' in info_title_list[index]:
                item['party_correspondence'] = dd.css('dd::text').get(default="null").strip()

            item['budget'] = self.format_list(response.css('.budgets__price::text').extract())

        items[counter] = item

        yield items

    @staticmethod
    def format_list(text_list):
        formatted_text = re.sub(r'\s+', '', ';'.join(text_list)) if len(text_list) > 0 else 'null'
        return formatted_text if formatted_text.strip() else 'null'
