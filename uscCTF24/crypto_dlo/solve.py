# Original: https://github.com/lwcM/RSA_attack/blob/master/partial_key_exposure_attack.py

from sage.all import *

def find_p_Coppersmith(n, pLow, lowerBitsNum, beta=0.5):
    x = PolynomialRing(Zmod(n), names='x').gen()
    nbits = n.bit_length()

    f = 2**lowerBitsNum*x + pLow
    f = f.monic()
    roots = f.small_roots(X=2**(nbits//2-lowerBitsNum), beta=beta)
    if roots:
        x0 = roots[0]
        p = gcd(2**lowerBitsNum*x0 + pLow, n)
        return ZZ(p)

def find_p(n, e, dLow, beta=0.5):
    X = var('X')
    lowerBitsNum = dLow.bit_length()

    for k in range(1, e+1):
        results = solve_mod([e*dLow*X - k*X*(n-X+1) + k*n == X], 2**lowerBitsNum)
        for x in results:
            pLow = ZZ(x[0])
            p = find_p_Coppersmith(n, pLow, lowerBitsNum)
            if p:
                return p

def partial_key_exposure_attack(n, e, dLow, beta=0.5):
    p = find_p(n, e, dLow, beta)
    assert p is not None and n % p == 0, 'fail'
    q = n / p
    return p, q

n = 9537465719795794225039144316914692273057528543708841063782449957642336689023241057406145879616743252508032700675419312420008008674130918587435719504215151
e = 7
dLow = int('b9b24053029f5f424adc9278c750b42b0b2a134b0a52f13676e94c01ef77', 16)

beta = 0.5

p, q = partial_key_exposure_attack(n, e, dLow, beta)
d = inverse_mod(e, (p-1)*(q-1))

print('p = ', p)
print('q = ', q)
print('d = ', d)

c = 4845609252254934006909399633004175203346101095936020726816640779203362698009821013527198357879072429290619840028341235069145901864359947818105838016519415
m = pow(c, d, n)

m = int(m)

print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))
# b"CYBORG{H0w_w3ll_d0_y0u_th1nk_d'lo_w1ll_d0_7h15_53ason??}"
