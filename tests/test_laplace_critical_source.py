"""Exact local source/Cauchy/Laplace tests; no assertion of pi normality."""
from __future__ import annotations
import cmath
from fractions import Fraction
from math import exp, pi, isclose
import unittest

from observational_succ.duck_bbp import forcing
from observational_succ import laplace_critical_source as L


def independent_four_poles(n):
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


class TestCriticalLaplace(unittest.TestCase):
    def test_density_exact_all_source_poles(self):
        for n in list(range(1,60))+[101,193,457]:
            self.assertEqual(L.source_laplace_moment(n), forcing(n))
            self.assertEqual(L.source_laplace_moment(n), independent_four_poles(n))

    def test_density_positive(self):
        for den in (1,7,41,256):
            for a in range(den+1):
                self.assertGreaterEqual(L.density_polynomial(Fraction(a,den)),0)

    def test_density_endpoints(self):
        self.assertEqual(L.density_polynomial(Fraction(0)),4)
        self.assertEqual(L.density_polynomial(Fraction(1)),0)

    def test_source_first_jet(self):
        self.assertEqual(L.asymptotic_leading(),Fraction(15,64))

    def test_source_recurrence_exact(self):
        for seed in (Fraction(0),Fraction(1,5),Fraction(-3,17)):
            x=L.lifted_phases(110,seed)
            for n in range(110):
                self.assertEqual((16*x[n]+forcing(n+1))%1,x[n+1])

    def test_ward_exponent_exact(self):
        x=L.lifted_phases(120)
        for h in (-17,-1,0,1,3,16,257):
            for n in (0,1,9,23,55,118):
                self.assertEqual(L.ward_phase_residual(x,h,n),0)

    def test_ward_rejects_mutated_source(self):
        x=L.lifted_phases(60)
        self.assertNotEqual((x[12]-16*x[11]-(forcing(12)+Fraction(1,100)))%1,0)

    def test_future_tail_bounds(self):
        for n,depth in ((0,3),(5,0),(17,5),(64,11)):
            lo,hi=L.source_tail_from_r(n,depth)
            bigger=sum((forcing(n+j)/16**j for j in range(1,depth+21)),Fraction())
            self.assertLessEqual(lo,bigger)
            self.assertLess(bigger,hi)

    def test_p_additive_fraction(self):
        for p in (3,5,7,17,41,73):
            for x in (Fraction(4,15),Fraction(7,21),Fraction(-9,146),Fraction(23,41)):
                y=L.p_fractional_part(x,p)
                d=x.denominator
                while d%p==0: d//=p
                self.assertEqual((x-y).denominator%p!=0,True)
                if x.denominator%p: self.assertEqual(y,0)
                self.assertNotEqual((x-y).denominator%p,0)

    def test_adelic_gluing_exact(self):
        for x in (Fraction(4,15),Fraction(3,35),Fraction(-9,146),Fraction(23,41),Fraction(83,1)):
            for h in (-3,1,5):
                y=sum((L.p_fractional_part(x,p) for p in (2,3,5,7,11,17,41,73)),Fraction())
                # All denominators here factor within this finite prime list.
                self.assertEqual((h*(x-y))%1,0)

    def test_laplace_overlap_trivial_coherent_guard(self):
        n=16
        a=tuple(cmath.exp(2j*pi*j/n) for j in range(n))
        b=tuple(v.conjugate() for v in a)
        for tau in (0.,0.25,1.,3.):
            direct,dual=L.laplace_phase_overlap(a,b,tau)
            target=sum(exp(-tau*j/n) for j in range(n))/n
            self.assertLess(abs(direct-target),1.e-13)
            self.assertLess(abs(direct-dual),1.e-12)

    def test_laplace_real_source_overlap(self):
        A=32; p=73; h=3
        phases=L.lifted_phases(2*A)
        a=[]; b=[]
        for n in range(A,2*A):
            x=phases[n]
            xp=L.p_fractional_part(x,p)
            a.append(cmath.exp(2j*pi*float((h*xp)%1)))
            b.append(cmath.exp(2j*pi*float((h*(x-xp))%1)))
        for tau in (0.,0.4,1.5):
            direct,dual=L.laplace_phase_overlap(tuple(a),tuple(b),tau)
            original=sum((exp(-tau*j/A)*cmath.exp(2j*pi*float((h*phases[A+j])%1)) for j in range(A)),0j)/A
            self.assertLess(abs(direct-dual),2e-12)
            self.assertLess(abs(direct-original),1e-12)

    def test_epoch_error(self):
        for tau in (0.,1/4,1.):
            a=[(-1)**j for j in range(400)]
            g=sum(exp(-tau*j/400)*a[j] for j in range(400))/400
            mu=sum(a)/400
            self.assertLessEqual(abs(g-mu),L.laplace_epoch_zero_error(tau)+1e-14)

    def test_source_twist_tail_bound(self):
        for A in (4,10,32):
            t=1./A
            for N in (A,4*A,12*A):
                self.assertGreater(L.source_twist_tail_bound(t,N),0)
                self.assertLess(L.source_twist_tail_bound(t,N),2*(1+t)*exp(-N/A))

    def test_ward_bound_nontrivial_at_subcritical(self):
        for h in (1,16,256):
            vals=[L.ward_boundary_bound(1/A,h) for A in (128,256,512)]
            self.assertGreater(vals[0],vals[1])
            self.assertGreater(vals[1],vals[2])

    def test_ward_bound_crudely_dominates_truncation(self):
        for A,h in ((20,1),(40,10),(30,1000)):
            t=1/A
            z=exp(-t)
            phases=L.lifted_phases(12*A)
            e=sum((z**n*cmath.exp(2j*pi*float((16*h*phases[n])%1))*(cmath.exp(2j*pi*float((h*forcing(n+1))%1))-1) for n in range(12*A)),0j)
            self.assertLessEqual((1-z)*abs(e),L.ward_boundary_bound(t,h)+1e-9)

    def test_laplace_source_twist_critical_is_nonzero_finite(self):
        for A,h in ((64,64),(128,256),(256,1024)):
            val=L.source_twist(1/A,h,12*A)
            self.assertLess(val.real,-0.1)

    def test_laplace_source_twist_correct_phase_sign(self):
        for A in (16,32):
            val=L.source_twist(1/A,A*A//8,12*A)
            val_neg=L.source_twist(1/A,-A*A//8,12*A)
            self.assertLess(abs(val.conjugate()-val_neg),1e-14)

if __name__=='__main__': unittest.main()

class TestSourceGammaAndSpectrum(unittest.TestCase):
    def test_renormalized_source_moment_exact(self):
        for N in (1,2,3,17,100):
            d=L.source_renormalized_moment(N)
            independent=sum((n*independent_four_poles(n)-Fraction(15,64*n) for n in range(1,N+1)),Fraction())
            self.assertEqual(d,independent)

    def test_renormalized_tail_budget_holds_on_finite_difference(self):
        bigger=L.source_renormalized_moment(600)
        for N in (2,4,8,16,40,100):
            self.assertLessEqual(abs(bigger-L.source_renormalized_moment(N)), L.source_renormalized_tail_bound(N))

    def test_matched_second_jet_mutant(self):
        # c=(1,-2,-1,2) has zero sum and zero first weighted moment,
        # but weighted second moment 16; perturb by 1/10.
        c=(1,-2,-1,2); b=(7,4,3,2)
        self.assertEqual(sum(c),0)
        self.assertEqual(sum(x*y for x,y in zip(c,b)),0)
        self.assertEqual(sum(x*y*y for x,y in zip(c,b)),16)
        for n in (3,10,100,300):
            mutant=forcing(n)+Fraction(1,10)*sum((Fraction(x,8*n-y) for x,y in zip(c,b)),Fraction())
            self.assertNotEqual(mutant,forcing(n))
            self.assertLess(abs(mutant-forcing(n)),Fraction(1,n**3))

    def test_signed_spectral_low_high_is_algebraically_safe(self):
        for A in (16,32):
            a=tuple(cmath.exp(2j*pi*j/A) for j in range(A))
            b=tuple(z.conjugate() for z in a)
            for cutoff in (0,1,2,4):
                if cutoff>=(A-1)//2:continue
                out=L.signed_overlap_certificate(a,b,cutoff,.5)
                self.assertLessEqual(abs(out['signed_low']),out['low_upper']+1e-11)
                self.assertLessEqual(abs(out['signed_high']),out['high_upper']+1e-11)
                self.assertLess(abs(out['signed_total']-sum(exp(-.5*j/A) for j in range(A))/A),1e-11)

    def test_signed_spectral_actual_source(self):
        A=32;p=73;ph=L.lifted_phases(2*A)
        pa=tuple(cmath.exp(2j*pi*float(L.p_fractional_part(ph[n],p))) for n in range(A,2*A))
        comp=tuple(cmath.exp(2j*pi*float((ph[n]-L.p_fractional_part(ph[n],p))%1)) for n in range(A,2*A))
        for tau in (0.,.25,1.):
            out=L.signed_overlap_certificate(pa,comp,2,tau)
            direct=sum((exp(-tau*j/A)*cmath.exp(2j*pi*float(ph[A+j])) for j in range(A)),0j)/A
            self.assertLess(abs(out['signed_total']-direct),1e-11)
            self.assertLessEqual(abs(out['signed_low']),out['low_upper']+1e-11)
            self.assertLessEqual(abs(out['signed_high']),out['high_upper']+1e-11)
