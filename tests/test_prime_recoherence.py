"""Exact hostile tests, including fake prime and independent-reservoir controls."""
from __future__ import annotations

import itertools
import unittest
from fractions import Fraction as Q

from observational_succ.prime_recoherence import (
    R90, RNEG90, IDENTITY, initial_bell_environment, rotate_shared_environment,
    density_ab, density_e, density_purity, bell_plus_fidelity, marker_overlap,
    purity_from_overlap, fidelity_from_overlap, independent_reservoir_overlap,
    phase_dephasing_step, minimum_normalized_purity, prime_power_label,
    prime_power_controlled_kick, ordered_event_recoherence,
)


class ExactRecoherenceTests(unittest.TestCase):
    def test_initial_joint_pure_and_individual_locals_mixed(self):
        state = initial_bell_environment()
        self.assertEqual(density_purity(density_ab(state)), 1)
        self.assertEqual(density_purity(density_e(state)), 1)
        self.assertEqual(marker_overlap(state), 1)
        self.assertEqual(bell_plus_fidelity(density_ab(state)), 1)
        # The *individual* A/B reduced states are I/2 already at preparation.
        rho = density_ab(state)
        self.assertEqual(rho[((0,0),(0,0))], Q(1,2))
        self.assertEqual(rho[((1,1),(1,1))], Q(1,2))
        self.assertEqual(rho[((0,0),(1,1))], Q(1,2))

    def test_shared_marker_decoherence_without_measurement(self):
        marked = rotate_shared_environment(initial_bell_environment(), 0, R90)
        self.assertEqual(marker_overlap(marked), 0)
        self.assertEqual(density_purity(density_ab(marked)), Q(1,2))
        self.assertEqual(density_purity(density_e(marked)), Q(1,2))
        self.assertEqual(bell_plus_fidelity(density_ab(marked)), Q(1,2))

    def test_coherent_uncompute_with_other_twin(self):
        state = initial_bell_environment()
        marked = rotate_shared_environment(state,0,R90)
        restored = rotate_shared_environment(marked,1,RNEG90)
        self.assertEqual(restored,state)
        self.assertEqual(density_purity(density_ab(restored)),1)
        self.assertEqual(density_purity(density_e(restored)),1)
        self.assertEqual(bell_plus_fidelity(density_ab(restored)),1)

    def test_periodic_purity_vs_bell_fidelity(self):
        state=initial_bell_environment()
        expected=((1,Q(1),Q(1)),(0,Q(1,2),Q(1,2)),(-1,Q(1),Q(0)),
                  (0,Q(1,2),Q(1,2)),(1,Q(1),Q(1)))
        for g,p,f in expected:
            self.assertEqual((marker_overlap(state),density_purity(density_ab(state)),
                              bell_plus_fidelity(density_ab(state))),(g,p,f))
            state=rotate_shared_environment(state,0,R90)

    def test_mismatch_same_observer_uncompute_exact(self):
        state=initial_bell_environment()
        marked=rotate_shared_environment(state,0,R90)
        self.assertEqual(rotate_shared_environment(marked,0,RNEG90),state)

    def test_invalid_rotation_mutation_rejected(self):
        with self.assertRaises(ValueError):
            rotate_shared_environment(initial_bell_environment(),0,((1,1),(0,1)))
        with self.assertRaises(ValueError):
            rotate_shared_environment(initial_bell_environment(),2,R90)

    def test_environment_norm_spectrum_identity_exhaustive_small(self):
        for control in (0,1):
            for matrix in (R90,RNEG90,IDENTITY):
                for s0,s1 in itertools.product((-2,-1,0,1,2),repeat=2):
                    if not (s0 or s1): continue
                    ray={(0,0,0):Q(s0),(1,1,0):Q(s1)}
                    after=rotate_shared_environment(ray,control,matrix)
                    self.assertEqual(density_purity(density_ab(ray)),density_purity(density_e(ray)))
                    self.assertEqual(density_purity(density_ab(after)),density_purity(density_e(after)))
                    self.assertEqual(sum(v*v for v in ray.values()),sum(v*v for v in after.values()))

    def test_overlap_formula_matches_partial_trace(self):
        state=initial_bell_environment()
        for _ in range(9):
            gamma=marker_overlap(state)
            self.assertEqual(density_purity(density_ab(state)),purity_from_overlap(gamma))
            self.assertEqual(bell_plus_fidelity(density_ab(state)),fidelity_from_overlap(gamma))
            state=rotate_shared_environment(state,0,R90)

    def test_no_zero_density_purity_finite_dim(self):
        self.assertEqual(minimum_normalized_purity(2),Q(1,2))
        self.assertEqual(minimum_normalized_purity(4),Q(1,4))
        self.assertGreater(minimum_normalized_purity(100000),0)
        with self.assertRaises(ValueError):minimum_normalized_purity(0)

    def test_orthogonal_independent_bucket_blocks_all_other_recoherence(self):
        for rest in itertools.product((-1,Q(-1,2),0,Q(1,3),1),repeat=3):
            gamma=independent_reservoir_overlap((Q(0),)+rest)
            self.assertEqual(gamma,0)
            self.assertEqual(purity_from_overlap(gamma),Q(1,2))

    def test_independent_bucket_product_and_phase_not_erase(self):
        self.assertEqual(independent_reservoir_overlap((Q(3,5),Q(-4,5))),Q(-12,25))
        self.assertEqual(purity_from_overlap(Q(-1)),1)
        self.assertEqual(fidelity_from_overlap(Q(-1)),0)
        with self.assertRaises(ValueError):independent_reservoir_overlap((2,))

    def test_positive_rate_markov_cannot_revive_gamma_zero(self):
        for q in (Q(0),Q(1,12),Q(1,4),Q(1,2)):
            self.assertEqual(phase_dephasing_step(Q(0),q),0)
            self.assertLessEqual(abs(phase_dephasing_step(Q(3,5),q)),Q(3,5))
        with self.assertRaises(ValueError):phase_dephasing_step(1,Q(-1,10))
        with self.assertRaises(ValueError):phase_dephasing_step(1,Q(3,4))

    def test_sign_only_not_physical_energy(self):
        self.assertEqual(purity_from_overlap(Q(3,5)),Q(17,25))
        self.assertEqual(fidelity_from_overlap(Q(3,5)),Q(4,5))
        self.assertEqual(purity_from_overlap(Q(-3,5)),Q(17,25))
        self.assertEqual(fidelity_from_overlap(Q(-3,5)),Q(1,5))


class PrimeSourceControls(unittest.TestCase):
    def test_genuine_prime_power_support(self):
        samples={1:None,2:(2,1),3:(3,1),4:(2,2),5:(5,1),6:None,7:(7,1),
                 8:(2,3),9:(3,2),10:None,12:None,16:(2,4),25:(5,2),
                 27:(3,3),49:(7,2),64:(2,6),121:(11,2),125:(5,3)}
        for n,wanted in samples.items():
            label=prime_power_label(n)
            self.assertEqual(None if label is None else (label.prime,label.exponent),wanted,n)
            if label:self.assertEqual(label.integer,n)

    def test_fake_six_fails_as_euler_place(self):
        with self.assertRaises(ValueError):
            prime_power_controlled_kick(initial_bell_environment(),6)
        with self.assertRaises(ValueError):
            prime_power_label(0)

    def test_prime_weight_symbolic_not_float(self):
        self.assertEqual(prime_power_label(8).formula,"log(2)/(2**(3/2))")
        self.assertEqual(prime_power_label(9).formula,"log(3)/(3**(2/2))")

    def test_selected_powers_preserve_no_statistical_source(self):
        # Four declared prime-power events cause the freely CHOSEN R90 gates
        # to return to |Phi+>. Nothing about Lambda weights is used.
        self.assertEqual(ordered_event_recoherence((2,3,4,5)),(1,1,1))
        self.assertEqual(ordered_event_recoherence((2,3)),(-1,1,0))
        self.assertEqual(ordered_event_recoherence((2,)),(0,Q(1,2),Q(1,2)))
        self.assertEqual(ordered_event_recoherence(()),(1,1,1))

    def test_composite_mutant_same_physics_but_wrong_arithmetic(self):
        same_gate_on_composite=rotate_shared_environment(initial_bell_environment(),0,R90)
        prime_gate=prime_power_controlled_kick(initial_bell_environment(),2)
        self.assertEqual(same_gate_on_composite,prime_gate)
        # This identity proves 'prime-labelled physical recoherence' is not
        # derivable from the gate alone; genuine-prime support is an extra rule.

    def test_orthogonality_after_independent_sectors_does_not_recover(self):
        self.assertEqual(purity_from_overlap(independent_reservoir_overlap((1,0,1))),Q(1,2))
        # A common reservoir can recover via two conditional rotations instead.
        marked=prime_power_controlled_kick(initial_bell_environment(),2)
        recovered=rotate_shared_environment(marked,1,RNEG90)
        self.assertEqual(density_purity(density_ab(recovered)),1)


if __name__ == '__main__':unittest.main()
