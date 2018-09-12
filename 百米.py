from bs4 import BeautifulSoup
import requests
get_url = "http://ctf5.shiyanbar.com/jia/"
post_url = "http://ctf5.shiyanbar.com/jia/index.php?action=check_pass"
session = requests.session()
html = session.get(get_url).content

soup = BeautifulSoup(html,"html.parser")
expr = soup.p.div.get_text()
print(expr)
num = eval(expr.replace('x', '*'))
print(num)
payload = {"pass_key":str(num)}
print(payload)
post = session.post(post_url,payload)
print(post.text)
