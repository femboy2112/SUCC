import unittest
from fractions import Fraction as F
from observational_succ.gamma_prime_phase_lock import (
    PhaseLockError,prime_power_parent,phase_lock,source_verified_phase_lock)

class PhaseLockTests(unittest.TestCase):
    def test_true_primes_and_powers(self):
        for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(16,2),(27,3),(49,7),(81,3)]:
            self.assertEqual(prime_power_parent(n),p)

    def test_fake_independent_composite(self):
        for n in [0,1,-2,6,10,12,15,18,21,36,False,2.0]:
            with self.subTest(n=n),self.assertRaises(PhaseLockError):
                phase_lock(n,0)

    def test_half_density_and_gamma_rate(self):
        for n in [2,3,4,5,7,8,9,16]:
            for j in range(8):
                p=phase_lock(n,j)
                self.assertEqual(p['gamma_ou_decay_rate'],F(4*j+1,2))
                self.assertEqual(p['exact_rational_times_inv_sqrt_n'],F(1,n**(2*j)))
                self.assertEqual(p['resulting_exact_rational_log_p_multiplier'],F(1,n**(2*j+1)))
                self.assertTrue(p['source_product_not_assumed'])

    def test_index_gates(self):
        for idx in [-1,100001,0.2,True]:
            with self.assertRaises(PhaseLockError):phase_lock(2,idx)

    def test_authentic_source_matches_tape(self):
        try:
            import observational_succ.source_weil_hierarchy  # noqa
            import observational_succ.tate_suzuki_shorting  # noqa
        except ImportError:
            self.skipTest('original source not mounted in isolated synthetic fixture')
        p=source_verified_phase_lock(4,3)
        self.assertTrue(p['source_verified'])
        self.assertEqual(p['prime_parent'],2)
        with self.assertRaises(PhaseLockError):source_verified_phase_lock(9,0)

if __name__ == '__main__':unittest.main()
