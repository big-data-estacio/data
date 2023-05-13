# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis


class TargetUrlPipeline(object):
    def __init__(self):
        # self.redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
        pass

    def process_item(self, item, spider):
        # for url in item.values():
        #     self.redis_db.rpush(str(spider.redis_key), str(url))
        return item
