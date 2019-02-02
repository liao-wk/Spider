import requests
import os

url = "http://static.ngchina.cn/repo/milu2018/./img/milu-115-1748S(1)-1.jpg"
root = "E://大道之君//爬虫学习//图片库"
path = root + '//'+url.split("/")[-1]
print(path)
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        with open(path, 'wb') as f:
            f.write(r.content)
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败！！!")

