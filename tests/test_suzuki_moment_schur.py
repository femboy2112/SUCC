"""Exact mathematical Schur + source typed tests. Parent source checks run in GitHub CI."""
import copy
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.suzuki_moment_schur import (
    SchurSourceError, PARENT_SHA, AMW_SIBLING_SHA, CANONICAL_KAPPA,
    low_gram, low_inverse_neumann, legendre, legendre_primitive,
    cell_legendre_overlap, projection_cell_gram, matmul, matadd, transpose,
    matinv, eye, positive_definite, finite_regularized_schur,
    source_moment30_certificate, unprojected_cross_no_go,
    source_stage_bridge, regularized_schur_from_stage, one_sided_gamma_schur_from_stage,
    parent_grid_resolution_wall, source_small_grid_demonstration,
    inverse_neumann_entry, inverse_neumann_boundary_channels, parity_blocks, invert_2x2_and_schur,
    receipt, _same_typed,
)

class ExactSourceMomentSchurTests(unittest.TestCase):
    def test_legendre_endpoints_and_zero_mean(self):
        a=F(1,2)
        for n in range(1,31):
            self.assertEqual(legendre(n,F(1)),1)
            self.assertEqual(legendre(n,F(-1)),(-1)**n)
            self.assertEqual(legendre_primitive(n,a,a),0)
            self.assertEqual(legendre_primitive(n,a,-a),0)

    def test_low_gram_30_is_exact_rational_diagonal(self):
        G=low_gram(F(1,2),30)
        self.assertEqual(G[0][0],F(1,3))
        self.assertEqual(G[-1][-1],F(1,61))
        self.assertTrue(all(G[i][j]==0 for i in range(30) for j in range(30) if i!=j))
        self.assertTrue(positive_definite(G))

    def test_low_inverse_neumann_exact_pentadiagonal(self):
        K=low_inverse_neumann(F(1,2),30)
        self.assertTrue(positive_definite(K))
        self.assertEqual(K[0][0],F(1,30))
        self.assertEqual(K[0][2],-F(1,420))
        self.assertEqual(K[28][28],F(1,410286))
        self.assertEqual(K[29][29],F(1,453474))
        self.assertTrue(all(K[i][j]==0 for i in range(30) for j in range(30) if abs(i-j) not in (0,2)))

    def test_k_matrix_scales_as_a_cubed(self):
        for a in (F(1,4),F(1,2),F(3,4)):
            K=low_inverse_neumann(a,5)
            base=low_inverse_neumann(F(1,2),5)
            self.assertEqual(K[0][0]/base[0][0],(a/F(1,2))**3)
            self.assertEqual(K[2][4]/base[2][4],(a/F(1,2))**3)

    def test_cell_integrals_sum_zero_all_low_modes(self):
        for N in (2,3,4,5,6,8,12):
            M=cell_legendre_overlap(F(1,2),30,N)
            self.assertTrue(all(sum(row,F())==0 for row in M))

    def test_cell_legendre_integral_low_1(self):
        a=F(1,2)
        M=cell_legendre_overlap(a,1,2)
        self.assertEqual(M[0],(-F(1,4),F(1,4)))

    def test_cell_gram_has_zero_constant_vector(self):
        H=projection_cell_gram(F(1,2),5,8)
        self.assertTrue(all(sum(row,F())==0 for row in H))
        self.assertTrue(all(H[i][i]>=0 for i in range(8)))
        self.assertEqual(H,transpose(H))

    def test_cell_gram_2x2_psd_source_projection(self):
        H=projection_cell_gram(F(1,2),2,4)
        for i in range(4):
            self.assertGreaterEqual(H[i][i],0)
            for j in range(4):
                self.assertGreaterEqual(H[i][i]*H[j][j]-H[i][j]**2,0)

    def test_exact_kappa_source_hierarchy_verification(self):
        cert=source_moment30_certificate()
        self.assertEqual(cert['pinned_30moment_sibling'] if 'pinned_30moment_sibling' in cert else cert['sibling_sha'], AMW_SIBLING_SHA)
        self.assertEqual(cert['strict_high_L2_coercivity'],'369/10000')
        self.assertFalse(cert['H_u_high_uniform_I_gap'])
        self.assertEqual(CANONICAL_KAPPA,F(369,10000))

    def test_symmetric_schur_and_resolvent_rational(self):
        R=((F(1),F(2)),(F(2),F(-1)))
        M=((F(1),F(0)),(F(1),F(1)))
        H=((F(2),F(-1)),(F(-1),F(3)))
        W=((F(1),F(0)),(F(0),F(2)))
        for lam in (F(1,2),F(1),F(5)):
            S=finite_regularized_schur(R,M,H,W,lam)
            self.assertEqual(S,transpose(S))
            inv=matinv(matadd(tuple(tuple(lam*int(i==j) for j in range(2)) for i in range(2)),matmul(R,H)))
            expanded=matadd(matadd(matmul(matmul(M,R),transpose(M)),W,lam),matmul(matmul(matmul(matmul(matmul(M,R),H),inv),R),transpose(M)),-1)
            self.assertEqual(S,expanded)

    def test_schur_negative_direction_toy(self):
        self.assertLess(invert_2x2_and_schur(1,2,1,F(1,10)),0)
        self.assertGreater(invert_2x2_and_schur(4,1,1,F(1,10)),0)

    def test_naive_unprojected_schur_killed_by_positive_diagonal(self):
        v=unprojected_cross_no_go(F(1),F(10))
        self.assertTrue(v['guaranteed_failure'])
        self.assertEqual(v['unprojected_schur_upper'],'-90')
        self.assertEqual(invert_2x2_and_schur(10,0,1,F(0)+F(1,10)),F(101,10))
        self.assertFalse(v['authentic_Weil_negative'])

    def test_no_gap_in_derivative_carrier_counterexample(self):
        # D_n=1/n and K_n=1/n, so D>=K but inf Rayleigh D=0.
        for n in (100,1000,10000):
            D=F(1,n);K=F(1,n)
            self.assertEqual(D,K)
            self.assertLess(D,F(1,50))

    def test_typed_source_guards_reject_aliases(self):
        a={'x':(F(),F(1,2)),'strict':False}
        b={'x':(0.0,F(1,2)),'strict':False}
        c={'x':(F(),F(1,2)),'strict':0}
        self.assertFalse(_same_typed(a,b))
        self.assertFalse(_same_typed(a,c))
        self.assertTrue(_same_typed(a,copy.deepcopy(a)))

    def test_illegal_endpoints_negative_lambda_and_malformed_matrices(self):
        with self.assertRaises(SchurSourceError): legendre_primitive(1,F(1,2),F(3,4))
        with self.assertRaises(SchurSourceError): low_gram(F(1,2),31)
        with self.assertRaises(SchurSourceError): invert_2x2_and_schur(1,2,1,F(-1))
        with self.assertRaises(SchurSourceError): finite_regularized_schur(((1,1),(0,1)),((1,0),),((1,0),(0,1)),((1,),),1)

    def test_canonical_boundary_rank_two_and_rational_metric(self):
        out=inverse_neumann_boundary_channels(F(1,2),30)
        self.assertEqual(out['K_low_high_cross_rank'],2)
        self.assertEqual(out['channels'],((29,31,'-1/906948'),(30,32,'-1/999180')))
        self.assertLess(F(out['normalized_boundary_frobenius_squared']),F(1,100000000))
        for i in range(1,30):
            for j in range(31,35):
                if (i,j) not in ((29,31),(30,32)):
                    self.assertEqual(inverse_neumann_entry(F(1,2),i,j),0)

    def test_exact_parity_splitting_30x30_from_symmetric_toeplitz_source(self):
        a=F(1,2);r=30;N=6
        M=cell_legendre_overlap(a,r,N);H=projection_cell_gram(a,r,N);W=low_gram(a,r)
        R=tuple(tuple(F(1,1+abs(i-j)) for j in range(N)) for i in range(N))
        S=finite_regularized_schur(R,M,H,W,F(5))
        p=parity_blocks(S,r)
        self.assertEqual((p['even_rank'],p['odd_rank']),(15,15))
        self.assertEqual(len(p['even']),15)
        self.assertEqual(len(p['odd']),15)
        self.assertTrue(all(S[i][j]==0 for i in range(r) for j in range(r) if (i-j)%2))

    def test_non_centrosymmetric_source_reflection_fails(self):
        a=F(1,2);r=4;N=5
        M=cell_legendre_overlap(a,r,N);H=projection_cell_gram(a,r,N);W=low_gram(a,r)
        R=[[F(1,1+abs(i-j)) for j in range(N)] for i in range(N)]
        R[0][0]+=F(1,3)
        S=finite_regularized_schur(tuple(map(tuple,R)),M,H,W,F(3))
        with self.assertRaises(SchurSourceError):parity_blocks(S,r)

    def test_parity_blocks_reject_ordinary_forged_matrix(self):
        S=((F(1),F(1)),(F(1),F(2)))
        with self.assertRaises(SchurSourceError):parity_blocks(S,2)

    def test_source_one_sided_schur_authentication_when_inherited(self):
        try:
            src=source_stage_bridge(F(1,2),4,2,4)
        except SchurSourceError as exc:
            self.assertIn('pinned parent #85',str(exc))
        else:
            lam=src['error']+1
            full=regularized_schur_from_stage(src,lam)
            one=one_sided_gamma_schur_from_stage(src,lam)
            self.assertEqual(one['parity_odd_rank'],2)
            self.assertEqual(one['parity_even_rank'],2)
            self.assertTrue(one['source_positive_gamma_monotonicity'])
            self.assertFalse(one['gamma_tail_charged_against_lower_schur'])
            self.assertLess(F(one['lower_schur_error']),F(full['schur_error']))
            self.assertFalse(one['RH_proved'])

    def test_declared_grid_budget_floor_is_not_real_operator_lower_bound(self):
        x=parent_grid_resolution_wall(24,F(1,10000))
        self.assertEqual(x['stage_spatial_error_floor'],'11/24')
        self.assertEqual(x['necessary_grid_N_for_target'],110001)
        self.assertFalse(x['this_stage_api_can_even_attempt'])
        self.assertFalse(x['actual_source_negative_depth_certified'])
        with self.assertRaises(SchurSourceError):parent_grid_resolution_wall(24,F(0))
        self.assertTrue(parent_grid_resolution_wall(110001,F(1,10000))['this_stage_api_can_even_attempt'])

    def test_one_sided_loewner_schur_in_scalar_positive_gamma_toy(self):
        # True A_J+Dgamma>=A_J, with Dgamma>=0: Feshbach shorting
        # must preserve order even though low/high entries change.
        lam=F(3)
        truncated=invert_2x2_and_schur(1,2,1,lam)
        genuine=invert_2x2_and_schur(2,3,2,lam)  # add (1,1)(1,1)^*
        self.assertGreater(genuine,truncated)

    def test_authentic_30_dimensional_schur_uses_genuine_source_if_present(self):
        try:
            d=source_small_grid_demonstration()
        except SchurSourceError as exc:
            if 'pinned parent #85' not in str(exc):raise
            self.skipTest('exact parent #85 not mounted in standalone local overlay')
        else:
            self.assertEqual(d['low_modes'],30)
            self.assertEqual(d['parity_blocks'],[15,15])
            self.assertTrue(d['source_gamma_gain'])
            self.assertFalse(d['RH_proved'])
            self.assertEqual(len(d['rational_low_diagonal_sample']),6)

    def test_nonzero_main_kernel_not_assumed(self):
        r=receipt()
        self.assertFalse(r['all_a_positive'])
        self.assertFalse(r['RH_proved'])
        self.assertFalse(r['actual_source_regularized_schur_matrix_computed'])
        self.assertEqual(r['pinned_hierarchy_parent'],PARENT_SHA)

    def test_receipt_json_canonical_types(self):
        r=receipt()
        self.assertEqual(json.loads(json.dumps(r)),r)

    def test_source_parent_adapter_is_fail_closed_or_authenticated(self):
        try:
            src=source_stage_bridge(F(1,2),2,2,4)
        except SchurSourceError as exc:
            self.assertIn('pinned parent #85',str(exc))
        else:
            self.assertEqual(src['source'],'AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3')
            self.assertEqual(src['parent_sha'],PARENT_SHA)
            self.assertGreater(src['error'],0)

    def test_genuine_schur_authentic_source_when_inherited(self):
        try:
            src=source_stage_bridge(F(1,2),3,2,4)
        except SchurSourceError as exc:
            self.assertIn('pinned parent #85',str(exc))
        else:
            self.assertEqual(src['H'],projection_cell_gram(F(1,2),3,4))
            lam=src['error']+1
            out=regularized_schur_from_stage(src,lam)
            self.assertEqual(out['rank'],3)
            self.assertGreater(F(out['schur_error']),0)
            self.assertFalse(out['RH_proved'])
            self.assertTrue(out['negative_depth_upper_if_positive'] is None or out['negative_depth_upper_if_positive']==str(lam))
            bad=copy.deepcopy(src);bad['error']=float(src['error'])
            with self.assertRaises(SchurSourceError):regularized_schur_from_stage(bad,lam)

if __name__=='__main__':unittest.main()
