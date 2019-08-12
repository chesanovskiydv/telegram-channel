# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Item
from scrapers.items import MessageItem

from sqlalchemy.orm import aliased

from database import session
from database.models import Message

from w3lib.html import remove_tags


class MessagePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, Item):
            self.save_item(item, spider)
        return item

    @staticmethod
    def save_item(item: Item, spider):
        if isinstance(item, MessageItem):

            def message_is_unique(message_model: Message, limit=20) -> bool:
                subquery = session.query(Message) \
                    .order_by(Message.created_at.desc(), Message.id.desc()) \
                    .limit(limit) \
                    .subquery()

                alias = aliased(Message, subquery)

                return not session.query(
                    session.query(alias).filter(
                        alias.text == message_model.text,
                        alias.image == message_model.image
                    ).exists()
                ).scalar()

            def message_fit_the_length(message_model: Message) -> bool:
                if message_model.image:
                    return len(remove_tags(message_model.text)) <= 1024
                return len(remove_tags(message_model.text)) <= 4096

            message = Message(text=item.get('text'), image=item.get('image'), url=item.get('url'))

            if message_is_unique(message) and message_fit_the_length(message):
                with session.begin():
                    session.add(message)
