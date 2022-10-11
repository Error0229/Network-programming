# 找出現金買入和賣出利差最多的前三名
import requests
from bs4 import BeautifulSoup
html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
bsObj = BeautifulSoup(html.content, "lxml")
all_spread = []
for single_tr in bsObj.find("table", {"title": "牌告匯率"}).find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    currency_name = cell[0].find(
        "div", {"class": "visible-phone"}).contents[0]
    currency_name = currency_name.strip()
    buy_in = cell[1].contents[0]
    sell_out = cell[2].contents[0]
    if (buy_in == "-") or (sell_out == "-"):
        continue
    spread = float(sell_out) - float(buy_in)
    all_spread.append([currency_name, spread])
all_spread.sort(key=lambda x: x[1], reverse=True)
for i in range(3):
    print(f'{all_spread[i][0]}  {all_spread[i][1]:.3f}')
