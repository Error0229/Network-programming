# 輸入一組統一編號
# 輸出是否中二百元，或者差一個號碼中兩百元
from __future__ import unicode_literals, print_function
import urllib
from bs4 import BeautifulSoup
import urllib.request
request_url = 'http://invoice.etax.nat.gov.tw/'
htmlContent = urllib.request.urlopen(request_url).read()
soup = BeautifulSoup(htmlContent, "html.parser")

recpt = input("請輸入發票號碼:")
results = soup.find_all(
    "span", {"class": {"font-weight-bold etw-color-red", "font-weight-bold"}})
# print(results)
jackpot = []

for index2, item2 in enumerate(results[2:8]):
    if index2 % 2 == 0:
        jackpot.append(item2.text+results[index2+3].text)
maxcnt = 0
for pots in jackpot:
    cnt = 0
    for i in range(5, 8):
        if recpt[i] == pots[i]:
            cnt += 1
    maxcnt = max(maxcnt, cnt)
if maxcnt == 3:
    print("中二百元")
elif maxcnt == 2:
    print("差一個號碼中二百元")
