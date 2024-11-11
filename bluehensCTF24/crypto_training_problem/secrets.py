e = 65537
N = 51328431690246050000196200646927542588629192646276628974445855970986472407007
ct = 9015202564552492364962954854291908723653545972440223723318311631007329746475


import math
import sympy
from factordb.factordb import FactorDB
from timeout_decorator import timeout

@timeout(10)
def main():
    print(f"log2(N) = {math.log2(N)}")
    print(f"is N prime? {sympy.isprime(N)}")

    f = FactorDB(N)
    f.connect()
    print(f"factors of N: {f.get_factor_list()}") # [p, q]

p = 186574907923363749257839451561965615541
q = 275108975057510790219027682719040831427



if __name__ == '__main__':
    main()
