"""Main XXI precision-isolation regression for observational_succ.gram_mobius.

The module used to run ``mp.mp.dps = 50`` at import time, so merely importing the library
raised the global precision of the whole process (measured 15 -> 50).  The identities are
now evaluated at 50 digits inside each call, with values bit-identical to the historical
evaluation.

Verified at integration against the old module: the import test FAILS there and the
bit-identity test ERRORS (no scoped wrapper).  The ambient-precision test is a behaviour
check only: a sweep of ambient dps 5..300 found NO precision at which the old
``single_clock_optimum`` returned False (log2/2 and log2/4 are exact binary scalings), so
no order-dependence of that test is claimed.  Inside the full suite the import-time effect
was also masked, because tests/test_gram_mobius.py sets dps=50 itself on import.
"""
import subprocess
import sys
import unittest

import mpmath as mp

from observational_succ import gram_mobius as gm


class GramMobiusPrecisionIsolation(unittest.TestCase):
    def test_import_does_not_change_global_precision(self):
        code = ("import mpmath; before = mpmath.mp.prec; "
                "import observational_succ.gram_mobius; "
                "print(before, mpmath.mp.prec)")
        out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
        before, after = out.stdout.split()
        self.assertEqual(before, after)

    def test_identity_decided_at_module_precision_whatever_the_ambient(self):
        for ambient in (15, 30, 120):
            with mp.workdps(ambient):
                r = gm.single_clock_optimum()
                self.assertEqual(mp.mp.dps, ambient)
            self.assertTrue(r["E_2_star_is_1_minus_log2"], ambient)

    def test_values_bit_identical_to_the_historical_50_digit_evaluation(self):
        for m, n in ((2, 2), (2, 3), (3, 5)):
            with mp.workdps(15):
                scoped = gm.gram(m, n)
            with mp.workdps(50):
                historical = gm.gram.__wrapped__(m, n)
            self.assertEqual(scoped, historical)
        with mp.workdps(15):
            s = gm.S_r(12, 5)
        with mp.workdps(50):
            self.assertEqual(s, gm.S_r.__wrapped__(12, 5))


if __name__ == "__main__":
    unittest.main()
