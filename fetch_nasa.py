import requests
import download_with_ext


def download_nasa_epic(token, epic_dir):
    epic_url = "https://api.nasa.gov/EPIC/api/natural/images?api_key={}".format(token)

    response = requests.get(epic_url)
    images_description = response.json()

    for image_num, image in enumerate(images_description[:10]):
        epic_image_name = image["image"]
        epic_image_date = image["date"][:10].replace("-", "/")
        image_url = "https://api.nasa.gov/EPIC/archive/natural/{linkdate}/png/{name}.png?api_key={token}".format(linkdate = epic_image_date, name=epic_image_name, token=token)
        download_with_ext.download_image(epic_dir, f"{epic_dir}{image_num}", image_url)

    return "Загружено - EPIC"


def download_nasa_apod(token, apod_dir):
    apod_url = "https://api.nasa.gov/planetary/apod?api_key={}".format(token)
    params = {
        "count": 30
    }
    response = requests.get(apod_url, params=params)
    apod_images = response.json()

    for image_num, image_url in enumerate(apod_images):
        image_url = apod_images[image_num]["url"]
        download_with_ext.download_image(apod_dir, f"{apod_dir}{image_num}", image_url)

    return "Загружено - APOD"
