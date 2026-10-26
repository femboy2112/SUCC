"""Exact-Q matrix-time walks, nonuniform band limits and source controls."""
import unittest
from fractions import Fraction as Q
from math import comb
import random

from observational_succ.succ_internal_matrix_walk import (
 MatrixWalkError,PhasePoly, circle,authentic_r, original_state,MatrixWalk,
 formal_character, gram_spectral_certificate,finite_koopman_phases,
 phase_plaquette,signed_source_difference, frequency_boundary_witness,
 temporal_derivative_boundary,walsh_digit_energy,exact_source_digits,
 geometric_frequency_gram,mixed_phase_derivative,
)


class ArithmeticPassport(unittest.TestCase):
    def test_four_poles_equal_independent_rational_combined_form(self):
        for n in range(1,101):
            value=Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(authentic_r(n),value)
            self.assertGreater(authentic_r(n),0)
    def test_zero_origin_and_source_succ(self):
        self.assertEqual(original_state(0),0)
        state=Q()
        for n in range(1,33):
            state=16*state+authentic_r(n)
            self.assertEqual(original_state(n),state)
    def test_truncation_and_type_errors(self):
        for input in (0,-1,1.0,True):
            with self.assertRaises(MatrixWalkError):authentic_r(input)
        for input in (0,1.0,True):
            with self.assertRaises(MatrixWalkError):MatrixWalk.initial(4,input)
        with self.assertRaises(MatrixWalkError):original_state(3000)


class FormalGroupAlgebra(unittest.TestCase):
    def test_phase_unit_periodicity_and_star(self):
        self.assertEqual(circle(Q(-2,3)),Q(1,3))
        e=PhasePoly.monomial(Q(17,5))
        self.assertEqual(e,PhasePoly.monomial(Q(2,5)))
        self.assertEqual(e*e.star(),PhasePoly.one())
        self.assertEqual((e+e.star())*e,PhasePoly.one()+e*e)
        self.assertEqual((e+e.star()).star(),e+e.star())
        self.assertEqual(PhasePoly.monomial(Q(1,2))+PhasePoly.monomial(Q(-1,2),-1),PhasePoly.zero())
    def test_exact_complex_evaluation_distinguished_from_certificate(self):
        p=PhasePoly.monomial(Q(1,2))*Q(3)-PhasePoly.one()
        z=p.evaluation(60)
        self.assertLess(abs(complex(z)-(-4+0j)),1e-50)
    def test_malformed_phase_rejected(self):
        with self.assertRaises(MatrixWalkError):PhasePoly(((Q(1,2),Q(0)),))
        with self.assertRaises(MatrixWalkError):PhasePoly(((Q(2),Q(1)),))
        with self.assertRaises(MatrixWalkError):circle(float('nan'))
        with self.assertRaises(MatrixWalkError):PhasePoly.one()/0


class ExactMatrixDifferential(unittest.TestCase):
    def test_rank_one_current_after_each_real_succ(self):
        state=MatrixWalk.initial(4,1)
        for n in range(1,14):
            old=state
            u,v=old.next_character_vector()
            state=old.succ()
            self.assertEqual(state.time,n)
            self.assertEqual(state.lifted_state,original_state(n))
            for a in range(4):
                for b in range(4):
                    self.assertEqual(state.gram[a][b]-old.gram[a][b],v[a]*v[b].star())
            self.assertTrue(state.validate())
    def test_purity_is_exact_weighted_weyl_excess(self):
        for width,frequency,n in ((2,1,7),(3,1,11),(4,2,8),(6,1,9)):
            state=MatrixWalk.initial(width,frequency)
            for _ in range(n):state=state.succ()
            cert=gram_spectral_certificate(state)
            self.assertEqual(cert['spectral_purity']-width,cert['offdiagonal_excess'])
            self.assertEqual(cert['zero_mode'],PhasePoly.one())
            self.assertEqual(cert['rank_purity_floor'],Q(width*width,min(width,n)))
            value=cert['spectral_purity'].evaluation(75)
            self.assertGreaterEqual(value.real+1e-12,float(cert['rank_purity_floor']))
            self.assertLessEqual(value.real,width*width+1e-12)
            self.assertLess(abs(value.imag),1e-25)
    def test_geometric_ladder_is_not_naive_linear_toeplitz(self):
        state=MatrixWalk.initial(5)
        for _ in range(8):state=state.succ()
        gram=geometric_frequency_gram(state)
        self.assertEqual(gram[0][0],PhasePoly.monomial(0,state.time))
        self.assertEqual(gram[1][0],sum((formal_character(15,u) for u in state.history),PhasePoly.zero()))
        self.assertNotEqual(gram[1][0],state.gram[1][0])
        self.assertEqual(gram[2][1],sum((formal_character(240,u) for u in state.history),PhasePoly.zero()))
        for i in range(5):
            for j in range(5):self.assertEqual(gram[i][j],gram[j][i].star())

    def test_innovation_matches_fejer_source_pairs_exactly(self):
        state=MatrixWalk.initial(4,1)
        for n in range(1,11):
            state=state.succ()
            innovation,predicted=state.innovation()
            self.assertEqual(predicted,state.succ().purity())
            self.assertEqual(innovation.star(),innovation)
    def test_periodic_fixed_source_would_have_maximal_purity(self):
        # Source-independent negative control: a point mass at 0.
        for width in (2,4,7):
            H=width
            v=tuple(PhasePoly.one() for _ in range(H))
            gram=tuple(tuple(v[i]*v[j].star() for j in range(H)) for i in range(H))
            self.assertEqual(sum((gram[i][j]*gram[j][i] for i in range(H) for j in range(H)),PhasePoly.zero()),PhasePoly.monomial(0,H*H))
            self.assertGreater(H*H,H)
    def test_finite_frequency_rank_floor(self):
        state=MatrixWalk.initial(9)
        state=state.succ().succ().succ()
        cert=gram_spectral_certificate(state)
        self.assertEqual(cert['rank_purity_floor'],Q(81,3))
        self.assertGreaterEqual(cert['spectral_purity'].evaluation(75).real,27-1e-12)


class TwistedKoopmanAndBoundary(unittest.TestCase):
    def test_exact_weighted_shift_and_declared_gauge(self):
        for n in (0,1,3,7,29):
            for h in (1,3,-2):
                row=finite_koopman_phases(n,h,8)
                self.assertEqual(row['finite_compression_boundary_squared_norm'],1)
                g=row['diagonal_gauge']
                for k,omega in enumerate(row['phases']):
                    self.assertEqual(circle(g[k]+omega-g[k+1]),0)
                    self.assertEqual(omega,circle(h*16**k*authentic_r(n+1)))
    def test_unwrapped_two_direction_plaquette(self):
        for n in range(15):
            for k in range(5):
                for h in (-3,1,2):
                    exact=15*h*16**k*(authentic_r(n+2)-authentic_r(n+1))
                    self.assertEqual(phase_plaquette(n,k,h),exact)
                    self.assertEqual(phase_plaquette(n,k,h),signed_source_difference(n,1,k+1,h)-signed_source_difference(n,1,k,h))
    def test_all_mixed_matrix_phase_derivatives(self):
        for n in (0,1,3,9):
            for k in range(4):
                for a in range(4):
                    for b in range(1,6):
                        w=mixed_phase_derivative(n,k,a,b)
                        self.assertEqual(w,15**a*signed_source_difference(n,b,k,1))
                        self.assertGreater((-1)**b*w,0)
        self.assertEqual(mixed_phase_derivative(3,2,1,1),phase_plaquette(3,2))

    def test_all_orders_source_pascal_signs(self):
        for n in (0,1,2,3,9,29):
            for order in range(1,9):
                d=signed_source_difference(n,order,0,1)
                self.assertGreater((-1)**order*d,0)
                manual=sum(((-1)**(order-j)*comb(order,j)*authentic_r(n+j+1) for j in range(order+1)),Q())
                self.assertEqual(d,manual)
    def test_critical_frequency_band_survives_local_source_decay(self):
        for j in range(0,9):
            witness=frequency_boundary_witness(j)
            self.assertLess(witness['positive_error'],witness['error_cap'])
            self.assertEqual(witness['frequency_exponent'],j)
            self.assertNotEqual(witness['limiting_twist']%1,0)
        for k in range(0,4):
            self.assertLess(16**k*authentic_r(100000),Q(1,10000000))
    def test_critical_temporal_derivative_band_survives(self):
        for j in range(0,6):
            w=temporal_derivative_boundary(j)
            self.assertLess(w['positive_error'],w['error_cap'])
            self.assertEqual(w['frequency_exponent'],3*j)
            self.assertNotEqual(w['limiting_drift']%1,0)
    def test_invalid_high_frequency_range_rejected(self):
        with self.assertRaises(MatrixWalkError):finite_koopman_phases(3,0,2)
        with self.assertRaises(MatrixWalkError):phase_plaquette(0,-1)
        with self.assertRaises(MatrixWalkError):signed_source_difference(0,-1)


class WalshInternalMatrix(unittest.TestCase):
    def test_exact_sign_hadamard_parseval_carries(self):
        state=MatrixWalk.initial(3)
        for _ in range(64):state=state.succ()
        digits=exact_source_digits(state.history)
        cert=walsh_digit_energy(digits)
        self.assertEqual(cert['alphabet'],16)
        self.assertEqual(cert['spectral_energy'],cert['collision_energy'])
        self.assertEqual(cert['walsh_amplitudes'][0],1)
        self.assertFalse(cert['normality_proved'])
        self.assertFalse(cert['source_authenticated'])
    def test_top_four_bit_interaction_is_essential(self):
        even=tuple(i for i in range(16) if i.bit_count()%2==0)
        cert=walsh_digit_energy(even)
        self.assertEqual(cert['collision_energy'],2)
        self.assertEqual(cert['highest_joint_bit_amplitude'],1)
        self.assertTrue(all(x==0 for x in cert['walsh_amplitudes'][1:15]))
        uniform=walsh_digit_energy(tuple(range(16)))
        self.assertEqual(uniform['collision_energy'],1)
        self.assertEqual(uniform['highest_joint_bit_amplitude'],0)
    def test_random_independent_exact_walsh_controls(self):
        rng=random.Random(2913)
        for _ in range(100):
            words=tuple(rng.randrange(16) for _ in range(rng.randrange(1,25)))
            cert=walsh_digit_energy(words)
            self.assertEqual(cert['spectral_energy'],cert['collision_energy'])
            self.assertGreaterEqual(cert['collision_energy'],1)
    def test_bad_digits_and_trust_boundary(self):
        with self.assertRaises(MatrixWalkError):walsh_digit_energy((0,16),4)
        with self.assertRaises(MatrixWalkError):walsh_digit_energy((1.0,),4)
        with self.assertRaises(MatrixWalkError):exact_source_digits(())
        with self.assertRaises(MatrixWalkError):exact_source_digits((Q(1),),0)


if __name__=='__main__':unittest.main()
