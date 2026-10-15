"""True Q-place Zeno completions: exact p-adic and archimedean controls."""
import unittest
from fractions import Fraction as Q
from observational_succ import adelic_zeno as a


class ProductFormulaTests(unittest.TestCase):
    def test_finite_genuine_prime_sources(self):
        for n in (1,2,3,4,5,6,10,16,25,97):
            ps=a.distinct_factors(n)
            self.assertEqual(len(ps),len(set(ps)))
            self.assertTrue(all(a.prime(p) and n%p==0 for p in ps))
        self.assertFalse(a.prime(6))
        self.assertFalse(a.prime(1))

    def test_exact_global_norm_product(self):
        for q in (Q(1,2),Q(4),Q(-3,8),Q(48,175),Q(1,1),Q(5,16)):
            result=a.finite_norm_product(q)
            self.assertEqual(result["global_norm_product"],1)
            self.assertFalse(result["all_places_contract_strictly"])
            self.assertTrue(result["all_other_prime_norms_exactly_one"])

    def test_p_adic_true_valuation(self):
        self.assertEqual(a.valuation(Q(4),2),2)
        self.assertEqual(a.local_norm(Q(4),2),Q(1,4))
        self.assertEqual(a.valuation(Q(1,2),2),-1)
        self.assertEqual(a.local_norm(Q(1,2),2),Q(2))
        self.assertEqual(a.valuation(Q(-75,8),5),2)
        self.assertEqual(a.local_norm(Q(3,4),2),4)

    def test_fake_places_and_float_refused(self):
        for fn in (
            lambda:a.local_norm(Q(1,2),6),
            lambda:a.valuation(Q(),2),
            lambda:a.finite_norm_product(Q()),
            lambda:a.finite_norm_product(0.5),
            lambda:a.distinct_factors(-2),
        ):
            with self.assertRaises(a.AdelicZenoError):fn()

    def test_q_nonzero_cannot_contract_all_places(self):
        for q in (Q(1,2),Q(4),Q(-3,8),Q(9,25)):
            result=a.finite_norm_product(q)
            local=[x[1] for x in result["finite_local_norms"]]
            self.assertFalse(result["arch_abs"]<1 and all(p<1 for p in local))
            self.assertEqual(result["global_norm_product"],Q(1))


class TwoPlaceZenoTests(unittest.TestCase):
    def test_real_zeno_not_two_adic(self):
        for n in (0,1,2,3,4,8,16):
            result=a.real_zeno_partial(n)
            self.assertEqual(result["partial"],2-Q(2,2**n))
            self.assertEqual(result["real_error"],Q(2,2**n))
            self.assertEqual(result["two_adic_step_norm"],Q(2**n))
            self.assertFalse(result["two_adic_contraction"])

    def test_two_adic_contraction_real_divergence(self):
        for n in (0,1,2,3,4,8,16,50):
            result=a.two_adic_zeno_partial(n)
            self.assertEqual(result["partial_integer"],(4**n-1)//3)
            self.assertEqual(result["two_adic_error_norm"],Q(1,4**n))
            self.assertEqual(3*result["partial_integer"]+1,4**n)
            self.assertFalse(result["arch_contraction"])

    def test_inverse_limit_compatible_precision_modulus(self):
        for precision in range(1,18):
            n=(precision+1)//2
            cert=a.two_adic_inverse_limit_residue(n,precision)
            self.assertTrue(cert["proved_at_precision"])
            self.assertEqual(cert["observed_residue"],cert["limit_residue"])
            if n>0 and precision%2==0:
                earlier=a.two_adic_inverse_limit_residue(n-1,precision)
                self.assertFalse(earlier["proved_at_precision"])
                self.assertNotEqual(earlier["observed_residue"],earlier["limit_residue"])

    def test_two_adic_coherent_projection(self):
        for n in range(2,8):
            r=a.two_adic_inverse_limit_residue(n,2*n)
            low=a.two_adic_inverse_limit_residue(n,n)
            self.assertEqual(r["observed_residue"] % 2**n,low["observed_residue"])
            self.assertEqual(r["limit_residue"] % 2**n,low["limit_residue"])

    def test_finite_prime_menu_hidden_denominator(self):
        for P in ((),(2,),(2,3),(2,3,5),(3,7,11)):
            witness=a.finite_place_blindspot(P)
            self.assertNotIn(witness["hidden_prime"],P)
            self.assertTrue(witness["real_contractive"])
            self.assertTrue(witness["all_selected_finite_places_neutral"])
            self.assertTrue(witness["global_product_verified"])
            self.assertGreater(witness["hidden_place_expansion_norm"],1)
            self.assertTrue(witness["inference_from_finite_menu_to_all_places_refuted"])

    def test_incorrect_independent_places_rejected(self):
        for bad in ((2,2),(2,6),(4,9),(1,),(2.0,)):
            with self.assertRaises(a.AdelicZenoError):a.finite_place_blindspot(bad)

    def test_no_universal_global_geometric_adic_clock(self):
        # The same rational source ratio cannot be a strict contraction
        # simultaneously in the real and EVERY finite p-adic completion.
        for q in (Q(1,2),Q(4),Q(3,4),Q(7,9)):
            norms=a.finite_norm_product(q)
            nontrivial=[norms["arch_abs"]]+[x[1] for x in norms["finite_local_norms"]]
            self.assertTrue(any(x>=1 for x in nontrivial))


if __name__=="__main__":
    unittest.main()
