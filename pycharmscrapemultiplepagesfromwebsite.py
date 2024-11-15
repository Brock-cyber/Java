import requests
from bs4 import BeautifulSoup
for i in range(2,11):
url = "https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as="+str(i)
r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.text,"lxml")
#print(soup)

#To have diff links
while True:
new_page = soup.find("a",{"class":"_1LKT03"}).get("href")
#print(new_page)
#To remove /search form the start of the link
complete = "https://www.flipkart.com/"+new_page
#print(complete)

url = complete
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")