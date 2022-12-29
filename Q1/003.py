# 新北市公共自行車即時資訊(xml)
# url ='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/xml/preview'

# 將此xml資料存取為data1.xml，再使用程式碼讀取data1.xml

# step 1：新增一個row
# <row>
# <sno>1033</sno>
# <sna>家樂福新店店</sna>
# <tot>30</tot>
# <sbi>29</sbi>
# <sarea>新店區</sarea>
# </row>
# step 2：將sno：1018站點資訊的sbi修改為0
# step 3：將上述兩步修改後的資料寫入data2.xml
# step 4：讀取data2.xml，列出所有新店區的站點資訊(sno、sna、tot、sbi)

import xml.etree.ElementTree as ET
import urllib.request
xmlfile = urllib.request.urlretrieve(
    "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/xml/preview", "data1.xml")

tree = ET.parse("data1.xml")
root = tree.getroot()
row = ET.SubElement(root, "row")
sno = ET.SubElement(row, "sno")
sno.text = "1033"
sna = ET.SubElement(row, "sna")
sna.text = "家樂福新店店"
tot = ET.SubElement(row, "tot")
tot.text = "30"
sbi = ET.SubElement(row, "sbi")
sbi.text = "29"
sarea = ET.SubElement(row, "sarea")
sarea.text = "新店區"


for elem in root.iter("row"):
    for sno in elem.iter("sno"):
        if sno.text == "1018":
            for sbi in elem.iter("sbi"):
                sbi.text = "0"
    # if elem.get("sno") == "1018":
    #     elem.get("sbi").text = "0"


tree.write('data2.xml', encoding='utf-8')
print("sno sna tot sbi")
with open('data2.xml', encoding='utf8'):
    tree = ET.parse("data2.xml")
    root = tree.getroot()
    for elem in root.iter("row"):
        for sarea in elem.iter("sarea"):
            if sarea.text == "新店區":
                for sno in elem.iter("sno"):
                    print(sno.text, end=", ")
                for sna in elem.iter("sna"):
                    print(sna.text, end=", ")
                for tot in elem.iter("tot"):
                    print(tot.text, end=", ")
                for sbi in elem.iter("sbi"):
                    print(sbi.text)
