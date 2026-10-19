"""Independent algebra and source-domain controls for the full inverse route."""
from fractions import Fraction as Q
import json
from pathlib import Path
import unittest
import sys
from observational_succ import full_prime_resolvent as F
from observational_succ import original_continuum_residual as R
from observational_succ import clamped_k_residual_bridge as B


class FullPrimeResolvent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.previous_digit_cap=None
        if hasattr(sys,'set_int_max_str_digits'):
            cls.previous_digit_cap=sys.get_int_max_str_digits()
            sys.set_int_max_str_digits(50000)

    @classmethod
    def tearDownClass(cls):
        if cls.previous_digit_cap is not None:
            sys.set_int_max_str_digits(cls.previous_digit_cap)

    def test_factorial_bessel_formula_against_recurrence(self):
        for ell in range(9):
            double=1
            for j in range(1,2*ell+2,2):double*=j
            recurrence=[Q(1,double)]
            for k in range(8):recurrence.append(-recurrence[-1]/(2*(k+1)*(2*ell+2*k+3)))
            self.assertEqual(F.bessel_coefficients(ell,8),tuple(recurrence))
        for args in ((True,2),(1,-1),(1,2.0)):
            with self.assertRaises(ValueError):F.bessel_coefficients(*args)

    def test_independent_all_high_budget_exactly_matches_source_budget(self):
        from observational_succ.tate_weighted_bessel_four_schur import source_parity_split_four_moment_coercivity_certificate
        inherited=source_parity_split_four_moment_coercivity_certificate()
        for parity in ('odd','even'):
            r=F.independent_high_budget(parity);p=inherited[parity+'_sector']
            self.assertEqual(r['gamma'],p['Gamma_multiplier_exact'])
            self.assertEqual(r['leakage'],p['weighted_Bessel_leakage_upper'])
            self.assertEqual(r['exact_margin'],p['kappa_'+parity+'_exact_lower'])
            self.assertGreater(r['exact_margin'],r['kappa'])
            self.assertFalse(r['derivative_L2_gap_claimed'])

    def test_exact_two_edge_inverse_and_center_identity(self):
        for kappa in (Q(63,500),Q(153,500),Q(2)):
            for w in (Q(12,25),Q(1,3),Q(7)):
                det=kappa*(kappa+2*w)
                for left,right,center in ((Q(1),Q(1),Q(0)),(Q(1),Q(-1),Q(2)),(Q(-2,3),Q(7,9),Q(1,4))):
                    direct=((kappa+w)*(left*left+right*right)+2*w*left*right)/det+center*center/(kappa+w)
                    scalar=(left*left+right*right+center*center)/kappa
                    saving=w/(kappa*(kappa+w))*center*center+w/(kappa*(kappa+2*w))*(right-left)**2
                    self.assertEqual(direct,scalar-saving)
                    self.assertGreaterEqual(saving,0)

    def test_source_mutations_fail_closed(self):
        p=R.source_parameters();F.source_regions(p)
        for key,value in (('b',Q(3,4)),('w',Q(0)),('real_gamma_count',2),('half_density','1'),('contact',p['contact']+1),('sha','0'*40)):
            with self.assertRaises(ValueError):F.source_regions(dict(p,**{key:value}))
        with self.assertRaises(ValueError):F.exact(0.25)
        with self.assertRaises(ValueError):F.exact(True)

    def test_exact_projection_and_full_region_integrals(self):
        p=R.source_parameters();b=p['b']
        cells=((-R.A,R.A-b),(R.A-b,b-R.A),(b-R.A,R.A))
        pieces=tuple((l,r,(Q(0),Q(0),Q(0),Q(0),Q(1)))for l,r in cells)
        projected=F.project_pieces(pieces)
        self.assertEqual(R.projected_piece_moments(projected),(0,0,0,0))
        result=F.whole_resolvent_saving((projected,projected),p,Q(63,500))
        self.assertEqual(result['center_Gram'][0][0],result['center_Gram'][0][1])
        self.assertTrue(F.matrix_psd(result['center_Gram']))
        broken=list(projected);broken[0]=(-R.A,R.A,broken[0][2])
        with self.assertRaises(ValueError):F.whole_resolvent_saving((broken,projected),p,Q(1))

    def test_transport_lower_handles_both_source_interval_endpoints(self):
        p=R.source_parameters();b=p['b']
        cells=((-R.A,R.A-b),(R.A-b,b-R.A),(b-R.A,R.A))
        columns=[]
        for degree in (4,5):
            poly=(Q(0),)*degree+(Q(1),)
            columns.append(F.project_pieces(tuple((l,r,poly)for l,r in cells)))
        result=F.whole_resolvent_saving(columns,p,Q(63,500))
        for delta in (-p['db'],p['db']):
            actual=[B.add(z[2][2],B.scale(R.shifted(z[0][2],-b-delta),-1))for z in columns]
            actual_gram=tuple(tuple(R.definite(B.mul(actual[i],actual[j]),*result['edge_region'])for j in range(2))for i in range(2))
            difference=tuple(tuple(actual_gram[i][j]-result['edge_Gram_lower'][i][j]for j in range(2))for i in range(2))
            self.assertTrue(F.matrix_psd(difference))

    def test_saved_actual_source_receipt_has_strict_matrix_gain(self):
        root=Path(__file__).resolve().parents[1]
        for depth in (8,24):
            path=root/f'research/2026-10-18/ROUND2_FULL_PRIME_J{depth}.json'
            r=json.loads(path.read_text())
            self.assertEqual(r['source_blob'],F.SOURCE_BLOB)
            self.assertEqual(r['base_commit'],F.PR177_HEAD)
            self.assertEqual(r['imports_from_PR178'],[])
            self.assertEqual(r['imports_from_PR179'],[])
            self.assertFalse(r['RH_proved'])
            for s in r['sectors'].values():
                matrices={name:tuple(tuple(Q(v)for v in row)for row in s[name])for name in ('old_lower','new_lower','gain')}
                self.assertTrue(F.matrix_pd(matrices['gain']))
                for i in range(2):
                    for j in range(2):self.assertEqual(matrices['new_lower'][i][j],matrices['old_lower'][i][j]+matrices['gain'][i][j])
                self.assertEqual(s['new_lower_PSD'],F.matrix_psd(matrices['new_lower']))
                self.assertTrue(F.matrix_pd(tuple(tuple(-v for v in row)for row in matrices['new_lower'])))

    def test_existing_capsule_authority_retains_open_sign_target(self):
        from observational_succ.source_proof_certificate import audit_capsules
        root=Path(__file__).resolve().parents[1]
        records=json.loads((root/'research/2026-10-18/ROUND2_SIGNED_CAPSULES.json').read_text())
        audit=audit_capsules(records,root)
        self.assertEqual(audit['theorems_proved_by_this_audit'],[])
        self.assertEqual(audit['claims'][-1]['recorded_authority'],'UNVERIFIED')
        self.assertEqual(audit['claims'][-1]['conclusion_mode'],'OPEN_TARGET')
        self.assertTrue(all(x['recorded_authority']!='LEAN_KERNEL_PROVED' for x in audit['claims']))



if __name__=='__main__':unittest.main()
