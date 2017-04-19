# -*- coding: utf-8 -*-
import scrapy


class QiyeoneSpider(scrapy.Spider):
    name = "QiyeOne"
    allowed_domains = ["qiye.qianzhan.com"]
    start_urls = ['http://qiye.qianzhan.com/']

    def parse(self, response):
        pass
