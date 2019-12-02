# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['sou.zhaopin.com']
    start_urls = ['http://sou.zhaopin.com/']

    def parse(self, response):
        pass
