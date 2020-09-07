import math
from Functions_Module_WK1 import saveFilePK
 # Function to generator prime number
def gen_prime(bits):
    primes = []
    
    #Creates numFrom and numTo, which are used in the for loop to test for prime numbers
    numFrom = int(2**((bits-1)/2))
    numTo = int(2**(bits/2))

    # For a number number between numFrom and numTo, it checks if there is any divisible number. If not, it is added to the prime list.
    for j in range(numFrom, numTo):
        for k in range(2, j):
            if (j % k) == 0:
                break
        
        #When not divisible, j is a prime number and is appended to the primes list for use.
        else:
            primes.append(j)
     
    # generates filename for prime numbers to be saved to.
    filename = "primes_" + str(bits) + "bits"     

    # Save file
    saveFilePK(primes, filename)
