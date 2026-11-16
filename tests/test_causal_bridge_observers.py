"""Exhaustive finite, exact-rational controls of causal/entangled two-view bridge."""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
import importlib.util
import unittest

from observational_succ.causal_bridge_observers import (
    Event, LocalLink, CausalWalk, PresentOutput, current_output, meeting_phase,
    gauge_transform, Gaussian, ZERO, ONE, II, FormalFourier,
    bell_joint_observables, local_bell_marginal, classical_dephased_observables,
    choi_left_and_mirrored_right, original_bbp_r, original_bbp_state,
    original_bbp_seed_recovery,
)


def fixture():
    a=Event('A',0,-2); b=Event('B',0,2)
    a1=Event('A1',1,-1); b1=Event('B1',1,1)
    m=Event('M',3,0)
    left=CausalWalk((LocalLink(a,a1,Q(2,15)), LocalLink(a1,m,Q(1,3))), 'bbp-0')
    right=CausalWalk((LocalLink(b,b1,Q(1,5)), LocalLink(b1,m,Q(1,6))), 'bbp-0')
    return left,right


class LocalCausalTransport(unittest.TestCase):
    def test_future_paths_and_present_only(self):
        a,b=fixture()
        self.assertEqual(a.meeting,b.meeting)
        self.assertEqual(meeting_phase(current_output(a,Q(1,7)),current_output(b,Q(1,7))),Q(1,10))
        self.assertEqual(current_output(a,0).meeting.name,'M')
        self.assertEqual(len(vars(current_output(a,0))),4)

    def test_gauge_covariance_exhaustive(self):
        a,b=fixture()
        events={edge.source for path in (a,b) for edge in path.links} | {a.meeting}
        expected=meeting_phase(current_output(a,Q(1,11)),current_output(b,Q(1,17)))
        for i,j in product(range(-2,3), repeat=2):
            gauge={event:Q(i,7)+Q(j,11)*event.time + Q(i+j,13)*event.space for event in events}
            ga,ca=gauge_transform(a,Q(1,11),gauge)
            gb,cb=gauge_transform(b,Q(1,17),gauge)
            self.assertEqual(meeting_phase(current_output(ga,ca),current_output(gb,cb)),expected)
            self.assertEqual(current_output(ga,ca).model_phase_turns,
                             (current_output(a,Q(1,11)).model_phase_turns+gauge[a.meeting])%1)

    def test_noncausal_rejected(self):
        with self.assertRaises(ValueError):LocalLink(Event('a',0,0),Event('b',1,2),0)
        with self.assertRaises(ValueError):LocalLink(Event('a',0,0),Event('b',-1,0),0)
        with self.assertRaises(ValueError):LocalLink(Event('a',0,0),Event('a',0,0),0)

    def test_disconnected_path_rejected(self):
        a,b=fixture()
        with self.assertRaises(ValueError): CausalWalk((a.links[0],b.links[1]),'bbp-0')
        with self.assertRaises(ValueError): CausalWalk((), 'bbp-0')
        with self.assertRaises(ValueError): gauge_transform(a,0,{a.start:0})

    def test_meeting_mismatch_and_wrong_frame_rejected(self):
        a,b=fixture()
        ra,rb=current_output(a,0),current_output(b,0)
        with self.assertRaises(ValueError): meeting_phase(ra,PresentOutput(Event('other',4,0),0,'bbp-0'))
        with self.assertRaises(ValueError): meeting_phase(ra,PresentOutput(rb.meeting,0,'bbp-0','untransported'))
        with self.assertRaises(ValueError): meeting_phase(ra,PresentOutput(rb.meeting,0,'wrong-source'))

    def test_mutually_wrong_common_gauge_and_source_spoof(self):
        a,b=fixture()
        clean=meeting_phase(current_output(a,0),current_output(b,0))
        # Twin phase-offset in both source pins cancels in their relation.
        wrong=meeting_phase(current_output(a,Q(1,16)),current_output(b,Q(1,16)))
        self.assertEqual(clean,wrong)
        self.assertNotEqual(original_bbp_seed_recovery(3,original_bbp_state(3,Q(1,16))),0)


class BellInterferometry(unittest.TestCase):
    def test_exact_quarter_turn_syndromes(self):
        expect=((1,0),(0,1),(-1,0),(0,-1))
        for k in range(4):
            xx,xy=bell_joint_observables(Q(k,4))
            self.assertEqual((xx.eval_quarter(),xy.eval_quarter()),(Gaussian(expect[k][0]),Gaussian(expect[k][1])))

    def test_local_no_signaling_all_phase_quarters_and_general_rationals(self):
        for q in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(2,15),Q(47,240)):
            self.assertEqual(local_bell_marginal(q),((Q(1,2),Q(0)),(Q(0),Q(1,2))))
        self.assertNotEqual(bell_joint_observables(Q(0)),bell_joint_observables(Q(1,4)))

    def test_symbolic_circle_char_and_cancellation(self):
        xx,xy=bell_joint_observables(Q(2,15))
        self.assertEqual(len(xx.terms),2)
        self.assertEqual(len(xy.terms),2)
        self.assertEqual(xx.terms[0][0],Q(2,15))
        self.assertEqual(xx.terms[1][0],Q(13,15))
        with self.assertRaises(ValueError): xx.eval_quarter()
        self.assertEqual(FormalFourier.char(Q(1)).eval_quarter(),ONE)
        self.assertEqual(bell_joint_observables(Q(0))[1].terms,())
        self.assertEqual(bell_joint_observables(Q(1,2))[1].terms,())

    def test_classical_mixture_same_locals_but_no_phase_signal(self):
        self.assertEqual(classical_dephased_observables(),(FormalFourier(),FormalFourier()))
        self.assertNotEqual(classical_dephased_observables(),bell_joint_observables(Q(1,4)))
        self.assertEqual(local_bell_marginal(0),local_bell_marginal(Q(1,4)))

    def test_common_phase_source_alias_not_certification(self):
        a,b=fixture()
        phi=meeting_phase(current_output(a,0),current_output(b,0))
        shifted=meeting_phase(current_output(a,Q(1,4)),current_output(b,Q(1,4)))
        self.assertEqual(phi,shifted)
        self.assertEqual(bell_joint_observables(phi),bell_joint_observables(shifted))

    def test_exact_bell_mirror_with_adversarial_matrices(self):
        vals=(ZERO,ONE,II,Gaussian(Q(2,3),Q(-1,7)),Gaussian(-2,3))
        for a,b,c,d in product(vals, repeat=4):
            lhs,rhs=choi_left_and_mirrored_right(((a,b),(c,d)))
            self.assertEqual(lhs,rhs)
            self.assertEqual(lhs,(a,b,c,d))

    def test_bell_mirror_does_not_mean_physical_gate_at_b(self):
        matrix=((ONE,ZERO),(ZERO,II))
        self.assertEqual(*choi_left_and_mirrored_right(matrix))
        # Locally inaccessible phase at B is the same before and after.
        self.assertEqual(local_bell_marginal(0),local_bell_marginal(Q(1,4)))

    def test_product_bond_cannot_replace_entangled_bridge(self):
        # A fake |00> "bridge" does not permit operator sliding:
        # (X otimes I)|00> = |10>, (I otimes X^T)|00> = |01>.
        fake_left=(ZERO,ZERO,ONE,ZERO)
        fake_right=(ZERO,ONE,ZERO,ZERO)
        self.assertNotEqual(fake_left,fake_right)
        self.assertEqual(choi_left_and_mirrored_right(((ZERO,ONE),(ONE,ZERO)))[0],
                         (ZERO,ONE,ONE,ZERO))

    def test_joint_readout_after_causal_meeting_only(self):
        a,b=fixture()
        p=meeting_phase(current_output(a,0),current_output(b,0))
        self.assertEqual(p,Q(1,10))
        self.assertEqual(len(bell_joint_observables(p)[0].terms),2)
        self.assertEqual(local_bell_marginal(p),local_bell_marginal(0))
        bad=PresentOutput(Event('M_other',4,0),Q(1,4),'bbp-0')
        with self.assertRaises(ValueError): meeting_phase(current_output(a,0),bad)

    def test_quarter_cos_sin_zero_and_negative_controls(self):
        for q in (Q(0),Q(1,4),Q(1,2),Q(3,4)):
            x,y=bell_joint_observables(q)
            evx,evy=x.eval_quarter(),y.eval_quarter()
            self.assertEqual(evx.imag,0)
            self.assertEqual(evy.imag,0)
            self.assertEqual(evx.real*evx.real+evy.real*evy.real,1)


class AuthenticSource(unittest.TestCase):
    def test_original_four_poles_and_zero_seed(self):
        self.assertEqual(original_bbp_r(1),Q(47,15))
        self.assertEqual(original_bbp_state(0),0)
        self.assertEqual(original_bbp_state(1)%1,Q(2,15))
        for n in range(0,50):
            self.assertEqual(original_bbp_seed_recovery(n,original_bbp_state(n)),0)
            self.assertEqual(original_bbp_seed_recovery(n,original_bbp_state(n,Q(1,16))),Q(1,16))

    def test_source_phase_appears_only_in_joint(self):
        q=original_bbp_state(1)%1
        self.assertEqual(q,Q(2,15))
        xx,xy=bell_joint_observables(q)
        self.assertEqual(len(xx.terms),2)
        self.assertEqual(local_bell_marginal(q),local_bell_marginal(0))

    def test_invalid_bbp_index(self):
        with self.assertRaises(ValueError): original_bbp_r(0)
        with self.assertRaises(ValueError): original_bbp_state(-1)
        with self.assertRaises(ValueError): original_bbp_seed_recovery(-1,0)

    @unittest.skipUnless(importlib.util.find_spec('observational_succ.duck_bbp'),
                         'full checkout needed for canonical source cross-check')
    def test_against_inherited_source(self):
        from observational_succ.duck_bbp import forcing, lifted_orbit
        for n in range(1,70):
            self.assertEqual(original_bbp_r(n),forcing(n))
            self.assertEqual(original_bbp_state(n),lifted_orbit(n))


if __name__ == '__main__': unittest.main()
