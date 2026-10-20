"""Historical hyphenated claims must be addressable without minting fake claims."""
import unittest
from observational_succ.claim_namespaces import fqid, load_registry, scan_supplement_prefixes


class AcademicVIINamespaces(unittest.TestCase):
    def test_existing_hyphenated_claims(self):
        self.assertEqual(fqid("ABC_CLOCK_GREEN_TAO", "ABC-CLK-01"), "ABC-CLK-01")
        self.assertEqual(fqid("CLOUD_ABC", "CLOUD-ABC-05"), "CLOUD-ABC-05")
        self.assertIn("CLOUD-ABC", scan_supplement_prefixes())

    def test_nonexistent_claims_and_wrong_family_rejected(self):
        for namespace, bare in [("CLOUD_ABC", "CLOUD-ABC-99"),
                                ("CLOUD_ABC", "ABC-CLK-01"),
                                ("ACADEMIC_MAIN_VII", "AMVII-99")]:
            with self.subTest(namespace=namespace, bare=bare), self.assertRaises(ValueError):
                fqid(namespace, bare)

    def test_namespace_and_qualified_prefix_uniqueness(self):
        entries = load_registry()["namespaces"]
        for key in ("namespace", "fq_prefix"):
            values = [x[key] for x in entries]
            self.assertEqual(len(values), len(set(values)))
