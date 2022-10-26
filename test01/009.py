# 財政部統一發票兌獎網頁

# 1、2月中獎號碼url：
# https://www.etax.nat.gov.tw/etw-main/ETW183W2_11101/
# 3、4月中獎號碼url：
# https://www.etax.nat.gov.tw/etw-main/ETW183W2_11103/
# 5、6月中獎號碼url：
# https://www.etax.nat.gov.tw/etw-main/ETW183W2_11105/
# 7、8月中獎號碼url：
# https://www.etax.nat.gov.tw/etw-main/ETW183W2_11107/

# 輸入
# N (總計要兌幾張發票)
# N 組統一發票號碼
# M (月份，範圍 1、2、3、4、5、6、7、8)
# 輸出每一張發票兌中該月份哪一個獎及該獎獎金，並輸出加總獎金。
# 獎項類別 : 特別獎、特獎、頭獎、二獎、三獎、四獎、五獎、六獎

# Ex.
# input：
# 3
# 05701949
# 97718570
# 65038222
# 7

# output：
# 05701949 無 0
# 97718570 特獎 2000000
# 65038222 三獎 10000
# total_price：2010000
from bs4 import BeautifulSoup
import urllib.request

N = int(input())
recpt = []
for i in range(N):
    recpt.append(input())
M = int(input())
M = M if M & 1 else M-1
request_url = 'https://www.etax.nat.gov.tw/etw-main/ETW183W2_1110'+str(M)+'/'
htmlContent = urllib.request.urlopen(request_url).read()
soup = BeautifulSoup(htmlContent, "html.parser")

results = soup.find_all(
    "div", {"class": {"col-12 mb-3"}})
for i in range(len(results)):
    results[i] = results[i].text
jackpot = []
ssr = results[0].replace(' ', '').strip('\n')
ss = results[1].replace(' ', '').strip('\n')
for i in range(2, 5):
    jackpot.append(results[i].replace(' ', '').strip('\n'))

total_price = 0
for i in range(N):
    maxcnt = 0
    for pots in jackpot:
        cnt = 0
        for j in range(7, -1, -1):
            if recpt[i][j] == pots[j]:
                cnt += 1
            else:
                break
        maxcnt = max(maxcnt, cnt)
    if recpt[i] == ssr:
        print(recpt[i], "特別獎", 10000000)
        total_price += 10000000
    elif recpt[i] == ss:
        print(recpt[i], "特獎", 2000000)
        total_price += 2000000
    elif maxcnt == 8:
        print(recpt[i], "頭獎", 200000)
        total_price += 200000
    elif maxcnt == 7:
        print(recpt[i], "二獎", 40000)
        total_price += 40000
    elif maxcnt == 6:
        print(recpt[i], "三獎", 10000)
        total_price += 10000
    elif maxcnt == 5:
        print(recpt[i], "四獎", 4000)
        total_price += 4000
    elif maxcnt == 4:
        print(recpt[i], "五獎", 1000)
        total_price += 1000
    elif maxcnt == 3:
        print(recpt[i], "六獎", 200)
        total_price += 200
    else:
        print(recpt[i], "無", 0)
print("total_price:", total_price)
