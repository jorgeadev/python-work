# getem.py
# python2 script to download all images in a given url
# use: python getem.py http://url.where.images.are

import time
import shutil
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def make_soup(url):
    req = requests.get(url).text
    return BeautifulSoup(req, 'html.parser')


def get_images(url):
    soup = make_soup(url)
    print(soup)
    images = [img for img in soup.find_all('img')]
    print(images)
    print(str(len(images)) + " images found.")
    print('Downloading images to current working directory.')
    image_links = [each.get('src') for each in images]
    print(image_links)
    for each in image_links:
        print(each.strip().split('/')[0])
        try:
            if each.strip().split('/')[0] == "https:" or each.strip().split('/')[0] == "http:":
                print("EACH", each)
                filename = each.strip().split('/')[-1].strip()
                print("\n" + filename)
                print('Getting: ' + each)
                response = requests.get(each)
                # delay to avoid corrupted previews
                time.sleep(1)
                with open(filename, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
            else:
                filename = each.strip().split('/')[-1].strip()
                src = urljoin(url, each)
                print('Getting: ' + filename)
                response = requests.get(src, stream=True)
                # delay to avoid corrupted previews
                time.sleep(1)
                with open(filename, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
        except:
            print('  An error occured. Continuing.')
    print('Done.')


if __name__ == '__main__':
    get_images('https://www.google.com/search?hl=en&tbm=isch&sxsrf=ALeKk024xwdimiNO-ICZmuQ9tugq16322w%3A1593496693927&source=hp&biw=958&bih=919&ei=ddT6XrScNI7cswXh9b-YAg&q=paisajes&oq=paisajes&gs_lcp=CgNpbWcQAzIFCAAQsQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgjEOoCECc6BAgjECdQmR9Yyyxg4C5oAXAAeACAAYoBiAGXBZIBAzcuMZgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img&ved=0ahUKEwj0qo3j7ajqAhUO7qwKHeH6DyMQ4dUDCAY&uact=5')
