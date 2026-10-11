"""Finite-support omega theorem and certified witness protocol.

The omega compactness lemma is an algebraic fact about finite derivations
over an increasing union of theories, NOT a proof of Gödel incompleteness
or a proof that infinity can be physically executed.

The Gram probe accepts ONLY exact rational endpoints/enclosures; future
Suzuki/Weil use needs an independently justified rigorous analytic
prime-and-Gamma interval oracle. Numeric mpmath point values are rejected.
"""
import unittest
from fractions import Fraction as Q

from observational_succ.observer_logic import (
    Num, Var, Pred, Forall, Implies, Not, Exists, And, Add,
    Theory, ProofStep, FiniteProof, check_finite_proof,
)
from observational_succ.observer_reflection import (
    ReflectionBoundaryError, IncreasingTheoryChain,
    external_consistency_step, RationalInterval,
    rational_gram_certificate, exact_quartic_screw,
    UnnamedElementOmegaCountermodel,
    exact_quadratic_screw, bounded_gram_search,
)
from observational_succ.godel_succ import machine_prefix, delayed_halt, two_counter_loop


class FinitaryOmegaTests(unittest.TestCase):
    def setUp(self):
        self.a=Pred("A",Num(0))
        self.b=Pred("B",Num(0))
        self.c=Pred("C",Num(0))
        self.bc=Implies(self.b,self.c)
        self.base=Theory("T0",frozenset((self.a,)))
        self.chain=IncreasingTheoryChain((self.base,))
        self.chain=self.chain.successor(self.b,label="external trial axiom B")
        self.chain=self.chain.successor(self.bc,label="external trial implication B=>C")

    def test_finitary_proof_at_omega_union_has_finite_stage_witness(self):
        proof=FiniteProof((
            ProofStep(self.b,"axiom"),
            ProofStep(self.bc,"axiom"),
            ProofStep(self.c,"modus_ponens",(0,1)),
        ))
        witness=self.chain.omega_finitary_support(proof)
        self.assertTrue(witness.finite_proof_verified)
        self.assertEqual(witness.earliest_stage,2)
        self.assertEqual(witness.conclusion,self.c)
        self.assertEqual(set(witness.used_axioms),{self.b,self.bc})
        self.assertEqual(witness.total_stages_inspected,3)
        self.assertFalse(witness.omega_rule_used)
        self.assertFalse(witness.physical_infinite_process_executed)
        self.assertTrue(check_finite_proof(self.chain.stages[2],proof))
        with self.assertRaises(ReflectionBoundaryError):
            IncreasingTheoryChain(self.chain.stages[:2]).omega_finitary_support(proof)

    def test_earliest_stage_handles_zero_and_skipped_earlier_axioms(self):
        p0=FiniteProof((ProofStep(self.a,"axiom"),))
        p1=FiniteProof((ProofStep(self.b,"axiom"),))
        self.assertEqual(self.chain.omega_finitary_support(p0).earliest_stage,0)
        self.assertEqual(self.chain.omega_finitary_support(p1).earliest_stage,1)
        self.assertEqual(self.chain.omega_finitary_support(p1).used_axioms,(self.b,))

    def test_reflection_successor_is_explicit_unproved_new_axiom(self):
        other,evidence=external_consistency_step(
            self.chain,evidence_label="metatheoretic assumption, not finite observation")
        self.assertEqual(len(other.stages),4)
        self.assertEqual(evidence["axiom_status"],"EXTERNAL_ASSUMPTION_ONLY")
        self.assertIsNone(evidence["claimed_truth_of_axiom"])
        self.assertFalse(evidence["verified_in_predecessor"])
        self.assertFalse(evidence["reflective_successor_is_ordinary_observation"])
        ax=evidence["new_axiom"]
        with self.assertRaises(ReflectionBoundaryError):
            self.chain.omega_finitary_support(FiniteProof((ProofStep(ax,"axiom"),)))
        witness=other.omega_finitary_support(FiniteProof((ProofStep(ax,"axiom"),)))
        self.assertEqual(witness.earliest_stage,3)
        self.assertEqual(witness.used_axioms,(ax,))

    def test_observational_omega_report_is_not_a_formula_proof(self):
        report=self.chain.semantic_omega_report("Survives",128)
        self.assertEqual(report["observed_through"],128)
        self.assertEqual(report["intended_global_formula"],
                         Forall("n",Pred("Survives",Var("n"))))
        self.assertEqual(report["proof_status"],"UNRESOLVED")
        self.assertFalse(report["finite_proof_manufactured"])
        self.assertTrue(report["omega_not_executed"])
        # A finite all-clear prefix is not a finitary universal theorem.
        loop=two_counter_loop()
        delayed=delayed_halt(100)
        self.assertEqual(machine_prefix(loop,17).status,"unresolved")
        self.assertEqual(machine_prefix(delayed,17).status,"unresolved")
        self.assertEqual(machine_prefix(delayed,100).first_counterexample,100)

    def test_nonmonotone_theories_cannot_claim_omega_colimit(self):
        a=Theory("T1",frozenset((self.a,)))
        b=Theory("T2",frozenset((self.b,)))
        with self.assertRaises(ReflectionBoundaryError):
            IncreasingTheoryChain((a,b))
        with self.assertRaises(ReflectionBoundaryError):
            IncreasingTheoryChain(())
        with self.assertRaises(ReflectionBoundaryError):
            self.chain.successor(Pred("P",Var("x")),label="invalid free variable")
        with self.assertRaises(ReflectionBoundaryError):
            self.chain.successor(self.a,label="")


class MonadicLimitSemanticTests(unittest.TestCase):
    def test_all_individual_named_observations_hold_but_universal_fails(self):
        # This is a mathematically explicit FIRST-ORDER model, not a
        # computation that has waited infinitely many SUCC steps.
        m=UnnamedElementOmegaCountermodel("Observed")
        for n in (0,1,2,3,19,1000,10**40):
            self.assertTrue(m.named_instance(n))
            self.assertTrue(m.evaluate(Pred("Observed",Num(n))))
        formula=Forall("x",Pred("Observed",Var("x")))
        self.assertFalse(m.evaluate(formula))
        self.assertTrue(m.evaluate(
            Exists("x",Not(Pred("Observed",Var("x"))))))
        self.assertTrue(m.evaluate(
            Forall("x",Implies(Pred("Observed",Var("x")),
                               Pred("Observed",Var("x"))))))
        self.assertFalse(m.evaluate(
            Forall("x",And(Pred("Observed",Var("x")),
                            Pred("Observed",Num(3))))))
        report=m.structural_report()
        self.assertTrue(report["all_named_ground_instances_true"])
        self.assertFalse(report["global_universal_claim_true"])
        self.assertFalse(report["applies_to_PA"])
        self.assertFalse(report["RH_independence_inferred"])

    def test_countermodel_cannot_launder_arithmetic_or_free_variable_claims(self):
        m=UnnamedElementOmegaCountermodel("P")
        with self.assertRaises(ReflectionBoundaryError):
            m.evaluate(Pred("Q",Num(0)))
        with self.assertRaises(ReflectionBoundaryError):
            m.evaluate(Pred("P",Var("x")))
        with self.assertRaises(ReflectionBoundaryError):
            m.evaluate(Forall("x",Pred("P",Add(Var("x"),Num(1)))))
        self.assertTrue(m.evaluate(Forall("x",Pred("P",Num(2)))))
        with self.assertRaises(ReflectionBoundaryError):
            UnnamedElementOmegaCountermodel("")
        with self.assertRaises(ReflectionBoundaryError):
            m.named_instance(-1)


class CertifiedGramTests(unittest.TestCase):
    def test_interval_arithmetic_propagates_uncertainty_and_sign(self):
        a=RationalInterval(Q(1,3),Q(2,3))
        b=RationalInterval(Q(-1),Q(2))
        self.assertEqual((a+b).lower,Q(-2,3))
        self.assertEqual((a+b).upper,Q(8,3))
        self.assertEqual((a*b).lower,Q(-2,3))
        self.assertEqual((a*b).upper,Q(4,3))
        self.assertEqual(a.scale(-3),RationalInterval(Q(-2),Q(-1)))
        self.assertEqual((-b),RationalInterval(Q(-2),Q(1)))
        self.assertTrue(a.intersects(RationalInterval(Q(1,2),Q(4))))
        self.assertFalse(a.intersects(RationalInterval(Q(1),Q(2))))
        with self.assertRaises(ReflectionBoundaryError):
            RationalInterval(Q(1),Q(0))
        with self.assertRaises(ReflectionBoundaryError):
            RationalInterval.exact(1.02)

    def test_strict_negative_quartic_certificate_is_exact(self):
        r=rational_gram_certificate(
            (Q(-1),Q(1)),(Q(1),Q(1)),
            exact_quartic_screw,provenance="exact polynomial identity")
        self.assertEqual(r.enclosure,RationalInterval.exact(-24))
        self.assertEqual(r.result,"STRICT_NEGATIVE_WITNESS_CONDITIONAL_ON_INTERVAL_ORACLE")
        self.assertFalse(r.universal_positivity_proved)
        self.assertTrue(r.relies_on_oracle_soundness)
        search=bounded_gram_search(exact_quartic_screw,
                                   points=(-1,0,1),budget=200,
                                   provenance="exact polynomial")
        self.assertEqual(search["status"],"STRICT_NEGATIVE_WITNESS")
        self.assertLess(search["certificate"].enclosure.upper,0)
        self.assertFalse(search["universal_positivity_proved"])

    def test_positive_hilbert_quadratic_example_stays_unresolved_not_proved(self):
        for a,b in ((Q(-2),Q(2)),(Q(1),Q(-1)),(Q(0),Q(3))):
            r=rational_gram_certificate(
                (-1,1),(a,b),exact_quadratic_screw,
                provenance="exact polynomial K=2tu")
            self.assertGreaterEqual(r.enclosure.lower,0)
            self.assertEqual(r.result,"FINITE_PROBE_UNRESOLVED")
        search=bounded_gram_search(exact_quadratic_screw,
                                   points=(-1,0,1),budget=400)
        self.assertEqual(search["status"],"UNRESOLVED")
        self.assertFalse(search["universal_positivity_proved"])

    def test_unverified_mpmath_or_inconsistent_symmetry_fails_closed(self):
        with self.assertRaises(ReflectionBoundaryError):
            rational_gram_certificate(
                (-1,1),(1,1),lambda x,y: 0.0,
                provenance="uncertified double")
        def asym(x,y):
            return (RationalInterval.exact(2)
                    if x<y else RationalInterval.exact(-2))
        with self.assertRaises(ReflectionBoundaryError):
            rational_gram_certificate(
                (-1,1),(1,1),asym,provenance="broken")
        with self.assertRaises(ReflectionBoundaryError):
            rational_gram_certificate(
                (1,1),(1,2),exact_quartic_screw,provenance="same time")
        with self.assertRaises(ReflectionBoundaryError):
            rational_gram_certificate(
                (-1,1),(0,0),exact_quartic_screw,provenance="zero vector")
        with self.assertRaises(ReflectionBoundaryError):
            rational_gram_certificate(
                (-1,1),(1,1),exact_quartic_screw,provenance="")
        with self.assertRaises(ReflectionBoundaryError):
            bounded_gram_search(exact_quartic_screw,points=(-1,1),budget=0)

    def test_delayed_counterexample_and_finite_search_false_negative(self):
        """A successful finite search only bounds its OWN chosen test family."""
        result=bounded_gram_search(exact_quartic_screw,
                                   points=(0,Q(1,100)),budget=5)
        self.assertEqual(result["status"],"UNRESOLVED")
        self.assertFalse(result["universal_positivity_proved"])
        later=bounded_gram_search(exact_quartic_screw,
                                  points=(-1,0,1),budget=200)
        self.assertEqual(later["status"],"STRICT_NEGATIVE_WITNESS")


if __name__=="__main__":
    unittest.main()
