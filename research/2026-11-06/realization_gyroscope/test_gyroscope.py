"""Hostile exact-rational tests for recursive SUCC realization and radix gauges."""
from __future__ import annotations
import cmath
from fractions import Fraction
import math
import unittest
from gyroscope import (
    forcing, circle, prefix, source_state, tail_interval, initialize, advance,
    exact_replay, model_policy, phase_orbit, interleave_phase, source_bound_polynomial,
)

class TestAuthenticSource(unittest.TestCase):
    def test_original_poles_and_first_value(self):
        self.assertEqual(forcing(1), Fraction(47,15))
        for n in (2,3,5,17,41,113,401):
            a=120*n*n-89*n+16
            d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
            self.assertEqual(forcing(n), Fraction(a,d))
            self.assertGreater(forcing(n), 0)
            self.assertLess(forcing(n), Fraction(1,n*n))
            self.assertEqual(d-n*n*a, source_bound_polynomial(n-2))

    def test_source_recurrence_exact_selected_seed(self):
        g=initialize()
        self.assertEqual(g.world, 0)
        for n in range(1,100):
            prior=g.world
            g=advance(g)
            self.assertEqual(g.world, circle(16*prior+forcing(n)))
            self.assertEqual(g.world, source_state(n))
            self.assertEqual(g.observer.model_world, g.world)

    def test_tail_positive_bounds_and_nested_enclosures(self):
        for n in (1,2,7,31,97,251):
            l1,u1=tail_interval(n,8)
            l2,u2=tail_interval(n,18)
            self.assertTrue(0<l1<l2<u2<u1)
            self.assertLessEqual(u1,Fraction(1,15*(n+1)**2))
            self.assertLess(u2-l2,u1-l1)

    def test_tail_shift_identity_in_intervals(self):
        for n in (1,2,7,41):
            a,b=tail_interval(n,12)
            c,d=tail_interval(n+1,12)
            self.assertLessEqual(16*a,forcing(n+1)+d)
            self.assertLessEqual(forcing(n+1)+c,16*b)

class TestRealizedObserver(unittest.TestCase):
    def test_carrier_internal_model_self_reproduces(self):
        for seed in (0, Fraction(1,5), Fraction(7,31), Fraction(3,11)):
            truth=initialize(seed)
            replica=initialize(seed)
            for _ in range(85):
                self.assertEqual(truth,replica)
                self.assertEqual(truth.world,truth.observer.model_world)
                truth=advance(truth)
                replica=advance(replica)
            self.assertEqual(truth,replica)
            self.assertEqual(len(truth.observer.transcript),85)
            self.assertEqual(truth.observer.time,85)

    def test_wrong_source_fails_while_full_replay_commutes(self):
        def mutant(n):
            return forcing(n)+Fraction(1,37)
        correct=advance(initialize(0))
        source_mutant=advance(initialize(0),physical_source=mutant)
        model_mutant=advance(initialize(0),internal_source=mutant)
        self.assertNotEqual(correct.world,source_mutant.world)
        self.assertNotEqual(correct.observer,model_mutant.observer)
        self.assertEqual(correct.observer.model_world,correct.world)
        self.assertNotEqual(source_mutant.observer.model_world,source_mutant.world)

    def test_intent_changes_observation_not_arithmetic(self):
        def deep(_): return 3
        def shallow(_): return 1
        x=initialize(Fraction(17,257))
        a=x
        b=x
        for _ in range(32):
            a=advance(a,policy=deep)
            b=advance(b,policy=shallow)
            self.assertEqual(a.world,b.world)
            self.assertEqual(a.observer.model_world,b.observer.model_world)
        self.assertNotEqual(a.observer.transcript,b.observer.transcript)

    def test_projection_discarding_model_does_not_close(self):
        # The same initial observed hex digit does not determine the next.
        self.assertEqual(prefix(0,16,1),prefix(Fraction(1,32),16,1))
        self.assertNotEqual(prefix(circle(forcing(1)),16,1),
                            prefix(circle(Fraction(1,2)+forcing(1)),16,1))

class TestEncodingAndGauge(unittest.TestCase):
    def test_four_binary_bits_exactly_one_hex_digit(self):
        xs=[Fraction(0),Fraction(1,5),Fraction(7,31),Fraction(15,16),
            Fraction(1,17),Fraction(199,257)]
        xs.extend(source_state(n) for n in (1,2,3,7,16,32,64,97))
        for x in xs:
            bits=prefix(x,2,24)
            hexd=prefix(x,16,6)
            by_four=tuple(sum(bits[4*i+j]*2**(3-j) for j in range(4)) for i in range(6))
            self.assertEqual(by_four,hexd)

    def test_four_phase_x16_is_x2_without_approximation(self):
        for beta in (Fraction(0),Fraction(1,5),Fraction(7,31),Fraction(3,17)):
            for blocks in (1,3,17,41):
                self.assertEqual(interleave_phase(beta,blocks),phase_orbit(beta,4*blocks,2))

    def test_same_carrier_non_normal_completion_both_encodings(self):
        self.assertEqual(set(phase_orbit(Fraction(1,5),100,16)),{Fraction(1,5)})
        self.assertEqual(set(phase_orbit(Fraction(1,5),100,2)),
                         {Fraction(1,5),Fraction(2,5),Fraction(3,5),Fraction(4,5)})

    def test_time_dependent_chart_can_fake_uniform_first_digit(self):
        # World x_n=0 forever, but a moving chart generates every hex cell.
        world=Fraction(0)
        observed=[prefix(world+Fraction(n,16),16,1)[0] for n in range(16)]
        self.assertEqual(sorted(observed),list(range(16)))
        self.assertEqual(len(set([world]*16)),1)
        # A pair-block measurement reveals the fake single-digit uniformity.
        self.assertNotEqual(len({(observed[n],observed[(n+1)%16]) for n in range(16)}),256)

    def test_staircase_irrational_chart_has_sublinear_switches(self):
        # Finite diagnostic only. Universal equidistribution is proved in THEOREMS.md.
        K=2000
        theta=math.sqrt(2)-1
        z=cmath.exp(2j*math.pi*theta)
        N=K*(K+1)//2
        mean=sum(k*z**k for k in range(1,K+1))/N
        self.assertLess(abs(mean),0.002)
        self.assertLess((K-1)/N,0.002)
        self.assertLessEqual(abs(mean), (2*K+2)/(abs(1-z)**2 * N) + 1e-12)

    def test_joint_harmonic_rejects_correct_marginals_wrong_joint(self):
        # Two 31-point marginals match, but diagonal vs product do not.
        q=31
        diag=[(Fraction(k,q),Fraction(k,q)) for k in range(q)]
        prod=[(Fraction(k,q),Fraction(j,q)) for k in range(q) for j in range(q)]
        self.assertEqual({x for x,y in diag},{x for x,y in prod})
        self.assertEqual({y for x,y in diag},{y for x,y in prod})
        character=lambda x,y: cmath.exp(2j*math.pi*float(x-y))
        mean_diag=sum(character(x,y) for x,y in diag)/len(diag)
        mean_prod=sum(character(x,y) for x,y in prod)/len(prod)
        self.assertAlmostEqual(mean_diag.real,1,places=12)
        self.assertLess(abs(mean_prod),1e-12)


class TestJointGaugeCertificate(unittest.TestCase):
    def test_gauge_log_recovers_constant_causal_state(self):
        from gyroscope import decode_gauge, joint_weyl
        actions=tuple(Fraction(i,16) for i in range(16))
        observations=actions  # constant realized world 0
        self.assertEqual(tuple(decode_gauge(y,a) for y,a in zip(observations,actions)),
                         (Fraction(0),)*16)
        self.assertLess(abs(sum(cmath.exp(2j*math.pi*float(y)) for y in observations)/16),1e-12)
        for h in (1,2,3,7):
            self.assertAlmostEqual(joint_weyl(observations,actions,h).real,1,places=12)

    def test_arbitrary_adaptive_charts_do_not_change_decoded_source(self):
        from gyroscope import decode_gauge, joint_weyl
        xs=tuple(source_state(n) for n in range(1,45))
        shifts=tuple(Fraction((n*n+5*n+3)%43,43) for n in range(len(xs)))
        observed=tuple(circle(x+a) for x,a in zip(xs,shifts))
        decoded=tuple(decode_gauge(y,a) for y,a in zip(observed,shifts))
        self.assertEqual(decoded,xs)
        for h in (-3,1,2,5):
            direct=sum(cmath.exp(2j*math.pi*h*float(x)) for x in xs)/len(xs)
            self.assertLess(abs(joint_weyl(observed,shifts,h)-direct),1e-12)

    def test_incorrect_action_log_detectably_changes_decoding(self):
        from gyroscope import decode_gauge
        x=Fraction(7,31)
        for shift in (Fraction(1,13),Fraction(3,17),Fraction(5,19)):
            observed=circle(x+shift)
            self.assertEqual(decode_gauge(observed,shift),x)
            self.assertNotEqual(decode_gauge(observed,shift+Fraction(1,32)),x)

if __name__=='__main__':
    unittest.main(verbosity=2)