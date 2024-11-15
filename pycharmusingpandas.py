import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = Beautifulsoup(r.text,"lxml")

names = soup.find_all("h4",{"class":"class_name"})
#print(names)
product_names = []
for i in names
    names = i.text
    product_names.append(names)
    print(product_names)

    prices = soup.find_all("h4", {"class": "class_name"})
    # print(prices)
    prices_list = []
    for i in prices
        prices = i.text
        prices_list.append(pricess)
        print(prices_list)

desc = soup.find_all("p",{"class":"class_name"})
#print(desc)
desc_list = []
for i in desc
    desc = i.text
    desc_list.append(desc)
    print(desc_list)

reviews = soup.find_all("p",{"class":"class_name"})
#print(reviews)
review_list = []
for i in reviews
    reviews = i.text
    review_list.append(reviews)
    print(review_list)

df = pd.DataFrame({"Product Name":product_names,"Prices":prices_list,"Description":desc,"Reviews":reviews})
print(df)

#convert to excel

df.to_csv("product_details.csv")