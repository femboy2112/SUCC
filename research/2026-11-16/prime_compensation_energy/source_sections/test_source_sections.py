import unittest
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import gcd
from source_sections import (
    Z_NEG1, forcing, orbit, state, floorq, ceilq,
    source_lift, forced_shift, observed_force, compensation, digit_carry,
    fiber_interval, forecast_carries, prime_pair, prime_uv, uv_from_pair,
    source_branch_section, signed_boost, projected_section_gap,
)

class SourceSectionsTest(unittest.TestCase):
    def test_negative_endpoint(self):
        for size in range(6):
            for ps in combinations([2,3,5,7,11],size):
                E,R=prime_pair(ps)
                self.assertEqual(E*R,Q(-1,12))
                self.assertEqual(R,Z_NEG1/E)

    def test_branch_parity_recovers_actual_source(self):
        for size in range(6):
            for ps in combinations([2,3,5,7,11],size):
                u,v,b=prime_uv(ps)
                self.assertEqual(u*u-v*v,Z_NEG1)
                self.assertEqual(source_branch_section(u,b),(u,v))
                self.assertEqual(1 if v>0 else -1,b)

    def test_prime_insertions_are_flat(self):
        for ps in [(),(2,),(3,5),(2,3,5)]:
            u,v,_=prime_uv(ps)
            for p,q in [(7,11),(13,17)]:
                self.assertEqual(signed_boost(*signed_boost(u,v,p),q),
                                 signed_boost(*signed_boost(u,v,q),p))

    def test_source_parity_closed_predictor(self):
        for ps in [(),(2,),(2,3),(3,5,7)]:
            for p in [11,13]:
                u,v,b=prime_uv(ps)
                self.assertEqual(source_branch_section(u,b),(u,v))
                u_next,v_next=signed_boost(*source_branch_section(u,b),p)
                self.assertEqual((u_next,v_next),prime_uv(ps+(p,))[:2])
                self.assertEqual(source_branch_section(u_next,-b),(u_next,v_next))

    def test_wrong_branch_real_hyperbola_cost(self):
        full,correct,wrong=projected_section_gap((),3,5,wrong_parity=+1)
        self.assertEqual(full,Q(-13,48))
        self.assertEqual(correct,full)
        self.assertEqual(wrong,Q(47,48))
        self.assertEqual(full-wrong,Q(-5,4))
        # It is a hyperbola-valid section, but not the actual p=3 history.
        u1,v1=signed_boost(*prime_uv(())[:2],3)
        self.assertEqual((u1,v1),(Q(-1,6),Q(-1,3)))
        self.assertEqual(source_branch_section(u1,+1),(Q(-1,6),Q(1,3)))
        self.assertEqual(source_branch_section(u1,+1)[0]**2-source_branch_section(u1,+1)[1]**2,Z_NEG1)

    def test_full_zeta_identity_with_fake_six_rejected(self):
        with self.assertRaises(ValueError):
            prime_pair((2,3,6))
        with self.assertRaises(ValueError):
            signed_boost(Q(1),Q(2),6)
        with self.assertRaises(ValueError):
            prime_uv((3,3))

    def test_bbpr0_initial_pole(self):
        self.assertEqual(forcing(1),Q(47,15))
        self.assertEqual(orbit(0),Q(0))
        self.assertEqual(state(1),(3,Q(2,15)))
        for n in range(1,45):
            self.assertTrue(Q(0)<forcing(n+1)<1)

    def test_exact_original_law(self):
        for n in range(1,32):
            self.assertEqual(orbit(n+1),16*orbit(n)+forcing(n+1))
            c,u=state(n)
            self.assertEqual(orbit(n),c+u)
            self.assertTrue(0<=u<1)

    def test_bbp_carry_is_source_bound(self):
        for n in range(1,40):
            j,e,k=digit_carry(n)
            c,u=state(n)
            cp,up=state(n+1)
            self.assertEqual(cp,16*c+j+e)
            self.assertEqual(up,16*u+forcing(n+1)-k)
            self.assertEqual(j,floorq(16*u))
            self.assertIn(e,(0,1))
            self.assertEqual(k,observed_force(n))

    def test_bbp_every_depth_compensation_exact(self):
        for n in range(1,18):
            for h in range(1,5):
                a,b=compensation(n,h)
                self.assertEqual(a+b,0)
                c,u=state(n)
                cp,up=state(n+h)
                self.assertEqual(a,cp-16**h*c)
                self.assertEqual(16**h*u+forced_shift(n,h)+b,up)

    def test_bbppointed_reinjection(self):
        for n in range(1,19):
            c,u=state(n)
            actual,seed=source_lift(n,c)
            self.assertEqual((actual,seed),(orbit(n),Q(0)))
            for k in [-2,-1,1,2]:
                out,s=source_lift(n,c+k)
                self.assertEqual(out,orbit(n,s))
                self.assertEqual(s,Q(k,16**n))

    def test_integer_seed_alias_regime(self):
        for n in range(1,11):
            c,u=state(n)
            new=orbit(n,Q(1))
            self.assertEqual(new,orbit(n)+16**n)
            self.assertEqual(new-floorq(new),u)
            self.assertEqual(floorq(new)%4,c%4)
        # s=1/16 is aliased only after the first tick for this mask.
        self.assertEqual((floorq(orbit(1,Q(1,16)))-floorq(orbit(1)))%4,1)
        self.assertEqual((floorq(orbit(2,Q(1,16)))-floorq(orbit(2)))%4,0)

    def test_point_in_cylinder_and_forecast(self):
        for n in range(1,21):
            for depth in range(1,4):
                c,k,lo,hi=fiber_interval(n,depth)
                self.assertTrue(lo<=orbit(n)<hi)
                self.assertEqual(hi-lo,Q(1,16**depth))
                for h in range(1,4):
                    low,high=forecast_carries(n,depth,h)
                    self.assertTrue(low<=state(n+h)[0]<=high)
                    self.assertGreaterEqual(high,low)

    def test_one_hex_digit_always_ambiguous(self):
        for n in range(1,20):
            low,high=forecast_carries(n,1,1)
            self.assertEqual(high-low,1)
        # Every one of the 16 bins has a source-dependent threshold for 0<r<1.
        for n in range(1,11):
            r=forcing(n+1)
            for k in range(16):
                low=floorq(Q(k)+r)
                high=ceilq(Q(k+1)+r)-1
                self.assertEqual(high-low,1)

    def test_two_hex_digits_ambiguity_at_most_sixteen(self):
        for n in range(1,10):
            r=forcing(n+1)
            ambiguous=0
            for k in range(256):
                low=floorq(Q(k,16)+r)
                high=ceilq(Q(k+1,16)+r)-1
                self.assertLessEqual(high-low,1)
                ambiguous+=int(high>low)
            self.assertLessEqual(ambiguous,16)

    def test_long_horizon_precision_debt(self):
        for n in range(1,12):
            for depth in [1,2]:
                a,b=forecast_carries(n,depth,depth+2)
                self.assertGreaterEqual(b-a+1,16**2)

    def test_coboundary_mutant_keeps_completed_state(self):
        g=lambda n:2*n*n
        old=Q(0);new=Q(0)
        for n in range(1,23):
            old=16*old+forcing(n)
            new=16*new+forcing(n)+g(n)-16*g(n-1)
            self.assertEqual(new-old,g(n))
            self.assertEqual(new-floorq(new),old-floorq(old))
            # Tail must change by -g(n) for the completed endpoint to agree.
            self.assertEqual(new-g(n),old)

    def test_two_step_carry_register(self):
        for n in range(1,30):
            c=state(n)[0]
            cp=state(n+1)[0]
            cpp=state(n+2)[0]
            self.assertEqual(cpp-256*c,16*(cp-16*c)+(cpp-16*cp))
            self.assertEqual(cpp-16*cp,observed_force(n+1))

    def test_input_contract(self):
        for bogus in [1,4,6,9,15]:
            with self.assertRaises(ValueError):
                prime_pair((bogus,))
        with self.assertRaises(ValueError):
            source_branch_section(Q(1),0)
        with self.assertRaises(ValueError):
            forcing(0)
        with self.assertRaises(ValueError):
            fiber_interval(1,0)

if __name__=='__main__':
    unittest.main()
