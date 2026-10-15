"""Exact arithmetic tests for carrier-locked affine Markov rigidity."""
import unittest
from fractions import Fraction as Q
from observational_succ.carrier_locked_rigidity import (
    CarrierRigidityError, distribution, shifted_noise_kernel,
    affine_stability_certificate, sharp_chain_noise,
    cyclic_uniform_control, gaussian_mix_control,
)


class CarrierLockedRigidityTests(unittest.TestCase):
    def test_ideal_carrier_is_an_exact_fixed_point(self):
        for p in (2, 3, 5, 6):  # Composite 6: affine symmetry != primality
            laws = shifted_noise_kernel({0: Q(1)}, p)
            r = affine_stability_certificate(laws, p, 12, p)
            self.assertTrue(r["exact_affine_covariance"])
            self.assertTrue(r["identity_for_this_kernel"])
            self.assertEqual(r["target_TV"], "0")
            self.assertFalse(r["RH_proved"])

    def test_sharp_fractional_defect_chains(self):
        for p, r, alpha in ((2, 3, Q(3, 4)), (3, 2, Q(2, 5)),
                            (2, 4, Q(1, 2)), (5, 2, Q(1))):
            noise, B = sharp_chain_noise(p, r, alpha)
            c = affine_stability_certificate(shifted_noise_kernel(noise, p), p, B, p)
            self.assertEqual(Q(c["successor_TV_max"]), 0)
            self.assertEqual(Q(c["dilation_TV"]), alpha/r)
            self.assertEqual(Q(c["nonzero_noise_within_B"]), alpha)
            self.assertEqual(Q(c["affine_window_bound"]), alpha)
            self.assertEqual(Q(c["target_TV"]), alpha)

    def test_tail_not_silently_set_to_zero(self):
        laws = shifted_noise_kernel({0: Q(1, 2), 1: Q(1, 4),
                                     16: Q(1, 4)}, 2)
        c = affine_stability_certificate(laws, 2, 2, 2)
        self.assertEqual(Q(c["noise_tail"]), Q(1, 4))
        self.assertLessEqual(Q(c["target_TV"]), Q(c["target_TV_bound"]))

    def test_imperfect_successor_transport(self):
        laws = {1: {1: Q(1)}, 2: {2: Q(3, 4), 3: Q(1, 4)}}
        c = affine_stability_certificate(laws, 2, 1, 2)
        self.assertEqual(Q(c["successor_TV_max"]), Q(1, 4))
        self.assertEqual(Q(c["dilation_TV"]), Q(1, 4))
        self.assertEqual(Q(c["affine_defect"]), Q(1, 2))

    def test_exhaustive_small_laws_independent_inequality(self):
        vectors = []
        for i in range(4):
            for j in range(i, 4):
                law = {k: Q((k == i) + (k == j), 2) for k in range(4)}
                vectors.append({k + 1: v for k, v in law.items() if v})
        self.assertEqual(len(vectors), 10)
        for u in vectors:
            for v in vectors:
                c = affine_stability_certificate({1: u, 2: v}, 2, 3, 2)
                e1 = sum((abs(v.get(k, Q()) - u.get(k - 1, Q()))
                          for k in set(v) | {x + 1 for x in u}), Q())/2
                e2 = sum((abs(v.get(k, Q()) -
                              u.get(k//2, Q())*(k%2 == 0))
                          for k in set(v) | {2*x for x in u}), Q())/2
                self.assertEqual(Q(c["successor_TV_max"]), e1)
                self.assertEqual(Q(c["dilation_TV"]), e2)
                self.assertLessEqual(Q(c["nonzero_noise_within_B"]),
                                     Q(c["affine_window_bound"]))

    def test_finite_cyclic_holes(self):
        for m, p in ((5, 2), (7, 3), (11, 6), (9, 2)):
            c = cyclic_uniform_control(m, p)
            self.assertTrue(c["source_action_covariant"])
            self.assertTrue(c["not_identity"])
        with self.assertRaises(CarrierRigidityError):
            cyclic_uniform_control(6, 2)

    def test_gaussian_state_change_not_carrier_equivalence(self):
        r = gaussian_mix_control()
        self.assertEqual(r["first_scale_moment"], "413/188")
        self.assertEqual(r["second_scale_moment"], "5477/752")
        self.assertEqual(r["observable_variance"], "43425/17672")
        self.assertEqual(r["successor_commutator_coordinate"], "-225/188")
        self.assertEqual(r["Mellin_distortion_s2"], "413/188")
        self.assertTrue(r["altered_test_is_valid_state"])
        self.assertFalse(r["underlying_arithmetic_changed"])

    def test_reject_float_ghost_mass_or_missing_history(self):
        for law in ({1: 0.5, 2: 0.5}, {1: Q(-1), 2: Q(2)},
                    {0: Q(1)}, {1: Q(1, 2)}, {}):
            with self.assertRaises(CarrierRigidityError):
                distribution(law)
        with self.assertRaises(CarrierRigidityError):
            affine_stability_certificate({1: {1: Q(1)}}, 3, 5)
        with self.assertRaises(CarrierRigidityError):
            sharp_chain_noise(2, 2, 0.8)


if __name__ == "__main__":
    unittest.main()
