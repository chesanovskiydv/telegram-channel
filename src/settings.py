# -*- coding: utf-8 -*-
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

BOT_ACCESS_TOKEN = os.getenv("BOT_ACCESS_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
