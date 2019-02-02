import requests

url = "http://www.baidu.com/"
hd = {"user-agent": "Mozilla/5.0"}
kv = {"wd": "Python"}
# 360
# kv = {"q": "Python"}
r = requests.get(url, headers=hd, params=kv)
print(r.status_code)
r.encoding = r.apparent_encoding
print(r.text[100000:500000])

