import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
table = soup.find("table",{"class":"ih-td-tab auction-tbl"})
#print(table)

header = table.find_all("th")
#print(header)
titles = []
for i in header:
    titles=i.text
    titles.append(title)
    #print(titles)

df = pd.DataFrame(columns = titles)
#print(df)

rows = table.find_all("tr")
#print(rows)

for i in rows[1:]:
    data = i.find_all("td")
    #print(data)

#to find data for each row
row = [tr.text for tr in data]
#print(row)

#to dataframe
l = len(df)
df.loc[l] = row
#print(df)

#To remove backslashes from team name

#for i in rows[1:]:
   # first_td = i.find_all("td")[0].find("div",{"class":"ih-pt-ic"}).text.strip()
   # data = i.find_all("td")[1:]
   # row = [tr.text for tr in data]
    #row.insert(0,first_td)
