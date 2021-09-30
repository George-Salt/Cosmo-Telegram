from dotenv import load_dotenv
import fetch_nasa
import fetch_spacex
import upload_to_telegram
import os


if __name__ == '__main__':
    dirs_for_images = ("spacex", "apod", "epic")
    for image_dir in dirs_for_images:
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

    load_dotenv()
    chat_id = os.getenv("TG_CHAT_ID")
    nasa_token = os.getenv("NASA_TOKEN")
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    seconds_in_one_day = 86400
    while True:
        fetch_nasa.download_nasa_epic(nasa_token)
        fetch_nasa.download_nasa_apod(nasa_token)
        fetch_spacex.fetch_last_launch()
        upload_to_telegram.bot_settings(bot_token, chat_id)
        upload_to_telegram.sleep(seconds_in_one_day)
