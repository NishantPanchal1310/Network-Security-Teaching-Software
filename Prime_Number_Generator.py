import math
from Functions_Module_WK1 import saveFilePK
 # Function to generator prime number
def gen_prime(bits):
    primes = []

    numFrom = int(2**((bits-1)/2))
    numTo = int(2**(bits/2))

    # For a number number between numFrom and numTo, it checks if there is any divisible number. If not, it is added to the prime list.
    for j in range(numFrom, numTo):
        for k in range(2, j):
            if (j % k) == 0:
                break
        else:
            primes.append(j)
            
    filename = "primes_" + str(bits) + "bits"     

    # Save file
    saveFilePK(primes, filename)