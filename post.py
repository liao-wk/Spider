import requests
#  学习post（）方法
pyyload = {'key1': "value1", "key2": "value2"}
r = requests.post("http://www.baidu.com/post", data=pyyload)
r.encoding = "utf-8"
print(r.text)

