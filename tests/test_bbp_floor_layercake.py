"""Exact BBP floor/threshold/prime slip and diagnostic Fourier tests."""
import cmath
import math
import unittest
from fractions import Fraction as F

from observational_succ.bbp_floor_layercake import (
    threshold_vector, carry_from_thresholds, haar_indicator_masses,
    haar_carry_masses, real_carry, modular_injection, prime_carry,
    joint_carry_step, centered_floor_character, floor_fourier_coefficient,
    fejer_floor_character, boundary_distance, fejer_epoch_budget,
    fejer_source_twist_budget,
)
from observational_succ.duck_bbp import forcing

class FloorLayerCake(unittest.TestCase):
    def test_original_r_equals_frozen_four_poles(self):
        for n in range(1,220):
            a=8*n-7
            self.assertEqual(forcing(n),4*F(1,a)-2*F(1,a+3)-F(1,a+4)-F(1,a+5))

    def test_thresholds_exact_all_integer_carries(self):
        for r in (F(0),F(1,8),F(77,100)):
            for x in (F(0),F(1,32),F(1,7),F(15,16),F(999,1000)):
                self.assertEqual(carry_from_thresholds(x,r),(16*x+r).__floor__())
        for j in range(17):
            x=F(j,16)
            if x<1:self.assertEqual(carry_from_thresholds(x,F(0)),j)

    def test_exact_continuous_integrals_and_uniform_residue(self):
        for r in (F(0),F(1,5),F(13,16),F(127,128)):
            mass=haar_carry_masses(r)
            self.assertEqual(sum(mass),1)
            for d in range(16):
                self.assertEqual(mass[d]+(mass[16] if d==0 else 0),F(1,16))
            self.assertEqual(sum(j*m for j,m in enumerate(mass)),F(15,2)+r)
            self.assertEqual(sum(haar_indicator_masses(r)),F(15,2)+r)

    def test_centered_primitive_char_matches_raw(self):
        for n in (2,3,8,25,99):
            r=forcing(n)
            for x in (F(0),F(1,17),F(4,13),F(399,400)):
                for h in (1,2,7,8,15):
                    raw=cmath.exp(2j*math.pi*h*carry_from_thresholds(x,r)/16)
                    self.assertLess(abs(raw-centered_floor_character(x,r,h)),5e-13)

    def test_exact_prime_real_slip_along_original_orbit(self):
        p=241
        real=F(0)
        prime=0
        for n in range(1,195):
            r=forcing(n)
            if n == 1:
                real=(16*real+r)%1
                prime=modular_injection(n,p)
                self.assertEqual(prime,0)
                continue
            v=joint_carry_step(real,prime,n,p)
            self.assertEqual(v['slip'],v['threshold_slip'])
            self.assertEqual(v['next_complement'],v['predicted_complement'])
            self.assertEqual(v['next_real'],(16*real+r)%1)
            self.assertEqual(v['next_prime'],(16*prime+modular_injection(n,p))%p)
            cp,z=prime_carry(prime,modular_injection(n,p),p)
            self.assertEqual((cp,z),(v['next_prime'],v['prime_carry']))
            real=v['next_real'];prime=v['next_prime']

    def test_prime_stages_come_from_four_poles(self):
        # First-shell p=241 prime births at 31,121,151,181.
        p=241
        births=[]
        for n in range(1,193):
            if modular_injection(n,p):births.append(n)
        self.assertEqual(births,[31,121,151,181])

    def test_fourier_single_congruence_and_shift(self):
        for h in (1,3,7,8,15):
            for m in range(-65,66):
                for r in (F(0),F(1,8)):
                    c=floor_fourier_coefficient(m,h,r)
                    if m==0 or (m-h)%16:self.assertEqual(c,0)
                    else:self.assertLess(abs(c),10/abs(m))

    def test_direct_independent_piecewise_fourier_integration(self):
        for h in (1,5,8,13):
            for r in (F(0),F(1,7),F(7,10)):
                bounds=sorted({0.,1.}|{float(F(j,16)-r/16) for j in range(1,17)
                                       if 0<F(j,16)-r/16<1})
                for m in range(-33,34):
                    if m==0:continue
                    integral=0j
                    for left,right in zip(bounds,bounds[1:]):
                        center=(left+right)/2
                        k=math.floor(16*center+float(r))
                        f=cmath.exp(2j*math.pi*h*k/16)
                        integral+=f*(cmath.exp(-2j*math.pi*m*left)-cmath.exp(-2j*math.pi*m*right))/(2j*math.pi*m)
                    self.assertLess(abs(integral-floor_fourier_coefficient(m,h,r)),4e-13)

    def test_fejer_bound_keeps_boundary_cost(self):
        H=256
        for h in (1,4,8,15):
            for x in (F(1,9),F(5,21),F(997,1000)):
                r=F(3,17)
                err=abs(cmath.exp(2j*math.pi*h*carry_from_thresholds(x,r)/16) -fejer_floor_character(x,r,h,H))
                d=boundary_distance(x,r)
                bound=min(2.,1/(H*float(d))) if d else 2.
                self.assertLessEqual(err,bound+1e-12)
        phases=[F(1,9),F(5,21),F(997,1000)]
        shifts=[F(3,17)]*3
        budget,bad=fejer_epoch_budget(phases,shifts,F(1,1024),H)
        err=sum(abs(cmath.exp(2j*math.pi*carry_from_thresholds(x,r)/16)-fejer_floor_character(x,r,1,H))
                for x,r in zip(phases,shifts))/len(phases)
        self.assertLessEqual(err,float(budget)+1e-12)

    def test_wrong_seed_one_fifth_prime_invisible_real_carries_change(self):
        # Literal same forcing and positive p-unit rational seed (the 16-periodic
        # circle displacement 1/5). No pi digits or exotic sample selection.
        p=241
        x=F(0)
        y=F(1,5)
        cp=0
        mismatches=0
        nchecked=0
        for n in range(1,201):
            rn=forcing(n)
            if n>1:
                j=modular_injection(n,p)
                if 100<=n<200:
                    kx=carry_from_thresholds(x,rn)
                    ky=carry_from_thresholds(y,rn)
                    self.assertIn((ky-kx)%16,(3,4))
                    self.assertNotEqual(ky%16,kx%16)
                    mismatches+=1
                    nchecked+=1
                cp=(16*cp+j)%p
            else:cp=modular_injection(n,p)
            x=(16*x+rn)%1
            y=(16*y+rn)%1
            self.assertEqual(y,(x+F(1,5))%1)
        self.assertEqual(mismatches,100)
        self.assertEqual(nchecked,100)

    def test_haar_floor_character_numerical_zero(self):
        for h in (1,2,3,8,15):
            for r in (F(0),F(1,7),F(9,10)):
                masses=haar_carry_masses(r)
                integral=sum(m*cmath.exp(2j*math.pi*h*k/16)
                             for k,m in enumerate(masses))
                self.assertLess(abs(integral),1e-14)

    def test_positive_source_floor_laplace_matches_independent_bins(self):
        # Independent source integral as a weighted sum over finite bins,
        # compared to the closed threshold-geometric-series formula.
        shifts=(0,3,4,5)
        coeffs=(4,-2,-1,-1)
        for a in (1., 2., 17.):
            lam=a
            R=sum(w/(a+d) for w,d in zip(coeffs,shifts))
            for z in (1.,-1.,0.5):
                closed=sum(w/(a+d)*(-math.expm1(-(a+d)/lam)) /
                           (1-z*math.exp(-(a+d)/lam))
                           for w,d in zip(coeffs,shifts))/R
                direct=0.
                for k in range(120):
                    moment=sum(w/(a+d)*(math.exp(-(a+d)*k/lam)-
                                          math.exp(-(a+d)*(k+1)/lam))
                               for w,d in zip(coeffs,shifts))
                    direct+=z**k *moment/R
                self.assertLess(abs(closed-direct),3e-12)

    def test_source_floor_gamma_two_reference_limit(self):
        # Limiting Gamma(2,1) floor PGF, not the actual real digit orbit.
        q=math.exp(-1)
        limit=lambda z:(1-2*q+q*q*z)/(1-q*z)**2
        self.assertAlmostEqual(limit(1),1)
        self.assertGreater(limit(-1),0)
        for a in (100.,1000.):
            R=sum(w/(a+d) for w,d in zip((4,-2,-1,-1),(0,3,4,5)))
            measured=sum(w/(a+d)*(-math.expm1(-(a+d)/a))/
                         (1+math.exp(-(a+d)/a))
                         for w,d in zip((4,-2,-1,-1),(0,3,4,5)))/R
            self.assertLess(abs(measured-limit(-1)),0.01 if a==100 else 0.001)

    def test_forcing_shift_is_invisible_below_quadratic_fourier_depth(self):
        for n in (100,256):
            for H in (17,64,257,1024):
                bound=fejer_source_twist_budget(n,1,H)
                for x in (F(1,16),F(1,16)-forcing(n)/32,F(1,7),F(357,512)):
                    diff=abs(fejer_floor_character(x,forcing(n),1,H)-
                             fejer_floor_character(x,F(0),1,H))
                    self.assertLessEqual(diff,float(bound)+1e-12)
                self.assertLess(float(bound),2*H*float(forcing(n))/8+float(forcing(n))*2)

    def test_exact_finite_receipt_replay(self):
        from pathlib import Path
        import importlib.util
        import json
        root=Path(__file__).resolve().parents[1]
        directory=root/"research/2026-11-09/floor_layercake_prime_carry"
        spec=importlib.util.spec_from_file_location("flp_receipt_probe",directory/"experiment.py")
        mod=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        recorded=json.loads((directory/"FINITE_RECEIPT.json").read_text(encoding="utf-8"))
        self.assertEqual(mod.receipt(),recorded)
        self.assertEqual([row["real_prime_equal_carry_count"] for row in recorded["cases"]],
                         [8,11,19])
        self.assertEqual([row["changed_seed_one_fifth_real_mod16_mismatch_count"]
                          for row in recorded["cases"]],[100,128,256])

    def test_bad_domains(self):
        for f,args in [(threshold_vector,(F(1),F(0))),
                       (threshold_vector,(F(1,2),F(1))),
                       (real_carry,(F(0),1)),
                       (prime_carry,(1,1,2)),
                       (floor_fourier_coefficient,(1,16,F(0))),
                       (fejer_floor_character,(F(0),F(0),1,1))]:
            with self.assertRaises((ValueError,TypeError)):f(*args)

if __name__=="__main__":unittest.main()
