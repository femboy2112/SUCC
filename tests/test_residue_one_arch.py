"""Hostile finite tests of Euler local units versus global Archimean scale.

The p-adic analytic K-L existence theorem and compact-group obstruction
are classical external proofs, not outputs of finite modular tests.
"""
from fractions import Fraction as Q
from math import factorial
import unittest

from observational_succ.residue_one_arch import (
    ResidueArchError, prime, valuation, residue, euler_unit, rival_units,
    prime_factors, factorial_one, product_formula, residue_idele_arch_norm,
    kl_weight_two_interpolation, demo,
)


class ResidueOneArchTests(unittest.TestCase):
    def test_euler_factor_is_a_genuine_p_adic_geometric_series(self):
        for p in (2,3,5,7,11,13,17):
            for k in (1,2,3,4,7,9):
                x=euler_unit(p,k)
                self.assertEqual(x["local_value"],str(Q(1,1-p)))
                self.assertEqual(x["exact_error"],str(Q(p**k,1-p)))
                self.assertEqual(x["error_valuation"],k)
                self.assertEqual(x["local_absolute_value"],"1")
                self.assertEqual(x["residue"],1)
                partial=sum((Q(p**j) for j in range(k)),Q())
                self.assertEqual(residue(Q(1,1-p),p,k),
                                 int(partial)%(p**k))
                self.assertEqual(valuation(Q(1,1-p)-partial,p),k)

    def test_residue_one_and_unit_norm_do_not_fix_full_local_factor(self):
        for p in (2,3,5,7,11,13,17):
            a,b=rival_units(p)
            self.assertNotEqual(a,b)
            self.assertEqual(valuation(a,p),0)
            self.assertEqual(valuation(b,p),0)
            self.assertEqual(residue(a,p,1),1%p)
            self.assertEqual(residue(b,p,1),1%p)
        self.assertNotEqual(Q(1,1-5),Q(1,1-25))

    def test_euler_factors_reject_composite_sources(self):
        for n in (0,1,4,6,8,9,12):
            self.assertFalse(prime(n))
            with self.assertRaises(ResidueArchError):
                euler_unit(n,3)
            with self.assertRaises(ResidueArchError):
                rival_units(n)
            with self.assertRaises(ResidueArchError):
                kl_weight_two_interpolation(n)
        with self.assertRaises(ResidueArchError):
            euler_unit(3,0)
        with self.assertRaises(ResidueArchError):
            residue(Q(1,3),3)

    def test_factorial_plus_one_p_adic_convergence_vs_real_divergence(self):
        prev=0
        for m in range(2,10):
            record=factorial_one(m)
            self.assertEqual(record["N"],factorial(m)+1)
            self.assertGreater(record["N"],prev)
            prev=record["N"]
            self.assertTrue(record["all_factors_larger_than_m"])
            for p,k in record["finite_residue_exponents"].items():
                self.assertGreater(k,0)
                self.assertEqual(valuation(factorial(m),p),k)
                self.assertEqual(residue(record["N"],p,k),1%(p**k))
                self.assertGreaterEqual(min(record["prime_factors"]),m+1)
        # Fixed p, v_p(m!) increases without bound as m increases.
        for p in (2,3,5):
            last=0
            for m in range(p,10):
                v=valuation(factorial(m),p)
                self.assertGreaterEqual(v,last)
                last=v

    def test_factorial_plus_one_new_prime_support_not_prime_itself(self):
        self.assertEqual(factorial_one(4)["N"],25)
        self.assertEqual(factorial_one(4)["prime_factors"],(5,))
        self.assertFalse(factorial_one(4)["prime_N"])
        self.assertEqual(factorial_one(5)["N"],121)
        self.assertEqual(factorial_one(5)["prime_factors"],(11,))
        self.assertFalse(factorial_one(5)["prime_N"])
        self.assertEqual(factorial_one(6)["N"],721)
        self.assertEqual(factorial_one(6)["prime_factors"],(7,103))

    def test_diagonal_rational_minus_one_twelfth_needs_nonunit_finite_norms(self):
        d=product_formula(Q(-1,12))
        self.assertEqual(d["arch_abs"],"1/12")
        self.assertEqual(d["finite_abs_product"],"12")
        self.assertEqual(d["norm"],"1")
        self.assertEqual(d["local"][2],{"v_p":-2,"abs_p":"4"})
        self.assertEqual(d["local"][3],{"v_p":-1,"abs_p":"3"})
        for x in (Q(1),Q(7),Q(12),Q(-1,12),Q(15,28),Q(361,147)):
            self.assertEqual(product_formula(x)["norm"],"1")
        with self.assertRaises(ResidueArchError):
            product_formula(Q(0))

    def test_nondiagonal_residue_one_unit_tuple_leaves_real_scale_free(self):
        ps=(2,3,5,7,11,13)
        a=residue_idele_arch_norm(ps,Q(1))
        b=residue_idele_arch_norm(ps,Q(2))
        c=residue_idele_arch_norm(ps,Q(1,12))
        self.assertEqual(a["finite_norm"],"1")
        self.assertEqual(b["finite_norm"],"1")
        self.assertEqual(c["finite_norm"],"1")
        self.assertTrue(a["norm_one"])
        self.assertFalse(b["norm_one"])
        self.assertFalse(c["norm_one"])
        self.assertEqual(c["idele_norm"],"1/12")
        self.assertNotEqual(c["idele_norm"],"1")
        self.assertTrue(c["not_diagonal_product_formula"])
        self.assertEqual(product_formula(Q(-1,12))["norm"],"1")
        # The two 1/12 values come from DIFFERENT source data:
        # diagonal -1/12 has 2/3-adic nonunit norms; residue tuple does not.

    def test_KL_weight_two_branch_is_source_normalization_not_euler_product_limit(self):
        expected={3:Q(1,6),5:Q(1,3),7:Q(1,2),
                  11:Q(5,6),13:Q(1)}
        for p,value in expected.items():
            entry=kl_weight_two_interpolation(p)
            self.assertEqual(Q(entry["branch_special_value"]),value)
            self.assertEqual(Q(entry["euler_removal_factor"]),Q(1-p))
            self.assertEqual(Q(entry["local_factor"])*value,Q(-1,12))
            self.assertEqual(entry["weight"],2)
            self.assertEqual(entry["weight_residue"],2%(p-1))
            self.assertFalse(entry["p_adic_measure_constructed"])
        # p=5 has branch weight residue 2 rather than the untwisted
        # weight 0: do not write a universal single-branch zeta_p(-1).
        self.assertEqual(kl_weight_two_interpolation(5)["weight_residue"],2)
        self.assertEqual(kl_weight_two_interpolation(3)["weight_residue"],0)
        with self.assertRaises(ResidueArchError):
            kl_weight_two_interpolation(2)

    def test_some_fixed_integer_not_one_cannot_be_one_at_every_prime(self):
        for n in range(2,40):
            # Prime q>n implies 0<n-1<q, so n is not 1 modulo q.
            q=next(p for p in range(n+1,2*n+5) if prime(p))
            self.assertNotEqual(n%q,1)
        # Literal "residue one at all primes" selects n=1 within Z.
        for p in (2,3,5,7,11):
            self.assertEqual(1%p,1%p)

    def test_invalid_local_source_assumptions(self):
        with self.assertRaises(ResidueArchError):
            valuation(Q(1),6)
        with self.assertRaises(ResidueArchError):
            valuation(0,3)
        with self.assertRaises(ResidueArchError):
            residue(Q(1,5),5,2)
        with self.assertRaises(ResidueArchError):
            residue(Q(1),3,0)
        with self.assertRaises(ResidueArchError):
            factorial_one(11)
        with self.assertRaises(ResidueArchError):
            residue_idele_arch_norm((2,2),Q(1))
        with self.assertRaises(ResidueArchError):
            residue_idele_arch_norm((2,6),Q(1))
        with self.assertRaises(ResidueArchError):
            residue_idele_arch_norm((2,3),Q(0))

    def test_reproducible_typed_claim_scope(self):
        d=demo()
        self.assertEqual(d["status"],"PRIME_RESIDUE_ONE_ADELIC_LOCAL_GLOBAL_OBSTRUCTION")
        self.assertTrue(d["euler_geometric_series_converges_p_adically"])
        self.assertTrue(d["all_euler_factors_are_residue_one_units"])
        self.assertTrue(d["same_residue_has_nonunique_local_units"])
        self.assertTrue(d["factorial_one_not_always_prime"])
        self.assertTrue(d["compact_to_positive_real_continuous_group_hom_trivial"])
        self.assertFalse(d["topological_group_theorem_tested_by_finite_sampling"])
        self.assertFalse(d["positive_real_scale_determined_by_residue_one_alone"])
        self.assertTrue(d["interpolation_theorem_imported"])
        self.assertFalse(d["p_adic_zeta_function_constructed"])
        self.assertFalse(d["Tate_arch_completion_constructed"])
        self.assertFalse(d["RH_claimed"])


if __name__=="__main__":
    unittest.main()
