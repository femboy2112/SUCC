"""Independent exact Laurent/phase-transport controls; no signed-saving assertion."""
import importlib.util
import math
import pathlib
import sys
import unittest
from fractions import Fraction as F

ROOT=pathlib.Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'carrier_relative_entropy'

def load_unique(short,filename):
    name='succ_lag_'+short+'_'+str(abs(hash(str(ROOT))))
    spec=importlib.util.spec_from_file_location(name,ROOT/filename)
    v=importlib.util.module_from_spec(spec)
    sys.modules[name]=v
    spec.loader.exec_module(v)
    return v

l=load_unique('normalform','laurent_lag.py')

class TestPoleNormalForm(unittest.TestCase):
    def test_exact_poles_and_residue_sum(self):
        self.assertEqual(sum(l.WEIGHTS),0)
        self.assertEqual(sum((F(w)*p for w,p in zip(l.WEIGHTS,l.POLES)),F(0)),F(15,8))

    def test_original_source_oracle(self):
        for j in range(1,100):self.assertEqual(l.original_r(j),l.direct_r(j))

    def test_initial_laurent_coefficients(self):
        for j in (1,2,4,9):
            self.assertEqual(l.source_laurent_coeff(0,j),0)
            self.assertEqual(l.source_laurent_coeff(1,j),F(15,64))
            self.assertEqual(l.source_laurent_coeff(2,j),F(151-240*j,512))

    def test_eulerian_moments_exact(self):
        self.assertEqual([l.moment(d) for d in range(6)],
                         [F(1,15),F(16,225),F(272,3375),F(1712,16875),F(37808,253125),F(201968,759375)])

    def test_moment_independent_finite_truncation(self):
        for d in (0,1,2,3,5):
            approx=sum((F(j**d,16**j) for j in range(1,100)),F(0))
            self.assertGreater(l.moment(d),approx)
            self.assertLess(l.moment(d)-approx,F(1,10**95))

    def test_leading_curvature_identity(self):
        for n in (1,2,5,32,96):
            for k in (1,2,4,9):
                self.assertEqual(l.corrected_lag(n,k,2),F(16**k-1,64*n*n))
                leading,actual,bound=l.first_positive_curvature_bound(n,k)
                self.assertGreater(leading-actual,0)
                self.assertLess(leading-actual,bound)

    def test_higher_order_polynomial(self):
        for n in (1,2,8,32):
            for k in (1,2,7):
                q=l.corrected_lag(n,k,3)-l.corrected_lag(n,k,2)
                expected=sum((F(16**(k-j)*(151-240*j),512*n**3) for j in range(1,k+1)),F(0))
                self.assertEqual(q,expected)

    def test_all_order_residual_fraction(self):
        for d in (2,3,4,5,7):
            for n in (1,2,7,17,53):
                for k in (1,2,5,11):
                    diff=abs(l.true_source_lag(n,k)-l.corrected_lag(n,k,d))
                    self.assertLess(diff,l.residual_bound(n,k,d))

    def test_exact_integer_ceil_roots(self):
        for p in (2,3,4,5):
            for n in (0,1,2,17,2000,2**41+3):
                r=l.integer_ceil_root(n,p)
                self.assertGreaterEqual(r**p,n)
                if r:self.assertLess((r-1)**p,n)

    def test_rational_ceil_root(self):
        for y in (F(0),F(1,13),F(11,105),F(16,7),F(5000,3)):
            for p in (3,4,7):
                r=l.fractional_ceil_root(y,p)
                self.assertGreaterEqual(r**p,y)
                if r:self.assertLess((r-1)**p,y)

    def test_all_harmonic_budgets_exact(self):
        for d in (2,3,4,6):
            for h in (1,2,7,29):
                for k in (1,3,7):
                    p=d+1
                    B=l.per_lag_phase_budget(k,h,d)
                    # Check direct mathematical rational envelope constant
                    c=l.fractional_ceil_root(F(22*abs(h),7)*l.moment(d)*16**k,p)
                    self.assertEqual(B,F(2*p,p-1)*c)

    def test_aggregate_budget_positive_and_clock(self):
        for n in (64,256,1024,4096):
            for d in (2,3,4):
                K=l.corrected_clock(n,d)
                self.assertLessEqual(16**K,n**(d+1))
                E=l.aggregate_transport_budget(n,K,1,d)
                self.assertGreaterEqual(E,0)
                self.assertLess(E,1)

    def test_clock_order_hierarchy(self):
        n=4096
        self.assertEqual([l.corrected_clock(n,d) for d in (2,3,4,5)], [9,12,15,18])

    def test_phase_budget_versus_finite_actual_differences(self):
        # Float complex phase is a diagnostic ONLY; proof is the exact
        # source residual plus analytic chord clipping above.
        for d in (2,3):
            for N,k,h in ((96,2,1),(128,4,3),(256,5,1)):
                x=F(0); states=[]
                for n in range(1,N+1):
                    x=16*x+l.direct_r(n)
                    states.append(x)
                actual=0j;corrected=0j
                for n in range(1,N-k+1):
                    u=states[n-1]
                    a=(F((16**k-1))*u+l.true_source_lag(n,k))%1
                    b=(F((16**k-1))*u+l.corrected_lag(n,k,d))%1
                    actual+=complex(math.cos(2*math.pi*h*float(a)),math.sin(2*math.pi*h*float(a)))
                    corrected+=complex(math.cos(2*math.pi*h*float(b)),math.sin(2*math.pi*h*float(b)))
                self.assertLessEqual(abs(actual-corrected),float(l.per_lag_phase_budget(k,h,d))+1e-9)

    def test_special_doubled_clock_bulk_profile(self):
        # N=4**m gives 16**K=N**2 exactly at the source-phase critical clock.
        for m in (4,5,6):
            n=4**m//2
            k=m
            leading,actual,bound=l.first_positive_curvature_bound(n,k)
            self.assertEqual(leading,F(16**k-1,64*n*n))
            self.assertLess(abs(actual-F(1,16)),bound+F(1,64*n*n))
            self.assertLess(abs(actual-F(1,16)),F(16**k,30*n**3)+F(1,64*n*n))

    def test_source_mutation_invalidates_phase_envelope(self):
        # Deliberate after-source additive mutant r'(m)=r(m)+1/m^2.
        # It does NOT keep original four poles. Original-source normal-form
        # error must FAIL rather than claiming a uniform arbitrary-source theorem.
        n,k=128,4
        actual=l.true_source_lag(n,k)
        mutated=actual+sum((F(16**(k-j),(n+j)**2) for j in range(1,k+1)),F(0))
        self.assertGreater(abs(mutated-l.corrected_lag(n,k,2)),l.residual_bound(n,k,2))

    def test_order_two_cubic_root_transport_and_order_three_quartic(self):
        for N in (256,4096,16384):
            # Exact integer clocks; the source error is O(1/K^2) at
            # a longer log-depth than Main XVIII's uncorrected order.
            K3=l.corrected_clock(N,2)
            K4=l.corrected_clock(N,3)
            self.assertLess(K3,K4)
            self.assertLess(l.aggregate_transport_budget(N,K3,1,2),F(1))
            self.assertLess(l.aggregate_transport_budget(N,K4,1,3),F(1))

    def test_predeclared_hostile_laurent_holdouts(self):
        # Fresh noncalibration points, integer-only source oracle (not floats).
        for n,k in ((131,17),(257,25),(503,31)):
            exact=l.true_source_lag(n,k)
            for d in (2,3,4,6):
                self.assertLess(abs(exact-l.corrected_lag(n,k,d)),l.residual_bound(n,k,d))

    def test_wrong_lag_inputs(self):
        for test in [lambda:l.original_r(0),lambda:l.true_source_lag(1,0),
                     lambda:l.corrected_lag(1,3,1),lambda:l.moment(-1),
                     lambda:l.aggregate_transport_budget(10,11,1,3),
                     lambda:l.corrected_clock(0,2),lambda:l.per_lag_phase_budget(2,0,3)]:
            with self.assertRaises(ValueError):test()

if __name__=='__main__':unittest.main()
