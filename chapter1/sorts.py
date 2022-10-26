"""
輸出全年成交平均重量的成交頭數，最低前 5 筆資料
輸出全年成交平均價格的成交頭數，最高前 5 筆資料
輸出全年成交平均重量的成交頭數，最低前 5 筆資料，原本資料的次序編號
"""

import numpy as np
dtype = [('id', 'i4'), ('weight', 'f4'), ('price', 'f4')]
nf1 = np.genfromtxt('npdata/pig.csv', delimiter=',',
                    dtype=dtype, skip_header=1)

# nf1 = np.genfromtxt('npdata/pig.csv', delimiter=',', skip_header=1)
# nf1 = np.array(list(zip(nf1[:, 0], nf1[:, 1], nf1[:, 2])), dtype=dtype)
fst = np.sort(nf1, order='weight')
for i in range(5):
    print(int(fst[i][0]))
print()
fst = np.sort(nf1, order='price')
fst = np.flip(fst)
for i in range(5):
    print(int(fst[i][0]))
print()
fst = np.sort(nf1, order='weight')
for i in range(5):
    print(np.where(nf1 == fst[i])[0][0])
