# 新北市不動產仲介經紀商業同業公會會員資料查詢
# 1. 公司名稱關鍵字
# 2. 公司地址關鍵字
# -----------------------------------
# input
# 1
# 產業

# output
# 列出所有公司名稱有"產業"
# -----------------------------------
# 2
# 中山路

# 列出所有公司地址有"中山路"
import requests as req
from bs4 import BeautifulSoup
url = 'http://www.tcr.org.tw/a/table_blogs/index/21654?page='

lst = []
for i in range(1, 20):
    res = req.get(url+str(i))
    soup = BeautifulSoup(res.text, "html.parser")
    for tr in soup.find('table').find('table').findAll('tr'):
        atd = tr.findAll('td')
        if len(atd) == 0:
            continue
        # print(atd[0].text, atd[1].text)
        lst.append([atd[0].text, atd[4].text])
# print(lst)
company = input('1. 公司名稱關鍵字\n')
for cmpy in lst:
    if company in cmpy[0]:
        print(cmpy[0])
address = input('2. 公司地址關鍵字\n')
for addr in lst:
    if address in addr[1]:
        print(addr[1])
