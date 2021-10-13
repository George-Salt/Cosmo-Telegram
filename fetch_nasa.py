import requests

import download_with_ext


def download_nasa_epic(token, epic_dir):
    epic_url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": token}

    response = requests.get(epic_url, params=payload)
    response.raise_for_status()
    image_descriptions = response.json()

    for image_num, image in enumerate(image_descriptions[:10]):
        epic_image_name = image["image"]
        epic_image_date = image["date"][:10].replace("-", "/")
        image_url = "https://api.nasa.gov/EPIC/"\
                    f"archive/natural/{epic_image_date}"\
                    f"/png/{epic_image_name}.png"
        download_with_ext.download_image(
            epic_dir,
            f"{epic_dir}{image_num}",
            image_url,
            payload
        )


def download_nasa_apod(token, apod_dir):
    apod_url = f"https://api.nasa.gov/planetary/apod"
    payload = {"count": 30, "api_key": token}
    response = requests.get(apod_url, params=payload)
    response.raise_for_status()
    apod_images = response.json()

    for image_num, image_url in enumerate(apod_images):
        image_url = apod_images[image_num]["url"]
        download_with_ext.download_image(
            apod_dir,
            f"{apod_dir}{image_num}",
            image_url
        )
