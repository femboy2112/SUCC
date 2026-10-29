"""Independent certificate attacks and a second exact optimization algorithm."""
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import gcd
import random
import unittest

from observational_succ.lonely_runner_verify import (
    CandidateBudgetExceeded, CertificateError, exact_maxmin, verify_cover,
)


def pair(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def resign(c):
    payload = {k: v for k, v in c.items() if k != "payload_sha256"}
    c["payload_sha256"] = hashlib.sha256(json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
        allow_nan=False).encode()).hexdigest()
    return c


def certificate(v, shifts, delta, chain=None):
    """Test-only Fraction arc enumeration; independent of production generator."""
    shifts, delta = list(map(Q, shifts)), Q(delta)
    if chain is None:
        arcs = []
        for i, speed in enumerate(v):
            for winding in range(-1, speed + 3):
                left = max(Q(0), (winding - shifts[i] - delta) / speed)
                right = min(Q(1), (winding - shifts[i] + delta) / speed)
                if left <= right:
                    arcs.append((i, winding, left, right))
        chain, frontier = [], Q(0)
        while frontier < 1:
            available = [a for a in arcs if a[2] <= frontier < a[3]]
            if not available:
                raise ValueError("test fixture does not cover")
            chosen = max(available, key=lambda a: a[3])
            chain.append(chosen)
            frontier = chosen[3]
    intervals, inequalities, frontier = [], [], Q(0)
    for i, k, left, right in chain:
        left, right = Q(left), Q(right)
        intervals.append({"runner": i, "winding": k,
                          "left": pair(left), "right": pair(right)})
        inequalities.append({"left_cross": left.numerator * frontier.denominator,
                             "right_cross": frontier.numerator * left.denominator})
        frontier = right
    common = 0
    for speed in v:
        common = gcd(common, speed)
    return resign({"schema": "SUCC-shifted-cover-v1", "n": len(v),
                   "velocities": v, "shifts": list(map(pair, shifts)),
                   "delta": pair(delta), "threshold": [1, len(v) + 1],
                   "velocity_gcd": common, "source": {"fixture": "independent test"},
                   "intervals": intervals, "ordering": list(range(len(intervals))),
                   "inequalities": inequalities})


def bcs5():
    return certificate([1, 2, 3, 4, 5],
                       [Q(0), Q(46, 94), Q(38, 94), Q(47, 94), Q(72, 94)],
                       Q(15, 94))


def distance(x):
    residue = x % 1
    return min(residue, 1 - residue)


def cell_arrangement_gamma(v, s):
    """All affine cells/intersections, unlike production opposite-slope pairs."""
    knots = {Q(0), Q(1)}
    for speed, shift in zip(v, s):
        for half_integer in range(-2, 2 * speed + 4):
            t = (Q(half_integer, 2) - shift) / speed
            if 0 <= t <= 1:
                knots.add(t)
    ordered = sorted(knots)
    candidates = set(knots)
    for left, right in zip(ordered, ordered[1:]):
        mid = (left + right) / 2
        lines = []
        for speed, shift in zip(v, s):
            residue = (shift + speed * mid) % 1
            slope = speed if residue < Q(1, 2) else -speed
            lines.append((slope, distance(shift + speed * mid) - slope * mid))
        for i, (a, b) in enumerate(lines):
            for c, d in lines[i + 1:]:
                if a != c:
                    t = (d - b) / (a - c)
                    if left <= t <= right:
                        candidates.add(t)
    return max(min(distance(shift + speed * t) for speed, shift in zip(v, s))
               for t in candidates)


class CoverVerifierTests(unittest.TestCase):
    def assert_rejected(self, mutant, *, rehash=True, coverage=False):
        if rehash:
            resign(mutant)
        with self.assertRaises(CertificateError):
            verify_cover(mutant, require_counterexample=not coverage)

    def test_published_five_runner_all_time_certificate(self):
        result = verify_cover(bcs5())
        self.assertTrue(result["all_time_cover"])
        self.assertTrue(result["strict_shifted_counterexample"])
        self.assertEqual(result["delta"], [15, 94])

    def test_closed_endpoint_touches_and_strict_threshold_separate(self):
        c = certificate([1, 2, 3], [0, 0, 0], Q(1, 4))
        self.assertTrue(verify_cover(c, require_counterexample=False)["all_time_cover"])
        self.assertFalse(verify_cover(c, require_counterexample=False)["strict_shifted_counterexample"])
        self.assert_rejected(c)

    def test_nonprimitive_velocities_are_valid_without_period_reduction(self):
        c = certificate([2, 4, 6], [0, 0, 0], Q(1, 4))
        self.assertTrue(verify_cover(c, require_counterexample=False)["all_time_cover"])
        c["velocity_gcd"] = 1
        self.assert_rejected(c, coverage=True)

    def test_source_endpoint_and_winding_forgery(self):
        for field, value in (("winding", 999), ("runner", 5), ("left", [1, 99])):
            with self.subTest(field=field):
                c = bcs5()
                c["intervals"][0][field] = value
                self.assert_rejected(c)

    def test_off_by_one_runner_count_and_threshold(self):
        for field, value in (("n", 6), ("threshold", [1, 5])):
            c = bcs5()
            c[field] = value
            self.assert_rejected(c)

    def test_missing_cover_and_nonpermutation(self):
        c = bcs5()
        c["intervals"].pop()
        c["ordering"].pop()
        c["inequalities"].pop()
        self.assert_rejected(c)
        c = bcs5()
        c["ordering"][1] = c["ordering"][0]
        self.assert_rejected(c)

    def test_wrong_cross_multiplication(self):
        c = bcs5()
        c["inequalities"][0]["left_cross"] += 1
        self.assert_rejected(c)

    def test_float_rounding_hides_a_real_gap(self):
        delta = Q(2**59 - 1, 2**60)
        self.assertEqual(float(delta), float(1 - delta))
        c = certificate([1], [0], delta,
                        chain=[(0, 0, 0, delta), (0, 1, 1 - delta, 1)])
        self.assert_rejected(c)

    def test_payload_integrity(self):
        c = bcs5()
        c["source"]["fixture"] = "different source"
        self.assert_rejected(c, rehash=False)

    def test_noncanonical_fraction_duplicate_speed_and_boolean(self):
        for mutate in (
            lambda c: c["shifts"].__setitem__(3, [2, 4]),
            lambda c: c["velocities"].__setitem__(0, 2),
            lambda c: c.__setitem__("n", True),
            lambda c: c["intervals"][0].__setitem__("runner", False),
        ):
            c = bcs5()
            mutate(c)
            self.assert_rejected(c)

    def test_float_and_unverified_inverse_fields_rejected(self):
        c = bcs5()
        c["source"]["rounding"] = 0.5
        self.assert_rejected(c)
        c = bcs5()
        c["inverse_witness"] = {"claimed_inverse": 3}
        self.assert_rejected(c)


class ExactMaxminTests(unittest.TestCase):
    def test_published_exact_optimum_and_witness(self):
        c = bcs5()
        result = exact_maxmin(c["velocities"], c["shifts"])
        self.assertEqual(result["gamma"], [15, 94])
        t = Q(*result["maximizing_time"])
        self.assertEqual(min(distance(Q(*s) + v*t)
                             for v, s in zip(c["velocities"], c["shifts"])), Q(15, 94))
        self.assertEqual(result["raw_breakpoint_bound"], 90)

    def test_independent_affine_cell_oracle(self):
        rng = random.Random(20261028)
        for trial in range(50):
            n = 1 + trial % 5
            v = rng.sample(range(1, 10), n)
            s = [Q(rng.randrange(den), den) for den in [rng.randrange(1, 12) for _ in v]]
            with self.subTest(v=v, s=s):
                got = exact_maxmin(v, list(map(pair, s)))
                self.assertEqual(Q(*got["gamma"]), cell_arrangement_gamma(v, s))

    def test_time_translation_scaling_and_reindexing(self):
        v, s = [2, 5, 7], [Q(1, 3), Q(4, 7), Q(2, 9)]
        baseline = exact_maxmin(v, list(map(pair, s)))["gamma"]
        shifted = [(a + speed * Q(7, 23)) % 1 for a, speed in zip(s, v)]
        for speeds, phases in ((v, shifted), ([3*x for x in v], s),
                               (v[::-1], s[::-1])):
            self.assertEqual(exact_maxmin(speeds, list(map(pair, phases)))["gamma"], baseline)

    def test_candidate_budget_is_an_execution_boundary(self):
        with self.assertRaises(CandidateBudgetExceeded):
            exact_maxmin([1, 2, 3], [[0, 1]]*3, max_candidates=23)
        self.assertEqual(exact_maxmin([1, 2, 3], [[0, 1]]*3,
                                     max_candidates=24)["gamma"], [1, 4])


if __name__ == "__main__":
    unittest.main()
