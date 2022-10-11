# 中央氣象局-專有名詞中英詞彙對照
# 輸入一個中文字，輸出所有這個中文字的中文、英文對照
# 輸入一個英文字母字串，輸出包含所有這些英文字母字串的英文、中文對照

from urllib.request import urlopen
from bs4 import BeautifulSoup

htmlname = "https://www.cwb.gov.tw/V8/C/K/bilingual_glossary.html"
html = urlopen(htmlname)
bsObj = BeautifulSoup(html, "lxml")
data = []
for single_tr in bsObj.find("table").find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    F1 = cell[1].text.lower()
    F2 = cell[2].text
    data.append([F1, F2])
zh_input = input("請輸入中文字:")
for i in range(len(data)):
    if zh_input in data[i][1]:
        print(data[i][1], data[i][0])
en_input = input("請輸入英文字母字串:").lower()
for i in range(len(data)):
    if en_input in data[i][0]:
        print(data[i][0], data[i][1])
