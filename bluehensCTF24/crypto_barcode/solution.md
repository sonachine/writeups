The barcodes are missing something, but what?

After googling for 11 digit barcode standarts, the first result is the one needed: [UPC](https://en.wikipedia.org/wiki/Universal_Product_Code).

UPC uses 12 digits, but the last one is used for checksum. Sounds familiar? The checksums are missing.

Simply calculate the checksum digit (0-9) for each barcode. For the barcodes in the same list, concatanate the digits ([9, 7] => 97).

`UDCTF{b4rc0d3s_c4n_b3_fun_t00}`
