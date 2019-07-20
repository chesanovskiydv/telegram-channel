# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import MapCompose

from w3lib.html import remove_tags

from bs4 import BeautifulSoup


def prepare_html(text, loader_context):
    soup = BeautifulSoup(text)
    for a in soup.findAll('a'):
        a['href'] = loader_context.get('response').urljoin(a['href'])

    return remove_tags(str(soup), keep=('a',))


class MessageItem(Item):
    text = Field(
        input_processor=MapCompose(prepare_html)
    )
    image = Field()
    url = Field()
