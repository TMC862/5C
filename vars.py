#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29538829"))
API_HASH = environ.get("API_HASH", "0098baaaa11b512a0a8b8eaf33a4d91a")
BOT_TOKEN = environ.get("BOT_TOKEN", "8043004739:AAFHi875pTJTaJjvIRvoqYWSYn-JivAZTgM")
OWNER = int(environ.get("OWNER", "1118716436"))
CHANNEL_ID = int(environ.get("CHANNEL_ID", "-1002850611486"))
CREDIT = "𝄟⃝‌🐬Golden Eagle𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '1118716436').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
