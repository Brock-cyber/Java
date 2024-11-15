import requests
from  bs4 import BeautifulSoup
import pandas as pd
from pandas.plotting import table

url = "https://ticker.finology.in/"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
row = soup.find("table",{"class":"class_name"})
print(row)
headers = row.find_all("th")
print(headers)
titles = []
for i in headers:
    row = i.text
    titles.append(row)
    print(row)

rows = row.find_all("tr")
#print(rows)

#now row of header will also print,to remove header
for i in rows[1:]:
    #print(i.text)

data = i.find_all("td")
#print(data)

rowss[tr.text for tr in data]
    #print(rowss)

l = lenf(df)
df.loc[l] = table
print(df)

#if convert this file to excel(csv file)
df.to_csv("stock_market_data.csv")