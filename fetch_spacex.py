from os import listdir
from urllib.parse import urlparse
import requests
import os
import random


def create_dir_for_images():
    if not os.path.exists("spacex"):
        os.makedirs("spacex")


def fetch_last_launch():
    spaceX_url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(spaceX_url)
    latest_launches_images = response.json()["links"]["flickr"]["original"]

    for image_num, image_url in enumerate(latest_launches_images):
        upload_images("spacex", f"spacex{image_num}", image_url)

    return "Загружено"


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


if __name__ == "__main__":
    create_dir_for_images()
    print(fetch_last_launch())
