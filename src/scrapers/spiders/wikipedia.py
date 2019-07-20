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
            for message in self.parse_box(box_selector):
                message['url'] = response.url
                yield message

    def parse_box(self, box_selector: Selector):
        if box_selector.xpath('./ul'):
            yield from self.parse_list_box(box_selector)
        elif box_selector.xpath('./p'):
            yield from self.parse_article_box(box_selector)

    def parse_article_box(self, box_selector: Selector):
        message_loader = MessageLoader(item=MessageItem, selector=box_selector)
        # @todo: implement
        # message_loader.add_xpath('text', '//div[@class="product_name"]')
        # message_loader.add_xpath('image', '//div[@class="product_name"]')
        message_loader.add_value('text', 'text_test')  # @todo: tmp
        message_loader.add_value('image', 'image_test')  # @todo: tmp
        # @todo: implement
        yield message_loader.load_item()

    def parse_list_box(self, box_selector: Selector) -> MessageItem:
        message_loader = MessageLoader(item=MessageItem(), selector=box_selector)
        # @todo: implement
        # message_loader.add_value('text', 'text_test')  # @todo: tmp
        # message_loader.add_value('image', 'image_test')  # @todo: tmp
        message_loader.add_xpath('text', './ul/li')
        message_loader.add_xpath('image', ".//a/img")
        # @todo: implement
        yield message_loader.load_item()
