"""Finite exact source controls and spectral positivity/energy escape diagnostics."""
import unittest
from fractions import Fraction
from math import pi
from cmath import exp
from probe import original,spectrum,wavelet,run

class SpectralExorcismTests(unittest.TestCase):
    def test_literal_zero_and_rational_poles(self):
        xs=original(256)
        self.assertEqual(xs[0],Fraction(0))
        for n in range(1,256):
            r=(xs[n]-16*xs[n-1])%1
            expected=(Fraction(4,8*n-7)-Fraction(2,8*n-4)
                      -Fraction(1,8*n-3)-Fraction(1,8*n-2))%1
            self.assertEqual(r,expected)
    def test_fejer_energy_positive(self):
        xs=original(512)
        for N in (256,512):
            for H in (8,16,32):
                e=spectrum(xs,N,H)
                self.assertGreaterEqual(e['fejer_float'],1)
                self.assertGreaterEqual(e['unweighted_float'],0)
    def test_dyadic_telescoping_and_shadow(self):
        xs=original(512)
        for N in (256,512):
            for ys in (xs,[Fraction(n,(2*n-1)**4) for n in range(N)],
                       [Fraction(pow(16,n,17),17) for n in range(N)]):
                data=wavelet(ys,N)
                self.assertAlmostEqual(sum(data['increments_float']),data['escape_float'],places=7)
        shadow=wavelet([Fraction(n,(2*n-1)**4) for n in range(512)],512)
        self.assertLess(shadow['escape_float'],0.001)
    def test_preregistered_original_holdouts(self):
        result=run()
        self.assertEqual(result['normality'],'OPEN')
        self.assertEqual([r['N'] for r in result['spectra']],[256,512,1024])
        self.assertEqual([r['H'] for r in result['periodic_fejer']],[16,256,4096])
        for r in result['spectra']:
            self.assertTrue(all(r['H'][str(H)]['fejer_float']>=1 for H in (8,16,32)))

if __name__=='__main__':unittest.main()
