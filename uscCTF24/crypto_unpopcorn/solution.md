We need to reverse each operation but don't know the value of p.

Let's break each operation into steps:

# 1 - Pop

- Input: char list (assumed because of the `ord` function)
- Process: each value is XOR'ed by a constant (42)
- Output: int list
- Notes: pretty easy to reverse, just XOR by 42 again
- - [(A XOR B) XOR B == A XOR (B XOR B) == A XOR 0 == A]

# 2 - Butter

- Input: int list (assumed because of the arithmetic operators)
- Process: each value is multiplied by p modulo m
- Output: int list
- Notes: if p is known, we could calculate easily create a brute force table
- - table = [ (x*p modulo m) for x in range(0, 256) ]
- - y = table[x] ===> reversed(y) = x
- - But we don't know p yet.

# 3 - Churn

- Input: int list (assumed because of the arithmetic operations)
- Process: multiply each value by 8, cut the first 16 values and paste them at the end of the list, convert each value to hex
- Output: space seperated hex values
- Notes: altough abstruse, easy to reverse. convert each hex value to int, reorder the list, divide each value by 8

The order of the operations applied is: 1, 2, 3.

In order to reverse, we must start with the message.txt and go through reversed 3, 2 and 1.

Reversed churn (unchurn) is simple enough:

```py
def unchurn(s):
    l = s.split(" ")
    l2 = list(map(lambda x: int(x, 16), l))
    l3 = l2[-16:] + l2[:-16]
    l4 = list(map(lambda x: x >> 3, l3))
    return l4
```

We now have an int list ([21038, ...]), but because we don't know p we can't reverse butter, right?

Luckily we can find p, because we know what the first character of the flag is.

This CTF's flag format is `CYBORG{...}` so the first int value (21038) is the popped and buttered version of `'C'`.

So why don't we search for p values and check which value gets us 21038?

(The modular arithmetic proof of how p is bounded between 0 and m-1 is left as an exercise)

```py
def p_bruteforce():
    encrypted_C = 21038
    
    for p in range(0, m):
        if (ord('C') ^ 42) * p % m == encrypted_C:
            return p

p = p_bruteforce()
```

And we get `p = 24498`.

Now we can reverse butter by constructing the lookup table:

```py
def unbutter(s):
    rev = {}
    
    for ch in range(0, 256):
        processed = ch * p % m
        rev[processed] = ch
    
    return map(lambda x: rev[x], s)
```

Reversing pop is trivial:

```py
def unpop(s):
    return map(lambda x: chr(x^42), s)
```

The full code is in `solve.py`
