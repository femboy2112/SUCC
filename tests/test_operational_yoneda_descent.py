"""Independent tests of genuine bounded Yoneda and source-coalgebra proof descent."""
import random
import unittest
from itertools import product

from observational_succ.core import BudgetExceeded, DomainError
from observational_succ.yoneda import (
    Arrow, validate_yoneda, representable_natural_transform,
    enumerate_natural_transforms,
)
from observational_succ.noncommuting_proof_transport import (
    FiniteCarrier, Instrument, _bit_field,
)
from observational_succ.adaptive_proof_policy import (
    conditional_source_field, solve_adaptive_claim,
)
from observational_succ.operational_yoneda_descent import (
    DescentError, BeliefGame, CertifiedSourceMorphism,
    greatest_goal_bisimulation, duplicate_carrier,
    ObservationPathCategory, restricted_yoneda_arrow_detection,
    least_faithful_context_family, shallow_probe_agreement,
    delayed_separator_models, yoneda_policy_descent_demo,
)


def independent_colored_bisim(left, right):
    """Independent partition-refinement oracle, not pair elimination.

    All reachable belief nodes from both games are included. Colors identify
    identical terminal targets and labeled branching patterns. Iterate until
    partitions stabilize. This is not the production relation-pruning code.
    """
    tagged=[(0,b) for b in left.nodes]+[(1,b) for b in right.nodes]
    def g(tag): return left if tag[0]==0 else right
    sig={tag:(g(tag).goal(tag[1]),) for tag in tagged}
    def colorize(labels):
        names={x:i for i,x in enumerate(sorted(set(labels.values()),
                                               key=repr))}
        return {x:names[label] for x,label in labels.items()}
    colors=colorize(sig)
    for _ in range(2*len(tagged)+2):
        old=colors
        labels={}
        for tag in tagged:
            game=g(tag)
            b=tag[1]
            branches=game.options(b)
            labels[tag]=(
                old[tag],
                tuple(sorted(
                    (name, tuple((outcome,old[(tag[0],child)])
                                 for outcome,child in children))
                    for name,children in branches.items())),
            )
        colors=colorize(labels)
        # stable up to a harmless global renaming if the equivalence
        # relations (color partitions) do not change.
        if all((old[a]==old[b])==(colors[a]==colors[b])
               for a in tagged for b in tagged):
            break
    else: raise AssertionError("Independent finite partition refinement did not settle")
    return colors[(0,left.root)]==colors[(1,right.root)]


def duplicated(field,target):
    cloned,h,pulled=duplicate_carrier(field,target)
    return CertifiedSourceMorphism(
        cloned,field,tuple(range(cloned.count)),tuple(range(field.count)),
        h,pulled,target,"source-target")


class SourceCoalgebraDescentTests(unittest.TestCase):
    def test_adaptive_winning_rank_and_every_receiving_source_replayed(self):
        abstract=conditional_source_field()
        target=("0","1","1","0")
        certificate=duplicated(abstract,target)
        report=certificate.policy_descent()
        self.assertEqual((report["abstract_rank"],report["concrete_rank"]),(2,2))
        self.assertEqual(report["transported_source_replays"],8)
        self.assertTrue(report["source_image_surjective"])
        self.assertTrue(report["source_claim_pullback"])
        self.assertFalse(report["state_map_injective"])
        self.assertFalse(report["independent_physical_provenance_authenticated"])
        rel=greatest_goal_bisimulation(
            BeliefGame.build(abstract,tuple(range(4)),target,target_id="same"),
            BeliefGame.build(certificate.concrete,tuple(range(8)),
                             certificate.t_concrete,target_id="same"))
        self.assertTrue(rel.roots_related)
        self.assertTrue(rel.ranks_equal_if_related)
        for s in range(8):
            trace=rel.transfer_source_policy(s)
            self.assertEqual(trace["claim"],target[s//2])
            self.assertLessEqual(trace["steps"],2)

    def test_same_morphism_transports_LOSING_nonrecoverable_source_claim(self):
        abstract=_bit_field()
        target=("0","1","1","0")
        receipt=duplicated(abstract,target).policy_descent()
        self.assertIsNone(receipt["abstract_rank"])
        self.assertIsNone(receipt["concrete_rank"])
        self.assertTrue(receipt["optimal_original_source_rank_equal"])
        self.assertEqual(receipt["transported_source_replays"],0)

    def test_all_16_original_source_claims_preserved_across_hidden_tag(self):
        abstract=conditional_source_field()
        for labels in product(("0","1"),repeat=4):
            receipt=duplicated(abstract,labels).policy_descent()
            self.assertEqual(receipt["abstract_rank"],receipt["concrete_rank"])
            self.assertEqual(receipt["source_image_surjective"],True)
            self.assertEqual(receipt["checked_action_state_squares"],24)

    def test_independent_exact_fixed_path_corollary_across_noncommuting_source(self):
        system=conditional_source_field()
        target=("0","1","1","0")
        certificate=duplicated(system,target)
        certificate.verify()
        names=tuple(a.name for a in system.actions)
        for length in range(4):
            for word in product(names,repeat=length):
                for x in range(certificate.concrete.count):
                    a=system.run(certificate.h[x],word)
                    c=certificate.concrete.run(x,word)
                    self.assertEqual(a.observed_values,c.observed_values)
                    self.assertEqual(
                        a.terminal_state,
                        certificate.h[c.terminal_state])
                    self.assertEqual(target[certificate.h[x]],
                                     certificate.t_concrete[x])

    def test_mutated_source_claim_outcome_effect_menu_and_source_set_rejected(self):
        a=conditional_source_field()
        t=("0","1","1","0")
        b,h,bt=duplicate_carrier(a,t)
        base=dict(concrete=b,abstract=a,
                  source_concrete=tuple(range(8)),
                  source_abstract=tuple(range(4)),
                  h=h,t_concrete=bt,t_abstract=t,target_id="original-XOR")
        cases=[]
        mismatch=list(bt);mismatch[3]="counterfeit"
        cases.append({**base,"t_concrete":tuple(mismatch)})
        cases.append({**base,"h":(0,)*8})
        cases.append({**base,"source_concrete":(0,1,2,3)})
        # Source-abstraction must be defined for every state, including
        # hidden tags and states presently outside original-source class.
        cases.append({**base,"h":tuple(list(h[:-1])+[9])})
        instruments=list(b.actions)
        wrong=list(instruments[0].outputs);wrong[1]=1-wrong[1]
        instruments[0]=Instrument(instruments[0].name,tuple(wrong),
                                   instruments[0].transitions,
                                   instruments[0].enabled)
        cases.append({**base,"concrete":FiniteCarrier(
            8,tuple(instruments),"mutation","B")})
        instruments=list(b.actions)
        altered=list(instruments[0].transitions)
        altered[0]=4 if altered[0]!=4 else 5
        instruments[0]=Instrument(instruments[0].name,instruments[0].outputs,
                                  tuple(altered),instruments[0].enabled)
        cases.append({**base,"concrete":FiniteCarrier(
            8,tuple(instruments),"mutation","B")})
        instruments=list(b.actions)
        flags=list(instruments[0].enabled);flags[0]=False
        instruments[0]=Instrument(instruments[0].name,instruments[0].outputs,
                                   instruments[0].transitions,tuple(flags))
        cases.append({**base,"concrete":FiniteCarrier(
            8,tuple(instruments),"mutation","B")})
        instruments=list(b.actions)
        instruments[0]=Instrument("forged",instruments[0].outputs,
                                   instruments[0].transitions,
                                   instruments[0].enabled)
        cases.append({**base,"concrete":FiniteCarrier(
            8,tuple(instruments),"mutation","B")})
        for case in cases:
            with self.subTest(case=case["h"][:3],
                              source_count=len(case["source_concrete"])):
                with self.assertRaises(DescentError):
                    CertifiedSourceMorphism(**case).verify()

    def test_exhaustive_small_noncommuting_models_preserve_original_policy_rank(self):
        specs=tuple(product((0,1),repeat=4))
        for i,a in enumerate(specs):
            for j,b in enumerate(specs):
                field=FiniteCarrier(2,(
                    Instrument("A",a[:2],a[2:],(True,True)),
                    Instrument("B",b[:2],b[2:],(True,True)),
                ),f"source-{i}-{j}","v1")
                certificate=duplicated(field,("0","1"))
                self.assertEqual(
                    certificate.policy_descent()["abstract_rank"],
                    solve_adaptive_claim(field,(0,1),("0","1"),
                                         target_id="T").rank)

    def test_global_morphism_noninjectivity_is_not_a_universal_information_loss(self):
        f=conditional_source_field()
        c=duplicated(f,("0","1","1","0"))
        h=c.h
        self.assertNotEqual(0,1)
        self.assertEqual(h[0],h[1])
        self.assertTrue(c.policy_descent()["optimal_original_source_rank_equal"])
        # Source tag is not a physical observer distinction; both hidden
        # representations have identical FULL public future behavior.
        for length in range(4):
            for word in product(("Q","R0","R1"),repeat=length):
                self.assertEqual(c.concrete.run(0,word).observed_values,
                                 c.concrete.run(1,word).observed_values)


class BeliefBisimulationAndProbeTests(unittest.TestCase):
    def test_finite_bisimulation_preserves_rank_when_roots_related(self):
        f=conditional_source_field()
        t=("0","1","1","0")
        a=BeliefGame.build(f,(0,1,2,3),t,target_id="T")
        b=BeliefGame.build(f,(0,1,2,3),t,target_id="T")
        relation=greatest_goal_bisimulation(a,b)
        self.assertTrue(relation.roots_related)
        self.assertTrue(relation.ranks_equal_if_related)
        for x in range(4):
            self.assertEqual(relation.transfer_source_policy(x)["claim"],t[x])

    def test_independent_partition_color_refinement_matches_pair_pruning(self):
        rng=random.Random(900173)
        for case in range(45):
            fields=[]
            for label in ("left","right"):
                sz=rng.choice((2,3))
                actions=[]
                for name in ("A","B"):
                    actions.append(Instrument(
                        name,tuple(rng.randrange(2) for _ in range(sz)),
                        tuple(rng.randrange(sz) for _ in range(sz)),
                        (True,)*sz))
                fields.append(FiniteCarrier(
                    sz,tuple(actions),f"{label}-{case}","v1"))
            games=[
                BeliefGame.build(f,tuple(range(f.count)),
                                 tuple(str(i%2) for i in range(f.count)),
                                 target_id="T")
                for f in fields]
            got=greatest_goal_bisimulation(*games)
            expected=independent_colored_bisim(*games)
            self.assertEqual(got.roots_related,expected)
            if got.roots_related:
                self.assertEqual(games[0].rank(),games[1].rank())

    def test_budget_probes_alias_but_lawful_future_separates(self):
        good,bad=delayed_separator_models()
        sources=(0,1)
        zero=shallow_probe_agreement(good,bad,sources,0)
        one=shallow_probe_agreement(good,bad,sources,1)
        two=shallow_probe_agreement(good,bad,sources,2)
        self.assertTrue(zero["equal"])
        self.assertTrue(one["equal"])
        self.assertFalse(two["equal"])
        self.assertEqual(two["first_distinguishing_word"],("A","B"))
        self.assertEqual(two["distinguishing_source"],1)
        t=("0","1","0","1")
        left=BeliefGame.build(good,sources,t,target_id="fixed-original")
        right=BeliefGame.build(bad,sources,t,target_id="fixed-original")
        self.assertEqual(left.rank(),2)
        self.assertIsNone(right.rank())
        self.assertFalse(greatest_goal_bisimulation(left,right).roots_related)
        with self.assertRaises(DescentError):
            greatest_goal_bisimulation(left,right).transfer_source_policy(0)

    def test_bisimulation_budget_and_source_class_mismatch_not_spoofed(self):
        f=conditional_source_field()
        t=("0","1","1","0")
        a=BeliefGame.build(f,(0,1,2,3),t,target_id="T")
        with self.assertRaises(BudgetExceeded):
            greatest_goal_bisimulation(a,a,max_pairs=1)
        with self.assertRaises(BudgetExceeded):
            BeliefGame.build(f,(0,1,2,3),t,target_id="T",max_nodes=1)
        with self.assertRaises(DescentError):
            BeliefGame.build(f,(0,1,2,3),("a",),target_id="T")


class GenuineYonedaCategoryTests(unittest.TestCase):
    def tiny(self):
        f=FiniteCarrier(1,(
            Instrument("A",(0,),(0,),(True,)),
            Instrument("B",(0,),(0,),(True,)),
        ),"Y","base")
        game=BeliefGame.build(f,(0,),("known",),target_id="constant")
        category=ObservationPathCategory(game,1)
        root=0
        leaf=next(i for i,(h,_) in enumerate(category.contexts) if h==0)
        return category,root,leaf

    def test_literal_full_yoneda_recovers_both_actual_observation_arrows(self):
        c,x,y=self.tiny()
        paths=c.hom(x,y)
        self.assertEqual(len(paths),2)
        self.assertEqual({c.pretty_path(p) for p in paths},
                         {(("A",0),),(("B",0),)})
        full=validate_yoneda(c,x,y)
        self.assertEqual(full["source_hom_count"],2)
        self.assertEqual(full["natural_transform_count"],2)
        self.assertTrue(full["surjective"])
        different=[
            representable_natural_transform(c,p,c.objects) for p in paths]
        self.assertNotEqual(different[0],different[1])
        self.assertEqual(
            set(tuple(p.word) for p in paths),{(1,),(2,)})

    def test_restricted_real_category_representables_collapse_distinct_paths(self):
        c,x,y=self.tiny()
        arrows=c.hom(x,y)
        local=(y,)
        restricted=validate_yoneda(c,x,y,local)
        self.assertEqual(restricted["source_hom_count"],2)
        self.assertEqual(restricted["natural_transform_count"],1)
        self.assertEqual(
            representable_natural_transform(c,arrows[0],local),
            representable_natural_transform(c,arrows[1],local))
        # Spurious inference: one weak probe context would report those
        # distinct arrows as identical; FULL Yoneda correctly separates.
        self.assertNotEqual(arrows[0],arrows[1])

    def test_restricted_faithfulness_iff_joint_precomposition_separator(self):
        category,source,target=self.tiny()
        weak=restricted_yoneda_arrow_detection(
            category,source,target,(target,))
        self.assertFalse(weak["faithful_on_selected_hom"])
        self.assertEqual(weak["distinct_arrow_pairs"],1)
        self.assertEqual(weak["detected_pairs"],0)
        self.assertEqual(len(weak["undetected_pairs"]),1)
        self.assertEqual(weak["undetected_pairs"][0],((1,),(2,)))
        strong=restricted_yoneda_arrow_detection(
            category,source,target,(source,))
        self.assertTrue(strong["faithful_on_selected_hom"])
        self.assertEqual(strong["detected_pairs"],1)
        self.assertEqual(strong["context_lamps"][0][2],(source,()))
        minimal=least_faithful_context_family(category,source,target)
        self.assertEqual(minimal["minimum_context_objects"],(source,))
        self.assertEqual(minimal["minimum_context_count"],1)
        self.assertFalse(minimal["physical_probe_cost_minimized"])
        for J in ((),(source,),(target,),(source,target)):
            result=restricted_yoneda_arrow_detection(
                category,source,target,J)
            self.assertEqual(result["faithful_on_selected_hom"],
                             source in J)
        with self.assertRaises(DomainError):
            restricted_yoneda_arrow_detection(
                category,source,target,(source,source))
        with self.assertRaises(DomainError):
            restricted_yoneda_arrow_detection(
                category,source,target,(999,))
        with self.assertRaises(BudgetExceeded):
            least_faithful_context_family(
                category,source,target,max_subsets=1)

    def test_full_yoneda_pairwise_naturality_on_real_belief_paths(self):
        c,x,y=self.tiny()
        identities={i:c.identity(i) for i in c.objects}
        for arrow in c.hom(x,y):
            eta=representable_natural_transform(c,arrow,c.objects)
            self.assertEqual(eta[x][identities[x]],arrow)
            for obj in c.objects:
                for h in c.hom(obj,x):
                    self.assertEqual(eta[obj][h],c.compose(arrow,h))
        self.assertEqual(len(enumerate_natural_transforms(
            c,x,y,c.objects)),len(c.hom(x,y)))

    def test_category_identity_composition_associativity_and_forgery(self):
        f=conditional_source_field()
        game=BeliefGame.build(f,(0,1,2,3),
                              ("0","1","1","0"),target_id="parity")
        c=ObservationPathCategory(game,3,max_objects=96)
        self.assertGreater(len(c.objects),3)
        all_arrows=[
            p for x in c.objects for y in c.objects for p in c.hom(x,y)]
        self.assertGreater(len(all_arrows),len(c.objects))
        for a in all_arrows:
            self.assertEqual(c.compose(c.identity(a.target),a),a)
            self.assertEqual(c.compose(a,c.identity(a.source)),a)
            self.assertEqual(len(c.pretty_path(a)),len(a.word))
        # Enumerate actual 3-level compositions from the root, not a
        # merely syntactic free monoid without intermediate state checks.
        triples=0
        atomic=[a for a in all_arrows if len(a.word)==1]
        for a in atomic:
            for b in atomic:
                if a.target!=b.source:continue
                ab=c.compose(b,a)
                for d in atomic:
                    if b.target!=d.source:continue
                    self.assertEqual(c.compose(d,ab),
                                     c.compose(c.compose(d,b),a))
                    triples+=1
        self.assertGreater(triples,0)
        with self.assertRaises(DomainError):
            c.compose(Arrow(0,0,(999999,)),c.identity(0))
        with self.assertRaises(DomainError):
            c.hom(0,len(c.objects)+1)

    def test_path_category_horizon_does_not_invent_transfinite_source_data(self):
        f=conditional_source_field()
        g=BeliefGame.build(f,(0,1,2,3),
                            ("0","1","1","0"),target_id="T")
        with self.assertRaises(BudgetExceeded):
            ObservationPathCategory(g,4,max_objects=1)
        with self.assertRaises(DescentError):
            ObservationPathCategory(g,-1)
        with self.assertRaises(DescentError):
            ObservationPathCategory(g,6)
        c=ObservationPathCategory(g,2)
        self.assertTrue(all(
            c.contexts[i][0]>=c.contexts[j][0]
            for i in c.objects for j in c.objects if c.hom(i,j)))

    def test_machine_receipt_enforces_all_boundaries(self):
        x=yoneda_policy_descent_demo()
        self.assertEqual(x["status"],
                         "OPERATIONAL_YONEDA_SOURCE_POLICY_DESCENT_EXACT")
        self.assertEqual(x["full_yoneda_natural_transforms"],2)
        self.assertEqual(x["full_yoneda_actual_distinct_arrows"],2)
        self.assertEqual(x["restricted_yoneda_natural_transforms"],1)
        self.assertTrue(x["restricted_context_collapses_distinct_arrows"])
        self.assertEqual(x["restricted_arrow_pairs_undetected"],1)
        self.assertEqual(x["full_arrow_pairs_detected"],1)
        self.assertEqual(x["minimum_faithful_context_count"],1)
        self.assertTrue(x["minimum_faithful_context_is_source"])
        self.assertTrue(x["noninjective_carrier_abstraction_preserves_winning_rank"])
        self.assertEqual(x["abstract_optimal_rank"],2)
        self.assertEqual(x["concrete_optimal_rank"],2)
        self.assertEqual(x["successful_concrete_policy_source_replays"],8)
        self.assertTrue(x["losing_original_parity_preserved_as_losing"])
        self.assertTrue(x["one_probe_model_signature_equal"])
        self.assertFalse(x["two_probe_model_signature_equal"])
        self.assertEqual(x["two_probe_discriminator"],["A","B"])
        self.assertEqual(x["good_model_winning_rank"],2)
        self.assertTrue(x["bad_model_has_no_finite_winning_policy"])
        self.assertTrue(x["root_bisimulation_rejects_shallow_alias"])
        self.assertFalse(x["independent_physical_source_attested"])
        self.assertTrue(x["Yoneda_fullness_does_not_imply_physical_or_RH_positivity"])


if __name__=="__main__":
    unittest.main()
