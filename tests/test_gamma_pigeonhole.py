"""Independent exact Gamma/CRT/BBP controls; no floating-point theorem fitting."""
import sys
import unittest
from pathlib import Path
from fractions import Fraction as F
from math import ceil, floor
HERE=Path(__file__).resolve().parents[1]/"research"/"2026-11-04"/"gamma_pigeonhole"
sys.path.insert(0,str(HERE))
from gamma_pigeonhole import (prime,forcing,gamma_delta_bounds,source_prime,
  pole_split,clock_state,birth_register,coset_count,count_certificates,
  pair_exclusion_possible,gamma_corrected_pin,false_neighbor,old_seed_same_newprime)


class GammaPigeonhole(unittest.TestCase):
    def test_original_four_poles_and_gamma(self):
        for n in (3,6,10,12,13,15):
            s=pole_split(n);p=s["p"]
            self.assertTrue(F(2,p*p)<s["r"]<F(15,p*(p+1)))
            self.assertTrue(s["r"]<s["gamma_lower"]<s["gamma_upper"]<F(15,p*p))
            self.assertEqual(s["r"].denominator,p*s["C_force"])

    def test_original_p_birth_and_integer_lift(self):
        for n in (3,6,10,12,13,15,18):
            s=pole_split(n); b=birth_register(n)
            self.assertEqual(b["p_residue"],4)
            self.assertEqual(b["p"],s["p"])
            self.assertNotEqual(b["Q"]%b["p"]**2,0)
            self.assertEqual(F(b["A"],b["Q"]),F(4,b["p"])+F((b["A"]-4*b["C_state"])//b["p"],b["C_state"]))

    def test_exact_coset_count_and_brute_independent(self):
        for M,C in ((6,10),(17,1155),(7,30),(41,11385)):
            Q=M*C
            for u in (F(0),F(1,13),F(3,5),F(199,200)):
                for w in (F(1,3),F(15,289),F(1,10),F(1,49)):
                    z=coset_count(Q,M,4*C,u,w)
                    self.assertIn(z,(floor(C*w),ceil(C*w)))
                    if C<=1155:
                        brute=sum((((F(4*C+M*k,Q)-u)%1)<w) for k in range(C))
                        self.assertEqual(z,brute)

    def test_coarse_gamma_has_many_rivals(self):
        for n in (3,6,10,12,13):
            s=pole_split(n);p=s["p"];C=s["C_force"]
            low,high=count_certificates(p*C,p,s["gamma_lower"],s["gamma_upper"])
            self.assertGreaterEqual(low,2)
            self.assertEqual(low,s["lower_candidates"])
            self.assertEqual(high,s["upper_candidates"])
            for u in (F(0),F(1,7),F(2,5)):
                v=coset_count(p*C,p,4*C,u,s["gamma_lower"])
                self.assertTrue(low<=v<=high)

    def test_four_term_corrected_jet_pins_unique(self):
        for n in (6,10,12,13,15,18,30,40):
            if prime(8*n-7):
                z=gamma_corrected_pin(n,4)
                self.assertEqual(z["source"],z["candidate"])
                self.assertLess(z["scaled_width"],1)

    def test_neighbor_mutation_is_falsified(self):
        for n in (6,10,12,13,15,18):
            if prime(8*n-7):
                z=false_neighbor(n)
                self.assertTrue(z["coarse"])
                self.assertFalse(z["refined"])

    def test_threshold_and_just_below(self):
        from math import prod
        p=41;C=prod([p+3,p+4,p+5])//8
        self.assertLess(C*(F(236,p**4)+F(6,p**5)),1)
        with self.assertRaises(ValueError):gamma_corrected_pin(3)
        with self.assertRaises(ValueError):gamma_corrected_pin(6,2)

    def test_pair_coset_pigeonhole_wall(self):
        z=pole_split(6);Q=z["p"]*z["C_force"]
        self.assertFalse(pair_exclusion_possible(Q,z["p"],64))
        self.assertTrue(pair_exclusion_possible(Q,Q,64))
        for M in (1,z["p"],Q):
            self.assertEqual(pair_exclusion_possible(Q,M,64),2*(Q//M)<64)

    def test_coherent_wrong_seed_preserves_newborn_p_residue(self):
        A=40
        for n in (43,47,50,57,63,72):
            if prime(8*n-7):
                x=old_seed_same_newprime(A,n)
                self.assertTrue(x["same_passport"])
                self.assertNotEqual(x["changed_seed"],0)

    def test_reject_composite_p_birth(self):
        for n in (1,2,4,5,7,8,9):
            with self.assertRaises(ValueError):pole_split(n)

    def test_rational_gamma_interval_does_not_claim_normality(self):
        z=gamma_corrected_pin(6)
        self.assertTrue(z["unique"])
        # Identity of ONE injection says nothing about orbit pair statistics.
        self.assertNotEqual(z["source"],F(0))


if __name__=="__main__":
    unittest.main()


class EndpointFirewall(unittest.TestCase):
    def test_open_nearpair_arc_equality_can_have_no_candidate(self):
        # At equality 2(L/M)/q=1, the open arc can omit both endpoints.
        Q,M,q,a=8,4,4,2
        self.assertTrue(pair_exclusion_possible(Q,M,q))
        pts=[F(a+M*k,Q)%1 for k in range(Q//M)]
        self.assertEqual(pts,[F(1,4),F(3,4)])
        self.assertTrue(all(min(x,1-x)>=F(1,q) for x in pts))
