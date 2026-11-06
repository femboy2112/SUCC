"""Exact finite mechanisms for CFG-1/2; not a normality/asymptotic test.

Run: python research/2026-11-04/critical_chirp_source/front_cfg/probe.py
     python research/2026-11-04/critical_chirp_source/front_cfg/probe.py --receipt
Only the Python standard library is used. No pi digits or floating phases.
"""
from __future__ import annotations

from fractions import Fraction as F
import json
from pathlib import Path
import sys
import unittest


def forcing_four(n: int) -> F:
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def forcing_polynomial(n: int) -> F:
    return F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def tail_interval(n: int, count: int = 12) -> tuple[F, F]:
    lower = sum((forcing_four(n+k)/16**k for k in range(1, count+1)), F(0))
    # Positivity and monotonicity are analytically proved from the Mellin kernel.
    return lower, lower + forcing_four(n+count+1)/F(15*16**count)


def rounded_pocket(H: int, n: int) -> tuple[int, int]:
    value = F(15*H, 64*n*n)+F(1, 2)
    k = value.numerator//value.denominator
    return k, k % 15


def patch_digits(A: int, j: int, p: int = 5, reverse: bool = False):
    """Finite patch with arbitrary continuation; not claimed normal.

    The shorter m=A//4 is a finite component fixture, not the theorem's m_A.
    """
    H = 16**j
    m = A//4
    first = 2*A-m
    stop = 2*A+p
    digits = {}
    pockets = {}
    for n in range(first, stop):
        k, d = rounded_pocket(H, n)
        pockets[n] = (k, (-d) % 15 if reverse else d)
        digits[n+j+1] = pockets[n][1]
    size = stop+j
    # Other digits need no probabilistic property; all future tails are allowed.
    numerator = 0
    for position in range(1, size+1):
        filler = 1 if position == 1 else (7*position+3) % 16
        numerator = 16*numerator+digits.get(position, filler)
    y = (F(numerator)+F(1, 7))/16**size
    assert y < F(1, 8)  # Distinguishes this finite completion from pi/16 > 3/16.
    return y, pockets, first, 2*A, H


def tracking_receipt(A: int, j: int, p: int = 5, reverse: bool = False) -> dict:
    y, pockets, first, stop, H = patch_digits(A, j, p, reverse)
    good = []
    bad = []
    failed = []
    Lambda = F(H, A*A)
    eta = F(1, 30)+F(1, 16**p)+Lambda/F(64*A)
    for n in range(first, stop):
        k, d = pockets[n]
        if any(pockets[n+t][1] != d for t in range(p)):
            bad.append(n)
            continue
        good.append(n)
        x = (16**(n+j)*y) % 1
        # An independent arithmetic route to the same selected high character.
        assert x == (H*((16**n*y) % 1)) % 1
        assert abs(x-F(d, 15)) <= F(1, 16**p)
        low, high = tail_interval(n)
        # For the reversed control choose its nearest integer independently.
        center = x-F(H, 64*n*n)
        nearest = (center+F(1, 2)).numerator//(center+F(1, 2)).denominator
        left = x-H*high-nearest
        right = x-H*low-nearest
        if not (-eta <= left <= right <= eta):
            failed.append(n)
    switches = sum(pockets[n][1] != pockets[n+1][1]
                   for n in range(first, stop+p-1))
    budget = p*(F(15)*Lambda*(stop-first+p)/F(32*A)+1)
    assert len(bad) <= p*switches
    assert len(bad) <= budget
    return {"A": A, "j": j, "H": H, "Lambda": str(Lambda),
            "p": p, "m": stop-first, "good": len(good), "bad": len(bad),
            "switches": switches, "bad_budget": str(budget),
            "eta_cycles": str(eta), "failed_certificates": failed,
            "control": "reversed_digit_orientation" if reverse else "aligned_digits"}


def finite_receipt() -> dict:
    tail_cases = []
    for A, Lambda in ((191, 137), (509, 257), (911, 509)):
        n = 2*A-A//4
        low, high = tail_interval(n)
        model = F(1, 64*n*n)
        error = F(1, 64*n*n*n)
        assert model-error < low < high < model
        H = A*A*Lambda
        k, d = rounded_pocket(H, n)
        assert abs(F(k, 15)-F(H, 64*n*n)) <= F(1, 30)
        tail_cases.append({"A": A, "Lambda_surrogate": Lambda, "n": n,
                           "tail_width": str(high-low), "pocket": d,
                           "source_tail_sandwich": True})
    aligned = [tracking_receipt(A, j) for A, j in ((191, 5), (509, 6), (911, 7))]
    reversed_cases = [tracking_receipt(A, j, reverse=True)
                      for A, j in ((191, 5), (509, 6), (911, 7))]
    assert all(not r["failed_certificates"] for r in aligned)
    assert any(r["failed_certificates"] for r in reversed_cases)
    return {"authority": "finite exact-rational component certificates only",
            "normality_proof": "paper density-zero argument, not this receipt",
            "critical_schedule": "not tested by these surrogate/radix component cases",
            "tail_and_rounding": tail_cases,
            "aligned": aligned, "reversed": reversed_cases}


class MechanismTests(unittest.TestCase):
    def test_independent_source_formulas(self):
        for n in (1, 2, 3, 7, 32, 64, 137, 191, 257, 509, 911):
            self.assertEqual(forcing_four(n), forcing_polynomial(n))

    def test_exact_tail_brackets(self):
        for n in (137, 191, 257, 509, 911):
            low, high = tail_interval(n)
            self.assertLess(F(1, 64*n*n)-F(1, 64*n*n*n), low)
            self.assertLess(high, F(1, 64*n*n))

    def test_local_half_turn_taylor_bound(self):
        # Independently check the explicit bound from g''(u)<=3/32 on [1,2].
        for Lambda in (137, 257, 509):
            for t in (F(0), F(1, 3), F(17), F(64), F(128)):
                exact = F(Lambda, 64)/(2-t/Lambda)**2
                linear = F(Lambda, 256)+t/256
                self.assertLessEqual(abs(exact-linear), F(3, 64)*t*t/Lambda)

    def test_rounding_and_literal_radix_transport(self):
        for A, j in ((191, 5), (509, 6), (911, 7)):
            row = tracking_receipt(A, j)
            self.assertGreater(row["good"], 0)
            self.assertFalse(row["failed_certificates"])

    def test_wrong_orientation_is_rejected(self):
        rows = [tracking_receipt(A, j, reverse=True)
                for A, j in ((191, 5), (509, 6), (911, 7))]
        self.assertTrue(any(r["failed_certificates"] for r in rows))

    def test_zero_digit_tail_bound(self):
        # Arbitrary exact continuations are bounded after p leading zero digits.
        for p in (1, 5, 13):
            for continuation in (F(0), F(1, 7), F(999, 1000)):
                residual = continuation/16**p
                self.assertLessEqual(residual, F(1, 16**p))

    def test_receipt_is_deterministic(self):
        self.assertEqual(finite_receipt(), finite_receipt())


if __name__ == "__main__":
    if sys.argv[1:] == ["--receipt"]:
        print(json.dumps(finite_receipt(), sort_keys=True, indent=2))
    elif sys.argv[1:] == ["--verify"]:
        expected = json.loads(Path(__file__).with_name("FINITE_RECEIPT.json").read_text())
        assert finite_receipt() == expected
        print("CFG_FINITE_RECEIPT_VERIFIED")
    else:
        unittest.main()
