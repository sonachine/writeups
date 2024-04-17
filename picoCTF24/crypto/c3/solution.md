Solve the ciphertext to get the following program:

```py
#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1
```

And give the program itself as the input to get the flag:
`picoCTF{adlibs}`
