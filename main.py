import os
from time import sleep

from dotenv import load_dotenv

import fetch_nasa
import fetch_spacex
import upload_to_telegram


if __name__ == "__main__":
    spacex_dir = "spacex"
    apod_dir = "apod"
    epic_dir = "epic"
    images_dirs = (spacex_dir, apod_dir, epic_dir)
    for image_dir in images_dirs:
        os.makedirs(image_dir, exist_ok=True)

    load_dotenv()
    chat_id = os.getenv("TG_CHAT_ID")
    nasa_token = os.getenv("NASA_TOKEN")
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    seconds_in_one_day = 86400
    while True:
        fetch_nasa.download_nasa_epic(nasa_token, epic_dir)
        fetch_nasa.download_nasa_apod(nasa_token, apod_dir)
        fetch_spacex.fetch_last_launch(spacex_dir)
        upload_to_telegram.send_picture(bot_token, chat_id, images_dirs)
        sleep(seconds_in_one_day)
