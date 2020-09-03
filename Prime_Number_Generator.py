import math
from Functions_Module_WK1 import saveFilePK

#This function basically generates prime numbers for the RSA key generation
def gen_prime(bits):
    primes = []
    
    #Creates numFrom and numTo, which are used in the for loop to test for prime numbers
    numFrom = int(2**((bits-1)/2))
    numTo = int(2**(bits/2))
    
    #Checks j in the range of numFrom and numTo and checks if it is divisible.
    for j in range(numFrom, numTo):
        for k in range(2, j):
            if (j % k) == 0:
                break
        
        #When not divisible, j is a prime number and is appended to the primes list for use.
        else:
            primes.append(j)
     
    # generates filename for prime numbers to be saved to.
    filename = "primes_" + str(bits) + "bits"     
    #saves the list of prime numbers to a file 
    saveFilePK(primes, filename)
