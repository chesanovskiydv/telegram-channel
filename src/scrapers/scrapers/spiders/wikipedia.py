# -*- coding: utf-8 -*-
import scrapy


class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    allowed_domains = ['wikipedia.org']
    start_urls = ['http://ru.wikipedia.org/']

    def parse(self, response):
        pass
