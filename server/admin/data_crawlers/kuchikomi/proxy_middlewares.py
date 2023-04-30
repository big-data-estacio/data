#!/usr/bin/env python
# -*- config: utf-8 -*-

import base64
import random


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy_ip_port = self.getProxy()
        proxy_user_pass = 'xxx:xxx'
        # Set the location of the proxy
        request.meta['proxy'] = "http://%s" % proxy_ip_port

        basic_auth = 'Basic ' + base64.b64encode(proxy_user_pass.encode()).decode()
        request.headers['Proxy-Authorization'] = basic_auth

    @staticmethod
    def getProxy():
        proxy = ["160.16.238.204:8080"]

        select_proxy = random.randint(0, 9)
        return proxy[select_proxy]
