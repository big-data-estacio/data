# -*- config: utf-8 -*-

from sqlalchemy import create_engine, Column, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Text

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"), encoding='utf8')


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class RettyKuchikomiDB(DeclarativeBase):
    __tablename__ = "retty_kuchikomi"

    id              = Column(Integer, primary_key=True)
    restaurant_id   = Column('店舗ID', String(20), comment="restaurant_id")
    kuchikomi_id    = Column('クチコミID', String(20), comment="kuchikomi_id")
    kuchikomi_url   = Column('クチコミURL', String(500), comment="kuchikomi_url")
    customer_name   = Column('投稿者', String(50), comment="customer_name", nullable=True, default='null')
    overall_score   = Column('評価', String(20), comment="overall_score", nullable=True, default='null')
    review_comment  = Column('コメント', Text, comment="review_comment", nullable=True, default='null')
    tags            = Column('タグ', Text, comment="tags", nullable=True, default='null')
    review_date     = Column('投稿日時', String(20), comment="review_date", nullable=True, default='null')
    num_of_likes    = Column('いいね件数', String(10), comment="num_of_likes", nullable=True, default='null')
    num_of_interested = Column('行きたい件数', String(10), comment="num_of_interested", nullable=True, default='null')
    # composite unique constraint.
    UniqueConstraint(kuchikomi_id, restaurant_id, name="unique_key_rettyk")


class RettyFacilityDB(DeclarativeBase):
    __tablename__ = "retty_facility"

    id              = Column(Integer, primary_key=True)
    get_url         = Column('url', String(500), comment="URL")
    url_pre         = Column('url_pre', String(50), comment="URL_PRE")
    url_area        = Column('url_area', String(50), comment="URL_ARE")
    url_sub         = Column('url_sub', String(50), comment="URL_SUB")
    restaurant_id   = Column('店舗ID', String(20), comment="restaurant id")
    area            = Column('エリア', Text, comment="area")
    store_name      = Column('店舗名', String(100), comment="store_name")
    store_kana_name = Column('よみ', String(100), comment="store_kana_name", nullable=True, default='null')
    num_of_interested   = Column('行きたい件数', String(10), comment="num_of_interested", nullable=True, default='null')
    store_popularity    = Column('人気店★数', String(10), comment="store_popularity", nullable=True, default='null')
    description_title   = Column('紹介文タイトル', Text, comment="description_title", nullable=True, default='null')
    description         = Column('紹介文', Text, comment="description", nullable=True, default='null')
    recommended_rate    = Column('オススメ度(％)', String(10), comment="recommended_rate", nullable=True, default='null')
    num_of_persons_went = Column('行った人', String(20), comment="num_of_persons_went", nullable=True, default='null')
    recommended_rate_excellent = Column('オススメ度 Excellent', String(20), comment="recommended_rate_excellent", nullable=True, default='null')
    recommended_rate_good      = Column('オススメ度 Good', String(20), comment="recommended_rate_good", nullable=True, default='null')
    recommended_rate_average   = Column('オススメ度 Average', String(20), comment="recommended_rate_average", nullable=True, default='null')
    recommended_num_of_people  = Column('おすすめ人数', String(20), comment="recommended_num_of_people", nullable=True, default='null')
    dinner_budget   = Column('夜予算', String(50), comment="dinner_budget", nullable=True, default='null')
    lunch_budget    = Column('昼予算', String(50), comment="lunch_budget", nullable=True, default='null')
    nearest_station = Column('最寄り駅', Text, comment="nearest_station", nullable=True, default='null')
    genre           = Column('ジャンル', Text, comment="genre", nullable=True, default='null')
    regular_holiday = Column('定休日', String(100), comment="regular_holiday", nullable=True, default='null')
    number_of_photo = Column('写真', String(20), comment="number_of_photo", nullable=True, default='null')
    number_of_reviews = Column('すべてのクチコミ', String(20), comment="number_of_reviews", nullable=True, default='null')
    reviews_for_lunch = Column('ランチのクチコミ', String(20), comment="reviews_for_lunch", nullable=True, default='null')
    reviews_for_dinner= Column('ディナーのクチコミ', String(20), comment="reviews_for_dinner", nullable=True, default='null')
    genre_info        = Column('ジャンル(店舗情報)', Text, comment="genre", nullable=True, default='null')
    business_hours  = Column('営業時間', Text, comment="business_hours", nullable=True, default='null')
    regular_holiday_info = Column('定休日(店舗情報)', String(100), comment="regular_holiday_info", nullable=True, default='null')
    payment_card    = Column('カード', String(100), comment="payment_card", nullable=True, default='null')
    budget          = Column('予算', String(100), comment="budget", nullable=True, default='null')
    street_address  = Column('住所', Text, comment="street_address", nullable=True, default='null')
    access          = Column('アクセス', Text, comment="access", nullable=True, default='null')
    store           = Column('店名', Text, comment="store", nullable=True, default='null')
    reservation_inquiry = Column('予約・問い合わせ', String(50), comment="reservation_inquiry", nullable=True, default='null')
    remarks         = Column('備考', Text, comment="remarks", nullable=True, default='null')
    online_booking  = Column('オンライン予約', String(50), comment="online_booking", nullable=True, default='null')
    home_page       = Column('お店のホームページ', String(500), comment="home_page", nullable=True, default='null')
    facebook_url    = Column('FacebookのURL', String(500), comment="facebook_url", nullable=True, default='null')
    phone_number    = Column('電話番号', String(50), comment="phone_number", nullable=True, default='null')
    banquet_capacity= Column('宴会収容人数', String(20), comment="banquet_capacity", nullable=True, default='null')
    party_correspondence = Column('ウェディング・二次会対応', Text, comment="party_correspondence", nullable=True, default='null')
    # composite unique constraint.
    UniqueConstraint(url_pre, url_area, url_sub, restaurant_id, name="unique_key_rettyf")


class TripAdvisorKuchikomiDB(DeclarativeBase):
    __tablename__ = "tripadvisor_kuchikomi"

    id                  = Column(Integer, primary_key=True)
    area_id             = Column('エリアID:g', String(20), comment="area_id")
    facility_id         = Column('施設ID:d', String(20), comment="facility_id")
    review_id           = Column('クチコミID:', String(20), comment="review_idr")
    get_url             = Column('クチコミURL', String(500), comment="get_url")
    reviewer_name       = Column('投稿者', String(50), comment="reviewer_name")
    post_date           = Column('投稿日', String(20), comment="post_date", nullable=True, default='null')
    post_area           = Column('投稿者エリア', String(100), comment="post_area", nullable=True, default='null')
    number_of_posts     = Column('投稿数', String(10), comment="number_of_posts", nullable=True, default='null')
    number_of_likes     = Column('いいね数', String(10), comment="number_of_likes", nullable=True, default='null')
    title               = Column('タイトル', Text, comment="title", nullable=True, default='null')
    review              = Column('クチコミ', Text, comment="review", nullable=True, default='null')
    traveler_type       = Column('旅行者タイプ', String(20), comment="traveler_type", nullable=True, default='null')
    stay_time           = Column('訪問時期', String(20), comment="stay_time", nullable=True, default='null')
    total_score         = Column('総合評価', String(10), comment="total_score", nullable=True, default='null')
    food_score          = Column('食事', String(10), comment="food_score", nullable=True, default='null')
    service_score       = Column('サービス', String(10), comment="service_score", nullable=True, default='null')
    price_score         = Column('価格', String(10), comment="price_score", nullable=True, default='null')
    atmosphere_score    = Column('雰囲気', String(10), comment="atmosphere_score", nullable=True, default='null')
    post_useful         = Column('役にたった', String(10), comment="post_useful", nullable=True, default='null')
    # composite unique constraint.
    UniqueConstraint(area_id, facility_id, review_id, name="unique_key_tak")


class TripAdvisorFacilityDB(DeclarativeBase):
    __tablename__ = "tripadvisor_facility"

    id                  = Column(Integer, primary_key=True)
    get_url             = Column('URL', String(500), comment="get_url")
    url_area            = Column('URL_エリア', String(100), comment="url_area")
    area_id             = Column('エリアID:g', String(20), comment="area_id")
    facility_id         = Column('施設ID:d', String(20), comment="facility_id")
    area                = Column('エリア', String(100), comment="area")
    store_name          = Column('店舗名', String(100), comment="store_name", nullable=True, default='null')
    overall_rating      = Column('総合評価', String(10), comment="overall_rating", nullable=True, default='null')
    number_of_reviews   = Column('クチコミ数', String(10), comment="number_of_reviews", nullable=True, default='null')
    rank                = Column('順位', String(100), comment="rank", nullable=True, default='null')
    price_range         = Column('価格帯', String(50), comment="price_range", nullable=True, default='null')
    cooking_genres      = Column('料理のジャンル', String(100), comment="cooking_genres", nullable=True, default='null')
    street_address      = Column('住所', Text, comment="street_address", nullable=True, default='null')
    phone_number        = Column('電話番号', String(20), comment="phone_number", nullable=True, default='null')
    business_hours      = Column('営業時間', String(100), comment="business_hours", nullable=True, default='null')
    number_of_photos    = Column('写真', String(20), comment="number_of_photos", nullable=True, default='null')
    award               = Column('受賞', Text, comment="award", nullable=True, default='null')
    food_score          = Column('食事', String(10), comment="food_score", nullable=True, default='null')
    service_score       = Column('サービス', String(10), comment="service_score", nullable=True, default='null')
    price_score         = Column('価格', String(10), comment="price_score", nullable=True, default='null')
    atmosphere_score    = Column('雰囲気', String(10), comment="atmosphere_score", nullable=True, default='null')
    cuisine             = Column('料理', String(100), comment="cuisine", nullable=True, default='null')
    meal_hours          = Column('食事の時間帯', String(100), comment="meal_hours", nullable=True, default='null')
    function            = Column('機能', String(100), comment="function", nullable=True, default='null')
    menu                = Column('食材別のメニュー', String(100), comment="menu", nullable=True, default='null')
    location            = Column('所在地', Text, comment="location", nullable=True, default='null')
    nearest_area        = Column('最寄り', Text, comment="nearest_area", nullable=True, default='null')
    official_site       = Column('公式サイト', String(500), comment="official_site", nullable=True, default='null')
    very_good_score     = Column('とても良い', String(10), comment="very_good_score", nullable=True, default='null')
    good_score          = Column('良い', String(10), comment="good_score", nullable=True, default='null')
    average_score       = Column('普通', String(10), comment="average_score", nullable=True, default='null')
    bad_score           = Column('悪い', String(10), comment="bad_score", nullable=True, default='null')
    very_bad_score      = Column('とても悪い', String(10), comment="very_bad_score", nullable=True, default='null')
    reviews_in_english  = Column('言語英語', Integer, comment="reviews_in_english", nullable=True, default='0')
    reviews_in_japanese = Column('言語日本語', Integer, comment="reviews_in_japanese", nullable=True, default='0')
    details                  = Column('詳細', Text, comment="details", nullable=True, default='null')
    travelers_type_family    = Column('ファミリー', Integer, comment="travelers_type_family", nullable=True, default='0')
    travelers_type_couple    = Column('カップル夫婦', Integer, comment="travelers_type_couple", nullable=True, default='0')
    travelers_type_solo      = Column('一人', Integer, comment="travelers_type_solo", nullable=True, default='0')
    travelers_type__business = Column('出張ビジネス', Integer, comment="travelers_type__business", nullable=True, default='0')
    travelers_type_friend    = Column('旅行者タイプ', Integer, comment="travelers_type_friend", nullable=True, default='0')
    # composite unique constraint.
    UniqueConstraint(url_area, area_id, facility_id, name="unique_key_taf")


class TabelogUserDB(DeclarativeBase):
    __tablename__ = "tabelog_user"

    id                  = Column(Integer, primary_key=True)
    hotel_id            = Column('店舗ID', String(20), comment="hotel_id")
    get_url             = Column('クチコミURL', String(500), comment="get_url")
    kuchikomi_id        = Column('クチコミID', String(20), comment="kuchikomi_id")
    customer_name       = Column('投稿者', String(50), comment="customer_id")
    customer_id         = Column('投稿者ID', String(20), comment="customer_id")
    night_total_rating      = Column('夜評価', String(10), comment="night_total_rating", nullable=True, default='null')
    night_culinary_rating   = Column('(夜)料理・味', String(10), comment="night_culinary_rating", nullable=True, default='null')
    night_service_rating    = Column('(夜)サービス', String(10), comment="night_service_rating", nullable=True, default='null')
    night_atmosphere_rating = Column('(夜)雰囲気', String(10), comment="night_atmosphere_rating", nullable=True, default='null')
    night_cp_rating         = Column('(夜)CP', String(10), comment="night_cp_rating", nullable=True, default='null')
    night_drink_rating      = Column('(夜)酒・ドリンク', String(10), comment="night_drink_rating", nullable=True, default='null')
    night_amount            = Column('(夜)使った金額（1人）', String(50), comment="night_amount", nullable=True, default='null')
    day_total_rating        = Column('昼評価', String(10), comment="ay_total_rating", nullable=True, default='null')
    day_culinary_rating     = Column('(昼)料理・味', String(10), comment="料理・味", nullable=True, default='null')
    day_service_rating      = Column('(昼)サービス', String(10), comment="day_service_rating", nullable=True, default='null')
    day_atmosphere_rating   = Column('(昼)雰囲気', String(10), comment="day_atmosphere_rating", nullable=True, default='null')
    day_cp_rating           = Column('(昼)CP', String(10), comment="day_cp_rating", nullable=True, default='null')
    day_drink_rating        = Column('(昼)酒・ドリンク', String(10), comment="day_drink_rating", nullable=True, default='null')
    day_amount              = Column('(昼)使った金額（1人）', String(50), comment="day_amount", nullable=True, default='null')
    number_of_visit         = Column('来店数', String(20), comment="number_of_visit", nullable=True, default='null')
    # composite unique constraint.
    UniqueConstraint(hotel_id, kuchikomi_id, customer_name, customer_id, name="unique_key_tbu")


class TabelogKuchikomiDB(DeclarativeBase):
    __tablename__ = "tabelog_kuchikomi"

    id                  = Column(Integer, primary_key=True)
    hotel_id            = Column('店舗ID', String(20), comment="hotel_id")
    kuchikomi_id        = Column('クチコミID', String(20), comment="kuchikomi_id")
    get_url             = Column('クチコミURL', String(500), comment="get_urlL")
    customer_name       = Column('投稿者', String(50), comment="customer_id")
    customer_id         = Column('投稿者ID', String(20), comment="customer_id")
    review_date         = Column('訪問日', String(20), comment="review_date")
    night_total_rating      = Column('夜評価', String(10), comment="night_total_rating", nullable=True, default='null')
    night_culinary_rating   = Column('(夜)料理・味', String(10), comment="night_culinary_rating", nullable=True, default='null')
    night_service_rating    = Column('(夜)サービス', String(10), comment="night_service_rating", nullable=True, default='null')
    night_atmosphere_rating = Column('(夜)雰囲気', String(10), comment="night_atmosphere_rating", nullable=True, default='null')
    night_cp_rating         = Column('(夜)CP', String(10), comment="night_cp_rating", nullable=True, default='null')
    night_drink_rating      = Column('(夜)酒・ドリンク', String(10), comment="night_drink_rating", nullable=True, default='null')
    night_amount            = Column('(夜)使った金額（1人）', String(50), comment="night_amount", nullable=True, default='null')
    day_total_rating        = Column('昼評価', String(10), comment="ay_total_rating", nullable=True, default='null')
    day_culinary_rating     = Column('(昼)料理・味', String(10), comment="料理・味", nullable=True, default='null')
    day_service_rating      = Column('(昼)サービス', String(10), comment="day_service_rating", nullable=True, default='null')
    day_atmosphere_rating   = Column('(昼)雰囲気', String(10), comment="day_atmosphere_rating", nullable=True, default='null')
    day_cp_rating           = Column('(昼)CP', String(10), comment="day_cp_rating", nullable=True, default='null')
    day_drink_rating        = Column('(昼)酒・ドリンク', String(10), comment="day_drink_rating", nullable=True, default='null')
    day_amount              = Column('(昼)使った金額（1人）', String(50), comment="day_amount", nullable=True, default='null')
    review_title        = Column('タイトル', Text, comment="review_title")
    review_comment      = Column('クチコミ詳細', Text, comment="review_comment")
    review_liked        = Column('いいね件数', String(50), comment="review_liked", nullable=True, default='null')
    # composite unique constraint.
    UniqueConstraint(hotel_id, kuchikomi_id, customer_name, customer_id, review_date, name="unique_key_tbk")


class TabelogFacilityDB(DeclarativeBase):
    __tablename__ = "tabelog_facility"

    id                  = Column(Integer, primary_key=True)
    get_url             = Column('URL', String(500), comment="get_url")
    url_pre             = Column('url_pre', String(50), comment="URL_PRE")
    url_area1           = Column('url_area1', String(50), comment="URL_ARE1")
    url_area2           = Column('url_area2', String(50), comment="URL_ARE2")
    hotel_id            = Column('店舗ID', String(20), comment="hotel_id")
    area                = Column('エリア', String(100), comment="area", nullable=True, default='null')
    pillow              = Column('枕詞', String(100), comment="pillow", nullable=True, default='null')
    store_name          = Column('店舗名', Text, comment="store_name", nullable=True, default='null')
    overall_rating      = Column('総合評価点数', String(10), comment="overall_rating", nullable=True, default='null')
    night_total_rating  = Column('夜点数', String(10), comment="night_total_rating", nullable=True, default='null')
    day_total_rating    = Column('昼点数', String(10), comment="day_total_rating", nullable=True, default='null')
    number_of_reviews   = Column('クチコミ件数', String(10), comment="number_of_reviews", nullable=True, default='null')
    number_of_photo     = Column('写真', String(10), comment="number_of_photo", nullable=True, default='null')
    review_menu         = Column('口コミに含まれるメニュー', Text, comment="menu", nullable=True, default='null')
    nearest_station     = Column('最寄り駅', Text, comment="nearest_station", nullable=True, default='null')
    genre               = Column('ジャンル', Text, comment="genre", nullable=True, default='null')
    night_budget        = Column('夜予算', String(100), comment="night_budget", nullable=True, default='null')
    day_budget          = Column('昼予算', String(100), comment="night_budget", nullable=True, default='null')
    regular_holiday     = Column('定休日', String(100), comment="day_budget", nullable=True, default='null')
    store_name_detail        = Column('店舗名(情報)', Text, comment="store_name", nullable=True, default='null')
    awards_selection_history = Column('受賞・選出歴', Text, comment="awards_selection_history", nullable=True, default='null')
    genre_detail             = Column('ジャンル(情報)', Text, comment="genre", nullable=True, default='null')
    reservation_inquiry      = Column('予約・お問い合わせ', String(20), comment="reservation_inquiry", nullable=True, default='null')
    reservation_acceptability= Column('予約可否', String(20), comment="reservation_acceptability", nullable=True, default='null')
    street_address           = Column('住所', Text, comment="street_address", nullable=True, default='null')
    transportation           = Column('交通手段', Text, comment="transportation", nullable=True, default='null')
    business_hours           = Column('営業時間', Text, comment="business_hours", nullable=True, default='null')
    regular_holiday_details  = Column('定休日(情報)', String(100), comment="business_hours", nullable=True, default='null')
    night_budget_detail      = Column('夜予算(情報)', String(100), comment="business_hours", nullable=True, default='null')
    day_budget_detail        = Column('昼予算(情報)', String(100), comment="business_hours", nullable=True, default='null')
    night_budget_in_reviews  = Column('夜予算(口コミ集計)', String(100), comment="business_hours", nullable=True, default='null')
    day_budget_in_reviews    = Column('昼予算(口コミ集計)', String(100), comment="business_hours", nullable=True, default='null')
    method_of_payment        = Column('支払い方法', String(20), comment="method_of_payment", nullable=True, default='null')
    service_charge           = Column('サービス料・チャージ', String(100), comment="service_charge", nullable=True, default='null')
    number_of_seats         = Column('席数', String(100), comment="number_of_seats", nullable=True, default='null')
    private_room            = Column('個室', String(100), comment="private_room", nullable=True, default='null')
    reserved                = Column('貸切', String(100), comment="reserved", nullable=True, default='null')
    smoking                 = Column('禁煙・喫煙', String(100), comment="smoking", nullable=True, default='null')
    parking                 = Column('駐車場', String(100), comment="parking", nullable=True, default='null')
    space_facilities        = Column('空間・設備', Text, comment="space_facilities", nullable=True, default='null')
    mobile                  = Column('携帯電話', String(100), comment="mobile", nullable=True, default='null')
    course                  = Column('コース', String(100), comment="course", nullable=True, default='null')
    drink                   = Column('ドリンク', String(100), comment="drink", nullable=True, default='null')
    cooking                 = Column('料理', String(100), comment="cooking", nullable=True, default='null')
    use_scene               = Column('利用シーン', String(100), comment="use_scene", nullable=True, default='null')
    location                = Column('ロケーション', String(100), comment="location", nullable=True, default='null')
    service                 = Column('サービス', String(100), comment="service", nullable=True, default='null')
    children                = Column('お子様連れ', String(100), comment="children", nullable=True, default='null')
    home_page               = Column('ホームページ', String(500), comment="home_page", nullable=True, default='null')
    official_account        = Column('公式アカウント', String(500), comment="official_account", nullable=True, default='null')
    open_date               = Column('オープン日', String(20), comment="open_date", nullable=True, default='null')
    phone_number            = Column('電話番号', String(20), comment="phone_number", nullable=True, default='null')
    remarks                 = Column('備考', Text, comment="remarks", nullable=True, default='null')
    original_contributor    = Column('初投稿者', String(50), comment="original_contributor", nullable=True, default='null')
    # composite unique constraint.
    UniqueConstraint(url_pre, url_area1, url_area2, hotel_id, name="unique_key_tbf")


