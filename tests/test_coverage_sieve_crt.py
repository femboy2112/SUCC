"""Independent exact CRT/sieve calibration and source-mutation controls."""
import sys, unittest
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.coverage_lower_bounds import CoverageError, uniform_frame
from observational_succ.coverage_sieve_crt import gaussian_sieve_crt_certificate, split_sieve_mixing_debt

class GaussianCRTCoverageTests(unittest.TestCase):
    def test_true_split_prime_5(self):
        r=gaussian_sieve_crt_certificate(((1,2),))
        self.assertEqual(r['sieve_survivors'],16)
        self.assertEqual(tuple(f['chi2'] for f in r['factors']),(F(1,4),)*2)

    def test_true_split_primes_5_and_13(self):
        r=gaussian_sieve_crt_certificate(((1,2),(2,3)))
        self.assertEqual(r['period'],65)
        self.assertEqual(r['sieve_survivors'],2304)
        self.assertEqual(tuple(f['chi2'] for f in r['factors']),
                         (F(1,4),F(1,4),F(1,12),F(1,12)))
        self.assertEqual(tuple(f['good_mass'] for f in r['factors']),
                         (F(4,5),F(4,5),F(12,13),F(12,13)))
        self.assertTrue(all(f['bad_count']==1 for f in r['factors']))
        self.assertIn('NOT Gaussian-prime walk',r['source_type'])


    def test_exact_irreducible_sieve_cost_and_extra_mixing_debt(self):
        p=5
        good=uniform_frame('sieve','signed',(F(0),)+(F(1,4),)*4)
        self.assertEqual(split_sieve_mixing_debt(good),{
            'irreducible_zero_cost':F(1,4),'path_mixing_debt':F(0),
            'total_chi2':F(1,4)})
        biased=uniform_frame('sieve','signed',(F(0),F(1,2),F(1,2),F(0),F(0)))
        self.assertEqual(split_sieve_mixing_debt(biased)['path_mixing_debt'],F(5,4))
        with self.assertRaises(CoverageError):
            split_sieve_mixing_debt(uniform_frame('wrong','has zero',(F(1,5),)*5))

    def test_fake_source_norm_and_duplicates_refused(self):
        for pairs in (((3,4),),((3,0),),((1,1),),((1,2),(1,2)),()):
            with self.assertRaises(CoverageError):
                gaussian_sieve_crt_certificate(pairs)

    def test_finite_enumeration_cap_is_not_math_obstruction(self):
        with self.assertRaisesRegex(CoverageError,'resource cap'):
            gaussian_sieve_crt_certificate(((1,2),(2,3)),max_period=64)

if __name__=='__main__':unittest.main()
