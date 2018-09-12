import requests
import base64
from bs4 import BeautifulSoup
import re

url = "http://192.168.109.240:20006/"
session = requests.session()
res = session.get(url)
#html = session.get(get_url).content
#print(html.decode("utf-8"))

#soup = BeautifulSoup(html,"html.parser")
#print(soup)

#res = requests.head("http://192.168.109.240:20006/")


#print (res.headers["FLAG"])
data = base64.b64decode(res.headers.get("FLAG"))
#print (data)
#sin = data.split(":")[1]
#print(sin)
a = data.decode("utf-8")                #bytes to string
#print (a)
mydata = a.split(":")[1]
#print (mydata)
updata = {
    "key":mydata
    
    }
print (updata)
res2 = session.post(url,updata)
print(res2.content.decode("utf-8"))
