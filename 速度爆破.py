import hashlib
import requests
from bs4 import BeautifulSoup

get_url = "http://ctf5.shiyanbar.com/ppc/sd.php"
session = requests.session()

html = session.get(get_url).content
#html = html.decode("utf-8")
#print(html)
soup = BeautifulSoup(html,"html.parser")
encode_str = soup.div.get_text()
#print (soup)
#print (encode_str)

for i in range(0,100000):
    hash_md5 = hashlib.md5(str(i).encode("utf-8")).hexdigest()
    hash_sha1 = hashlib.sha1(hash_md5.encode('utf-8')).hexdigest()
    if encode_str == hash_sha1:
        #提交
        payload = {'inputNumber':i}
        post =session.post(get_url, payload)
        #print(post.text)
        print(post.content.decode("utf-8"))
