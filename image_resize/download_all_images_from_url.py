import requests
import subprocess
from bs4 import BeautifulSoup
from urllib3 import PoolManager
from urllib.request import urlretrieve

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTPyHR8YZ8RKM4RbJsvyvqgNfcEnSsTetlSpA&usqp=CAU"


def get_iamge_from_url(url):
    return urlretrieve(url, "local-filename_2.jpg")

print(get_iamge_from_url(url))


"""

# use this image scraper from the location that
# you want to save scraped images to

def make_soup(url):
    x = urlretrieve(url, "local_filename.jpg")
    print(x)


def get_images(url):
    soup = make_soup(url)

    # this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print(str(len(images)) + "images found.")
    print('Downloading images to current working directory.')

    # compile our unicode list of image links
    image_links = [each.get('src') for each in images]
    for each in image_links:
        filename = each.split('/')[-1]
        urllib.urlretrieve(each, filename)
    return image_links


# a standard call looks like this
# get_images('http://www.wookmark.com')


print(make_soup(url))"""


url = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTPyHR8YZ8RKM4RbJsvyvqgNfcEnSsTetlSpA&usqp=CAU"
html = requests.get(url).text  # get the html
soup = BeautifulSoup(html, "lxml")  # give the html to soup

# get all the anchor links with the custom class
# the element or the class name will change based on your case
imgs = soup.findAll("a", {"class": "envira-gallery-link"})
for img in imgs:
    imgUrl = img["href"]  # get the href from the tag
    cmd = ["wget", imgUrl]  # just download it using wget.
    subprocess.Popen(cmd)  # run the command to download
    # if you don"t want to run it parallel;
    # and wait for each image to download just add communicate
    subprocess.Popen(cmd).communicate()
