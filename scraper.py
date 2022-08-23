from dataclasses import replace
import requests
from threading import Condition
from tkinter.ttk import Style
from bs4 import BeautifulSoup
from numpy import product
import pandas as pd
import urllib.request

response = requests.get("https://www.thredup.com/product/women-zapelle-casual-dress/124851824")
soup = BeautifulSoup(response.text, 'html.parser')
brand_titles = soup.select('a.ui-link')
for title in brand_titles:
    brand = title.text
# brand
print(brand)

products = soup.findAll('div', attrs={"class" : "Dtqm58cMCEcuWeKEsVy_ u-border u-border-gray-1 u-border-solid u-rounded-4"})
product_style = products[0]['style']
product_imgs = product_style.split('"')
product = product_imgs[1]
# product
print(product)
urllib.request.urlretrieve(product, "scraping.jpg")

original_prices = soup.findAll('span', attrs={"class" : "u-text-20 u-font-bold u-mr-1xs"})
original_price = original_prices[0].text
# original_price
print(original_price)

final_prices = soup.findAll('span', attrs={"class" : "price u-font-bold u-text-20 u-text-alert"})
final_price = final_prices[0].text
# final_price
print(final_price)

sizes = soup.select('div.P9j6cGJ6kvC9bBgLk4pE')
size_string = sizes[0].text
size_a = size_string.split()
size = size_a[1]
# size
print(size)

item_details = soup.select('li.u-mr-1x')
details = ""
for title in item_details:
    details = details + title.text + "; "
# item_details
print(details)

conditions = soup.findAll('div', attrs={"class" : "qIe8uEwlaO9qd8EVVIlr"})
condition_ul = conditions[2].text
condition = condition_ul.replace("Condition", "")
print(condition)

data = {
    "brand" : brand,
    "product" : product,
    "original_price" :  original_price,
    "final_price" : final_price,
    "size" : size,
    "item_details" : details,
    "condition" : condition
}

df = pd.DataFrame(data, index=[0])
print(df)
df.to_csv('scraping.csv', index=False, encoding='utf-8')