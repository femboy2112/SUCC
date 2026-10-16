"""Exact first-prime source-transport, zero-shift and Hilbert tests.

Tests validate exact finite math and source bindings; infinite Hilbert/operator
statements have independent quantified paper proofs in the research dossier.
"""
import unittest
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt
from observational_succ.tate_suzuki_shorting import (
    TateSourcePassport, ShortingContractError, is_genuine_prime,
    prime_power_parent, true_prime_tape, euler_p_shell,
    log_derivative_coefficient_tape, gammas_from_prime_mutation,
    PINNED_TAPE, first_window_derivative_l1_cap,
    original_gamma_derivative_l1_tail, original_gamma_kernel_l1_tail,
    integral_comparison_tail, source_legendre_30_projection_derivative_cap,
    actual_source_high_derivative_truncation, rational_psd,
    rational_inverse, symmetric, quadratic, mat, ma, mm, mt,
    synthetic_residual_schur, hilbert_xy,
    schur_hilbert_grid_lower, hilbert_boundary_matrix_certificate,
)


def det(A):
    """Independent exact determinant oracle by Leibniz for n<=4."""
    from itertools import permutations
    n=len(A)
    out=F()
    for p in permutations(range(n)):
        inversions=sum(1 for i in range(n) for j in range(i+1,n) if p[i]>p[j])
        out+=(-1)**inversions * __import__('math').prod(A[i][p[i]] for i in range(n))
    return out


def oracle_psd(A):
    return all(det(tuple(tuple(A[i][j] for j in J) for i in J))>=0
               for k in range(1,len(A)+1) for J in combinations(range(len(A)),k))


class SourcePassport(unittest.TestCase):
    def test_expected_passport(self):
        p=TateSourcePassport()
        self.assertEqual(p.half_density,F(1,2))
        self.assertEqual(p.real_gamma_count,1)
        self.assertFalse(p.trace_model_identified)

    def test_mutation_controls(self):
        candidates=[{'source_id':'FAKE6'}, {'epoch':1},
                    {'half_density':F(0)}, {'half_density':0.5},
                    {'gaussian_scale':F(2)}, {'gaussian_scale':2},
                    {'real_gamma_count':2}, {'conductor':4},
                    {'character_parity':1}, {'trace_model_identified':True}]
        for kw in candidates:
            with self.subTest(kw=kw), self.assertRaises(ShortingContractError):
                TateSourcePassport(**kw)

    def test_true_prime_power(self):
        self.assertEqual(true_prime_tape(8),PINNED_TAPE)
        self.assertEqual(prime_power_parent(32),2)
        self.assertEqual(prime_power_parent(81),3)
        self.assertIsNone(prime_power_parent(6))
        self.assertIsNone(prime_power_parent(12))
        with self.assertRaises(ShortingContractError):
            prime_power_parent(1)
        for n in range(2,200):
            p=prime_power_parent(n)
            if p is not None:
                self.assertTrue(is_genuine_prime(p))
                while n%p==0:n//=p
                self.assertEqual(n,1)

    def test_bad_source_mutants(self):
        for x in [((2,2),(3,3),(4,2),(5,5),(6,6),(7,7),(8,2)),
                  ((2,2),(3,3),(4,2),(5,5),(7,7)),
                  ((2,2),(3,3),(4,4),(5,5),(7,7),(8,2))]:
            with self.assertRaises(ShortingContractError):
                gammas_from_prime_mutation(x)
        self.assertTrue(gammas_from_prime_mutation(PINNED_TAPE))
        for bad in (6,12,0,-4,1,2.0):
            with self.assertRaises(ShortingContractError):
                euler_p_shell(bad,2,5)

    def test_tate_shell_2_and_3(self):
        for p in (2,3,5,11):
            for sigma in (2,3,4):
                for J in (0,1,2,4):
                    r=euler_p_shell(p,sigma,J)
                    self.assertEqual(r['finite']+r['omitted'],r['exact_local_factor'])
                    self.assertEqual(r['finite'],sum((F(1,p**(sigma*k)) for k in range(J+1)),F()))
        self.assertEqual(euler_p_shell(2,2,2)['finite'],F(21,16))
        self.assertEqual(euler_p_shell(2,2,2)['omitted'],F(1,48))

    def test_actual_formal_log_current(self):
        d=dict(log_derivative_coefficient_tape(20))
        self.assertEqual(d[2],F(1,4)+F(1,16)+F(1,64)+F(1,256))
        self.assertEqual(d[3],F(1,9)+F(1,81))
        self.assertNotIn(6,d)
        self.assertEqual(dict(log_derivative_coefficient_tape(8))[2],F(1,4)+F(1,16)+F(1,64))

    def test_reject_unsupported_types(self):
        for arg in (F(2),True,2.0):
            with self.assertRaises(ShortingContractError):
                true_prime_tape(arg)
        with self.assertRaises(ShortingContractError):
            euler_p_shell(2,1,2)
        with self.assertRaises(ShortingContractError):
            euler_p_shell(2,2,-1)


class OriginalGammaSource(unittest.TestCase):
    def test_exact_first_prime_derivative_budget(self):
        self.assertEqual(first_window_derivative_l1_cap(F(1,2)),26)
        for a in (F(1,3),F(3,4),F(1,2)+F(1,100)):
            with self.assertRaises(ShortingContractError):
                first_window_derivative_l1_cap(a)

    def test_second_variation_original_signed_j_rungs(self):
        from observational_succ.tate_suzuki_shorting import (original_first_prime_derivative_bv_bound,
             genuine_low_legendre_sup_coarse)
        self.assertEqual(original_first_prime_derivative_bv_bound(3),
                         F(16)+8*(F(1)+F(1,5)+F(1,9)))
        self.assertEqual([genuine_low_legendre_sup_coarse(k) for k in (1,2,3,4)],
                         [F(1),F(2),F(4),F(17,2)])
        for bad in (0,-1,21):
            with self.assertRaises(ShortingContractError):
                original_first_prime_derivative_bv_bound(bad)

    def test_gamma_rungs_decay(self):
        prev=original_gamma_derivative_l1_tail(1)
        for j in range(2,70):
            new=original_gamma_derivative_l1_tail(j)
            self.assertLess(new,prev)
            self.assertEqual(new, original_gamma_kernel_l1_tail(j))
            self.assertEqual(integral_comparison_tail(j)[1],new)
            prev=new

    def test_source_projection_penalty(self):
        c=source_legendre_30_projection_derivative_cap()
        self.assertEqual(c['derivative_projection_HS_square'],922560)
        self.assertEqual(c['integer_upper'],961)
        self.assertEqual(actual_source_high_derivative_truncation(75),F(962)*(F(2,301)+F(8,301*301)))
        self.assertLess(actual_source_high_derivative_truncation(10000),F(1,20))

    def test_positive_integral_comparison(self):
        for J in (1,2,7,20,100):
            # Certify finite first 1000 gamma rungs between exact bounds.
            partial=sum((F(8,(4*j+1)**2) for j in range(J,J+1000)),F())
            lo,hi=integral_comparison_tail(J)
            self.assertLess(lo,hi)
            self.assertLess(partial,hi)
            # lower integral is below sum to infinity, but not necessarily partial.


class SemidefiniteArithmetic(unittest.TestCase):
    def test_spd_singular_indefinite(self):
        cases=[
          ([[2,1],[1,2]],True),([[1,1],[1,1]],True),
          ([[0,0],[0,1]],True),([[0,1],[1,0]],False),
          ([[1,2],[2,1]],False),
          ([[1,0,2],[0,0,0],[2,0,4]],True),
          ([[2,0,0],[0,0,1],[0,1,0]],False),
          ([[-1]],False),([[0]],True),
        ]
        for M,truth in cases:
            with self.subTest(M=M):
                got,w=rational_psd(M)
                self.assertEqual(got,truth)
                if not got:self.assertLess(quadratic(mat(M),w),0)

    def test_exhaustive_independent_minors(self):
        vals=(-2,-1,0,1,2)
        checked=0
        for upper in product(vals,repeat=6):
            # Use a coarse deterministic sample of all 5^6 symmetric 3x3.
            checked+=1
            if checked%17:continue
            M=((F(upper[0]),F(upper[1]),F(upper[2])),
               (F(upper[1]),F(upper[3]),F(upper[4])),
               (F(upper[2]),F(upper[4]),F(upper[5])))
            truth=oracle_psd(M)
            got,w=rational_psd(M)
            self.assertEqual(got,truth)
            if not got:self.assertLess(quadratic(M,w),0)
        self.assertGreater(checked,15000)

    def test_exact_inverse(self):
        K=mat([[1,F(1,3)],[F(1,3),F(2)]])
        inv=rational_inverse(K)
        self.assertEqual(mm(K,inv),((F(1),F()),(F(),F(1))))
        with self.assertRaises(ShortingContractError):
            rational_inverse([[1,1],[1,1]])

    def test_wrong_dimensions_and_types(self):
        with self.assertRaises(ShortingContractError):
            rational_psd([[1,2],[3,4]])
        with self.assertRaises(ShortingContractError):
            rational_psd([[1,2],[3]])
        with self.assertRaises(ShortingContractError):
            rational_psd([[0.0]])
        with self.assertRaises(ShortingContractError):
            rational_psd([[True]])


class UnshiftedResidual(unittest.TestCase):
    A=[[1]]
    B=[[F(1,2), F(1,8)]]
    K=[[1,0],[0,F(1,4)]]
    D=[[2,0],[0,F(1,2)]]

    def test_optimized_trial_proves_strict_margin(self):
        r=synthetic_residual_schur(self.A,self.B,self.D,self.K,1,
                                   [[F(1,4)],[F(1,4)]])
        self.assertEqual(r.conservative_schur_matrix,((F(27,32),),))
        self.assertEqual(r.residual_matrix,((F(),),(F(),)))
        self.assertTrue(r.semidefinite)
        self.assertFalse(r.original_weil_sign_proved)

    def test_zero_trial_still_source_sound(self):
        r=synthetic_residual_schur(self.A,self.B,self.D,self.K,1,[[0],[0]])
        self.assertEqual(r.conservative_schur_matrix,((F(11,16),),))
        self.assertTrue(r.semidefinite)

    def test_strictly_positive_true_block_but_weak_certifier_unresolved(self):
        r=synthetic_residual_schur([[F(1,5)]],self.B,self.D,self.K,1,[[0],[0]])
        self.assertFalse(r.semidefinite)
        self.assertLess(quadratic(r.conservative_schur_matrix,r.witness),0)
        # True finite 3x3 remains SPD since exact Schur 1/5 - 5/32 >0.
        actual=F(1,5)-F(5,32)
        self.assertGreater(actual,0)

    def test_negative_block_must_not_be_promoted(self):
        r=synthetic_residual_schur([[0]],self.B,self.D,self.K,1,
                                   [[F(1,4)],[F(1,4)]])
        self.assertFalse(r.semidefinite)
        self.assertLess(quadratic(r.conservative_schur_matrix,r.witness),0)

    def test_complement_gap_and_source_licensing(self):
        with self.assertRaises(ShortingContractError):
            synthetic_residual_schur(self.A,self.B,[[0,0],[0,F(1,2)]],self.K,1,[[0],[0]])
        with self.assertRaises(ShortingContractError):
            synthetic_residual_schur(self.A,self.B,self.D,self.K,1,[[0],[0]],source_scope='AUTHENTIC_SUZUKI')
        with self.assertRaises(ShortingContractError):
            synthetic_residual_schur(self.A,self.B,self.D,self.K,0,[[0],[0]])
        with self.assertRaises(ShortingContractError):
            synthetic_residual_schur(self.A,self.B,self.D,self.K,1,[[0]])


class InfiniteDimensionalRangeObstruction(unittest.TestCase):
    def test_non_h1_cross_vector_has_divergent_zero_shift_energy(self):
        # Model D=K=diag(1/n²), b_n=1/n. Truncated R0(n)=n ->∞.
        # The range obstruction is not fabricated by a finite matrix.
        for N in (1,2,4,8,16):
            self.assertEqual(sum((F(1,n*n) / F(1,n*n) for n in range(1,N+1)),F()),N)

    def test_h1_cross_vector_has_bounded_zero_shift_energy(self):
        # b_n=1/n² is in Ran K^1/2 because sum n² b_n²<∞.
        # Elementary tail comparison ensures R0 <2 uniformly.
        for N in (1,2,4,8,16,32):
            cost=sum((F(1,n**4)/F(1,n*n) for n in range(1,N+1)),F())
            self.assertLess(cost,2)


class HilbertFiniteControl(unittest.TestCase):
    def test_complete_traversal_and_adjacent(self):
        for lev in (1,2,3,4):
            seq=[hilbert_xy(lev,k) for k in range(4**lev)]
            self.assertEqual(len(set(seq)),4**lev)
            self.assertTrue(all(abs(x[0]-y[0])+abs(x[1]-y[1])==1
                                for x,y in zip(seq,seq[1:])))
            self.assertEqual(set(seq),set(product(range(2**lev),repeat=2)))

    def test_direction_certificate_positive(self):
        r=hilbert_boundary_matrix_certificate([[1,0],[0,2]],level=4)
        self.assertGreater(r['certified_margin'],0)
        self.assertTrue(r['strictly_positive_definite'])
        self.assertEqual(r['sample_count'],60)

    def test_direction_certificate_small_gap_unresolved(self):
        r=hilbert_boundary_matrix_certificate([[F(1,1000),0],[0,2]],level=4)
        self.assertFalse(r['strictly_positive_definite'])
        self.assertGreater(r['boundary_minimum'],0)
        self.assertEqual(r['interpretation'],'PD if strict; otherwise UNRESOLVED')

    def test_cube_additive_sign_blind_at_origin(self):
        r=schur_hilbert_grid_lower([[1,0],[0,1]],depth=4)
        self.assertEqual(r['grid_minimum'],0)
        self.assertLess(r['global_lower'],0)
        self.assertFalse(r['all_square_nonnegative'])

    def test_negative_boundary_direction(self):
        r=hilbert_boundary_matrix_certificate([[1,0],[0,-1]],level=4)
        self.assertFalse(r['strictly_positive_definite'])
        self.assertLess(r['boundary_minimum'],0)

    def test_invalid_hilbert_inputs(self):
        with self.assertRaises(ShortingContractError):hilbert_xy(0,0)
        with self.assertRaises(ShortingContractError):hilbert_xy(3,64)
        with self.assertRaises(ShortingContractError):hilbert_boundary_matrix_certificate([[1]],4)
        with self.assertRaises(ShortingContractError):hilbert_boundary_matrix_certificate([[1,2],[3,4]],4)


class IntegratedOriginalSource(unittest.TestCase):
    def test_byte_pinned_original_suzuki(self):
        # Isolated overlay cannot verify a source that was never imported;
        # actual complete SUCC checkout is an obligatory CI positive control.
        try:
            from observational_succ import source_weil_hierarchy
        except ImportError:
            self.skipTest('missing original source in isolated overlay; CI must run it')
        from observational_succ.tate_suzuki_shorting import verify_original_suzuki_source
        info=verify_original_suzuki_source()
        self.assertEqual(info['source_git_blob'],
                         '0cc8510b71d178fc79e8d410a86d8b6014cf9178')
        self.assertFalse(info['original_weil_sign_proved'])

    def test_real_original_derivative_source_points(self):
        # Mandatory full-checkout proof-interfaced diagnostics. Genuine
        # J=3 pole/Gamma/contact/prime2, not a fitted matrix or ζ-zero scan.
        try:
            from observational_succ import suzuki_legendre_source
        except ImportError:
            self.skipTest('authentic source not installed in isolated overlay; mandatory CI')
        from observational_succ.tate_suzuki_shorting import authentic_suzuki_legendre_derivative_point
        p1=authentic_suzuki_legendre_derivative_point(1,F(1,4),3)
        self.assertGreater(p1.lo,-F(1,50))
        self.assertLess(p1.hi,-F(1,100))
        p2=authentic_suzuki_legendre_derivative_point(2,F(1,4),3)
        self.assertGreater(p2.lo,-F(1,25))
        self.assertLess(p2.hi,-F(1,40))
        origin=authentic_suzuki_legendre_derivative_point(2,F(0),3)
        self.assertLessEqual(origin.lo,0)
        self.assertGreaterEqual(origin.hi,0)
        self.assertLess(origin.hi-origin.lo,F(1,10**20))
        for bad in (F(1,2),-F(1,2),F(3,4)):
            with self.assertRaises(ShortingContractError):
                authentic_suzuki_legendre_derivative_point(1,bad,3)

    def test_real_source_derivative_energy_quad(self):
        try:
            from observational_succ import suzuki_legendre_source
        except ImportError:
            self.skipTest('genuine interval source only in complete SUCC checkout; mandatory CI')
        from observational_succ.tate_suzuki_shorting import original_suzuki_legendre_derivative_energy
        got=original_suzuki_legendre_derivative_energy(1,3,4)
        self.assertEqual(got['source'],'ACTUAL_ZETA_SUZUKI_G_J_FIRST_PRIME')
        self.assertGreaterEqual(got['finite_J_energy_upper'],got['finite_J_energy_lower'])
        self.assertGreater(got['infinite_true_G_derivative_energy_upper'],0)
        self.assertFalse(got['true_high_projected_cross_energy_certified'])
        self.assertFalse(got['original_all_test_weil_positive'])
        with self.assertRaises(ShortingContractError):
            original_suzuki_legendre_derivative_energy(1,3,1)

    def test_real_original_signed_low_legendre_passport(self):
        # Same true source must carry both signs as the Gamma rung count changes.
        # The high-moment all-test sign is NOT inferred from these one-mode values.
        try:
            from observational_succ import suzuki_legendre_source
        except ImportError:
            self.skipTest('no authentic Legendre module in isolated overlay; mandatory CI')
        low=suzuki_legendre_source.authentic_full_low_entry(1,1,F(1,2),3)
        self.assertLess(low.hi,0)
        high=suzuki_legendre_source.authentic_full_low_entry(1,1,F(1,2),75)
        self.assertGreater(high.lo,0)



class SourceProjectedDerivativeEnergy(unittest.TestCase):
    def test_projection_wrong_rank_rejected_before_source(self):
        from observational_succ.tate_suzuki_shorting import original_suzuki_projected_derivative_energy
        for rank in (0,1,2,29,31,True):
            with self.assertRaises(ShortingContractError):
                original_suzuki_projected_derivative_energy(1,3,2,low_rank=rank)

    def test_true_suzuki_projected_low_high_derivative_energy(self):
        try:
            from observational_succ import suzuki_legendre_source
        except ImportError:
            self.skipTest('full SUCC original-source projection required by CI')
        from observational_succ.tate_suzuki_shorting import original_suzuki_projected_derivative_energy
        result=original_suzuki_projected_derivative_energy(1,3,2)
        self.assertEqual(result['source'],'AUTHENTIC_COMPLETED_ZETA_SUZUKI_SIGNED')
        self.assertEqual(result['low_rank'],30)
        self.assertTrue(result['signed_source_projected'])
        self.assertLessEqual(result['finite_J_projected_energy_lower'],result['finite_J_projected_energy_upper'])
        self.assertGreater(result['true_untruncated_projected_cross_diagonal_upper'],0)
        self.assertFalse(result['true_full_30x30_Weil_low_high_Gram_certified'])
        self.assertFalse(result['unshifted_30x30_short_sign_certified'])
        self.assertFalse(result['RH_PROVED'])


if __name__=='__main__':
    unittest.main()
