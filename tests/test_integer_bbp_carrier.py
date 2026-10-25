"""Independent exact tests: integer-hosted source, carries, phase and rejection."""
from fractions import Fraction as Q
from math import gcd, lcm
import unittest

from observational_succ.integer_bbp_carrier import (
    IntegerState, forcing_pair, step, source_states, conductor_at,
    pair, unpair, coded_step, coded_predecessor, source_level_inverse,
    carry_residue16, common_clock, integer_collision_count, tail_bounds,
    hexadecimal_digit, circle_inverse_discontinuity,
    odd_rational_counterfeit_tail, odd_rational_counterfeit_forcing,
)


def reference_forcing(n):
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def machin_pi(terms=200):
    # Independent alternating arctangent enclosures, no imported pi digits.
    def atan(q):
        a=sum((Q((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(terms)),Q())
        b=a+Q((-1)**terms,(2*terms+1)*q**(2*terms+1))
        return min(a,b),max(a,b)
    a,b=atan(5); c,d=atan(239)
    return 16*a-4*d,16*b-4*c


class IntegerHostAndSource(unittest.TestCase):
    def test_odd_reduced_source_against_original_four_poles(self):
        for n in range(1,1025):
            a,b=forcing_pair(n)
            self.assertEqual(Q(a,b),reference_forcing(n))
            self.assertEqual(b%2,1)
            self.assertEqual(gcd(a,b),1)
            self.assertGreater(a,0)
        self.assertEqual(forcing_pair(1),(47,15))

    def test_full_unwrapped_and_circle_recurrences_and_literal_carries(self):
        history=source_states(512); u=y=Q(); ksum=0
        for n,state in enumerate(history[1:],1):
            r=reference_forcing(n)
            raw=16*y+r; carry=raw.numerator//raw.denominator
            u=16*u+r; y=raw%1
            self.assertEqual(Q(state.numerator,state.conductor),u)
            self.assertEqual(Q(state.remainder,state.conductor),y)
            out,k=step(history[n-1])
            self.assertEqual(out,state)
            self.assertEqual(k,carry)
            ksum=16*ksum+k
            self.assertEqual(ksum,state.integer_part)
            self.assertEqual(state.conductor%2,1)
            self.assertEqual(state.conductor%history[n-1].conductor,0)
            self.assertEqual(carry_residue16(n,state.remainder),carry%16)

    def test_least_nested_conductor_and_odd_lcm_upper_bound(self):
        q=1; bound=1; j=1
        for n in range(1,129):
            q=lcm(q,reference_forcing(n).denominator)
            while j<=8*n-3:
                bound=lcm(bound,j); j+=2
            self.assertEqual(conductor_at(n),q)
            self.assertEqual(bound%q,0)
            self.assertLess(source_states(n)[-1].numerator,16**n*q)

    def test_actual_N_program_is_total_injective_and_not_ordinary_succ(self):
        for a in range(30):
            for b in range(30): self.assertEqual(unpair(pair(a,b)),(a,b))
        outputs=[coded_step(k) for k in range(1000)]
        self.assertEqual(len(set(outputs)),len(outputs))
        for k,out in enumerate(outputs): self.assertEqual(coded_predecessor(out),k)
        self.assertNotEqual(coded_step(0),1)
        c=0
        for n,state in enumerate(source_states(100)):
            self.assertEqual(c,pair(n,state.numerator))
            c=coded_step(c)
        with self.assertRaises(ValueError): coded_predecessor(0)
        with self.assertRaises(ValueError): coded_predecessor(pair(1,48))

    def test_odd_finite_phase_transition_is_injective_with_exact_partial_inverse(self):
        for n in range(1,5):
            q0,q=conductor_at(n-1),conductor_at(n)
            a,b=forcing_pair(n); c=(q//b)*a; g=q//q0
            inputs=list(range(min(q0,500)))+[q0-1]
            outs={}
            for x in inputs:
                out=(16*g*x+c)%q
                self.assertEqual(source_level_inverse(n,out),x)
                self.assertEqual((out-c)%g,0)
                outs[x]=out
            self.assertEqual(len(set(outs.values())),len(outs))
            if g>1:
                with self.assertRaises(ValueError): source_level_inverse(n,(c+1)%q)
        with self.assertRaises(ValueError): IntegerState(1,16,0)

    def test_recover_complete_phase_history_and_carries_from_final_integer(self):
        states=source_states(256)
        residue=states[-1].remainder
        for n in range(256,0,-1):
            self.assertEqual(residue,states[n].remainder)
            previous=source_level_inverse(n,residue)
            a,b=forcing_pair(n); q=conductor_at(n); g=q//conductor_at(n-1)
            c=(q//b)*a
            k=(16*g*previous+c-residue)//q
            self.assertEqual(k,step(states[n-1])[1])
            residue=previous
        self.assertEqual(residue,0)

    def test_literal_carry16_is_not_hex_digit_zero(self):
        # General odd-clock state, NOT the authenticated numerator at this n.
        st=IntegerState(1,1001,1000)
        out,k=step(st)
        self.assertEqual(k,16)
        self.assertEqual(k%16,0)
        with self.assertRaises(ValueError): hexadecimal_digit(out)


class ObserversAndLimits(unittest.TestCase):
    def test_all_finite_phase_history_in_one_odd_clock(self):
        states=source_states(97)[1:]
        modulus,addresses=common_clock(states)
        for s,a in zip(states,addresses):
            self.assertEqual(Q(a,modulus),Q(s.remainder,s.conductor))
        self.assertEqual(modulus%2,1)

    def test_source_pair_collision_count_matches_independent_fraction_oracle(self):
        states=source_states(128)
        for p in (17,41,97,257):
            m=(p-1)//8; window=states[m+1:4*m+1]
            ys=[Q(s.remainder,s.conductor) for s in window]
            for mesh in (4,16,64):
                expected=sum(min(abs(x-y),1-abs(x-y))<=Q(1,mesh)
                             for x in ys for y in ys)
                self.assertEqual(integer_collision_count(window,mesh),expected)
            if p==97:
                self.assertEqual(integer_collision_count(window,16),240)
        with self.assertRaises(ValueError): integer_collision_count(tuple(),16)

    def test_lossless_forward_transition_can_have_discontinuous_circle_inverse(self):
        for k in (1,2,16,100,10000):
            num,den=circle_inverse_discontinuity(k)
            self.assertEqual((16*num)%den,1)
            self.assertGreater(Q(num,den),Q(1,16))
            self.assertLess(Q(num,den)-Q(1,16),Q(1,k))
        # An even clock has the familiar multiple inverse branches.
        preimages=[r for r in range(16) if 16*r%16==0]
        self.assertEqual(len(preimages),16)

    def test_true_pi_digits_source_only_and_independent_machin_interval(self):
        lo,hi=machin_pi(220)
        used=[]
        for state in source_states(128)[1:]:
            digit,depth=hexadecimal_digit(state)
            a,b=16**state.n*lo,16**state.n*hi
            self.assertEqual(a.numerator//a.denominator,b.numerator//b.denominator)
            self.assertEqual(digit,(a.numerator//a.denominator)%16)
            used.append(depth)
        self.assertLessEqual(max(used),48)
        with self.assertRaises(ValueError): hexadecimal_digit(IntegerState(2,4095,0))

    def test_boundaries_in_true_digit_carry_cocycle(self):
        states=source_states(129)
        eps=[]
        for s in states[1:]:
            a,b=tail_bounds(s.n,10)
            y=Q(s.remainder,s.conductor)
            low,hi=y+a,y+b
            self.assertEqual(low.numerator//low.denominator,hi.numerator//hi.denominator)
            eps.append(low.numerator//low.denominator)
        for i,s in enumerate(states[1:-1]):
            digit,_=hexadecimal_digit(s)
            literal=step(s)[1]
            self.assertEqual(digit,literal+eps[i+1]-16*eps[i])

    def test_positive_odd_rational_fake_has_same_host_but_nonnormal_orbit(self):
        u=Q(); q=1
        for n in range(1,80):
            r=odd_rational_counterfeit_forcing(n)
            self.assertGreater(r,0); self.assertEqual(r.denominator%2,1)
            q=lcm(q,r.denominator);u=16*u+r
            self.assertEqual((u+odd_rational_counterfeit_tail(n))%1,Q(1,3))
            self.assertEqual((u*q).denominator,1)
        self.assertNotEqual(odd_rational_counterfeit_forcing(1),reference_forcing(1))

    def test_all_finite_time_congruence_decoders_have_real_error_floor(self):
        from observational_succ.integer_bbp_carrier import finite_residue_decoder_lower_bound
        for q in (2,3,8,16,17,32,64,127,256):
            states=source_states(q+1)
            y0=Q(); y1=Q(2,15)
            yq=Q(states[q].remainder,states[q].conductor)
            yq1=Q(states[q+1].remainder,states[q+1].conductor)
            def dist(a,b):
                d=abs(a-b); return min(d,1-d)
            lower=finite_residue_decoder_lower_bound(q)
            self.assertGreater(lower,Q(1,510))
            self.assertGreaterEqual(max(dist(yq,y0),dist(yq1,y1)),2*lower)
            self.assertLess(lower,Q(1,255))
        with self.assertRaises(ValueError): finite_residue_decoder_lower_bound(1)

    def test_state_domain_and_source_mutants_fail_closed(self):
        for args in ((-1,1,0),(0,0,0),(0,2,0),(0,1,-1)):
            with self.assertRaises(ValueError): IntegerState(*args)
        with self.assertRaises(ValueError): forcing_pair(0)
        with self.assertRaises(ValueError): coded_step(-1)
        with self.assertRaises(ValueError): unpair(True)
        with self.assertRaises(ValueError): common_clock(tuple())


if __name__=='__main__': unittest.main()
