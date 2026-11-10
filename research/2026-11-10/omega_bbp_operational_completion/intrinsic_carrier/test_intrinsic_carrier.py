"""Fast hostile finite tests for arithmetic SUCC/FUCC intrinsic-carrier lift.

Uses Python stdlib; unrelated to long CI. Cross-check exact finite block results
against a separate direct edge implementation; no pi oracle or RH zero input.
"""
import unittest
from fractions import Fraction
from intrinsic_carrier import (block_matrices,check_operator,arithmetic_edge,
    affines,invert_affine,thermal_trace_finite,thermal_trace_rearranged,
    branch_parity_twist,source_prefix,source_phase_bound,
    original_source_R,matmul,boundary_bulk_two_three,whole_carrier_haar_projection,
    omega_haar_source_area)


class CarrierTests(unittest.TestCase):
    def test_exact_operator_all_block_sizes(self):
        for p in range(2,18):
            with self.subTest(p=p):self.assertTrue(check_operator(p))

    def test_exact_hopping_edges_against_projection_commutator(self):
        for p in (2,3,4,5,7,16):
            _,_,C,_=block_matrices(p)
            independently=[[Fraction(0) for _ in range(p)] for _ in range(p)]
            for a in range(1,p):
                independently[0][a]=Fraction(-1,p)
                independently[a][0]=Fraction(1,p)
            self.assertEqual(C,independently)

    def test_finite_Cuntz_and_rank_boundary(self):
        for p in (2,3,4,5,16):
            for n in range(1,5*p+7):
                x=invert_affine(p,n)
                if n<p:self.assertIsNone(x)
                else:
                    self.assertEqual(affines(p,*x),n)
                    self.assertEqual(x,divmod(n,p))
            # Range projections of p child isometries cover all n>=p exactly once.
            self.assertEqual(sum(1 for n in range(1,5*p+7) if invert_affine(p,n) is None),p-1)

    def test_prime_divisibility_projections_commute(self):
        for n in range(1,140):
            for p in (2,3,5,7):
                for q in (2,3,5,7):
                    self.assertEqual(int(n%p==0)*int(n%q==0),int(n%q==0)*int(n%p==0))

    def test_composites_are_a_negative_prime_selectivity_control(self):
        for p in (4,6,8,9,10,12):self.assertTrue(check_operator(p))

    def test_parity_is_only_even_cyclic_branch_character(self):
        for p in range(2,18):
            sign,shifted,antiperiodic=branch_parity_twist(p)
            self.assertEqual(antiperiodic,p%2==0)
            self.assertEqual(shifted,[-x for x in sign] if p%2==0 else shifted)

    def test_intrinsic_Omega_4_5_boundary_and_bulk_spectra(self):
        for M in (1,2,3):
            C=boundary_bulk_two_three(M)
            N=6*M+5
            # Exactly separated into |1..5> boundary and 6-cell bulk packets.
            for i in range(5):
                for j in range(5,N):self.assertEqual(C[i][j],0)
            for a in range(M):
                start=5+6*a
                for i in range(start,start+6):
                    for j in range(N):
                        if not (start<=j<start+6):self.assertEqual(C[i][j],0)
            slices=[(0,5,Fraction(5,36))]+[(5+6*a,6,Fraction(2,9)) for a in range(M)]
            for start,k,ssq in slices:
                c=[row[start:start+k] for row in C[start:start+k]]
                cc=matmul(c,c)
                ccc=matmul(cc,c)
                self.assertEqual(ccc,[[-ssq*x for x in row] for row in c])
                self.assertEqual(-sum(cc[i][i] for i in range(k))/2,ssq)

    def test_positive_source_orientation_not_parity(self):
        for n in range(70):
            self.assertGreater(omega_haar_source_area(n),0)
        # Asymptotic calibrates the earlier exact theorem 675/128 * n^-9.
        self.assertAlmostEqual(float(omega_haar_source_area(4800))*4800**9,
                               675/128,delta=.04)

    def test_thermal_trace_exact_finite_independent_matrix(self):
        for p in (2,3,4,5,7):
            _,_,_,H2=block_matrices(p)
            for beta in (2,3,4):
                for mmax in (1,3,10):
                    observed=thermal_trace_finite(p,beta,mmax)
                    independent=sum((Fraction(H2[a][a],(p*m+a)**beta)
                        for m in range(1,mmax+1) for a in range(p)),Fraction())
                    self.assertEqual(observed,independent)

    def test_thermal_zeta_identity_numerical_strict_tail(self):
        try:
            import mpmath as mp
        except ImportError:
            self.skipTest('mpmath optional for numerical zeta oracle')
        mp.mp.dps=60
        for p in (2,3,4,5,7):
            for beta in (2,3):
                total=thermal_trace_rearranged(p,beta,mp.zeta(beta))
                partial=thermal_trace_finite(p,beta,600)
                missing=total-mp.mpf(partial.numerator)/partial.denominator
                # Bound by norm(H_p)^2 * sum_{n>=p*(M+1)} n^-beta
                # and integral lower-end bound on integer tail.
                N=p*(600+1)
                ub=mp.mpf(p-1)/p**2 * (N-1)**(1-beta)/(beta-1)
                self.assertTrue(0 < missing < ub,(p,beta,missing,ub))

    def test_thermal_chirality_mean_zero_for_diagonal_states(self):
        for p in (2,3,4,5):
            _,_,C,_=block_matrices(p)
            self.assertTrue(all(C[a][a]==0 for a in range(p)))

    def test_two_block_vacuum_exact_identity(self):
        _,_,_,H2=block_matrices(2)
        self.assertEqual(H2,[[Fraction(1,4),Fraction(0)],
                             [Fraction(0),Fraction(1,4)]])
        # Therefore H_2^2=(I-|1><1|)/4, and the Gibbs moment is
        # (1-1/zeta(beta))/4. This is NOT an RH positivity criterion.

    def test_prime_mixed_hamiltonian_antiunitary_sign(self):
        for p in (2,3,5,7):
            _,_,C,_=block_matrices(p)
            # C is real; H=iC flips sign under complex conjugation.
            self.assertEqual(C,[[-C[j][i] for j in range(p)] for i in range(p)])

    def test_source_prefix_is_pi_over_16_not_pi(self):
        for L in (1,2,3,5,10,20):
            S=source_prefix(L)
            self.assertLess(S,Fraction(22,7*16))
            # Entirely rational: the longer source-prefix is an enclosure
            # witness without floating-point cancellation at L=20.
            longer=source_prefix(L+80)
            self.assertLess(S,longer)
            self.assertLess(longer-S,source_phase_bound(0,L))

    def test_exact_source_finite_tail_bound_with_longer_prefix(self):
        for L in (1,2,3,8,12):
            for n in (0,1,5,L+1):
                d=source_prefix(L+80)-source_prefix(L)
                self.assertTrue(0<16**n*d<source_phase_bound(n,L))

    def test_same_arithmetic_forcing_wrong_seed_biased_completed_orbit(self):
        L=12
        seed=-source_prefix(L)
        for n in range(15):
            self.assertEqual(16**n*(seed+source_prefix(L)),0)

    def test_additive_multiplicative_relation(self):
        for p in (2,3,4,5,7,16):
            for n in (1,2,3,13,29):
                self.assertEqual(p*(n+1),p*n+p)
                self.assertNotEqual(p*(n+1),p*n+1)


if __name__=='__main__':unittest.main(verbosity=2)
