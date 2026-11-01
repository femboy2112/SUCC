"""Discoverable exact research regression: carrier path measures and original BBP."""
import sys
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research" / "2026-10-31" / "carrier_path_measure"))

from carrier_path_measure import (
    affine_next, bbp_forcing, bbp_orbit, bbp_tail_partial, bbp_tail_upper,
    circle_distance_to_integer, cyclotomic_two_power, effective_resistance,
    enumerate_pascal_paths, finite_matching_upper_bound, gauge_path_phase,
    gaussian_pascal, pairing_phase_error, pascal_bitpath, prime_square_defect,
    fair_pascal_measure, finite_integer_line_green, integer_line_green_three_fifths,
    source_residue_pairs, two_adic_residue,
)

class TestCarrierPathMeasure(unittest.TestCase):
    def test_original_four_pole_signs(self):
        self.assertEqual(bbp_forcing(1), Fraction(47,15))
        self.assertEqual(bbp_forcing(2), Fraction(106,819))
        self.assertEqual(bbp_orbit(3), (Fraction(0),Fraction(47,15),16*Fraction(47,15)+Fraction(106,819)))

    def test_original_source_positive_and_rational_tail(self):
        for n in range(1,45):
            r = bbp_forcing(n)
            self.assertGreater(r, 0)
            self.assertLessEqual(r, Fraction(15, (8*n-7)*(8*n-6)))
        for n in range(0,16):
            for extra in (1,2,6,16):
                self.assertLess(bbp_tail_partial(n,extra), bbp_tail_upper(n))
        self.assertLess(bbp_tail_upper(1), Fraction(1,64))

    def test_rational_operators_have_original_square_defect(self):
        for n,p,x in product(range(0,20),[2,3,5,7,11],[Fraction(0), Fraction(1,3), Fraction(-17,19)]):
            self.assertEqual(affine_next(n,p*x)-p*affine_next(n,x),prime_square_defect(n,p))

    def test_square_defect_decay_not_phase_theorem(self):
        for p in (2,3,5):
            for n in range(0,24):
                self.assertLessEqual(abs(prime_square_defect(n,p)),
                                     Fraction(15*(p-1),(8*n+1)*(8*n+2)))

    def test_pascal_q_polynomial_matches_direct_oracle(self):
        for n in range(0,11):
            for k in range(n+1):
                self.assertEqual(gaussian_pascal(n,k),enumerate_pascal_paths(n,k))
                self.assertEqual(sum(gaussian_pascal(n,k)),comb(n,k))

    def test_pascal_root_of_unity_complete_row(self):
        for m in (2,4,8,16):
            for k in range(1,m):
                self.assertFalse(any(cyclotomic_two_power(gaussian_pascal(m,k),m)))
            self.assertEqual(cyclotomic_two_power(gaussian_pascal(m,0),m)[0],1)
            self.assertEqual(cyclotomic_two_power(gaussian_pascal(m,m),m)[0],1)

    def test_fair_pascal_measure(self):
        for n in range(0,20):
            mu = fair_pascal_measure(n)
            self.assertEqual(sum(mu),1)
            self.assertEqual(mu[0],Fraction(1,2**n))
            self.assertEqual(tuple(reversed(mu)),mu)

    def test_integer_line_discounted_all_paths(self):
        self.assertEqual(tuple(integer_line_green_three_fifths(0,d)
                               for d in range(4)),
                         (Fraction(5,4),Fraction(5,12),Fraction(5,36),Fraction(5,108)))
        for d in range(6):
            for horizon in (20,35):
                partial=finite_integer_line_green(0,d,horizon)
                full=integer_line_green_three_fifths(0,d)
                tailbound=Fraction(5,2)*Fraction(3,5)**(horizon+1)
                self.assertLess(partial,full)
                self.assertLessEqual(full-partial,tailbound)

    def test_flat_gauge_paths_never_interfere(self):
        potential = {(n,k): Fraction(n*n+3*k,7) for n in range(0,6) for k in range(n+1)}
        for n in range(1,6):
            for bits in product((0,1),repeat=n):
                path = pascal_bitpath(bits)
                self.assertEqual(gauge_path_phase(path,potential),potential[path[-1]]-potential[(0,0)])
        self.assertEqual(gauge_path_phase(pascal_bitpath((0,1)),potential),
                         gauge_path_phase(pascal_bitpath((1,0)),potential))

    def test_nonflat_pascal_diamond_exact(self):
        # Two realizations 01 and 10 have distinct q-weights q and 1.
        self.assertEqual(gaussian_pascal(2,1),(1,1))
        self.assertNotEqual(cyclotomic_two_power(gaussian_pascal(2,1),4),(0,0))

    def test_thomson_rational_line_triangle_cycle(self):
        line = [(0,1,Fraction(1)),(1,2,Fraction(1))]
        tri = line + [(0,2,Fraction(1))]
        self.assertEqual(effective_resistance(3,line,0,2),Fraction(2))
        self.assertEqual(effective_resistance(3,tri,0,2),Fraction(2,3))
        self.assertEqual(effective_resistance(3,tri,0,1),Fraction(2,3))
        self.assertEqual(effective_resistance(4,[(0,1,1),(1,2,1),(2,3,1),(3,0,1)],0,2),Fraction(1))
        self.assertLess(effective_resistance(3,tri,0,2), effective_resistance(3,line,0,2))

    def test_disconnected_carrier_rejected(self):
        with self.assertRaises(ValueError):
            effective_resistance(3,[(0,1,1)],0,1)
        with self.assertRaises(ValueError):
            effective_resistance(3,[(0,1,0),(1,2,1)],0,2)

    def test_two_adic_integrality_and_finite_permutation(self):
        for a in range(1,7):
            m = 2**a
            for start in (0,1,5) if a<=4 else (0,):
                residues = [two_adic_residue(u,a) for u in bbp_orbit(m+start)[start:]]
                self.assertEqual(sorted(residues),list(range(m)))
                pairs=source_residue_pairs(a,start)
                self.assertEqual(len(pairs),m//2)
                self.assertEqual(set(j for ij in pairs for j in ij), set(range(m)))
                for i,j in pairs:
                    self.assertEqual((residues[i]-residues[j]) %m,m//2)

    def test_local_character_cancellation_not_real(self):
        # Values 0,1 make a complete mod-2 residue system. Its parity
        # character sum is 1+(-1)=0, but real exp(2pi i*x) is 1+1=2.
        values = (Fraction(0),Fraction(1))
        self.assertEqual(tuple(two_adic_residue(v,1) for v in values),(0,1))
        self.assertEqual(sum((-1)**two_adic_residue(v,1) for v in values),0)
        self.assertEqual(tuple(circle_distance_to_integer(v) for v in values),(0,0))

    def test_two_adic_not_archimedean_opposite(self):
        orbit=bbp_orbit(8)
        pairs=source_residue_pairs(3)
        err=pairing_phase_error(orbit,pairs,1)
        self.assertGreater(err,0)
        self.assertGreater(finite_matching_upper_bound(orbit,pairs,1),0)
        self.assertEqual(circle_distance_to_integer(Fraction(5,3)),Fraction(1,3))

    def test_matching_certificate_stronger_than_exact_vanishing(self):
        # Uniform fourth roots: sum exactly zero regardless of the ordering.
        # A fixed residue-pairing of the second arrangement is BAD despite
        # perfect cancellation -- so this condition is sufficient, not necessary.
        good = (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4))
        bad = (Fraction(0),Fraction(1,2),Fraction(1,4),Fraction(3,4))
        pairs = ((0,2),(1,3))
        self.assertEqual(pairing_phase_error(good,pairs,1),0)
        self.assertEqual(pairing_phase_error(bad,pairs,1),Fraction(1,2))
        self.assertEqual(sum(cyclotomic_two_power((1,1,1,1),4)),0)

    def test_changing_seed_counterexample_uniform_bound(self):
        # Analytic identity U_n(-pi/16)=-T_n is proved in PROOFS.md.
        # From 0<T_n<=1/[(8n+1)(8n+2)], summing n>=1 gives <1/32.
        # With pi<22/7, |S_N(h; -pi/16)-N|<11|h|/56 for every N.
        # This is a TRUE unconditional bound, not a sampled normality test.
        for n in range(1,60):
            self.assertLess(bbp_tail_partial(n,10),bbp_tail_upper(n))
        self.assertLess(sum((bbp_tail_upper(n) for n in range(1,1000)),Fraction(0)),Fraction(1,32))

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError): bbp_forcing(0)
        with self.assertRaises(ValueError): bbp_orbit(-1)
        with self.assertRaises(ValueError): cyclotomic_two_power((1,1),6)
        with self.assertRaises(ValueError): two_adic_residue(Fraction(1,2),3)
        with self.assertRaises(ValueError): pairing_phase_error((Fraction(0),Fraction(0)),((0,1),(0,1)),1)
        with self.assertRaises(ValueError): source_residue_pairs(9)

if __name__ == '__main__':
    unittest.main()

# Independent algorithms are deliberately imported after the test class.
import importlib.util as _carrier_import_util
_carrier_oracle_path = ROOT / 'research' / '2026-10-31' / 'carrier_path_measure' / 'independent_oracle.py'
_carrier_oracle_spec = _carrier_import_util.spec_from_file_location('_carrier_path_independent_oracle', _carrier_oracle_path)
_carrier_oracle = _carrier_import_util.module_from_spec(_carrier_oracle_spec)
_carrier_oracle_spec.loader.exec_module(_carrier_oracle)
direct_pascal_cyclotomic_zero = _carrier_oracle.direct_pascal_cyclotomic_zero
two_forest_resistance = _carrier_oracle.two_forest_resistance

class TestIndependentOracles(unittest.TestCase):
    def test_full_bitword_oracle_sixteen(self):
        self.assertTrue(direct_pascal_cyclotomic_zero(16))

    def test_kirchhoff_two_forest_oracle(self):
        examples = (
            (3,[(0,1,1),(1,2,1)],0,2),
            (3,[(0,1,1),(1,2,1),(0,2,1)],0,2),
            (4,[(0,1,1),(1,2,1),(2,3,1),(3,0,1)],0,2),
            (4,[(0,1,2),(1,2,3),(2,3,4),(3,0,5),(0,2,7)],1,3),
            (5,[(0,1,1),(1,2,2),(2,3,3),(3,4,5),(4,0,7),(1,3,2)],0,3),
        )
        for vertices, edges, a,b in examples:
            self.assertEqual(effective_resistance(vertices,edges,a,b),
                             two_forest_resistance(vertices,edges,a,b))
