"""Finite Fourier holdout via dyadic roots, independent of Taylor evaluation."""
from fractions import Fraction as Q
import unittest

from observational_succ.pi_fourier_certificate import (
    pi_orbit_fourier_enclosure, rational_orbit_fourier_enclosure,
)
from observational_succ.pi_polygon_normality import rational_sqrt_enclosure


def machin_interval(terms=48):
    def atan(q):
        value = sum(((-1)**j*q**(2*j+1)/(2*j+1) for j in range(terms)), Q())
        next_term = (-1)**terms*q**(2*terms+1)/(2*terms+1)
        return min(value,value+next_term), max(value,value+next_term)
    l5,u5=atan(Q(1,5)); l239,u239=atan(Q(1,239))
    return 16*l5-4*u239, 16*u5-4*l239


def dyadic_character_holdout(phase, dyadic_bits=20, rounding_bits=160):
    """No Taylor series: nested square roots give a dyadic root of unity.

    Quantize the phase to a dyadic rational and exponentiate its enclosed
    primitive root. Pay at most 8*2^-dyadic_bits for the phase quantization.
    """
    grid = 1 << rounding_bits
    def outward(lo, hi):
        return Q((lo*grid)//1,grid), Q(-((-hi*grid)//1),grid)
    def add(a,b):
        return outward(a[0]+b[0],a[1]+b[1])
    def sub(a,b):
        return outward(a[0]-b[1],a[1]-b[0])
    def mul(a,b):
        values = [x*y for x in a for y in b]
        return outward(min(values),max(values))
    def times(z,w):
        return sub(mul(z[0],w[0]),mul(z[1],w[1])), add(mul(z[0],w[1]),mul(z[1],w[0]))
    cosine, sine = (Q(0),Q(0)), (Q(1),Q(1))  # exp(2*pi*i/4)
    for _ in range(2,dyadic_bits):
        new_cos = (rational_sqrt_enclosure((1+cosine[0])/2,rounding_bits)[0],
                   rational_sqrt_enclosure((1+cosine[1])/2,rounding_bits)[1])
        sine = (rational_sqrt_enclosure((1-cosine[1])/2,rounding_bits)[0],
                rational_sqrt_enclosure((1-cosine[0])/2,rounding_bits)[1])
        cosine = new_cos
    exponent = ((phase % 1)*(1 << dyadic_bits))//1
    result = ((Q(1),Q(1)),(Q(0),Q(0)))
    root = cosine,sine
    while exponent:
        if exponent % 2:
            result = times(result,root)
        root = times(root,root)
        exponent //= 2
    budget = Q(8,1 << dyadic_bits)
    return tuple((lo-budget,hi+budget) for lo,hi in result)


def independent_pi_holdout(base,frequency,depth):
    lo,hi = machin_interval()
    source = (lo+hi)/2
    real_lo = real_hi = imag_lo = imag_hi = Q()
    for j in range(depth):
        re,im = dyadic_character_holdout(frequency*base**j*source)
        real_lo += re[0]; real_hi += re[1]
        imag_lo += im[0]; imag_hi += im[1]
    # Derive the telescoping budget here, without calling the implementation.
    budget = 8*abs(frequency)*(hi-lo)/2*Q(base**depth-1,depth*(base-1))
    return ((real_lo/depth-budget,real_hi/depth+budget),
            (imag_lo/depth-budget,imag_hi/depth+budget))


class CertifiedFourierTests(unittest.TestCase):
    def assertContains(self, interval, value):
        self.assertLessEqual(interval[0],value)
        self.assertLessEqual(value,interval[1])

    def test_periodic_controls_have_exact_known_averages(self):
        zero = rational_orbit_fourier_enclosure(0,2,1,16)
        self.assertEqual(zero.real,(Q(1),Q(1)))
        self.assertEqual(zero.imag,(Q(0),Q(0)))
        self.assertEqual(zero.squared_modulus,(Q(1),Q(1)))
        for n in (2,8,16):
            thirds = rational_orbit_fourier_enclosure(Q(1,3),2,1,n)
            self.assertContains(thirds.real,Q(-1,2))
            self.assertContains(thirds.imag,Q(0))
            self.assertContains(thirds.squared_modulus,Q(1,4))
            quarters = rational_orbit_fourier_enclosure(Q(1,4),2,1,n)
            self.assertContains(quarters.real,Q(n-3,n))
            self.assertContains(quarters.imag,Q(1,n))

    def test_nonreal_gauss_sum_algebraic_control(self):
        # sum_{r in {1,2,4}} exp(2*pi*i*r/7)=(-1+i*sqrt(7))/2.
        result = rational_orbit_fourier_enclosure(Q(1,7),2,1,3)
        self.assertContains(result.real,Q(-1,6))
        lo,hi = result.imag
        self.assertGreater(lo,0)
        self.assertLessEqual(lo*lo,Q(7,36))
        self.assertGreaterEqual(hi*hi,Q(7,36))
        self.assertContains(result.squared_modulus,Q(2,9))

    def test_true_pi_against_machin_and_nested_root_holdout(self):
        for b,h,n in ((2,1,8),(2,1,32),(2,-3,16),(3,2,12)):
            result = pi_orbit_fourier_enclosure(b,h,n)
            holdout = independent_pi_holdout(b,h,n)
            # A sharper Taylor interval lies inside a separately proved wider
            # radical interval. Agreement is a finite holdout, not normality.
            for interval,other in zip((result.real,result.imag),holdout):
                self.assertLess(other[0],interval[0])
                self.assertLess(interval[1],other[1])

    def test_refinement_is_not_cancellation(self):
        coarse = pi_orbit_fourier_enclosure(2,1,32,polygon_steps=2,precision_bits=16)
        self.assertEqual(coarse.real,(Q(-1),Q(1)))
        self.assertEqual(coarse.imag,(Q(-1),Q(1)))
        self.assertEqual(coarse.squared_modulus,(Q(0),Q(1)))
        fine = pi_orbit_fourier_enclosure(2,1,32)
        self.assertLess(fine.source_transport_error,Q(1,10**12))
        self.assertLess(fine.squared_modulus[1],Q(1,20))
        self.assertGreater(fine.squared_modulus[0],Q(1,25))
        # The same precision for a rational nonnormal source retains its bias.
        fixed = rational_orbit_fourier_enclosure(0,2,1,32)
        self.assertEqual(fixed.squared_modulus,(Q(1),Q(1)))

    def test_exact_conjugation_and_modulo_one(self):
        for phase in (Q(11,29),Q(-17,13)):
            positive = rational_orbit_fourier_enclosure(phase,3,2,9)
            negative = rational_orbit_fourier_enclosure(phase+7,3,-2,9)
            self.assertEqual(positive.real,negative.real)
            self.assertEqual(positive.imag,(-negative.imag[1],-negative.imag[0]))
            self.assertEqual(positive.squared_modulus,negative.squared_modulus)

    def test_nonexact_and_invalid_parameters_rejected(self):
        for value in (True,2.0,Q(2)):
            for args in ((value,1,8),(2,value,8),(2,1,value)):
                with self.assertRaises(ValueError):
                    pi_orbit_fourier_enclosure(*args)
        for phase in (True,0.1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):
                rational_orbit_fourier_enclosure(phase,2,1,8)
        for order in (0,-1,True,2.0,Q(2),129):
            with self.assertRaises(ValueError):
                pi_orbit_fourier_enclosure(2,1,8,taylor_order=order)
        for args in ((1,1,8),(2,0,8),(2,1,0),(2,1,4097)):
            with self.assertRaises(ValueError):
                pi_orbit_fourier_enclosure(*args)


if __name__ == '__main__':
    unittest.main()
