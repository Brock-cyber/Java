import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
#print(soup.find('div'))
#print(soup.find("h4",{"class" : "class_name""}))
#price = (soup.find("h4",{"class" : "class_name""}))
print(price.string)