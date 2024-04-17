from random import randint
import sys


def generator(g, x, p):
    return pow(g, x) % p

def decrypt(cipher_list, key):
    plaintext = ""

    for number in cipher_list:
        assert number % (key * 311) == 0
        plaintext += chr((number // key) // 311)
    
    return plaintext


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True

def dynamic_xor_decrypt(semi_cipher, text_key):
    plaintext = ""
    key_length = len(text_key)
    for i, char in enumerate(semi_cipher):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plaintext += decrypted_char
    return plaintext


def solve(cipher_list, text_key, a, b):
    p = 97
    g = 31
    
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    
    semi_cipher = decrypt(cipher_list, shared_key)
    plaintext = dynamic_xor_decrypt(semi_cipher, text_key)
    print(f'plaintext is: {plaintext}')



if __name__ == "__main__":
    from output import a, b, cipher
    solve(cipher, "trudeau", a, b)
