"""Certify the two-moment inequality with independent alternating rational brackets."""
from fractions import Fraction as Q
from math import comb
import json


def harmonic(n):
    return sum((Q(1, k) for k in range(1, n+1)), Q())


def enclose(n, last=4):
    m = 8*n
    # M_j = E[x^(2j)] for Beta(1,m+1).  Successive odd/even partial
    # sums below/above 1/(1+x^2) also bound its product with -log x.
    denom, numer = Q(), Q()
    for j in range(last+1):
        k = 2*j
        moment = Q(1, comb(m+k+1, k))
        denom += (-1)**j * moment
        numer += (-1)**j * moment * (harmonic(m+k+1)-harmonic(k))
        if j == last-1:
            low_denom, low_numer = denom, numer
    low = low_numer/denom-harmonic(m+1)
    high = numer/low_denom-harmonic(m+1)
    assert 0 < low < high < Q(3,(m+2)*(m+3)-2)
    # delta_N(1) < 16^(-N)/(m+1); altered seed 1/5 subtracts 4/5.
    assert Q(1,16**n*(m+1)) - Q(4,5) < 0
    return {"blocks": n, "scaled_lower":str(low*m*m), "scaled_upper":str(high*m*m)}


if __name__ == "__main__":
    print(json.dumps([enclose(n) for n in (2,7,20,38)], indent=2))
