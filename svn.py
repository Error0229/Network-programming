# 找出店最多個數的街/路前三名
import requests as req
import pandas as pd
# citys = ['基隆市', '台北市', '新北市', '桃園市', '新竹市', '新竹縣', '苗栗縣', '台中市', '彰化縣', '雲林縣', '南投縣',
#  '嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '台東縣', '花蓮縣', '宜蘭縣', '連江縣', '金門縣', '澎湖縣']
citys = input("請輸入3個縣市名稱，以空白鍵隔開:").split()
dct = {}
for city in citys:
    data = {'strTargetField': 'COUNTY', 'strKeyWords': city}
    res = req.post(
        'https://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    # print(pd.read_html(res.text))
    df = pd.read_html(res.text, header=0)[0]
    for index, row in df.iterrows():
        street = ""
        for id, word in reversed(list(enumerate(row['地址']))):
            if word == '路' or word == '街':
                street = row['地址'][:id+1]
                break
        if street == "":
            continue
        if street not in dct:
            dct[street] = 0
        dct[street] += 1
dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
    print(dct[i][0], dct[i][1])
