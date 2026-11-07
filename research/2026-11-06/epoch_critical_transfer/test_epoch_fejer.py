from __future__ import annotations
import unittest
from fractions import Fraction
from all_radius import max_all_radius_ratio
from epoch_fejer import (original_r,combined_r,circle_states,tail_interval,
                         mean_tail_upper,hilbert_transport_bound,weight_square_sum,
                         fourier_energy,epoch_pair_count,window_epoch)

class EpochFejer(unittest.TestCase):
    def test_original_source_contract(self):
        for n in list(range(1,257))+[1023,2049]:
            self.assertEqual(original_r(n),combined_r(n))
    def test_harmonic_square_weight_identity(self):
        for H in range(1,129):
            self.assertEqual(weight_square_sum(H),Fraction(H*(H+1)*(H+2),6))
    def test_averaged_tail_bound(self):
        for A in [1,2,3,5,16,32,64,128,256]:
            self.assertLess(mean_tail_upper(A),Fraction(1,30*A*A))
    def test_tail_positive_and_numerators(self):
        for n in [1,3,17,64,127,256]:
            lo,hi=tail_interval(n,16)
            self.assertLess(Fraction(0),lo)
            self.assertLess(lo,hi)
            self.assertLess(hi,Fraction(1,15*(n+1)**2))
    def test_epoch_transport_float_diagnostic(self):
        for A in [16,32,64,128,256]:
            d=window_epoch(A)
            self.assertTrue(d['pass_float_check'],repr(d))
            self.assertLess(d['rigorous_upper'],0.025)
    def test_critical_transport_decreases(self):
        prev=1.0
        for A in [16,32,64,128,256]:
            d=hilbert_transport_bound(A,A)
            self.assertLess(d,prev)
            prev=d
    def test_exact_pair_counts_original(self):
        for A in [16,32,64,128]:
            st=circle_states(2*A)[A:]
            self.assertLessEqual(epoch_pair_count(st,Fraction(1,A+1)),A+3*A*A*Fraction(1,A+1))
            self.assertEqual(epoch_pair_count(st,Fraction(1,2)),A*A)
    def test_nonnormal_controls_fail_uniform_critical_energy(self):
        A=32
        const=tuple(Fraction(1,5) for _ in range(A))
        shadow=tuple(Fraction(n,(2*n-1)**4) for n in range(A,2*A))
        self.assertAlmostEqual(fourier_energy(const,A),A+1,places=9)
        self.assertGreater(fourier_energy(shadow,A),A)
    def test_exact_all_radius_small_calibration(self):
        for A in [16,32,64]:
            self.assertTrue(max_all_radius_ratio(A)["all_radius_bound_K3"])
    def test_split_prime_window_against_current_original_source(self):
        def isprime(q): return q > 1 and all(q%d for d in range(2,int(q**.5)+1))
        for n in [17,32,64,97]:
            den=circle_states(n+1)[n].denominator
            for p in range(n+1,4*n+1):
                if isprime(p): self.assertEqual(den%p,0,(n,p))
    def test_shadow_failure_critical_collision(self):
        for A in [16,64,191,319]:
            H_A=Fraction(A,(2*A-1)**4)
            self.assertLess(H_A,Fraction(1,A+1))
            self.assertGreater(A*A,A+3*Fraction(A*A,A+1))
    def test_non_haar_geometric_grid_is_not_an_expanding_orbit(self):
        # Shows why Fejer boundedness without the x16 frequency ray is insufficient.
        for A in [16,64,128]:
            grid=tuple(Fraction(2*i+1,4*A) for i in range(A))
            self.assertLess(fourier_energy(grid,A),3.0)
            self.assertTrue(all(p<Fraction(1,2) for p in grid))
    def test_clock_endpoint_source_identity(self):
        x=circle_states(130)
        for n in [16,64,120]:
            zprev=(x[n-1]+tail_interval(n-1,20)[0])%1
            znow=(x[n]+tail_interval(n,20)[0])%1
            q=(16*zprev-znow)%1
            self.assertEqual(q,(-Fraction(1,16**20)*original_r(n+20))%1)
    def test_epoch_ray_with_direct_completed_diagnostics(self):
        A=32
        x=circle_states(2*A+1)
        z=[(x[n]+sum((Fraction(1,16**j)*original_r(n+j) for j in range(1,21)),Fraction(0)))%1 for n in range(A,2*A+1)]
        for h in [1,2,3,4]:
            import cmath,math
            L=sum(cmath.exp(2j*math.pi*h*float(v)) for v in z[:-1])/A
            R=sum(cmath.exp(2j*math.pi*16*h*float(v)) for v in z[:-1])/A
            self.assertLessEqual(abs(L-R),2/A+1e-10)
if __name__=='__main__': unittest.main()
