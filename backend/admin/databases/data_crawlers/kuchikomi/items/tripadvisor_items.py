# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KuchikomiTripAdvisorItem(scrapy.Item):
    area_id             = scrapy.Field()
    facility_id         = scrapy.Field()
    review_id           = scrapy.Field()
    get_url             = scrapy.Field()
    reviewer_name       = scrapy.Field()
    post_date           = scrapy.Field()
    post_area           = scrapy.Field()
    number_of_posts     = scrapy.Field()
    number_of_likes     = scrapy.Field()
    title               = scrapy.Field()
    review              = scrapy.Field()
    traveler_type       = scrapy.Field()
    stay_time           = scrapy.Field()
    total_score         = scrapy.Field()
    food_score          = scrapy.Field()
    service_score       = scrapy.Field()
    price_score         = scrapy.Field()
    atmosphere_score    = scrapy.Field()
    post_useful         = scrapy.Field()


class FacilityTripAdvisorItem(scrapy.Item):
    get_url             = scrapy.Field()
    url_area            = scrapy.Field()
    area_id             = scrapy.Field()
    facility_id         = scrapy.Field()
    area                = scrapy.Field()
    store_name          = scrapy.Field()
    overall_rating      = scrapy.Field()
    number_of_reviews   = scrapy.Field()
    rank                = scrapy.Field()
    price_range         = scrapy.Field()
    cooking_genres      = scrapy.Field()
    street_address      = scrapy.Field()
    phone_number        = scrapy.Field()
    business_hours      = scrapy.Field()
    number_of_photos    = scrapy.Field()
    award               = scrapy.Field()
    food_score          = scrapy.Field()
    service_score       = scrapy.Field()
    price_score         = scrapy.Field()
    atmosphere_score    = scrapy.Field()
    cuisine             = scrapy.Field()
    meal_hours          = scrapy.Field()
    function            = scrapy.Field()
    menu                = scrapy.Field()
    location            = scrapy.Field()
    nearest_area        = scrapy.Field()
    official_site       = scrapy.Field()
    very_good_score     = scrapy.Field()
    good_score          = scrapy.Field()
    average_score       = scrapy.Field()
    bad_score           = scrapy.Field()
    very_bad_score      = scrapy.Field()
    reviews_in_english   = scrapy.Field()
    reviews_in_japanese  = scrapy.Field()

    details             = scrapy.Field()
    travelers_type_family    = scrapy.Field()
    travelers_type_couple    = scrapy.Field()
    travelers_type_solo      = scrapy.Field()
    travelers_type__business = scrapy.Field()
    travelers_type_friend    = scrapy.Field()

