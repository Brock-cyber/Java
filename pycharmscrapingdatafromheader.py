import requests
from  bs4 import BeautifulSoup
import pandas as pd
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

df = pd.DataFrame(columns=titles)
print(df)