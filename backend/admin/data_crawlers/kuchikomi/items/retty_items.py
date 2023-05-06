# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KuchikomiRettyItem(scrapy.Item):
    # define the fields for your item here like:
    restaurant_id       = scrapy.Field()
    kuchikomi_id        = scrapy.Field()
    kuchikomi_url       = scrapy.Field()
    customer_name       = scrapy.Field()
    overall_score       = scrapy.Field()
    review_comment      = scrapy.Field()
    tags                = scrapy.Field()
    review_date         = scrapy.Field()
    num_of_likes        = scrapy.Field()
    num_of_interested   = scrapy.Field()


class FacilityRettyItem(scrapy.Item):
    # define the fields for your item here like:
    restaurant_id       = scrapy.Field()
    get_url             = scrapy.Field()
    url_pre             = scrapy.Field()
    url_area            = scrapy.Field()
    url_sub             = scrapy.Field()
    area                = scrapy.Field()
    store_name          = scrapy.Field()
    store_kana_name     = scrapy.Field()
    num_of_interested   = scrapy.Field()
    store_popularity    = scrapy.Field()
    description         = scrapy.Field()
    description_title   = scrapy.Field()
    recommended_rate            = scrapy.Field()
    num_of_persons_went         = scrapy.Field()
    recommended_rate_excellent  = scrapy.Field()
    recommended_rate_good       = scrapy.Field()
    recommended_rate_average    = scrapy.Field()
    recommended_num_of_people   = scrapy.Field()
    dinner_budget       = scrapy.Field()
    lunch_budget        = scrapy.Field()
    budget              = scrapy.Field()
    nearest_station     = scrapy.Field()
    genre               = scrapy.Field()
    regular_holiday     = scrapy.Field()
    number_of_photo     = scrapy.Field()
    number_of_reviews   = scrapy.Field()
    reviews_for_lunch   = scrapy.Field()
    reviews_for_dinner  = scrapy.Field()
    genre_info          = scrapy.Field()
    business_hours      = scrapy.Field()
    regular_holiday_info = scrapy.Field()
    street_address      = scrapy.Field()
    access              = scrapy.Field()
    store               = scrapy.Field()
    reservation_inquiry = scrapy.Field()
    remarks             = scrapy.Field()
    phone_number        = scrapy.Field()
    home_page           = scrapy.Field()
    facebook_url        = scrapy.Field()
    banquet_capacity    = scrapy.Field()
    payment_card        = scrapy.Field()
    online_booking      = scrapy.Field()
    party_correspondence = scrapy.Field()

