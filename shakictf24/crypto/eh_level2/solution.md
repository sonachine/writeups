```py
from output import h

h2  = []

for by in h:
    h2.append(by % 1024)

print(h2)

for n in range(256):
    st = ""
    for x in h2:
        st += chr(x ^ n)
    
    print("n = ", n, " st = ", st)

print("REAL N = ", h[0] - h[0] % 1024 + 101)
```


`n =  101  st =  The e = 46307 :)`

`REAL N =  94679407488132818404660699098842374931489424397235444032237590365827255722083367058700051514705537574410165711179896056841523082769989050948432027496868754650692929646830509011686345739543788335116663878603193093822729085523727432834299509271223474277629700801997533152872965865087117035426980349126297961573`


```py
from output import ct
import sys
e = 46307
n = 94679407488132818404660699098842374931489424397235444032237590365827255722083367058700051514705537574410165711179896056841523082769989050948432027496868754650692929646830509011686345739543788335116663878603193093822729085523727432834299509271223474277629700801997533152872965865087117035426980349126297961573

d = pow(e, -1, n-1)

m = pow(ct, d, n)

bytestr = m.to_bytes(1024, sys.byteorder)
byte_array = bytearray(bytestr)

# print(byte_array)

startswithzero = True

ls = []

for byte in reversed(byte_array):
    if byte == 0 and startswithzero:
        continue
    startswithzero = False
    
    # print(byte, end=" ")
    ls.append(byte)
    
for n2 in range(256):
    st = ""
    for x in ls:
        st += chr(x ^ n2)
    
    print("n2 = ", n2, " st = ", st)
```

I suspected that `n` was not prime, but the traditional `p`*`q` value, so I had to change a line from the script above.

I changed the `d = pow(e, -1, n-1)` line into this:

```py
from output import p, q
d = pow(e, -1, (p-1)*(q-1))
```

And it gave me the flag.
