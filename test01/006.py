import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 1000)
fig, axes = plt.subplots(nrows=2)
axes[0].set_title("height line chart")
axes[1].set_title("height pie chart")
scr10 = np.array([0 for i in range(12)])
for dt in x:
    if dt >= 141 and dt <= 200:
        scr10[int((dt-141)/5)] += 1

xt = ['141-145', '146-150', '151-155', '156-160', '161-165',
      '166-170', '171-175', '176-180', '181-185', '186-190', '191-195', '196-200']
axes[0].plot(xt, scr10)
scr3 = np.array([0 for i in range(6)])
for dt in x:
    if 140 < dt < 151:
        scr3[0] += 1
    elif 150 < dt < 161:
        scr3[1] += 1
    elif 160 < dt < 171:
        scr3[2] += 1
    elif 170 < dt < 181:
        scr3[3] += 1
    elif 180 < dt < 191:
        scr3[4] += 1
    elif 190 < dt < 201:
        scr3[5] += 1
axes[1].pie(scr3, labels=["141-150", "151-160", "161-170",
            "171-180", "181-190", "191-200"])
plt.show()
