import matplotlib.pyplot as plt
import numpy as np
n = int(input())
x = np.random.randint(101, size=n)
titles = ['failed or passed', 'score in range 5 count',
          'score in range 10 count', 'score in three part']
fig, axes = plt.subplots(nrows=2, ncols=2)
for i in range(4):
    axes[i//2, i % 2].set_title(titles[i], size=10)
pscnt = np.array([0, 0])
pscnt[0] = len(x[x > 59])
pscnt[1] = len(x[x < 59])
print(pscnt)
xx = np.arange(2)
label1 = ['pass', 'failed']
axes[0, 0].bar(xx, pscnt)
axes[0, 0].set(xlabel='Score', ylabel='Quantity',
               xticklabels=label1, xticks=xx)

scr5 = np.array([0 for i in range(20)])
for dt in x:
    scr5[int(abs(dt-1)/5)] += 1
xs = ['0~5', '5~10', '10~15', '15~20', '20~25', '25~30', '30~35', '35~40', '40~45', '45~50',
      '50~55', '55~60', '60~65', '65~70', '70~75', '75~80', '80~85', '85~90', '90~95', '95~100']
axes[0, 1].plot(xs, scr5, 'r')
axes[0, 1].set(xlabel='Score', ylabel='Quantity')
axes[0, 1].set_xticklabels(xs, rotation=90)

scr10 = np.array([0 for i in range(10)])
for dt in x:
    scr10[int(abs(dt-1)/10)] += 1
tenx = ['0~10', '10~20', '20~30', '30~40', '40~50',
        '50~60', '60~70', '70~80', '80~90', '90~100']
# axes[1, 0].plot(tenx, scr10)
axes[1, 0].scatter(tenx, scr10, marker="h")
axes[1, 0].set(xlabel='Score', ylabel='Quantity')
axes[1, 0].set_xticklabels(tenx, rotation=90)

scr3 = np.array([0 for i in range(3)])
for dt in x:
    if dt < 60:
        scr3[0] += 1
    elif dt < 80:
        scr3[1] += 1
    else:
        scr3[2] += 1
thx = ['0~60', '60~80', '80~100']
axes[1, 1].pie(scr3, labels=thx, autopct='%1.1f%%')
axes[1, 1].axis('equal')
fig.tight_layout()
plt.show()


"""
隨機亂數產生全班N ( 輸入)位學成績，0~100
畫四個子圖，每一個子圖要有標題、刻度、標籤樣式
1. 長條圖 統計及格與不及格人數
2. 折線圖 x 分數， y 人數，每五分一個區間
3. 散射圖 x 分數， y 人數，每 10 分一個區間，自訂一個 mark
4. 圓餅圖 81~100, 60~80, 0~59 三塊餅
"""
