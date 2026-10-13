"""Independent finite dual-place common-source and fake-receipt controls."""
import unittest
from dataclasses import replace
from fractions import Fraction as F
from observational_succ.dual_place_verifier import DualPlaceProof,RationalClaim,PlaceReceipt
from observational_succ.diagonal_adele_zeta import DiagonalSourceError

class DualPlaceTests(unittest.TestCase):
    def setUp(self):
        self.s=DualPlaceProof('Q','rational-basis',2,3,{5:1,7:1})
        self.q=F(1,2)
        self.claim=RationalClaim('numerator positive',
            {v:('positive' if v>0 else 'not-positive') for v in self.s.sources})

    def test_two_finite_clocks_solve_original_source(self):
        rs=tuple(self.s.finite_observation(self.q,p,f'E-{p}') for p in (5,7))
        self.assertEqual(self.s.fiber(rs),(self.q,))
        r=self.s.conclude(rs,self.claim)
        self.assertEqual(r['status'],'PROVED')
        self.assertEqual(r['value'],'positive')
        self.assertFalse(r['external_observation_authentication'])

    def test_two_sides_cross_verify_without_secret_q(self):
        rs=tuple(self.s.finite_observation(self.q,p,'finite') for p in (5,7))
        ar=(self.s.real_observation(self.q,F(1,10),'arch'),)
        report=self.s.cross_check(rs,ar)
        self.assertTrue(report['intersection_equals_joint'])
        self.assertEqual(report['joint_size'],1)
        self.assertFalse(report['physical_source_authenticated'])

    def test_real_alone_insufficient_coarse_interval(self):
        ar=(self.s.real_observation(self.q,F(2),'arch'),)
        self.assertEqual(self.s.conclude(ar,self.claim)['status'],'UNRESOLVED')

    def test_missing_clock_can_fail_to_recover_full_source(self):
        weak=DualPlaceProof('Q','clock',2,3,{2:1})
        q=F(1,3)
        r=(weak.finite_observation(q,2,'A'),)
        self.assertGreater(len(weak.fiber(r)),1)

    def test_stale_basis_refused(self):
        r=self.s.finite_observation(self.q,5,'A')
        for mutant in (replace(r,version=3),replace(r,basis_id='other'),
                       replace(r,source_id='different')):
            with self.assertRaises(DiagonalSourceError):
                self.s.fiber((mutant,))

    def test_wrong_prime_label_and_forged_precision_refused(self):
        r=self.s.finite_observation(self.q,5,'A')
        for mutant in (replace(r,label='6'),replace(r,precision=2),
                       replace(r,data=(999,)),replace(r,observer='')):
            with self.assertRaises(DiagonalSourceError):
                self.s.fiber((mutant,))

    def test_conflicting_individually_source_compatible_reports(self):
        rs=(self.s.finite_observation(F(0),5,'A'),
            self.s.finite_observation(F(1),5,'B'))
        self.assertEqual(self.s.conclude(rs,self.claim)['status'],'INCONSISTENT_SOURCE')

    def test_forged_global_claim_table_fails(self):
        r=(self.s.finite_observation(self.q,5,'A'),)
        false=RationalClaim('forged',{self.q:'definitely'})
        with self.assertRaises(DiagonalSourceError):self.s.conclude(r,false)

if __name__=='__main__':unittest.main()
