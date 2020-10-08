import re
import io
import PIL
import requests
from PIL import Image
from bs4 import BeautifulSoup
from urllib.request import urlopen
from utils import extract_sqft, process_property, extract_pcm, numbers_only


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
                pass

    for heading in soup.find_all("div", {"class": "details-heading"}):
        # Address
        for address in heading.find_all("p", {'class': None}):
            data["address"] = address.text.replace("'", '')
        # Price
        for price in heading.find_all("span", {"class": "price-data"}):
            # Let
            if ("pcm" in price.text):
                pcm = extract_pcm(price.text)
                try:
                    data["price"] = int(float(pcm))
                except:
                    print(f"Error parsing pcm: {pcm}, raw: {price.text}")
                    pass
            # Sale
            else:
                price = numbers_only(price.text)
                try:
                    data["price"] = int(float(price))
                except:
                    print(
                        f"Error parsing sale price: {price}, raw: {price.text}")
                    pass

    return data


def crawl_rightmove(root_url, counter):
    print(f"\n🕷 crawling page {counter+1}")
    page = urlopen(f"{root_url}&page={counter}")
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    results = soup.find_all("a", {"class": "propertyCard-anchor"})
    if (len(results) > 0):
        for a in results:
            property_id = a['id'].replace('prop', '')
            url = f"https://www.rightmove.co.uk/properties/{property_id}/"
            data = extract(url)
            if (data['sqft'] != -1):
                process_property(data)
        counter += 1
        crawl_rightmove(root_url, counter)
    else:
        print('✨Finished ✨')
