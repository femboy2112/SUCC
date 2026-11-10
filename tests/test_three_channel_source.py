"""Exact rational and hostile controls for three-channel BBP source."""
import unittest
import math
from fractions import Fraction
from observational_succ.three_channel_source import (
    source, source_four_poles, raw_gram, determinant_3, principal_minors,
    channel_weights, response, response_magnitude, signed_covariance,
)


class ThreeChannel(unittest.TestCase):
    def test_four_pole_exact(self):
        for a in (1,17,33,127,Fraction(7,2),1024):
            self.assertEqual(source(a),source_four_poles(a))

    def test_positive_three_dimensional_gram(self):
        for a in (1,17,64,128,1024):
            self.assertTrue(all(x>0 for x in principal_minors(a)))

    def test_mixture_weights(self):
        for a in (1,17,1024,1000000):
            self.assertEqual(sum(channel_weights(a)),1)
            self.assertTrue(all(x>0 for x in channel_weights(a)))
        w=channel_weights(10**9)
        self.assertLess(max(abs(float(x)-y) for x,y in zip(w,(6/15,4/15,5/15))),1e-8)

    def test_gram_asymptotic(self):
        for a in (1000,10000,100000):
            v=Fraction(a)**15*determinant_3(raw_gram(a))
            self.assertLess(abs(float(v)-57600)/57600,0.1 if a==1000 else 0.015)

    def test_poisson_exact(self):
        for t in (0,.1,math.pi/2,math.pi,2*math.pi/3):
            z=complex(math.cos(t),math.sin(t))
            self.assertAlmostEqual(abs(response(z)),response_magnitude(t),places=12)
        self.assertAlmostEqual(abs(response(-1)),1/9)
        self.assertAlmostEqual(abs(response(1)),1)

    def test_seed_blind_gram(self):
        self.assertEqual(raw_gram(17),raw_gram(17))
        self.assertNotEqual(raw_gram(17),raw_gram(33))

    def test_joint_covariance_countermodels(self):
        p=[1,-1,1,-1]
        self.assertEqual(signed_covariance(p,p),1)
        self.assertEqual(signed_covariance(p,[-x for x in p]),-1)
        self.assertEqual(signed_covariance(p,[1]*4),0)

    def test_three_channels_not_nine_independent(self):
        w=channel_weights(17)
        cov=[[(w[i] if i==j else 0)-w[i]*w[j] for j in range(3)] for i in range(3)]
        self.assertTrue(all(sum(row)==0 for row in cov))
        self.assertEqual(determinant_3(cov),0)


if __name__=='__main__':
    unittest.main()
