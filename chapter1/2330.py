# 找台積電股票
# 輸入2個 年期範圍
# 輸出現金股利與加總
import requests
from bs4 import BeautifulSoup
html = requests.get("https://tw.stock.yahoo.com/quote/2330.TW/dividend")
bsObj = BeautifulSoup(html.text, "html.parser")
year_start = input("請輸入起始年份:")
year_end = input("請輸入結束年份:")
all_ss = []
for single_tr in bsObj.find("ul", class_="M(0) P(0) List(n)").findAll("li", class_="List(n)"):
    cell = single_tr.findAll("div", class_="D(f) W(98px) Ta(start)")
    season = cell[0].contents[0]
    divi = single_tr.findAll(
        "div", class_="Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)")[0].contents[0].text
    all_ss.append([season, float(divi)])
start = 0
alls = 0.0
all_ss = all_ss[::-1]
for i in range(len(all_ss)):
    if all_ss[i][0] == year_start:
        start = 1
    if start == 1:
        alls += all_ss[i][1]
        print(all_ss[i][0], all_ss[i][1])
    if all_ss[i][0] == year_end:
        break
print("加總:", alls)
