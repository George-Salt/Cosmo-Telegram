from urllib.parse import urlparse
import requests
import os


def download_image(directory, name, image_url, payload={}):
    filepath = f"{directory}/{name}{get_extension(image_url)}"

    response = requests.get(image_url, params=payload)
    response.raise_for_status()

    with open(filepath, "wb") as file:
        file.write(response.content)


def get_extension(image_url):
    parsed_url = urlparse(image_url)
    extension = os.path.splitext(parsed_url.path)[1]
    return extension
