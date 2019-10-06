def gcd(a,b):
    while b > 0:
        old_b = b 
        b = a % b
        a = old_b
    return a 

print(gcd(13,21**12))

def reduce_fraction(a,b):
    d = gcd(a, b)
    a = a/d
    b = b/d
    return a, b
print(reduce_fraction(100,40))