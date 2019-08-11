# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import re

from scrapy import Item, Field
from scrapy.loader.processors import MapCompose

from w3lib.html import remove_tags
from urllib import parse

from bs4 import BeautifulSoup


def prepare_html(text, loader_context):
    soup = BeautifulSoup(text, 'html.parser')
    for a in soup.findAll('a'):
        a['href'] = loader_context.get('response').urljoin(a['href'])

    return remove_tags(str(soup), keep=('a',))


def extract_img_url(image, loader_context):
    soup = BeautifulSoup(image, 'html.parser')
    img = soup.find('img')

    if img:
        src = img.get('src')
        original_width = img.get('data-file-width')
        if original_width:
            src = re.sub(r'/(\d+)px-', '/{w}px-'.format(w=original_width), src)
        return loader_context.get('response').urljoin(src)
    return image


class MessageItem(Item):
    text = Field(
        input_processor=MapCompose(prepare_html, parse.unquote)
    )
    image = Field(
        input_processor=MapCompose(extract_img_url, parse.unquote)
    )
    url = Field(
        input_processor=MapCompose(parse.unquote)
    )
