"""Exact affine normalizer controls, full finite oracles and mutated sources."""
import random
import unittest
from observational_succ.finite_affine_presentation import (
    AffinePresentationError, AffineMap, normalize_word, evaluate_direct,
    two_probe_certificate,
)


class AffinePresentationTests(unittest.TestCase):
    def test_normalizer_against_direct_source(self):
        rng = random.Random(1015)
        for _ in range(200):
            word = tuple(("S", rng.randint(0, 9)) if rng.randrange(2) else
                         ("V", rng.choice((2, 3, 5, 7))) for _ in range(rng.randrange(9)))
            nf = normalize_word(word)
            for x in (0, 1, 2, 5, 30):
                self.assertEqual(nf.evaluate(x), evaluate_direct(word, x))
        self.assertEqual(normalize_word(()), AffineMap(1, 0))

    def test_succ_fucc_relation_and_finite_compatibility(self):
        for p in (2, 3, 5, 7, 11):
            self.assertEqual(normalize_word((("S", 1), ("V", p))),
                             normalize_word((("V", p), ("S", p))))
        for n in range(2, 20):
            c = two_probe_certificate((("S", n),), (), n, source_id="s", epoch=0)
            self.assertTrue(c["equal_on_entire_finite_affine_carrier"])
            self.assertFalse(c["equal_as_source_N_maps"])

    def test_two_probes_complete_and_irredundant(self):
        for n in range(2, 25):
            a = two_probe_certificate((), (("V", 2),), n, source_id="s", epoch=0)
            self.assertEqual(a["separating_probe"], 1)  # agree at 0
            b = two_probe_certificate((), (("V", 2), ("S", n-1)), n,
                                      source_id="s", epoch=0)
            self.assertEqual(b["separating_probe"], 0)  # agree at 1
        rng = random.Random(4815)
        for _ in range(300):
            n = rng.randint(2, 20)
            w1 = tuple(("S", rng.randint(0, 9)) if rng.randrange(2) else
                       ("V", rng.choice((2, 3, 5))) for _ in range(rng.randrange(5)))
            w2 = tuple(("S", rng.randint(0, 9)) if rng.randrange(2) else
                       ("V", rng.choice((2, 3, 5))) for _ in range(rng.randrange(5)))
            got = two_probe_certificate(w1, w2, n, source_id="s", epoch=1)
            f, g = normalize_word(w1), normalize_word(w2)
            self.assertEqual(got["equal_on_entire_finite_affine_carrier"],
                             all(f.evaluate(x) % n == g.evaluate(x) % n for x in range(n)))

    def test_controls(self):
        for bad in ((("V", 6),), (("V", 1),), (("S", -1),),
                    (("S", True),), (("V", 2.0),)):
            with self.assertRaises(AffinePresentationError):
                normalize_word(bad)
        for n, source, epoch in ((1, "s", 0), (0, "s", 0), (2, "", 0),
                                 (2, "s", -1), (2, "s", True)):
            with self.assertRaises(AffinePresentationError):
                two_probe_certificate((), (), n, source_id=source, epoch=epoch)
        with self.assertRaises(AffinePresentationError):
            normalize_word((("M", 2),))
        with self.assertRaises(AffinePresentationError):
            normalize_word((("S",),))
        with self.assertRaises(AffinePresentationError):
            normalize_word((("V", 2),) * 129)


if __name__ == "__main__":
    unittest.main()
