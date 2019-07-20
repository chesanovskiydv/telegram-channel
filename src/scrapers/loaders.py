# -*- coding: utf-8 -*-

# See documentation in:
# https://doc.scrapy.org/en/latest/topics/loaders.html
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class MessageLoader(ItemLoader):
    default_output_processor = TakeFirst()
