from os import listdir
import telegram
import random


def send_picture(bot_token, chat_id, dirs):
    bot = telegram.Bot(token=bot_token)
    with open(fetch_random_path(dirs), "rb") as file:
        bot.send_document(chat_id=chat_id, document=file)
    return "Отправлено"


def fetch_random_path(dirs):
    random_directory = random.choice(dirs)
    random_picture = random.choice(listdir(random_directory))
    resalt_path = f"{random_directory}/{random_picture}"
    return resalt_path
