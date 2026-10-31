"""Original SUCC four-pole and 2×3 half-power horizon exact regressions.

No floating approximation, no pi/RH proof, all proof scopes in PROOF.md.
"""
import sys
import unittest
from fractions import Fraction
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1] /
    "research" / "2026-10-31" / "half_power_horizon"))

from half_power import (
    v_p, geometric_prefix, successor_snapshot, product_formula_power,
    square_roots_one_mod2, half_binomial_term, half_sqrt_mod,
    half_geometric_term, bbp_source, bbp_denominator,
    bbp_joint_successor, eisenstein_uniformizer,
    three_sqrt_mod, joint_sqrt_successor,
)


class HalfPowerHorizonTests(unittest.TestCase):
    def test_01_binary_geometric_snapshots(self):
        for n in range(70):
            self.assertEqual(geometric_prefix(2,n),2**n-1)
            self.assertEqual(successor_snapshot(7,2,n),8-2**n)
            self.assertEqual(v_p(successor_snapshot(7,2,n)-8,2),n)

    def test_02_sixadic_successor_and_global_norm_product(self):
        for base in (2,3,6,16,36):
            for m in range(20):
                self.assertEqual(product_formula_power(base,m),1)
                self.assertEqual(successor_snapshot(Fraction(-7,11),base,m),
                                 Fraction(4,11)-base**m)
        for m in range(1,22):
            self.assertEqual(v_p(successor_snapshot(0,6,m)-1,2),m)
            self.assertEqual(v_p(successor_snapshot(0,6,m)-1,3),m)

    def test_03_four_modular_one_roots_and_two_ghosts(self):
        for k in range(3,12):
            roots=square_roots_one_mod2(k)
            self.assertEqual(len(roots),4)
            self.assertEqual(roots,tuple(i for i in range(2**k)
                             if (i*i-1) % (2**k) == 0))
            lifted=set(r % (2**k) for r in square_roots_one_mod2(k+1))
            self.assertEqual(lifted,{1,2**k-1})

    def test_04_binomial_half_terms_have_controlled_2adic_tails(self):
        for k in range(1,40):
            fact=1
            for j in range(1,k+1):
                fact*=j
            self.assertEqual(v_p(half_binomial_term(k,1),2),
                             2*k-v_p(fact,2))
            self.assertGreaterEqual(v_p(half_binomial_term(k,1),2),k+1)

    def test_05_half_power_moduli_and_real_branch_disagreement(self):
        for t in (-5,-1,0,1,2,3,8):
            for bits in range(3,22):
                r=half_sqrt_mod(t,bits)
                self.assertEqual(r%4,1)
                self.assertEqual((r*r-(1+8*t))%2**bits,0)
        for bits in range(3,24):
            self.assertEqual(half_sqrt_mod(1,bits),(-3)%2**bits)

    def test_06_half_geometric_series_at_two_is_divergent(self):
        for j in range(1,14):
            k=2**j
            self.assertEqual(v_p(half_geometric_term(k),2),1-k)
        self.assertEqual(half_geometric_term(1),1)
        self.assertEqual(half_geometric_term(2),Fraction(3,2))

    def test_07_original_signed_four_poles_and_odd_denominators(self):
        for n in range(-40,41):
            self.assertEqual(bbp_source(n),
                             Fraction(120*n*n-89*n+16,bbp_denominator(n)))
            self.assertEqual(bbp_denominator(n)%2,1)

    def test_08_exact_2adic_original_BBP_successor_transport(self):
        for n in range(-8,27):
            for m in range(1,14):
                self.assertEqual(bbp_joint_successor(n,m)["v2"],m)

    def test_09_original_BBP_3adic_source_pole_cost(self):
        for n in range(-8,27):
            for m in range(1,14):
                z=bbp_joint_successor(n,m)
                if z["qualified"]:
                    self.assertGreaterEqual(z["v3"],z["v3_lower_bound"])
        self.assertEqual(bbp_joint_successor(0,10)["pole_order"],1)
        self.assertEqual(bbp_joint_successor(1,10)["pole_order"],3)

    def test_10_extension_at_two_genuinely_eisenstein(self):
        data=eisenstein_uniformizer()
        self.assertEqual(data["u2"],data["two_times_i"])
        self.assertEqual(data["norm"],2)
        a,b,c=data["minimal_polynomial"]
        self.assertEqual(a,1)
        self.assertEqual(b%2,0)
        self.assertEqual(c%2,0)
        self.assertEqual(c%4,2)

    def test_11_original_2power_prefix_does_not_converge_at_three(self):
        for m in range(1,14):
            self.assertEqual(v_p(2**m,3),0)
            self.assertEqual(v_p(6**m,2),m)
            self.assertEqual(v_p(6**m,3),m)

    def test_12_a_moving_square_root_realizes_finite_ghost(self):
        for n in range(3,22):
            target=successor_snapshot(0,2,n)
            self.assertEqual(target%8,1)
            # First expectation was incorrectly "root = 1 modulo 2^n".
            # Corrected against exact test: the moving target selects
            # the NONLIFTING root of the FIXED polynomial x^2=1.
            self.assertEqual(half_sqrt_mod(-2**(n-3),n),
                             1+2**(n-1))
            self.assertEqual(geometric_prefix(2,n)%8,7)

    def test_13_unique_three_adic_hensel_branch(self):
        for m in range(1,14):
            target=1-6**m
            for bits in (1,2,3,5,8,12):
                r=three_sqrt_mod(target,bits)
                self.assertEqual(r%3,1)
                self.assertEqual((r*r-target)%3**bits,0)
        for bad in (-1,0,2,3,5):
            with self.assertRaises(ValueError):
                three_sqrt_mod(bad,7)

    def test_14_joint_real_two_three_half_power_horizon(self):
        for m in range(3,17):
            result=joint_sqrt_successor(m)
            self.assertLess(result["target"],0)
            self.assertEqual(result["root2_residue"]%2**m,1+2**(m-1))
            self.assertEqual(result["root3_residue"]%3**m,1)
            self.assertEqual(v_p(result["root2_residue"]-1,2),m-1)
            self.assertEqual(v_p(result["root3_residue"]-1,3),m)


if __name__=="__main__":
    unittest.main()
