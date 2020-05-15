import  requests
import bs4


chunk_size = 256

link = "https://codigofacilito.com/videos/multiples-valores-de-entrada-y-salida"
url = 'https://player.vimeo.com/video/238137238?api=1&amp;player_id=vimeo_player&amp;speed=1'


def get_links(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    files_2 = [a.attrs.get("href") for a in soup.select("a")]
    files = files_2[0:]
    return files


r = requests.get(url, stream = True)
with open('fdxd.mp4', 'wb') as f:
    for chunk in r.iter_content(chunk_size = chunk_size):
        f.write(chunk)
