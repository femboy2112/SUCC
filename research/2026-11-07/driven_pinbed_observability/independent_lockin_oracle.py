#!/usr/bin/env python3
"""Independent exact G_4 lock-in oracle; no SUCC or third-party imports.

Scope was written in oscillator-adversary.md before this program was executed.
All Gaussian arithmetic is rational. This is a finite test, not an infinite proof.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from hashlib import sha256
from pathlib import Path
import json


@dataclass(frozen=True)
class G:
    re: Q = Q(0)
    im: Q = Q(0)

    @staticmethod
    def coerce(other):
        return other if isinstance(other, G) else G(Q(other))

    def __add__(self, other):
        z = G.coerce(other)
        return G(self.re + z.re, self.im + z.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + -G.coerce(other)

    def __rsub__(self, other):
        return G.coerce(other) + -self

    def __mul__(self, other):
        z = G.coerce(other)
        return G(self.re*z.re - self.im*z.im,
                 self.re*z.im + self.im*z.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        z = G.coerce(other)
        d = z.norm2()
        if d == 0:
            raise ZeroDivisionError("zero Gaussian divisor")
        return self*z.conjugate()*G(1/d)

    def conjugate(self):
        return G(self.re, -self.im)

    def norm2(self):
        return self.re*self.re + self.im*self.im


ROOTS = (G(Q(1)), G(Q(0), Q(1)), G(Q(-1)), G(Q(0), Q(-1)))
ZERO = G()


def root(n):
    return ROOTS[n % 4]


def average(xs):
    xs = tuple(xs)
    assert xs
    return sum(xs, ZERO)/len(xs)


def hsum(length, mode):
    return sum((root(mode*j) for j in range(length)), ZERO)


def response(length, tone, source, center):
    j = (source-center) % 4
    return root(-tone*j) if j < length else ZERO


def positive_phase_readout(length, phase_quarter, source, center):
    j = (source-center) % 4
    if j >= length:
        return Q(0)
    return 1 + root(j+phase_quarter).re


def lockin(length, target, source, center, mutation=None):
    a = hsum(length, target)
    b = hsum(length, target-1)
    s = a.norm2()+b.norm2()
    assert s > 0
    r0 = response(length, 0, source, center)
    r1 = response(length, 1, source, center)
    numerator = a.conjugate()*r0 + b.conjugate()*r1
    reference = root(-target*center)
    if mutation == "erase_reference":
        reference = root(0)
    elif mutation == "reverse_reference":
        reference = root(target*center)
    factor = 1 if mutation == "omit_normalization" else 4
    value = factor*reference*numerator/s
    if mutation == "power_only":
        return G(value.norm2())
    return value


def profile(length, tone, law):
    return tuple(sum((law[x]*response(length, tone, x, y)
                      for x in range(4)), ZERO) for y in range(4))


def encode_g(z):
    return {"real": str(z.re), "imag": str(z.im)}


def main():
    counts = {"atom_unbiasedness": 0, "second_moment_formula": 0,
              "four_phase_reconstruction": 0, "nonnegative_phase_masks": 0,
              "source_words": 0, "source_reference_word_pairs": 0,
              "constant_gain_calibration": 0}
    variances = {}
    table = {}
    for length in (1, 2, 3):
        for target in (1, 2, 3):
            key = (length, target)
            table[key] = {(x, y): lockin(length, target, x, y)
                          for x in range(4) for y in range(4)}
            a, b = hsum(length, target), hsum(length, target-1)
            s = a.norm2()+b.norm2()
            q_formula = (Q(4)/(s*s))*sum(
                ((a.conjugate()+b.conjugate()*root(-j)).norm2()
                 for j in range(length)), Q(0))
            for x in range(4):
                zs = tuple(table[key][x, y] for y in range(4))
                expected = root(-target*x)
                assert average(zs) == expected
                counts["atom_unbiasedness"] += 1
                second = sum((z.norm2() for z in zs), Q(0))/4
                assert second == q_formula
                assert second <= Q(8*length)/s
                counts["second_moment_formula"] += 1
            assert q_formula >= 1
            variances[key] = q_formula-1
    assert variances[2, 2] == 3

    # Four nonnegative sinusoidal settings recover coherent channels only
    # when they are readings of the same source snapshot and reference center.
    for length in (1, 2, 3):
        for x, y in product(range(4), repeat=2):
            values = [positive_phase_readout(length, phase, x, y)
                      for phase in range(4)]
            assert all(value >= 0 for value in values)
            counts["nonnegative_phase_masks"] += 4
            baseline = (values[0]+values[2])/2
            assert baseline == (values[1]+values[3])/2
            recovered = G((values[0]-values[2])/2,
                          (values[1]-values[3])/2)
            assert G(baseline) == response(length, 0, x, y)
            assert recovered == response(length, 1, x, y)
            counts["four_phase_reconstruction"] += 1

    def verify_word(length, target, source_word):
        n = len(source_word)
        truth = average(root(-target*x) for x in source_word)
        estimated_mean = ZERO
        squared_error = Q(0)
        word_count = 0
        lookup = table[length, target]
        for centers in product(range(4), repeat=n):
            estimate = sum((lookup[x, y] for x, y in zip(source_word, centers)), ZERO)/n
            estimated_mean += estimate
            squared_error += (estimate-truth).norm2()
            word_count += 1
        assert estimated_mean/word_count == truth
        assert squared_error/word_count == variances[length, target]/n
        counts["source_words"] += 1
        counts["source_reference_word_pairs"] += word_count

    for length in (1, 2, 3):
        for target in (1, 2, 3):
            for n in (1, 2, 3):
                for source_word in product(range(4), repeat=n):
                    verify_word(length, target, source_word)
            for source_word in ((0, 1, 1, 2, 3), (3, 0, 2, 2, 1), (1, 3, 0, 3, 2)):
                verify_word(length, target, source_word)

    laws = ((Q(1, 4),)*4, (Q(1), Q(0), Q(0), Q(0)),
            tuple(Q(j, 10) for j in (1, 2, 3, 4)),
            tuple(Q(j, 17) for j in (5, 3, 2, 7)))
    gains = (G(Q(3, 5), Q(4, 5)), G(Q(-7, 5), Q(2, 3)))
    for length in (1, 2, 3):
        normalizer = hsum(length, -1)
        assert normalizer != ZERO
        for law in laws:
            p = profile(length, 1, law)
            assert sum(p, ZERO) == normalizer
            for gain in gains:
                measured = tuple(gain*z for z in p)
                recovered_gain = sum(measured, ZERO)/normalizer
                assert recovered_gain == gain
                assert tuple(z/recovered_gain for z in measured) == p
                counts["constant_gain_calibration"] += 1

    mutations = {}
    for name in ("erase_reference", "reverse_reference", "omit_normalization", "power_only"):
        witness = None
        for length, target, x in product((1, 2, 3), (1, 2, 3), range(4)):
            mean = average(lockin(length, target, x, y, mutation=name) for y in range(4))
            if mean != root(-target*x):
                witness = {"length": length, "target": target, "source": x,
                           "mutant_mean": encode_g(mean),
                           "correct_mean": encode_g(root(-target*x))}
                break
        assert witness is not None
        mutations[name] = witness

    # A source-locked constant and a genuinely uniform source have identical
    # erased-clock relative words, but the registered-clock reconstruction splits them.
    source_a, clock_a = (0, 0, 0, 0), (0, 1, 2, 3)
    source_b, clock_b = (0, 3, 2, 1), (0, 0, 0, 0)
    relative_a = tuple((x-y) % 4 for x, y in zip(source_a, clock_a))
    relative_b = tuple((x-y) % 4 for x, y in zip(source_b, clock_b))
    assert relative_a == relative_b
    transported = []
    for h in (1, 2, 3):
        relative_mean = average(root(-h*z) for z in relative_a)
        truth_a = average(root(-h*x) for x in source_a)
        truth_b = average(root(-h*x) for x in source_b)
        corrected_a = average(root(-h*z)*root(-h*y) for z, y in zip(relative_a, clock_a))
        corrected_b = average(root(-h*z)*root(-h*y) for z, y in zip(relative_b, clock_b))
        assert relative_mean == ZERO and truth_a == root(0) and truth_b == ZERO
        assert corrected_a == truth_a and corrected_b == truth_b
        transported.append({"h": h, "relative_mean": encode_g(relative_mean),
                            "source_a": encode_g(truth_a), "source_b": encode_g(truth_b)})
    mutations["erase_clock_false_uniformity"] = {
        "source_a": source_a, "clock_a": clock_a,
        "source_b": source_b, "clock_b": clock_b,
        "identical_relative_word": relative_a,
        "transported_means": transported}

    # Equal power and equal static windows do not identify coherent phase.
    even_law = (Q(1, 2), Q(0), Q(1, 2), Q(0))
    odd_law = (Q(0), Q(1, 2), Q(0), Q(1, 2))
    p0, q0 = profile(2, 0, even_law), profile(2, 0, odd_law)
    p1, q1 = profile(2, 1, even_law), profile(2, 1, odd_law)
    assert p0 == q0 and p1 != q1
    assert tuple(z.norm2() for z in p1) == tuple(z.norm2() for z in q1)
    mutations["erase_profile_phase"] = {
        "first_law": [str(x) for x in even_law],
        "second_law": [str(x) for x in odd_law],
        "static_profiles_equal": True, "driven_powers_equal": True,
        "coherent_profiles_equal": False}

    # An unbound phase cycle need not be a reading of any single snapshot.
    changed_sources = (0, 0, 1, 0)
    changed_cycle = tuple(positive_phase_readout(2, p, changed_sources[p], 0)
                          for p in range(4))
    assert changed_cycle[0]+changed_cycle[2] != changed_cycle[1]+changed_cycle[3]
    mutations["change_source_during_phase_cycle"] = {
        "source_states": changed_sources,
        "phase_readings": [str(x) for x in changed_cycle],
        "two_baseline_reconstructions_disagree": True}

    payload = {
        "status": "PASS",
        "arithmetic": "exact Gaussian rationals; Python standard library only",
        "scope": "G_4; L=1,2,3; h=1,2,3; all source/reference words of lengths 1..3 plus three predeclared length-5 source words",
        "counts": counts,
        "single_sample_variances": [
            {"L": l, "h": h, "variance": str(variances[l, h])}
            for l in (1, 2, 3) for h in (1, 2, 3)],
        "mutations_rejected": len(mutations),
        "mutation_witnesses": mutations,
        "sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "infinite_theorems_proved_by_this_run": False,
        "pi_base16_normality": "OPEN"}
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
