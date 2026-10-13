"""Exact posterior, source-gate, shape-prior and categorical quotient adversarial tests."""
import unittest
from fractions import Fraction as Q
from itertools import product
from observational_succ.contextual_heuristics import (
    ModelShape,ModelProbe,ProbeReceipt,HeuristicTower,HeuristicError,
    ModelClassMisspecified,shape_prior,bridge_pushforward_posterior,
)


def pair():
    models=(ModelShape("A","c",frozenset(("graph","memory")),3,"T"),
            ModelShape("B","c",frozenset(("graph",)),3,"F"))
    tower=HeuristicTower(models,frozenset(("graph","memory")),
                          source_id="declared",epoch=2,basis_id="b")
    probe=ModelProbe("noisy","c",("yes","no"),
                     {"A":(Q(3,4),Q(1,4)),"B":(Q(1,4),Q(3,4))})
    return tower,probe


def report(instrument,ordinal=1,outcome="yes",**changes):
    args=dict(event_id=f"e{ordinal}",source_id="declared",epoch=2,
              basis_id="b",probe=instrument.name,outcome=outcome,observer="E")
    args.update(changes)
    return ProbeReceipt(**args)


class HeuristicPosteriorTests(unittest.TestCase):
    def test_shape_score_context_weighting(self):
        tower,_=pair()
        self.assertEqual(tower.prior,{"A":Q(2,3),"B":Q(1,3)})
        self.assertEqual(sum(tower.prior.values()),1)

    def test_exact_update_and_posterior_odds(self):
        t,p=pair()
        self.assertEqual(t.forecast(p),{"yes":Q(7,12),"no":Q(5,12)})
        new=t.observe(p,report(p))
        self.assertEqual(new,{"A":Q(6,7),"B":Q(1,7)})
        self.assertEqual(new["A"]/new["B"],Q(6))
        self.assertEqual(t.verdict()["status"],"HEURISTIC_NOT_FORMAL_PROOF")

    def test_expected_quadratic_risk_identity(self):
        t,p=pair()
        self.assertGreater(t.expected_gini_gain(p),0)
        self.assertEqual(t.expected_gini_gain(p,target_relative=False),
                         t.expected_gini_gain(p,target_relative=True))

    def test_exact_perfect_probe_gain(self):
        t,_=pair()
        p=ModelProbe("perfect","c",("A","B"),{"A":(1,0),"B":(0,1)})
        self.assertEqual(t.expected_gini_gain(p),Q(4,9))
        self.assertEqual(t.rank_probes((p,))[0][1],Q(4,9))

    def test_zero_gain_when_all_models_predict_same(self):
        t,_=pair()
        p=ModelProbe("alias","c",("yes","no"),
                     {"A":(Q(1,2),Q(1,2)),"B":(Q(1,2),Q(1,2))})
        self.assertEqual(t.expected_gini_gain(p),0)
        self.assertEqual(t.rank_probes((p,))[0][2],0)
        t.observe(p,report(p))
        self.assertEqual(t.posterior,t.prior)

    def test_target_relevance_can_differ_from_model_relevance(self):
        models=(ModelShape("a","c",frozenset(),2,"same"),
                ModelShape("b","c",frozenset(),2,"same"),
                ModelShape("c","c",frozenset(),2,"other"))
        t=HeuristicTower(models,frozenset(),source_id="declared",epoch=2,basis_id="b",
                         prior={"a":Q(1,4),"b":Q(1,4),"c":Q(1,2)})
        p=ModelProbe("nuisance","c",("left","right"),
                     {"a":(1,0),"b":(0,1),"c":(Q(1,2),Q(1,2))})
        self.assertEqual(t.expected_gini_gain(p,target_relative=True),0)
        self.assertGreater(t.expected_gini_gain(p,target_relative=False),0)

    def test_expected_gini_identity_independent_oracle_300(self):
        for a in range(1,21):
            for b in range(1,16):
                t,_=pair()
                t.posterior={"A":Q(a,a+b),"B":Q(b,a+b)}
                p=ModelProbe("p","c",("0","1"),
                             {"A":(Q(a,a+1),Q(1,a+1)),
                              "B":(Q(b,b+1),Q(1,b+1))})
                gain=t.expected_gini_gain(p)
                assert gain>=0
                base=1-sum((x*x for x in t.posterior.values()),Q(0))
                risk=Q(0)
                for j in range(2):
                    q=sum((t.posterior[k]*p.law(k)[j] for k in t.posterior),Q(0))
                    posterior=[t.posterior[k]*p.law(k)[j]/q for k in t.posterior]
                    risk+=q*(1-sum((u*u for u in posterior),Q(0)))
                self.assertEqual(gain,base-risk)

    def test_correlated_observation_without_conditional_law_rejected(self):
        t,p=pair()
        a=ModelProbe("first","c",p.outcomes,p.kernels,noise_group="sensor-1")
        b=ModelProbe("second","c",p.outcomes,p.kernels,noise_group="sensor-1")
        t.observe(a,report(a,ordinal=1))
        with self.assertRaisesRegex(HeuristicError,"Correlated"):
            t.observe(b,report(b,ordinal=2))
        conditioned=ModelProbe("second-conditional","c",("yes","no"),
                               {"A":(1,0),"B":(1,0)},noise_group="sensor-1",
                               conditioned_on=("e1",))
        before=dict(t.posterior)
        t.observe(conditioned,report(conditioned,ordinal=2))
        self.assertEqual(t.posterior,before)

    def test_forged_conditional_prior_event_rejected(self):
        t,p=pair()
        conditional=ModelProbe("p","c",p.outcomes,p.kernels,
                               noise_group="cal",conditioned_on=("not-seen",))
        with self.assertRaisesRegex(HeuristicError,"unseen"):
            t.observe(conditional,report(conditional))

    def test_duplicate_event_rejected(self):
        t,p=pair()
        t.observe(p,report(p))
        with self.assertRaisesRegex(HeuristicError,"twice"):
            t.observe(p,report(p))

    def test_source_epoch_basis_and_probe_rejected(self):
        for change in ({"source_id":"unrelated"},{"epoch":3},
                       {"basis_id":"new-basis"},{"probe":"wrong"}):
            t,p=pair()
            with self.assertRaises(HeuristicError):t.observe(p,report(p,**change))
            self.assertEqual(t.posterior,t.prior)

    def test_model_class_misspecification_triggers_repair_not_false_certainty(self):
        t,_=pair()
        p=ModelProbe("impossible","c",("yes","no"),
                     {"A":(1,0),"B":(1,0)})
        with self.assertRaises(ModelClassMisspecified):
            t.observe(p,report(p,outcome="no"))
        self.assertEqual(t.posterior,t.prior)
        self.assertEqual(t.events,[])

    def test_high_posterior_is_not_proof(self):
        t,p=pair()
        for i in range(10):
            t.observe(p,report(p,ordinal=i+1))
        self.assertGreater(t.posterior["A"],Q(9999,10000))
        v=t.verdict()
        self.assertFalse(v["source_authenticated"])
        self.assertFalse(v["source_class_exhaustive"])
        self.assertFalse(v["conditional_target_identified"])

    def test_zero_prior_cannot_be_resurrected(self):
        t,p=pair()
        t.posterior={"A":Q(1),"B":Q(0)}
        t.observe(p,report(p,outcome="no"))
        self.assertEqual(t.posterior["B"],0)

    def test_context_mismatch_rejected(self):
        t,p=pair()
        wrong=ModelProbe("same","other",p.outcomes,p.kernels)
        with self.assertRaises(HeuristicError):t.rank_probes((wrong,))

    def test_bad_distributions_and_float_injections_rejected(self):
        for vals in ((Q(1,2),Q(1,3)),(-1,2),(0.7,0.3)):
            with self.assertRaises(HeuristicError):
                ModelProbe("x","c",("y","n"),{"A":vals})
        with self.assertRaises(HeuristicError):
            ModelProbe("x","c",("y",),{"A":(1,)},cost=0)

    def test_capsule_indistinguishable_models_cannot_decide_ontology(self):
        models=(ModelShape("inside","c",frozenset(),2,"internal"),
                ModelShape("outside","c",frozenset(),2,"external"))
        t=HeuristicTower(models,frozenset(),source_id="declared",epoch=2,basis_id="b")
        p=ModelProbe("boundary","c",("yes","no"),
                     {"inside":(Q(3,4),Q(1,4)),"outside":(Q(3,4),Q(1,4))})
        c=t.observational_capsules((p,))
        self.assertEqual(len(c),1)
        self.assertFalse(c[0]["target_defined"])
        for i in range(6):t.observe(p,report(p,ordinal=i+1))
        self.assertEqual(t.posterior["inside"],Q(1,2))
        self.assertFalse(t.verdict()["conditional_target_identified"])

    def test_bridge_naturality_and_forgery(self):
        from observational_succ.heuristic_bridge_discovery import cross_context_analogy_demo
        self.assertEqual(cross_context_analogy_demo()["translated_posterior"],
                         {"Heat:two":Q(2,3),"Heat:three":Q(1,3)})
        a,pa=pair()
        other=(ModelShape("X","other",frozenset(),2,"T"),
               ModelShape("Y","other",frozenset(),2,"F"))
        b=HeuristicTower(other,frozenset(),source_id="s",epoch=0,basis_id="b",
                         prior={"X":a.prior["A"],"Y":a.prior["B"]})
        wrong=ModelProbe("bad","other",pa.outcomes,
                         {"X":(Q(1,2),Q(1,2)),"Y":pa.law("B")})
        with self.assertRaisesRegex(HeuristicError,"not law-preserving"):
            bridge_pushforward_posterior(a,b,{"A":"X","B":"Y"},((pa,wrong),))

    def test_target_alias_with_nontrivial_target_dependent_probs(self):
        t,p=pair()
        with self.assertRaises(HeuristicError):
            t.observational_capsules((ModelProbe("missing","c",("a",),{"A":(1,)}),))

if __name__=="__main__":unittest.main()

class SyntaxCloneTests(unittest.TestCase):
    def test_copying_one_behavior_should_not_double_its_model_prior(self):
        from observational_succ.contextual_heuristics import syntax_clone_counterexample
        r=syntax_clone_counterexample()
        self.assertEqual(r["naive_A_before"],Q(1,2))
        self.assertEqual(r["naive_A_after_syntax_clone"],Q(2,3))
        self.assertEqual(r["quotient_A_before"],Q(1,2))
        self.assertEqual(r["quotient_A_after"],Q(1,2))
        self.assertFalse(r["behavioral_menu_is_exhaustive"])

class BinaryGainFormulaTests(unittest.TestCase):
    def test_closed_form_independent_400_instance_oracle(self):
        from observational_succ.contextual_heuristics import binary_bernoulli_target_gain
        for a in range(1,21):
            for b in range(1,21):
                p=Q(a,21);u=Q(b,21);v=Q(1,3)
                model=(ModelShape("x","c",frozenset(),2,"x"),
                       ModelShape("y","c",frozenset(),2,"y"))
                tower=HeuristicTower(model,frozenset(),source_id="s",epoch=0,basis_id="b",
                                     prior={"x":p,"y":1-p})
                probe=ModelProbe("p","c",("yes","no"),
                                 {"x":(u,1-u),"y":(v,1-v)})
                self.assertEqual(binary_bernoulli_target_gain(p,u,v),
                                 tower.expected_gini_gain(probe))
