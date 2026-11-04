"""Independent reflection and arithmetic tape checks; run as a plain script."""
from fractions import Fraction
from math import comb
import json

import mpmath as mp


def quotient_from_top(n):
    """Exact division of 16^N-(1-x)^(8N) by (1+x²), from highest degree."""
    degree = 8 * n
    remainder = [(-1) ** (i + 1) * comb(degree, i) for i in range(degree + 1)]
    remainder[0] += 16**n
    quotient = [0] * (degree - 1)
    for i in range(degree, 1, -1):
        quotient[i - 2] = remainder[i]
        remainder[i - 2] -= remainder[i]
    assert remainder[:2] == [0, 0]
    return quotient


def chi(n):
    return (0, 1, 0, -1)[n % 4]


def log_vector(n):
    exponents = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            exponents[p] = exponents.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        exponents[n] = 1
    return exponents


def tape(a):
    # Coefficients are indexed from 1 with an unused zeroth entry.
    # Factorwise comparison avoids evaluation/equality assumptions for logarithms.
    out = [{}]
    for n in range(1, len(a)):
        row = {p: Fraction(e * a[n]) for p, e in log_vector(n).items()}
        for d in range(2, n):
            if n % d == 0:
                for p, coeff in out[d].items():
                    row[p] = row.get(p, 0) - coeff * a[n // d]
        out.append({p: c / a[1] for p, c in row.items() if c})
    return out


def exact_cases():
    results = []
    for n in (23, 73, 199):
        numerators = quotient_from_top(n)
        den = 16 ** n
        e = [0, 0]
        cutoff = None
        for l in range(4*n+1):
            absolute = comb(8*n,l) - e[l]
            e.append(absolute)
            signed = numerators[l] - chi(l+1) * den
            assert absolute > 0 and signed == (-1)**(l+1) * absolute
            if cutoff is None and 2*absolute >= den:
                cutoff = l
        assert cutoff is not None
        raw = [0] + [Fraction(c, den) for c in numerators[:cutoff]]
        rounded = [round(c) for c in raw]
        b = tape(rounded)
        for k in range(1, len(b)):
            vector = log_vector(k)
            expected = {next(iter(vector)): chi(k)} if len(vector)==1 and chi(k) else {}
            assert b[k] == expected
        raw2 = tape(raw[:3])[2]
        assert raw2 == {2:raw[2]/raw[1]} and raw2 != {2:raw[2]}
        assert numerators[0]-den != 1
        last = cutoff + 3
        full = [0] + [Fraction(c, den) for c in numerators[:last]]
        raw_tape = tape(full)
        certified_max = Fraction(0)
        for k in range(1, last+1):
            exponents = log_vector(k)
            row = raw_tape[k].copy()
            if len(exponents) == 1:
                p = next(iter(exponents))
                row[p] = row.get(p, 0) - chi(k)
            for p, exponent in exponents.items():
                row[p] = row.get(p, 0) - (full[k] - chi(k)) * exponent
            certified_max = max(certified_max, sum(p*abs(a) for p, a in row.items()))
        inner_bound = Fraction(comb(8*n,last//2),den)
        assert certified_max <= last**4 * inner_bound
        results.append({'N': n, 'first_failure_at_l': cutoff, 'rounded_tape_rows_verified':cutoff,
                        'raw_tape_rows_verified':last, 'rigorous_residual_upper_bound_approx':float(certified_max)})
    return results


def scaling_cases():
    mp.mp.dps = 80
    ln = mp.log
    lam = mp.findroot(lambda x: -x*ln(x/8) - (8-x)*ln(1-x/8) - ln(16), (0.6,1.5))
    slope = ln((8-lam)/lam)
    r = mp.exp(-slope)
    c = 1/(mp.sqrt(2*mp.pi*lam*(1-lam/8))*(1+r*r))
    d = c/(mp.sqrt(lam)*(1-r))
    results = []
    for n in (50,200,800,2400):
        last = int(mp.floor(lam*n+(ln(n)-ln(ln(n)))/slope))
        norm = mp.mpf(0)
        binom = 1
        prev = [0,0]
        for l in range(last):
            absnum = binom-prev[l%2]
            prev[l%2] = absnum
            norm += mp.mpf(absnum)*ln(l+1)/mp.sqrt(l+1)
            binom = binom*(8*n-l)//(l+1)
        norm /= 16**n
        prediction = d*mp.exp(slope*(last-1-lam*n))*ln(n)/n
        results.append({'N':n,'L':last,'leading_weighted_error_over_asymptotic':float(norm/prediction)})
    return {'lambda':float(lam),'slope':float(slope),'coefficient_constant':float(c),'weighted_constant':float(d),'cases':results}


if __name__ == '__main__':
    print(json.dumps({'exact': exact_cases(), 'scaling':scaling_cases(),
        'authority':'exact finite coefficient and rounded tape checks; floating leading-term diagnostic'}, indent=2))
