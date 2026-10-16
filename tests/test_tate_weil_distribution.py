"""Exact source gates and numerical cross-oracles; no numeric sign proof."""
import unittest
from fractions import Fraction as Q

import mpmath as mp

from observational_succ.completed_weil_transport import (
    accelerated_arch_c2_remainder_bound, arch_ladder_remainder_bound,
    compact_weil_tent, tent_convolution,
)
from observational_succ.tate_weil_distribution import (
    TateWeilSource, evaluate_compact_numeric,
    pointwise_negative_bump_certificate,
)


class ExactWeilSourceTests(unittest.TestCase):
    def test_upstream_tate_provenance_adapter(self):
        from observational_succ.tate_idelic_zeta import StandardTateSource
        from observational_succ.tate_chi4 import Chi4TateSource
        for source, name in ((StandardTateSource("event-a", 7), "zeta"),
                             (Chi4TateSource("event-b", 11), "chi4")):
            target = TateWeilSource.from_tate(source)
            self.assertEqual(target.character, name)
            self.assertEqual((target.source_id, target.epoch),
                             (source.source_id, source.epoch))
        with self.assertRaises(ValueError):
            TateWeilSource.from_tate({"character": "zeta"})

    def test_signed_atoms_against_trial_factorization(self):
        for name in ("zeta", "chi4"):
            source = TateWeilSource(name)
            for R in (Q(1, 3), Q(7, 4), Q(3)):
                ceiling = 3**(-((-R.numerator)//R.denominator))
                expected = []
                for n in range(2, ceiling):
                    factors = []
                    d, m = 2, n
                    while d*d <= m:
                        while m % d == 0:
                            factors.append(d)
                            m //= d
                        d += 1
                    if m > 1:
                        factors.append(m)
                    chi = 1 if name == "zeta" else (0, 1, 0, -1)[n % 4]
                    if len(set(factors)) == 1 and chi:
                        expected.append((n, factors[0], chi))
                self.assertEqual(source.atoms(R), tuple(expected))
                self.assertTrue(source.verify_tape(R, tuple(expected)))

    def test_mutations_fail_in_actual_tape(self):
        source = TateWeilSource("chi4")
        tape = source.atoms(3)
        self.assertIn((3, 3, -1), tape)
        self.assertIn((9, 3, 1), tape)
        mutants = [tape[1:], tape+((6, 6, 1),), tape+(tape[-1],),
                   tuple((n, p, -1 if n == 9 else c) for n, p, c in tape),
                   tuple((n, n, c) for n, p, c in tape)]
        for mutant in mutants:
            with self.assertRaises(ValueError):
                source.verify_tape(3, mutant)

    def test_normalization_contract_and_mutants(self):
        for name in ("zeta", "chi4"):
            source = TateWeilSource(name)
            args = dict(conductor=source.conductor, parity=source.parity,
                        half_density=Q(1, 2),
                        pole_multiplicity=source.pole_multiplicity, root_number=1)
            self.assertTrue(source.require_normalization(**args))
            for field, bad in (("conductor", 5), ("parity", 1-source.parity),
                               ("half_density", Q(1, 3)),
                               ("pole_multiplicity", 1-source.pole_multiplicity),
                               ("root_number", -1)):
                with self.assertRaises(ValueError):
                    source.require_normalization(**{**args, field: bad})

    def test_inherited_gamma_bounds_exact_compatibility(self):
        source = TateWeilSource()
        for J in (1, 3, 16, 101):
            self.assertEqual(source.gamma_tail(J, M0=2, M1=3),
                             arch_ladder_remainder_bound(8, J))
            self.assertEqual(source.accelerated_gamma_tail(J, M0=2, M2=7),
                             accelerated_arch_c2_remainder_bound(2, 7, J))
            odd = TateWeilSource("chi4")
            self.assertLess(odd.gamma_tail(J, M0=2, M1=3),
                            source.gamma_tail(J, M0=2, M1=3))

    def test_continuity_budget_is_cofinal_and_homogeneous(self):
        for name in ("zeta", "chi4"):
            source = TateWeilSource(name)
            small = source.continuity_budget(1, delta0=Q(1, 7), delta1=Q(1, 11))
            self.assertIsInstance(small, Q)
            self.assertGreater(small, 0)
            self.assertEqual(source.continuity_budget(1, delta0=Q(3, 7),
                             delta1=Q(3, 11)), 3*small)
            self.assertGreater(source.continuity_budget(2, delta0=Q(1, 7),
                               delta1=Q(1, 11)), small)
            self.assertEqual(source.continuity_budget(1, delta0=0, delta1=0), 0)

    def test_authentic_pointwise_positivity_refutation_is_rational(self):
        r = pointwise_negative_bump_certificate()
        self.assertEqual(r["strict_Weil_upper"], -Q(19, 75))
        self.assertLess(r["strict_Weil_upper"], 0)
        self.assertFalse(r["autocorrelation_test"])
        self.assertFalse(r["RH_proved"])
        with self.assertRaises(ValueError):
            pointwise_negative_bump_certificate(Q(1, 2))

    def test_bad_inputs_not_silently_coerced(self):
        for name in ("nonEuler", "chi3", ""):
            with self.assertRaises(ValueError):
                TateWeilSource(name)
        for args in ((0, 1, 1), (True, 1, 1), (2, -1, 1), (2, 1.0, 1)):
            with self.assertRaises(ValueError):
                TateWeilSource().gamma_tail(args[0], M0=args[1], M1=args[2])
        with self.assertRaises(ValueError):
            TateWeilSource(epoch=True)


class NumericalCrossOracleTests(unittest.TestCase):
    def test_existing_complete_tent_adapter(self):
        for a in (Q(2, 5), Q(1)):
            old = compact_weil_tent(a, J=4, dps=35)
            new = evaluate_compact_numeric(TateWeilSource(),
                    lambda x: tent_convolution(x, a), 2*a,
                    knots=(a,), J=4, dps=35)
            for field, oldfield in (("pole", "pole"), ("prime", "prime"),
                                    ("gamma", "arch_ladder"), ("value", "q_ladder")):
                self.assertLess(abs(new[field]-old[oldfield]), mp.mpf("1e-28"))
            self.assertFalse(new["quadrature_certified"])

    def test_even_polynomial_family_gamma_tail_and_odd_cancellation(self):
        # C_c^3 family beyond the inherited tent. Exact M2<=56/R².
        with mp.workdps(35):
            for name in ("zeta", "chi4"):
                source = TateWeilSource(name)
                for R in (Q(3, 4), Q(5, 4)):
                    rr = mp.mpf(R.numerator)/R.denominator
                    def bump(x):
                        return (1-(x/rr)**2)**4 if abs(x) < rr else mp.mpf(0)
                    full = evaluate_compact_numeric(source, bump, R, dps=35)
                    part = evaluate_compact_numeric(source, bump, R, J=5, dps=35)
                    a = 10+source.alpha
                    corrected = part["value"]-mp.mpf(a.denominator)/(2*a.numerator)
                    err = source.accelerated_gamma_tail(5, M0=1, M2=56/R**2)
                    self.assertLess(abs(corrected-full["value"]),
                                    mp.mpf(err.numerator)/err.denominator)
                    odd = evaluate_compact_numeric(source, lambda x: x*bump(x), R,
                                                   J=3, dps=35)
                    self.assertEqual(odd["value"], 0)
                    if name == "chi4":
                        self.assertEqual(full["pole"], 0)


if __name__ == "__main__":
    unittest.main()
