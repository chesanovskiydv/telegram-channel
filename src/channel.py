import telegram


def default_args(func):
    def decorator(self, *args, **kwargs):
        kwargs.setdefault('chat_id', self.chat_id)
        kwargs.setdefault('parse_mode', telegram.ParseMode.HTML)

        return func(self, *args, **kwargs)

    return decorator


class Channel:
    def __init__(self, bot_access_token: str, chat_id: str or int):
        self.bot = telegram.Bot(token=bot_access_token)
        self.chat_id = chat_id

    @default_args
    def send_message(self, text, **kwargs):
        self.bot.send_message(text=text, **kwargs)

    @default_args
    def send_photo(self, photo: str, **kwargs):
        self.bot.send_photo(photo=photo, **kwargs)
