import requests

url = "https://www.amazon.cn/gp/product/B07JYQTKM4/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-1&pf_rd_r=EMR4BE337PMSM7QGQGBK&pf_rd_t=101&pf_rd_p=a6e56a89-663d-4383-b7dd-e54b892d2865&pf_rd_i=1994342071"

try:
    kv = {"user-agent": "Mozilla/5.0"}
    r = requests.get(url, headers=kv)
    print(r.status_code)
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败！！！")


