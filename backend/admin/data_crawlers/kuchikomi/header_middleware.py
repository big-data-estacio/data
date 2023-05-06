#!/usr/bin/env python
# -*- config: utf-8 -*-

"""
DefaultHeaders downloader middleware

See documentation in docs/topics/downloader-middleware.rst
"""


class HeaderMiddleware(object):

    def __init__(self, headers):
        self._headers = headers

    @classmethod
    def from_crawler(cls, crawler):
        headers = {
            "Accept"                   : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding"          : "gzip, deflate, sdch",
            "Accept-Language"          : "ja;q=0.9, en;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type"             : 'text/html; charset=UTF-8',
            "User-Agent"               : "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
            #"User-Agent"              : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        return cls(headers.items())

    def process_request(self, request, spider):
        for k, v in self._headers:
            request.headers.setdefault(k, v)
