# -*- coding:utf-8 -*-
import os
from subprocess import call

os.chdir("target_url_crawlers/")
# example: for crawling tabelog restaurant
call(["scrapy", "runspider", "target_url/spiders/tabelog_target_url.py"])


os.chdir("../data_crawlers/")
# example: for tabelog restaurant review data
call(["scrapy", "runspider", "kuchikomi/spiders/tabelog_kuchikomi.py"])
os.chdir("../")
