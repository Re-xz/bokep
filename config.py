# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6325594724:AAH-2SZRoxVdpbirNhXlyG5-uwlE7HU43CQ")

APP_ID = int(os.environ.get("APP_ID", "29486311"))

API_HASH = os.environ.get("API_HASH", "ffdc688dc4eee8d2585cb24155188432")

CHANNEL_DB = int(os.environ.get("CHANNEL_DB", "-1001950756152"))
OWNER = os.environ.get("OWNER", "skandal")
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "True"))

HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database type
DATABASE_TYPE = os.getenv("DATABASE_TYPE", "sql")

# Database SQL
DB_URI = os.getenv("DB_URL", "postgres://tlmyyost:P2inlcCa4QcIWDD0QvlleYEkGsjBAX2I@flora.db.elephantsql.com/tlmyyost")

# Database MongoDB
MONGO_NAME = os.getenv("MONGO_NAME", "")
MONGO_URL = os.getenv("MONGO_URL", "")


FORCE_SUB_1 = {-1002037994205}
FORCE_SUB_2 = {-1002018123667}
FSUB_TOTAL = 2
while True:
    key = f"FORCE_SUB_{FSUB_TOTAL}"
    value = os.getenv(key)
    if value is None:
        break
    FORCE_SUB_[FSUB_TOTAL] = int(value)
    FSUB_TOTAL += 2

BUTTON_ROW = int(os.getenv("BUTTON_ROW", 3))

BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1707380693").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)


CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)


DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

ADMINS.extend((844432220, 1250450587, 1750080384, 182990552, 903187853, 5050907047))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
