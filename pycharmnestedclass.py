import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
#box = soup.find("div",{"class":class_name})[3]
#print(box)
name = box.find("a").text
print(name)
print(len(name))