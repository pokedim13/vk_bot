import time
import eventlet
import requests
import logging
import telebot
from time import sleep

 # Каждый раз получаем по 10 последних записей со стены
URL_VK = 'https://api.vk.com/method/wall.get?domain=team&count=10&filter=owner&access_token=Ваш_токен_VK&v=5.68'
FILENAME_VK = 'last_known_id.txt'
BASE_POST_URL = 'https://vk.com/wall-22822305_'

BOT_TOKEN = 'токен бота, постящего в канал'
CHANNEL_NAME = '@канал'

bot = telebot.TeleBot(BOT_TOKEN)


def get_data():
    timeout = eventlet.Timeout(10)
    try:
        feed = requests.get(URL_VK)
        return feed.json()
    except eventlet.timeout.Timeout:
        logging.warning('Got Timeout while retrieving VK JSON data. Cancelling...')
        return None
    finally:
        timeout.cancel()