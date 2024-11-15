import prices
import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
prices = (soup.find_all("h4",{"class" : "class_name""}))
print(prices)
#print(len(prices))
for i in price:
#prices(i)
#prices(i.text)
print(prices[3])