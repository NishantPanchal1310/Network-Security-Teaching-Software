import math
from Functions_Module import saveFilePK

bits = 100
while bits != 16:
    bits = int(input("Enter amount bits of RSA keys: "))

primes = []

numFrom = int(2**(bits/2))
numTo = int(2**((bits/2)+1))

print("making number list")
for i in range(numFrom, numTo):
    primes.append(i)

print("finding primes")
for j in primes:
    for k in range(2, j//2):
        if (j % k) == 0:
            primes.remove(j)
            break
        
filename = "primes_" + str(bits) + "bits"     

saveFilePK(primes, filename)