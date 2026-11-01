"""Root-discoverable exact source and independent adaptive Fourier frame tests."""
import cmath
import importlib.util
import math
import pathlib
import sys
import unittest
from fractions import Fraction as F

ROOT=pathlib.Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'adaptive_arctan_frame'
OLD=pathlib.Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'arctan_reciprocity'

def load(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    o=importlib.util.module_from_spec(s);sys.modules[name]=o;s.loader.exec_module(o)
    return o

m=load('succ_adaptive_frame_unique',ROOT/'adaptive_frame.py')
o=load('succ_adaptive_poly_oracle_unique',ROOT/'polynomial_oracle.py')
prior=load('succ_prior_mirror_unique',OLD/'arctan_mirror.py')

class ExactSourceAndProof(unittest.TestCase):
    def test_source_contract_against_parent(self):
        for n in range(1,130):
            self.assertEqual(m.source(n),prior.forcing(n))
            self.assertEqual(m.source(n),m.source_combined(n))

    def test_wrong_types_rejected(self):
        for h in (0,-1,True,1.2):
            with self.assertRaises(m.FrameError):m.source_index(h)
        with self.assertRaises(m.FrameError):m.original_phase_states(5,seed=0.1)
        with self.assertRaises(m.FrameError):m.frame_paper_bound(5,1,F(-1),F(0))
        with self.assertRaises(m.FrameError):m.gaussian_power(1,0,True)

    def test_exact_polynomial_certificate(self):
        proof=o.verify_coefficients()
        self.assertEqual(proof['status'],'EXACT_INTEGER_POLYNOMIAL_CERTIFIED')
        self.assertGreater(proof['sine_lower_taylor'],F(1,8))
        self.assertEqual(proof['coefficients'],m.arithmetic_source_polynomial_certificates())

    def test_inequalities_exact_on_grid(self):
        for n in range(2,140):
            r=m.source(n)
            self.assertGreater(r,F(15,64*n*n))
            self.assertLess(r,F(8,15*n*n))
            self.assertGreater(F((n-1)**2+1)*r,F(1,5))
            if n>=8:self.assertLess(r,F(9,32*n*n))

    def test_exact_radix_indices(self):
        self.assertEqual(m.source_index(1),1)
        self.assertEqual(m.source_index(16),8)
        self.assertEqual(m.source_index(256),16)
        self.assertEqual(m.source_index(4096),128)
        self.assertEqual(m.valuation16(16**3*7),3)
        for h in range(1,3000):
            a=m.source_index(h)
            z=h if m.valuation16(h)%2==0 else 4*h
            self.assertTrue((a-1)**2<z<=a*a)
            self.assertNotEqual(m.valuation16(h)%2,m.valuation16(16*h)%2)

    def test_original_orbit_exact(self):
        for n in (1,2,5,14,31):
            self.assertEqual(m.original_phase_states(n),prior.rational_orbit(n))
        self.assertEqual(m.original_phase_states(1)[0],F(2,15))

class UniformFrame(unittest.TestCase):
    def test_uniform_exact_denominators(self):
        for h in list(range(1,101))+[128,256]:
            c=m.frame_cross_integer(h)
            self.assertGreater(c['determinant_squared'],F(1,64))
            self.assertEqual(c['uniform_abs_lower'],F(1,8))
            self.assertNotEqual(c['numerator'],0)

    def test_independent_float_angle_diagnostic(self):
        # Diagnostic only; mathematical authority is the exact polynomials.
        for h in [1,2,3,5,13,16,17,31,32,96,256,1024,4096]:
            q=m.source_axis(h);q2=m.source_axis(16*h)
            delta=16*h*math.atan(float(q2))-h*math.atan(float(q))
            self.assertGreater(abs(math.sin(delta)),1/8)
            self.assertLess(abs(delta),math.pi/2)
            if h<=256:
                exact=m.frame_cross_integer(h)
                self.assertAlmostEqual(abs(math.sin(delta))**2,float(exact['determinant_squared']),places=11)

    def test_prior_fixed_axis_actual_resonance(self):
        # This explicitly refutes trying to carry a UNIFORM >=1/8 bound
        # from the fixed r(2) mirror of the parent PR.
        self.assertLess(prior.mirror_sine_squared(13),F(1,400))
        self.assertGreater(m.frame_cross_integer(13)['determinant_squared'],F(1,64))

    def test_parity_mutation_loses_uniform_bound_exactly(self):
        # A source-native but non-alternating all-slow index is NOT adequate.
        h=3
        k1=m.ceil_sqrt(4*h)
        k2=m.ceil_sqrt(4*16*h)
        q1,q2=m.source(k1),m.source(k2)
        a,b=m.gaussian_power(q1.denominator,-q1.numerator,h)
        c,d=m.gaussian_power(q2.denominator,q2.numerator,16*h)
        cross=a*d+b*c
        norm=(q1.denominator**2+q1.numerator**2)**h*(q2.denominator**2+q2.numerator**2)**(16*h)
        self.assertLess(F(cross*cross,norm),F(1,64))
        self.assertGreater(m.frame_cross_integer(h)['determinant_squared'],F(1,64))

    def test_gaussian_two_projection_compatibility(self):
        for h in (1,2,3,5,16,17,31,64):
            left=m.signed_coefficients(h)
            right=m.signed_coefficients(16*h)
            r1=left['real'];i1=left['imag'];r2=right['real'];i2=right['imag']
            self.assertEqual((r1*r2+i1*i2)**2+(r1*(-i2)+i1*r2)**2,
                             left['norm_squared']**h*right['norm_squared']**(16*h))

    def test_uniform_projection_reconstruction_real_stream(self):
        # Independent complex-plane identity for ARBITRARY streams, not BBP only.
        for h in (1,2,3,16,17):
            x1=h*math.atan(float(m.source_axis(h)))
            x2=16*h*math.atan(float(m.source_axis(16*h)))
            for z in [complex(0.3,0.6),complex(-0.7,0.12),complex(0.01,-0.8)]:
                b1=(cmath.exp(-1j*x1)*z).imag
                b2=(cmath.exp(-1j*x2)*z).imag
                recovered=(b1*cmath.exp(1j*x2)-b2*cmath.exp(1j*x1))/math.sin(x2-x1)
                self.assertAlmostEqual(recovered.real,z.real,places=11)
                self.assertAlmostEqual(recovered.imag,z.imag,places=11)

    def test_true_source_finite_unconditional_bound(self):
        for n in (2,10,32,64):
            orbit=m.original_phase_states(n)
            for h in (1,2,3,5,7,13):
                z=sum(cmath.exp(2j*math.pi*h*float(x)) for x in orbit)/n
                w=sum(cmath.exp(2j*math.pi*16*h*float(x)) for x in orbit)/n
                x1=h*math.atan(float(m.source_axis(h)))
                x2=16*h*math.atan(float(m.source_axis(16*h)))
                b1=(cmath.exp(-1j*x1)*z).imag
                b2=(cmath.exp(-1j*x2)*w).imag
                bound=8*(abs(b1)+abs(b2)+float(m.source_radix_error(n,h)))
                self.assertLessEqual(abs(z),bound+1e-12)

class RationalIntervalOracle(unittest.TestCase):
    def test_arctan_interval_special_n1(self):
        lo,hi=m.axis_angle_interval(1,24)
        self.assertLess(lo,hi)
        self.assertLess(float(lo),math.atan(47/15)+1e-12)
        self.assertGreater(float(hi),math.atan(47/15)-1e-12)
        self.assertLess(hi-lo,F(1,10**15))
        self.assertGreater(lo,F(3,4))

    def test_pi_interval_parent_independent(self):
        self.assertEqual(m.pi_interval(20),prior.pi_bracket(20))
        for h in (2,3,16,17,48):
            lo,hi=m.axis_angle_interval(h)
            self.assertLessEqual(lo,hi)
            self.assertLessEqual(float(lo),math.atan(float(m.source_axis(h)))+1e-12)
            self.assertGreaterEqual(float(hi),math.atan(float(m.source_axis(h)))-1e-12)

    def test_sin_cos_rational_interval(self):
        for a,b in [(F(0),F(0)),(F(1,5),F(1,5)+F(1,10**10)),(F(3),F(3)+F(1,10**7)),(F(-3),F(-3)+F(1,10**9))]:
            sl,su=m.sin_interval(a,b,18)
            cl,cu=m.cos_interval(a,b,18)
            for x in (a,b,(a+b)/2):
                self.assertLessEqual(float(sl)-1e-14,math.sin(float(x)))
                self.assertGreaterEqual(float(su)+1e-14,math.sin(float(x)))
                self.assertLessEqual(float(cl)-1e-14,math.cos(float(x)))
                self.assertGreaterEqual(float(cu)+1e-14,math.cos(float(x)))

    def test_certified_original_cases(self):
        for n,h in ((4,1),(8,2),(12,3),(16,5),(20,1),(24,13)):
            r=m.certified_original_frame_probe(n,h,terms=19)
            self.assertGreater(r['frame_bound']**2,r['upper_A_squared'])
            self.assertEqual(r['frame_lower_det'],F(1,8))
            self.assertLess(r['mirror_h'][1]-r['mirror_h'][0],F(1,10**13))

    def test_zero_angle_interval(self):
        lo,hi=m.phase_angle_interval(F(0),1,theta_harmonic=None)
        self.assertEqual((lo,hi),(0,0))
        # A 15th harmonic of authentic U1=2/15 has exact integer phase.
        lo,hi=m.phase_angle_interval(F(2,15),15,theta_harmonic=None)
        self.assertEqual((lo,hi),(0,0))

    def test_rational_seed_hostile_case(self):
        # A simple nonselected rational seed does not become normal by covariance.
        for n in (1,5,16):
            obs=m.original_phase_states(n,seed=F(1,5))
            self.assertNotEqual(obs,m.original_phase_states(n))

if __name__=='__main__':unittest.main()

class FiniteObserverMutation(unittest.TestCase):
    def test_rational_completed_positive_strict_fake(self):
        for depth in (2,5,16,40):
            q=m.finite_positive_counterfeit_completed(depth)
            self.assertIsInstance(q,F)
            self.assertGreater(q,0)
            prev=None
            for n in range(1,depth+13):
                y=m.finite_positive_counterfeit_source(n,depth)
                self.assertGreater(y,0)
                if prev is not None:self.assertLess(y,prev)
                prev=y
            # Identity for geometric tail: sum_{j>=1}16^-j 2^-j = 1/31.
            self.assertEqual(q-sum((m.source(j)*F(1,16**j) for j in range(1,depth+1)),F(0)),
                             m.source(depth)*F(1,31*16**depth))

    def test_finite_observer_source_and_mirror_indistinguishable(self):
        H=20
        depth=max(18,max(m.source_index(16*h) for h in range(1,H+1)))
        orig=m.original_phase_states(18)
        counterfeit=m.finite_positive_counterfeit_states(18,depth)
        self.assertEqual(orig,counterfeit)
        for h in range(1,H+1):
            self.assertLessEqual(m.source_index(h),depth)
            self.assertLessEqual(m.source_index(16*h),depth)
            self.assertEqual(m.source_axis(h),m.finite_positive_counterfeit_source(m.source_index(h),depth))
            self.assertEqual(m.source_axis(16*h),m.finite_positive_counterfeit_source(m.source_index(16*h),depth))
        self.assertNotEqual(m.finite_positive_counterfeit_source(depth+1,depth),m.source(depth+1))
        self.assertNotEqual(m.finite_positive_counterfeit_states(depth+1,depth)[-1],m.original_phase_states(depth+1)[-1])
