We can see that the first 8 bytes of the file "original.png" are used as the key that encrypts the file.
The encryption method is simple, every byte (e.g. n-th byte) is xor'ed with the [n % 8]th byte of the key.

The xor operation has a simple property:

a XOR b = c  ==> a XOR b XOR b = c XOR b ==> a = c XOR b

Which means that if we somehow get the key and use the key to xor the output, we should get the input (which means decrypting).

How do we get the key? The hint is in the file extension: ".png".

PNG file format denotes that the first 8 bytes of a png file must be [137, 80, 78, 71, 13, 10, 26, 10] (source: http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html)

So we simply use those values as the key and apply the same operation on the encrypted file. This gives us a picture that has the flag.
