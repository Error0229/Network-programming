import numpy as np
nf1 = np.genfromtxt('npdata/pig.csv', delimiter=',', skip_header=1)
print(np.std(nf1, axis=0)[1])
print(np.median(nf1, axis=0)[2])
print(np.percentile(nf1, 75, axis=0)[1])
