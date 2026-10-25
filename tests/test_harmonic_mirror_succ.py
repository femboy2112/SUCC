"""Exact independent controls for the mirror SUCC and BBP four rays."""
import unittest
from fractions import Fraction as Q
from math import comb

from observational_succ.harmonic_mirror_succ import (
    harmonic, harmonic_pascal, harmonic_difference, harmonic_mirror_history,
    mirror_step, reciprocal_orbit, unipotent_shear, prime_fucc_log_bracket,
    source_rays, bbp_mirror_forcing, source_pole_moment, source_signed_harmonic_sum,
    counterfeit_mirror_tail, counterfeit_mirror_force, counterfeit_mirror_state,
)


class MirrorSuccTests(unittest.TestCase):
    def test_reciprocal_succ_semiconjugacy(self):
        for n in range(1,101):
            self.assertEqual(mirror_step(Q(1,n)),Q(1,n+1))
            for k in range(9):
                self.assertEqual(reciprocal_orbit(n,k),Q(1,n+k))

    def test_matrix_exponent_independent_multiplication(self):
        for k in range(0,23):
            a,b=unipotent_shear(k)
            self.assertEqual((a,b),((1,0),(k,1)))
            self.assertEqual(Q(a[0]+a[1]*5,b[0]+b[1]*5),Q(1,5+k))
        self.assertEqual(unipotent_shear(1),((1,0),(1,1)))

    def test_step_composition(self):
        for a in range(8):
            for b in range(8):
                self.assertEqual(mirror_step(mirror_step(Q(3,7),a),b),
                                 mirror_step(Q(3,7),a+b))

    def test_harmonic_accumulation_is_not_only_reciprocal_orbit(self):
        self.assertEqual(harmonic(0),Q())
        self.assertEqual(harmonic_mirror_history(0),())
        for n in range(1,30):
            hist=harmonic_mirror_history(n)
            self.assertEqual(hist[-1],(n,Q(1,n),harmonic(n)))
            self.assertEqual(harmonic(n)-harmonic(n-1),Q(1,n))

    def test_classical_pascal_harmonic_identity_direct(self):
        for n in range(0,55):
            self.assertEqual(harmonic(n),harmonic_pascal(n))

    def test_forward_pascal_harmonic_difference(self):
        for n in range(0,15):
            for k in range(1,11):
                direct=sum((Q((-1)**(k-j)*comb(k,j))*harmonic(n+j)
                            for j in range(k+1)),Q())
                self.assertEqual(harmonic_difference(n,k),direct)

    def test_fucc_log_rectangular_trapezoidal_bounds(self):
        # Float log is only a sanity check; mathematical proof is integral
        # Riemann lower/trapezoid upper, not numerical certification.
        from math import log
        for n in range(1,21):
            for q in (2,3,5,7,11):
                low,high=prime_fucc_log_bracket(n,q)
                self.assertEqual(high-low,Q(q-1,2*q*n))
                self.assertLess(float(low),log(q))
                self.assertLess(log(q),float(high))

    def test_fucc_multiplication_cocycle(self):
        for n in range(1,10):
            for p in (2,3,5):
                for q in (2,3,5):
                    self.assertEqual(harmonic(p*q*n)-harmonic(n),
                        (harmonic(p*q*n)-harmonic(q*n))+(harmonic(q*n)-harmonic(n)))

    def test_original_bbp_four_reciprocal_rays(self):
        for n in range(1,151):
            rays=source_rays(n)
            self.assertEqual(len(rays),4)
            for c,x in zip((7,4,3,2),rays):
                self.assertEqual(mirror_step(x,8),Q(1,8*(n+1)-c))
            direct=Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
            self.assertEqual(bbp_mirror_forcing(n),direct)
            self.assertGreater(direct,0)

    def test_signed_zero_moment_and_first_two_nonzero(self):
        self.assertEqual(source_pole_moment(0),0)
        self.assertEqual(source_pole_moment(1),15)
        self.assertEqual(source_pole_moment(2),151)
        for r in range(8):
            self.assertEqual(source_pole_moment(r),4*7**r-2*4**r-3**r-2**r)

    def test_signed_harmonic_forcing_is_original_unweighted_sum(self):
        for n in range(0,26):
            self.assertEqual(source_signed_harmonic_sum(n),
                sum((bbp_mirror_forcing(j) for j in range(1,n+1)),Q()))

    def test_mutated_mirror_coefficient_not_source_faithful(self):
        # Four mirrored rays alone do not fix the authentic coefficients.
        n=23
        rays=source_rays(n)
        counterfeit = rays[0]-rays[1]
        self.assertNotEqual(counterfeit,bbp_mirror_forcing(n))
        self.assertEqual(sum((1,-1,0,0)),0)  # Same 1/n cancellation.

    def test_hostile_positive_reciprocal_source_is_nonnormal(self):
        # Same N carrier, signed reciprocal SUCC components, positive force,
        # and leading 15/(64*n^2); BUT the authenticated four poles change.
        self.assertEqual(counterfeit_mirror_state(0),Q())
        self.assertEqual(counterfeit_mirror_tail(0),Q(1,128))
        for n in range(1,75):
            r=counterfeit_mirror_force(n)
            self.assertGreater(r,0)
            self.assertEqual(r,16*counterfeit_mirror_tail(n-1)-counterfeit_mirror_tail(n))
            self.assertEqual(counterfeit_mirror_state(n),
                16*counterfeit_mirror_state(n-1)+r)
            self.assertEqual(r,Q(16,64*n)-Q(17,64*(n+1))+Q(1,64*(n+2)))
            if n>=2:
                self.assertEqual(counterfeit_mirror_state(n)%1,
                                 (-counterfeit_mirror_tail(n))%1)
        self.assertNotEqual(counterfeit_mirror_force(1),bbp_mirror_forcing(1))
        # 16^n/128 is an integer for every n>=2; the authentic radix
        # orbit of rational alpha*=1/128 is eventually 0, not normal.
        for n in range(2,10):
            self.assertEqual(Q(16**n,128)%1,0)
        # Leading coefficient: n^2*r*(n) -> 15/64, paper algebra.
        for n in (10,100,1000):
            self.assertLess(abs(n*n*counterfeit_mirror_force(n)-Q(15,64)),Q(1,n))

    def test_reject_nonexact_and_bad_domain(self):
        for invalid in (0,-1,True):
            with self.assertRaises(ValueError):reciprocal_orbit(invalid)
        for func,args in ((mirror_step,(0,)),(mirror_step,(0.5,)),
                (unipotent_shear,(-1,)),(harmonic,(-1,)),
                (harmonic_difference,(1,0)),(prime_fucc_log_bracket,(0,2)),
                (prime_fucc_log_bracket,(1,1)),(bbp_mirror_forcing,(0,)),
                (source_pole_moment,(-1,))):
            with self.assertRaises(ValueError):func(*args)


if __name__ == "__main__":
    unittest.main()
