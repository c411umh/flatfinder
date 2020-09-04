import re
import csv
import requests
import pytesseract
from bs4 import BeautifulSoup
from urllib.request import urlopen
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

sqft_pattern = r'(\d+SQFT)|(\d+ sqft)|(\d+|\d+.\d+)(\W*(sq)\W*(\W(ft)|feet))'
sqft_without_case = re.compile(sqft_pattern, re.IGNORECASE)

pcm_pattern = r'(.*?)\s*\('
pcm_without_case = re.compile(pcm_pattern, re.IGNORECASE)


def numbers_only(input):
    return re.sub("[^0-9.]", "", str(input))


def get_pcm(text):
    res = pcm_without_case.findall(text)
    if (len(res)):
        return res[0]
    else:
        raise Exception('Failed to extract pcm')


def extract_sqft(img):
    parsed = pytesseract.image_to_string(img)
    res = sqft_without_case.findall(parsed)

    highest_sqft = 0
    if (len(res)):
        for capture_groups in res:
            # print(f"capture_groups: {capture_groups}")
            for capture in capture_groups:
                # print(f"capture:{capture}")
                if (capture != ''):
                    num_str = numbers_only(capture)
                    # print(f"\tnum_str:{num_str}")
                    if (len(num_str) > 1):
                        num = int(float(num_str))
                        # print(f"\t\tnum:{num}")
                        if (num > highest_sqft):
                            highest_sqft = num

        # print(f"\nhighest_sqft: {highest_sqft}\n")
        return highest_sqft
    else:
        # import pdb
        # pdb.set_trace()
        raise Exception("Failed to extract SQFT")


def process_property(dict):
    print(dict)
    sqft = dict["sqft"]
    price = dict["price"]
    address = dict["address"]
    url = dict["url"]

    # TODO check if this exists, append etc
    if (sqft > 1000):
        f = csv.writer(open("properties.csv", "a"))
        f.writerow([sqft, price, f"£{round(price/sqft, 2)}", url, address])
