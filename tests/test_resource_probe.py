"""Certified finite indistinguishability and direct SUCC integration tests."""
import unittest

from observational_succ.core import BudgetExceeded, DomainError, ONE, Scalar
from observational_succ.engine import Engine, run_arithmetic
from observational_succ.phenomenology import Phenomenology, example
from observational_succ.resource_probe import (
    ProbeBudget, ValuationWord, budget_demo, compare_observers,
    execute_probe, lcm_word, sample_signature)


class ResourceProbeTests(unittest.TestCase):
    def test_sharp_6_12_and_6_30_bound(self):
        six=ValuationWord.from_integer(6)
        twelve=ValuationWord.from_integer(12)
        thirty=ValuationWord.from_integer(30)
        self.assertEqual(six.min_separating_prime_power(twelve),(2,2,4))
        self.assertEqual(six.min_separating_prime_power(thirty),(5,1,5))
        self.assertEqual(compare_observers(six,twelve,ProbeBudget(3)).verdict,
                         "indistinguishable_within_budget")
        self.assertEqual(compare_observers(six,twelve,ProbeBudget(4)).verdict,"distinguished")
        self.assertFalse(execute_probe(six,twelve,2,ProbeBudget(3))['distinguishes'])
        self.assertTrue(execute_probe(six,twelve,4,ProbeBudget(4))['distinguishes'])

    def test_exhaustive_prime_power_witness_matches_literal_probes(self):
        words={n:ValuationWord.from_integer(n) for n in range(1,69)}
        for n in range(1,69):
            for m in range(1,69):
                if n == m: continue
                first=words[n].min_separating_prime_power(words[m])[2]
                actual=min(j for j in range(1,max(n,m)+1)
                           if (n%j==0)!=(m%j==0))
                self.assertEqual(first,actual,(n,m))
        for n,m in [(6,12),(6,30),(24,36),(27,45),(7,49),(1,16)]:
            a,b=words[n],words[m]
            for B in range(1,11):
                cert=compare_observers(a,b,ProbeBudget(B))
                self.assertEqual(cert.verdict=="indistinguishable_within_budget",
                    sample_signature(a,ProbeBudget(B))==sample_signature(b,ProbeBudget(B)))

    def test_lcm_shadow_indistinguishable_without_expanding_value(self):
        result=budget_demo()
        self.assertEqual(result['B'],10000)
        self.assertEqual(result['first_discrimination'],16384)
        self.assertEqual(result['formal_target_factors'],1229)
        self.assertEqual(result['finite_verdict'],"indistinguishable_within_budget")
        for B in [3,4,7,11,31,64,129,256,4096]:
            word=lcm_word(B)
            altered=word.multiply_prime(2)
            first=word.min_separating_prime_power(altered)[2]
            self.assertGreater(first,B)
            self.assertTrue(first <= 2*B) # next binary power

    def test_equal_words_do_not_claim_global_rh(self):
        a=ValuationWord.from_integer(36)
        cert=compare_observers(a,a,ProbeBudget(3))
        self.assertEqual(cert.verdict,"same_valuation_word")
        self.assertTrue(cert.same_global_valuation)
        self.assertIn("not proof of global equality",cert.data()['epistemic_warning'])

    def test_symbolic_huge_exponent_and_budget_error(self):
        a=ValuationWord(((2,2048),))
        b=a.multiply_prime(3)
        cert=compare_observers(a,b,ProbeBudget(1000))
        # The added factor of 3 is immediately visible; the large exponent is not.
        self.assertEqual(cert.verdict,"distinguished")
        self.assertEqual(cert.first_discriminating_value,3)
        c=ValuationWord(((2,2047),))
        cert=compare_observers(a,c,ProbeBudget(1000))
        self.assertEqual(cert.verdict,"indistinguishable_within_budget")
        self.assertEqual(cert.first_discriminating_value,2**2048)
        with self.assertRaises(BudgetExceeded):ProbeBudget(2**2048)
        with self.assertRaises(DomainError):ValuationWord(((4,1),))
        with self.assertRaises(DomainError):ValuationWord(((2,1),(2,2)))
        with self.assertRaises(BudgetExceeded):lcm_word(10001)

    def test_full_signature_rejects_budget_overrun(self):
        a=ValuationWord.from_integer(12)
        with self.assertRaises(BudgetExceeded):
            sample_signature(a,ProbeBudget(100,max_materialized_queries=10))
        with self.assertRaises(BudgetExceeded):
            execute_probe(a,a,101,ProbeBudget(100))
        with self.assertRaises(DomainError):
            ValuationWord.from_integer(0)

    def test_phenomenology_shadow_6_12(self):
        out=example()
        c=out['comparison']
        self.assertTrue(c['thin_indistinguishable'])
        self.assertFalse(c['path_indistinguishable'])
        self.assertEqual(c['thin_signature_a'],[1,1,1])
        self.assertEqual(c['thin_signature_b'],[1,1,1])
        self.assertEqual(c['path_signature_a'][0],2)
        self.assertEqual(c['path_signature_b'][0],3)
        self.assertFalse(out['transfer']['faithful'])
        self.assertEqual(c['shadow_a']['stage'],'shadow')
        self.assertEqual(c['shadow_b']['stage'],'shadow')
        self.assertEqual(c['shadow_a']['weight'],Scalar(-1).data())
        self.assertEqual(c['shadow_b']['weight'],Scalar(1).data())

    def test_probe_regime_evolves_after_observational_succ(self):
        e=run_arithmetic(2)
        o=Phenomenology(e,max_shadow_target=36)
        self.assertTrue(o.compare(6,12)['path_indistinguishable'])
        e.advance(ONE)
        o=Phenomenology(e,max_shadow_target=36)
        self.assertFalse(o.compare(6,12)['path_indistinguishable'])
        self.assertEqual(o.witness(6)['observational_succ'],'shadow')
        for n in (4,5):
            e.advance(ONE)
        e.step(ONE)
        # An unpropagated observation isn't an available source factor yet.
        o=Phenomenology(e,max_shadow_target=36)
        self.assertEqual(o.witness(6)['observational_succ'],'observed')
        self.assertNotIn(6,o.multipliers)
        e.propagate()
        self.assertEqual(Phenomenology(e,max_shadow_target=36).witness(6)['observational_succ'],'integrated')

    def test_false_primitive_6_not_covered_by_yoneda_coherence(self):
        normal=run_arithmetic(6)
        fake=run_arithmetic(6,overrides={6:Scalar("8/7")})
        n,f=Phenomenology(normal,max_shadow_target=36),Phenomenology(fake,max_shadow_target=36)
        self.assertEqual(n.compare(6,12)['path_signature_a'],
                         f.compare(6,12)['path_signature_a'])
        self.assertEqual(n.witness(6)['source_audit']['status'],'consistent')
        self.assertEqual(f.witness(6)['source_audit']['status'],'mixed_composite_defect')
        self.assertEqual(f.witness(6)['source_audit']['connected'],Scalar("1/7").data())

    def test_genuine_character_vs_positive_mixture(self):
        chi=Phenomenology(run_arithmetic(6,kind='chi5'),max_shadow_target=36)
        mixture=Phenomenology(run_arithmetic(6,kind='mixture5'),max_shadow_target=36)
        self.assertEqual(chi.witness(6)['source_audit']['status'],'consistent')
        self.assertEqual(mixture.witness(6)['source_audit']['status'],'mixed_composite_defect')
        self.assertEqual(chi.witness(6)['path_representable_hom_sizes'],
                         mixture.witness(6)['path_representable_hom_sizes'])

    def test_undeclared_global_object_rejected(self):
        e=run_arithmetic(3)
        o=Phenomenology(e,max_shadow_target=36)
        with self.assertRaises(DomainError):
            o.witness(100)
        with self.assertRaises(DomainError):
            Phenomenology(Engine())
        with self.assertRaises(BudgetExceeded):
            Phenomenology(e,max_shadow_target=1000000)


if __name__ == '__main__':
    unittest.main()
