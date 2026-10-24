"""Galois tomography / p-free conductor / selected BBP outlier crucible."""
import cmath
import math
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_galois_tomography import (
    source_field_conductor, source_galois_window,
    rational_cyclotomic_group_ring_moment,
    galois_exception_fraction_bound,
    source_selected_galois_outlier_interval,
    prime_free_single_rule_counterexample,
)
from observational_succ.bbp_cyclotomic_birth import (
    source_window_split, multiplicative_order_16,
)


def e(x):
    """Untrusted FLOAT regression only; rational phase reduced first."""
    return cmath.exp(2j*math.pi*float(Q(x)%1))


class ExactGaloisTyping(unittest.TestCase):
    def test_actual_source_conductor_is_truly_prime_to_p(self):
        for p in (17,41,73,97,113):
            obj=source_galois_window(p)
            w=obj["complement"]
            self.assertEqual(len(w),obj["delta"])
            self.assertEqual(obj["L"],multiplicative_order_16(p))
            q=source_field_conductor(p)
            self.assertEqual(math.gcd(p,q),1)
            self.assertTrue(all(q%v.denominator==0 for v in w))
            self.assertEqual(len(set(obj["p_exponents"])),obj["L"])
            self.assertTrue(all(v != 0 for v in obj["p_exponents"]))
            self.assertEqual(tuple(v for _,v in source_window_split(p)),w)

    def test_exact_full_twisted_relative_trace_orthogonality(self):
        for p in (17,41,73,97):
            for h in (1,2,-3):
                out=rational_cyclotomic_group_ring_moment(p,h)
                d=out["Delta"];L=out["L"];B=out["B"]
                self.assertEqual(out["same_p_residue_pair_count"],d*B)
                self.assertEqual(out["total_pair_count"],d*d)
                self.assertGreater(out["coefficient_l1"],0)
                self.assertGreater(out["signed_group_ring_terms"],0)
                self.assertEqual(d,B*L)
        with self.assertRaises(ValueError):
            source_galois_window(17,0)
        with self.assertRaises(ValueError):
            source_galois_window(17,17)
        for p in (9,True,1,-3):
            with self.assertRaises(ValueError):
                source_field_conductor(p)

    def test_complex_finite_second_moment_numeric_regression_not_a_proof(self):
        for p in (17,41,73,97):
            obj=source_galois_window(p)
            L,B,Delta=obj["L"],obj["B"],obj["delta"]
            w=obj["complement"]
            V=[sum(e(w[b*L+s]) for b in range(B)) for s in range(L)]
            G=[sum(V[s]*e(Q(4*a*pow(16,s,p),p))
                   for s in range(L)) for a in range(1,p)]
            lhs=sum(abs(z)**2 for z in G)/(p-1)
            rhs=(p*sum(abs(z)**2 for z in V)-abs(sum(V))**2)/(p-1)
            self.assertAlmostEqual(lhs,rhs,places=9)
            tr=sum(G)/(p-1)
            self.assertLess(abs(tr+sum(V)/(p-1)),1e-10)

    def test_exception_proportion_requires_no_false_selected_conclusion(self):
        for p in (17,41,73,97,113):
            L=source_galois_window(p)["L"]
            self.assertEqual(
                galois_exception_fraction_bound(p,Q(1,2)),
                min(Q(1),Q(4*p,(p-1)*L)))
        self.assertLess(galois_exception_fraction_bound(97,Q(1,2)),Q(1,2))
        with self.assertRaises(ValueError):
            galois_exception_fraction_bound(17,0)
        with self.assertRaises(ValueError):
            galois_exception_fraction_bound(17,1.0)


class SelectedEmbeddingControls(unittest.TestCase):
    def test_ACTUAL_p97_selected_amplitude_exceeds_twice_galois_mean(self):
        # Certified with rational BBP input states, Machin pi brackets and
        # Taylor outward error, NOT a float or supplied digit transcript.
        data=source_selected_galois_outlier_interval(97,1,14,26)
        self.assertEqual((data["L"],data["Delta"]),(12,36))
        self.assertGreater(data["selected_normalized_amplitude_sq_lower"],
                           Q(1,20))
        self.assertLess(data["galois_mean_square_upper"],Q(1,40))
        self.assertTrue(data["selected_over_twice_rms_certified"])
        self.assertGreater(data["selected_normalized_amplitude_sq_lower"],
                           2*data["galois_mean_square_upper"])
        self.assertLessEqual(data["subgroup_weight_squares_bracket"][0],
                             data["subgroup_weight_squares_bracket"][1])

    def test_pfree_one_rule_clock_can_sustain_maximal_selected_coherence(self):
        for p in (17,41,73):
            data=prime_free_single_rule_counterexample(p,4)
            self.assertGreater(data["selected_normalized_amplitude_lower"],
                               Q(999,1000))
            self.assertLess(data["universal_galois_rms_sq_upper"],Q(1))
            self.assertGreater(data["exceptional_amplification_lower"],
                               Q(data["L"],2))
            self.assertEqual(data["Delta"],3*(p-1)//8)
            self.assertNotEqual(data["phase"].denominator%p,0)  # full phase retains p-primary
            self.assertNotEqual(data["denominator"]%p,0)  # complement Q is p-free
        with self.assertRaises(ValueError):
            prime_free_single_rule_counterexample(17,-1)

    def test_selected_certificate_input_refusal(self):
        with self.assertRaises(ValueError):
            source_selected_galois_outlier_interval(97,h=97)
        with self.assertRaises(ValueError):
            source_selected_galois_outlier_interval(257)
        with self.assertRaises(ValueError):
            source_selected_galois_outlier_interval(97,terms=True)


if __name__=="__main__":
    unittest.main()
