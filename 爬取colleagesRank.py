import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        print(r.status_code)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取网址失败")


def fillUnivList(ulist, html):
    Collsoup = BeautifulSoup(html, "lxml")
    colleges = Collsoup.select("tr.alt")
    for college in colleges:
        rank = college.select("td")[0].string
        college_name = college.select("td")[1].string
        score = college.select("td")[3].string
        ulist.append([rank, college_name, score])


def printUnivList(ulist, num):
    print("{0:^10}\t{1:{3}^30}\t{2:^10}".format("排名", "学校名称", "得分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print("{0:^10}\t{1:{3}^30}\t{2:^10}".format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
    html = getHTMLText(url)  # 将url传递给html
    fillUnivList(uinfo, html)  # 通过html，输入大学的信息。
    printUnivList(uinfo, 20)  # 只打印20所大学的信息


if __name__ == "__main__":
    main()


