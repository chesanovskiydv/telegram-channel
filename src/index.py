# -*- coding: utf-8 -*-
import settings

from datetime import datetime
from database import session
from database.models import Message

from channel import Channel

while True:
    message = session.query(Message).filter(Message.sent_at.is_(None), Message.is_success.is_(None)).first()
    if message is None:
        raise ValueError("Message not found")

    try:
        channel = Channel(settings.BOT_ACCESS_TOKEN, settings.CHAT_ID)

        if message.image is not None:
            channel.send_photo(photo=message.image, caption=message.text)
        else:
            channel.send_message(text=message.text)
    except:
        message.is_success = False
    else:
        message.sent_at = datetime.now()
        message.is_success = True
    session.flush()

    if message.is_success:
        break
