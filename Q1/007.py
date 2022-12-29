# 地震測報中心-全球地震
# url='https://scweb.cwb.gov.tw/zh-tw/earthquake/world/#'

# 、列出規模最大的前3筆地震資訊(地震時間深度、規模、地震位置)，
# 若規模相同則再以深度由淺至深排序

# Ex.
# 地震時間 深度 規模 地震位置
# 2022/09/29-11:03 10 6.8 南大西洋南三明治群島東方
# 2022/09/24-06:53 12 6.1 墨西哥米卻肯
# 2022/09/24-04:52 48 6.1 印尼巴布亞
# 中央氣象局-專有名詞中英詞彙對照
# 輸入一個中文字，輸出所有這個中文字的中文、英文對照
# 輸入一個英文字母字串，輸出包含所有這些英文字母字串的英文、中文對照

from urllib.request import urlopen
from bs4 import BeautifulSoup

htmlname = "https://scweb.cwb.gov.tw/zh-tw/earthquake/world/#"
html = urlopen(htmlname)
bsObj = BeautifulSoup(html, "lxml")
data = []
for single_tr in bsObj.find("table").find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    F1 = cell[0].text
    F2 = cell[3].text
    F3 = cell[4].text
    F4 = cell[5].find("a").text
    data.append([F1, F2, F3, F4])

data.sort(key=lambda x: (float(x[2]), -float(x[1])), reverse=True)
for i in range(3):
    print(data[i][0], data[i][1], data[i][2], data[i][3])
