## Credit: Nishant Panchal coded this!
## Credit: Maths behind it was provided by this video: https://www.youtube.com/watch?v=oOcTVTpUsPQ

import random
from math import gcd
from Functions_Module_WK1 import readFilePK
import time

#Algorithm to generate keys manually using prime numbers
def generate_key_with_custom_RSA_alogrithm(bits):
    
    #opens and reads a file containing all of the prime numbers.
    filename = "primes_" + str(bits) + "bits" 
    primeNumberList = readFilePK(filename)

    # Random prime numbers from prime file
    p = random.choice(primeNumberList)
    q = random.choice(primeNumberList)

    # gets the n value
    n = p*q
    PhiFunction = (p-1)*(q-1)
    conditionValues = []
    eValues = []
    
    #generating the possible values for e.
    for t in range(2, PhiFunction + 1):
        conditionValues.append(t)
        
    for values in conditionValues:
        if (gcd(n, values) == 1) and (gcd(PhiFunction, values) == 1):
            eValues.append(values)
        
    # Choices a random e value from eValues list
    e = random.choice(eValues)


    randomNumber = random.randrange(0, 10)
    

    for u in range(1, PhiFunction + 1):
        if (e*u)%PhiFunction == 1:
            nthNumber = u
            break
 
    d = randomNumber*PhiFunction + nthNumber
    
    #Return keys as tuple: (e,d,n)
    return e, d, n

if __name__ == "__main__":
    generate_key_with_custom_RSA_alogrithm(16)