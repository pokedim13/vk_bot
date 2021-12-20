import asyncpraw
import asyncio
import config
import sqlite3
import os
import requests
import wikipedia
import json
from config import settings
from vkbottle.bot import Bot, Message
import datetime



filepath = os.path.abspath('db.db')
print(str(filepath))
assert os.path.exists(filepath)
db = sqlite3.connect(filepath)
sql = db.cursor()
wikipedia.set_lang("RU")

# Использование Reddita
reddit = asyncpraw.Reddit(client_id=config.settings['CLIENT_ID'],
                     client_secret=config.settings['SECRET_CODE'],
                     user_agent='random_raddit_bot/0.0.1')

SUBREDDIT_NAME = 'Animemes'
POST_LIMIT = 1





# Сам код
bot = Bot(token=settings["TOKEN"])

@bot.on.private_message(text="инфа")
async def message_handler(message=Message):
    user = await bot.api.users.get(message.from_id)
    await message.answer(f"Это @id{user[0].id} ({user[0].first_name})")

# @bot.message_handler(bot.command_filter('мем'))
# async def send_mem(event: SimpleBotEvent) -> str:
#     user_id = event.object.object.message.peer_id
    
#     memes_submissions = await reddit.subreddit(SUBREDDIT_NAME)
#     memes_submissions = memes_submissions.new(limit=POST_LIMIT)
#     item = await memes_submissions.__anext__()

#     photo = await PhotoUploader(bot.api_context).get_attachment_from_link(peer_id=user_id, link=item.url)
#     await event.answer(message=item.title, attachment=photo)


bot.run_forever()