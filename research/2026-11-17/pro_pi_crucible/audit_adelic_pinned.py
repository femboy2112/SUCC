"""Focused read-only calibration for SUCC head 97c7433.

No repository modules are imported and no repository files or refs are changed.
This checks the exact three reported errors and algebraic repairs; it is not a
run of the remote author's test suite or a normality certificate.
"""

from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
import json
import subprocess

import sympy as s


REPO = Path(__file__).resolve().parents[3]
HEAD = '97c7433371feca631991a1b8227b656e92e4abcb'
FILES = (
    'research/2026-11-17/causal_clock_scrambling/ADELIC_BBP_NULL_SEED_AND_NORMALITY_CRUCIBLE.md',
    'research/2026-11-17/causal_clock_scrambling/ADELIC_BBP_NULL_SEED_VALIDATION.md',
    'observational_succ/adelic_bbp_normality_crucible.py',
    'tests/test_adelic_bbp_normality_crucible.py',
)


def git(*args):
    return subprocess.check_output(('git', *args), cwd=REPO, text=True).strip()


def r(n):
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def torus(q):
    frac = q % 1
    return min(frac, 1-frac)


v, t, z = s.symbols('v t z')
A = 1-2*v+2*v*v
B = 1-2*v*v
g_prime = (4*v**6-2*v**3-v*v-v)/(1-16*v**8)
printed_prime = ((2*v-1)/A+2*v/B)/4-1/(4*A)
corrected_prime = -((2*v-1)/A+2*v/B)/4-1/(4*A)
r2_prime = (4*v**5+2*v**4+2*v**3-s.Rational(1, 2))/(1-16*v**8)
assert g_prime.subs(v, 0) == 0
assert printed_prime.subs(v, 0) == -s.Rational(1, 2)
assert s.cancel(g_prime-corrected_prime) == 0
assert s.cancel(r2_prime-printed_prime) == 0

rows = (
    (2, 0, 4, 0, 8, 0, 16, 0),
    (0, 2, 0, 4, 0, 8, 0, 16),
    (2, 0, -4, 0, 8, 0, -16, 0),
    (0, 2, 0, -4, 0, 8, 0, -16),
    (1, 2, 2, 0, -4, -8, -8, 0),
    (1, 0, -2, -4, -4, 0, 8, 16),
    (1, -2, 2, 0, -4, 8, -8, 0),
    (1, 0, -2, 4, -4, 0, 8, -16),
)
matrix = s.Matrix(rows)/64
for j in range(8):
    a1, b1, a2, b2, a3, b3, a4, b4 = matrix[:, j]
    rhs = ((a1+b1*t)/(2-t*t)+(a2+b2*t)/(t*t+2)
           +(a3+b3*(1-t))/(t*t-2*t+2)
           +(a4+b4*(t+1))/(t*t+2*t+2))
    assert s.cancel(t**j/(16-t**8)-rhs) == 0

gaussian_coefficients_on_c = s.Matrix([[s.Rational(1, 16), s.Rational(1, 8),
                                       s.Rational(1, 8), 0, -s.Rational(1, 4),
                                       -s.Rational(1, 2), -s.Rational(1, 2), 0]])
assert gaussian_coefficients_on_c == 4*matrix[4, :]
assert gaussian_coefficients_on_c != 4*(matrix[4, :]-matrix[6, :])

u = F(0)
for n in range(1, 7):
    u = 16*u+r(n)
shell = 3
N = 2*shell
primes = [p for p in range(3, 8*N-2, 2)
          if isprime(p)
          and ((4*N < p <= 8*N-3 and p % 8 in (1, 5))
               or (8*N < 3*p and p <= 4*N-1 and p % 8 in (3, 7)))]
pi_star = 1
for p in primes:
    pi_star *= p
mod = 16**shell
r_sharp = u.numerator % (mod*pi_star)
c = u.numerator//u.denominator
c_sharp = (c//mod)*mod
v_sharp = F(c_sharp)+F(r_sharp, u.denominator)
denominator_loss = gcd(r_sharp, u.denominator)
assert denominator_loss == 3
assert u.denominator == 24536311574775
assert pi_star == 19224941
assert r_sharp == 67379365062
assert v_sharp.denominator == 8178770524925
assert r_sharp < u.denominator
assert ((v_sharp-u).numerator*pow((v_sharp-u).denominator, -1, mod)) % mod == 0
assert all((v_sharp-u).denominator % p for p in primes)
assert (v_sharp.numerator//v_sharp.denominator) % mod == 0
energy = sum(torus(v_sharp/(16**k))**2 for k in range(1, shell+1))/shell
assert energy < F(1, 255*shell)

results = {
    'scope': 'Focused exact algebra/counterexample calibration; no remote test suite rerun',
    'head': HEAD,
    'parent': git('show', '-s', '--format=%P', HEAD),
    'blobs': {path: git('rev-parse', f'{HEAD}:{path}') for path in FILES},
    'ANC7': {
        'actual_Gprime_at_zero': '0',
        'printed_Gprime_at_zero': '-1/2',
        'printed_residual': str(s.factor(g_prime-printed_prime)),
        'corrected_residual': str(s.cancel(g_prime-corrected_prime)),
        'printed_primitive_matches_r2_derivative': True,
        'correct_repair': 'Flip the FIRST logarithm sign, leave the second minus sign unchanged',
    },
    'ANC10': {'all_eight_partial_fraction_basis_identities': True},
    'ANC13': {
        'correct_gaussian_character': '4*alpha_3',
        'counterexample_polynomial': 'Q(t)=1',
        'alpha_3': '1/64',
        'alpha_4': '1/64',
        'four_times_alpha3_minus_alpha4': '0',
        'gaussian_sum': '1/16',
    },
    'ANC12': {
        'B': shell,
        'N_6': str(u.numerator),
        'Q_6': str(u.denominator),
        'Pi_6_star': str(pi_star),
        'prime_band': primes,
        'R_sharp': str(r_sharp),
        'C_sharp': str(c_sharp),
        'V_sharp': str(v_sharp),
        'gcd_R_sharp_Q_6': denominator_loss,
        'denominator_V_sharp': str(v_sharp.denominator),
        'fits': True,
        'late_2adic_congruence_preserved': True,
        'uncollided_principal_parts_preserved': True,
        'D_B': 0,
        'J_B': 0,
        'backward_energy': str(energy),
        'energy_less_than_1_over_255B': True,
    },
    'status': 'All intended exact calibrations passed; original claims fail as described',
}
print(json.dumps(results, indent=2))
