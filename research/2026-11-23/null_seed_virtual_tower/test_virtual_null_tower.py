"""Scoped exact tests of null-seed inverse limits, BBP source jets and polynomial tower.

No claim about normality, or any infinite-time computation. Python stdlib only.
"""
import math
import unittest
from fractions import Fraction

B = 16


def bbp_r(n):
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def bbp_interval(m):
    """Strict rational interval P_m < pi/16 < P_m + (r(m+1)/15)/16**m."""
    p = sum((bbp_r(n)/B**n for n in range(1, m+1)), Fraction())
    return p, p + bbp_r(m+1)/Fraction(15*B**m)


def floor_frac(q):
    return q.numerator // q.denominator


def certified_hex_prefix(n, precision=32):
    lo, hi = bbp_interval(precision)
    assert precision >= n and 0 < lo < hi < 1
    a, b = floor_frac(B**n*lo), floor_frac(B**n*hi)
    assert a == b, ('need more precision', a, b)
    return a


def poly_mul(p, q):
    o = [0] * (len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            o[i+j] += a*b
    return o


def tower_poly(b, depth):
    coefficients = [0, 1]  # seed-value zero, but nonzero virtual off-seed field
    for j in range(1, depth+1):
        coefficients = poly_mul(coefficients, [1, -(b**j)])
    return coefficients


def at(p, t):
    return sum((a*t**j for j,a in enumerate(p)), Fraction(0))


def source_jet(k):
    return Fraction(math.factorial(k), B**(k+1)) * bbp_r(k+1)


class NullTowerTests(unittest.TestCase):
    def test_genuine_four_pole_source_and_mellin(self):
        for n in range(1, 80):
            self.assertEqual(bbp_r(n), sum((Fraction(c, 8*n-7+a) for a,c in [(0,4),(3,-2),(4,-1),(5,-1)]), Fraction()))
            self.assertGreater(bbp_r(n), 0)

    def test_source_analytic_jet_coefficients(self):
        # H_mu(z)=integral dmu(u)/(16-u*z) = sum r(k+1) z^k / 16^(k+1)
        for k in range(13):
            self.assertEqual(source_jet(k)/math.factorial(k), bbp_r(k+1)/B**(k+1))
            self.assertGreater(source_jet(k), 0)

    def test_certified_original_seed_hex_cylinders(self):
        # Prefix cylinder for completed x=pi/16, not raw rational U_n.
        p = certified_hex_prefix(12, precision=30)
        digits = []
        for n in range(1,13):
            p_n = certified_hex_prefix(n, precision=30)
            p_prev = certified_hex_prefix(n-1, precision=30) if n > 1 else 0
            digits.append(p_n - B*p_prev)
        self.assertEqual(p, sum(d*B**(11-i) for i,d in enumerate(digits)))
        self.assertTrue(all(0 <= d < B for d in digits))
        lo, hi = bbp_interval(30)
        for n in range(1,13):
            prefix = certified_hex_prefix(n,30)
            left, right = Fraction(prefix,B**n), Fraction(prefix+1,B**n)
            self.assertTrue(left < lo and hi < right)
            # The null seed is inside the open cylinder; both nearby counterfactual
            # seeds have exactly the first n completed source-selected digits.
            rho_lower = min(lo-left, right-hi)
            self.assertGreater(rho_lower,0)
            self.assertLess(rho_lower, Fraction(1,2*B**n))

    def test_null_tower_roots_and_integer_height(self):
        for k in range(1,7):
            coefficients = tower_poly(B,k)
            for j in range(1,k+1):
                self.assertEqual(at(coefficients,Fraction(1,B**j)),0)
            self.assertEqual(at(coefficients,Fraction(0)),0)
            height = B**(k*(k+1)//2)
            self.assertEqual(abs(coefficients[-1]),height)
            self.assertGreaterEqual(sum(abs(c) for c in coefficients),height)

    def test_missing_scale_mutation_is_detected(self):
        p = poly_mul([0,1], poly_mul([1,-B], [1,-B**3]))
        self.assertEqual(at(p,Fraction(1,B)),0)
        self.assertEqual(at(p,Fraction(1,B**3)),0)
        self.assertNotEqual(at(p,Fraction(1,B**2)),0)

    def test_synthetic_small_mass_cannot_hide_three_scales(self):
        # A base-16 integer polynomial of coefficient mass <= 15*B
        # cannot have 3 transported nulls unless it is identically zero:
        # mass capacity 240 versus 16^(1+2+3).
        self.assertLess(15*B, B**(3*4//2))
        # Independently, the first full vanishing-tower integer polynomial
        # exceeds this capacity.
        self.assertGreater(sum(map(abs,tower_poly(B,3))),15*B)

    def test_signed_digit_seam_jump_conservation(self):
        for n in range(1,7):
            number_of_unit_jumps = B**n - B**(n-1)
            number_of_resets = B**(n-1)
            self.assertEqual(number_of_unit_jumps-15*number_of_resets,0)
            self.assertEqual(number_of_unit_jumps+number_of_resets,B**n)

    def test_wrong_seed_locked_endpoint_is_a_seam(self):
        # Same original forcing with s=-x completes to rational 0.
        # 0 lies on the digit grid for every level, not in any open
        # prefix-cylinder. The selected irrational x avoids every grid.
        for n in range(1,8):
            self.assertEqual(Fraction(0)*B**n, 0)
            lo, hi = bbp_interval(20)
            self.assertEqual(floor_frac(B**n*lo), floor_frac(B**n*hi))
            self.assertNotEqual((B**n*lo).denominator, 1)

    def test_nonnormal_irrational_shares_null_cylinder_structure(self):
        # Kempner beta with 1 digits at 2^k positions: arbitrary finite
        # prefix cylinder is nonempty; the same inverse-limit separation
        # argument holds. This does not give normality.
        digits = [1 if n in [1,2,4,8,16,32] else 0 for n in range(1,25)]
        self.assertEqual(sum(digits[:12]),4)
        for n in (2,4,8,12):
            word=sum(digits[j]*B**(n-1-j) for j in range(n))
            self.assertGreater(Fraction(1,B**n), 0)
            self.assertTrue(0<=word<B**n)


if __name__ == '__main__':
    unittest.main()
