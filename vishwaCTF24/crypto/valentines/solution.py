from PIL import Image
from itertools import cycle

def xor(a, b):
    return [i^j for i, j in zip(a, cycle(b))]

key = [137, 80, 78, 71, 13, 10, 26, 10]

with open("enc.txt", "rb") as f:
    text = f.read()

    with open("output.png", "wb") as f2:
        f2.write(bytearray(xor(text, key)))
