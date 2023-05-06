from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes
from selenium import webdriver
from scrapy import signals
from selenium.webdriver.chrome.options import Options


class SeleniumMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signals.spider_opened)
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_request(self, request, spider):
        request.meta['driver'] = self.driver  # to access driver from response
        self.driver.get(request.url)
        body = to_bytes(self.driver.page_source)  # body must be of type bytes
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

    def spider_opened(self, spider):
        self.driver = webdriver.Firefox()
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # # chrome_options.add_argument('--disable-gpu')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def spider_closed(self, spider):
        self.driver.close()