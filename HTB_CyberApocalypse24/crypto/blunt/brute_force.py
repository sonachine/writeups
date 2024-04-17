from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import getPrime, long_to_bytes
from hashlib import sha256


import random


from output import p, g, A, B

temp = g

for i in range(1, p):
    if i % (1 << 28) == 0:
        print(f"{i} / {p}")
    if temp == A:
        print("a = ")
        print(i)
    
    if temp == B:
        print("b = ")
        print(i)
    
    temp *= g
    temp %= p
