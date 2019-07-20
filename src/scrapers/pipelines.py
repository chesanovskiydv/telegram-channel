# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Item

from database import session
from scrapers.items import MessageItem
from database.models import Message


class MessagePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, Item):
            self.save_item(item, spider)
        return item

    @staticmethod
    def save_item(item: Item, spider):
        if isinstance(item, MessageItem):
            with session.begin():
                message = Message(text=item.get('text'), image=item.get('image'), url=item.get('url'))
                session.add(message)
