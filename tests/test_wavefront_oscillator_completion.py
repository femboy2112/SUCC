"""Exact finite source and hostile tests for pumped/complete Oily wavefronts.

This is a research-only positive-source observer model. It must not replace the
original BBP signed forcing, seed, or Weyl cancellation obligation.
"""
from __future__ import annotations

import unittest
from fractions import Fraction as F
from math import comb

from observational_succ.wavefront_oracle_two_stage import SourceGeometry
from observational_succ.wavefront_oscillator_completion import (
    BBP_TAPS, _matrix_power, _apply, oily_packet_matrix,
    packet_matrix_coefficient, stationary_oily_state,
    stationary_oily_source, partial_oily_source, raw_packet_tail,
    certified_uniform_raw_tail_bound, kernel_hankel_determinant,
    minimum_registers_oily, observer_matrix, step_observer,
    critical_memory_power, critical_transient_bound, source_signed_tap,
    pumped_source_oscillator, signed_four_pole_moment,
    impulse_shell_moment, periodic_response, periodic_trace,
    two_stage_high_frequency_condition, critical_stage_condition,
    critical_periodic_source_average,
)


class WavefrontOscillatorTests(unittest.TestCase):
    SOURCE_X=(F(0),F(1,9),F(1,3),F(1,2),F(2,3),F(7,8),F(1))

    def test_packet_source_exact_for_many_grades(self):
        for x in self.SOURCE_X:
            for j in range(18):
                self.assertEqual(packet_matrix_coefficient(x,j),SourceGeometry(x).raw_grade(j))

    def test_oily_source_same_global_integral_kernel(self):
        for x in self.SOURCE_X:
            self.assertEqual(stationary_oily_source(x),SourceGeometry(x).source_total())
            self.assertEqual(stationary_oily_source(x),
                (1-x)/((2-x*x)*(x*x-2*x+2)))

    def test_oily_resolvent_fixed_point(self):
        for x in self.SOURCE_X:
            y=stationary_oily_state(x)
            m=oily_packet_matrix(x)
            self.assertEqual(y,(y[0]*m[0][0]+y[1]*m[0][1],y[1]*m[1][1]+1))

    def test_positive_completion_with_certified_uniform_tail(self):
        for x in self.SOURCE_X:
            for j in range(22):
                rem=raw_packet_tail(x,j)
                self.assertGreaterEqual(rem,0)
                self.assertLessEqual(rem,certified_uniform_raw_tail_bound(x,j))
                self.assertEqual(partial_oily_source(x,j)+rem,stationary_oily_source(x))

    def test_uniform_tail_sharp_normalized_at_endpoint(self):
        x=F(1)
        # Raw source goes to zero at x=1. Divide by 1-x first.
        for j in range(10):
            prob_tail=1-sum((SourceGeometry(x).grade_probability(k) for k in range(j+1)),F(0))
            self.assertEqual(prob_tail,F(j+3,2**(j+2)))

    def test_rank_two_hankel_determinant(self):
        for x in self.SOURCE_X:
            s=SourceGeometry(x)
            self.assertEqual(kernel_hankel_determinant(x),-s.normalization**2*s.u*s.v)
            self.assertEqual(minimum_registers_oily(x),2)
        self.assertEqual(kernel_hankel_determinant(1),F(-1,64))

    def test_moment_kernel_hankel_no_one_register(self):
        x=F(1)
        s=SourceGeometry(x)
        # Rank-one impulse response would require q0 q2 = q1^2.
        self.assertNotEqual(s.grade_probability(0)*s.grade_probability(2),
                            s.grade_probability(1)**2)

    def test_critical_jordan_exact_matrix_powers(self):
        for n in range(45):
            self.assertEqual(_matrix_power(observer_matrix(1),n),critical_memory_power(n))

    def test_transient_bound_and_contraction(self):
        self.assertEqual(critical_transient_bound(8),F(9,256))
        self.assertLess(critical_transient_bound(4),1)
        for n in range(2,35):
            self.assertGreater(critical_transient_bound(n),critical_transient_bound(n+1))

    def test_original_source_taps_not_replaced(self):
        self.assertEqual(BBP_TAPS,(F(4),F(0),F(0),F(-2),F(-1),F(-1),F(0),F(0)))
        for n in range(1,40):
            self.assertEqual(signed_four_pole_moment(n),impulse_shell_moment(n))

    def test_contracting_vs_pumped_shells(self):
        for t in range(80):
            self.assertEqual(pumped_source_oscillator(t),16**(t//8)*source_signed_tap(t))
            self.assertEqual(source_signed_tap(t+8),source_signed_tap(t)/16)
            self.assertEqual(pumped_source_oscillator(t+8),pumped_source_oscillator(t))

    def test_mean_zero_signed_source_waves(self):
        self.assertEqual(sum(BBP_TAPS),0)
        self.assertEqual(critical_periodic_source_average(),0)

    def test_pumped_periodic_orbit_is_exact_cycle(self):
        for x in self.SOURCE_X:
            states, y0=periodic_response(x)
            self.assertEqual(len(states),8)
            self.assertEqual(states[0],y0)
            _,one_period=periodic_trace(x,start=y0,cycles=1)
            self.assertEqual(one_period,y0)
            self.assertEqual(sum(z[0] for z in states),0)
            self.assertEqual(sum(z[1] for z in states),0)

    def test_real_cycle_not_constant(self):
        states,_=periodic_response(1)
        self.assertGreater(len(set(states)),1)
        self.assertNotEqual(states[0],(0,0))
        self.assertEqual(states[0],(F(-4,17),F(-2548,4335)))

    def test_convergence_to_pumped_cycle_exact(self):
        x=F(1)
        states,correct=periodic_response(x)
        wrong=(F(2),F(-3))
        for cycles in (1,2,3,5):
            _,actual=periodic_trace(x,start=wrong,cycles=cycles)
            delta=(wrong[0]-correct[0],wrong[1]-correct[1])
            expected=_apply(critical_memory_power(8*cycles),delta)
            self.assertEqual((actual[0]-correct[0], actual[1]-correct[1]),expected)
            err=max(abs(v) for v in expected)
            self.assertLessEqual(err,critical_transient_bound(8*cycles)*max(map(abs,delta)))

    def test_steady_state_completion_requires_pump(self):
        # The actual c_n contracts as 16^-k. The artificially pumped period
        # does not. Removing the external pump is not a harmless relabeling.
        self.assertEqual(source_signed_tap(0),F(4))
        self.assertEqual(source_signed_tap(8),F(1,4))
        self.assertEqual(pumped_source_oscillator(8),F(4))

    def test_sign_mutation_breaks_four_pole_passport(self):
        changed=list(BBP_TAPS)
        changed[3]=F(2) # wrong sign
        wrong=sum((c/F(j+1) for j,c in enumerate(changed)),F(0))
        self.assertNotEqual(wrong,signed_four_pole_moment(1))

    def test_gain_control_breaks_original_signed_source(self):
        wrong=tuple(2*c for c in BBP_TAPS)
        self.assertNotEqual(sum((c/F(j+1) for j,c in enumerate(wrong)), F(0)),
                            signed_four_pole_moment(1))

    def test_equal_stage_conditioning(self):
        self.assertEqual(two_stage_high_frequency_condition(F(1)),F(9))
        self.assertEqual(two_stage_high_frequency_condition(F(0)),F(1))
        for m in range(8):
            self.assertEqual(critical_stage_condition(m),3**m)

    def test_critical_fourier_phase_exponential_loss(self):
        # The alternating 8-cycle has frequency pi; each 1/2 filter
        # attenuates it by 1/3, so the m-stage inversion costs 3^m.
        alternating=tuple(F((-1)**j) for j in range(8))
        for x in (F(1),):
            y,_=periodic_response(x,alternating)
            # y0[1], the second stage, has alternating amplitude 1/9.
            self.assertEqual(tuple(s[1] for s in y),
                             tuple(F(1 if j%2==0 else -1,9) for j in range(8)))

    def test_constant_oracle_perfect_knowledge_control(self):
        # An informed observer with the periodic source law and phase can
        # forecast W(t) exactly regardless of retarded smoothing.
        for n in range(32):
            self.assertEqual(pumped_source_oscillator(n+8),pumped_source_oscillator(n))
        # Constant is another lawful wavefront: no temporal epistemic defect.
        states,_=periodic_response(1,(F(5),))
        self.assertEqual(states,((F(5),F(5)),))

    def test_one_step_identity_beats_oily_for_exact_received_signal(self):
        # With noiseless W(t-1) available and MSE target W(t-1),
        # zero extra smoothing is optimal, not theta=1/2.
        received=F(1)
        smooth_estimate=F(1,2)
        perfect_estimate=received
        self.assertGreater((smooth_estimate-received)**2,
                           (perfect_estimate-received)**2)

    def test_bad_input_guard(self):
        for func in (lambda:packet_matrix_coefficient(1,-1),
                     lambda:partial_oily_source(1,-1),
                     lambda:critical_memory_power(-1),
                     lambda:periodic_response(1,()),
                     lambda:SourceGeometry(F(3,2))):
            with self.assertRaises(ValueError):
                func()

if __name__ == "__main__":
    unittest.main()

# Separate class is intentionally recognized by unittest discovery.
class SourceInverseAndChiralOscillatorTests(unittest.TestCase):
    def test_exact_source_reconstruction_from_two_stage_report(self):
        from observational_succ.wavefront_oscillator_completion import decode_source_two_steps
        from observational_succ.wavefront_oracle_two_stage import run_two_stages
        values=[F(2),F(-3),F(7,4),F(0),F(1),F(-2),F(8,7),F(5)]
        for x in (F(0),F(1,2),F(7,8),F(1)):
            e1,e2=run_two_stages(values+[F(0)]*6,x)
            decoded=decode_source_two_steps(e2,x)
            self.assertEqual(decoded[:len(values)],tuple(values))

    def test_reconstruction_noise_amplification_sharp(self):
        from observational_succ.wavefront_oscillator_completion import (
            decode_source_two_steps,decoder_noise_gain,
        )
        eps=F(1,100000)
        err=[eps if t%2==0 else -eps for t in range(64)]
        decoded=decode_source_two_steps(err,1)
        self.assertEqual(decoder_noise_gain(1),9)
        for t in range(2,len(err)):
            self.assertEqual(abs(decoded[t-2]),9*eps)

    def test_phase_corrected_reemission_no_new_smoothing(self):
        from observational_succ.wavefront_oscillator_completion import decode_source_two_steps
        from observational_succ.wavefront_oracle_two_stage import run_two_stages
        W=tuple(BBP_TAPS*5)
        _,e2=run_two_stages(W+tuple(F(0) for _ in range(5)),1)
        decoded=decode_source_two_steps(e2,1)
        # A descendant can emit these exact already-delivered source values,
        # just later. It cannot receive W(t) at the same time t.
        self.assertEqual(tuple(decoded[:len(W)]),W)

    def test_chiral_period_exact_R_sqrt2(self):
        from observational_succ.wavefront_oscillator_completion import (
            normalized_chiral_period_radical2, normalized_chiral_periodic_response,
        )
        t=normalized_chiral_period_radical2()
        self.assertEqual(t,((F(4),F(0)),(0,0),(0,0),
                            (0,F(-4)),(F(-4),0),(0,F(-4)),(0,0),(0,0)))
        self.assertEqual(sum(a for a,b in t),0)
        self.assertEqual(sum(b for a,b in t),F(-8))
        states=normalized_chiral_periodic_response(1)
        self.assertEqual(len(states),8)
        self.assertEqual(sum(p[0][0] for p in states),0)
        self.assertEqual(sum(p[0][1] for p in states),F(-8))
        self.assertEqual(sum(p[1][0] for p in states),0)
        self.assertEqual(sum(p[1][1] for p in states),F(-8))


class ConditionalMaxEntropyBirthTests(unittest.TestCase):
    def test_binary_maxent_probabilities_and_exact_source_rates(self):
        from observational_succ.wavefront_oscillator_completion import (
            maximum_entropy_two_bit_emitter,sizebiased_emitter_rates,
        )
        for x in (F(0),F(1,7),F(1,4),F(1,2),F(4,5),F(1)):
            p=maximum_entropy_two_bit_emitter(x)
            self.assertEqual(sum(p),1)
            self.assertEqual(p[1]+p[2]+2*p[3],x)
            self.assertEqual(sizebiased_emitter_rates(x),
                             (SourceGeometry(x).u,SourceGeometry(x).v))
        self.assertEqual(sizebiased_emitter_rates(1),(F(1,2),F(1,2)))

    def test_correlated_birth_same_mean_different_source(self):
        x=F(1)
        # MaxEnt law: P(00)=P(01)=P(10)=P(11)=1/4.
        # Correlated alternative: P(00)=P(11)=1/2. Same E[B]=1,
        # but size-biased rates (0,1), not authentic (1/2,1/2).
        bad=(F(1,2),F(0),F(0),F(1,2))
        self.assertEqual(bad[1]+bad[2]+2*bad[3],x)
        self.assertEqual((bad[1]+bad[2],2*bad[3]),(0,1))
        self.assertNotEqual((bad[1]+bad[2],2*bad[3]),
                            (SourceGeometry(x).u,SourceGeometry(x).v))


class FullRepoOriginalSourceBridgeTests(unittest.TestCase):
    def test_actual_chiral_main_source_passport(self):
        try:
            from observational_succ.rank_two_chiral_towers import (
                TAPS as REPO_TAPS, impulse as repo_impulse,
                source_moment as repo_moment,
                original_zero_seed_prefix,
            )
        except ImportError:
            self.skipTest('full SUCC original rank_two_chiral_towers.py required')
        from observational_succ.wavefront_oscillator_completion import (
            source_signed_tap, signed_four_pole_moment,
        )
        self.assertEqual(tuple(REPO_TAPS),BBP_TAPS)
        for k in range(128):
            self.assertEqual(repo_impulse(k),source_signed_tap(k))
        for n in range(1,65):
            self.assertEqual(repo_moment(n),signed_four_pole_moment(n))
        self.assertEqual(original_zero_seed_prefix(0),F(0))
        self.assertEqual(original_zero_seed_prefix(1),signed_four_pole_moment(1))


class ConditionalRetentionControl(unittest.TestCase):
    def test_maxent_not_sufficient_without_rate_to_retention_transport(self):
        from observational_succ.wavefront_oscillator_completion import sizebiased_emitter_rates
        x=F(1)
        u,v=sizebiased_emitter_rates(x)
        self.assertEqual((u,v),(F(1,2),F(1,2)))
        authentic_q0=(1-u)*(1-v)
        alt_q0=(1-u*u)*(1-v*v) # same binary source, different retention law
        self.assertEqual(authentic_q0,F(1,4))
        self.assertEqual(alt_q0,F(9,16))
        self.assertNotEqual(authentic_q0,alt_q0)
