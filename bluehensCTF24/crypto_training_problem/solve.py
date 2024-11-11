from secrets import *

totient = (p-1) * (q-1)
d = pow(e, -1, totient)
m = pow(ct, d, N)

print(bytes.fromhex(hex(m)[2:]).decode())

