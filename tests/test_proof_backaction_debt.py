"""Hostile mathematical tests for source-changing proof-support and Zeno debt.

Distinct tests: independent source-tail enumeration (not the source model's
verdict helper), independent recurrence loops, independent digit-fiber
certification from PR #19, transient counterexamples, physically scoped
single-carrier no-go and explicitly hypothetical omega timestamps.
"""
from fractions import Fraction
from itertools import product
import unittest

from observational_succ.proof_backaction_debt import (
    BackactionError, SupportCarrier, support_frontier_formula,
    support_transport_law, PrecisionDebtChase, zeno_clock,
    proof_backaction_debt_demo,
)
from observational_succ.precision_transport import (
    ClaimContext, certify_transport,
)
from observational_succ.probe_coherence import (
    InitialSource, DestructiveCarrier,
    independent_carrier_repair, nondestructive_probe_repair,
)


class SupportBackactionTests(unittest.TestCase):
    def test_exact_independent_conservation_all_three_birth_rules(self):
        for mode in ("proportional", "matched", "frozen"):
            for initial in range(1, 5):
                for k0 in range(3):
                    for alpha in range(3):
                        for n in range(0, 8):
                            births = 0
                            active = initial
                            pending = initial
                            for i in range(1, n + 1):
                                if pending == 0:
                                    break
                                born = (alpha*(k0+i) if mode == "proportional"
                                        else 1 if mode == "matched" else 0)
                                births += born
                                active += born
                                pending = pending-1+born
                            else:
                                prediction = support_frontier_formula(
                                    initial, k0, alpha, n, mode)
                                self.assertEqual(prediction["active"], active)
                                self.assertEqual(prediction["debt"], pending)
                                self.assertEqual(prediction["observed"], n)
                                self.assertEqual(prediction["new_obligations"], births)

    def test_actual_carrier_actions_and_knowledge_indexed_births(self):
        carrier = SupportCarrier((0,)*130, active=1)
        predicted = [1, 1, 2, 4, 7, 11, 16, 22, 29]
        for n, d in enumerate(predicted):
            self.assertEqual(carrier.debt, d)
            self.assertEqual(carrier.K, n)
            self.assertEqual(carrier.verdict, "unresolved")
            self.assertEqual(carrier.compatible_target_values,(False, True))
            if n+1 < len(predicted):
                next_carrier, event = carrier.probe()
                self.assertEqual(event.index, n)
                self.assertEqual(event.bit, 0)
                self.assertEqual(event.after_knowledge, n+1)
                self.assertEqual(event.births, n+1)
                self.assertEqual(next_carrier.active, carrier.active+n+1)
                self.assertNotEqual(next_carrier.target_contract, carrier.target_contract)
                self.assertEqual(next_carrier.observed, carrier.observed+(0,))
                self.assertEqual(next_carrier.source_id,carrier.source_id)
                self.assertEqual(next_carrier.tape, carrier.tape)
                carrier = next_carrier

    def test_same_evidence_both_truth_values_in_independent_latent_sources(self):
        # All 2^8 possible latent tapes; probe acts on active support, but
        # the simulator must NOT infer all-zero from its stored true tape.
        buckets = {}
        for bits in product((0, 1), repeat=8):
            carrier = SupportCarrier(bits, active=1)
            for _ in range(2):
                carrier, _ = carrier.probe()
            self.assertEqual((carrier.active, len(carrier.observed)), (4, 2))
            actually_true = all(x == 0 for x in bits[:carrier.active])
            if carrier.verdict == "certified-true":
                self.assertTrue(actually_true)
            if carrier.verdict == "refuted":
                self.assertFalse(actually_true)
            if carrier.verdict == "unresolved":
                self.assertEqual(carrier.compatible_target_values,(False,True))
                self.assertEqual(carrier.possible_false_witness(),2)
            buckets.setdefault(carrier.observed,set()).add(actually_true)
        self.assertEqual(buckets[(0,0)],{False,True})
        for observed in ((0,1),(1,0),(1,1)):
            self.assertEqual(buckets[observed],{False})

    def test_one_way_truth_and_refutation_transport_under_active_expansion(self):
        for old in range(1,7):
            for new in range(old,7):
                law=support_transport_law(old,new)
                self.assertTrue(law["reverse_true_valid_for_all_sources"])
                self.assertTrue(law["forward_refutation_valid_for_all_sources"])
                for bits in product((0,1),repeat=new):
                    old_true=not any(bits[:old])
                    new_true=not any(bits[:new])
                    if new_true:
                        self.assertTrue(old_true)
                    if not old_true:
                        self.assertFalse(new_true)
                    if old==new:
                        self.assertEqual(old_true,new_true)
                if new>old:
                    mutant=(0,)*old+(1,)+(0,)*(new-old-1)
                    self.assertTrue(not any(mutant[:old]))
                    self.assertFalse(not any(mutant[:new]))
                    self.assertFalse(law["forward_true_valid_for_all_sources"])
                    self.assertEqual(law["new_support_counterexample_bit"],old)
                else:
                    self.assertTrue(law["forward_true_valid_for_all_sources"])
                    self.assertIsNone(law["new_support_counterexample_bit"])

    def test_frozen_support_closes_and_matched_support_does_not(self):
        frozen=SupportCarrier((0,0,0,0),active=3,birth_mode="frozen")
        self.assertEqual(frozen.debt,3)
        for debt in (2,1,0):
            frozen, event=frozen.probe()
            self.assertEqual(event.births,0)
            self.assertEqual(frozen.debt,debt)
        self.assertEqual(frozen.verdict,"certified-true")
        self.assertEqual(frozen.compatible_target_values,(True,))
        with self.assertRaises(BackactionError):
            frozen.probe()
        matched=SupportCarrier((0,)*40,active=1,birth_mode="matched")
        for i in range(20):
            self.assertEqual(matched.debt,1)
            self.assertEqual(matched.verdict,"unresolved")
            matched,event=matched.probe()
            self.assertEqual(event.births,1)
        self.assertEqual(matched.debt,1)

    def test_negative_witness_finitely_refutes_moving_target(self):
        for first_one in (0,1,2,3):
            bits=(0,)*first_one+(1,)+(0,)*70
            state=SupportCarrier(bits,active=1)
            for n in range(first_one+1):
                state,_=state.probe()
                if n<first_one:
                    self.assertEqual(state.verdict,"unresolved")
            self.assertEqual(state.verdict,"refuted")
            self.assertEqual(state.compatible_target_values,(False,))
            self.assertIsNone(state.possible_false_witness())

    def test_finite_simulator_exhaustion_is_not_a_theorem_about_omega(self):
        state=SupportCarrier((0,)*4,active=1)
        state,_=state.probe()
        state,_=state.probe()
        self.assertEqual(state.active,4)
        with self.assertRaises(BackactionError):
            state.probe()
        with self.assertRaises(BackactionError):
            support_frontier_formula(1,0,0,2,"frozen")

    def test_fake_source_histories_and_invalid_inputs_rejected(self):
        with self.assertRaises(BackactionError):
            SupportCarrier((0,1),active=1,observed=(1,),epoch=1)
        with self.assertRaises(BackactionError):
            SupportCarrier((0,1),active=1,observed=(0,),epoch=0)
        with self.assertRaises(BackactionError):
            SupportCarrier((0,1),active=3)
        with self.assertRaises(BackactionError):
            SupportCarrier((False,0))
        with self.assertRaises(BackactionError):
            SupportCarrier((0,1),birth_mode="unknown")
        with self.assertRaises(BackactionError):
            support_transport_law(3,2)
        with self.assertRaises(BackactionError):
            support_transport_law(0,1)
        with self.assertRaises(BackactionError):
            zeno_clock(-1)

    def test_omega_pointwise_clearance_does_not_mean_any_finite_closure(self):
        for n in range(1,120):
            frame=support_frontier_formula(1,0,1,n)
            self.assertGreater(frame["debt"],0)
            self.assertGreaterEqual(frame["active"],frame["observed"]+1)
            self.assertEqual(frame["observed"],n)
            # Every *fixed* bit index j is eventually observed at n=j+1.
            j=n-1
            self.assertTrue(j<frame["observed"])
            self.assertTrue(j<frame["active"])
        # Unbounded pending CARDINALITY is compatible with pointwise
        # eventual clearing of every fixed obligation: nonuniform limit.
        self.assertLess(support_frontier_formula(1,0,1,10)["debt"],
                        support_frontier_formula(1,0,1,119)["debt"])

    def test_geometric_zeno_timestamps_do_not_execute_omega(self):
        self.assertEqual(zeno_clock(0),Fraction(0))
        self.assertEqual(zeno_clock(1),Fraction(1,2))
        self.assertEqual(zeno_clock(4),Fraction(15,16))
        for n in range(1,30):
            self.assertEqual(zeno_clock(n)-zeno_clock(n-1),
                             Fraction(1,2**n))
            self.assertLess(zeno_clock(n),Fraction(1))
        with self.assertRaises(BackactionError):
            zeno_clock(2049)


class PrecisionDebtDynamicsTests(unittest.TestCase):
    def test_precision_matched_shortfall_exactly_constant(self):
        for alpha,k0 in product((0,1,2,3),(0,1,4)):
            chase=PrecisionDebtChase(5,3,2,k0,alpha,0,1,"matched")
            baseline=chase.at(0)["shortfall"]
            for n in range(25):
                row=chase.at(n)
                self.assertEqual(row["K"],k0+n)
                self.assertEqual(row["shortfall"],baseline)
                self.assertFalse(row["claim_channel_decodable"])
            self.assertIsNone(chase.exact_first_decodable_stage())

    def test_overtaking_reaches_finite_stage_and_matching_does_not(self):
        for gap in range(1,9):
            for surplus in range(1,7):
                chase=PrecisionDebtChase(
                    5,3,1,0,1,gap,1,"surplus",surplus=surplus)
                expected=(gap+surplus-1)//surplus
                self.assertEqual(chase.at(0)["shortfall"],gap)
                self.assertEqual(chase.exact_first_decodable_stage(),expected)
                if expected>0:
                    self.assertFalse(chase.at(expected-1)["claim_channel_decodable"])
                self.assertTrue(chase.at(expected)["claim_channel_decodable"])

    def test_fixed_capacity_exact_first_stage_against_independent_bounded_oracle(self):
        # Exhaust enough parameters to validate the discrete-convex theorem.
        for alpha,cap,k0,v0,q0 in product(
                range(4),range(9),range(4),range(5),range(1,5)):
            chase=PrecisionDebtChase(3,4,3,k0,alpha,v0,q0,
                                     "fixed",fixed_capacity=cap)
            first=next((n for n in range(101)
                        if chase.at(n)["claim_channel_decodable"]),None)
            self.assertEqual(chase.exact_first_decodable_stage(),first)

    def test_eventual_quadratic_dominance_has_transient_success_counterexample(self):
        chase=PrecisionDebtChase(5,2,2,0,1,0,1,"fixed",fixed_capacity=3)
        self.assertEqual(chase.at(0)["shortfall"],1)
        self.assertEqual(chase.exact_first_decodable_stage(),1)
        self.assertTrue(chase.at(1)["claim_channel_decodable"])
        self.assertFalse(chase.at(8)["claim_channel_decodable"])
        # Thus asymptotic increasing debt does not imply never previously solved.

    def test_nonzero_claim_fiber_matches_independent_transport_theorem(self):
        p,r=5,2
        source=ClaimContext.from_mapping(
            p,r,{x:str(x//5) for x in range(25)},
            source_id="independent",basis_id="v1",claim_id="high")
        chase=PrecisionDebtChase(p,r,2,0,1,0,1,"matched")
        for n in range(5):
            f=chase.finite_frame(n)
            self.assertEqual(certify_transport(source,f).valid,
                             chase.at(n)["claim_channel_decodable"])
            self.assertFalse(certify_transport(source,f).valid)
        faster=PrecisionDebtChase(p,r,2,0,1,0,1,"surplus",surplus=1)
        for n in range(4):
            f=faster.finite_frame(n)
            self.assertEqual(certify_transport(source,f).valid,
                             faster.at(n)["claim_channel_decodable"])

    def test_combined_retained_history_cannot_be_worse_than_old_certificate(self):
        transient=PrecisionDebtChase(
            5,2,2,0,1,0,1,"fixed",fixed_capacity=3)
        self.assertEqual(transient.exact_first_decodable_stage(),1)
        self.assertFalse(transient.at(8)["claim_channel_decodable"])
        self.assertTrue(transient.history_at(8)["joint_claim_decodable"])
        self.assertFalse(transient.history_at(8)["current_claim_decodable"])
        self.assertEqual(transient.history_at(8)["best_retained_stage"],2)
        self.assertEqual(transient.history_at(8)["joint_source_digit_depth"],2)
        matched=PrecisionDebtChase(5,2,2,0,1,0,1,"matched")
        for n in range(25):
            self.assertFalse(matched.history_at(n)["joint_claim_decodable"])
            self.assertEqual(matched.history_at(n)["joint_source_digit_depth"],1)
            self.assertEqual(matched.history_at(n)["best_retained_stage"],0)

    def test_joint_observation_fibers_against_independent_congruence_oracle(self):
        # A family of honest fixed-source observations determines precisely
        # the intersection of congruence kernels. At a stage, that is the
        # finest input digit depth of ANY measurement retained thus far.
        for mode,cap,extra in (
            ("fixed",3,0),("fixed",1,0),("matched",0,0),
            ("surplus",0,1)):
            chase=PrecisionDebtChase(
                5,2,2,0,1,0,1,mode,
                fixed_capacity=cap,surplus=extra)
            messages={x:[] for x in range(25)}
            for n in range(4):
                frame=chase.finite_frame(n)
                for x in range(25):
                    messages[x].append(frame.observe(x))
                history=chase.history_at(n)
                depth=history["joint_source_digit_depth"]
                group={}
                for x in range(25):
                    key=tuple(messages[x])
                    group.setdefault(key,set()).add(x)
                self.assertEqual(len(group),5**depth)
                for xs in group.values():
                    self.assertEqual(len(xs),5**(2-depth))
                for x in range(25):
                    for y in range(25):
                        self.assertEqual(messages[x]==messages[y],
                                         (x-y)%(5**depth)==0)
                # High-digit target on all 25 sources requires 2 digits.
                self.assertEqual(history["joint_claim_decodable"],depth>=2)
                self.assertFalse(history["source_payload_changes_assumed"])
                self.assertFalse(history["history_physically_authenticated"])

    def test_historical_first_resolution_complete_for_bounded_schedules(self):
        for alpha,capacity,k0 in product(range(4),range(7),range(3)):
            chase=PrecisionDebtChase(
                3,3,2,k0,alpha,0,1,"fixed",
                fixed_capacity=capacity)
            for n in range(20):
                history=chase.history_at(n)
                best=min(range(n+1),key=lambda j:chase.at(j)["shortfall"])
                minimum=chase.at(best)["shortfall"]
                self.assertEqual(
                    history["minimum_history_shortfall"],minimum)
                self.assertEqual(
                    history["joint_claim_decodable"],minimum<=0)
                self.assertEqual(
                    history["joint_source_digit_depth"],
                    min(chase.r,max(0,chase.k-minimum)))

    def test_wrong_primes_invalid_claim_depth_and_large_materialization_blocked(self):
        for kwargs in (
            dict(p=6,r=2,k=1,K0=0,alpha=1,v0=0,q0=1,schedule="matched"),
            dict(p=5,r=2,k=3,K0=0,alpha=1,v0=0,q0=1,schedule="matched"),
            dict(p=5,r=2,k=0,K0=0,alpha=1,v0=0,q0=1,schedule="matched"),
            dict(p=5,r=2,k=1,K0=0,alpha=1,v0=0,q0=1,schedule="surplus",surplus=0),
        ):
            with self.assertRaises(BackactionError):
                PrecisionDebtChase(**kwargs)
        chase=PrecisionDebtChase(5,2,1,0,10,0,1,"matched")
        with self.assertRaises(BackactionError):
            chase.finite_frame(3)


class PhysicalCarrierProvenanceControls(unittest.TestCase):
    def test_destructive_fixed_source_is_different_no_go_mechanism(self):
        for a,b in product((0,1),repeat=2):
            source=InitialSource(a,b)
            carrier=DestructiveCarrier.from_source(source)
            following=carrier.probe("a").probe("b")
            self.assertEqual(following.initial_support(),{"a":a})
            self.assertIsNone(following.target_certificate())
            self.assertEqual(independent_carrier_repair(source),a^b)
            self.assertEqual(nondestructive_probe_repair(source),a^b)

    def test_machine_receipt_enforces_negative_claims(self):
        receipt=proof_backaction_debt_demo()
        self.assertEqual(receipt["status"],
                         "SOURCE_BACKACTION_PROOF_DEBT_AND_ZENO_EXACT")
        self.assertEqual(receipt["proportional_debt_first_nine_stages"],
                         [1,1,2,4,7,11,16,22,29])
        self.assertTrue(receipt["matching_births_no_finite_zero_certificate"])
        self.assertFalse(receipt["old_true_forward_transport_universal"])
        self.assertTrue(receipt["old_refutation_forward_transport_universal"])
        self.assertEqual(receipt["rate_matched_precision_shortfall_stage_0"],1)
        self.assertEqual(receipt["rate_matched_precision_shortfall_stage_4"],1)
        self.assertIsNone(receipt["rate_matched_precision_first_decodable_stage"])
        self.assertEqual(receipt["overtaking_precision_first_decodable_stage"],1)
        self.assertTrue(receipt["early_transient_can_decide_despite_later_debt"])
        self.assertTrue(receipt["transient_earlier_proof_remains_in_joint_history"])
        self.assertFalse(receipt["transient_current_channel_loses_decodability"])
        self.assertFalse(receipt["matched_joint_history_cannot_resolve_original_gap"])
        self.assertEqual(receipt["matched_joint_history_digit_depth"],1)
        self.assertFalse(any(receipt["independent_precision_transport_oracle_matched"]))
        self.assertEqual(receipt["zeno_t_four"],"15/16")
        self.assertEqual(receipt["zeno_t_eight"],"255/256")
        self.assertFalse(receipt["omega_probe_event_executed"])
        self.assertTrue(receipt["destructive_single_carrier_original_parity_impossible"])
        self.assertTrue(receipt["independent_carrier_restores_original_parity"])
        self.assertFalse(receipt["physical_information_time_or_RH_theorem_claimed"])


if __name__=="__main__":
    unittest.main()
