"""Finite-horizon moving-cylinder normality certificate (stdlib only).

Independent computational experiment, not a proof of pi normality.
Authoritative paper proof is in MOVING_SCALE_THEOREM.md.
"""
from collections import Counter
from fractions import Fraction
from math import log, sqrt


def block_counts(digits, n, m, base=16):
    """Counts all length-m words starting at positions 0..n-1."""
    assert base >= 2 and n >= 1 and m >= 1
    assert len(digits) >= n + m - 1
    window = 0
    power = base ** (m - 1)
    for i in range(m):
        assert 0 <= digits[i] < base
        window = base * window + digits[i]
    counts = Counter((window,))
    for t in range(1, n):
        assert 0 <= digits[t + m - 1] < base
        window = base * (window % power) + digits[t + m - 1]
        counts[window] += 1
    return counts


def collision_energy(digits, n, m, base=16):
    c = block_counts(digits, n, m, base)
    return Fraction(base ** m * sum(x*x for x in c.values()), n*n)


def l1_short_block(digits, n, k, base=16):
    counts = block_counts(digits, n, k, base)
    q = base ** k
    return sum((abs(Fraction(counts.get(word, 0), n) - Fraction(1,q)) for word in range(q)), Fraction())


def finite_certificate_bound(q_energy, n, m, k):
    """Provably valid L1 bound via KL superadditivity + Pinsker + shift edge.

    Returns a real floating witness for tests; mathematical statement uses
    the exact Q rational and a symbolic natural log/square root bound.
    """
    assert n >= 1 and m >= k >= 1 and q_energy >= 1
    blocks = m // k
    return sqrt(2 * log(q_energy) / blocks) + Fraction(2*m, n)


def witness(digits, n, m, k, base=16):
    q = collision_energy(digits, n, m, base)
    actual = l1_short_block(digits, n, k, base)
    bound = finite_certificate_bound(q, n, m, k)
    return {'N':n,'m':m,'k':k,'base':base,'Q':str(q),
            'Q_decimal':float(q),'L1':float(actual),'upper':float(bound),
            'pass':float(actual) <= float(bound) + 1e-12}


def debruijn(base, order):
    """FKM universal cycle, same math as parent but separate implementation."""
    buf = [0] * (base*order + 1)
    out = []
    def visit(t, p):
        if t > order:
            if order % p == 0: out.extend(buf[1:p+1])
        else:
            buf[t] = buf[t-p]
            visit(t+1, p)
            for j in range(buf[t-p]+1, base):
                buf[t] = j
                visit(t+1, t)
    visit(1, 1)
    assert len(out) == base ** order
    return out


def finite_test_cases():
    import random
    cases=[]
    base=16
    cyc=debruijn(base,2)
    cases.append(('debruijn2', (cyc * 5)[:260],256,2,1))
    cases.append(('debruijn3', (debruijn(base,3)*2)[:4100],4096,3,2))
    cases.append(('zeros', [0]*513,512,2,1))
    rng=random.Random(991208)
    cases.append(('uniform', [rng.randrange(base) for _ in range(8196)],8192,4,1))
    cases.append(('biased', [0 if rng.random()<.65 else rng.randrange(base) for _ in range(4099)],4096,4,1))
    cases.append(('quarter_cycle', ([i%16 for i in range(8193)]),8192,2,1))
    return cases


if __name__ == '__main__':
    import json
    rows=[]
    for name,ds,n,m,k in finite_test_cases():
        row={'name':name,**witness(ds,n,m,k)}
        assert row['pass'],row
        rows.append(row)
    print(json.dumps({'tested_cases':len(rows),'rows':rows},indent=2))
