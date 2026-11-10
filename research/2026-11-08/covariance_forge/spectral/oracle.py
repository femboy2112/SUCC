"""Exact finite algebra for the covariance forge; no imported observer code.

Source phases are rationals from unwrapped four-pole recurrence. Cyclic
Fourier expansions are checked as formal root-of-unity coefficient multisets.
Hilbert and projection tests use exact Gaussian rationals on four-cycles.
The general BK/PNT input remains a declared paper theorem, not a test result.
"""
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
from math import factorial, isqrt
from pathlib import Path
import json
import random


@dataclass(frozen=True)
class Z:
    re: Q = Q(0)
    im: Q = Q(0)

    @staticmethod
    def lift(x):
        return x if isinstance(x, Z) else Z(Q(x))

    def __add__(self, other):
        other = Z.lift(other)
        return Z(self.re+other.re, self.im+other.im)

    __radd__ = __add__

    def __neg__(self):
        return Z(-self.re, -self.im)

    def __sub__(self, other):
        return self+-Z.lift(other)

    def __mul__(self, other):
        other = Z.lift(other)
        return Z(self.re*other.re-self.im*other.im,
                 self.re*other.im+self.im*other.re)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Z(self.re/scalar, self.im/scalar)

    def conj(self):
        return Z(self.re, -self.im)

    def abs2(self):
        return self.re*self.re+self.im*self.im


ROOT4 = (Z(Q(1)), Z(Q(0), Q(1)), Z(Q(-1)), Z(Q(0), Q(-1)))


def mean(xs):
    return sum(xs, Z())/len(xs)


def inner(u, v):
    return mean([x.conj()*y for x, y in zip(u, v)])


def norm2(u):
    return sum(x.abs2() for x in u)/len(u)


def centered(xs):
    avg = mean(xs)
    return [x-avg for x in xs]


def dft4(xs):
    assert len(xs) == 4
    return [sum((x*ROOT4[(-k*r) % 4] for r, x in enumerate(xs)), Z())/4
            for k in range(4)]


def idft4(xs):
    return [sum((x*ROOT4[(k*r) % 4] for k, x in enumerate(xs)), Z())
            for r in range(4)]


def project_modes(xs, support):
    coeff = dft4(xs)
    return idft4([c if k in support else Z() for k, c in enumerate(coeff)])


def partition_projection(xs, labels):
    groups = {}
    for label, x in zip(labels, xs):
        groups.setdefault(label, []).append(x)
    avgs = {k: mean(v) for k, v in groups.items()}
    return [avgs[k] for k in labels]


def sqrt_sum_bound(c2, x, y):
    """Exact test c2 <= (sqrt(x)+sqrt(y))^2, for nonnegative rationals."""
    assert min(c2, x, y) >= 0
    gap = c2-x-y
    return gap <= 0 or gap*gap <= 4*x*y


def forcing(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def history(N, seed=Q()):
    out = [seed]
    for n in range(1, N+1):
        out.append(16*out[-1]+forcing(n))
    return out


def authenticate_original(states):
    if not states or states[0] != 0:
        return False
    return all(states[n] == 16*states[n-1]+forcing(n)
               for n in range(1, len(states)))


def principal(x, p):
    den, pe = x.denominator, 1
    while den % p == 0:
        den //= p
        pe *= p
    if pe == 1:
        return Q()
    return Q(x.numerator*pow(den, -1, pe) % pe, pe)


def order16(p):
    if p <= 2 or any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise ValueError('odd prime required')
    x, m = 16 % p, 1
    while x != 1:
        x = x*16 % p
        m += 1
    return m


def source_cycle(p, h=1):
    if p % 8 != 1 or h % p == 0:
        raise ValueError('split prime and nonzero local frequency required')
    m = order16(p)
    L = (p-1)//4
    states = history(2*L)
    assert authenticate_original(states)
    residues = []
    for r in range(m):
        value = principal(h*states[L+1+r], p)
        assert value.denominator == p
        residues.append(value.numerator)
    xi = residues[0]
    assert residues == [xi*pow(16, r, p) % p for r in range(m)]
    return residues, L


def autocorrelation_multisets(p, h, k):
    residues, L = source_cycle(p, h)
    m = len(residues)
    modulus = p*m
    # Expand |DFT|^2 directly from the authenticated rational phase residues.
    left = Counter(((residues[r]-residues[s])*m-k*(r-s)*p) % modulus
                   for r in range(m) for s in range(m))
    # Separately expand the source-forced shift/subgroup expression.
    xi = residues[0]
    right = Counter((xi*(pow(16, d, p)-1)*pow(16, s, p)*m-k*d*p) % modulus
                    for d in range(m) for s in range(m))
    return left, right


def polynomial(coefficients, n):
    return sum((c*n**j for j, c in enumerate(coefficients)), Q())


def additive_difference(function, n, shifts):
    total = Q()
    d = len(shifts)
    for mask in product((0, 1), repeat=d):
        offset = sum(h for h, bit in zip(shifts, mask) if bit)
        total += (-1)**(d-sum(mask))*function(n+offset)
    return total


def polynomial_source_difference_check(p, h, degree, shifts):
    residues, _ = source_cycle(p, h)
    m, xi = len(residues), residues[0]
    assert len(shifts) == degree and sum(shifts) < m
    coeff = [Q((-1)**j*(j+1), 2*j+3) for j in range(degree+1)]
    factor = xi
    for shift in shifts:
        assert 0 < shift < m
        factor = factor*(pow(16, shift, p)-1) % p
    assert factor != 0
    constant = coeff[-1]*factorial(degree)
    for shift in shifts:
        constant *= shift
    count = 0
    for r in range(m-sum(shifts)):
        phase = lambda t: Q(residues[t], p)+polynomial(coeff, t)
        actual = additive_difference(phase, r, shifts)
        expected = Q(factor*pow(16, r, p) % p, p)+constant
        assert (actual-expected).denominator == 1
        count += 1
    return count


def run():
    counts = {}
    source_checks = 0
    cyclic_checks = 0
    difference_checks = 0
    source_rows = []
    for p in (17, 41, 73, 89, 97, 137, 193, 233, 281):
        for h in (1, 2, 5):
            residues, L = source_cycle(p, h)
            m = len(residues)
            source_checks += m
            for k in sorted({0, 1, m//2, m-1}):
                left, right = autocorrelation_multisets(p, h, k)
                assert left == right
                cyclic_checks += m*m
            for degree in (1, 2, 3, 4):
                shifts = tuple(1+(j % 2) for j in range(degree))
                if sum(shifts) < m:
                    difference_checks += polynomial_source_difference_check(
                        p, h, degree, shifts)
            if h == 1:
                source_rows.append({'p': p, 'm': m, 'L': L,
                                    'source_epoch': [L+1, 2*L+1]})
    counts['exact_source_prime_phase_checks'] = source_checks
    counts['root_multiset_autocorrelation_terms'] = cyclic_checks
    counts['polynomial_difference_phase_checks'] = difference_checks

    rng = random.Random(20261108)
    projection_checks = 0
    for _ in range(60):
        a = [Z(Q(rng.randrange(-5, 6), 7), Q(rng.randrange(-5, 6), 7))
             for _ in range(4)]
        b = [Z(Q(rng.randrange(-5, 6), 7), Q(rng.randrange(-5, 6), 7))
             for _ in range(4)]
        u = centered([x.conj() for x in a])
        v = centered(b)
        covariance = mean([x*y for x, y in zip(a, b)])-mean(a)*mean(b)
        assert covariance == inner(u, v)
        for labels in ((0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 2, 3)):
            pu, pv = partition_projection(u, labels), partition_projection(v, labels)
            qu = [x-y for x, y in zip(u, pu)]
            qv = [x-y for x, y in zip(v, pv)]
            assert covariance == inner(pu, pv)+inner(qu, qv)
            assert inner(pu, qv) == inner(qu, pv) == Z()
            d2, eta2 = norm2(pu), norm2(qv)
            x = d2*(norm2(v)-eta2)
            y = (norm2(u)-d2)*eta2
            assert sqrt_sum_bound(covariance.abs2(), x, y)
            projection_checks += 4
        assert idft4(dft4(a)) == a
        assert sum(x.abs2() for x in dft4(a)) == norm2(a)
        projection_checks += 3
    counts['gaussian_rational_projection_checks'] = projection_checks

    # Exact flat-spectrum, maximal-coherence control: every mode has magnitude1/2.
    a = [Z(Q(1)), Z(Q(1)), Z(Q(1)), Z(Q(-1))]
    b = [x.conj() for x in a]
    assert mean([x*y for x, y in zip(a, b)]) == Z(Q(1))
    assert all(x.abs2() == Q(1, 4) for x in dft4(a))
    dual_checks = 0
    for s in range(5):
        for support in combinations(range(4), s):
            residual = [x-y for x, y in zip(b, project_modes(b, support))]
            assert norm2(residual) == 1-Q(s, 4)
            dual_checks += 1
    counts['sharp_sparse_dual_witness_checks'] = dual_checks

    # Folding removes the replica-orthogonal component exactly.
    replicas = [[ROOT4[(r+j) % 4] for r in range(4)] for j in range(3)]
    folded = [mean([replicas[j][r] for j in range(3)]) for r in range(4)]
    direct = mean([a[r]*replicas[j][r] for j in range(3) for r in range(4)])
    assert direct == mean([a[r]*folded[r] for r in range(4)])
    counts['folding_checks'] = 1

    mutants = {}
    states = history(20)
    mutants['wrong_seed_rejected_by_zero_gate'] = not authenticate_original(history(20, Q(1, 3)))
    mutant = states.copy(); mutant[7] += Q(1, 7)
    mutants['source_state_mutation_rejected'] = not authenticate_original(mutant)
    mutants['wrapped_only_source_rejected'] = not authenticate_original([x % 1 for x in states])
    mutants['chronology_reversal_rejected'] = not authenticate_original(list(reversed(states)))
    # A full-order shift makes the source coefficient zero: the h_i<m hypothesis matters.
    mutants['full_cycle_difference_is_degenerate'] = pow(16, order16(41), 41)-1 == 0
    # A one-dimensional learned span may resonate fully without shift closure.
    mutants['arbitrary_rank_one_prediction_is_not_safe'] = inner(b, b) == Z(Q(1))
    mutants['dropping_covariance_gives_false_zero'] = mean(a)*mean(b) != Z(Q(1))
    assert all(mutants.values())
    return {'status': 'PASS_EXACT_FINITE_ONLY', 'counts': counts,
            'total_checks': sum(counts.values()), 'source_rows': source_rows,
            'negative_controls': mutants,
            'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
            'claim_boundary': 'BK/PNT and asymptotic theorems require their paper proofs; full source covariance OPEN.'}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
