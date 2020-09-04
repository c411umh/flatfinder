from onthemarket import crawl


def main():
    search_urls = [
        # "https://www.onthemarket.com/to-rent/2-bed-property/central-london/?max-bedrooms=&max-price=3000&min-price=2000&radius=3.0&shared=false",
        "https://www.onthemarket.com/for-sale/2-bed-houses/london/?character-property=true&max-bedrooms=&max-price=500000&property-features=garden&retirement=false&shared-ownership=false&view=grid"
    ]

    # Init file
    # f = csv.writer(open("properties.csv", "w"))
    # f.writerow(["SQFT", "Price", "£ / SQFT", "url", "Address"])

    for url in search_urls:
        if "onthemarket" in url:
            crawl(url, 0)
        else:
            print(f'unknown domain: {url}')


if __name__ == "__main__":
    main()
