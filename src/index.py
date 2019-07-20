# -*- coding: utf-8 -*-
import settings

from database import session
from database.models import Message

from channel import Channel

message = session.query(Message).filter(Message.is_sent.is_(False)).first()
if message is None:
    raise ValueError("Message not found")

channel = Channel(settings.BOT_ACCESS_TOKEN, settings.CHAT_ID)

if message.image is not None:
    channel.send_photo(photo=message.image, caption=message.text)
else:
    channel.send_message(text=message.text)

message.is_sent = True
session.flush()
