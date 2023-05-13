# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserTabelogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hotel_id            = scrapy.Field()
    kuchikomi_id        = scrapy.Field()
    customer_id         = scrapy.Field()
    customer_name       = scrapy.Field()
    number_of_visit     = scrapy.Field()
    get_url             = scrapy.Field()
    night_total_rating      = scrapy.Field()
    night_culinary_rating   = scrapy.Field()
    night_service_rating    = scrapy.Field()
    night_atmosphere_rating = scrapy.Field()
    night_cp_rating         = scrapy.Field()
    night_drink_rating      = scrapy.Field()
    night_amount            = scrapy.Field()
    day_total_rating        = scrapy.Field()
    day_culinary_rating     = scrapy.Field()
    day_service_rating      = scrapy.Field()
    day_atmosphere_rating   = scrapy.Field()
    day_cp_rating           = scrapy.Field()
    day_drink_rating        = scrapy.Field()
    day_amount              = scrapy.Field()


class KuchikomiTabelogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hotel_id            = scrapy.Field()
    kuchikomi_id        = scrapy.Field()
    customer_id         = scrapy.Field()
    customer_name       = scrapy.Field()
    review_liked        = scrapy.Field()
    get_url             = scrapy.Field()
    night_total_rating      = scrapy.Field()
    night_culinary_rating   = scrapy.Field()
    night_service_rating    = scrapy.Field()
    night_atmosphere_rating = scrapy.Field()
    night_cp_rating         = scrapy.Field()
    night_drink_rating      = scrapy.Field()
    night_amount            = scrapy.Field()
    day_total_rating        = scrapy.Field()
    day_culinary_rating     = scrapy.Field()
    day_service_rating      = scrapy.Field()
    day_atmosphere_rating   = scrapy.Field()
    day_cp_rating           = scrapy.Field()
    day_drink_rating        = scrapy.Field()
    day_amount              = scrapy.Field()
    review_date             = scrapy.Field()
    review_title            = scrapy.Field()
    review_comment          = scrapy.Field()


class FacilityTabelogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hotel_id            = scrapy.Field()
    get_url             = scrapy.Field()
    url_pre             = scrapy.Field()
    url_area1           = scrapy.Field()
    url_area2           = scrapy.Field()
    area                = scrapy.Field()
    pillow              = scrapy.Field()
    store_name          = scrapy.Field()
    overall_rating      = scrapy.Field()
    night_total_rating  = scrapy.Field()
    day_total_rating    = scrapy.Field()
    number_of_reviews   = scrapy.Field()
    number_of_photo     = scrapy.Field()
    review_menu         = scrapy.Field()
    nearest_station     = scrapy.Field()
    genre               = scrapy.Field()
    night_budget        = scrapy.Field()
    day_budget          = scrapy.Field()
    regular_holiday     = scrapy.Field()
    store_name_detail        = scrapy.Field()
    awards_selection_history = scrapy.Field()
    genre_detail             = scrapy.Field()
    reservation_inquiry      = scrapy.Field()
    reservation_acceptability= scrapy.Field()
    street_address           = scrapy.Field()
    transportation           = scrapy.Field()
    business_hours           = scrapy.Field()
    regular_holiday_details  = scrapy.Field()
    night_budget_detail      = scrapy.Field()
    day_budget_detail        = scrapy.Field()
    night_budget_in_reviews  = scrapy.Field()
    day_budget_in_reviews    = scrapy.Field()
    method_of_payment        = scrapy.Field()
    service_charge           = scrapy.Field()
    number_of_seats         = scrapy.Field()
    private_room            = scrapy.Field()
    reserved                = scrapy.Field()
    smoking                 = scrapy.Field()
    parking                 = scrapy.Field()
    space_facilities        = scrapy.Field()
    mobile                  = scrapy.Field()
    course                  = scrapy.Field()
    drink                   = scrapy.Field()
    cooking                 = scrapy.Field()
    use_scene               = scrapy.Field()
    location                = scrapy.Field()
    service                 = scrapy.Field()
    children                = scrapy.Field()
    home_page               = scrapy.Field()
    official_account        = scrapy.Field()
    open_date               = scrapy.Field()
    phone_number            = scrapy.Field()
    remarks                 = scrapy.Field()
    original_contributor    = scrapy.Field()