import requests
import download_with_ext


def fetch_last_launch(spacex_dir):
    spacex_url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(spacex_url)
    latest_launch_images = response.json()["links"]["flickr"]["original"]

    for image_num, image_url in enumerate(latest_launch_images):
        download_with_ext.download_image(spacex_dir, f"{spacex_dir}{image_num}", image_url)
