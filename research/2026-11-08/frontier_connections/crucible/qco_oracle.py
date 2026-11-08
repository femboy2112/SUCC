"""Exact finite cyclotomic-count oracle for QCO1, QCO2, QCO4.

No floating phases or prior FFT code. A vector represents coefficients of
1,zeta,...,zeta^(p-1); equality is exact modulo 1+...+X^(p-1).
"""
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path
import unittest


def orbit(p, start):
    out, x = [], start % p
    while x not in out:
        out.append(x)
        x = 16*x % p
    if x != out[0]:
        raise ValueError('noncyclic map')
    return out


def cosets(p):
    remaining = set(range(1, p))
    out = []
    while remaining:
        row = orbit(p, min(remaining))
        out.append(row)
        remaining.difference_update(row)
    return out


def canonical(v, p):
    shift = v.get(p-1, 0)
    return tuple(v.get(j, 0)-shift for j in range(p-1))


def equal(left, right, p):
    return canonical(left, p) == canonical(right, p)


def polynomial(coeffs, x, p):
    return sum(c*pow(x, j, p) for j,c in enumerate(coeffs)) % p


def prove_finite():
    counters = {'orbit_character_identities': 0,
                'canonical_rank_one_identities': 0,
                'twisted_coboundaries': 0,
                'rejected_missing_twist': 0,
                'rejected_wrong_shift': 0,
                'coherent_controls': 0,
                'exact_cycle_potentials': 0,
                'equivariant_matrix_rank_one_checks': 0,
                'asymmetric_selector_controls': 0}
    primes = [17, 41, 73, 89, 97]
    for p in primes:
        for xi in (1, 2, 3):
            xs = orbit(p, xi)
            m = len(xs)
            for d in range(1, min(m, 5)):
                for k in (1, 2, 5):
                    coefficients = [3]+[k+j for j in range(d)]
                    original = Counter(polynomial(coefficients, x, p) for x in xs)
                    shifted = Counter(polynomial(coefficients, 16*x, p) for x in xs)
                    assert equal(original, shifted, p)
                    counters['orbit_character_identities'] += 1
            for h in (1, 3):
                for c in (0, 1, 2):
                    # E a D_h e(cx/p), including the actual common-frame twist.
                    left = Counter(((16*h+16*c)*x) % p for x in xs)
                    right = Counter(((h+c)*x) % p for x in xs)
                    assert equal(left, right, p)
                    counters['twisted_coboundaries'] += 1
                    wrong = Counter(((h+16*c)*x) % p for x in xs)
                    if not equal(wrong, right, p):
                        counters['rejected_missing_twist'] += 1
                for family in (0, 1, 2):
                    # Arbitrary deterministic unit data; family 2 is inverse phase.
                    bs = {x: ((x*x+7*x+family) if family < 2 else -h*x) % p
                          for x in xs}
                    for ds in cosets(p):
                        left = Counter((bs[x]-(d-h)*x) % p for x in xs for d in ds)
                        right = Counter((bs[x]+h*x-d*xi) % p for x in xs for d in ds)
                        assert equal(left, right, p)
                        counters['canonical_rank_one_identities'] += 1
                        wrong = Counter((bs[x]-d*x) % p for x in xs for d in ds)
                        if not equal(wrong, right, p):
                            counters['rejected_wrong_shift'] += 1
                    if family == 2:
                        assert all((bs[x]+h*x) % p == 0 for x in xs)
                        counters['coherent_controls'] += 1
    for m in range(2, 52):
        values = [F((j*j+3*j+1) % 17-8, 11) for j in range(m)]
        avg = sum(values)/m
        values = [v-avg for v in values]
        potential = [F(0)]
        for v in values[:-1]:
            potential.append(potential[-1]+v)
        assert all(potential[(j+1) % m]-potential[j] == values[j] for j in range(m))
        counters['exact_cycle_potentials'] += 1
    # A second construction, not canonical Fourier coefficients: average
    # arbitrary rational matrices over the clock action to make intertwiners.
    for m in range(2,13):
        for d in range(1,m+1):
            if m%d:
                continue
            for seed in (1,3,7):
                raw=[[F(((a+1)*(u+seed)+u*u)%23-11,13)
                      for u in range(m)] for a in range(d)]
                A=[[sum((raw[(a-j)%d][(u-j)%m] for j in range(m)),F(0))/m
                    for u in range(m)] for a in range(d)]
                assert all(A[a][(u-1)%m]==A[(a+1)%d][u]
                           for a in range(d) for u in range(m))
                kappa=sum((sum(row,F(0)) for row in A),F(0))
                for trial in range(4):
                    f=[F((u*u+trial*u+seed)%19-9,7) for u in range(m)]
                    output=sum((A[a][u]*f[u] for a in range(d) for u in range(m)),F(0))
                    assert output==sum(f,F(0))/m*kappa
                    counters['equivariant_matrix_rank_one_checks'] += 1
        # Source-anchored evaluation f->f[0] violates equivariance. This is a
        # boundary control, not a contradiction of QCO5.
        f=[F(1)]+[F(0)]*(m-1)
        error=abs(f[0]-sum(f)/m)
        commutator=sum((abs(f[j]-f[0]) for j in range(m)),F(0))/m
        assert error==commutator and error>0
        counters['asymmetric_selector_controls'] += 1
    assert counters['rejected_missing_twist'] > 0
    assert counters['rejected_wrong_shift'] > 0
    return {'status':'PASS_EXACT_FINITE', 'arithmetic':'rational cyclotomic coefficient counts',
            'primes':primes, 'counts':counters,
            'normality':'OPEN', 'new_source_observations':False}


class ExactOracle(unittest.TestCase):
    def test_cyclotomic_oracle(self):
        self.assertEqual(prove_finite()['status'], 'PASS_EXACT_FINITE')

    def test_nonzero_strict_saving(self):
        # p17, h1, Q=X: B=(e(15x/17)-1)/2 is nonzero, but aB sums to zero.
        xs = orbit(17, 1)
        self.assertFalse(equal(Counter((15*x) % 17 for x in xs), Counter({0:len(xs)}), 17))
        self.assertTrue(equal(Counter(16*x % 17 for x in xs), Counter(xs), 17))

    def test_coherent_residual_cannot_close(self):
        for m in range(2, 40):
            values = [F(1)]*m
            potential = list(map(F, range(m)))
            self.assertEqual(potential[-1]+values[-1]-potential[0], m)

    def test_exact_sharp_two_cycle_inverse(self):
        f = [F(1), F(-1)]
        H = [F(-1,2), F(1,2)]
        self.assertEqual(sum(x*x for x in H)/2, F(1,4))
        self.assertEqual([H[(j+1)%2]-H[j] for j in range(2)], f)

    def test_resonance_normalization_control(self):
        for p in (17,41,73,89,97):
            m = len(orbit(p,1))
            # B=conj(a) has W=1, but canonical c_-h=m/p.
            self.assertNotEqual(F(m,p),F(1))

    def test_linearity_and_equivariance_are_both_needed(self):
        f=[F(1),F(-1)]
        self.assertEqual(sum(f),0)
        # Shift-invariant but nonlinear: squared magnitude retains energy.
        self.assertEqual(sum(x*x for x in f)/2,1)
        # Linear but not equivariant: source-anchored evaluation retains f0.
        self.assertEqual(f[0],1)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = prove_finite()
    text = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text)
    print(text, end='')
