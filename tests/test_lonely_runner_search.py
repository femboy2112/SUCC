"""A Fraction-based constructor checked by a separate integer-only verifier."""
from fractions import Fraction as F
import unittest

from observational_succ.lonely_runner_search import (
    bcs_five_configuration, cover_certificate, poliakova_configuration,
)
from observational_succ.lonely_runner_verify import (
    CertificateError, exact_maxmin, payload_digest, verify_cover,
)


class LonelyRunnerSearchTests(unittest.TestCase):
    def test_published_five_runner_control(self):
        v, s, d = bcs_five_configuration()
        c = cover_certificate(v, s, d, source={"reference": "BCS v4 Fig. 1"})
        self.assertEqual(verify_cover(c)["checked_intervals"], 11)
        self.assertEqual(exact_maxmin(v, c["shifts"])["gamma"], [15, 94])

    def test_published_uniform_control_at_threshold(self):
        v, s, d = poliakova_configuration(96)
        self.assertEqual(len(v), 95)
        c = cover_certificate(v, s, d, source={"reference": "Poliakova v1 Theorem 7"})
        result = verify_cover(c)
        self.assertTrue(result["strict_shifted_counterexample"])
        self.assertEqual(result["delta"], [1, 97])
        self.assertLess(result["checked_intervals"], sum(v))

    def test_source_mutation_with_recomputed_hash_is_rejected(self):
        c = cover_certificate(*bcs_five_configuration(), source={"reference": "control"})
        c["shifts"][0] = [1, 100]
        c["payload_sha256"] = payload_digest(c)
        with self.assertRaises(CertificateError):
            verify_cover(c)

    def test_corrupt_generator_chain_is_rejected(self):
        c = cover_certificate(*bcs_five_configuration(), source={"reference": "control"})
        old = F(*c["intervals"][3]["left"])
        forged = old + F(1, 10**20)
        c["intervals"][3]["left"] = [forged.numerator, forged.denominator]
        c["payload_sha256"] = payload_digest(c)
        with self.assertRaises(CertificateError):
            verify_cover(c)

    def test_noncover_is_not_generated(self):
        with self.assertRaisesRegex(ValueError, "uncovered"):
            cover_certificate([1, 2, 3], [0, 0, 0], F(1, 5), source={"type": "negative"})

    def test_weak_cover_does_not_become_a_strict_counterexample(self):
        c = cover_certificate([1, 2, 3], [0, 0, 0], F(1, 4), source={"type": "tight"})
        self.assertTrue(verify_cover(c, require_counterexample=False)["all_time_cover"])
        with self.assertRaisesRegex(CertificateError, "strictly"):
            verify_cover(c)

    def test_exact_input_contract_and_published_cutoff(self):
        for args in (([1, 1], [0, 0], F(1, 3)), ([1], [0.0], F(1, 3)),
                     ([True], [0], F(1, 3)), ([1], [0], 0.3)):
            with self.assertRaises(ValueError):
                cover_certificate(*args, source={"type": "invalid"})
        with self.assertRaises(ValueError):
            cover_certificate([1], [0], F(1, 3))
        with self.assertRaises(ValueError):
            poliakova_configuration(95)


if __name__ == "__main__":
    unittest.main()
