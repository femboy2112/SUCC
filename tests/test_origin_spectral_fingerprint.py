"""Exact independent controls for source/origin/spectral fingerprint. No normality claim."""
import itertools
import math
import unittest
from fractions import Fraction
from observational_succ.origin_spectral_fingerprint import (
    original_forcing, iterate, partial_source, split_completed_source,
    original_tail_upper, certified_hex_digits, exact_phase_fraction,
    rational_clock, seed_alias, phase, sideband_coefficients,
    stratum_character_means, stratum_energy, p_primary_part,
    decaying_g, mutant_forcing, word_counts, word_energy,
    word_fourier, machin_pi_over_16_interval,
)


class SourceAndInvariant(unittest.TestCase):
    def test_literal_four_signed_poles(self):
        self.assertEqual(original_forcing(1), Fraction(47, 15))
        for n in range(1, 20):
            r = original_forcing(n)
            self.assertGreater(r, 0)
            # independent common-denominator numerator-polynomial source
            self.assertEqual(r, Fraction(120*n*n - 89*n + 16,
                                         (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
        with self.assertRaises(ValueError):original_forcing(0)

    def test_exact_split_every_rational_seed(self):
        for s in (Fraction(0), Fraction(2, 7), Fraction(-13, 9)):
            for n in (0, 1, 3, 7):
                for L in (0, 2, 5):
                    self.assertEqual(split_completed_source(n, L, s), partial_source(n+L))

    def test_finished_prefix_against_independent_machin(self):
        m, k = 40, 32
        a = partial_source(m)
        b = a + original_tail_upper(m)
        machin_lo, machin_hi = machin_pi_over_16_interval(70)
        self.assertLess(a, machin_hi)
        self.assertLess(machin_lo, b)
        self.assertEqual(int(16**k*machin_lo), int(16**k*machin_hi))
        self.assertEqual(certified_hex_digits(m, k), '3243f6a8885a308d313198a2e0370734')
        self.assertEqual(int(16**k*a), int(16**k*machin_lo))
        with self.assertRaises(ValueError):certified_hex_digits(8, 9)

    def test_seed_cocycle_unwrapped_exact(self):
        for n in (0, 1, 5, 21):
            for q in (Fraction(1, 17), Fraction(3, 512), Fraction(-1, 5)):
                self.assertEqual(iterate(n, q)-iterate(n), 16**n*q)

    def test_coherent_no_pi_oracle_rational_shadow(self):
        # Source-selected reference S_M is finite Fraction, not a pi oracle.
        for A in (8, 16, 32):
            m = 2*A + 7
            s = -partial_source(m)
            for n in range(A, 2*A):
                x = iterate(n, s)
                self.assertLessEqual(x, 0)
                self.assertLess(abs(x), Fraction(1, 64*n*n))


class SeedSpectralStructure(unittest.TestCase):
    def test_alias_tower_and_frequency_gcd(self):
        for N in range(5):
            self.assertTrue(seed_alias(Fraction(1, 16**N), N))
            if N > 0:
                self.assertFalse(seed_alias(Fraction(1, 16**N), N-1))
            self.assertFalse(seed_alias(Fraction(1, 3*16**N), N))
        self.assertTrue(seed_alias(Fraction(1, 2*16**3), 3, (2, 4)))
        self.assertFalse(seed_alias(Fraction(1, 2*16**3), 3, (1, 2)))

    def test_rational_preperiod_and_clock_minimality(self):
        cases = ((Fraction(1, 5), 0, 1), (Fraction(1, 17), 0, 2),
                 (Fraction(1, 257), 0, 4),
                 (Fraction(3, 512*17), 3, 2),
                 (Fraction(-5, 16**3), 3, 1))
        for q, expected_pre, expected_d in cases:
            pre, d, residues = rational_clock(q)
            self.assertEqual((pre, d), (expected_pre, expected_d))
            self.assertEqual(len(residues), d)
            for n in range(pre, pre+3*d):
                self.assertEqual(exact_phase_fraction(q, n),
                                 exact_phase_fraction(q, n+d))
            if d > 1:
                self.assertNotEqual(exact_phase_fraction(q, pre),
                                    exact_phase_fraction(q, pre+1))
        with self.assertRaises(ValueError):rational_clock(Fraction(1, 257), max_period=15)

    def test_two_line_spectrum_sin_cos(self):
        c0, c1 = sideband_coefficients(Fraction(1, 17), 3)
        theta = 2*math.pi*3/17
        self.assertLess(abs(c0-math.cos(theta)), 1e-12)
        self.assertLess(abs(c1-1j*math.sin(theta)), 1e-12)
        self.assertLess(abs(abs(c0)**2+abs(c1)**2-1), 1e-12)

    def test_cyclic_spectra_parseval_and_inversion(self):
        for q in (Fraction(1,5), Fraction(1,7), Fraction(1,17), Fraction(1,257)):
            pre, d, _ = rational_clock(q)
            for h in (-2, 1, 5):
                coefficients = sideband_coefficients(q, h)
                self.assertLess(abs(sum(abs(z)**2 for z in coefficients)-1), 1e-10)
                for j in range(d):
                    actual = phase(q, pre+j, h)
                    reconstructed = sum(coefficients[l]*complex(math.cos(2*math.pi*l*j/d),
                                                                 math.sin(2*math.pi*l*j/d))
                                        for l in range(d))
                    self.assertLess(abs(actual-reconstructed), 1e-10)

    def test_exact_stratified_rational_action(self):
        for q in (Fraction(1,17), Fraction(1,7)):
            pre, d, _ = rational_clock(q)
            A=30
            zero=stratum_character_means(A,d,2)
            moved=stratum_character_means(A,d,2,q)
            self.assertLess(abs(stratum_energy(zero)-stratum_energy(moved)),1e-12)
            for j in range(d):
                factor=phase(q,(A-A%d+j)%d,2)
                self.assertEqual(zero[j][0],moved[j][0])
                self.assertLess(abs(moved[j][1]-factor*zero[j][1]),1e-11)

    def test_seed_sidebands_recover_real_mean(self):
        q=Fraction(1,17)
        A=30;h=2
        zero=stratum_character_means(A,2,h)
        moved=stratum_character_means(A,2,h,q)
        wz=sum(n*z for n,z in zero)/A
        wm=sum(n*z for n,z in moved)/A
        self.assertLessEqual(abs(wm),math.sqrt(stratum_energy(moved))+1e-12)
        self.assertNotAlmostEqual(wz.real,wm.real,places=4)

    def test_p_primary_additive_p_unit_and_mutant_witness(self):
        for n in (1,2,7,14):
            for p in (7, 11, 19):
                q=Fraction(3,17)
                self.assertEqual(p_primary_part(iterate(n)+16**n*q,p),
                                 p_primary_part(iterate(n),p))
        self.assertEqual(mutant_forcing(1)-original_forcing(1),Fraction(1,6939))
        self.assertNotEqual(p_primary_part(mutant_forcing(1),257),
                            p_primary_part(original_forcing(1),257))


class SamePiDifferentSources(unittest.TestCase):
    def test_positive_mutant_and_odd_denominator(self):
        for n in range(1,201):
            r=mutant_forcing(n)
            self.assertGreater(r,0)
            self.assertEqual(r.denominator%2,1)
            self.assertEqual(decaying_g(n).denominator%2,1)
        self.assertGreater(mutant_forcing(1),original_forcing(1))

    def test_null_coboundary_exact_telescoping(self):
        # Sum (delta r)/16^k = g_m/16^m; exactly zero in the limit.
        for M in (1,2,7,20,50):
            self.assertEqual(partial_source(M,mutant_forcing)-partial_source(M),
                             decaying_g(M)/(16**M))
            self.assertEqual(iterate(M,forcing=mutant_forcing)-iterate(M),decaying_g(M))

    def test_mutant_real_phase_cost_finite(self):
        for A in (6,15,50,110):
            h=3
            w0=sum(cmath_phase(iterate(n),h) for n in range(A,2*A))/A
            w1=sum(cmath_phase(iterate(n,forcing=mutant_forcing),h) for n in range(A,2*A))/A
            self.assertLessEqual(abs(w0-w1),math.pi*abs(h)/(1028*A*A)+1e-14)


class DigitSpectra(unittest.TestCase):
    def test_one_digit_spectrum_misses_pair_abnormality(self):
        digits=tuple(range(16))
        c1=word_counts(digits,1)
        c2=word_counts(digits,2)
        self.assertEqual(word_energy(c1,1),0)
        self.assertEqual(word_energy(c2,2),15)
        self.assertLess(abs(word_fourier(c1,(1,))),1e-12)
        self.assertGreater(abs(word_fourier(c2,(1,-1))),0.99)

    def test_exact_energy_split_and_fourier_plancherel(self):
        digit_text=certified_hex_digits(40,32)
        digits=tuple(int(z,16) for z in digit_text)
        for k in (1,2):
            hist=word_counts(digits,k)
            energy=word_energy(hist,k)
            spectral_sum=sum(abs(word_fourier(hist,t))**2
                             for t in itertools.product(range(16), repeat=k)
                             if any(t))
            self.assertLess(abs(spectral_sum-float(energy)),1e-9)
        c1=word_counts(digits,1); c2=word_counts(digits,2)
        increment=word_energy(c2,2)-word_energy(c1,1)
        expected=Fraction(256)*sum(
            (Fraction(c2.get((j,l),0),len(digits))-
             Fraction(c1.get((j,),0),16*len(digits)))**2
            for j in range(16) for l in range(16))
        self.assertEqual(increment,expected)
        self.assertGreaterEqual(increment,0)

    def test_cyclic_compatibility_is_required(self):
        digits=tuple(range(16))
        c1=word_counts(digits,1,cyclic=False)
        c2=word_counts(digits,2,cyclic=False)
        self.assertNotEqual(sum(c1.values()),sum(c2.values()))


def cmath_phase(x,h):
    import cmath
    return cmath.exp(2j*math.pi*float((h*x)%1))


# Additional fresh (post-protocol) exact critical-spectral checks: separate
# theorem vs numerical experiments in the claim ledger.
class CriticalRelativeSpectroscopy(unittest.TestCase):
    def test_exact_critical_phase_formula(self):
        from observational_succ.origin_spectral_fingerprint import relative_phase_arg
        for A in (24, 49, 100):
            for n in (A, (4*A+2)//3, (3*A)//2, 2*A-1):
                if not A<=n<2*A:continue
                got=relative_phase_arg(A,n)
                expected=Fraction(A*A, n*n)*Fraction((2*n)**3,(2*n+1)**3)
                self.assertEqual(got,expected)

    def test_uniform_rational_critical_contrast(self):
        from observational_succ.origin_spectral_fingerprint import relative_phase_arg
        # Entire finite proof uses rational phase intervals and the elementary
        # cosine fact: cos(2πt)<=-1/2 for 3/8<=t<=5/8.
        for A in (24, 48, 64, 97, 128, 233):
            interval=[n for n in range(A,2*A) if 4*A<=3*n and 2*n<=3*A]
            self.assertGreaterEqual(Fraction(len(interval),A),Fraction(1,8))
            for n in interval:
                t=relative_phase_arg(A,n)
                self.assertGreaterEqual(t,Fraction(3,8))
                self.assertLessEqual(t,Fraction(5,8))

    def test_critical_frequency_hits_nonzero_real_line(self):
        from observational_succ.origin_spectral_fingerprint import critical_relative_phase
        for A in (24,48,64,128,256):
            self.assertLess(critical_relative_phase(A).real,13/16+1e-12)

    def test_low_frequency_does_not_resolve_same_pi_mutant(self):
        from observational_succ.origin_spectral_fingerprint import relative_phase_arg
        for A in (16,32,64,128):
            # At h=1, pointwise exact phase difference stays at O(A^-2).
            self.assertTrue(all(0<=decaying_g(n)<=Fraction(1,2056*A*A)
                                for n in range(A,2*A)))


if __name__ == "__main__":
    unittest.main()
