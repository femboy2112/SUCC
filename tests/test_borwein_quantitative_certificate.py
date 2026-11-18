"""Independent rational controls for source-energy-to-digit discrepancy."""
import unittest
from fractions import Fraction as F
from math import pi,sin
from borwein_quantitative_certificate import (C, DELTA, HAAR_MEAN, FOURIER_FLOOR,
     source_r,U,original_phases,L,swept,shadow_tail,origin_breakpoints,
     polynomial_quadrature,original_energy,quantitative_interval_discrepancy,
     discrete_interval_discrepancy)

class QuantitativeBorweinProofTests(unittest.TestCase):
    def test_source_is_literal_four_pole_zero_seed(self):
        self.assertEqual(U(0),0)
        self.assertEqual(U(1),F(47,15))
        for n in (1,2,3,10,31):
            self.assertEqual(U(n),16*U(n-1)+source_r(n))

    def test_exact_mean_and_one_atom_energy(self):
        one_moment=F(8192,3758445)  # 2*C**2*(1/2-DELTA)**5/5
        self.assertEqual(one_moment-HAAR_MEAN**2,F(335872,304434045))
        for x in (F(0),F(1,16),F(1,7),F(8,15)):
            self.assertEqual(polynomial_quadrature((x,)),one_moment-HAAR_MEAN**2)

    def test_exact_quadrature_rotation_invariance(self):
        for vals in ((F(0),F(1,7)),(F(0),F(1,4),F(1,2),F(3,4)),
                     (F(1,15),)*4):
            base=polynomial_quadrature(vals)
            self.assertGreater(base,0)
            for a in (F(0),F(1,9),F(3,17),F(1,2)):
                self.assertEqual(polynomial_quadrature(tuple((x+a)%1 for x in vals)),base)

    def test_exact_quadrature_independent_polynomial_pointwise_integral(self):
        for vals in ((F(0),F(1,3),F(2,3)),
                     (F(1,7),F(2,9),F(4,17)),original_phases(4)):
            q=polynomial_quadrature(vals)
            # Real-valued Riemann sum approximates the independently integrated
            # exact rational polynomial. This is a check, not a proof.
            m=3000
            approx=sum(float(swept(vals,F(2*j+1,2*m))-HAAR_MEAN)**2 for j in range(m))/m
            self.assertLess(abs(float(q)-approx),1e-6)
            self.assertGreaterEqual(q,0)

    def test_original_BBP_energy_positive_finite_shells(self):
        for B in (2,4,8,16):
            q=original_energy(B)
            self.assertGreater(q,0)
            self.assertLess(q,F(1))
            self.assertLess(shadow_tail(B),F(1))

    def test_original_two_pulse_fourier_floor_spectral_modes(self):
        # Independent numerical cross-check of exact trig inequality:
        # Fourier Lhat(h) =4*C*( (4/9)(-1)^h/(2πh)^2 + sin(πh/9)/(2πh)^3).
        for h in range(1,128):
            t=2*pi*h
            hat=4*float(C)*(float(F(4,9))*(-1)**h/t**2+sin(pi*h/9)/t**3)
            self.assertGreaterEqual(abs(hat)*h*h+1e-15,float(FOURIER_FLOOR))
        self.assertEqual(FOURIER_FLOOR,F(2205,139876))

    def test_explicit_discrepancy_rule_uses_exact_upper_square_root(self):
        for B in (2,4,8):
            q=original_energy(B)
            from math import isqrt
            D=10**10
            approx=F(isqrt((q.numerator*D*D+q.denominator-1)//q.denominator)+1,D)
            self.assertGreater(approx*approx,q)
            for H in (1,2,4):
                bound=quantitative_interval_discrepancy(B,H,approx)
                disc=discrete_interval_discrepancy(original_phases(B))
                self.assertGreaterEqual(bound,disc)

    def test_exact_full_discrepancy_catches_duplicate_phase_case(self):
        self.assertEqual(discrete_interval_discrepancy((F(0),)*16),F(1))
        self.assertEqual(discrete_interval_discrepancy((F(0),F(1,2))),F(1,2))
        self.assertEqual(discrete_interval_discrepancy((F(1,10),F(9,10))),F(4,5))

    def test_bad_square_root_certificate_rejected(self):
        with self.assertRaises(ValueError):
            quantitative_interval_discrepancy(4,3,F(0))


class BorweinAutocorrelationAndDigitTests(unittest.TestCase):
    def test_autocorrelation_complementarity(self):
        from borwein_quantitative_certificate import autocorrelation,polynomial_quadrature,autocorrelation_energy
        for t in (F(0),F(1,10),F(1,7),F(1,2),F(17,18)):
            self.assertEqual(autocorrelation(t),autocorrelation(-t))
            self.assertGreaterEqual(autocorrelation(t),0)
        from borwein_quantitative_certificate import C,DELTA
        exact_mean_square=2*C*C*(F(1,2)-DELTA)**5/5
        self.assertEqual(autocorrelation(0),exact_mean_square)
        for phases in ((F(0),),(F(0),F(1,2)),(F(1,7),F(2,9),F(4,17)),original_phases(4)):
            self.assertEqual(autocorrelation_energy(phases),polynomial_quadrature(phases))

    def test_locked_sources_fail_full_normality_energy(self):
        from borwein_quantitative_certificate import autocorrelation_energy
        singleton=F(335872,304434045)
        for B in (2,4,8,16):
            self.assertEqual(autocorrelation_energy((F(0),)*B),singleton)
            self.assertEqual(autocorrelation_energy((F(1,15),)*B),singleton)
            self.assertEqual(autocorrelation_energy((F(1,2),)*B),singleton)
        # Equally spaced finite grids are not Haar, but their kernel energies
        # approach zero while the locked orbit remains fixed away from zero.
        for n in (4,8,16):
            self.assertLess(autocorrelation_energy(tuple(F(i,n) for i in range(n))),singleton)

    def test_source_rational_exact_hex_word_certificates(self):
        from borwein_quantitative_certificate import certified_hex_words
        for B in (4,8,16,32,64):
            for k in (1,2,3):
                counts,ambig=certified_hex_words(B,k)
                self.assertEqual(sum(counts.values())+len(ambig),B)
                self.assertEqual(len(set(ambig)),len(ambig))
                self.assertTrue(all(B<=n<2*B for n in ambig))
                self.assertTrue(all(0<=v<16**k for v in counts))
                self.assertLessEqual(len(ambig),B)

    def test_no_false_hex_ambiguities_in_finite_in_sample_BBP(self):
        from borwein_quantitative_certificate import certified_hex_words
        for B in (32,64,128):
            for k in (1,2,3,4):
                counts,ambig=certified_hex_words(B,k)
                self.assertEqual(len(ambig),0)
                self.assertEqual(sum(counts.values()),B)

    def test_direct_zero_seed_words_agree_with_independent_source_recurrence(self):
        from borwein_quantitative_certificate import certified_hex_words
        for B in (4,8,16,32):
            counts,ambig=certified_hex_words(B,1)
            if ambig: continue
            U_end=U(2*B)
            words=[int((16*U_end/F(16**(2*B-n)))//1)%16
                   for n in range(B,2*B)]
            expect={}
            for w in words:expect[w]=expect.get(w,0)+1
            self.assertEqual(counts,expect)


if __name__=='__main__': unittest.main()
