"""Symbolic parity shells plus independent, full four-term local recurrence."""
import json
from fractions import Fraction as F
from hostile_probe import forcing, prime_power


def shell_terms(a):
    q = 3**a
    taps = {1:(7,4),4:(4,-2),5:(3,-1),6:(2,-1)}
    h = 0
    entries = []
    for ell in range(1,27):
        d = ell*(q//9)
        if d % 8 not in taps:
            continue
        e,c = taps[d % 8]
        j = (d+e)//8
        weight = F(9*c,ell)
        h = (h+pow(16,-j,27)*weight.numerator*pow(weight.denominator,-1,27)) % 27
        entries.append((j,ell,h))
    return entries


def run():
    summary = {}
    for a in [4,5]:
        entries = shell_terms(a)
        summary[str(a%2)] = [next(h for j,l,h in reversed(entries) if l<=9),
                              [(l,h) for j,l,h in entries if l>9]]
    q = 1
    a = 0
    residue = 0
    exact = F(0)
    h = 0
    entries = {}
    for n in range(1,180002):
        if 8*n >= 3*q:
            while 8*n >= 3*q:
                q *= 3
                residue = 3*residue % 27
                a += 1
            if a>=4:
                full = shell_terms(a)
                entries = {j:v for j,l,v in full}
                h = next(v for j,l,v in reversed(full) if j<=n)
        elif n in entries:
            h = entries[n]
        residue = 16*residue % 27
        for e,c in [(7,4),(4,-2),(3,-1),(2,-1)]:
            den = 8*n-e
            factor = prime_power(den,3)
            residue = (residue+c*(q//factor)*pow(den//factor,-1,27))%27
        if n<=333:
            exact=16*exact+forcing(n)
        if n>=11:
            assert h and pow(16,n,27)*h%27 == residue
            if n<=333:
                assert prime_power(exact.denominator,3) == q//prime_power(h,3)
    return {'first':11,'modular_last':180001,'fraction_last':333,'parity_shells':summary}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
