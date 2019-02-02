import requests

r = requests.get("https://sale.jd.com/act/8yaD0qZuE6VFk.html")
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)

print(r.request.headers)
#  更改头部信息,伪装成浏览器。
#  {'User-Agent': 'python-requests/2.18.4',、
#  'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
#  Mozilla/5.0代表火狐浏览器
kv = {"user-agent": "Mozilla/5.0"}
