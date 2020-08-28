import math
from Functions_Module import saveFilePK

primes = []

for i in range(10000000000, 100000000000):
    primes.append(i)
    print(i)

for j in primes:
    print(j)
    for k in range(2, j//2):
        print(" " + str(k))
        if (j % k) == 0:
            primes.remove(j)
            break
        
        
saveFilePK(primes, "primes")
