import urllib.request
import json
url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json/preview"
json_name = "ubike_rent.json"
urllib.request.urlretrieve(url, json_name)
lst = []
with open("ubike_rent.json", encoding="utf8") as file:
    data = json.load(file)
    fl = True
    for item in data:
        if fl:
            fl = False
            continue
        if (int(item['sbi']) > 6):
            lst.append([item['sno'], item['sna'],
                        item['tot'], item['sbi'], item['ar'], item['bemp']])
    lst.sort(key=lambda s: int(s[3]))
    for row in lst:
        print(
            f'{row[0]:\u3000<5}, {row[1]:\u3000<10}, {row[2]:5s}, {row[3]:5s}, {row[4]:\u3000<20}, {row[5]:5s}')
