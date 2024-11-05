# D' Lo

We need to execute a RSA attack.

## What do we know?

- e = 7, small.
- the least significant 60 bytes of private key (d)

## What can we do?

After searching for partial key exposure attacks, more spesifically searching for the case when some of the LSB's of d is known, we find papers written about such an attack:
- http://honors.cs.umd.edu/reports/lowexprsa.pdf
- https://www.utc.edu/sites/default/files/2021-04/course-paper-5600-rsa.pdf
- https://www.ams.org/notices/199902/boneh.pdf

## Next steps

I first tried to implement the attack myself, but found the math to be quite challenging. Also, the math required me to use some library (for ring theory) so I opted for pre written implementations online.

This implementation works (written for python 2, had to port to python 3): [https://github.com/lwcM/RSA_attack](https://github.com/lwcM/RSA_attack/blob/master/partial_key_exposure_attack.py)

The modified script (with the plugged in values) is solve.py
