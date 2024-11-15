import requests
from bs4 import BeautifulSoup
import re
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
#data = soup.find_all(string="string exact name")
#print(data)
data = soup.find_all(string = re.compile("string name"))
print(data)
print(len(data))