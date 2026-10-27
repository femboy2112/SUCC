"""Global referee tests: true-source compatibility, null calibration, no false pi theorem.

Independent enumerations check the exact formulas. The source-history tests
in this file use the preexisting native SUCC APIs, not a pi digit oracle.
"""
from __future__ import annotations

import unittest
from fractions import Fraction as Q
from math import gcd

from observational_succ import wtf_global_calibration as w


class ExactFiniteArithmetic(unittest.TestCase):
    def test_mobius_totient_kluyver(self):
        expect={1:1,2:-1,3:-1,4:0,6:1,8:0,9:0,10:1,30:-1}
        for n,v in expect.items():
            self.assertEqual(w.mobius(n),v)
        for q in (1,2,3,4,5,8,9,16,32,45,60):
            for d in (-2*q,-q,-1,0,1,2,5,q,q+1):
                # Independent exact Ramanujan value via additive group
                # orthogonality + Möbius inversion on proper divisors.
                divisor_sum=sum(w.ramanujan(k,d) for k in range(1,q) if q%k==0)
                self.assertEqual(w.ramanujan(q,d)+divisor_sum,
                                 q if d%q==0 else 0)
                self.assertEqual(w.ramanujan(q,d),w.ramanujan(q,-d))
                self.assertLessEqual(abs(w.primitive_projection(q,d)),1)
        self.assertEqual(w.totient(16),8)

    def test_full_vs_primitive_16(self):
        for d in range(-64,65):
            self.assertEqual(w.full_projection(16,d),int(d%16==0))
            expected=1 if d%16==0 else (-1 if d%16==8 else 0)
            self.assertEqual(w.primitive_projection(16,d),expected)
        self.assertNotEqual(w.full_projection(16,8),w.primitive_projection(16,8))

    def test_quadratic_same_variable_is_fourfold_but_primitive_zero(self):
        for k in range(4,9):
            q=1<<k
            rec=w.resonance_receipt(q,lambda x:2*x,lambda x:x*x)
            self.assertEqual(rec.agreements,4)
            self.assertEqual(rec.anti_agreements,4)
            self.assertEqual(rec.same_variable_probability,Q(4,q))
            self.assertEqual(rec.independent_copy_probability,Q(1,q))
            self.assertEqual(rec.naive_independent_copy_ratio,4)
            self.assertEqual(rec.primitive_projection_mean,0)
            self.assertEqual(rec.full_projection_mean,Q(4,q))
            exact=tuple(x for x in range(q) if (x*x-2*x)%q==0)
            opposed=tuple(x for x in range(q) if (x*x-2*x)%q==q//2)
            self.assertEqual(exact,w.quadratic_exact_roots(k))
            self.assertEqual(opposed,w.quadratic_antipodal_roots(k))
            self.assertEqual(w.stable_lifts(k),(0,2))

    def test_unrelated_comparator_is_not_an_evalue(self):
        for q in (8,16,31):
            rec=w.resonance_receipt(q,lambda x:x,lambda x:x)
            self.assertEqual(rec.same_variable_probability,1)
            self.assertEqual(rec.independent_copy_probability,Q(1,q))
            self.assertEqual(rec.naive_independent_copy_ratio,q)
            self.assertEqual(rec.primitive_projection_mean,1)
            self.assertFalse(rec.null_family_selected)
            self.assertFalse(rec.new_weyl_saving_proved)
        # A quite plausible "spectacular coincidence" is a pure re-expression.
        self.assertEqual(w.resonance_receipt(16,lambda x:7*x+3,
                                               lambda x:7*x+3).naive_independent_copy_ratio,16)

    def test_domains_fail_closed(self):
        for bad in (0,-1,True,3.5):
            with self.assertRaises(ValueError):w.totient(bad)
            with self.assertRaises(ValueError):w.full_projection(bad,0)
            with self.assertRaises(ValueError):w.resonance_receipt(bad,int,int)
        with self.assertRaises(ValueError):w.ramanujan(16,2.0)
        with self.assertRaises(ValueError):w.resonance_receipt(16,lambda x:1.5,lambda x:x)
        with self.assertRaises(ValueError):w.quadratic_exact_roots(3)
        with self.assertRaises(ValueError):w.quadratic_antipodal_roots(23)


class GlobalFrameCalibration(unittest.TestCase):
    def test_fixed_predeclared_frame_has_unit_null_expectation(self):
        for q in (4,16,64):
            for fixed in (0,1,q-1):
                self.assertEqual(sum((w.fixed_frame_evalue(q,x,fixed) for x in range(q)),Q())/q,1)
            # Invalid after-the-fact choice A=X always receives a high score.
            self.assertEqual(tuple(w.fixed_frame_evalue(q,x,x) for x in range(q)),(Q(q),)*q)
            self.assertEqual(sum(w.fixed_frame_evalue(q,x,x) for x in range(q))/q,q)
            # A predeclared uniformly weighted mixture corrects postselection.
            prior=(Q(1,q),)*q
            self.assertTrue(all(w.global_frame_mixture(q,x,prior)==1 for x in range(q)))
            self.assertEqual(sum(w.global_frame_mixture(q,x,prior) for x in range(q))/q,1)
            self.assertEqual(w.expected_postselected_frame_score(q,3),q*q)

    def test_prior_not_chosen_from_current_outcome(self):
        q=16
        prior=(Q(1,2),Q(1,2))+(Q(0),)*(q-2)
        self.assertEqual(w.global_frame_mixture(q,0,prior),8)
        self.assertEqual(w.global_frame_mixture(q,1,prior),8)
        self.assertEqual(w.global_frame_mixture(q,2,prior),0)
        self.assertEqual(sum((w.global_frame_mixture(q,x,prior) for x in range(q)),Q())/q,1)
        for bad in ((Q(1,q),)*(q-1), (Q(-1),)+(Q(2),)+(Q(0),)*(q-2)):
            with self.assertRaises(ValueError):w.global_frame_mixture(q,0,bad)
        with self.assertRaises(ValueError):w.global_frame_mixture(q,0,list((Q(1,q),)*q))

    def test_linear_provenance_rank_guard(self):
        rows=((-16,1,0,0),(0,-16,1,0),(0,0,-16,1))
        self.assertEqual(w.linear_constraint_rank_gain(rows,(-16**3,0,0,1)),0)
        self.assertEqual(w.linear_constraint_rank_gain(rows,(1,0,0,0)),1)
        self.assertEqual(w.linear_constraint_rank_gain(rows,(0,0,0,0)),0)
        with self.assertRaises(ValueError):w.linear_constraint_rank_gain(rows,(1,2))

    def test_predictable_martingale_adaptive_state_exact(self):
        def policy(history):
            p=Q(1,3) if sum(history)%2==0 else Q(2,3)
            stake=Q(1,2) if len(history)%2==0 else Q(2,3)
            return p,stake
        out=w.exact_binary_checkpoint_audit(9,policy,Q(4))
        self.assertEqual(out['expected_each_checkpoint'],(Q(1),)*9)
        self.assertLessEqual(out['crossing_probability'],Q(1,4))
        self.assertEqual(out['tree_leaves'],512)
        self.assertTrue(out['only_under_declared_null'])
        self.assertEqual(w.predictable_bet_factor(Q(1,2),Q(1),1),Q(3,2))
        self.assertEqual(w.predictable_bet_factor(Q(1,2),Q(1),0),Q(1,2))
        with self.assertRaises(ValueError):w.predictable_bet_factor(Q(1,2),3,0)
        with self.assertRaises(ValueError):w.exact_binary_checkpoint_audit(13,policy)
        with self.assertRaises(ValueError):w.exact_binary_checkpoint_audit(2,policy,Q(1))

    def test_null_optional_stopping_falsifier(self):
        # Under a fixed P0(X=1)=1/16, the predeclared per-step LR is 16
        # on X=1, zero on X=0. A single observation has expectation one.
        # Repeating the SAME observation as if it were new independent
        # evidence creates E0[LR^2]=16: invalid 'coherence amplification'.
        self.assertEqual(w.expected_postselected_frame_score(16,1),1)
        self.assertEqual(w.expected_postselected_frame_score(16,2),16)
        self.assertEqual(w.expected_postselected_frame_score(16,3),256)


class AuthenticSourceCountermodel(unittest.TestCase):
    def test_carry_forms_are_source_forced_and_not_new_phase_saving(self):
        for horizon in (1,2,9,32,79,127):
            r=w.authentic_carry_resonance(horizon)
            self.assertTrue(r.original_seed_authenticated)
            self.assertEqual(r.full_agreement,r.primitive_agreement)
            self.assertEqual(r.full_agreement,Q(horizon-r.spill_count,horizon))
            self.assertTrue(r.source_forcing_identical)
            self.assertFalse(r.pi_normality_proved)
            self.assertGreaterEqual(r.full_agreement,0)
            self.assertLessEqual(r.full_agreement,1)
            # The changed selector retains the SAME literal four-pole forcing.
            changed=w.authentic_carry_resonance(horizon,seed_offset=Q(1,3))
            self.assertFalse(changed.original_seed_authenticated)
            self.assertTrue(changed.source_forcing_identical)
            self.assertEqual(changed.primitive_agreement,changed.full_agreement)
            self.assertFalse(changed.pi_normality_proved)
        flags=w.status_flags()
        self.assertFalse(flags['pi_base16_normality_proved'])
        self.assertFalse(flags['nontrivial_selected_weyl_bound_proved'])
        self.assertFalse(flags['source_selector_specific_saving_proved'])


if __name__=='__main__':unittest.main()
