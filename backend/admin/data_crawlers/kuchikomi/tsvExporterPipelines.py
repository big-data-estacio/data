# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from kuchikomi.items.tabelog_items import FacilityTabelogItem, KuchikomiTabelogItem, UserTabelogItem
from kuchikomi.items.tripadvisor_items import KuchikomiTripAdvisorItem, FacilityTripAdvisorItem
from kuchikomi.items.retty_items import KuchikomiRettyItem, FacilityRettyItem


class TsvExporterPipeline(object):
    def process_item(self, item, spider):
        item_fields = ''
        if 'tabelog' in spider.name:
            if 'facility' in spider.name:
                item_fields = FacilityTabelogItem
            elif 'kuchikomi' in spider.name:
                item_fields = KuchikomiTabelogItem
            elif 'user' in spider.name:
                item_fields = UserTabelogItem
        elif 'tripadvisor' in spider.name:
            if 'kuchikomi' in spider.name:
                item_fields = KuchikomiTripAdvisorItem
            elif 'facility' in spider.name:
                item_fields = FacilityTripAdvisorItem
        elif 'retty' in spider.name:
            if 'kuchikomi' in spider.name:
                item_fields = KuchikomiRettyItem
            elif 'facility' in spider.name:
                item_fields = FacilityRettyItem

        keys = list(item_fields.fields)
        formatted_item = self.get_formatted_item(item, item_fields)

        with open('../data/'+spider.name+'.tsv', 'a', encoding='UTF-8') as out_file:
            tsv_writer = csv.DictWriter(out_file, keys, dialect='excel-tab')
            if out_file.tell() == 0:
                tsv_writer.writeheader()
            tsv_writer.writerows(formatted_item)

    def get_formatted_item(self, item, item_class):
        z_key = {}
        z = dict(item_class.fields)
        z.update((k, 'null') for k in z.keys())
        z_key.update(z)
        formatted_item = []
        for k, v in item.items():
            z.update(z_key)
            z.update(v)
            formatted_item.append(z.copy())

        return formatted_item
