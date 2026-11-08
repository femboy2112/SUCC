"""Finite conditional-law diagnostics with exact polynomial and mass arithmetic.

No routine asserts that the original law is a polynomial branch model.
"""
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'research/2026-11-08/signal_frontier/prime_resonance'))
from pr_resonance import clock, evaluate, normalize, order16, source_xi


def transform(poly, p):
    """T(P)(X)=16^-1 P(16X) in F_p[X]."""
    inv = pow(16, -1, p)
    return tuple(normalize([c*pow(16, d, p)*inv for d,c in enumerate(poly)], p))


def orbit(poly, p):
    start = tuple(normalize(poly, p))
    result, current = [], start
    while current not in result:
        result.append(current)
        current = transform(current, p)
    assert current == start
    return result


def law_at(polynomials, weights, x, p):
    if len(polynomials) != len(weights) or not weights:
        raise ValueError('nonempty equal-length branches and weights required')
    weights = tuple(Q(w) for w in weights)
    if any(w <= 0 for w in weights) or sum(weights) != 1:
        raise ValueError('strictly positive probability weights required')
    law = Counter()
    for poly, weight in zip(polynomials, weights):
        law[evaluate(poly, x, p)] += weight
    return law


def tv(left, right):
    return sum(abs(left[k]-right[k]) for k in set(left)|set(right))/2


def law_defects(polynomials, weights, p, xi=None):
    """Exact TV under one multiplication-by16 source-clock step."""
    xi = source_xi(p) if xi is None else xi
    support = clock(p, xi)
    result = []
    for x in support:
        now = law_at(polynomials, weights, x, p)
        pushed = Counter()
        for residue, weight in now.items():
            pushed[16*residue % p] += weight
        nxt = law_at(polynomials, weights, 16*x % p, p)
        result.append(tv(nxt, pushed))
    return result


def rigidity_hypotheses(polynomials, p):
    values = [tuple(normalize(poly,p)) for poly in polynomials]
    if not values or len(set(values)) != len(values):
        return False
    D = max(1, max(len(poly)-1 for poly in values))
    return len(values)*D < order16(p)


def exact_source_angles(p):
    """Build literal-zero source and canonical complementary angles on I.

    Exact lifted-state and carry hashes come from the existing four-pole
    builder. Canonical forcing and an independent power sum check it here.
    """
    from observational_succ.duck_bbp import forcing
    sys.path.insert(0, str(ROOT/'research/2026-11-08/covariance_forge'))
    from source import common_history, direct_modular_residue, principal_pair
    L=(p-1)//4; n0=L+1; last=2*L
    data=common_history(last, n0)
    den=data['denominator']; residues=data['residues']
    support=clock(p,source_xi(p)); m=len(support)
    assert L % m == 0
    angles=[]
    for offset, residue in enumerate(residues):
        x,d=principal_pair(residue,den,p)
        assert d==p and x==support[offset%m]
        angles.append((Q(residue,den)-Q(x,p))%1)
    for offset in range(L-1):
        n=n0+offset
        assert (angles[offset+1]-16*angles[offset]-forcing(n+1))%1==0
    for n in (n0,(n0+last)//2,last):
        assert residues[n-n0]==direct_modular_residue(n,den)
    return {'p':p,'m':m,'L':L,'q':L//m,'n0':n0,'angles':angles,
            'residues':residues,'denominator':den,'support':support,
            'unwrapped_sha256':data['unwrapped_sha256'],
            'carry_sha256':data['carry_sha256']}
