"""
week02
05
使用 Pandas
載入 bike.json
1. 找出空位數大於 10 的站點資料，輸出所在區、站點名稱、地址、空位數
2. 根據第一點的資料，
統計出每一區(新店區、板橋區、....)空位數大於 10 的資料，
輸出每一區空位數大於 10 的所有加總空位數
e.g.
新店區 30
板橋區 50

"""

import pandas as pd
df = pd.read_json('npdata/bike.json')
df = df[df['sbi'] > 10]
print(df[['sarea', 'sna', 'ar', 'sbi']])
dctcnt = {}
for index, row in df.iterrows():
    if row['sarea'] not in dctcnt:
        dctcnt[row['sarea']] = 0
    dctcnt[row['sarea']] += 1
for key in dctcnt:
    print(key, dctcnt[key])
print()
dct = {}
for index, row in df.iterrows():
    if row['sarea'] not in dct:
        dct[row['sarea']] = 0
    dct[row['sarea']] += row['sbi']

for k, v in dct.items():
    print(k, v)
