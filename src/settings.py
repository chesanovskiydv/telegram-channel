import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

BOT_ACCESS_TOKEN = os.getenv("BOT_ACCESS_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
