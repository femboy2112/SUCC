"""Exact finite tests for Pascal/Gamma quarter turn; classical infinite proofs are paper."""
import itertools
import unittest
from fractions import Fraction as Q
from math import comb
from observational_succ.pascal_gamma_turn import (
    PascalGammaError,affine_triangle,quadrant,pascal_quadrant_certificate,
    fractional_coefficient,fractional_convolution,fractional_hockey_stick,
    sideways_geometric,random_walk_integer_moments,heat_resolvent_fourier,
    completed_gamma_bath_fourier,normalized_pascal_boundary_2adic,is_prime,
    v_p_integer,receipt,weighted_pascal_adjoint_certificate
)


class PascalQuarterTurnTests(unittest.TestCase):
    def test_quadrant_pascal_15_by_15(self):
        for r in range(15):
            for k in range(15):
                self.assertTrue(pascal_quadrant_certificate(r,k)["recurrence"])
                self.assertEqual(quadrant(r,k),comb(r+k,k))

    def test_affine_lift_matches_independent_word_enumeration(self):
        for p in (2,3,6):
            rows=affine_triangle(p,5)
            for n in range(6):
                self.assertEqual(sum(sum(d.values()) for d in rows[n].values()),2**n)
                for k in range(n+1):
                    oracle={}
                    for w in itertools.product(('S','V'),repeat=n):
                        if w.count('V')!=k:continue
                        x=0
                        for op in w:
                            x=(x+1) if op=='S' else (p*x)
                        oracle[x]=oracle.get(x,0)+1
                    self.assertEqual(rows[n][k],oracle)
                    self.assertEqual(sum(oracle.values()),comb(n,k))
        self.assertEqual(affine_triangle(2,3)[3][1],{2:1,3:1,4:1})
        self.assertEqual(affine_triangle(2,5)[5][2][6],2)

    def test_affine_source_is_not_prime_oracle(self):
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(2))
        self.assertEqual(sum(affine_triangle(6,3)[3][1].values()),3)
        with self.assertRaises(PascalGammaError):
            affine_triangle(6,3,authenticate_prime=True)
        self.assertEqual(sum(affine_triangle(2,3,authenticate_prime=True)[3][1].values()),3)

    def test_rotation_is_metric_relative_weighted_adjoint(self):
        for a,b in (
                ((Q(1),Q(2),Q(-1)),(Q(1),Q(0),Q(3))),
                ((Q(0),Q(1),Q(2),Q(3)),(Q(2),Q(1),Q(-1),Q(1,2)))):
            r=weighted_pascal_adjoint_certificate(a,b)
            self.assertEqual(r['left'],r['right'])
            self.assertTrue(r['bare_transpose_is_not_generally_Hilbert_adjoint'])

    def test_fractional_semigroup_grid_exact(self):
        for a,b in ((Q(1,2),Q(1,2)),(Q(1,3),Q(2,3)),(Q(3,2),Q(5,4))):
            for k in range(24):
                self.assertTrue(fractional_convolution(a,b,k)['equal'])

    def test_fractional_half_coefficients(self):
        self.assertEqual([fractional_coefficient(Q(1,2),k) for k in range(5)],
                         [Q(1),Q(1,2),Q(3,8),Q(5,16),Q(35,128)])
        self.assertTrue(all(fractional_coefficient(Q(1,2),k)>0 for k in range(25)))

    def test_hockey_stick_and_negative_alpha(self):
        for a in (Q(1,2),Q(1,3),Q(2,3),Q(3)):
            for m in range(30):
                self.assertEqual(Q(fractional_hockey_stick(a,m)['sum']),
                                 fractional_coefficient(a+1,m))
        for a in (Q(0),Q(-1,2),0.5):
            with self.assertRaises(PascalGammaError):
                fractional_coefficient(a,3)

    def test_sideways_geometric_finite_to_global(self):
        for q in (Q(1,2),Q(1,3),Q(2,3)):
            for k in range(8):
                r=sideways_geometric(q,k,80)
                self.assertEqual(Q(r['global']),(q/(1-q))**k)
                self.assertGreaterEqual(Q(r['tail']),0)
        for k in range(8):
            self.assertEqual(sideways_geometric(Q(1,2),k,80)['global'],'1')
        with self.assertRaises(PascalGammaError):sideways_geometric(1,1)

    def test_exact_binomial_walk_moments(self):
        for n in range(1,61):
            r=random_walk_integer_moments(n)
            self.assertEqual(r['mean'],'0')
            self.assertEqual(r['second_moment'],str(n))
            self.assertFalse(r['Gaussian_limit_proved_by_finite_test'])

    def test_ou_heat_fourier_resolvent_exact(self):
        for a in (Q(1,2),Q(5,2),Q(9,2),Q(7,3)):
            for w in (Q(0),Q(1),Q(3,5),Q(-11,6)):
                r=heat_resolvent_fourier(a,w)
                self.assertEqual(r['OU_fourier_multiplier'],r['heat_laplace_multiplier'])
                self.assertTrue(r['exact'])

    def test_suzuki_bath_is_positive_but_not_weil(self):
        for w in (Q(0),Q(1,2),Q(3,5),Q(7,3)):
            r=completed_gamma_bath_fourier(w,32)
            self.assertTrue(r['positive_terms'])
            self.assertFalse(r['signed_completion_included'])
            self.assertFalse(r['RH_proved'])

    def test_two_adic_escape_of_normalized_pascal(self):
        for n in (1,2,4,8,16,32,64):
            r=normalized_pascal_boundary_2adic(n)
            self.assertEqual(r['v2_normalized'],-n)
            self.assertEqual(Q(r['two_adic_absolute']),2**n)
            self.assertEqual(Q(r['real_absolute']),Q(1,2**n))
            self.assertFalse(r['adelic_convergence_from_real_weak_limit'])
        self.assertEqual(v_p_integer(20,2),2)
        self.assertEqual(v_p_integer(20,5),1)
        with self.assertRaises(PascalGammaError):v_p_integer(20,6)

    def test_receipt_firewalls(self):
        r=receipt()
        self.assertFalse(r['RH_proved'])
        self.assertFalse(r['global_Weil_operator_identified'])
        self.assertEqual(r['pascal_affine_shadow'][6],2)
        self.assertTrue(r['Gamma_link_source_derived_from_discrete_Pascal'])


if __name__=='__main__':
    unittest.main()
