## Credit: Nishant Panchal coded this!
## Credit: Maths behind it was provided by this video: https://www.youtube.com/watch?v=oOcTVTpUsPQ

import random
from math import gcd

primeNumberList = []

for r in range(0,65536):
    if r > 1:  
        print(r)
        for s in range(2,r):  
            if (r % s) == 0:  
                break  
        else:  
            primeNumberList.append(r)

    print(primeNumberList)
    


p = random.choice(primeNumberList)
q = random.choice(primeNumberList)

print(f"p = {p}\nq = {q}")

n = p*q

print(n)

PhiFuction = (p-1)*(q-1)

print(PhiFuction)

condition1Values = []

eValues = []

for t in range(2, PhiFuction + 1):
    condition1Values.append(t)
    
for value in condition1Values:
    if gcd(n, value) == 1 and gcd(PhiFuction, value) == 1:
        eValues.append(value)

e = random.choice(eValues)
print(e)

randomNumber = random.randrange(0, 100)

for u in range(1, PhiFuction + 1):
    if (e*u)%PhiFuction == 1:
        nthNumber = u
        break

d = randomNumber*PhiFuction + nthNumber

print(d)