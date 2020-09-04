import re
import io
import PIL
import requests
from PIL import Image
from bs4 import BeautifulSoup
from urllib.request import urlopen
from utils import extract_sqft, process_property, get_pcm, numbers_only


def extract(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    data = {
        "sqft": -1,
        "address": -1,
        "price": -1,
        "url": url
    }

    # SQFT
    for img in soup.find_all("img"):
        if 'floorplan' in img["alt"].lower():
            image_url = img['src']
            response = requests.get(image_url)
            img = Image.open(io.BytesIO(response.content))
            try:
                sqft = extract_sqft(img)
                if (sqft):
                    data["sqft"] = sqft
            except:
                print('failed to extract sqft :(')

    for heading in soup.find_all("div", {"class": "details-heading"}):
        # Address
        for address in heading.find_all("p", {'class': None}):
            data["address"] = address.text.replace("'", '')
        # Price
        for price in heading.find_all("span", {"class": "price-data"}):
            # Let
            if ("(" in price):
                pcm = get_pcm(price.text)
                # if (len(res)):
                # pcm = res[0]
                pcm = re.sub("[^0-9]", "", pcm)
                data["price"] = int(float(pcm))
            # Sale
            else:
                # re.sub("[^0-9]", "", price.text)
                price = numbers_only(price.text)
                data["price"] = int(float(price))

    return data


def crawl(root_url, counter):
    print(f"\n🕷 crawling page {counter+1}")
    page = urlopen(f"{root_url}&page={counter}")
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    results = soup.find_all("ul", {"id": "properties"})
    crawled = False

    for ul in results:
        if (len(ul) == 0):
            crawled = True
        for li in ul.find_all("li"):
            property_id = li['data-instruction-id']
            url = f"https://www.onthemarket.com/details/{property_id}/"
            data = extract(url)
            if (data['sqft'] != -1):
                process_property(data)

    counter += 1

    if (crawled == True):
        print('✨Finished ✨')
    else:
        crawl(root_url, counter)
