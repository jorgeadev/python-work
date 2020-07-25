import requests
from io import StringIO
from bs4 import BeautifulSoup


def url_to_image(url):
    """
    Fetch an image from url and convert it into a Pillow Image object
    """
    r = requests.get(url)
    image = BeautifulSoup(r.content)
    return image


url = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTPyHR8YZ8RKM4RbJsvyvqgNfcEnSsTetlSpA&usqp=CAU"
print(url_to_image(url))