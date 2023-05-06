# -*- coding: utf-8 -*-
import re
import requests
import redis
from bs4 import BeautifulSoup
from scrapy.utils.project import get_project_settings

class RettyTargetUrlSpider(object):
    redis_db = redis.StrictRedis(host=get_project_settings().get("REDIS_HOST"),
                                 port=get_project_settings().get("REDIS_PORT"), db=0)

    name = "retty_target_urls"
    redis_key_kuchikomi = "retty_kuchikomi"
    redis_key_facility = "retty_facility"

    # analyze
    def parse(self):
        htm = requests.get('https://retty.me/')
        soup = BeautifulSoup(htm.text, "html.parser")

        area_urls = []
        number_of_pref = 1 # 47
        for pref in range(1, number_of_pref+1):
            pref = str(pref) if len(str(pref)) > 1 else '0' + str(pref)
            soup_area = soup.find("section", {"key": "PRE" + pref}).get(":children")
            for url in re.findall("(?<=url: ')(\S+)(?=')", soup_area):
                if 'SUB' not in url:
                    area_urls.append(url)

        for area_url in area_urls:
            self.parse_prefecture_sub_area(area_url)

    def parse_prefecture_sub_area(self, response_url):
        htm_sub_area = requests.get(response_url)
        soup_sub_area = BeautifulSoup(htm_sub_area.text, "html.parser")

        sub_area_urls = []
        for ul in soup_sub_area.find("ul", class_="related-links__similars"):
            type_tag = type(ul.find("a"))
            if type_tag is not int:
                sub_area_urls.append(ul.find("a").get("href"))

        for sub_area_url in sub_area_urls:
            self.parse_prefecture_sub_area_paginate(sub_area_url)

    def parse_prefecture_sub_area_paginate(self, response_url):
        htm_sub_area_paginate = requests.get(response_url)
        soup_sub_area_paginate = BeautifulSoup(htm_sub_area_paginate.text, "html.parser")

        sub_area_pages_urls = []
        number_of_pages = soup_sub_area_paginate.findAll("li", class_="pager__item")[-1].text
        # number_of_pages = 1

        for page in range(1, int(number_of_pages) + 1):
            if page == 1:
                sub_area_pages_urls.append(response_url)
            else:
                sub_area_pages_urls.append(response_url + "page-{}/".format(str(page)))

        for sub_area_url_page in sub_area_pages_urls:
            self.parse_prefecture_sub_area_restaurant(sub_area_url_page)

    def parse_prefecture_sub_area_restaurant(self, response_url):
        htm_sub_area_restaurant = requests.get(response_url)
        soup_sub_area_restaurant = BeautifulSoup(htm_sub_area_restaurant.text, "html.parser")

        url_list = dict()
        count = 1
        for sel_restaurant_list in soup_sub_area_restaurant.findAll("li", class_="restaurants__item"):
            sel_restaurant_link = sel_restaurant_list.find("a")
            if sel_restaurant_link is not None:
                restaurant_url = sel_restaurant_link.get("href")
                restaurant_id = re.search('(?<=/)(\d+)', restaurant_url).group()

                url_json = '{"url":"' + str(restaurant_url) + '", "restaurant_id": "' + str(restaurant_id) + '"}'
                url_json_kuchikomi = '{"url":"' + str(restaurant_url+'reports/') + '", "restaurant_id": "' + str(restaurant_id) + '"}'

                self.redis_db.rpush(self.redis_key_facility, url_json)
                self.redis_db.rpush(self.redis_key_kuchikomi, url_json_kuchikomi)

                url_list[count] = url_json
                count += 1

        print(url_list)


if __name__ == '__main__':
    rettyclass = RettyTargetUrlSpider()
    rettyclass.parse()
