from onthemarket import crawl_onthemarket
from rightmove import crawl_rightmove


def main():
    search_urls = [
        "https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E85330&insId=1&radius=0.0&minPrice=2250&maxPrice=3000&minBedrooms=2&maxBedrooms=3&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare=",
        # "https://www.onthemarket.com/to-rent/2-bed-property/clerkenwell/?max-bedrooms=2&max-price=3000&min-price=2250&radius=0.25&shared=false&view=grid",
        # "https://www.onthemarket.com/to-rent/2-bed-property/shad-thames/?max-bedrooms=2&max-price=3000&min-price=2250&radius=0.25&shared=false&view=grid"
        # "https://www.onthemarket.com/for-sale/2-bed-houses/central-london/?max-bedrooms=&max-price=500000&property-features=garden&radius=1.0&shared-ownership=false&view=grid"
        # "https://www.onthemarket.com/to-rent/2-bed-property/barnsbury/?max-bedrooms=&max-price=3000&min-price=2250&shared=false&view=grid",
        # "https://www.onthemarket.com/to-rent/2-bed-property/farringdon-london/?max-bedrooms=&max-price=3000&min-price=2250&shared=false&view=grid",
        # "https://www.onthemarket.com/to-rent/2-bed-property/clerkenwell/?max-bedrooms=&max-price=3000&min-price=2250&shared=false&view=grid"
        # "https://www.onthemarket.com/to-rent/2-bed-property/kings-cross/?max-bedrooms=&max-price=3000&min-price=2250&shared=false&view=grid",
        # "https://www.onthemarket.com/to-rent/2-bed-property/fitzrovia/?max-bedrooms=&max-price=3000&min-price=2250&shared=false&view=grid",
        # "https://www.onthemarket.com/to-rent/2-bed-property/south-london/?max-bedrooms=&max-price=3000&min-price=1800&shared=false&view=grid",
        # "https://www.onthemarket.com/to-rent/2-bed-property/mayfair/?max-bedrooms=&max-price=3000&min-price=2250&shared=false&view=grid",
        # "https://www.onthemarket.com/to-rent/2-bed-property/kennington/?max-bedrooms=&max-price=3000&min-price=2250&shared=false&view=grid",
        # "https://www.onthemarket.com/to-rent/2-bed-property/notting-hill/?max-bedrooms=&max-price=3000&min-price=2250&shared=false&view=grid",
        # "https://www.onthemarket.com/to-rent/2-bed-property/kensal-green/?max-bedrooms=&max-price=3000&min-price=1800&shared=false&view=grid"
    ]

    # Init file
    # f = csv.writer(open("properties.csv", "w"))
    # f.writerow(["SQFT", "Price", "£ / SQFT", "url", "Address"])

    for url in search_urls:
        if "onthemarket" in url:
            crawl_onthemarket(url, 0)
        if "rightmove" in url:
            crawl_rightmove(url, 0)
        else:
            print(f'unknown domain: {url}')


if __name__ == "__main__":
    main()
