from secrets import barcodes

def checksum(barcode):
    barcode = str(barcode)
    sum = 0

    for i in range(len(barcode)):
        if i % 2 == 0:
            sum += 3 * int(barcode[i])
        else:
            sum += int(barcode[i])
    
    sum %= 10

    return 10 - sum if sum != 0 else 0


numbers = []

for barcode_list in barcodes:
    number = 0

    for barcode in barcode_list:
        number *= 10
        number += checksum(barcode)
    
    numbers.append(number)

print(bytes(numbers).decode())
