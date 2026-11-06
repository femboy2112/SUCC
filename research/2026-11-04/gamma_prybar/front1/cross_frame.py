from fractions import Fraction as F
from math import gcd, prod
import json
from cofactor_probe import four_poles, primes_up_to


def angular(n):
    taps = [2,2,1,0,F(-1,2),F(-1,2),F(-1,4),0]
    return sum((F(w,8*(n-1)+j) for j,w in enumerate(taps,1)),F(0))


def angular_poly(n):
    num = 30720*n**5-63232*n**4+45792*n**3-13892*n**2+1641*n-48
    den = (4*n-3)*(4*n-1)*(8*n-7)*(8*n-5)*(8*n-3)*(8*n-1)
    return F(num,den)


def probe(A):
    U=Y=F(0)
    for n in range(1,A+1):
        b=angular(n)
        assert b==angular_poly(n)
        U,Y=16*U+four_poles(n),16*Y+b
    primes=[p for p in primes_up_to(8*A-11) if p>4*A and p%8==5]
    H=prod(primes)
    hits=[]
    for s in [F(0),F(1,H),F(1,primes[0]),F(1,primes[0]*primes[1]),F(2,H)]:
        Us,Ys=U+16**A*s,Y+16**A*s
        assert Ys-Us==Y-U
        observed=gcd((2*Ys-Us).denominator,H)
        assert observed==s.denominator
        hits.append(observed.bit_length())
    assert gcd((3*Y-U).denominator,H)==H
    return {"A":A,"S_size":len(primes),"mixed_denominator_gcd_bits":hits,
            "incorrect_coefficient_surviving_primes":len(primes)}


if __name__=="__main__":
    print(json.dumps([probe(A) for A in [157,293,503]], indent=2))
