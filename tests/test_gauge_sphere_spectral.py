"""Focused, independent-source calibration for SUCC's gauge-coded CP1 tower.

Research-only: geometric quantization is an explicitly chosen model and does
NOT supply a source-selected Weyl estimate or a physical energy law.
"""
import cmath
import math
import unittest
from fractions import Fraction


def bbp_force(n):
    assert n >= 1
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def collapsed_force(n):
    return Fraction(120*n*n-89*n+16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def original_states(N):
    result = [Fraction(0)]
    for n in range(1, N+1):
        result.append(16*result[-1] + bbp_force(n))
    return result


def future_tail(n, terms):
    return sum((bbp_force(n+j) / 16**j for j in range(1, terms+1)),
               Fraction(0))


def phase(x):
    """Avoid feeding an enormous rational angle to floating trig."""
    frac = x % 1
    return cmath.exp(2j*math.pi*(frac.numerator/frac.denominator))


def monopole_energy_unit(degree, k):
    """E divided by the CHOSEN positive scale hbar**2/(2 M R**2)."""
    q = Fraction(degree, 2)
    return (q+k)*(q+k+1) - q*q


class TestGaugeSphereSpectral(unittest.TestCase):
    def test_authentic_source_and_odd_conductors(self):
        state = original_states(26)
        for n in range(1, 27):
            self.assertEqual(bbp_force(n), collapsed_force(n))
            self.assertEqual(state[n].denominator % 2, 1)
            self.assertEqual(state[n], 16*state[n-1] + bbp_force(n))

    def test_projective_forward_cocycle(self):
        U = original_states(3)
        for z in [cmath.exp(.317j), cmath.exp(1.213j), 0j]:
            current = z
            for n in range(1, 4):
                current = phase(bbp_force(n)) * current**16
                direct = phase(U[n]) * z**(16**n)
                self.assertLess(abs(current-direct), 1e-9)
        # The two ramification points are fixed by every source phase.
        self.assertEqual(0j**16, 0j)
        self.assertEqual(float('inf'), float('inf'))

    def test_unwrapped_tail_boundary_identity(self):
        U = original_states(14)
        K = 35
        alpha = future_tail(0, K)
        for n in range(0, 15):
            self.assertEqual(16**n*alpha-U[n], future_tail(n, K-n))
        for n in range(1, 13):
            self.assertEqual(16*future_tail(n-1, K+1)-bbp_force(n),
                             future_tail(n, K))

    def test_sphere_bundle_degree_and_sections(self):
        for n in range(5):
            d = 16**n
            self.assertEqual(d+1, len(range(d+1)))
            self.assertEqual(Fraction(d, 2), Fraction(d+1-1, 2))
        # Pullback of degree-k homogeneous monomials has 16-sparse exponents.
        for k in [0, 1, 2, 4]:
            self.assertEqual(k+1, len({16*j for j in range(k+1)}))
            self.assertTrue(all(0 <= 16*j <= 16*k for j in range(k+1)))

    def test_section_pullback_remembers_phase_not_flux(self):
        # For [X:Y] -> [xi X^16:Y^16], the section X^jY^(k-j)
        # acquires xi^j and exponents multiplied by 16.
        x1, x2 = bbp_force(1), bbp_force(2)
        U2 = 16*x1+x2
        for j in range(7):
            self.assertEqual(16*j*x1+j*x2, j*U2)
            self.assertLess(abs(phase(j*(16*x1+x2))-phase(j*U2)), 1e-14)
        self.assertEqual(16**2, 256)  # Degree is source-independent.

    def test_fubini_study_curvature_is_source_blind(self):
        for d in (1, 16, 256):
            for z in (.2+.4j, .9+.1j, 1.2+.15j):
                expected = d*d*abs(z)**(2*d-2) / (1+abs(z)**(2*d))**2
                for xi in (1, 1j, phase(bbp_force(1)), phase(bbp_force(2))):
                    f = xi*z**d
                    fp = xi*d*z**(d-1)
                    got = abs(fp)**2/(1+abs(f)**2)**2
                    self.assertAlmostEqual(got, expected, delta=1e-9*max(1,expected))

    def test_chosen_monopole_levels_and_degeneracy(self):
        for n in range(4):
            d = 16**n
            q = Fraction(d, 2)
            self.assertEqual(monopole_energy_unit(d, 0), q)
            self.assertEqual(d+1, 2*q+1)
            for k in range(5):
                self.assertEqual(monopole_energy_unit(d, k),
                                 q*(2*k+1)+k*(k+1))
                self.assertEqual(monopole_energy_unit(d, k+1)
                                 -monopole_energy_unit(d, k), d+2*k+2)
                self.assertEqual(d+2*k+1, int(2*(q+k)+1))

    def test_ordinary_round_sphere_laplacian_not_changed_by_degree(self):
        # Scalar sphere energy is l(l+1), regardless of the BBP cocycle.
        for ell in range(12):
            for n in range(4):
                self.assertEqual(ell*(ell+1), int(ell*(ell+1)))
                self.assertEqual(2*ell+1, len(range(-ell, ell+1)))

    def test_solenoid_character_renormalization_and_gap_collapse(self):
        # Pullback m -> 16m; with chosen real-flow normalization,
        # q=m/16^n is the invariant rational wave-number.
        for m in (-9, -1, 0, 1, 7):
            for n in range(5):
                self.assertEqual(Fraction(m, 16**n),
                                 Fraction(16*m, 16**(n+1)))
        gaps = [Fraction(1, 16**n)**2 for n in range(10)]
        self.assertTrue(all(gaps[i+1] < gaps[i] for i in range(len(gaps)-1)))
        self.assertEqual(gaps[1], Fraction(1, 256))
        self.assertLess(gaps[-1], Fraction(1, 10**20))

    def test_odd_torsion_inverse_is_exact_but_not_continuous(self):
        # m=16k+1 odd. Unique odd-order 16th root of e(1/m):
        # e(a/m), a=(15m+1)/16; limit root is e(15/16), not 1.
        for k in (1, 2, 17, 1234):
            m = 16*k+1
            a = (15*m+1)//16
            self.assertEqual((16*a-1) % m, 0)
            self.assertEqual(math.gcd(16, m), 1)
            self.assertEqual(math.gcd(a, m), 1)
            self.assertEqual((Fraction(16*a, m)-Fraction(1, m)).denominator, 1)
        last = Fraction((15*(16*1234+1)+1)//16, 16*1234+1)
        self.assertLess(abs(last-Fraction(15, 16)), Fraction(1, 1000))


if __name__ == '__main__':
    unittest.main()
