from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import getPrime, long_to_bytes
from hashlib import sha256
import random

from output import p, g, A, B, ciphertext

def bruteforce():
    temp = g

    for i in range(1, p):
        if i % (1 << 28) == 0:
            print(f"{i} / {p}")
        if temp == A:
            print("A = ")
            print(i)
        
        if temp == B:
            print("B = ")
            print(i)
        
        temp *= g
        temp %= p

# bruteforce()
a = 2766777741
b = 1913706799

C = pow(A, b, p)
assert C == pow(B, a, p)

# now use it as shared secret
hash = sha256()
hash.update(long_to_bytes(C))

key = hash.digest()[:16]
iv = b'\xc1V2\xe7\xed\xc7@8\xf9\\\xef\x80\xd7\x80L*'
cipher = AES.new(key, AES.MODE_CBC, iv)

decrypted = cipher.decrypt(pad(ciphertext, 16))
print(f'ciphertext = {decrypted}')
