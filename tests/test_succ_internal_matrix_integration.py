"""Native-host checks against Main X original source and Pascal/Walsh/Fourier code.

Run on full SUCC checkout. Do not run with shims; independent source refs
are essential. No nontrivial zero or pi-normality assertion.
"""
import unittest
from fractions import Fraction as Q
from observational_succ.succ_internal_matrix_walk import (
    authentic_r, original_state, MatrixWalk, exact_source_digits,
    walsh_digit_energy, gram_spectral_certificate,
    PhasePoly,source_cyclotomic_quotient,
)
from observational_succ import bbp_natural_carrier as NC
from observational_succ import integer_bbp_carrier as IC
from observational_succ import pi_joint_prime_carrier as JP
from observational_succ import pascal_carry_interferometry as PC
from observational_succ import gamma_bbp_signed_coherence as SGO
from observational_succ import dynamic_fourier_tower as DFT


class NativeSourceMatrixIntegration(unittest.TestCase):
    def test_all_four_source_implementations_agree(self):
        for n in range(1,51):
            value=authentic_r(n)
            a,b=IC.forcing_pair(n)
            self.assertEqual(value,Q(a,b))
            self.assertEqual(value,NC.exact_forcing(n))
            self.assertEqual(value,JP.forcing(n))

    def test_all_four_orbit_realizations_agree(self):
        states=IC.source_states(38)
        jp=JP.states(39)
        walk=MatrixWalk.initial(4)
        for n in range(0,39):
            self.assertEqual(original_state(n),NC.orbit_state(n).rational)
            self.assertEqual(original_state(n),Q(states[n].numerator,states[n].conductor))
            self.assertEqual(original_state(n),jp[n])
            self.assertEqual(original_state(n),SGO.authentic_orbit_rational(n))
            if n>0:
                walk=walk.succ()
                self.assertEqual(walk.lifted_state,original_state(n))
                self.assertTrue(gram_spectral_certificate(walk)['offdiagonal_excess'].star()==gram_spectral_certificate(walk)['offdiagonal_excess'])

    def test_walsh_gram_is_original_pascal_high_four_interaction(self):
        walk=MatrixWalk.initial(4)
        for _ in range(53):walk=walk.succ()
        digits=exact_source_digits(walk.history)
        proof=walsh_digit_energy(digits)
        hist=proof['counts']
        native=PC.walsh_moments(hist)
        self.assertEqual(tuple(Q(v,walk.time) for v in native),proof['walsh_amplitudes'])
        native_certificate=PC.walsh_pascal_certificate(hist)
        self.assertEqual(native_certificate['walsh_moments'],native)
        self.assertEqual(native[-1],walk.time*proof['highest_joint_bit_amplitude'])
        self.assertEqual(proof['spectral_energy'],proof['collision_energy'])

    def test_formal_free_phase_algebra_to_actual_cyclotomic_quotient(self):
        # e(0)+e(1/2) != zero in the formal group algebra, but evaluates
        # to zero exactly in Q(zeta_2) where zeta_2=-1.
        aliased=PhasePoly.one()+PhasePoly.monomial(Q(1,2))
        self.assertNotEqual(aliased,PhasePoly.zero())
        self.assertEqual(source_cyclotomic_quotient(aliased,2),
                         __import__("observational_succ.finite_fourier_carrier",fromlist=["CyclotomicElement"]).CyclotomicElement.scalar(2,0))
        f=PhasePoly.monomial(Q(2,15))
        self.assertNotEqual(source_cyclotomic_quotient(f,30).polynomial,(Q(0),))
        from observational_succ.succ_internal_matrix_walk import MatrixWalkError
        with self.assertRaises(MatrixWalkError):
            source_cyclotomic_quotient(f,14)

    def test_declared_dyadic_fourier_quotient_compatible(self):
        walk=MatrixWalk.initial(3)
        for _ in range(43):walk=walk.succ()
        hist=walsh_digit_energy(exact_source_digits(walk.history))['counts']
        correct=DFT.exact_fourier_restriction(hist,4)
        self.assertTrue(correct['all_character_squares_exact'])
        self.assertFalse(correct['full_adelic_or_archimedean_completion'])


if __name__=='__main__':unittest.main()
