"""Exact controls of source algebra, metrics and residual/shift boundaries."""
from copy import deepcopy
from fractions import Fraction as F
from itertools import product
import unittest
from unittest.mock import patch

from observational_succ import arithmetic_resolvent as A
from observational_succ import one_object_relative_residual as R
from observational_succ import suzuki_legendre_source as L


class ArithmeticResolventTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.candidate = A.freeze_candidate(10, 8)
        cls.upper = A.certify_upper(cls.candidate, 16)

    def test_correlation_against_double_integral(self):
        for i, j in ((1, 1), (2, 6), (5, 9), (12, 16), (19, 19), (20, 20), (2, 3)):
            for alpha in (F(1, 2), F(13, 2), F(801, 2)):
                self.assertEqual(A.correlation_ou_affine(i, j, alpha),
                                 L.source_ou_pair_affine(i, j, F(1, 2), alpha))

    def test_true_truncated_source_matches_inherited(self):
        for i, j in ((1, 1), (2, 4), (5, 9), (10, 10), (2, 7)):
            a = A.truncated_entry(i, j, 3)
            b = L.authentic_full_low_entry(i, j, J=3)
            self.assertLessEqual(a.lo, b.hi)
            self.assertLessEqual(b.lo, a.hi)

    def test_whole_gamma_tail_contains_further_rungs(self):
        for i, j in ((2, 2), (2, 6), (9, 9)):
            outer = A.full_entry(i, j, 4)
            later = A.truncated_entry(i, j, 12)
            self.assertLessEqual(outer.lo, later.lo)
            self.assertLessEqual(later.hi, outer.hi)

    def test_ou_high_decay_enclosure(self):
        lo, hi = A._exp(F(801, 2), 60)
        self.assertEqual(lo, 0)
        self.assertEqual(hi, F(1, 2**400))

    def test_exact_solve_multiple_columns(self):
        a = ((F(3), F(1)), (F(1), F(2)))
        b = ((F(1), F(4)), (F(2), F(3)))
        x = A.solve(a, b)
        self.assertEqual(x, ((F(), F(1)), (F(1), F(1))))
        self.assertEqual(R.mm(a, x), b)

    def test_solve_rejects_indefinite(self):
        with self.assertRaises(A.ResolventError):
            A.solve(((1, 2), (2, 1)), ((1,), (1,)))

    def test_candidate_freeze_and_grid(self):
        c = self.candidate
        self.assertEqual(c['candidate_sha256'], A.candidate_digest(c))
        self.assertTrue(all((z*c['denominator']).denominator == 1 for row in c['U'] for z in row))
        self.assertTrue(all(s['exact_equation_verified'] for s in c['exact_sector_solves'].values()))

    def test_forged_candidate_rejected(self):
        c = deepcopy(self.candidate)
        c['degree'] = 12
        with self.assertRaises(A.ResolventError):
            A.validate_candidate(c)

    def test_parity_forgery_rejected_even_with_new_hash(self):
        c = deepcopy(self.candidate)
        u = [list(row) for row in c['U']]
        u[0][1] = F(1)
        c['U'] = tuple(map(tuple, u)); c['candidate_sha256'] = A.candidate_digest(c)
        with self.assertRaises(A.ResolventError):
            A.validate_candidate(c)

    def test_high_projection_and_trial_metric(self):
        v = A.trial_columns(self.candidate)
        self.assertEqual(v[:4], R.eye(4))
        gram = R.mm(R.mm(R.trans(v), A.metric(tuple(range(1, 11)))), v)
        self.assertEqual(gram, self.upper['V_Gram'])
        self.assertTrue(R.psd(self.upper['U_Gram']))

    def test_gamma_tail_propagated_as_positive_matrix(self):
        h = self.upper
        s = L._pinned_source()
        intervals = tuple(tuple(s.I(F(lo), F(hi)) for lo, hi in row) for row in h['truncated_H_intervals'])
        lo, hi, _ = A.interval_majorants(intervals)
        self.assertEqual(lo, h['H_lower'])
        self.assertEqual(R.add(h['S0_upper_form'], hi, -1),
                         R.scale(h['whole_Gamma_tail_norm_upper'], h['V_Gram']))

    def test_interval_majorant_all_corners(self):
        s = L._pinned_source()
        m = [[s.iv(0) for _ in range(4)] for _ in range(4)]
        for i,j,lo,hi in ((0,0,-1,2),(0,2,-2,1),(2,2,0,3)):
            m[i][j] = m[j][i] = s.I(F(lo),F(hi))
        lower, upper, _ = A.interval_majorants(m)
        for a,b,d in product((-1,2),(-2,1),(0,3)):
            corner = ((F(a),0,F(b),0),(0,0,0,0),(F(b),0,F(d),0),(0,0,0,0))
            self.assertTrue(R.psd(R.add(upper,corner,-1)))
            self.assertTrue(R.psd(R.add(corner,lower,-1)))

    def test_parity_interval_rejected(self):
        s = L._pinned_source(); m = [[s.iv(0) for _ in range(4)] for _ in range(4)]
        m[0][1] = m[1][0] = s.iv(1)
        with self.assertRaises(A.ResolventError):
            A.interval_majorants(m)

    def test_W_metric_caps(self):
        form = R.scale(F(1, 10), A.metric((1,2,3,4)))
        caps = A.sector_caps(form)
        for c in caps.values():
            self.assertGreaterEqual(c['operator_upper_cap'], F(1,10))
            self.assertLess(c['operator_upper_cap'], F(100001,1000000))
            self.assertTrue(c['cap_slack_exact_PSD'])
        # Raw coefficient diagonal 1/30 is not the operator eigenvalue 1/10.
        self.assertFalse(R.psd(R.add(R.scale(F(1,30), A.metric((1,2,3,4))),form,-1)))

    def test_source_caps_have_independent_2x2_slack(self):
        for c in self.upper['parity_caps'].values():
            m = c['cap_slack']
            self.assertGreaterEqual(m[0][0],0); self.assertGreaterEqual(m[1][1],0)
            self.assertGreaterEqual(m[0][0]*m[1][1]-m[0][1]**2,0)
        self.assertFalse(self.upper['zero_shift_lower_improved'])

    def test_shifted_certificate_keeps_gap_open(self):
        c = A.shifted_certificate(self.candidate,F(1,100),16)
        self.assertTrue(R.psd(c['residual_Gram_upper']))
        self.assertEqual(c['one_sided_spatial_tail_squared'],F(11,40)**2/F(4*11*12))
        self.assertEqual(c['regularization_gap_S_lambda_minus_S0'],'UNBOUNDED_BY_THIS_CERTIFICATE')
        self.assertFalse(c['RH_PROVED'])

    def test_zero_shift_residual_division_rejected(self):
        for shift in (F(),-F(1,10),0.1,True):
            with self.assertRaises(A.ResolventError):
                A.shifted_certificate(self.candidate,shift,16)

    def test_residual_identity_with_nonorthonormal_metric(self):
        # Independent exact 3-high finite operator; the third mode is omitted.
        w = ((F(1,3),0,0),(0,F(1,5),0),(0,0,F(1,7)))
        d = ((F(2),F(1,5),0),(F(1,5),F(1),F(1,7)),(0,F(1,7),F(1,2)))
        b = ((F(1,3),),(F(1,4),),(F(1,9),)); shift=F(1,10)
        q = R.add(d,R.scale(shift,w))
        u = ((F(1,8),),(F(1,7),),(F(),))
        residual=R.add(b,R.mm(q,u),-1)
        exact=R.mm(R.mm(R.trans(b),R.inv(q)),b)[0][0]
        trial=(2*R.mm(R.trans(u),b)[0][0]-R.mm(R.mm(R.trans(u),q),u)[0][0])
        error=R.mm(R.mm(R.trans(residual),R.inv(q)),residual)[0][0]
        gram=R.mm(R.mm(R.trans(residual),R.inv(w)),residual)[0][0]
        self.assertEqual(exact-trial,error)
        self.assertGreaterEqual(error,0); self.assertLessEqual(error,gram/shift)
        self.assertTrue(R.psd(d))

    def test_regularization_gap_can_flip_sign(self):
        c=A.regularization_counterexample(1000)
        self.assertGreater(c['S_lambda'],0); self.assertLess(c['S0'],0)
        self.assertGreater(c['regularization_gap'],F(999,1000))
        self.assertFalse(c['arithmetic_source'])

    def test_resource_and_type_guards(self):
        for n in (8,21,True,12.0):
            with self.assertRaises(A.ResolventError): A.freeze_candidate(n,8)
        for j in (0,2049,True):
            with self.assertRaises(A.ResolventError): A.truncated_entry(1,1,j)

    def test_cached_source_path_still_authenticates(self):
        A.truncated_entry(1,1,3)
        with patch.object(L,'_pinned_source',side_effect=RuntimeError('source drift')):
            with self.assertRaises(RuntimeError): A.truncated_entry(1,1,3)

    def test_cached_entry_rejects_runtime_source_mutation(self):
        source = L._pinned_source()
        A.truncated_entry(1,1,3)
        with patch.object(source, 'contact_iv', lambda: source.iv(0)):
            with self.assertRaises(A.ResolventError): A.truncated_entry(1,1,3)
        with patch.object(source, 'SCALE', 1):
            with self.assertRaises(A.ResolventError): A.truncated_entry(1,2,3)

    def test_forged_external_upper_is_no_longer_accepted(self):
        forged = deepcopy(self.upper)
        forged['H_lower'] = forged['S0_upper_form'] = R.scale(1000,A.metric((1,2,3,4)))
        forged['V_Gram'] = forged['U_Gram'] = R.zero(4,4)
        with self.assertRaises(TypeError):
            A.shifted_certificate(self.candidate,F(1,100),16,upper=forged)

    def test_directed_square_root(self):
        for x in (F(),F(4),F(2),F(1,10**30)):
            y = A.sqrt_upper(x)
            self.assertGreaterEqual(y*y,x)
            if y: self.assertLess((y-F(1,10**12))**2,x)

    def test_whole_cell_lipschitz_integration(self):
        # Extremal cone m+L|t| gives exactly all three recorded terms.
        m, lip, h = F(1,7), F(3,5), F(1,16)
        exact = 2*L.poly_integral((m*m,2*m*lip,lip*lip),F(),h/2)
        self.assertEqual(exact,h*m*m+m*lip*h*h/2+lip*lip*h**3/12)

    def test_zero_trial_lower_includes_whole_tail(self):
        c = A.certified_zero_trial_lower(2,4)
        for s in c['sectors'].values():
            self.assertGreaterEqual(s['trace_sqrt_upper']**2,s['finite_J_normalized_trace_upper'])
            self.assertEqual(s['R0_operator_upper_cap'],
                             (s['trace_sqrt_upper']+s['whole_Gamma_derivative_operator_tail'])**2/c['kappa'])
        self.assertTrue(c['Gamma_tail_closed_for_this_lower_bound'])
        self.assertFalse(c['RH_PROVED'])


if __name__=='__main__':
    unittest.main()
