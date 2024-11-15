import requests
url = "https://www.youtube.com/watch?v=V-j0FTGoblg&list=PLc20sA5NNOvrsn3a78ewy2VTCXVV47NB4&index=4"
r = requests.get(url)
#print(r.status_code)
print(r.text)