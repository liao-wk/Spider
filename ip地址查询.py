import requests

url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + "202.204.80.112")
    print(r.status_code)
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
