from output import n, e, c
import sys

d = pow(e, -1, (n-1))
m = pow(c, d, n)

print(m)

bytestr = m.to_bytes(1024, sys.byteorder)
byte_array = bytearray(bytestr)

startswithzero = True

ls = []

for byte in reversed(byte_array):
    if byte == 0 and startswithzero:
        continue
    startswithzero = False
    
    ls.append(byte)
    
[print(chr(x), end="") for x in ls]
