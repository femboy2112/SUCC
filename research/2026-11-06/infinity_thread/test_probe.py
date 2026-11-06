"""Focused finite validations of conditional infinity-thread proof, not normality."""
import unittest
from cmath import exp
from math import pi
from random import Random
from fractions import Fraction
from probe import (authentic_r,independent_four_poles,original_fractions,
                   averaged_energy,prefix_max,gluing_upper,horizon_parameters,
                   poiss_half,run)


def energies_clock(seq):
    N=len(seq);m=N.bit_length()-1
    assert N==(1<<m)
    energies=[]
    for k in range(m+1):
        Q=1<<k;M=N//Q
        means=[sum(seq[j+t*Q] for t in range(M))/M for j in range(Q)]
        energies.append(sum(abs(x)**2 for x in means)/Q)
    return energies


class InfinityThreadFiniteTests(unittest.TestCase):
    def test_source_exact_rational(self):
        for n in range(1,257):
            self.assertEqual(authentic_r(n),independent_four_poles(n))
            self.assertEqual(authentic_r(n).denominator%2,1)
        self.assertEqual(original_fractions(1),[Fraction(0)])

    def test_gluing_universal_anti_fit_controls(self):
        rng=Random(411006)
        for A in (64,128,256):
            kinds=[
                [1+0j]*(2*A),
                [(-1)**n+0j for n in range(2*A)],
                [exp(2j*pi*rng.random()) for _ in range(2*A)],
            ]
            for seq in kinds:
                E=averaged_energy(seq,A)
                sup=prefix_max(seq,A)
                self.assertLessEqual(sup,gluing_upper(A,E)+1e-10)
                self.assertGreaterEqual(E,-1e-12)
                self.assertLessEqual(E,1+1e-10)

    def test_clock_wavelet_exact_telescoping(self):
        rng=Random(16422)
        for seq in (
            [exp(2j*pi*rng.random()) for _ in range(128)],
            [exp(2j*pi*n/17) for n in range(128)],
        ):
            levels=energies_clock(seq)
            self.assertAlmostEqual(levels[-1],1,places=12)
            self.assertAlmostEqual(levels[-1]-levels[0],
                                   sum(levels[k+1]-levels[k] for k in range(7)),places=12)
            for k in range(7):self.assertLessEqual(levels[k],levels[k+1]+1e-10)

    def test_poisson_fourier_normalization(self):
        from math import cos
        r=.5
        for theta in (0,.1,.3,.7,.99):
            closed=(1-r*r)/(1-2*r*cos(2*pi*theta)+r*r)
            terms=1+sum(2*r**h*cos(2*pi*h*theta) for h in range(1,21))
            self.assertLessEqual(abs(closed-terms),2**(1-20)+1e-12)

    def test_predeclared_source_and_shadow_holdouts(self):
        report=run()
        self.assertEqual(report['normality'],'OPEN')
        self.assertEqual(report['A_holdouts'],[2048,4096])
        original=[r for r in report['rows'] if r['kind']=='original_zero_four_pole']
        shadow=[r for r in report['rows'] if r['kind']=='isometric_nonnormal_H_shadow']
        periodic=[r for r in report['rows'] if r['kind']=='periodic_rational_beta_1_17']
        self.assertEqual(len(original),2)
        for r in original:
            self.assertEqual(r['M_count'],65)
            self.assertLessEqual(r['h1_prefix_shell_sup_float'],
                                 r['h1_gluing_bound_float']+1e-10)
        self.assertTrue(all(all(v>.99 for v in r['h1_to_h3_avg_R_float']) for r in shadow))
        self.assertTrue(all(all(abs(v-1)<1e-10 for v in r['h1_to_h3_avg_R_float']) for r in periodic))

if __name__=='__main__':unittest.main()
