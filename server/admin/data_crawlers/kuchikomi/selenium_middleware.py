from shutil import which

from pyvirtualdisplay import Display
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

HEADLESS = True


class SeleniumMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signals.spider_opened)
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_request(self, request, spider):
        self.driver.get(request.url)
        request.meta['driver'] = self.driver
        body = str.encode(self.driver.page_source)
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

    def spider_opened(self, spider):
        if HEADLESS:
            self.display = Display(visible=0, size=(1280, 1024))
            self.display.start()
        binary = FirefoxBinary(which('firefox'))
        options = Options()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(firefox_binary=binary, firefox_options=options)

    def spider_closed(self, spider):
        self.driver.close()
        if HEADLESS:
            self.display.stop()