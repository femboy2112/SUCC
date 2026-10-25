"""Independent exact source/cyclotomic/vdC adversarial controls."""
import itertools
import unittest
from fractions import Fraction as Q
from math import gcd, lcm

from observational_succ.pi_succ_lag_bridge import (
    forcing_upper_remainder, lag_source, lag_positive_upper,
    lag_window_upper, lag_window_geometric_upper,
    source_circle_prefix, exact_lag_phase_defect, multiplicative_order_16,
    clock_blind_lag, special_clock_valuation, resonance_frequency,
    gaussian_vdc_certificate, fourier_log_schedule,
    fourier_lag_rational_upper,
)
from observational_succ.bbp_natural_carrier import exact_forcing


class SourceLagBridgeTests(unittest.TestCase):
    def test_original_four_pole_and_sharp_cubic(self):
        for j in range(2,100):
            t=j-2
            self.assertEqual(forcing_upper_remainder(j),
                5696*t**3+24760*t**2+35342*t+16503)
            self.assertLess(exact_forcing(j),Q(15,64*(j-1)**2))

    def test_exact_signed_lag_identity_not_independent_product(self):
        phases=source_circle_prefix(35)
        for n in range(1,17):
            for k in range(1,11):
                self.assertEqual(exact_lag_phase_defect(phases,n,k),0)

    def test_original_source_lag_bounds_many_histories(self):
        for n in range(1,40):
            for k in range(1,12):
                r=lag_source(n,k)
                self.assertTrue(0<r<lag_positive_upper(n,k),(n,k))

    def test_lag_upper_asymptotically_optimal(self):
        for k in (1,2,4,6):
            x=lag_source(500,k)/lag_positive_upper(500,k)
            self.assertTrue(Q(96,100)<x<1,(k,x))

    def test_window_lag_bounds_independent_of_window_length(self):
        for start in (2,3,11,31):
            for size in (0,1,7,17):
                for k in (1,2,4):
                    actual=sum((lag_source(n,k) for n in range(start,start+size)),Q())
                    self.assertTrue(actual<lag_window_upper(start,size,k) if size else actual==0)
                    self.assertLess(lag_window_upper(start,size,k),lag_window_geometric_upper(start,k))
                    self.assertGreaterEqual(fourier_lag_rational_upper(2,start,size,k),0)

    def test_orders_and_LTE_against_direct_integer_factorization(self):
        for p in (3,5,7,13):
            for k in range(1,84):
                a=16**k-1
                v=0
                while a%p==0:
                    v+=1; a//=p
                self.assertEqual(special_clock_valuation(p,k),v,(p,k))
        for p in (3,5,7,13,17,19):
            for depth in (1,2,3):
                if p**depth>1400:continue
                k=multiplicative_order_16(p,depth)
                self.assertEqual(pow(16,k,p**depth),1)
                for j in range(1,k):
                    self.assertNotEqual(pow(16,j,p**depth),1)

    def test_simultaneous_prime_blindness_cost(self):
        self.assertEqual(clock_blind_lag(((3,1),(5,1),(7,1),(13,1))),3)
        self.assertEqual(clock_blind_lag(((3,2),(5,2),(7,2),(13,2))),1365)
        for p,depth in ((3,2),(5,2),(7,2),(13,2)):
            self.assertEqual((16**1365-1)%(p**depth),0)
        # Explicit shared order-3 clock: it erases at least one place from p=7 AND 13.
        for k in (1,2,4,5,7,8):
            self.assertEqual((16**k-1)%7==0,False)
            self.assertEqual((16**k-1)%13==0,False)

    def test_prime_Blindness_not_full_source_blindness(self):
        k=clock_blind_lag(((3,1),(5,1),(7,1),(13,1)))
        assert k==3
        phase=Q(1,7**2)
        self.assertNotEqual((16**k-1)*phase%1,0)
        self.assertEqual((16**k-1)*Q(1,7)%1,0)

    def test_rational_resonance_refutes_uniform_all_h(self):
        phases=source_circle_prefix(30)
        for N in (3,7,15,29):
            L=resonance_frequency(phases[:N])
            self.assertTrue(L>1)
            self.assertTrue(all((L*p).denominator==1 for p in phases[:N]))
            self.assertEqual(resonance_frequency(phases[:N]+(Q(0),)),L)

    def test_vdc_exact_all_fourth_roots(self):
        roots=((1,0),(-1,0),(0,1),(0,-1))
        for n in range(2,7):
            for steps in itertools.product(roots,repeat=n):
                for H in (1,2,n):
                    lhs,rhs=gaussian_vdc_certificate(steps,H)
                    self.assertLessEqual(lhs,rhs,(steps,H))

    def test_vdc_rejects_inert_false_saving(self):
        all_one=((1,0),)*13
        for H in (2,3,7):
            lhs,rhs=gaussian_vdc_certificate(all_one,H)
            self.assertEqual(lhs,13**2)
            self.assertTrue(rhs>=lhs)

    def test_explicit_schedule_and_domain_controls(self):
        for j in range(1,8):
            N=16**(2*j)
            self.assertEqual(fourier_log_schedule(N),j)
            self.assertLessEqual(16**fourier_log_schedule(N),N**0.5)
        for fn,args in (
            (lag_source,(0,1)),(lag_source,(1,0)),
            (multiplicative_order_16,(2,1)),(clock_blind_lag,(((3,1),(3,2)),)),
            (gaussian_vdc_certificate,(((1,0),),2)),
            (resonance_frequency,((Q(1,3),1),)),
        ):
            with self.assertRaises((ValueError,TypeError)):
                fn(*args)

if __name__=='__main__': unittest.main()
