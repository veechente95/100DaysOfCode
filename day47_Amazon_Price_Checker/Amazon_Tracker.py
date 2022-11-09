import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


url = "https://www.amazon.com/OPTIMUM-NUTRITION-STANDARD-Protein-Chocolate/dp/B002DYIZH6/ref=sr_1_5?keywords=whey+protein&qid=1667953934&sr=8-5"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(id="sns-base-price").get_text()

# TODO: Find the ID tag for price
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


title = soup.find(id="productTitle").get_text().strip()
print(title)
