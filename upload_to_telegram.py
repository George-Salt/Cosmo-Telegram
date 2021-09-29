from dotenv import load_dotenv
from os import listdir
from time import sleep
import os
import telegram
import random


def bot_settings(bot_token, chat_id):
    bot = telegram.Bot(token=bot_token)
    bot.send_document(chat_id=chat_id, document=open(random_path(["nasa", "epic", "spacex"]), 'rb'))
    return "Отправлено"


def random_path(dirs):
    random_directory = random.choice(dirs)
    random_picture = random.choice(listdir(random_directory))
    resalt_path = f"{random_directory}/{random_picture}"
    return resalt_path
