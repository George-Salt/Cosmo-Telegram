from dotenv import load_dotenv
import fetch_nasa
import fetch_spacex
import upload_to_telegram
import os


def create_dirs_for_images():
    if not os.path.exists("spacex"):
        os.makedirs("spacex")
    if not os.path.exists("nasa"):
        os.makedirs("nasa")
    if not os.path.exists("epic"):
        os.makedirs("epic")


if __name__ == '__main__':
    load_dotenv()
    chat_id = os.getenv("CHAT_ID")
    nasa_token = os.getenv("NASA_API")
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    seconds_in_one_day = 86400
    create_dirs_for_images()
    while True:
        print(fetch_nasa.upload_nasa_epic(nasa_token))
        print(fetch_nasa.upload_nasa_apod(nasa_token))
        print(fetch_spacex.fetch_last_launch())
        print(upload_to_telegram.bot_settings(bot_token, chat_id))
        upload_to_telegram.sleep(seconds_in_one_day)
