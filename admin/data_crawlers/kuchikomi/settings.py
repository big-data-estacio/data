# -*- coding: utf-8 -*-

# Scrapy settings for kuchikomi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys
import configparser

# Config file path
path_dir = os.path.dirname(__file__)
configFilePath = '/home/crawler/conf/docker_config.cfg'
# configFilePath = os.path.join(path_dir, '../../conf/local_config.cfg')
config = configparser.RawConfigParser()

try:
    with open(configFilePath) as f:
        config.readfp(f)
except IOError:
    print('Can not open file ', configFilePath)
    sys.exit()


BOT_NAME = 'kuchikomi'

SPIDER_MODULES = ['kuchikomi.spiders']
NEWSPIDER_MODULE = 'kuchikomi.spiders'

# Redis host setting
REDIS_HOST = config.get("redis", "host")
REDIS_PORT = config.get("redis", "port")

# sqlAlchemy mysql db connection string
CONNECTION_STRING = "{driver_name}+pymysql://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
    driver_name="mysql",
    user=config.get("mysql", "user"),
    passwd=config.get("mysql", "password"),
    host=config.get("mysql", "host"),
    port=config.get("mysql", "port"),
    db_name=config.get("mysql", "db"),
)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'kuchikomi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'kuchikomi.middlewares.KuchikomiSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'kuchikomi.middlewares.KuchikomiDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

FEED_EXPORT_ENCODING = 'utf-8'

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'kuchikomi.pipelines.KuchikomiPipeline': 300,
    # 'kuchikomi.tsvExporterPipelines.TsvExporterPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
