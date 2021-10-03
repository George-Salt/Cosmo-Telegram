from dotenv import load_dotenv
from os import listdir
from time import sleep
import os
import telegram
import random


def bot_settings(bot_token, chat_id, dirs):
    bot = telegram.Bot(token=bot_token)
    with open(random_path(dirs), "rb") as file:
        bot.send_document(chat_id=chat_id, document=file)
    return "Отправлено"


def random_path(dirs):
    random_directory = random.choice(dirs)
    random_picture = random.choice(listdir(random_directory))
    resalt_path = f"{random_directory}/{random_picture}"
    return resalt_path
