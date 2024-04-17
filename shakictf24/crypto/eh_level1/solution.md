The hint is XOR'ed byte-by-byte with a secret `b` value.
I seperated the hint into bytes and gave it to `cyberchef`, made it bruteforce the b.

`b = 0x3b`
The hint: `The e = 79400+(the single byte that was xored) :)`
`e = 79549`

```py
from output import p, q, ct
import sys

e = 79459
n = (p-1)*(q-1)
print("n = ", n)

d = pow(e, -1, n)
print("d = ", d)

m = pow(ct, d, p*q)
print("m = ", m)

bytestr = m.to_bytes(1024, sys.byteorder)
byte_array = bytearray(bytestr)

print(byte_array)
```

`d =  83816041327437334058748126743415262110841023198066302167837351030768514357090560328417035537847021044863281018168981580418538594427863188881057338194448147212010147731155071091342811722712540340670547740944981279767015297805638341951499842385250509395424842603575240972511892552474428010178479297491118806139`
`Here is your reward '\vvrkxuqgi{r0i43m0r_f0_hu3_u3gtu3!!!}'\ You can ask '\Doraemon'\ to help you with this. Bye!!`

Used vignette cipher and got the flag:
`shaktictf{d0r43m0n_t0_th3_r3scu3!!!}`
