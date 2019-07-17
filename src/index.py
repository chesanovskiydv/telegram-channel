import settings
from channel import Channel

channel = Channel(settings.BOT_ACCESS_TOKEN, settings.CHAT_ID)
channel.send_message('test from python')

