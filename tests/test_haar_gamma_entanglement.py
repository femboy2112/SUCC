from fractions import Fraction as F
import unittest
from observational_succ.haar_gamma_entanglement import (
    GQ,I,O,J,PAULI,adjoint,matmul,kron,trace,expectation,sector_state,
    gamma_phase,gamma_dephase,co_moving_gauge_sector,marked_digit_haar_parity,
    joint_pauli,reduced_b,local_projective_a,nonselective_b,
    signed_haar_bond_contrast,chsh_optimum_squared,ppt_negative_minor,
    outcome_product_plus_probability,fresh_repetition_bayes,suite_certificate,radix16_haar_parity,uniform_haar_response,policy_haar_experiment,
)
class HaarGammaEntanglementTests(unittest.TestCase):
    def test_exact_gaussian_rational(self):
        self.assertEqual((I+J)**(-2),-J/2)
        self.assertEqual((I+J)**0,I)
        with self.assertRaises(ZeroDivisionError):_=I/O
        with self.assertRaises(TypeError):_=I+0.1
    def test_physical_state_validation(self):
        with self.assertRaises(ValueError):sector_state(GQ(2))
        self.assertEqual(trace(sector_state(GQ(1))),I)
    def test_gamma_marked_depth_two(self):
        self.assertEqual(gamma_phase(2,1),-J/2)
        self.assertEqual(gamma_phase(0,1),I)
        for a in range(6):
            for b in range(6):
                self.assertEqual(gamma_phase(a+b,F(1,2)),gamma_phase(a,F(1,2))*gamma_phase(b,F(1,2)))
    def test_gamma_local_phase_twirl(self):
        self.assertEqual(gamma_dephase(I,2,1),sector_state(-J/2))
        self.assertEqual(co_moving_gauge_sector(I),sector_state(I))
        self.assertNotEqual(gamma_dephase(I,2,1),co_moving_gauge_sector(I))
    def test_haar_parity_exact_sixteen_children(self):
        self.assertEqual(sum(marked_digit_haar_parity(x) for x in range(16)),0)
        self.assertEqual(marked_digit_haar_parity(0),1)
        self.assertEqual(marked_digit_haar_parity(1),-1)
        self.assertEqual(sum(marked_digit_haar_parity(x)**2 for x in range(16)),16)
        with self.assertRaises(ValueError):marked_digit_haar_parity(16)
    def test_bell_and_separable_identical_diagonal_haar(self):
        a=sector_state(I);b=sector_state(O)
        for i in range(4):self.assertEqual(a[i][i],b[i][i])
        for which in ('ZI','IZ','ZZ'):
            self.assertEqual(joint_pauli(a,which[0],which[1]),joint_pauli(b,which[0],which[1]))
        self.assertEqual(joint_pauli(a,'X','X'),I)
        self.assertEqual(joint_pauli(b,'X','X'),O)
    def test_gamma_two_complementary_haar(self):
        g=gamma_phase(2,1)
        self.assertEqual(signed_haar_bond_contrast(g),(I,O,GQ(F(1,2))))
        self.assertEqual(signed_haar_bond_contrast(O),(I,O,O))
        self.assertEqual(outcome_product_plus_probability(g,'XY'),F(3,4))
        self.assertEqual(outcome_product_plus_probability(O,'XY'),F(1,2))
        self.assertEqual(outcome_product_plus_probability(g,'ZZ'),I.re)
    def test_no_signalling_for_each_local_basis_and_phase(self):
        half=((GQ(F(1,2)),O),(O,GQ(F(1,2))))
        for gamma in (I,O,GQ(F(1,2)),gamma_phase(2,1),gamma_phase(4,F(1,3))):
            r=sector_state(gamma)
            self.assertEqual(reduced_b(r),half)
            for basis in ('X','Y','Z'):
                self.assertEqual(nonselective_b(r,basis),half)
                self.assertEqual(sum(local_projective_a(r,basis,a)[0] for a in (-1,1)),1)
    def test_selective_steering_in_x_not_in_sep(self):
        _,b=local_projective_a(sector_state(I),'X',1)
        self.assertEqual(b,((GQ(F(1,2)),GQ(F(1,2))),(GQ(F(1,2)),GQ(F(1,2)))))
        _,bs=local_projective_a(sector_state(O),'X',1)
        self.assertEqual(bs,((GQ(F(1,2)),O),(O,GQ(F(1,2)))))
        self.assertNotEqual(b,bs)
    def test_z_basis_classical_conditioning_looks_identical(self):
        for gamma in (O,I,gamma_phase(2,1)):
            r=sector_state(gamma)
            _,b=local_projective_a(r,'Z',1)
            self.assertEqual(b,((I,O),(O,O)))
    def test_gamma_npt_and_chsh(self):
        g=gamma_phase(2,1)
        self.assertEqual(ppt_negative_minor(g),-F(1,16))
        self.assertEqual(chsh_optimum_squared(g),F(5))
        self.assertEqual(chsh_optimum_squared(O),F(4))
        self.assertEqual(chsh_optimum_squared(I),F(8))
    def test_blind_haar_probe_gives_no_evidence(self):
        g=gamma_phase(2,1)
        for n in range(12):self.assertEqual(fresh_repetition_bayes(n,g,O,'ZZ'),F(1,2))
    def test_fresh_complementary_probe_produces_bayes_update(self):
        g=gamma_phase(2,1)
        self.assertEqual(fresh_repetition_bayes(0,g,O,'XY'),F(1,2))
        self.assertEqual(fresh_repetition_bayes(1,g,O,'XY'),F(3,5))
        self.assertEqual(fresh_repetition_bayes(4,g,O,'XY'),F(81,97))
    def test_infinite_fresh_report_reuse_not_bayesian(self):
        g=gamma_phase(2,1)
        self.assertNotEqual(fresh_repetition_bayes(4,g,O,'XY'),fresh_repetition_bayes(1,g,O,'XY'))
    def test_covariant_relative_gauge_vs_local_physical_change(self):
        c=suite_certificate(2,1)
        self.assertEqual(c['haar_ZZ'],I)
        self.assertEqual(c['haared_XX'],O)
        self.assertEqual(c['haared_XY'],GQ(F(1,2)))
        self.assertEqual(c['bob'],c['b_after_X'])
    def test_pauli_tensor_algebra(self):
        self.assertEqual(matmul(PAULI['X'],PAULI['Y']),tuple(tuple(J*z for z in row) for row in PAULI['Z']))
        self.assertEqual(adjoint(PAULI['Y']),PAULI['Y'])
        for z in ('X','Y','Z'):
            self.assertEqual(matmul(PAULI[z],PAULI[z]),PAULI['I'])
    def test_zero_likelihood_branch_control(self):
        with self.assertRaises(ValueError):local_projective_a(sector_state(O),'Q',1)
        with self.assertRaises(ValueError):fresh_repetition_bayes(-1,I,O,'ZZ')
    def test_raw_retained_joint_state_changes_after_measurement(self):
        # The receiver is unchanged. But the *joint* output is altered.
        r=sector_state(I)
        Pp=tuple(tuple((PAULI['I'][i][j]+PAULI['Z'][i][j])/2 for j in (0,1)) for i in (0,1))
        Pm=tuple(tuple((PAULI['I'][i][j]-PAULI['Z'][i][j])/2 for j in (0,1)) for i in (0,1))
        q=tuple(tuple(O for _ in range(4)) for _ in range(4))
        for p in (Pp,Pm):
            K=kron(p,PAULI['I'])
            m=matmul(matmul(K,r),adjoint(K))
            q=tuple(tuple(q[i][j]+m[i][j] for j in range(4)) for i in range(4))
        self.assertEqual(q,sector_state(O))
        self.assertEqual(reduced_b(q),reduced_b(r))
    def test_normalized_radix16_local_haar(self):
        for d in range(4):
            prefix=tuple(range(d))
            samples=[radix16_haar_parity(prefix,prefix+(a,)) for a in range(16)]
            self.assertEqual(sum(samples),0)
            self.assertEqual(sum(x*x for x in samples),16*16**d)
            self.assertEqual(radix16_haar_parity(prefix,tuple([15]*d+[0])),0 if d>0 else 1)
    def test_policy_driven_haar_attraction_requires_propensity(self):
        responses=tuple(F(3,4) if a%2==0 else F(1,4) for a in range(16))
        policy=tuple(F(3,32) if a%2==0 else F(1,32) for a in range(16))
        report=policy_haar_experiment(responses,policy)
        self.assertEqual(report['target'],F(1,4))
        self.assertEqual(report['raw_policy_weighted'],F(1,2))
        self.assertEqual(report['propensity_corrected'],F(1,4))
    def test_no_full_policy_observation_without_support(self):
        responses=(F(1,2),)*16
        with self.assertRaises(ValueError):policy_haar_experiment(responses,(F(1),)+(F(0),)*15)
    def test_nested_haar_wavelet_orthogonality(self):
        prefix=(2,)
        psi_parent=[radix16_haar_parity((),(a,)) for a in range(16)]
        inner=sum((radix16_haar_parity(prefix,(a,b))*psi_parent[a] for a in range(16) for b in range(16)))
        self.assertEqual(inner,0)
if __name__=='__main__':unittest.main()
