# -*- coding: utf-8 -*-
import settings
from channel import Channel

channel = Channel(settings.BOT_ACCESS_TOKEN, settings.CHAT_ID)
# channel.send_message('test from python')
# channel.send_message('<img alt="Ракета-носитель Сатурн-5 с космическим кораблём Аполлон-11 в момент отрыва от стартового стола" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Apollo_11_Launch2.jpg/400px-Apollo_11_Launch2.jpg" decoding="async" elementtiming="thumbnail" width="400" height="500" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Apollo_11_Launch2.jpg/600px-Apollo_11_Launch2.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Apollo_11_Launch2.jpg/800px-Apollo_11_Launch2.jpg 2x" data-file-width="2400" data-file-height="3000">')
# channel.send_message('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
#                     disable_web_page_preview=None
#                      )
# channel.send_message('Some <b>test</b> <a href="https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0">message</a>')

channel.send_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Apollo_11_Launch2.jpg/400px-Apollo_11_Launch2.jpg',
                   caption='test')
