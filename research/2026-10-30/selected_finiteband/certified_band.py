"""Integer outward intervals for actual selected Fejer energies.

No supplied pi digits, floating point, FFT or mpmath is used in certificates.
The separate oracle is calibration, not the authority for these intervals.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from math import factorial
from pathlib import Path

P = 128
S = 1 << P
Interval = tuple[int, int]


def ceildiv(a, b):
    return -((-a)//b)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    v = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(v)//S, ceildiv(max(v), S)


def div(a, n):
    assert n > 0
    return a[0]//n, ceildiv(a[1], n)


def square(a):
    lo = 0 if a[0] <= 0 <= a[1] else min(a[0]**2, a[1]**2)
    return lo//S, ceildiv(max(a[0]**2, a[1]**2), S)


def fraction(a, b):
    return (a*S)//b, ceildiv(a*S, b)


def source_pair(n):
    """Combined fraction, checked separately against all four signed poles."""
    assert n >= 1
    return (120*n*n-89*n+16,
            (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def pi_interval(bits):
    """BBP: pi=sum_{n>=1}16^(1-n)r(n), positive terms."""
    count = bits//4+1
    total = 0
    for n in range(1, count+1):
        a, b = source_pair(n)
        shift = bits+4-4*n
        total += ((a << shift)//b if shift >= 0 else a//(b << -shift))
    # Each floor costs <one unit; remaining geometric tail costs <one unit.
    a, b = source_pair(count+1)
    shift = bits+4-4*count
    tail_units = Fraction(a, 15*b) * (2**shift if shift >= 0 else Fraction(1, 2**-shift))
    assert 0 < tail_units < 1
    return total, total+count+1


PI = None


def small_pi():
    global PI
    if PI is None:
        a, b = pi_interval(P+32)
        PI = a//(1 << 32), ceildiv(b, 1 << 32)
    return PI


def trig(x):
    """Return cos(2pi*x), sin(2pi*x) with exact outward rounding."""
    assert x[0] <= x[1]
    lift = (x[0]+S//2)//S
    x = x[0]-lift*S, x[1]-lift*S
    angle = mul((2*small_pi()[0], 2*small_pi()[1]), x)
    assert max(abs(angle[0]), abs(angle[1])) < 4*S
    a2 = neg(mul(angle, angle))
    tc, ts = (S, S), angle
    c, s = tc, ts
    # Through degree126 for cosine and127 for sine. Lagrange remainders
    # bounded by 4^127/127! and 4^128/128!, both less than one fixed unit.
    assert 4**127*S < factorial(127)
    for k in range(1, 64):
        tc = div(mul(tc, a2), (2*k-1)*(2*k))
        ts = div(mul(ts, a2), (2*k)*(2*k+1))
        c, s = add(c, tc), add(s, ts)
    return (c[0]-1, c[1]+1), (s[0]-1, s[1]+1)


def cmul(z, w):
    return add(mul(z[0], w[0]), neg(mul(z[1], w[1]))), add(mul(z[0], w[1]), mul(z[1], w[0]))


def unit_powers(z, count):
    """Round centers and propagate a Euclidean error disk using |true z|=1.

    Plain rectangle multiplication would amplify dependency errors needlessly.
    In fixed units E_next <= E+R+ceil(E*R/S)+2; the last two units cover
    rounding both real and imaginary coordinates of one complex product.
    """
    zr, zi = (z[0][0]+z[0][1])//2, (z[1][0]+z[1][1])//2
    R = max(zr-z[0][0], z[0][1]-zr)+max(zi-z[1][0], z[1][1]-zi)
    pr, pi, E = S, 0, 0
    for _ in range(1, count):
        pr, pi = (pr*zr-pi*zi)//S, (pr*zi+pi*zr)//S
        E = E+R+ceildiv(E*R, S)+2
        yield (pr-E, pr+E), (pi-E, pi+E)


def tail_interval(n, terms=40):
    lo = 0
    hi = 0
    for j in range(1, terms+1):
        a, b = source_pair(n+j)
        t = fraction(a, b*16**j)
        lo += t[0]
        hi += t[1]
    a, b = source_pair(n+terms+1)
    hi += ceildiv(S*a, 15*b*16**terms)
    return lo, hi


def selected_intervals(N, mode="original"):
    bits = 4*N+P+64
    lo, hi = pi_interval(bits)
    for n in range(1, N+1):
        shift = bits-4*(n-1)-P
        yl, yu = lo >> shift, ceildiv(hi, 1 << shift)
        yl, yu = yl % S, yl % S + yu-yl
        if mode == "coherent":
            yl, yu = 0, 0
        elif mode == "periodic01":
            yl, yu = fraction(pow(16, n-1, 255), 255)
        elif mode != "original":
            raise ValueError(mode)
        t = tail_interval(n)
        yield n, (yl-t[1], yu-t[0])


def decimal_out(x, lower, digits=12):
    u = x*10**digits
    integer = u//S if lower else ceildiv(u, S)
    sign = "-" if integer < 0 else ""
    a = abs(integer)
    return f"{sign}{a//10**digits}.{a%10**digits:0{digits}d}"


def energies(horizons, bands, mode="original"):
    horizons, bands = sorted(set(horizons)), sorted(set(bands))
    assert horizons[0] > 0 and bands[0] >= 2
    hmax = max(bands)
    sums = [((0, 0), (0, 0)) for _ in range(hmax)]
    rows = []
    for n, x in selected_intervals(max(horizons), mode):
        z = trig(x)
        for h, power in enumerate(unit_powers(z, hmax), 1):
            sums[h] = add(sums[h][0], power[0]), add(sums[h][1], power[1])
        if n in horizons:
            for H in bands:
                value = (S, S)
                for h in range(1, H):
                    mag2 = add(square(sums[h][0]), square(sums[h][1]))
                    weighted = (2*(H-h)*mag2[0], 2*(H-h)*mag2[1])
                    value = add(value, div(weighted, H*n*n))
                rows.append({"N":n,"H":H,"mode":mode,
                             "lower":decimal_out(value[0], True),
                             "upper":decimal_out(value[1], False),
                             "dyadic_lower":str(value[0]),"dyadic_upper":str(value[1]),
                             "denominator_power_two":P})
    return rows


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--horizons",nargs="+",type=int,default=[256,1024,4096])
    p.add_argument("--bands",nargs="+",type=int,default=[8,128,512])
    p.add_argument("--mode",default="original",choices=["original","coherent","periodic01"])
    p.add_argument("--output",required=True)
    a=p.parse_args()
    result={"status":"CERTIFIED FINITE ONLY","method":"outward integer Taylor intervals; positive BBP pi enclosure and Green tail",
            "code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "rows":energies(a.horizons,a.bands,a.mode)}
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
