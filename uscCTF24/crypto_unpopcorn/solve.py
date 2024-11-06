m = 57983


def p_bruteforce():
    encrypted_C = 21038
    
    for p in range(0, m):
        if (ord('C') ^ 42) * p % m == encrypted_C:
            return p


p = p_bruteforce()
print(f"p = {p}")


def unpop(s):
    return map(lambda x: chr(x^42), s)


def unbutter(s):
    rev = {}
    
    for ch in range(0, 256):
        processed = ch * p % m
        rev[processed] = ch
    
    return map(lambda x: rev[x], s)


def unchurn(s):
    l = s.split(" ")
    l2 = list(map(lambda x: int(x, 16), l))
    l3 = l2[-16:] + l2[:-16]
    l4 = list(map(lambda x: x >> 3, l3))
    return l4


message = open("message.txt").read().strip()

reversed_message = "".join(unpop(unbutter(unchurn(message))))
print(f"flag: {reversed_message}")

flag = open("flag.txt", "w")
flag.write(reversed_message)
flag.close()
