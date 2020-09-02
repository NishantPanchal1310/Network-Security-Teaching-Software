## Credit: Nishant Panchal coded this!
## Credit: Maths behind it was provided by this video: https://www.youtube.com/watch?v=oOcTVTpUsPQ

import random
from math import gcd
from Functions_Module import readFilePK
import time


bits = 100
while int(bits) != 16:
    bits = input("Enter amount bits of RSA keys: ")

filename = "primes_" + str(bits) + "bits" 

primeNumberList = readFilePK(filename)

p = random.choice(primeNumberList)
q = random.choice(primeNumberList)

print(f"p = {p}\nq = {q}")

n = p*q

print(f"n = {n}")

PhiFunction = (p-1)*(q-1)

print(f"Phi Function = {PhiFunction}")

conditionValues = []

eValues = []

print("Print evalues")
for t in range(int(PhiFunction/2), PhiFunction + 1):
    if gcd(n, t) == 1 and gcd(PhiFunction, t) == 1:
        eValues.append(t)
    

e = random.choice(eValues)
print(f"e = {e}")

randomNumber = random.randrange(0, 65536)

for u in range(1, PhiFunction + 1):
    if (e*u)%PhiFunction == 1:
        nthNumber = u
        break

d = randomNumber*PhiFunction + nthNumber

print(f"d = {d}")

