import requests
from bs4 import BeautifulSoup
import os

os.chdir("E:\\大道之君\\爬虫学习")
demo = open("demo.txt")
doc = ''
for line in demo:
    doc += line
demo.close()
soup = BeautifulSoup(doc, "lxml")
# 用prettify（）函数进行结构上的美化
print(soup.prettify())
print(soup.a.prettify())

