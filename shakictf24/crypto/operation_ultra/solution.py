# 0 1 4 5 8 9 ...28 29 2 3 6 7 10 11 ... 30 31
unk_arr3 = [32, 0, 27, 30, 84, 79, 86, 22, 97, 100, 63, 95, 60, 34, 1, 71, 0, 15, 81, 68, 6, 4, 91, 40, 87, 0, 9, 59, 81, 83, 102, 21]

unk_str = [""] * 32

cnt = 0
pos = 0

while cnt < 16:
    unk_str[pos] = chr(unk_arr3[cnt])
    unk_str[pos + 1] = chr(unk_arr3[cnt + 1])
    pos += 4
    cnt += 2

pos = 0

while cnt < 32:
    unk_str[pos + 2] = chr(unk_arr3[cnt])
    unk_str[pos + 3] = chr(unk_arr3[cnt + 1])
    pos += 4
    cnt += 2

print("".join(unk_str))

XORST = "Shadow2024"

for i in range(32):
    unk_str[i] = chr(ord(unk_str[i]) ^ ord(XORST[i % len(XORST)]))

print("".join(unk_str))
