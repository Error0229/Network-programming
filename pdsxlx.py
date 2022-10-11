"""
計算 2002 年全球人口各國平均數
計算 2002 年全球各洲平均壽命、平均財富
"""
import pandas as pd
gap = pd.read_excel('npdata/gapminder.xlsx', engine='openpyxl')

means = gap[gap.year == 2002].mean()
print(means['pop'])

conti = gap[gap.year == 2002].groupby('continent').mean()

print(conti['lifeExp'])
print(conti['gdpPercap'])
