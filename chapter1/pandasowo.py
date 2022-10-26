import pandas as pd
df1 = pd.read_csv('npdata/president_heights.csv', encoding="utf-8", sep=",")
df1.columns = ['order', 'name', 'height']
print(df1.sort_values("height", ascending=False).head(5))
print(df1[df1.height > 180].sort_values("height", ascending=False).tail(5))
"""
輸出總統身高的敘述統計資料
輸出總統身高，最高前 5 筆資料
輸出總統身高 > 180，最低的 5 筆資料
"""
