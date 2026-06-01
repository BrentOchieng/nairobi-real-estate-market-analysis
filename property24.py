import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#single page scraping
url="https://www.property24.co.ke/property-for-sale-in-nairobi-c1890"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
properties = soup.find_all("div", class_="p24_regularTile")
data = []

for property in properties:

    title = property.find("span", class_="p24_propertyTitle")

    price = property.find("span", class_="p24_price")

    location = property.find("span", class_="p24_location")

    data.append({
        "title": title.text.strip() if title else None,
        "price": price.text.strip() if price else None,
        "location": location.text.strip() if location else None
    })

df = pd.DataFrame(data)

print(df.head())

#multipage for single category scraping
all_data = []

for page in range(1, 20):

    url = f"https://www.property24.co.ke/property-for-sale-in-nairobi-c1890?Page=1"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    properties = soup.find_all("div", class_="p24_regularTile")

    for property in properties:

        title = property.find("span", class_="p24_propertyTitle")

        price = property.find("span", class_="p24_price")

        location = property.find("span", class_="p24_location")

        all_data.append({
            "title": title.text.strip() if title else None,
            "price": price.text.strip() if price else None,
            "location": location.text.strip() if location else None
        })

df = pd.DataFrame(all_data)
df

df['location'].unique()

#multipage for different category scraping
#defining categories
categories = {
    "apartments": "https://www.property24.co.ke/apartments-flats-for-sale-in-nairobi-c1890",
    "houses": "https://www.property24.co.ke/houses-for-sale-in-nairobi-c1890",
    "townhouses": "https://www.property24.co.ke/townhouses-for-sale-in-nairobi-c1890",
    "plots": "https://www.property24.co.ke/townhouses-for-sale-in-nairobi-c1890",
    "farms": "https://www.property24.co.ke/farms-for-sale-in-nairobi-c1890",
    "commercial_property":"https://www.property24.co.ke/commercial-property-for-sale-in-nairobi-c1890",
    "industrial_property":"https://www.property24.co.ke/industrial-property-for-sale-in-nairobi-c1890",
}
#creating a scraping function
headers = {"User-Agent": "Mozilla/5.0"}

def scrape_category(url, category_name, pages=3):
    data = []

    for page in range(1, pages + 1):

        paginated_url = f"{url}?Page={page}"

        response = requests.get(paginated_url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        listings = soup.find_all("div", class_="p24_regularTile")

        for item in listings:

            title = item.find("span", class_="p24_propertyTitle")
            price = item.find("span", class_="p24_price")
            location = item.find("span", class_="p24_location")

            data.append({
                "category": category_name,
                "title": title.text.strip() if title else None,
                "price": price.text.strip() if price else None,
                "location": location.text.strip() if location else None
            })

        time.sleep(2)  # avoid blocking

    return data

#looping through all categories
all_data = []

for category, url in categories.items():
    print(f"Scraping {category}...")
    category_data = scrape_category(url, category, pages=5)
    all_data.extend(category_data)

df = pd.DataFrame(all_data)

df

df.to_csv("property24_all_categories.csv", index=False)
