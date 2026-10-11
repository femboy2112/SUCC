"""Lambert-W SUCC test lab: independent count, branch, source, and rank controls.

Exact certificates do NOT depend on Lambert W rounding.  All tree
coefficients are exact Fractions.  Independent Prüfer-free parent-map
enumeration is a separate combinatorial implementation, not an RH witness.
"""
import itertools
import math
import unittest
from fractions import Fraction

import mpmath as mp

from observational_succ.gamma_succ_path import FactorialSuccPath
from observational_succ.gamma_interferometer import GammaInterferometer
from observational_succ.lambert_succ import (
    LambertPathError, FactorialInverseCertificate,
    principal_bulk_inverse, bulk_branches, invert_factorial_mass,
    gamma_bulk_defect, gamma_defect_succ,
    rooted_tree_coefficients, rooted_tree_succ_ratio,
    tree_functional_residual, rooted_tree_count, leaf_only_extension_count,
    tree_series_vs_lambert,
)


def independent_rooted_parent_count(n):
    """Literally enumerate all rooted directed parent forests, n<=5.

    Root has no parent. Every other vertex chooses one different
    vertex as parent. Admit precisely maps whose arrows reach root
    without cycles. Different implementation from EGF recurrence.
    """
    assert 1<=n<=5
    count=0
    for root in range(n):
        nonroot=tuple(x for x in range(n) if x!=root)
        alphabets=[tuple(k for k in range(n) if k!=i) for i in nonroot]
        for parents in itertools.product(*alphabets):
            p=dict(zip(nonroot,parents))
            good=True
            for v in nonroot:
                seen=set()
                while v!=root:
                    if v in seen:
                        good=False
                        break
                    seen.add(v)
                    v=p[v]
                if not good:
                    break
            count+=int(good)
    return count


class LambertSuccInversionTests(unittest.TestCase):
    def test_w_exact_stirling_bulk_inverse_positive_branch(self):
        with mp.workdps(75):
            for y in ["0.1","1","5","20","200","10000"]:
                y=mp.mpf(y)
                x=principal_bulk_inverse(y,dps=75)
                self.assertGreater(x,mp.e)
                self.assertLess(abs(x*(mp.log(x)-1)-y),mp.mpf("1e-68"))
                w=mp.lambertw(y/mp.e,0)
                self.assertLess(abs(x-y/w),mp.mpf("1e-65"))

    def test_real_branches_same_value_different_succ_chart(self):
        with mp.workdps(75):
            for y in ("-0.1","-0.5","-0.9"):
                hi,lo=bulk_branches(y,dps=75)
                self.assertGreater(hi,1)
                self.assertLess(hi,mp.e)
                self.assertGreater(lo,0)
                self.assertLess(lo,1)
                for x in (hi,lo):
                    self.assertLess(abs(x*(mp.log(x)-1)-mp.mpf(y)),
                                    mp.mpf("1e-65"))
            self.assertEqual(bulk_branches("-1"),(mp.mpf(1),mp.mpf(1)))
        with self.assertRaises(LambertPathError):
            bulk_branches("-1.1")
        with self.assertRaises(LambertPathError):
            principal_bulk_inverse(-1)

    def test_w_is_seed_not_certified_full_gamma_inverse(self):
        for n in (2,3,4,5,6,10,30,100,255):
            target=math.factorial(n)
            cert=invert_factorial_mass(target,dps=80)
            self.assertEqual(cert.stage,n)
            self.assertTrue(cert.verify())
            self.assertEqual(cert.lower_factorial,target)
            self.assertEqual(cert.upper_factorial,target*(n+1))
            if n>=2:
                self.assertEqual(
                    math.prod(p**k for p,k in cert.prime_valuation),target
                )
            self.assertGreaterEqual(cert.succ_steps_corrected,0)
        self.assertGreater(invert_factorial_mass(2).succ_steps_corrected,0)
        for n in (3,8,40):
            # A nonfactorial integer still admits an exact factorial
            # bracket, even if the W seed falls in the wrong interval.
            target=math.factorial(n+1)-1
            cert=invert_factorial_mass(target)
            self.assertEqual(cert.stage,n)
            self.assertTrue(cert.verify())
        self.assertEqual(invert_factorial_mass(1).stage,1)
        with self.assertRaises(LambertPathError):
            invert_factorial_mass(0)
        with self.assertRaises(LambertPathError):
            invert_factorial_mass(2.0)
        with self.assertRaises(LambertPathError):
            invert_factorial_mass(math.factorial(11),max_stage=10)

    def test_gamma_bulk_residual_and_same_succ_log_one_plus_one(self):
        with mp.workdps(75):
            for n in (2,3,5,10,100,120):
                residual=gamma_bulk_defect(n,dps=75)
                step=gamma_defect_succ(n,dps=75)
                self.assertGreater(residual,0)
                self.assertGreater(step,0)
                self.assertLess(abs(
                    gamma_bulk_defect(n+1,dps=75)-residual-step
                ),mp.mpf("1e-67"))
                # Tree SUCC ratio is built from the SAME logarithmic
                # shift but is not itself a prime-specific witness.
                r=rooted_tree_succ_ratio(n)
                v=mp.log(mp.mpf(r.numerator)/r.denominator)
                self.assertLess(abs(
                    step+v+mp.log1p(mp.mpf(1)/n)-1
                ),mp.mpf("1e-66"))

    def test_many_factorial_histories_share_value_w_cannot_restore(self):
        history=FactorialSuccPath(6).multipliers()
        reversed_history=tuple(reversed(history))
        self.assertNotEqual(history,reversed_history)
        self.assertEqual(math.prod(history),math.prod(reversed_history))
        self.assertEqual(
            invert_factorial_mass(math.prod(history)).report()["w_seed"],
            invert_factorial_mass(math.prod(reversed_history)).report()["w_seed"]
        )

    def test_no_prime_connected_sensitivity(self):
        # A fake Euler coefficient a(6) changes the arithmetic connection
        # but cannot change Lambert-W applied only to factorial mass.
        good={n:1 for n in range(1,12)}
        fake=dict(good);fake[6]=2
        a=GammaInterferometer.from_prefix(good,11)
        b=GammaInterferometer.from_prefix(fake,11)
        self.assertEqual(a.connected[6],0)
        self.assertEqual(b.connected[6],1)
        first=invert_factorial_mass(math.factorial(11))
        second=invert_factorial_mass(math.factorial(11))
        self.assertEqual(first,second)
        # This is a deliberately negative RH relevance control.
        self.assertNotEqual(a.connected,b.connected)


class RootedTreeSuccTests(unittest.TestCase):
    def test_exact_succ_recurrence_recovers_cayley(self):
        coeffs=rooted_tree_coefficients(60)
        for n in range(1,61):
            self.assertEqual(coeffs[n],Fraction(n**(n-1),math.factorial(n)))
            self.assertEqual(tree_functional_residual(coeffs,n),0)

    def test_independent_labelled_parent_maps(self):
        for n in (1,2,3,4,5):
            self.assertEqual(independent_rooted_parent_count(n),
                             rooted_tree_count(n))
            self.assertEqual(independent_rooted_parent_count(n),
                             math.factorial(n)*rooted_tree_coefficients(n)[n])

    def test_leaf_only_succ_misses_shadow_paths(self):
        for n in (1,2,3,4,8,20):
            full=rooted_tree_count(n+1)
            leaf=leaf_only_extension_count(n)
            self.assertEqual(leaf,n**n)
            self.assertEqual(full,(n+1)**n)
            self.assertGreater(full,leaf)

    def test_tree_ratio_growth_and_analytic_w_branch(self):
        ratios=[rooted_tree_succ_ratio(n) for n in range(1,120)]
        self.assertEqual(ratios[0],1)
        self.assertTrue(all(a<b for a,b in zip(ratios,ratios[1:])))
        with mp.workdps(70):
            self.assertLess(abs(mp.mpf(ratios[-1].numerator)/
                                ratios[-1].denominator-mp.e),mp.mpf(".05"))
            for z in (Fraction(1,4), Fraction(1,3)):
                short=tree_series_vs_lambert(z,30,dps=70)
                long=tree_series_vs_lambert(z,128,dps=70)
                self.assertLess(long["absolute_error"],short["absolute_error"])
                self.assertLess(long["absolute_error"],mp.mpf("1e-7"))
                self.assertLess(long["principal_limit"],1)
                self.assertGreater(long["other_real_branch"],1)
                self.assertGreater(long["other_real_branch"]-
                                   long["principal_limit"],mp.mpf(".5"))
                self.assertLess(long["truncation"],long["principal_limit"])

    def test_tree_mutation_first_degree_residual_is_exact(self):
        base=rooted_tree_coefficients(12)
        mutated=rooted_tree_coefficients(
            12,overrides={6:base[6]+Fraction(1,10)})
        self.assertEqual(base[:6],mutated[:6])
        for n in range(1,6):
            self.assertEqual(tree_functional_residual(mutated,n),0)
        self.assertEqual(tree_functional_residual(mutated,6),Fraction(1,10))
        # Later coefficients are dynamically revised; forgetting the
        # new source would erase its effect on subsequent tree stages.
        self.assertNotEqual(mutated[7:],base[7:])
        for n in range(7,13):
            self.assertEqual(tree_functional_residual(mutated,n),0)
        with mp.workdps(60):
            fake=tree_series_vs_lambert(Fraction(1,4),12,dps=60,
                                        coefficients=mutated)
            truth=tree_series_vs_lambert(Fraction(1,4),12,dps=60)
            self.assertNotEqual(fake["truncation"],truth["truncation"])
        with self.assertRaises(LambertPathError):
            rooted_tree_coefficients(5,overrides={6:1})
        with self.assertRaises(LambertPathError):
            rooted_tree_coefficients(5,overrides={3:1.01})
        with self.assertRaises(LambertPathError):
            tree_series_vs_lambert(Fraction(1,2),10)


if __name__=="__main__":
    unittest.main()
