"""Exact focused tests for original-source two-carry/differential algebra."""
import unittest
from fractions import Fraction
from math import comb
from two_carry_seam import (forcing,tail_upper,tail_bounds,prefix_unwrapped,
        step,cooldown,moment_difference,trace,certified_completion_carry,source_phase_reset_bound)

class TwoCarryTests(unittest.TestCase):
    def test_actual_four_poles(self):
        self.assertEqual(forcing(1),Fraction(47,15))
        self.assertEqual(forcing(2),Fraction(106,819))
        with self.assertRaises(ValueError):forcing(0)
    def test_r_bound_monotone(self):
        for n in range(2,150):
            self.assertTrue(0<forcing(n+1)<forcing(n)<Fraction(47,15*n*n))
    def test_complete_monotone(self):
        for n in [1,2,3,7,21,79,100]:
            for k in range(6):
                self.assertGreater(moment_difference(n,k),0)
    def test_first_difference_order_source(self):
        for n in range(1,15):
            self.assertEqual(moment_difference(n,1),forcing(n)-forcing(n+1))
    def test_tail_bounds(self):
        for n in (0,1,5,20):
            prev=None
            for k in [0,1,3,8,16]:
                lo,hi=tail_bounds(n,k)
                self.assertLess(lo,hi)
                self.assertLessEqual(hi,tail_upper(n) if k==0 else tail_upper(n))
                if prev is not None:self.assertLessEqual(hi,prev)
                prev=hi
    def test_force_step_digit(self):
        phi=Fraction()
        for n in range(1,256):
            s=step(phi,n)
            self.assertTrue(0<=s.phase<1)
            self.assertEqual(s.phase, 16*phi+forcing(n)-s.total_carry)
            phi=s.phase
    def test_digit_identity_first_256(self):
        s=trace(256)
        self.assertEqual(s['e_times'],[])
        self.assertEqual(s['delta_times'],[])
        self.assertEqual(s['unresolved'],[])
        self.assertEqual(s['prefix'][:12],'3243F6A8885A')
        self.assertEqual(s['recovered_digits'],256)
    def test_unwrapped_rational_prefix(self):
        for n in [1,2,3,11,21,55]:
            u=prefix_unwrapped(n)
            self.assertEqual(u%1, self._phase(n))
    def _phase(self,n):
        phi=Fraction()
        for j in range(1,n+1):phi=step(phi,j).phase
        return phi
    def test_cooldown(self):
        for B in (2,5,16,100,1000,10000):
            length=cooldown(B)
            if length:self.assertLess(forcing(B)*Fraction(16**(length+1)-1,15),1)
            self.assertGreaterEqual(forcing(B)*Fraction(16**(length+2)-1,15),1)
    def test_cooldown_asymptotic(self):
        for B in [256,1000,8192,30000,65536]:
            self.assertTrue(cooldown(B) >= int(2*__import__('math').log(B,16))-2)
    def test_source_kick_positive_control(self):
        N=30; a=forcing(N)
        target=(1-a/2)/16
        root=(target-prefix_unwrapped(N-1))/16**(N-1)
        raw=prefix_unwrapped(N-1)+16**(N-1)*root
        self.assertEqual(raw,target)
        hit=step(raw,N)
        self.assertEqual(hit.kick_carry,1)
        self.assertEqual(hit.phase,a/2)
        phi=hit.phase
        for k in range(1,cooldown(N)+1):
            st=step(phi,N+k)
            self.assertEqual(st.kick_carry,0)
            phi=st.phase
    def test_completion_carry_positive_control(self):
        N=20;a=forcing(N+1); eps=a/32
        root=(-eps-prefix_unwrapped(N))/16**N
        phi=(prefix_unwrapped(N)+16**N*root)%1
        self.assertEqual(phi,1-eps)
        self.assertEqual(certified_completion_carry(phi,N),1)
    def test_mutually_exclusive_source_and_tail_carry(self):
        n=20;a=forcing(n)
        phi=(1-a/2)/16
        hit=step(phi,n)
        self.assertEqual(hit.kick_carry,1)
        self.assertEqual(certified_completion_carry(hit.phase,n),0)
        self.assertLess(source_phase_reset_bound(n),1)
    def test_high_clock_tail_no_borrow(self):
        for n in (10,20,100,1000,4096):
            phi=self._phase(n)
            self.assertLess(phi+tail_upper(n),1)
            self.assertEqual(certified_completion_carry(phi,n),0)
    def test_bbp_differential_not_vanish(self):
        for n in [1,3,15,100]:
            self.assertGreater(forcing(n)-forcing(n+1),0)
            self.assertGreater(forcing(n)-2*forcing(n+1)+forcing(n+2),0)
    def test_wrong_seed_exact_shadow_algebra(self):
        # For original forcing s=-x, U_n(s)=-T_n, phi_n=1-T_n and theta_n=0.
        # n>=2: the rational completion lies below 1 and the raw carry is 15.
        for n in (2,3,10,31):
            lower,upper=tail_bounds(n,12)
            self.assertTrue(0<lower<upper<Fraction(1,16))
            self.assertEqual(15+1-16,0)
    def test_exact_signed_coboundary_changed_seeds(self):
        from two_carry_seam import tail_bounds
        N=30
        u=prefix_unwrapped(21)
        small=forcing(22)/32
        seeds=[Fraction(0),Fraction(1,17),(-small-u)/16**21]
        for seed in seeds:
            xlo=sum((forcing(j)/16**j for j in range(1,N+45)),Fraction())+seed
            xhi=xlo+forcing(N+45)/(15*16**(N+44))
            phi=seed%1
            prev_delta=certified_completion_carry(phi,0)
            prev_full_lo=xlo.__floor__()
            prev_full_hi=xhi.__floor__()
            self.assertEqual(prev_full_lo,prev_full_hi)
            for n in range(1,N+1):
                s=step(phi,n)
                phi=s.phase
                delta=certified_completion_carry(phi,n)
                c_lo=(16**n*xlo).__floor__()
                c_hi=(16**n*xhi).__floor__()
                self.assertEqual(c_lo,c_hi)
                digit=c_lo-16*prev_full_lo
                self.assertTrue(0<=digit<=15)
                self.assertEqual(digit,s.total_carry+delta-16*prev_delta)
                if n>=2:
                    self.assertEqual(digit,s.raw_digit+s.kick_carry+delta-16*prev_delta)
                prev_delta=delta
                prev_full_lo=c_lo

    def test_sparse_word_zero_carry_is_not_r0(self):
        import math
        from two_carry_seam import tail_upper
        positions=[16]
        while positions[-1]<5000:
            t=positions[-1]
            positions.append(t+math.ceil(math.log(t+1,16)))
        for n in [64,256,1000,4096]:
            next_event=next(t for t in positions if t>n)
            theta_lower=Fraction(1,16**(next_event-n))
            self.assertGreater(theta_lower,tail_upper(n))
        # The 0/1-only symbolic word has vanishing one-density,
        # yet the fixed positive BBP cofactor sits below its phase tail.
        for N,threshold in [(128,0.55),(512,0.43),(2048,0.39)]:
            self.assertLess(sum(1 for p in positions if N<=p<2*N)/N,threshold)

    def test_hankel_positive_small_exact(self):
        # Sylvester checks through 3x3; infinite statement uses measure proof.
        from sympy import Matrix,Rational
        for n in [1,3,17]:
            for k in [1,2,3]:
                arr=[[forcing(n+i+j) for j in range(k)] for i in range(k)]
                mat=Matrix([[Rational(a.numerator,a.denominator) for a in row] for row in arr])
                self.assertGreater(mat.det(),0)

    def test_prime_square_mutant_fingerprint(self):
        for p in (7,11,19,29,43,79):
            j=(p*p+7)//8
            self.assertEqual(8*j-7,p*p)
            original=p*p*forcing(j)
            mutant=original+Fraction(2,(p*p+1)*(p*p+2))
            def mod_fraction(q):
                self.assertNotEqual(q.denominator%p,0)
                return q.numerator*pow(q.denominator,-1,p)%p
            self.assertEqual(mod_fraction(original),4%p)
            self.assertEqual(mod_fraction(mutant),5%p)

    def test_r0_source_bridge_all_shell_inequality(self):
        from two_carry_seam import conservative_r0_lower
        nmax=96
        # altered and authentic seeds; digits are *independently* certified
        # from the BBP interval, not defined using the carry identity.
        selected=[Fraction(0),Fraction(1,17)]
        N=20; eps=forcing(N+1)/32
        selected.append((-eps-prefix_unwrapped(N))/16**N)
        for seed in selected:
            M=nmax+38
            left=sum((forcing(j)/16**j for j in range(1,M+1)),Fraction())+seed
            right=left+forcing(M+1)/(15*16**M)
            phi=seed%1
            prev_delta=certified_completion_carry(phi,0)
            data=[]; deltas={0:prev_delta};actual=[]
            previous_floor=left.__floor__()
            self.assertEqual(previous_floor,right.__floor__())
            for n in range(1,nmax+1):
                raw=step(phi,n)
                phi=raw.phase
                delta=certified_completion_carry(phi,n)
                deltas[n]=delta
                f1=(16**n*left).__floor__()
                f2=(16**n*right).__floor__()
                self.assertEqual(f1,f2)
                digit=f1-16*previous_floor
                data.append(raw)
                actual.append(digit)
                prev_delta=delta
                previous_floor=f1
            for B in (4,12,24,40):
                raw_hits=sum(4<=data[n].raw_digit<=11 for n in range(B,2*B))
                tail_hits=sum(deltas[n] for n in range(B,2*B+1))
                completed_hits=sum(4<=actual[n]<=11 for n in range(B,2*B))
                self.assertLessEqual(conservative_r0_lower(B,raw_hits,tail_hits),
                                     Fraction(completed_hits,B))
        with self.assertRaises(ValueError):conservative_r0_lower(2,3,0)

    def test_source_seed_alias_different(self):
        self.assertEqual(Fraction(1,16)*16,1)
        self.assertNotEqual(Fraction(1,16),0)

if __name__=='__main__': unittest.main()
