# for sending requests to the server
import requests

# for parsing out the html response
from bs4 import BeautifulSoup

# for os related stuff
import os

# TODO: make a class for parsing , saving and creating new folder


class Image:
    def __init__(self, url: str, folder: str):
        self.url = url
        self.folder = folder

        try:
            if not os.path.exists(self.folder):
                os.mkdir(self.folder)

        except:
            if os.path.exists(self.folder):
                print("It already exists")

    def parsing_content(self):
        response = requests.get(self.url)
        try:
            response.raise_for_status()

        except Exception as e:
            print(f"There was an error:{e}")
        self.soup = BeautifulSoup(response.text, "lxml")
        return self.soup

    def saving_images(self):
        images = self.soup.find_all("img")

        for img_tags in images:
            img_url = img_tags.get("src")
            img_name = img_tags.get("alt","image")
            if img_url and img_name:
                img_data = requests.get(img_url).content
                with open(f"{self.folder}/{img_name}.jpg", "wb") as handler:
                    handler.write(img_data)
                print(f"{img_name} saved successfully in {self.folder}")

if __name__ == "__main__":
    url ="https://unsplash.com/s/photos/yellow-flowers"
    folder = "Image_folder"
    image = Image(url, folder)
    image.parsing_content()
    image.saving_images()