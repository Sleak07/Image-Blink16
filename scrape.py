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
        image = self.soup.find_all("img")
        