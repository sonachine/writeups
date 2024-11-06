# original: https://stackoverflow.com/a/6752874/9260807
# assumes p is prime
# returns the cube root of a mod p
def cuberoot(a, p):
    if p == 2:
        return a
    if p == 3:
        return a
    if (p%3) == 2:
        assert (2*p - 1) % 3 == 0
        return pow(a,(2*p - 1)//3, p)
    if (p%9) == 4:
        assert (2*p + 1) % 9 == 0
        root = pow(a,(2*p + 1)//9, p)
        
        if pow(root,3,p) == a%p:
            return root
        else:
            return None
    if (p%9) == 7:
        assert (p + 2) % 9 == 0
        root = pow(a,(p + 2)//9, p)
        
        if pow(root,3,p) == a%p:
            return root
        else:
            return None
    else:
        print("Not implemented yet. See the second paper")

a = 6
p = 7
root = cuberoot(a, p)

if root is None:
    print("No cube root found")
else:
    if pow(root,3,p) == a%p:
        print(f"Cube root of {a} mod {p} is {root}")
    else:
        print("Something went wrong")
