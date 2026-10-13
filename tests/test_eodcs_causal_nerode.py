"""Hostile source-changing transport / repair, all contracts checkable."""
import unittest
from fractions import Fraction as Q
from itertools import product
from random import Random

from observational_succ.causal_nerode_succ import (
    SourceChart, CausalInstrument, SourceTransportError, causal_descent,
    verify_refinement_factorization, compose_instruments, audit_original_claim,
    causal_repair_demo,
)


def chart(source, epoch, states, obs, basis="b"):
    return SourceChart(source, epoch, basis, tuple(states), tuple(obs))


def partitions(states):
    """Independent exhaustive RGS partition oracle (Bell numbers)."""
    n = len(states)
    for rgs in product(range(n), repeat=n):
        if not rgs or rgs[0] != 0:
            continue
        if all(rgs[i] <= 1+max(rgs[:i]) for i in range(1,n)):
            yield tuple((s, str(i)) for s, i in zip(states, rgs))


class TestCausalDescent(unittest.TestCase):
    def test_state_change_demands_new_report_and_repairs_exactly(self):
        demo = causal_repair_demo()
        self.assertFalse(demo["one_step_source_obstruction"]["one_step_v_exists"])
        self.assertEqual(demo["one_step_source_obstruction"]["pair"], ["00","01"])
        self.assertEqual(demo["one_step_source_obstruction"]["minimum_new_binary_bits"], 1)
        self.assertEqual(demo["one_step_source_obstruction"]["canonical_augmented_states"], 4)
        self.assertTrue(demo["second_step_observational_identity"])
        self.assertTrue(demo["first_step_obstruction_not_erased"])
        self.assertTrue(demo["claim_transport_not_automatic"])
        self.assertFalse(demo["physical_reset_and_probe_available"])

    def test_exact_four_state_repair_factors_through_all_sufficient_partitions(self):
        states=("00","01","10","11")
        before=chart("s",0,states,("0","0","1","1"))
        after=chart("s",1,states,("0","0","1","1"))
        instrument=CausalInstrument("flip",before,after,("00","10","01","11"))
        cert=causal_descent(instrument)
        pair=dict(cert.repaired_reports)
        seen=0
        for r in partitions(states):
            if verify_refinement_factorization(instrument,r):
                seen+=1
                tags=dict(r)
                for s in states:
                    for t in states:
                        if tags[s]==tags[t]:
                            self.assertEqual(pair[s],pair[t])
        self.assertGreater(seen,0)
        # Minimality: every sufficient map has >= |image canonical pair|
        self.assertEqual(min(len(set(dict(r).values())) for r in partitions(states)
                             if verify_refinement_factorization(instrument,r)),
                         cert.repaired_report_classes)

    def test_all_1728_three_state_source_squares_independent_function_oracle(self):
        states=("a","b","c")
        candidate_outputs=("0","1")
        for old_obs in product(candidate_outputs,repeat=3):
            src=chart("s",0,states,old_obs)
            for new_obs in product(candidate_outputs,repeat=3):
                dst=chart("s",1,states,new_obs)
                for u in product(states,repeat=3):
                    instrument=CausalInstrument("U",src,dst,u)
                    cert=causal_descent(instrument)
                    image=src.image()
                    possible_v=any(all(dict(zip(image,vals))[src.report(s)]==
                                       dst.report(dict(zip(states,u))[s])
                                       for s in states)
                                   for vals in product(dst.image(),repeat=len(image)))
                    self.assertEqual(cert.descended,possible_v)
                    canonical=dict(cert.repaired_reports)
                    self.assertEqual(cert.repaired_report_classes,
                                     len(set(canonical.values())))
                    if cert.descended:
                        decoded=dict(cert.observed_successor)
                        self.assertTrue(all(decoded[src.report(s)]==
                                            instrument.future_report(s)
                                            for s in states))
                    else:
                        w=cert.witness
                        self.assertEqual(src.report(w.state_a),src.report(w.state_b))
                        self.assertNotEqual(instrument.future_report(w.state_a),
                                            instrument.future_report(w.state_b))

    def test_independent_fixed_width_bit_lower_bound_and_explicit_codes(self):
        rng=Random(712)
        states=("a","b","c","d")
        for _ in range(130):
            src=chart("s",0,states,tuple(str(rng.randrange(3)) for _ in states))
            dst=chart("s",1,states,tuple(str(rng.randrange(3)) for _ in states))
            u=tuple(rng.choice(states) for _ in states)
            inst=CausalInstrument("U",src,dst,u)
            cert=causal_descent(inst)
            codes=dict(cert.extra_code)
            bits=cert.minimum_extra_fixed_width_bits
            self.assertTrue(all(len(c)==bits for c in codes.values()))
            self.assertTrue(all(src.report(a)!=src.report(b)
                                or inst.future_report(a)==inst.future_report(b)
                                or codes[a]!=codes[b]
                                for a,b in product(states,repeat=2)))
            # Hostile shorter alphabet could not distinguish all successors.
            for smaller in range(bits):
                alphabet=tuple(str(i) for i in range(2**smaller))
                self.assertFalse(any(
                    all(src.report(a)!=src.report(b)
                        or inst.future_report(a)==inst.future_report(b)
                        or code[i]!=code[j]
                        for i,a in enumerate(states)
                        for j,b in enumerate(states))
                    for code in product(alphabet,repeat=len(states))))

    def test_composite_can_descend_despite_intermediate_failure(self):
        states=("00","01","10","11")
        src=chart("s",0,states,("0","0","1","1"))
        mid=chart("s",1,states,("0","0","1","1"))
        end=chart("s",2,states,("0","0","1","1"))
        swap=("00","10","01","11")
        a=CausalInstrument("swap",src,mid,swap)
        b=CausalInstrument("swap",mid,end,swap)
        self.assertFalse(causal_descent(a).descended)
        self.assertFalse(causal_descent(b).descended)
        combined=compose_instruments(a,b)
        self.assertTrue(causal_descent(combined).descended)
        self.assertEqual(dict(causal_descent(combined).observed_successor),
                         {"0":"0","1":"1"})

    def test_lawful_composed_squares_are_lawful(self):
        rng=Random(91)
        for _ in range(80):
            states=("a","b","c")
            obs=tuple(str(rng.randrange(2)) for _ in states)
            first=chart("s",0,states,obs)
            mid=chart("s",1,states,obs)
            last=chart("s",2,states,obs)
            # Identity intervention must descend; the second, if it does,
            # composes as the formal Lean theorem predicts.
            u=CausalInstrument("id",first,mid,states)
            v=CausalInstrument("id2",mid,last,states)
            self.assertTrue(causal_descent(u).descended)
            self.assertTrue(causal_descent(v).descended)
            self.assertTrue(causal_descent(compose_instruments(u,v)).descended)

    def test_claim_truth_is_not_inherited_from_square_commutation(self):
        s=("0","1")
        c=chart("s",0,s,("false","true"))
        inst=CausalInstrument("id",c,c,s)
        cert=causal_descent(inst)
        self.assertTrue(cert.descended)
        failed=audit_original_claim(inst,(False,True),(True,False))
        self.assertTrue(failed.observation_square_commutes)
        self.assertFalse(failed.intervention_preserves_original_claim)
        self.assertFalse(failed.original_claim_transport_certified)
        fixed=audit_original_claim(inst,(False,True),(False,True))
        self.assertTrue(fixed.original_claim_transport_certified)

    def test_source_basis_epoch_and_reset_forgery_fail_closed(self):
        s=("a","b")
        a=chart("s",0,s,("0","1"))
        b=chart("s",1,s,("0","1"))
        with self.assertRaises(SourceTransportError):
            CausalInstrument("bad",a,chart("different",1,s,("0","1")),s)
        with self.assertRaises(SourceTransportError):
            CausalInstrument("bad",b,a,s)
        with self.assertRaises(SourceTransportError):
            CausalInstrument("bad",a,chart("s",1,s,("0","1"),"other"),s)
        with self.assertRaises(SourceTransportError):
            CausalInstrument("bad",a,b,s,source_authenticated=True)
        with self.assertRaises(SourceTransportError):
            compose_instruments(CausalInstrument("a",a,b,s),
                                CausalInstrument("b",a,b,s))
        with self.assertRaises(SourceTransportError):
            verify_refinement_factorization(CausalInstrument("a",a,b,s),
                                            (("b","x"),("a","y")))
        with self.assertRaises(SourceTransportError):
            audit_original_claim(CausalInstrument("a",a,b,s),(0,1),(False,True))

    def test_small_zero_information_source_always_descends(self):
        states=("a","b","c")
        for step in product(states,repeat=3):
            before=chart("s",0,states,("0","0","0"))
            after=chart("s",1,states,("0","0","0"))
            cert=causal_descent(CausalInstrument("U",before,after,step))
            self.assertTrue(cert.descended)
            self.assertEqual(cert.minimum_extra_fixed_width_bits,0)
            self.assertEqual(cert.repaired_report_classes,1)


if __name__=="__main__":
    unittest.main()
