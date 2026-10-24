"""Compatibility-surface test for the BBP minimal-path shim.

Guards the scoped compat surface created when PRs #260 and #261's independent
``bbp_minimal_path`` implementations were split into two canonical modules during
the coherent-main integration. It does NOT re-test either family's mathematics
(that stays in ``test_bbp_minimal_path_gauge`` and ``test_bbp_minimal_path_births``);
it only verifies that the shim re-exports both families, keeps the two private
``_prime`` domains apart, and keeps the public names disjoint so a future addition
to either family cannot silently shadow a symbol in the other.
"""
import unittest

from observational_succ import bbp_minimal_path as shim
from observational_succ import bbp_minimal_path_births as births
from observational_succ import bbp_minimal_path_gauge as gauge


class ShimSurface(unittest.TestCase):
    def test_family_namespaces_reachable(self):
        self.assertIs(shim.gauge, gauge)
        self.assertIs(shim.births, births)

    def test_gauge_public_symbols_reexported(self):
        for name in (
            "single_missing_prime_counterfeit",
            "period_phase",
            "nearest_integer",
            "circle_distance",
            "is_prime_power_denominator",
            "rational_target_proxy",
        ):
            self.assertTrue(hasattr(shim, name), name)
            self.assertIs(getattr(shim, name), getattr(gauge, name))

    def test_births_public_symbols_reexported(self):
        for name in (
            "prime_births_through",
            "prime_power_first_birth",
            "rational_first_order_impossibility",
            "counterfeit_selected_state",
            "finite_prime_support_no_go",
        ):
            self.assertTrue(hasattr(shim, name), name)
            self.assertIs(getattr(shim, name), getattr(births, name))

    def test_private_prime_not_exported(self):
        self.assertNotIn("_prime", getattr(shim, "__all__", []))
        self.assertFalse(hasattr(shim, "_prime"))

    def test_two_prime_domains_stay_distinct(self):
        # #260 gauge permits the even prime 2 (a missing prime may be 2).
        self.assertEqual(gauge._prime(2), 2)
        # #261 births requires an odd rational prime p >= 3; 2 is rejected.
        with self.assertRaises(ValueError):
            births._prime(2)

    def test_public_apis_disjoint(self):
        def public(mod):
            return {
                name
                for name, value in vars(mod).items()
                if callable(value)
                and not name.startswith("_")
                and getattr(value, "__module__", None) == mod.__name__
            }

        self.assertEqual(
            public(gauge) & public(births),
            set(),
            "gauge/births public APIs must stay disjoint for the flat shim to be safe",
        )


if __name__ == "__main__":
    unittest.main()
