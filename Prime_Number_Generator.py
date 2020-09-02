import math
from Functions_Module_WK1 import saveFilePK

def gen_prime(bits):
    primes = []

    numFrom = int(2**((bits-1)/2))
    numTo = int(2**(bits/2))

    for j in range(numFrom, numTo):
        for k in range(2, j):
            if (j % k) == 0:
                break
        else:
            primes.append(j)
            
    filename = "primes_" + str(bits) + "bits"     

    saveFilePK(primes, filename)