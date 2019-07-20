# -*- coding: utf-8 -*-
from scrapy import Spider, Selector
from scrapy.http import TextResponse

from scrapers.items import MessageItem
from scrapers.loaders import MessageLoader


class WikipediaSpider(Spider):
    name = 'wikipedia'
    allowed_domains = ['wikipedia.org']
    start_urls = ['http://ru.wikipedia.org/']

    def parse(self, response: TextResponse):
        boxes_selectors = response.xpath("//*[has-class($cls)]", cls='main-box')

        for box_selector in boxes_selectors.css("#main-dyk, #main-cur"):
            for message in self.parse_box(response, box_selector):
                yield message

    def parse_box(self, response, box_selector: Selector):
        if box_selector.xpath('./ul'):
            yield from self.parse_list_box(response, box_selector)
        elif box_selector.xpath('./p'):
            yield from self.parse_article_box(response, box_selector)

    def parse_article_box(self, response, box_selector: Selector):
        raise NotImplementedError('{}.parse_article_box callback is not defined'.format(self.__class__.__name__))

    def parse_list_box(self, response, box_selector: Selector) -> MessageItem:
        message_loader = MessageLoader(item=MessageItem(), selector=box_selector, response=response)
        message_loader.add_xpath('text', './ul/li')
        # message_loader.add_xpath('image', './/a/img')
        message_loader.add_value('url', response.url)
        yield message_loader.load_item()
