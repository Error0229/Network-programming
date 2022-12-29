# ibon便利生活站門市查詢
# url='https://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0'

# 輸入一個路/街名，
# 輸出所有依此查詢出的門市資訊(店號、店名、地址)，
# 以城市(縣市)為群組(同一城市可能有相同的路、街名)，
# 再以門牌號碼由小到大排序。

# 註：
# (1) 以城市為群組意思為僅需將相同城市之門市置於前後行相繼輸出，而城市間的輸出順序並沒有限定。
# (2) 門牌號碼皆以地址中第一組門牌號碼來排序，且測資所查詢出的第一組門牌號碼不會出現連字號或頓號等特殊符號。

# Ex.
# input：
# 青年路

# outptu：
# 店號 店名 地址
# 148052 青園 台北市萬華區青年路18號1樓
# 188599 鑫青天 台北市萬華區青年路144號
# 238739 青年 台北市萬華區青年路188號1樓
# 207492 展奇 高雄市鳳山區青年路2段169號1.2樓
# 183206 澄清湖 高雄市鳳山區青年路二段596號.598巷2.4號1.2樓
# 936484 武德 台南市中西區青年路134號
# 251732 慶東 台南市東區青年路416號
# 903831 日南 台中市大甲區日南里青年路130號

import requests as req
import pandas as pd
citys = ['基隆市', '台北市', '新北市', '桃園市', '新竹市', '新竹縣', '苗栗縣', '台中市', '彰化縣', '雲林縣', '南投縣',
         '嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '台東縣', '花蓮縣', '宜蘭縣', '連江縣', '金門縣', '澎湖縣']
datas = []
sest = input()

for city in citys:
    data = {'strTargetField': 'COUNTY', 'strKeyWords': city}
    res = req.post(
        'https://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    # print(pd.read_html(res.text))
    df = pd.read_html(res.text, header=0)[0]
    dt = []
    for index, row in df.iterrows():
        if sest in (row['地址']):
            # print(row['店號'], row['店名'], row['地址'])
            tot = 0
            for i in range(len(row['地址'])):
                if (row['地址'][i] == '號'):
                    id = i-1
                    while (row['地址'][id].isdigit()):
                        tot += int(row['地址'][id])*(10**(i-id-1))
                        id -= 1

                    break
            dt.append([row['店號'], row['店名'], row['地址'], tot])
    if len(dt) == 0:
        continue

    dt.sort(key=lambda x: x[3])
    if len(dt) > 0:
        datas.extend(dt)
for data in datas:
    print(data[0], data[1], data[2])
# 承德路
