"""Fast source-grounded quantum circuit identities; no repo-wide CI."""
import unittest
from cmath import exp, pi
from fractions import Fraction
from math import sqrt, sin, isclose
from omega_quantum import *
from omega_haar import (partition_mean, commutator, chronological_area,
                        branch_parity_detail, fiber_at, source_block, energy)


class TestOmegaQuantum(unittest.TestCase):
    def test_full_haar_parseval_and_reversal(self):
        for n in (2,4,8,16,32):
            raw = tuple(complex((k*k+7)%19, (5*k)%11-6) for k in range(n))
            coeff=haar_analyze(raw)
            recovered=haar_synthesize(coeff)
            self.assertLess(max(abs(a-b) for a,b in zip(raw,recovered)),1e-12)
            self.assertAlmostEqual(sum(abs(x)**2 for x in raw),sum(abs(x)**2 for x in coeff),places=10)
        self.assertNotEqual(haar_analyze((1+0j,)+(0j,)*15),
                            walsh_hadamard((1+0j,)+(0j,)*15))

    def test_Walsh_H_four_vs_fiber_parity(self):
        chi=parity_character_state()
        self.assertEqual(len(chi),16)
        self.assertLess(max(abs(chi[k]-(-1)**k/4) for k in range(16)),1e-15)
        for t in (0.1,0.35,0.75):
            values=fiber_at(t,lambda x: exp(2j*pi*25*x)+.4*exp(-2j*pi*8*x))
            self.assertLess(abs(fiber_parity_overlap(values)-4*branch_parity_detail(values)),1e-13)
            vnorm=sqrt(sum(abs(v)**2 for v in values))
            probability=abs(fiber_parity_overlap(values)/vnorm)**2
            self.assertGreaterEqual(probability,-1e-14)
            self.assertLessEqual(probability,1+1e-12)

    def test_pair_triple_analysis_is_unitary(self):
        for group in (2,3):
            for n in (0,1,15):
                raw=tuple(complex(x) for x in source_block(n))
                transformed=group_butterfly(raw,group)
                recovered=group_butterfly(transformed,group,inverse=True)
                self.assertLess(max(abs(x-y) for x,y in zip(raw,recovered)),1e-14)
                self.assertAlmostEqual(sum(abs(x)**2 for x in raw),
                                       sum(abs(x)**2 for x in transformed),places=13)
                projected=projected_by_measurement(raw,group)
                goal=partition_mean(source_block(n),group)
                self.assertLess(max(abs(x-float(y)) for x,y in zip(projected,goal)),1e-14)
                # Projected output is lossy even though the analyzed detail is not.
                self.assertGreater(sum(abs(x-y)**2 for x,y in zip(raw,projected)),0)

    def test_zero_group_rejected(self):
        with self.assertRaises(ValueError):
            group_butterfly((1j, 2j), 0)

    def test_skew_rotation_unitarity_inverse_period(self):
        for n in (0,2,8):
            v=tuple(float(x) for x in source_block(n))
            for t in (-2.1,.25,1.5,3.0):
                y=skew_exp_rotation(v,t)
                back=skew_exp_rotation(y,-t)
                self.assertLess(max(abs(x-z) for x,z in zip(v,back)),1e-12)
                self.assertAlmostEqual(sum(x*x for x in v),sum(x*x for x in y),places=12)
        self.assertAlmostEqual(GAMMA*GAMMA,2/9)

    def test_quantum_chirality_exact_matrix_expectation(self):
        M=chirality_matrix()
        for i in range(12):
            for j in range(12):
                self.assertLess(abs(M[i][j]-M[j][i].conjugate()),1e-15)
        for n in (0,1,7,20):
            v,w=source_block(n),source_block(n+1)
            exact=chirality_exact(v,w)
            self.assertEqual(exact,2*chronological_area(n)/(energy(v)+energy(w)))
            self.assertLess(abs(float(exact)-chirality_direct(v,w)),5e-15)
            self.assertGreater(exact,0)
            self.assertEqual(chirality_exact(w,v),-exact)
            self.assertEqual(chirality_exact(v,v),0)
            self.assertLessEqual(abs(float(exact)),GAMMA+1e-14)
        for n in (1000,4096):
            self.assertLess(abs(float(source_chirality(n))*n**5/16-1),.02)

    def test_hermitian_chirality_invariant_countermodels(self):
        constant=(Fraction(3),)*6
        self.assertEqual(chirality_exact(constant,constant),0)
        self.assertEqual(chirality_exact(source_block(0),source_block(0)),0)
        mutated=source_chirality(11,mutate=True)
        self.assertGreater(mutated,0)  # source chirality not unique to authentic four poles
        self.assertNotEqual(mutated,source_chirality(11))

    def test_bbp_omega4_omega5_diamond_source_exact(self):
        for n in (0,2,25,128):
            for seed in (Fraction(0),Fraction(-3,7)):
                self.assertEqual(grouped_fold(n,(2,2,2),seed),
                                 grouped_fold(n,(3,3),seed))

    def test_source_clock_prefix_not_pi_shift(self):
        # This p_L is pi/16, not pi; exact n-step carrier/tail contract.
        for L in (1, 3, 8, 17):
            p=bbp_prefix(L)
            self.assertEqual(16*p,sum((Q**j*source(j) for j in range(L)),Fraction()))
            u=Fraction()
            for n in range(L+1):
                tail=sum((Q**(j-n)*source(j-1) for j in range(n+1,L+1)),Fraction())
                self.assertEqual(u+tail,16**n*p)
                if n<L:
                    u=16*u+source(n)

    def test_phase_oracle_weyl_probability_control(self):
        for A in (2,4,8,16):
            L=2*A
            for h in (1,8,24):
                state=exact_rational_phase_state(A,L,h)
                mean,p=weyl_mean_and_zero_probability(state)
                self.assertLess(abs(p-abs(mean)**2),1e-13)
                self.assertLess(abs(p-abs(sum(state)/sqrt(A))**2),1e-13)
                self.assertGreaterEqual(p,0)
                self.assertLessEqual(p,1+1e-12)
            # Coherent rational wrong-seed shadow: completed phase identically zero.
            bad=exact_rational_phase_state(A,L,8,seed=-bbp_prefix(L))
            mean,p=weyl_mean_and_zero_probability(bad)
            self.assertAlmostEqual(abs(mean),1)
            self.assertAlmostEqual(p,1)

    def test_source_specific_phase_oracle_error_bound(self):
        for L in (1,2,4,8,16,32):
            trunc=bbp_prefix(L)
            further=bbp_prefix(L+40)
            for n in (0,1,L,L+1):
                observed=16**n*(further-trunc)
                self.assertGreater(observed,0)
                self.assertLess(observed,completed_phase_tail_bound(L,n))
        for A in (2,4,8,16):
            for h in (1,8,24):
                self.assertEqual(finite_phase_mean_error_bound(A, 2*A, h),
                                 Fraction(44, 7) * h * completed_phase_tail_bound(2*A, 2*A-1))
                self.assertLessEqual(finite_hadamard_probability_error_bound(A,2*A,h),1)
                if A>=8:
                    self.assertLess(finite_hadamard_probability_error_bound(A,2*A,h),.05)

    def test_phase_bound_beyond_float_range(self):
        mean_bound = finite_phase_mean_error_bound(2, 1000, 1)
        self.assertGreater(mean_bound, 0)
        self.assertEqual(float(mean_bound), 0.0)
        self.assertEqual(finite_hadamard_probability_error_bound(2, 1000, 1), 2 * mean_bound)

    def test_ancilla_dilation_restores_all_details(self):
        for n in (0,1,30):
            raw=tuple(complex(v) for v in source_block(n))
            for group in (2,3):
                lo,hi=coarse_instrument_isometry(raw,group)
                self.assertLess(max(abs(x-a-b) for x,a,b in zip(raw,lo,hi)),1e-14)
                self.assertAlmostEqual(sum(abs(x)**2 for x in raw),
                                       sum(abs(x)**2 for x in lo)+sum(abs(x)**2 for x in hi),
                                       places=13)
                self.assertGreater(sum(abs(x)**2 for x in hi),0)

    def test_heralded_echo_defect_signal_and_strength(self):
        for n in (0,1,10,1000,4096):
            v=source_block(n)
            p=heralded_minus_probability(v)
            self.assertEqual(p,energy(commutator(v))/(4*energy(v)))
            self.assertGreater(p,0)
            self.assertLess(p,Fraction(1,18)+Fraction(1,10**12))
            if n >= 1000:
                self.assertLess(abs(float(p)*n**2/(11/18)-1),.02)
        self.assertEqual(heralded_minus_probability((Fraction(1),)*6),0)

    def test_chirality_real_quantum_unitary_evolution(self):
        for seed in range(12):
            basis=tuple(1.+0j if k==seed else 0j for k in range(12))
            for t in (.01,1.0,2.0):
                forward=chirality_evolve(basis,t)
                backward=chirality_evolve(forward,-t)
                self.assertAlmostEqual(sum(abs(x)**2 for x in forward),1,places=12)
                self.assertLess(max(abs(a-b) for a,b in zip(backward,basis)),2e-13)

    def test_chirality_shot_variance_is_weaker_than_weyl(self):
        for n in (256,1000,4096):
            a,b=source_block(n),source_block(n+1)
            m=chirality_exact(a,b)
            second=chirality_second_moment(a,b)
            variance=second-m*m
            self.assertGreater(variance,0)
            if n>=1000:
                self.assertLess(abs(float(second)*n**2/(22/9)-1),.02)
                self.assertLess(abs(float(variance/m**2)/n**8/(11/1152)-1),.04)

    def test_mobius_phase_is_global_unless_referenced(self):
        # A single state's sign is globally invisible; an interferometric
        # control register makes the relative minus observable.
        for phi in (0.0,.3,2.1):
            state=(1/sqrt(2),exp(1j*phi)/sqrt(2))
            minus=(-state[0],-state[1])
            for a,b in zip(state,minus):
                self.assertAlmostEqual(abs(a)**2,abs(b)**2)
            # phase on only the path arm flips relative-ancilla X expectation
            before=2*(state[0].conjugate()*state[1]).real
            after=2*(state[0].conjugate()*(-state[1])).real
            self.assertAlmostEqual(before,-after)

    def test_branch_increment_monodromy_hadamard_control(self):
        for m in range(16):
            chi=branch_character_state(m)
            moved=branch_increment(chi)
            eigen=exp(-2j*pi*m/16)
            self.assertLess(max(abs(moved[k]-eigen*chi[k]) for k in range(16)),1e-13)
            p=controlled_increment_minus_probability(chi)
            self.assertAlmostEqual(p,abs(1-eigen)**2/4,places=13)
            self.assertGreaterEqual(p,0)
            self.assertLessEqual(p,1+1e-12)
        self.assertAlmostEqual(controlled_increment_minus_probability(branch_character_state(8)),1)
        self.assertAlmostEqual(controlled_increment_minus_probability(branch_character_state(0)),0)

    def test_explicit_five_qubit_controlled_increment_truth_table(self):
        for control in (0,1):
            for k in range(16):
                self.assertEqual(controlled_increment_gate_schedule(control,k),
                                 (k+control)%16)
        # The QASM gate schedule uses only controlled reversible bit-flips;
        # its parity-eigenphase test is already calibrated above.

    def test_no_cloning_hostile_inner_product(self):
        old_overlap=1/sqrt(2)             # <0|+>
        cloned_overlap=old_overlap**2    # <00|++>
        self.assertNotAlmostEqual(old_overlap,cloned_overlap)
        # exact contradiction to unitarity for a purported generic copier
        self.assertAlmostEqual(cloned_overlap,1/2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
