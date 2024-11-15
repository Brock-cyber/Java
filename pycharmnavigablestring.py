import requests
from  bs4 import BeautifulSoup4
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = bs4.BeautifulSoup(r.text, "lxml")
tag=soup.header.div.p.button.span
#print(tag.string)
print(tag)