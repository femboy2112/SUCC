"""Collision guard for the claim-namespace registry.

Pins the resolved PH collision, the shape of the registry, and -- most importantly
-- that no cross-file bare-prefix collision is left unregistered. The last assertion
is the live guard: it passes today and fails the moment a future PR mints a new
bare prefix in two supplement files without recording it in the registry. A quiet
namespace collision is exactly the kind of thing that rots a proof-extraction keyspace
from the inside, so we close the incision with a test, not a promise.
"""

import unittest
from pathlib import Path

from observational_succ.claim_namespaces import (
    REGISTRY_PATH,
    fqid,
    load_registry,
    scan_supplement_prefixes,
    unregistered_prefix_collisions,
)

_REPO_ROOT = REGISTRY_PATH.parent.parent


class RegistryShapeTests(unittest.TestCase):
    def test_registry_loads_and_schema_version(self):
        registry = load_registry()
        self.assertEqual(registry["schema_version"], 1)
        self.assertEqual(registry["RH_PROVED"], "NO")

    def test_every_supplement_file_exists_on_disk(self):
        registry = load_registry()
        for entry in registry["namespaces"]:
            for rel_path in entry["supplement_files"]:
                self.assertTrue(
                    (_REPO_ROOT / rel_path).is_file(),
                    f"registry references missing supplement file: {rel_path}",
                )


class PhCollisionTests(unittest.TestCase):
    def test_ph_resolved_collision_entry(self):
        registry = load_registry()
        ph_entries = [
            rc for rc in registry["resolved_collisions"] if rc["bare_prefix"] == "PH"
        ]
        self.assertEqual(len(ph_entries), 1, "exactly one PH resolved_collisions entry expected")
        self.assertEqual(
            set(ph_entries[0]["namespaces"]),
            {"PROFINITE_HILBERT", "PRIME_FORM_HEAT"},
        )

    def test_ph_fqids_are_distinct(self):
        self.assertEqual(fqid("PROFINITE_HILBERT", "PH-01"), "PH.PROF-01")
        self.assertEqual(fqid("PRIME_FORM_HEAT", "PH-01"), "PH.PFH-01")

    def test_bare_ph01_disambiguates_not_merges(self):
        # The regression that matters: one bare ID, two meanings, two FQIDs.
        prof = fqid("PROFINITE_HILBERT", "PH-01")
        pfh = fqid("PRIME_FORM_HEAT", "PH-01")
        self.assertNotEqual(prof, pfh)

    def test_unknown_namespace_raises(self):
        with self.assertRaises(KeyError):
            fqid("NO_SUCH_NAMESPACE", "PH-01")


class GuardTests(unittest.TestCase):
    def test_no_unregistered_prefix_collisions(self):
        # Live future-collision guard. Empty today; must stay empty.
        self.assertEqual(unregistered_prefix_collisions(), [])

    def test_census_sees_ph_in_two_files(self):
        census = scan_supplement_prefixes()
        self.assertIn("PH", census)
        self.assertEqual(
            set(census["PH"]),
            {
                "docs/CLAIM_SUPPLEMENT_PRIME_FORM_HEAT.md",
                "docs/CLAIM_SUPPLEMENT_PROOF_TEETH.md",
            },
        )


if __name__ == "__main__":
    unittest.main()
