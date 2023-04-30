# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import IntegrityError
from kuchikomi.models import db_connect, create_table
from kuchikomi.models import RettyFacilityDB, RettyKuchikomiDB, TabelogFacilityDB, TabelogKuchikomiDB, TabelogUserDB, \
    TripAdvisorFacilityDB, TripAdvisorKuchikomiDB


class KuchikomiPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.session = scoped_session(sessionmaker(bind=engine))

    def process_item(self, items, spider):
        session = self.session()
        current_db = None
        if 'tabelog' in spider.name:
            if 'facility' in spider.name:
                current_db = TabelogFacilityDB
            elif 'kuchikomi' in spider.name:
                current_db = TabelogKuchikomiDB
            elif 'user' in spider.name:
                current_db = TabelogUserDB
        elif 'tripadvisor' in spider.name:
            if 'kuchikomi' in spider.name:
                current_db = TripAdvisorKuchikomiDB
            elif 'facility' in spider.name:
                current_db = TripAdvisorFacilityDB
        elif 'retty' in spider.name:
            if 'kuchikomi' in spider.name:
                current_db = RettyKuchikomiDB
            elif 'facility' in spider.name:
                current_db = RettyFacilityDB

        try:
            for item in items.values():
                session.add(current_db(**item))
                session.commit()
        except IntegrityError:
            session.rollback()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return items
