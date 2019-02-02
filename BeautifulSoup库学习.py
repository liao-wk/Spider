import requests
from bs4 import BeautifulSoup

kv = {'user-agent': 'Mozilla/5.0'}
url = "https://search.jd.com/Search?keyword=%E8%8D%A3%E8%80%80128g%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=2.def.0.V13&wq=\
%E8%8D%A3%E8%80%80128G&pvid=85d60b1b886249299dda037ccbe46d0b"
r = requests.get(url, headers=kv)
print(r.status_code)
r.encoding = r.apparent_encoding
elems = BeautifulSoup(r.text, 'lxml')
print("成功1")

