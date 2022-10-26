import csv
lst = []
with open("radi.csv", "r", encoding="Big5") as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # next(plots)
    fl = True
    for row in plots:
        if fl:
            fl = False
            continue
        lst.append(row)
while True:
    lo, la, dev_o, dev_a = map(float, input().split())
    data = []

    for info in lst:
        # print(info[4], info[5], lo-dev_o, lo+dev_o, la-dev_a, la+dev_a)
        if (float(info[4]) > lo - dev_o and float(info[4]) < lo + dev_o) and (float(info[5]) > la - dev_a and float(info[5]) < la + dev_a):
            data.append(info)
    data.sort(key=lambda s: s[2])
    for info in data:
        print(f'{info[0]:\u3000<6},{info[2]:<6}')

"""
針對全國環境輻射偵測即時資訊
輸入
一個經緯度(整數)
經度與緯度偏離值

輸出
這個經緯度周圍偏離值的監測點和監測值
以監測值大小排序
"""
