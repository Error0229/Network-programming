# 臺灣銀行新台幣黃金存摺牌價
# url='https://www.bot.com.tw/Govinfo/opendata/csv/233/110GoldPassbook.csv'

# 使用numpy讀取csv檔，
# (1) 列出本行買入價格最低價的前五筆資訊(日期、本行買入價格、本行賣出價格)
# (2) 輸出本行買入價格的中位數 (3)
# (3) 輸出本行賣出價格的平均值(四捨五入至小數點後第二位)
# (4) 輸出本行賣出價格的標準差(四捨五入至小數點後第二位)
import numpy as np
import urllib.request
file = urllib.request.urlretrieve(
    "https://www.bot.com.tw/Govinfo/opendata/csv/233/110GoldPassbook.csv", "gold.csv")
dtype = [('date', '<U8'), ('bi', '<U8'), ('wei', '<U8'),
         ('buy', 'i4'), ('sell', 'i4')]
nf1 = np.genfromtxt('gold.csv', delimiter=',',
                    skip_header=1, dtype=dtype, encoding="utf8")
nf1 = np.sort(nf1, axis=0, order='buy')
print("日期 本行買入價格 本行賣出價格")
for i in range(5):
    print(f'{nf1[i][0]}, {nf1[i][3]}, {nf1[i][4]}')
nplst = np.array(nf1['buy'])
nplst2 = np.array(nf1['sell'])
print(int(np.median(nplst, axis=0)))
print(f'{np.mean(nplst2, axis=0):.2f}')
print(f'{np.std(nplst2, axis=0):.2f}')
