import sys

m1 = 6053758479463965567
m2 = 7495220422968891654
m3 = 3983999411754849384
m4 = 22790

def fun(m):
    bytestr = m.to_bytes(1024, sys.byteorder)
    byte_array = bytearray(bytestr)

    startswithzero = True

    ls = []

    for byte in reversed(byte_array):
        if byte == 0 and startswithzero:
            continue
        startswithzero = False
        
        byte ^= 55

        ls.append(byte)
        
    [print(chr(x), end="") for x in reversed(ls)]

fun(m1)
fun(m2)
fun(m3)
fun(m4)
