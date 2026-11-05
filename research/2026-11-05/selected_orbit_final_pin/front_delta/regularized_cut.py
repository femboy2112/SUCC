"""Exact source lifts and outward interval Abel-log cut measurements.

The midpoint enclosure uses an analytic second-derivative bound, not a
floating-point quadrature tolerance. No numerical pi digits construct states.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
from mpmath import iv

iv.dps = 40


def forcing(n, mutant=False):
    c = 3 if mutant else 4
    value = F(c, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)
    collapsed = F(120*n*n-89*n+16,
                  (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    if mutant:
        collapsed -= F(1, 8*n-7)
    assert value == collapsed
    return value


def exact_states(last, seed=F(0), mutant=False):
    u = seed
    result = [u]
    carries = []
    x = u % 1
    for n in range(1, last+1):
        r = forcing(n, mutant)
        u = 16*u+r
        raw = 16*x+r
        k = raw.numerator // raw.denominator
        x = raw-k
        assert x == u % 1
        carries.append(k)
        result.append(u)
    digest = sha256(json.dumps(carries, separators=(',', ':')).encode()).hexdigest()
    return [(v, v) for v in result], digest


def green(n, terms=24):
    lo = sum((forcing(n+k)/16**k for k in range(1, terms+1)), F())
    hi = lo+F(1, 16**terms*(8*(n+terms)+1)*(8*(n+terms)+2))
    return lo, hi


def periodic_beta(period=5):
    terms = 16
    lo = sum((forcing(n)/16**n for n in range(1, terms+1)), F())
    hi = lo+F(1, 16**terms*(8*terms+1)*(8*terms+2))
    den = 16**period-1
    kl, kh = int(den*lo+F(1, 2)), int(den*hi+F(1, 2))
    assert kl == kh
    return F(kl, den)


def completed_states(last, beta=F(0)):
    out = []
    for n in range(last+1):
        lo, hi = green(n)
        out.append((16**n*beta-hi, 16**n*beta-lo))
    return out


def point(q):
    return iv.mpf(q.numerator)/q.denominator


def interval(lo, hi):
    return iv.mpf([point(lo).a, point(hi).b])


def kernel(alpha, r):
    lo, hi = alpha
    shift = lo.numerator // lo.denominator
    x = interval(lo-shift, hi-shift)
    ri = point(r)
    return iv.log(1-2*ri*iv.cos(2*iv.pi*x)+ri*ri)


def average_short(alpha, length, r, panels=4):
    """Enclose average of g_r(alpha+t), 0<=t<=length<=1/16."""
    assert F(0) < length <= F(1, 16)
    value = iv.mpf(0)
    for j in range(panels):
        shift = length*F(2*j+1, 2*panels)
        value += kernel((alpha[0]+shift, alpha[1]+shift), r)/panels
    # |g_r''| <= 8*pi^2*r/(1-r)^2; midpoint composite error /24.
    ri = point(r)
    error = 8*iv.pi**2*ri/(1-ri)**2*point(length)**2/(24*panels**2)
    return value+iv.mpf([-error.b, error.b])


def pair_mean(i, j, K, states, r):
    if K <= i:
        return iv.mpf(0)
    alpha = (states[j][0]-states[i][1], states[j][1]-states[i][0])
    Q = F(16**j-16**i, 16**K)
    if j >= K:
        delta = F(1, 16**(K-i))
        shifted = (alpha[0]-delta, alpha[1]-delta)
        return -point(delta/Q)*average_short(shifted, delta, r)
    return average_short(alpha, Q, r)


def pressure(A, K, states, r):
    parts = {'future': iv.mpf(0), 'cross': iv.mpf(0), 'past': iv.mpf(0)}
    for i in range(A, 2*A):
        for j in range(i+1, 2*A):
            key = 'future' if i >= K else 'cross' if j >= K else 'past'
            parts[key] += pair_mean(i, j, K, states, r)/A**2
    return parts


def energy(A, states, r):
    value = iv.mpf(0)
    for i in range(A, 2*A):
        for j in range(i+1, 2*A):
            alpha = (states[j][0]-states[i][1], states[j][1]-states[i][0])
            value += kernel(alpha, r)/A**2
    return value


def dyadic_endpoint(raw):
    sign, man, exp, _ = raw
    return F((-1 if sign else 1)*man)*F(2)**exp


def encode(value):
    lo, hi = map(dyadic_endpoint, value._mpi_)
    return {'lower': str(lo), 'upper': str(hi), 'display': str(value),
            'sign': 'negative' if hi < 0 else 'positive' if lo > 0 else 'unresolved'}


def run():
    rows = []
    carry_hashes = {}
    beta = periodic_beta()
    for A in (17, 29, 53, 89):
        original, digest = exact_states(2*A-1)
        rational, rat_digest = exact_states(2*A-1, F(1, 5))
        mutant, mut_digest = exact_states(2*A-1, mutant=True)
        carry_hashes[str(A)] = {'original': digest, 'rational_1_5': rat_digest,
                               'first_pole_3': mut_digest}
        models = {'original': original, 'rational_1_5': rational,
                  'first_pole_3': mutant, 'unforced': [(F(0), F(0))]*(2*A),
                  'coherent': completed_states(2*A-1),
                  'periodic_5': completed_states(2*A-1, beta)}
        for name, states in models.items():
            for r in (F(1, 2), F(3, 4)):
                actual = energy(A, states, r)
                cuts = {}
                for K in (A, A+A//3, A+2*A//3, 2*A):
                    parts = pressure(A, K, states, r)
                    cuts[str(K)] = {key: encode(v) for key, v in parts.items()}
                    cuts[str(K)]['total'] = encode(sum(parts.values()))
                rows.append({'A': A, 'model': name, 'r': str(r),
                             'actual_energy': encode(actual), 'cuts': cuts})
        print('completed epoch', A, flush=True)
    return {'status': 'FINITE_INTERVAL_OBSERVATION_NOT_ASYMPTOTIC',
            'arithmetic': 'Fraction source and carries; mpmath interval dps=40',
            'quadrature': 'four midpoint panels with proved second derivative remainder',
            'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
            'periodic_beta': str(beta), 'carry_sha256': carry_hashes, 'rows': rows}


if __name__ == '__main__':
    receipt = run()
    target = Path(__file__).with_name('FINITE_RECEIPT.json')
    target.write_text(json.dumps(receipt, indent=2)+'\n')
    print(target)
