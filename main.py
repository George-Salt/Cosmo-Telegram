from dotenv import load_dotenv
from os import listdir
from time import sleep
from urllib.parse import urlparse
import requests
import os
import telegram
import random


def create_dirs_for_images():
    if not os.path.exists("spacex"):
        os.makedirs("spacex")
    if not os.path.exists("nasa"):
        os.makedirs("nasa")
    if not os.path.exists("epic"):
        os.makedirs("epic")


def upload_nasa_epic(token):
    epic_url = "https://api.nasa.gov/EPIC/api/natural/images?api_key={}".format(token)

    response = requests.get(epic_url)
    images_description = response.json()

    for image_num, image in enumerate(images_description[:10]):
        epic_image_name = image["image"]
        epic_image_date = image["date"][:10].replace("-", "/")
        image_url = "https://api.nasa.gov/EPIC/archive/natural/{linkdate}/png/{name}.png?api_key={token}".format(linkdate = epic_image_date, name=epic_image_name, token=token)
        upload_images("epic", f"epic{image_num}", image_url)

    return "Загружено - EPIC"


def upload_nasa_apod(token):
    apod_url = "https://api.nasa.gov/planetary/apod?api_key={}".format(token)
    params = {
        "count": 30
    }
    response = requests.get(apod_url, params=params)
    apod_images = response.json()

    for image_num, image_url in enumerate(apod_images):
        image_url = apod_images[image_num]["url"]
        upload_images("nasa", f"apod{image_num}", image_url)

    return "Загружено - APOD"


def fetch_spacex_last_launch():
    spaceX_url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(spaceX_url)
    latest_launches_images = response.json()["links"]["flickr"]["original"]

    for image_num, image_url in enumerate(latest_launches_images):
        upload_images("spacex", f"spacex{image_num}", image_url)

    return "Загружено - SpaceX"


def upload_images(directory, name, image_url):
    filepath = "{directory}/{name}{ext}".format(directory=directory, name=name, ext=get_extension(image_url))

    response = requests.get(image_url)
    response.raise_for_status()

    with open(filepath, "wb") as file:
        file.write(response.content)


def get_extension(image_url):
    parsed_url = urlparse(image_url)
    extension = os.path.splitext(parsed_url.path)[1]
    return extension


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
    nasa_token = os.getenv("NASA_API")
    seconds_in_one_day = 86400
    create_dirs_for_images()
    while True:
        print(upload_nasa_epic(nasa_token))
        print(upload_nasa_apod(nasa_token))
        print(fetch_spacex_last_launch())
        print(bot_settings(bot_token))
        sleep(seconds_in_one_day)
