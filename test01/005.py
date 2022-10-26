# 台北市公共自行車即時資訊(json)
# url='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

# 使用Pandas將資料轉換為DataFrame，
# (1) 列出所有場站總停車格(tot)大於80的站點資訊(sno、sna、tot)
# (2) 統計並列出每區的場站總停車格(tot)總數


import pandas as pd
import urllib.request

file = urllib.request.urlretrieve(
    "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json", "bikes.json")
df = pd.read_json('bikes.json')
dctcnt = {}
for index, row in df.iterrows():
    if row['sarea'] not in dctcnt:
        dctcnt[row['sarea']] = 0
    dctcnt[row['sarea']] += int(row['tot'])
df = df[df['tot'] > 80]
print(df[['sno', 'sna', 'tot']])
for key in dctcnt:
    print(key, dctcnt[key])
