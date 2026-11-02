"""Research-only exact tests for a NEW selected source prime-window theorem.

This is NOT the full SUCC suite, a Lean proof, or pi normality.
"""
from __future__ import annotations

import cmath
import importlib.util
import math
from fractions import Fraction as F
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT/'research/2026-11-01/selected_prime_phase'

def load(name):
    spec=importlib.util.spec_from_file_location(name,RESEARCH/(name+'.py'))
    import sys
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

m=load('prime_phase');o=load('independent_oracle')

class ExactSourcePrimePhase(unittest.TestCase):
    def test_original_four_poles_and_combined_source(self):
        for j in range(1,125):self.assertEqual(m.source(j),o.r_combined(j))
        self.assertEqual(m.source(1),F(47,15))
        self.assertEqual(m.source(2),F(106,819))

    def test_convolution_independent_oracle(self):
        for N in range(0,55):self.assertEqual(m.state(N),o.u_convolution(N))
        self.assertEqual(m.state(3),F(615863723,765765))

    def test_birth_and_first_reuse(self):
        expected=((13,2,-1,7),(17,3,4,9),(29,4,-1,15),
                  (37,5,-1,19),(41,6,4,21),(53,7,-1,27))
        for p,n,c,j0 in expected:
            b=m.birth(p)
            self.assertEqual((b.n,b.coefficient,b.first_reuse),(n,c,j0))
            self.assertEqual(b.length,j0-n)

    def test_birth_invalid(self):
        for p in [2,3,5,7,9,11,19,23,31,49]:
            with self.assertRaises(ValueError):m.birth(p)

    def test_persistence_windows_full_rational_replay(self):
        for p in m.primes_upto(241):
            if p<=5 or p%8 not in (1,5):continue
            b=m.birth(p)
            for j in range(b.n,b.first_reuse):
                self.assertEqual(m.persistent_residue(p,j),
                                 (b.coefficient*pow(16,j-b.n,p))%p)

    def test_all_horizon_large_primes_exact(self):
        for N in range(1,101):
            u=m.state(N)
            ps=m.horizon_primes(N)
            self.assertEqual(ps,o.positive_integer_poles_for_n(N))
            for p in ps:
                b=m.birth(p)
                self.assertTrue(b.n<=N<b.first_reuse)
                self.assertEqual(m.p_residue_of_state(u,p),
                                 b.coefficient*pow(16,N-b.n,p)%p)
                self.assertTrue(o.verify_horizon(N,p))

    def test_product_divides_reduced_denominator_once(self):
        for N in [2,3,4,5,8,16,32,64,100]:
            u=m.state(N)
            P=math.prod(m.horizon_primes(N))
            self.assertEqual(u.denominator%P,0)
            self.assertEqual(math.gcd(u.denominator//P,P),1)
            self.assertEqual(math.gcd(u.numerator,P),1)

    def test_primary_phase_cofactor_n3(self):
        u=m.state(3)
        v,ps=m.phase_split(u,[13,17])
        self.assertEqual(ps,((13,10),(17,4)))
        self.assertEqual(v,F(2783233,3465))
        self.assertEqual(m.trace_factor(ps,1),F(1,192))
        self.assertEqual(m.trace_factor(ps,13),-F(1,16))
        self.assertEqual(m.trace_factor(ps,13*17),F(1))

    def test_source_whole_prime_cofactor_split(self):
        for N in [2,3,4,8,16,32,64,100]:
            u=m.state(N)
            ps=m.horizon_primes(N)
            v,parts=m.phase_split(u,ps)
            self.assertEqual(v+sum((F(a,p) for p,a in parts),F(0)),u)
            self.assertTrue(all(v.denominator%p for p in ps))
            if ps and 2*N>3:
                self.assertEqual(abs(m.trace_factor(parts,1)),
                                 F(1,math.prod(p-1 for p in ps)))

    def test_galois_trace_exponent_permutation(self):
        for p in [13,17,29,41,53,137]:
            for a in [1,2,p-1]:self.assertEqual(o.ramanujan_trace_sum(p,a),-1)

    def test_relative_trace_numeric_two_primes_diagnostic_only(self):
        u=m.state(3);v,parts=m.phase_split(u,[13,17]);phase=1+0j
        for p,a in parts:
            avg=sum(cmath.exp(2j*math.pi*a*k/p) for k in range(1,p))/(p-1)
            phase*=avg
        self.assertAlmostEqual(phase.real,1/192,places=12)
        self.assertAlmostEqual(phase.imag,0.,places=12)
        self.assertEqual(m.trace_factor(parts,1),F(1,192))

    def test_cofactor_spoof_exact(self):
        for p in [13,17,29,101,137,241]:
            b=m.birth(p)
            xs=[b.coefficient*pow(16,t,p)%p for t in range(min(30,b.length))]
            vs=m.spoof_cofactors(p,xs)
            q=math.isqrt(p)+1
            self.assertTrue(all(v.denominator%p for v in vs))
            self.assertTrue(all(abs(F(x,p)+v)<=F(1,2*q) for x,v in zip(xs,vs)))

    def test_counterfeit_all_prime_conductors_coherent(self):
        for N in [8,16,32,64,100]:
            ps=m.horizon_primes(N);P=math.prod(ps)
            self.assertGreater(P,1)
            # Completely coherent fake x_N=1/P_N (not original source).
            self.assertLess(F(44,7*P),F(1,10))
            self.assertEqual(abs(m.trace_factor(tuple((p,(P//p)**(-1)%p) for p in ps),1)),
                             F(1,math.prod(p-1 for p in ps)))

    def test_rational_seed_preserves_p_residues(self):
        for seed in [F(0),F(1,7),F(1,15),F(4,11)]:
            for p in [13,17,29,41,53]:
                b=m.birth(p)
                for j in [b.n,b.first_reuse-1]:
                    self.assertEqual(m.persistent_residue(p,j,seed),
                                     b.coefficient*pow(16,j-b.n,p)%p)

    def test_exact_rational_seed_15_phase_translation(self):
        for s in [F(1,15),F(7,15),F(-8,15)]:
            for n in range(0,48):
                self.assertEqual(((16**n-1)*s).denominator,1)
                self.assertEqual(m.state(n,s)-m.state(n),16**n*s)

    def test_source_mass_sharp_rational_envelope(self):
        part,upper=m.source_mass_certificate()
        self.assertGreater(part,F(0))
        self.assertLess(upper,F(65,256))
        self.assertGreater(upper,F(1,4))
        for h in [1,2,11,101]:
            self.assertEqual(m.ladder_uniform_error(5,h),
                             (F(2)+F(715,448)*h)/5)
        self.assertLess(F(715,448),F(165,56))

    def test_quarter_frame_switches_in_16_ladder(self):
        for h in [1,2,3,15,17,256,257,4096]:
            self.assertNotEqual(m.quarter_frame(h),m.quarter_frame(16*h))
            self.assertEqual(m.quarter_frame(h),m.quarter_frame(256*h))
        with self.assertRaises(ValueError):m.quarter_frame(0)

    def test_real_phase_ladder_and_reconstruction_numerical_diagnostic(self):
        for N in [4,12,24,48,80]:
            states=[m.state(n)%1 for n in range(1,N+1)]
            for h in [1,3,7,13,16,17,256]:
                z=sum(cmath.exp(2j*math.pi*h*float(q)) for q in states)/N
                w=sum(cmath.exp(2j*math.pi*16*h*float(q)) for q in states)/N
                bound=float(m.ladder_uniform_error(N,h))
                self.assertLessEqual(abs(w-z),bound+1e-9)
                if m.quarter_frame(h)==0:
                    bh=z.imag;b16=-w.real;reconstructed=complex(-b16,bh)
                else:
                    bh=-z.real;b16=w.imag;reconstructed=complex(-bh,b16)
                self.assertLessEqual(abs(z-reconstructed),bound+1e-9)
                self.assertLessEqual(abs(z),math.hypot(bh,b16)+bound+1e-9)

    def test_period_four_257_primary_nonmixing_exact_bound(self):
        b=m.birth(257)
        self.assertEqual((b.n,b.first_reuse,b.coefficient),(33,129,4))
        self.assertEqual(b.length,96)
        self.assertEqual(pow(16,2,257),256)
        self.assertEqual(pow(16,4,257),1)
        self.assertEqual([4*pow(16,t,257)%257 for t in range(4)],
                         [4,64,253,193])
        # Mean = (cos(8*pi/257)+cos(128*pi/257))/2.
        # cos(128*pi/257)>0, cos(8*pi/257)>1-(176/1799)^2/2.
        lower=(F(1)-F(176,1799)**2/F(2))/2
        self.assertGreater(lower,F(49,100))

    def test_multiplicative_Galois_Fourier_energy_numeric_diagnostic(self):
        for p in [13,17,29]:
            # Construct a generator g of (Z/p)^x with exact powers.
            g=next(t for t in range(2,p) if len({pow(t,j,p) for j in range(p-1)})==p-1)
            dlogs={pow(g,j,p):j for j in range(p-1)}
            for k in range(p-1):
                amp=sum(cmath.exp(2j*math.pi*a/p)*
                        cmath.exp(-2j*math.pi*k*dlogs[a]/(p-1))
                        for a in range(1,p))/(p-1)
                expected=F(1,(p-1)**2) if k==0 else F(p,(p-1)**2)
                self.assertAlmostEqual(abs(amp)**2,float(expected),places=10)
            self.assertEqual(F(1,(p-1)**2)+(p-2)*F(p,(p-1)**2),F(1))

    def test_shell_localized_sum_exact_sequence_partition(self):
        # Exact partition of a finite signed orbit, not a cancellation claim.
        for N in [48,64,128,256]:
            ps=[p for p in m.horizon_primes(N) if 2*N<p<3*N]
            self.assertTrue(ps)
            p=ps[0];b=m.birth(p)
            self.assertLess(b.n,F(3*N,8)+2)
            self.assertGreater(b.first_reuse,N)
            states=[m.state(j) for j in range(1,N+1)]
            prefix=sum((m.F(1) for _ in states[:b.n-1]),m.F(0))
            suffix=sum((m.F(1) for _ in states[b.n-1:]),m.F(0))
            self.assertEqual(prefix+suffix,m.F(N))
            for j in [b.n,N]:
                a=(b.coefficient*pow(16,j-b.n,p))%p
                v=states[j-1]-m.F(a,p)
                self.assertEqual((v+m.F(a,p)),states[j-1])
                self.assertNotEqual(v.denominator%p,0)

if __name__=='__main__': unittest.main()
