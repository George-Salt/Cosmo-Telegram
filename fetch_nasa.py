from dotenv import load_dotenv
from os import listdir
from urllib.parse import urlparse
import requests
import os


def create_dirs_for_images():
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
    load_dotenv()
    nasa_token = os.getenv("NASA_API")
    create_dirs_for_images()
    print(upload_nasa_epic(nasa_token))
    print(upload_nasa_apod(nasa_token))
