# 新北市電動機車充電站-板橋區(json)
# url ='https://data.ntpc.gov.tw/api/datasets/1688B7B8-106E-4967-AA38-DBD86D81D495/json/preview'

# 部分欄位說明：
# sta(站名)、add(地址)、cha(是否收費)、ope(是否對外開放)、no(充電插座數)

# 使用程式碼讀取json格式檔案，
# 列出全部有收費且不對外開放的電動機車充電站資訊(sta、add、no)
import urllib.request
import json
url = "https://data.ntpc.gov.tw/api/datasets/1688B7B8-106E-4967-AA38-DBD86D81D495/json/preview"
json_name = "ubike_rent.json"
urllib.request.urlretrieve(url, json_name)
lst = []
with open("ubike_rent.json", encoding="utf8") as file:
    data = json.load(file)
    for item in data:
        if (item['cha'] == "是" and item['ope'] == "否"):
            lst.append([item['sta'], item['add'], item['no']])
    print("sta add no")
    for row in lst:
        print(row[0], row[1], row[2])
