from dotenv import load_dotenv
from os import listdir
from time import sleep
import os
import telegram
import random


def bot_settings(bot_token, chat_id):
    bot = telegram.Bot(token=bot_token)
    bot.send_document(chat_id=chat_id, document=open(random_path(), 'rb'))
    return "Отправлено"


def random_path():
    random_directory_num = random.randint(1, 3)
    if random_directory_num == 1:
        random_directory = "nasa"
        random_picture = random.sample(listdir("nasa"), 1)
    if random_directory_num == 2:
        random_directory = "epic"
        random_picture = random.sample(listdir("epic"), 1)
    if random_directory_num == 3:
        random_directory = "spacex"
        random_picture = random.sample(listdir("spacex"), 1)
    resalt_path = f"{random_directory}/{random_picture[0]}"
    return resalt_path


if __name__ == "__main__":
    load_dotenv()
    chat_id = os.getenv("CHAT_ID")
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    seconds_in_one_day = 86400
    while True:
        print(bot_settings(bot_token))
        sleep(seconds_in_one_day)
