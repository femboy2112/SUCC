"""Hostile minimal-path source test: gauge, q-local counterfeits, spectral lag."""
import unittest
from fractions import Fraction as Q
from math import isqrt
from observational_succ.bbp_source_memory import forcing, tail_interval, forced_step
from observational_succ.bbp_minimal_path_gauge import (
    nearest_integer,circle_distance,is_prime_power_denominator,
    period_phase,single_missing_prime_counterfeit,
)
from observational_succ.bbp_cyclotomic_spectral import (
    dft,single_prime_spectral_ledger,adversarial_alignment,
)


def primes_upto(n):
    return [p for p in range(2,n+1)
            if all(p%d for d in range(2,isqrt(p)+1))]


def primary(q, p):
    """Independent CRT principal part at p; any negative p-adic depth."""
    q=Q(q);den=q.denominator;power=1
    while den%p==0:
        power*=p;den//=p
    return Q(q.numerator*pow(den,-1,power)%power,power) if power>1 else Q(0)


class MinimalPathProofTests(unittest.TestCase):
    def test_rounding_edge_cases(self):
        for r,k in [(Q(0),0),(Q(1,2),1),(Q(-1,2),0),
                    (Q(-3,2),-1),(Q(13,7),2),(Q(-13,7),-2)]:
            self.assertEqual(nearest_integer(r),k)
        self.assertEqual(circle_distance(Q(1,9),Q(8,9)),Q(2,9))
        self.assertTrue(is_prime_power_denominator(Q(17,3**9),3))
        self.assertFalse(is_prime_power_denominator(Q(1,35),3))

    def test_gauge_exact_interval_recursion(self):
        for n in (0,1,2,7,18,60):
            tl,th=tail_interval(n,20)
            ul,uh=tail_interval(n+1,20)
            # Same infinite Green equality via independent enclosures.
            self.assertLessEqual(16*tl-uh,forcing(n+1))
            self.assertGreaterEqual(16*th-ul,forcing(n+1))
            self.assertGreater(tl,0)
        for n in range(2,100):
            self.assertGreater(forcing(n),0)
            self.assertLess(forcing(n),1)

    def test_periodic_near_source_initial_point_without_pi_digits(self):
        for L in (8,12,25):
            z,err=period_phase(L)
            self.assertGreater(z,0)
            self.assertLess(z,1)
            self.assertLess(err,Q(1,16**(L-1)))
            self.assertEqual((16**L*z)%1,z)

    def test_missing_prime_all_other_primary_torsion_is_exact(self):
        x=single_missing_prime_counterfeit(55,period=25,missing_prime=3,
                                          precision=Q(1,10**6),frozen_prefix=4)
        for r in x['records']:
            self.assertLess(r['forcing_error'],Q(1,10**6)/16**r['n'])
            self.assertGreater(r['source'],0)
            self.assertTrue(is_prime_power_denominator(r['counterfeit_phase']-r['authentic_phase'],3))
            self.assertTrue(is_prime_power_denominator(r['source']-forcing(r['n']),3))
            for p in primes_upto(59):
                if p != 3:
                    self.assertEqual(primary(r['counterfeit_phase'],p),primary(r['authentic_phase'],p))
                    self.assertEqual(primary(r['source'],p),primary(forcing(r['n']),p))
        for r in x['records'][:4]:
            self.assertEqual(r['forcing_error'],0)
        self.assertTrue(any(r['forcing_error']>0 for r in x['records'][4:]))

    def test_second_missing_prime_and_false_generalization(self):
        # Not a property unique to q=3: density of q^-k works for q=5.
        x=single_missing_prime_counterfeit(35,period=22,missing_prime=5,
                                          precision=Q(1,10**5),frozen_prefix=2)
        self.assertTrue(all(r['forcing_error']<Q(1,10**5)/16**r['n'] for r in x['records']))
        self.assertTrue(all(is_prime_power_denominator(r['source']-forcing(r['n']),5) for r in x['records']))
        with self.assertRaises(ValueError):
            single_missing_prime_counterfeit(4,period=1,precision=Q(1,10**6))
        with self.assertRaises(ValueError):
            single_missing_prime_counterfeit(4,period=20,missing_prime=9)

    def test_forced_selected_phase_changes_despite_weak_source_convergence(self):
        x=single_missing_prime_counterfeit(70,period=24,missing_prime=3,
                                          precision=Q(1,10**5),frozen_prefix=4)
        for r in x['records']:
            self.assertLess(circle_distance(r['counterfeit_phase'],r['period_phase']),
                            r['tail_upper']+r['target_error'])
            if r['n']>=2:
                self.assertLess(r['source'],1)
        self.assertNotEqual(x['records'][-1]['counterfeit_phase'],x['records'][-1]['authentic_phase'])

    def test_cyclic_dft_exact_identity_numerically_calibrated(self):
        for p in (17,41,73,97,113,257):
            r=single_prime_spectral_ledger(p)
            self.assertAlmostEqual(abs(r['full']-r['fourier_reconstruction']),0,places=10)
            self.assertAlmostEqual(abs(r['full']-r['zero_mode']-r['mixed']),0,places=10)
            self.assertAlmostEqual(r['u_energy'],1,places=10)
            self.assertLessEqual(abs(r['mixed']),r['gauss_upper_nonzero']+1e-8)
            self.assertLessEqual(abs(r['local_mean']),1+1e-8)
            self.assertLessEqual(r['v_energy'],1+1e-8)
        # Remove the complex conjugate to see that a source-blind local
        # cancellation bound fails for an adversarial complementary clock.
        for p in (17,41,73,97,113):
            local, global_amplitude=adversarial_alignment(p)
            self.assertAlmostEqual(global_amplitude,1,places=12)
            self.assertLess(local,1)


if __name__=='__main__':unittest.main()
