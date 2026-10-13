"""Exact Lorentz/source-clock falsifiers; no physics/observer empirical claims."""
import random
import unittest
from fractions import Fraction as F
from observational_succ.covariant_observer_frames import (
    EventPoint, LorentzFrame, CausalEvent, CausalLedger, FrameError,
    causally_before, spacelike, physical_frame_demo)


class RationalLorentzTests(unittest.TestCase):
    def test_rational_boost_coordinates_and_clock(self):
        x=LorentzFrame.boost('x',F(1,3))
        self.assertEqual(x.apply(EventPoint(0,1)),EventPoint(F(-3,4),F(5,4)))
        self.assertEqual(x.apply(EventPoint(5,3)),EventPoint(4,0))
        self.assertEqual(EventPoint(5,3).interval(),16)
        self.assertEqual(x.apply(EventPoint(5,3)).interval(),16)

    def test_all_small_rational_spacetime_intervals(self):
        frames=[LorentzFrame.identity(),
                LorentzFrame.boost('x',F(1,3)),LorentzFrame.boost('y',F(-1,2)),
                LorentzFrame.boost('x',F(1,3)).then(LorentzFrame.boost('y',F(-1,2)))]
        rng=random.Random(472)
        for _ in range(250):
            p=EventPoint(*(rng.randint(-8,8) for _ in range(3)))
            for b in frames:
                self.assertEqual(b.apply(p).interval(),p.interval())
                self.assertEqual(b.inverse().apply(b.apply(p)),p)

    def test_timelike_and_null_order_never_reverse(self):
        base=EventPoint(-2,1,1)
        vecs=[EventPoint(2,1,1),EventPoint(4,-3,0),EventPoint(1,1,0),EventPoint(10,0,-7)]
        for v in vecs:
            later=EventPoint(base.t+v.t,base.x+v.x,base.y+v.y)
            self.assertTrue(causally_before(base,later,strict=True))
            for axis in ('x','y'):
                for p in (F(0),F(1,3),F(-2,3)):
                    B=LorentzFrame.boost(axis,p)
                    self.assertTrue(causally_before(B.apply(base),B.apply(later),strict=True))

    def test_spacelike_order_reverses_in_opposite_frames(self):
        a,b=EventPoint(0,-1),EventPoint(0,1)
        f1=LorentzFrame.boost('x',F(1,3));f2=LorentzFrame.boost('x',F(-1,3))
        self.assertTrue(spacelike(a,b))
        self.assertEqual(a.t,b.t)
        self.assertGreater(f1.apply(a).t,f1.apply(b).t)
        self.assertLess(f2.apply(a).t,f2.apply(b).t)

    def test_transverse_boosts_do_not_commute(self):
        a=LorentzFrame.boost('x',F(1,3)); b=LorentzFrame.boost('y',F(1,3))
        self.assertNotEqual(a.then(b).matrix,b.then(a).matrix)
        self.assertEqual(a.then(b).apply(EventPoint(2,1,1)).interval(),2)

    def test_collinear_boosts_commute(self):
        a=LorentzFrame.boost('x',F(1,3)); b=LorentzFrame.boost('x',F(1,2))
        self.assertEqual(a.then(b),b.then(a))

    def test_boost_inverse(self):
        b=LorentzFrame.boost('x',F(1,3))
        self.assertEqual(b.inverse(),LorentzFrame.boost('x',F(-1,3)))
        self.assertEqual(b.then(b.inverse()),LorentzFrame.identity())

    def test_mutated_nonlorentz_matrix_rejected(self):
        with self.assertRaises(FrameError):
            LorentzFrame(((F(1),F(1),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))))
        with self.assertRaises(FrameError):
            LorentzFrame(((-1,0,0),(0,-1,0),(0,0,1)))

    def test_invalid_boost_parameter_or_coordinate_type(self):
        for p in (F(1),F(-1),F(3,2)):
            with self.assertRaises(FrameError):LorentzFrame.boost('x',p)
        with self.assertRaises(FrameError):LorentzFrame.boost('z',F(1,3))
        with self.assertRaises(FrameError):EventPoint(0.1,1)


class CausalLedgerTests(unittest.TestCase):
    def make_ledger(self):
        return CausalLedger((
            CausalEvent('L',EventPoint(0,-1),'probe','S'),
            CausalEvent('R',EventPoint(0,1),'probe','S'),
            CausalEvent('E',EventPoint(0,0),'checkpoint','S'),
            CausalEvent('late',EventPoint(1,0),'checkpoint','S',('L','R'))))

    def test_physical_demo_and_no_coordinate_time_autoreceipts(self):
        report=physical_frame_demo()
        self.assertEqual(report['spacelike_order_boosted'],['3/4','-3/4'])
        self.assertEqual(report['slice_mismatch'],('left',))
        self.assertTrue(report['mismatch_only_spacelike'])
        l=self.make_ledger()
        self.assertEqual(l.certified_probes_at('E'),())
        self.assertEqual({e.ident for e in l.certified_probes_at('late')},{'L','R'})

    def test_difference_between_causal_past_and_coordinate_cut(self):
        l=self.make_ledger(); x=LorentzFrame.boost('x',F(1,3))
        rep=l.compare_slices(LorentzFrame.identity(),x,'E')
        self.assertEqual(rep['causal_past'],('E',))
        self.assertEqual(rep['mismatch'],('L',))
        self.assertTrue(rep['all_mismatches_spacelike_to_anchor'])
        self.assertEqual(l.causal_ancestry('late'),frozenset(('late','L','R')))

    def test_declared_parent_is_real_causal_arrow(self):
        l=self.make_ledger()
        self.assertFalse(l.is_downset(('late',)))
        self.assertTrue(l.is_downset(('late','L','R')))
        with self.assertRaisesRegex(FrameError,'cannot signal'):
            CausalLedger((CausalEvent('far',EventPoint(0,1),'probe','S'),
                         CausalEvent('now',EventPoint(0,0),'checkpoint','S',('far',))))

    def test_missing_or_duplicate_event_or_cross_source(self):
        with self.assertRaises(FrameError):
            CausalLedger((CausalEvent('a',EventPoint(0,0),'probe','S',('missing',)),))
        with self.assertRaises(FrameError):
            CausalLedger((CausalEvent('a',EventPoint(0,0),'probe','S'),
                          CausalEvent('a',EventPoint(1,0),'relay','S')))
        with self.assertRaises(FrameError):
            CausalLedger((CausalEvent('a',EventPoint(0,0),'probe','S'),
                          CausalEvent('b',EventPoint(1,0),'relay','T',('a',))))

    def test_spacelike_not_a_parent_and_future_not_access_without_link(self):
        l=CausalLedger((CausalEvent('x',EventPoint(0,0),'probe','S'),
                        CausalEvent('E',EventPoint(10,0),'checkpoint','S')))
        self.assertTrue(causally_before(l.get('x').point,l.get('E').point))
        self.assertEqual(l.certified_probes_at('E'),())

    def test_source_at_same_spacetime_point_not_same_event(self):
        l=CausalLedger((CausalEvent('a',EventPoint(0,0),'probe','S'),
                        CausalEvent('b',EventPoint(0,0),'probe','S')))
        self.assertEqual(l.causal_ancestry('a'),frozenset({'a'}))
        self.assertEqual(l.causal_ancestry('b'),frozenset({'b'}))


if __name__=='__main__': unittest.main()

class WignerControlTests(unittest.TestCase):
    def test_two_noncollinear_rational_boosts_induce_exact_wigner_rotation(self):
        a=LorentzFrame.boost('x',F(1,3));b=LorentzFrame.boost('y',F(1,3))
        L=a.then(b)
        pure,rot=L.decompose_boost_then_rotation()
        self.assertEqual(rot.matrix,((F(1),F(0),F(0)),
                           (F(0),F(40,41),F(-9,41)),
                           (F(0),F(9,41),F(40,41))))
        self.assertEqual(rot.apply(EventPoint(0,3,4)).interval(),-25)
        self.assertEqual(rot.then(pure),L)

    def test_collinear_boosts_have_no_wigner_rotation(self):
        L=LorentzFrame.boost('x',F(1,3)).then(LorentzFrame.boost('x',F(1,2)))
        _,R=L.decompose_boost_then_rotation()
        self.assertEqual(R,LorentzFrame.identity())

    def test_bad_pure_velocity_and_irrational_gamma_refused(self):
        with self.assertRaises(FrameError):LorentzFrame.pure_boost(F(1),F(0))
        with self.assertRaises(FrameError):LorentzFrame.pure_boost(F(1,2),F(0))

class EpistemicFluxTests(unittest.TestCase):
    def test_same_receipts_have_different_coordinate_and_proper_rates(self):
        from observational_succ.covariant_observer_frames import epistemic_flux_demo
        r=epistemic_flux_demo()
        self.assertEqual(r['E_coordinate_rate'],'8/5')
        self.assertEqual(r['climber_proper_rate'],'2')
        self.assertEqual(r['physical_clock_ratio'],'5/4')
        self.assertFalse(r['literal_cognitive_lorentz_law_demonstrated'])

