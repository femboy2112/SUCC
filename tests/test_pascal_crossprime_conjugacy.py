"""Scoped exact regressions: Pascal 2→3 dynamics, Haar obstruction, Pisot controls."""
import sys
import unittest
from fractions import Fraction
from math import gcd
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1] /
 "research" / "2026-10-31" / "pascal_crossprime"))

from pascal_crossprime import (
 pascal_forward,pascal_inverse,binomial_integer,
 three_pow_in_two_adics,sixteen_pow_in_three_adics,v_p_integer,
 odd_binary_to_ternary_unit,ternary_unit_to_odd_binary,
 binary_affine_to_ternary,ternary_to_binary_affine,
 induced_ternary_prefix_probabilities,empirical_prefix_probabilities,
 predicted_shell_measures,quadratic_product,quadratic_power,
 algebraic_pascal_conjugate_trace)

class PascalCrossprimeTests(unittest.TestCase):
    def test_01_pascal_two_to_three_and_inverse(self):
        a=tuple(2**n for n in range(56))
        b=tuple(3**n for n in range(56))
        self.assertEqual(pascal_forward(a),b)
        self.assertEqual(pascal_inverse(b),a)

    def test_02_general_signed_pascal_recovery(self):
        for a in (
            (0,1,2,3,4,5),(1,-3,5,-7,11,-13),
            tuple(n*n-3*n+2 for n in range(30)),
        ):
            self.assertEqual(pascal_inverse(pascal_forward(a)),a)
            self.assertEqual(pascal_forward(pascal_inverse(a)),a)

    def test_03_signed_binomial_coefficients(self):
        for n in range(-19,20):
            for k in range(30):
                v=binomial_integer(n,k)
                self.assertEqual(v,int(v))
                if k>=1:
                    self.assertEqual((k*v),((n-k+1)*binomial_integer(n,k-1)))

    def test_04_three_power_extends_continuously_two_adically(self):
        for a in (1,2,3,4,7,13,16):
            q=2**a
            for n in (-93,-21,-3,-1,0,1,2,3,17,100):
                expected=pow(3,n,q)
                self.assertEqual(three_pow_in_two_adics(n,a),expected)
                self.assertEqual(three_pow_in_two_adics(n+q,a),expected)
        for k in range(1,14):
            self.assertEqual(v_p_integer(3**(2**k)-1,2),k+2)

    def test_05_sixteen_power_extends_continuously_three_adically(self):
        for b in (1,2,3,4,7,10):
            q=3**b
            for n in (-17,-3,-1,0,1,2,5,19,40):
                expected=pow(16,n,q)
                self.assertEqual(sixteen_pow_in_three_adics(n,b),expected)
                self.assertEqual(sixteen_pow_in_three_adics(n+q,b),expected)
        for k in range(1,7):
            self.assertEqual(v_p_integer(16**(3**k)-1,3),k+1)

    def test_06_two_power_has_no_full_three_adic_continuation(self):
        for k in range(1,15):
            self.assertEqual((3**k)%3,0)
            self.assertEqual(pow(2,3**k,3),2)
            self.assertNotEqual(pow(2,0,3),pow(2,3**k,3))

    def test_07_no_nontrivial_group_iso_pro_two_pro_three(self):
        for a in range(1,9):
            for b in range(1,7):
                self.assertEqual(gcd(2**a,3**b),1)
                self.assertTrue(all((2**a*y)%(3**b)!=0
                         for y in range(1,3**b)))

    def test_08_unit_code_is_bijective_on_finite_integers(self):
        for u in range(1,20000,2):
            y=odd_binary_to_ternary_unit(u)
            self.assertNotEqual(y%3,0)
            self.assertEqual(ternary_unit_to_odd_binary(y),u)
        for y in range(1,16000):
            if y%3:
                self.assertEqual(odd_binary_to_ternary_unit(
                        ternary_unit_to_odd_binary(y)),y)

    def test_09_affine_topological_conjugacy_exact_10000(self):
        for x in range(10000):
            y=binary_affine_to_ternary(x)
            self.assertEqual(binary_affine_to_ternary(2*x+1),3*y)
            self.assertEqual(ternary_to_binary_affine(y),x)
        self.assertEqual(binary_affine_to_ternary(-1),0)
        self.assertEqual(ternary_to_binary_affine(0),-1)

    def test_10_crossprime_map_inverse_on_ternary_naturals(self):
        for y in range(1,12000):
            x=ternary_to_binary_affine(y)
            self.assertEqual(binary_affine_to_ternary(x),y)

    def test_11_valuation_holder_continuity_binary_to_ternary(self):
        for x in range(0,1000,7):
            for y in range(1,1000,9):
                if x==y:continue
                b=v_p_integer(x-y,2)
                c=v_p_integer(binary_affine_to_ternary(x)
                              -binary_affine_to_ternary(y),3)
                self.assertGreaterEqual(c,b//2)
                self.assertGreaterEqual(b,c)

    def test_12_exact_transport_of_binary_haar_prefixes(self):
        for m in range(1,7):
            self.assertEqual(empirical_prefix_probabilities(m),
                             induced_ternary_prefix_probabilities(m))
            self.assertEqual(sum(induced_ternary_prefix_probabilities(m).values()),
                             Fraction(1))

    def test_13_entropy_and_haar_mismatch(self):
        # Tail ternary probabilities are 1/4,1/4,1/2 versus native 1/3.
        q=induced_ternary_prefix_probabilities(2)
        self.assertEqual(q[(1,0)],Fraction(1,8))
        self.assertEqual(q[(1,1)],Fraction(1,8))
        self.assertEqual(q[(1,2)],Fraction(1,4))
        self.assertGreater(3**2,2**3) # D = log3 - 1.5log2 > 0.
        for n in range(1,12):
            transported,native=predicted_shell_measures(n)
            self.assertEqual(transported,Fraction(1,2**n))
            self.assertEqual(native,Fraction(1,3**n))
            self.assertNotEqual(transported,native)

    def test_14_pascal_can_destroy_pisot_under_plus_one(self):
        # β=2+√2 is Pisot, β+1=3+√2 has conjugate >1.
        beta=(2,1)
        shifted=(3,1)
        for n in range(1,18):
            a,b=quadratic_power(beta,n)
            self.assertGreater(2*b*b,(a-1)**2)
            self.assertLess(2*b*b,a*a)
            a,b=quadratic_power(shifted,n)
            self.assertGreater((a-1)**2,2*b*b)

    def test_15_pascal_transforms_exact_quadratic_trace(self):
        beta=(2,1);gamma=(3,1)
        traces=tuple(2*quadratic_power(beta,n)[0] for n in range(24))
        shifted=tuple(2*quadratic_power(gamma,n)[0] for n in range(24))
        self.assertEqual(algebraic_pascal_conjugate_trace(traces),shifted)
        self.assertEqual(pascal_inverse(shifted),traces)

    def test_16_invalid_inputs_are_rejected(self):
        for fn,args in (
            (odd_binary_to_ternary_unit,(4,)),
            (ternary_unit_to_odd_binary,(9,)),
            (binary_affine_to_ternary,(-4,)),
            (ternary_to_binary_affine,(-1,)),
            (three_pow_in_two_adics,(0,0)),
            (sixteen_pow_in_three_adics,(0,0)),
        ):
            with self.assertRaises(ValueError):fn(*args)

if __name__=="__main__":
    unittest.main()
