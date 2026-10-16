"""Independent exact adversarial tests: source phantom and noncomputable Z2 tree."""
from fractions import Fraction as Q
from itertools import product
import unittest
from observational_succ.prime_completion_obstructions import (
    phantom_zero_stage, integer_to_cantor_digits, cantor_digit_to_integer,
    idealhard_2adic_stage,idealhard_2adic_packet,padded_immediate_halt_indices,
    idealhard_prime_bridge_probe,
)
from observational_succ.effective_field_gates import (
    diagonal_tree_admissible,diagonal_tree_level_witness,bounded_self_output,
)
from observational_succ.classical_tate_window import TateWindow,TateWindowError


class PrimeCompletionTests(unittest.TestCase):
    def test_source_true_phantom_all_prime_observation_horizons(self):
        for p,r,m in product((2,3,5,7),(1,2,3),(2,3,6,11)):
            d=phantom_zero_stage(p,r,m)
            self.assertEqual(d['actual_source_n'],p**r)
            self.assertEqual(d['actual_after_multiplication'],m*p**r)
            self.assertEqual(d['phantom_chart_residue'],p**r-1)
            self.assertFalse(d['phantom_n_in_source'])
            self.assertTrue(d['all_multipliers_fix_the_formal_chart_point_minus_one'])
            self.assertNotEqual(m*d['actual_source_n'],d['actual_source_n'])

    def test_independent_binary_digit_oracle_and_exact_admissibility(self):
        for n in range(0,8):
            st=idealhard_2adic_stage(n)
            brute=tuple(x for x in range(1<<n)
                if diagonal_tree_admissible(tuple((x>>j)&1 for j in range(n))))
            self.assertEqual(st['admissible_residues'],brute)
            self.assertEqual(st['real_haar_mass'],Q(len(brute),1<<n))
            self.assertGreater(len(brute),0)
            for x in brute:
                self.assertEqual(cantor_digit_to_integer(integer_to_cantor_digits(x,n)),x)
            finite_witness=diagonal_tree_level_witness(n)
            self.assertIn(cantor_digit_to_integer(finite_witness),brute)

    def test_projective_nesting_and_no_forced_global_witness(self):
        for n in range(1,7):
            lo=idealhard_2adic_stage(n)
            hi=idealhard_2adic_stage(n+1)
            self.assertTrue({x%(1<<n) for x in hi['admissible_residues']}
                            .issubset(set(lo['admissible_residues'])))
            self.assertLessEqual(hi['real_haar_mass'],lo['real_haar_mass'])
            self.assertFalse(hi['infinite_source_path_computed'])

    def test_real_haar_L2_norm_of_admissible_cylinder(self):
        for n in range(1,7):
            w,vec=idealhard_2adic_packet(n)
            d=TateWindow(2,n,0)
            norm=w.inner(vec,vec)
            self.assertEqual(norm,w.additive_integral(vec))
            self.assertEqual(norm,d.inner(w.fourier(vec),w.fourier(vec)))
            self.assertEqual(norm.coeff[0],idealhard_2adic_stage(n)['real_haar_mass'])
            self.assertTrue(all(x==0 for x in norm.coeff[1:]))

    def test_forbidden_diagonal_mutation_and_padding(self):
        for n in range(1,7):
            word=diagonal_tree_level_witness(n)
            for i in range(n):
                out=bounded_self_output(i,n)
                if out is not None:
                    mutated=list(word)
                    mutated[i]=out
                    self.assertFalse(diagonal_tree_admissible(tuple(mutated)))
        codes=padded_immediate_halt_indices(5)
        self.assertEqual(len(codes),len(set(codes)))
        for e in codes:
            self.assertEqual(bounded_self_output(e,1),e%2)

    def test_unsafe_source_domains_and_receipt(self):
        for bad in (4,1,-3,2.0,True):
            with self.assertRaises(TateWindowError):phantom_zero_stage(bad,2,3)
        with self.assertRaises(TateWindowError):phantom_zero_stage(3,0,3)
        with self.assertRaises(TateWindowError):phantom_zero_stage(3,2,1)
        with self.assertRaises(TateWindowError):idealhard_2adic_stage(8)
        with self.assertRaises(TateWindowError):idealhard_2adic_packet(0)
        got=idealhard_prime_bridge_probe()
        self.assertTrue(got['idealhard_2adic_cylinder_exact_fourier_parseval'] if 'idealhard_2adic_cylinder_exact_fourier_parseval' in got else got['idealhard_cylinder_exact_fourier_parseval'])
        self.assertFalse(got['completed_Weil_positivity_or_RH_proved'])
