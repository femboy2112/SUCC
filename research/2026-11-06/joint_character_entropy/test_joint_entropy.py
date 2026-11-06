"""Exact-rational source + finite entropy inequality hostile controls."""
import math
import random
import unittest
from fractions import Fraction
from joint_entropy import (four_pole,tail_enclosure,original_states,
    certified_completed_digit,certified_source_digits,pole_clock,
    mealy_run,decode_reversible_observer,block_distribution,block_entropy,entropy_budget,
    rotations_for_rational_seed,circle_joint_character)
from independent_oracle import machin_pi16_interval,digit_certificates,independent_combined_source


def binary_debruijn(order):
    """Independent standard Eulerian de Bruijn recursion; finite calibration only."""
    a=[0]*(2*order)
    seq=[]
    def db(t,p):
        if t>order:
            if order%p==0:
                seq.extend(a[1:p+1])
        else:
            a[t]=a[t-p]
            db(t+1,p)
            for j in range(a[t-p]+1,2):
                a[t]=j
                db(t+1,t)
    db(1,1)
    return tuple(seq)


class BBPSourceChecks(unittest.TestCase):
    def test_poles_two_oracles(self):
        self.assertEqual(four_pole(1),Fraction(47,15))
        for n in range(1,300):
            self.assertEqual(four_pole(n),independent_combined_source(n))

    def test_source_enclosure_contains_deeper_source_enclosure(self):
        for n in (0,1,2,7,13,37,127):
            left,right=tail_enclosure(n,8)
            deeper_left,deeper_right=tail_enclosure(n,20)
            self.assertLessEqual(left,deeper_left)
            self.assertLessEqual(deeper_right,right)
            self.assertLess(left,right)

    def test_pi_digits_certified_by_two_analytic_routes(self):
        n=96
        digits,depths=certified_source_digits(n)
        independent=digit_certificates(machin_pi16_interval(120,36),n)
        self.assertEqual(digits,independent)
        self.assertEqual(''.join(format(x,'x') for x in digits[:16]),'3243f6a8885a308d')
        self.assertLessEqual(max(depths),20)

    def test_rational_seed_translation_exact_every_state(self):
        for s in (Fraction(1,7), Fraction(1,5), Fraction(1,32),Fraction(-5,17)):
            u=original_states(180)
            v=original_states(180,s)
            a=rotations_for_rational_seed(s,180)
            for x,y,q in zip(u,v,a):
                self.assertEqual(y,(x+q)%1)

    def test_periodic_source_pole_clock(self):
        p=7
        self.assertEqual([pole_clock(i,p) for i in range(p)],[(8*(i+1)-7)%p for i in range(p)])
        self.assertEqual([pole_clock(i,p) for i in range(100)], [pole_clock(i+p,p) for i in range(100)])

    def test_digit_boundary_mutation_fails_closed_certificate(self):
        lo,hi=tail_enclosure(0,1)
        x=(Fraction(1,4)-(lo+hi)/2)%1
        # Deliberately short source enclosure straddles a digit boundary.
        with self.assertRaises(ArithmeticError):
            certified_completed_digit(x,0,initial_depth=1,max_depth=1)


class FiniteStateEntropyChecks(unittest.TestCase):
    def test_mealy_output_and_state_determinism(self):
        x=[(5*i)%16 for i in range(100)]
        s=[pole_clock(i) for i in range(100)]
        y,q=mealy_run(x,s)
        self.assertEqual(len(y),100)
        self.assertEqual(len(q),101)
        for i in range(100):
            self.assertEqual(y[i],(x[i]+s[i]+q[i])%16)
            self.assertEqual(q[i+1],(q[i]+3*x[i]+2*s[i])%16)

    def test_finite_entropy_inequality_exact_path_families(self):
        rng=random.Random(4815)
        for base,states,N in ((2,1,230),(2,4,230),(4,8,260),(16,16,270)):
            inputs=[rng.randrange(base) for _ in range(N)]
            sources=[(8*(i+1)-7)%7 for i in range(N)]
            outputs,_=mealy_run(inputs,sources,base=base,states=states)
            for k,L in ((1,1),(1,2),(1,4),(2,4),(2,6),(3,6),(3,9)):
                r=entropy_budget(inputs,sources,outputs,states,base,k,L)
                self.assertGreaterEqual(r['slack'],-1e-10,(base,states,k,L,r))

    def test_source_logged_reversible_observer(self):
        digits,_=certified_source_digits(180)
        tape=tuple(pole_clock(i,7) for i in range(180))
        encoded,states=mealy_run(digits,tape)
        self.assertEqual(decode_reversible_observer(encoded,tape),digits)
        self.assertEqual(decode_reversible_observer(encoded,tape,start=states[0]),digits)
        # A single deliberate source-tape mutation changes the recovered world.
        wrong=list(tape)
        wrong[37]=(wrong[37]+1)%7
        self.assertNotEqual(decode_reversible_observer(encoded,wrong),digits)

    def test_constant_input_periodic_source_cannot_fake_asymptotic_normality(self):
        N=512
        input_digits=(0,)*N
        source=tuple(i%7 for i in range(N))
        output,q=mealy_run(input_digits,source,base=16,states=16)
        r=entropy_budget(input_digits,source,output,16,16,2,12)
        self.assertGreater(r['input_deficit'],0)
        self.assertGreaterEqual(r['slack'],-1e-10)
        # At most clock phases * internal states => no full normality in arbitrary L.
        self.assertLessEqual(len(set(tuple(output[i:i+12]) for i in range(N-11))),7*16)

    def test_necessary_source_information_term_with_debruijn_mutant(self):
        n=160
        raw=(0,)*n
        seq=binary_debruijn(5)
        self.assertEqual(len(seq),32)
        external=tuple(seq[i%len(seq)] for i in range(n))
        output,_=mealy_run(raw,external,base=2,states=1,
                          emit=lambda q,d,s,b:s,transition=lambda q,d,s,b:0)
        r=entropy_budget(raw,external,output,1,2,1,5)
        self.assertGreaterEqual(r['slack'],-1e-10)
        # If the positive-entropy finite-window source cost is omitted, inequality fails.
        bound_without_source=(r['output_deficit'])/5+r['continuity_budget']
        self.assertLess(bound_without_source,r['input_deficit'])
        self.assertGreater(r['source_block_entropy'],2.0)

    def test_unconstrained_output_length_rejected(self):
        with self.assertRaises(ValueError):
            mealy_run([0,1],[0],base=2)
        with self.assertRaises(ValueError):
            entropy_budget([1]*7,[0]*7,[1]*7,1,2,2,7)

    def test_nontrivial_certified_source_digit_observer(self):
        x,_=certified_source_digits(128)
        source=tuple(pole_clock(i,7) for i in range(128))
        y,q=mealy_run(x,source)
        for k,L in ((1,8),(2,8),(2,12)):
            r=entropy_budget(x,source,y,16,16,k,L)
            self.assertGreaterEqual(r['slack'],-1e-10)
        self.assertTrue(0<=x[0]<16)
        self.assertTrue(any(a!=b for a,b in zip(x,y)))


class GaugeHostileControls(unittest.TestCase):
    def test_periodic_chart_fourier_and_exact_joint_reconstruction(self):
        x=original_states(100)
        a=tuple(Fraction(pole_clock(i,7),7) for i in range(100))
        z=circle_joint_character(x,a,1)
        direct=circle_joint_character(x,tuple(Fraction(0) for _ in x),1)
        self.assertLess(abs(z-direct),1e-12)

    def test_periodic_chart_marginal_can_mask_one_mode_but_not_all(self):
        N=700
        a=[Fraction(i%7,7) for i in range(N)]
        y=a  # constant input x=0
        e1=abs(sum(complex(math.cos(2*math.pi*float(t)),math.sin(2*math.pi*float(t))) for t in y)/N)
        e7=abs(sum(complex(math.cos(14*math.pi*float(t)),math.sin(14*math.pi*float(t))) for t in y)/N)
        self.assertLess(e1,1e-12)
        self.assertLess(abs(e7-1),1e-12)
        self.assertLess(abs(circle_joint_character(tuple(Fraction(0) for _ in y),tuple(a),7)-1),1e-12)

    def test_irrational_staircase_needs_unbounded_clock(self):
        K=150
        theta=math.sqrt(2)-1
        obs=[((k*theta)%1) for k in range(1,K+1) for _ in range(k)]
        N=len(obs)
        e1=sum(complex(math.cos(2*math.pi*t),math.sin(2*math.pi*t)) for t in obs)/N
        self.assertLess(abs(e1),0.08)
        self.assertEqual(N,K*(K+1)//2)
        self.assertLess(K/N,0.02)
        # The decoded input of this gauge is exactly zero, hence e(hx)=1.


if __name__=='__main__':
    unittest.main(verbosity=2)
