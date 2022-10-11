import numpy as np
nf1 = np.genfromtxt('npdata/pig.csv', delimiter=',', skip_header=1)
maxweight = np.min(nf1[:, 1])
maxprice = np.max(nf1[:, 2])
MinWeightAmountid = np.where(nf1[:, 1] == maxweight)
MaxPriceAmountid = np.where(nf1[:, 2] == maxprice)
print(int(nf1[MinWeightAmountid, 0]))
print(int(nf1[MaxPriceAmountid, 0]))
