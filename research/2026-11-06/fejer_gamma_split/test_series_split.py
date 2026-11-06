"""Focused preregistered SUCC tests; no asymptotic normality inference."""
import unittest
import math
import cmath
from fractions import Fraction

from series_split import (
 original_forcing,exact_original_states,shadow_states,phases,completed_beta_one_fifth,
 direct_energy,global_mean,spectral_energy,independent_split_energy,
 martingale_budget,triad_budget,fejer_energy,normalized_lag,
 original_lag_phase,tails,completed_phases,half_gamma_series_partial,
 harmonic_series_partial,Abel_prefix_coefficient,proxy_quadrant_example)


def close(a,b,tol=2e-11):
    if abs(a-b)>tol:
        raise AssertionError(f"{a!r} != {b!r}, error={abs(a-b)!r}")

class ReturnEnergyTests(unittest.TestCase):
    def test_source_first_terms_exact(self):
        for n in (1,2,7,11,23,47):
            a=120*n*n-89*n+16
            d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
            self.assertEqual(original_forcing(n),Fraction(a,d))

    def test_original_unwrapped_fractional_recursion(self):
        states=exact_original_states(62)
        self.assertEqual(states[0],0)
        for n in range(1,len(states)):
            self.assertEqual(states[n],(16*states[n-1]+original_forcing(n))%1)

    def test_gaussian_q_split_harmonic_m_split(self):
        for Q in (1,2,4,8,16):
            for M in (1,2,3,5,7):
                for J in (1,2,4,8,20):
                    root=half_gamma_series_partial(Q,J)
                    self.assertAlmostEqual(root+1/math.sqrt(Q+J),1/math.sqrt(Q),places=14)
                    source=harmonic_series_partial(M,J)
                    self.assertEqual(source+Fraction(1,M+J),Fraction(1,M))
                # Each limit is normed; this also compares the scalar amplitude split.
                self.assertAlmostEqual((1/math.sqrt(Q))**2*(1/M)**2,1/(Q*M*M),places=14)

    def test_spectral_parseval_original(self):
        for Q,M,h in ((4,5,1),(8,6,1),(16,5,2)):
            z=phases(exact_original_states(Q*M),h)
            close(direct_energy(z,Q),spectral_energy(z,Q))

    def test_martingale_original(self):
        for k,M,h in ((2,5,1),(3,6,1),(4,5,2)):
            Q=1<<k;z=phases(exact_original_states(Q*M),h)
            c,inc,levels=martingale_budget(z,k)
            self.assertEqual(len(inc),k)
            close(levels[0],c)
            close(levels[-1],direct_energy(z,Q))
            close(c+sum(inc),levels[-1])
            for x,y in zip(levels,levels[1:]):
                self.assertGreaterEqual(y+1e-12,x)
            for x in inc:
                self.assertGreaterEqual(x,-1e-12)

    def test_triad_budget_original(self):
        for Q,M,h in ((4,5,1),(8,6,1),(16,5,2)):
            z=phases(exact_original_states(Q*M),h)
            p,b,w=triad_budget(z,Q)
            close(p+b+w,1)
            close(p+b,direct_energy(z,Q))
            self.assertGreaterEqual(min(p,b,w),-1e-12)

    def test_fejer_original(self):
        for Q,M,h in ((4,5,1),(8,6,1),(16,5,2)):
            z=phases(exact_original_states(Q*M),h)
            close(fejer_energy(z,Q),direct_energy(z,Q))
            c=1/M+sum(2*(M-d)/M**2*normalized_lag(z,Q,d).real for d in range(1,M))
            close(c,direct_energy(z,Q))

    def test_lag_original_forcing_identical_phase(self):
        for Q,M,h in ((4,5,1),(8,6,1),(16,5,2)):
            z=phases(exact_original_states(Q*M),h)
            for d in range(1,M):
                for n in (0,1,Q*(M-d)-1):
                    lhs=z[n+d*Q]*z[n].conjugate()
                    rhs=original_lag_phase(n,d*Q,h)
                    close(lhs,rhs)

    def test_absolutely_convergent_generating_series_coefficient(self):
        z=phases(exact_original_states(24),1)
        for Q in (2,4,8):
            M=len(z)//Q
            for a in range(Q):
                values=z[a::Q]
                close(Abel_prefix_coefficient(values,M),sum(values)/M)

    def test_coherent_constant_negative_control(self):
        for Q,M in ((2,8),(8,3),(16,5)):
            z=[1+0j]*(Q*M)
            close(direct_energy(z,Q),1)
            close(abs(global_mean(z))**2,1)
            p,b,w=triad_budget(z,Q)
            close((p,b,w),(1,0,0)) if False else close(p,1)
            close(b,0);close(w,0)

    def test_unbalanced_residue_ghost_w0_r1(self):
        for Q,M in ((2,7),(4,5),(8,6),(16,5)):
            z=[(-1)**n+0j for n in range(Q*M)]
            close(abs(global_mean(z))**2,0)
            close(direct_energy(z,Q),1)
            close(spectral_energy(z,Q),1)
            b=triad_budget(z,Q)
            close(b[0],0);close(b[1],1);close(b[2],0)

    def test_periodic_quadrant_same_gap(self):
        for Q,M in ((4,5),(8,6),(16,5)):
            R,W=proxy_quadrant_example(Q,M)
            close(R,1);close(W,0)

    def test_beta_one_fifth_negative_control(self):
        for Q,M in ((4,5),(8,6),(16,5)):
            z=completed_beta_one_fifth(Q*M,h=1)
            close(direct_energy(z,Q),1)
            close(abs(global_mean(z))**2,1)

    def test_real_nonnormal_shadow_control(self):
        Q,M=8,40
        z=phases(shadow_states(Q*M),1)
        R=direct_energy(z,Q)
        self.assertGreater(R,0.90)
        close(R,spectral_energy(z,Q))
        close(R,fejer_energy(z,Q))

    def test_finer_census_never_decreases_energy(self):
        z=phases(exact_original_states(64),1)
        levels=[direct_energy(z,1<<j) for j in range(7)]
        for x,y in zip(levels,levels[1:]):
            self.assertGreaterEqual(y+1e-12,x)
        close(levels[0],abs(global_mean(z))**2)
        close(levels[-1],1)

    def test_raw_completed_rigorous_tail_enclosure(self):
        for n in (0,1,11,73):
            lo,hi=tails(n,40)
            self.assertLess(hi-lo,Fraction(1,2**110))
            self.assertLess(lo,hi)
        zz=completed_phases(20,1,depth=40)
        z=phases(exact_original_states(20),1)
        self.assertLess(abs(direct_energy(zz,4)-direct_energy(z,4)),0.03)

    def test_completed_lag_selected_high_frequency_exact(self):
        # Derive beta=T_0 from a rational source interval, never from float pi.
        Q,M,h=4,5,1;N=Q*M;L=(M-1)*Q
        z=completed_phases(N,h,depth=65)
        blo,bhi=tails(0,N+35)
        beta=(blo+bhi)/2
        for d in range(1,M):
            ell=d*Q
            values=[]
            for n in range(Q*(M-d)):
                v=(h*(16**ell-1)*16**n*beta)%1
                values.append(cmath.exp(2j*math.pi*float(v)))
            rhs=sum(values)/len(values)
            lhs=normalized_lag(z,Q,d)
            close(lhs,rhs,5e-11)

if __name__=='__main__':
    unittest.main()

class ExtendedSourceAndSeriesTests(unittest.TestCase):
    def test_gamma_harmonic_fake_contraction_on_constant(self):
        from series_split import gamma_harmonic_truncation_factor
        # Fully coherent original R=1, but partial series counterfeit 0 at growing Q,M.
        c1=gamma_harmonic_truncation_factor(32,64,20,20)
        c2=gamma_harmonic_truncation_factor(1024,2048,20,20)
        self.assertGreater(c1,c2)
        self.assertLess(c2,1e-7)
        self.assertAlmostEqual(gamma_harmonic_truncation_factor(8,9,10**12,10**12),1,places=4)

    def test_gluing_projector_original_and_ghost(self):
        from series_split import gluing_projector_energy
        for Q,M,h in ((4,5,1),(8,6,1),(16,5,2)):
            z=phases(exact_original_states(Q*M),h)
            close(direct_energy(z,Q),gluing_projector_energy(z,Q))
        Q=8;M=6
        zz=[(-1)**n+0j for n in range(Q*M)]
        close(gluing_projector_energy(zz,Q),1)
        close(independent_split_energy(zz,Q),0)

    def test_original_p149_local_rephase_but_real_separation(self):
        from series_split import original_forcing
        p=149;n=19;L=37
        self.assertEqual(pow(16,L,p),1)
        self.assertEqual(original_forcing(n).denominator%p,0)
        self.assertTrue(all(original_forcing(j).denominator%p for j in range(n+1,n+L+1)))
        states=exact_original_states(n+L+1)
        a,b=states[n],states[n+L]
        self.assertEqual(a.denominator%p,0)
        self.assertEqual(b.denominator%p,0)
        self.assertNotEqual((b-a).denominator%p,0)
        distance=min((b-a)%1, (a-b)%1)
        self.assertGreater(distance,Fraction(45,100))
        self.assertLess(distance,Fraction(46,100))

    def test_original_257_dyadic_prime_local_rephase(self):
        from series_split import original_forcing
        p=257;n=33;L=4
        self.assertEqual(pow(16,L,p),1)
        self.assertNotEqual(pow(16,L//2,p),1)
        self.assertEqual(original_forcing(n).denominator%p,0)
        self.assertTrue(all(original_forcing(j).denominator%p for j in range(n+1,n+L+1)))
        z=exact_original_states(n+L+1)
        self.assertEqual(z[n].denominator%p,0)
        self.assertEqual(z[n+L].denominator%p,0)
        self.assertNotEqual((z[n+L]-z[n]).denominator%p,0)
        dist=min((z[n+L]-z[n])%1,(z[n]-z[n+L])%1)
        self.assertGreater(dist,Fraction(42,100))
        self.assertLess(dist,Fraction(43,100))
