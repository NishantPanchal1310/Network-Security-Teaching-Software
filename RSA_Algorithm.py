## Credit: Nishant Panchal coded this!
## Credit: Maths behind it was provided by this video: https://www.youtube.com/watch?v=oOcTVTpUsPQ

import random
from math import gcd
from Functions_Module_WK1 import readFilePK
import time

#Algorithm to generate keys manually using prime numbers
def generate_key_with_custom_RSA_alogrithm(bits):
    filename = "primes_" + str(bits) + "bits" 

    primeNumberList = readFilePK(filename)

    p = random.choice(primeNumberList)
    q = random.choice(primeNumberList)

    n = p*q

    PhiFunction = (p-1)*(q-1)

    conditionValues = []

    eValues = []

    for t in range(2, PhiFunction + 1):
        conditionValues.append(t)
        
    for values in conditionValues:
        if (gcd(n, values) == 1) and (gcd(PhiFunction, values) == 1):
            eValues.append(values)
        

    e = random.choice(eValues)

    randomNumber = random.randrange(0, 10)

    for u in range(1, PhiFunction + 1):
        if (e*u)%PhiFunction == 1:
            nthNumber = u
            break

    d = randomNumber*PhiFunction + nthNumber
    
    return e, d, n

