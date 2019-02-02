import requests
res = requests.get("http://www.baidu.com/")
print(res.status_code)
print(res.encoding)
print(res.apparent_encoding)
res.encoding = "utf-8"
print(res.text)
