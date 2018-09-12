import requests
r = requests.get("http://www.baidu.com")
#r.status_code  r状态码
#print (r)
r.encoding = "utf-8"
print(r.text)
print(r.headers)
