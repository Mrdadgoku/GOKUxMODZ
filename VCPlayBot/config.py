import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LaylaBots")
BG_IMAGE = getenv("BG_IMAGE", "https://graph.org/file/eabfb1087a5508dbbb218.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "˹ ᴬᴺᴺᴵᴱ ✘ ᴍᴜsɪᴄ˼ ♪™➜")
OWNER_NAME = getenv("OWNER_NAME", "❛𝗚𝗢𝗞𝗨🇽𝐄𝐝𝐢𝐭𝐢𝐨𝐧™श्रीराम ❜ ᯤ̸")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "GOKUxENGINE")
PROJECT_NAME = getenv("PROJECT_NAME", "GOKUxEDITION")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Mrdadgoku/GOKUxMODZ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7128863379").split()))
