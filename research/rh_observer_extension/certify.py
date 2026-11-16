#!/usr/bin/env python3
"""Exact rational certificates; standard library only, no zeta-zero inputs.

The optional floating proposer is not part of this verifier's trust boundary.
See RESEARCH.md for the periodic-tail proof and the scope of each certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from math import gcd, lcm
import json
from pathlib import Path


def coefficients(raw: dict[str, str]) -> dict[int, F]:
    """Parse canonical decimal index strings and exact rational values."""
    out = {}
    for key, value in raw.items():
        k = int(key)
        if str(k) != key or k < 2 or not isinstance(value, str):
            raise ValueError('Indices must be canonical integers >=2; values rational strings')
        c = F(value)
        if c:
            out[k] = c
    return out


def mobius(n: int) -> int:
    if not isinstance(n, int) or n < 1:
        raise ValueError('n must be a positive integer')
    value, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
        p += 1
    return -value if n > 1 else value


def value_at(c: dict[int, F], n: int) -> F:
    return sum((v * F(n % k, k) for k, v in c.items()), F())


def prefix_direct(c: dict[int, F], n: int) -> bool:
    return all(value_at(c, j) == 1 for j in range(1, n+1))


def prefix_mobius(c: dict[int, F], n: int) -> bool:
    return (sum((v/k for k, v in c.items()), F()) == 1
            and all(c.get(k, F()) == -mobius(k) for k in range(2, n+1)))


def pair_mean(k: int, ell: int) -> F:
    d = gcd(k, ell)
    return F(3*(k-1)*(ell-1) + d*d-1, 12*k*ell)


def integer_model(c: dict[int, F]) -> tuple[int, list[tuple[int, int]]]:
    """f(n)=sum b_k*(n mod k)/D exactly."""
    a = [(k, v/k) for k, v in sorted(c.items()) if v]
    D = lcm(*(v.denominator for _, v in a)) if a else 1
    return D, [(k, int(v*D)) for k, v in a]


def tail_constants(c: dict[int, F]) -> tuple[F, F, F]:
    """Exact period mean Q, Abel discrepancy bound C, and pointwise bound B."""
    D, terms = integer_model(c)
    qnum = cnum = 0
    for k, b in terms:
        for ell, d in terms:
            g = gcd(k, ell)
            qnum += b*d*(3*(k-1)*(ell-1) + g*g-1)
            cnum += abs(b*d)*k*ell*lcm(k, ell)
    Q, C = F(qnum, 12*D*D), F(cnum, 4*D*D)
    B = F(sum(abs(b)*k for k, b in terms), D)
    if not 0 <= Q <= B*B:
        raise ArithmeticError('Invalid mean-square bound')
    return Q, C, B


def norm_interval(c: dict[int, F], cutoff: int = 10000, bits: int = 80,
                  target: dict[int, F] | None = None) -> tuple[F, F]:
    """Enclose ||f-target||^2; target has finite support, cutoff covers it."""
    if type(cutoff) is not int or cutoff < 1 or type(bits) is not int or bits < 1:
        raise ValueError('cutoff and bits must be positive integers')
    target = target or {}
    if any(type(n) is not int or not 1 <= n <= cutoff for n in target):
        raise ValueError('target support must be within 1..cutoff')
    D, terms = integer_model(c)
    scale = 1 << bits
    floor_sum = 0
    for n in range(1, cutoff+1):
        num = sum(b*(n % k) for k, b in terms)
        if n in target:
            x = F(num, D)-target[n]
            floor_sum += (x.numerator*x.numerator*scale)//(
                x.denominator*x.denominator*n*(n+1))
        else:
            floor_sum += (num*num*scale)//(D*D*n*(n+1))
    Q, C, B = tail_constants(c)
    center = Q/(cutoff+1)
    radius = C/((cutoff+1)*(cutoff+2))
    tail_lower = max(F(), center-radius)
    tail_upper = min(B*B/(cutoff+1), center+radius)
    return (F(floor_sum, scale)+tail_lower,
            F(floor_sum+cutoff, scale)+tail_upper)


def decimal_outward(q: F, places: int, upper: bool = False) -> str:
    scale = 10**places
    num = q.numerator*scale
    value = -((-num)//q.denominator) if upper else num//q.denominator
    return f'{value//scale}.{value%scale:0{places}d}'


def verify_record(record: dict, cutoff: int, bits: int = 80) -> dict:
    n = record['prefix_length']
    if type(n) is not int or n < 1:
        raise ValueError('prefix_length must be a positive integer')
    c = coefficients(record['coefficients'])
    direct, structured = prefix_direct(c, n), prefix_mobius(c, n)
    if direct != structured:
        raise ArithmeticError('Prefix implementations disagree')
    if not direct:
        raise ValueError('Invalid prefix certificate')
    lo, hi = norm_interval(c, cutoff, bits)
    status = 'LT_1' if hi < 1 else ('GT_1' if lo > 1 else 'UNRESOLVED')
    expected = record.get('expected', '').replace('CERTIFIED_', '')
    if expected and expected != status:
        raise ValueError(f"Unexpected verdict for {record['name']}: {status}, expected {expected}")
    return {'name': record['name'], 'prefix_length': n,
            'nonzero_coefficients': len(c), 'largest_index': max(c, default=1),
            'cutoff': cutoff, 'bits': bits, 'status': status,
            'lower_exact': str(lo), 'upper_exact': str(hi),
            'outward_decimal': [decimal_outward(lo, 12), decimal_outward(hi, 12, True)]}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input', type=Path)
    p.add_argument('--cutoff', type=int, default=10000)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    records = json.loads(args.input.read_text())
    result = [verify_record(r, args.cutoff) for r in records]
    text = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    for r in result:
        print(r['name'], r['status'], r['outward_decimal'])


if __name__ == '__main__':
    main()
