Random Oracle (https://en.wikipedia.org/wiki/Random_oracle):

A black box, answers a truly random string deterministically for the given input.


I try to get the exponent "d". For this, I will attempt to make the oracle give me the smallest output possible (bigger than 1). The intuition behind this is, the smallest output is likely to be smaller than "n" itself, and so we could do "output^-d" to get 1. In other words, we could brute force the d.

I used the command:

`python3 -c "print(chr(0x2) + '\n')" | xclip -selection clipboard`

And tried this input but it failed, as the oracle only expects integers to decrypt.

So I tried giving it "2" and it worked:

```
*****************************************
****************THE ORACLE***************
*****************************************
what should we do for you? 
E --> encrypt D --> decrypt. 
D
Enter text to decrypt: 2
decrypted ciphertext as hex (c ^ d mod n): 252925ecd8a1a846840a390fbd000e256b1a53209e06399aca8a4df809739870244afe334ac8692e6b561da7041f7a32e6134df11f764b14b9d535dcbe64a9fa
decrypted ciphertext: %)%ìØ¡¨F

9½%k�S Mø	s
```

I closed the connection and tried again and got the same result. The "d" and "n" values are constant between sessions.

Next, I converted the decrypted text from hex to decimal and then used log2 on it.

But it failed, as the output was already bigger than "n" and got modded:

```
$ echo "252925ecd8a1a846840a390fbd000e256b1a53209e06399aca8a4df809739870244afe334ac8692e6b561da7041f7a32e6134df11f764b14b9d535dcbe64a9fa" | python3 -c "import math; print(math.log2(int(input(), 16)))"
509.2157071296319
```

I switched my focus to encryption and tried the same aproach:

```
$ python3 -c "print('E\n' + chr(2) + '\n')" | nc titan.picoctf.net 57853
*****************************************
****************THE ORACLE***************
*****************************************
what should we do for you? 
E --> encrypt D --> decrypt. 
enter text to encrypt (encoded length must be less than keysize): 

encoded cleartext as Hex m: 2

ciphertext (m ^ e mod n) 5067313465613043651275429665315895824157755779222372979446076012356324498190828210335763979330272318657269048435311897896433721115606764442199497891219230
```

```
$ echo "5067313465613043651275429665315895824157755779222372979446076012356324498190828210335763979330272318657269048435311897896433721115606764442199497891219230" | python3 -c "import math; print(math.log2(int(input())))"
510.5962195949587
```

And failed again.

Tried giving -1 as the input [(-1 mod n) == (n-1 mod n)]:

```
what should we do for you? 
E --> encrypt D --> decrypt. 
D
Enter text to decrypt: -1
decrypted ciphertext as hex (c ^ d mod n): 692894990b08e3148106c90ccf5fffe4a0a81180fb048cf38e363850acd6a6ba62bd5bd2415cf84d2f4471399da695f24fac315fb42586ea124db6b6b076db12
decrypted ciphertext: i(
                       ãÉ
                         Ï_ÿä ¨ûó68P¬Ö¦ºb½[ÒA\øM/Dq9òO¬1_´%êM¶¶°vÛ
```

```
$ echo "692894990b08e3148106c90ccf5fffe4a0a81180fb048cf38e363850acd6a6ba62bd5bd2415cf84d2f4471399da695f24fac315fb42586ea124db6b6b076db12" | python3 -c "print(int(input(), 16)+1)"
5507598452356422225755194020880876452588463543445995226287547479009566151786764261801368190219042978883834809435145954028371516656752643743433517325277971
```

We most likely got the "n".

```
what should we do for you? 
E --> encrypt D --> decrypt. 
d
Enter text to decrypt: 5507598452356422225755194020880876452588463543445995226287547479009566151786764261801368190219042978883834809435145954028371516656752643743433517325277971
decrypted ciphertext as hex (c ^ d mod n): 0
decrypted ciphertext: 
```

Yup. This is the n.

n=5507598452356422225755194020880876452588463543445995226287547479009566151786764261801368190219042978883834809435145954028371516656752643743433517325277971


# The Second Part

The encrypted password is even. Let's call it c=2k.

Decrypted password = c^d mod n = (2k)^d mod n = (2^d)*(k^d) mod n = ((2^d mod n) * (k^d mod n)) mod n

Oracle can calculate (2^d mod n) and (k^d mod n)

```
2^d mod n:
1946265611883852059229177938924673620335830398278788862485815325238212887269295665437679235190806256855682977637538255090519491523139135273135228070439418

k^d mod n:
(as hex):
851f4df4fc0e814b94ddaa7f9ccc3d4a8771cd44b4a24568e0cfb66cc5a1b03d1ca40ad1d8d12c6824559311929d56456975777b684d8f2af49221c040c2763
(as decimal):
435761231787095059057124135912316761352568142716880007932025177274153372743650096589808618432620925797430492979718325246381664905275459237363513299838819

c^d mod n = 431127279929

431127279929 ==> "da099"
```

```
what should we do for you? 
E --> encrypt D --> decrypt. 
E
enter text to encrypt (encoded length must be less than keysize): da099
da099

encoded cleartext as Hex m: 6461303939

ciphertext (m ^ e mod n) 4228273471152570993857755209040611143227336245190875847649142807501848960847851973658239485570030833999780269457000091948785164374915942471027917017922546
```

ciphertext is the same as the given ciphertext. We got the password: da099

All that is left to do is to decrypt the secret.enc:

```
$ openssl enc -aes-256-cbc -d -in secret.enc 
enter AES-256-CBC decryption password:
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
picoCTF{su((3ss_(r@ck1ng_r3@_da099d93}
```
