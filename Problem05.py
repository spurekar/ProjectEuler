import fractions
import functools

def lcm(a,b):
    return a*b//fractions.gcd(a,b)

print(functools.reduce(lcm,range(1,20+1)))
