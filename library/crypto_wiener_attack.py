# LOW PRIVATE EXPONENT (d)
# WIENER ATTACK
# q < p < 2q
# d < (1/3) * N^(1/4)

from math import floor, gcd
from fractions import Fraction

# n = 9537465719795794225039144316914692273057528543708841063782449957642336689023241057406145879616743252508032700675419312420008008674130918587435719504215151
# e = 7

FRACTION_LENGTH = 100000

a = []
r = Fraction(e, n)

whole_part = r.numerator // r.denominator
a.append(whole_part)

r -= whole_part 
r = 1 / r

for i in range(1, FRACTION_LENGTH):
    whole_part = r.numerator // r.denominator
    a.append(whole_part)
    
    r -= whole_part
    
    if r == 0:
        break
    
    r = 1 / r

print(f"a = {a}")

convergents = []
convergents.append((a[0], 1))
convergents.append((a[0] * a[1] + 1, a[1]))

for i in range(2, len(a)):
    convergents.append((a[i] * convergents[-1][0] + convergents[-2][0], a[i] * convergents[-1][1] + convergents[-2][1]))

print(f"convergents = {convergents}")

for k, d in convergents:
    print(f"k = {k}, d = {d}")
    
    assert gcd(k, d) == 1
    
    if k == 0:
        print("k == 0")
        continue
    
    if d % 2 != 1:
        print("d is not odd")
        continue
    
    if (e * d) % k != 1:
        print("ed % k != 1")
        continue
    
    totient = (e * d - 1) // k
    
    a = 1
    b = n - totient + 1
    c = n
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("delta < 0")
        continue
    
    if delta == 0:
        print("delta == 0")
        continue
    
    sqrt_delta = floor(delta**0.5)
    
    x1 = (-b + sqrt_delta) // (2*a)
    x2 = (-b - sqrt_delta) // (2*a)
    
    print(f"x1 = {x1}, x2 = {x2}")
    # if x1 and x2 are integers, then we have found the factors of n
