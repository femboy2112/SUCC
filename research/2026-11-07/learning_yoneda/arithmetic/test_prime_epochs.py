import unittest
from fractions import Fraction as Q
import prime_epochs as p


class PrimeEpochTests(unittest.TestCase):
    def test_clean_source_epochs(self):
        for prime in (577,641,881,1201,1601):
            w,counts=p.exact_clean_check(prime)
            self.assertEqual(sum(counts.values()),w['L'])

    def test_selector_and_exact_interval_weights(self):
        for A in (37,73,137,257,521):
            prime=p.good_prime(A)
            self.assertIsNotNone(prime)
            self.assertLessEqual(prime,4*A)
            self.assertGreater(p.order16(prime)**3,prime)
            w=p.window(prime)
            full=sum(abs(Q(int(A<=n<2*A),A)-Q(int(w['start']<=n<w['stop']),w['L']))
                     for n in range(min(A,w['start']),max(2*A,w['stop'])))
            self.assertEqual(full,p.variation(A,prime))
            self.assertLessEqual(full,Q(4*(A-w['L']),A))

    def test_no_gauss_saving_claim_when_bound_large(self):
        self.assertGreater(p.gauss_rational_upper(641),1)

    def test_reject_wrong_arithmetic_domains(self):
        for prime in (9,15,2,3,7,True,17.0):
            with self.subTest(prime=prime),self.assertRaises(ValueError):
                p.window(prime)
        for h in (0,137,274,True,1.0):
            with self.subTest(h=h),self.assertRaises(ValueError):
                p.gauss_rational_upper(137,h)


if __name__=='__main__':
    unittest.main()
