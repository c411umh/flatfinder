from onthemarket import crawl_onthemarket
from rightmove import crawl_rightmove


def main():
    search_urls = [
      "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E92824&maxBedrooms=3&minBedrooms=2&maxPrice=2250"
    ]

    for url in search_urls:
        if "onthemarket" in url:
            crawl_onthemarket(url, 0)
        if "rightmove" in url:
            crawl_rightmove(url, 0)
        else:
            print(f'unknown domain: {url}')


if __name__ == "__main__":
    main()
