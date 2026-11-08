"""Exact history-aware learning observer for SUCC's unchanged four-pole BBP.

Classical finite epistemic instrumentation; no proof of pi normality or physical
observer realization. A zero-source, phase-calibrated sensor is an ASSUMPTION.

Past-local reports can remain informative after the carrier's projected circle
state has forgotten them. In the UNWRAPPED arithmetic carrier integer carries
may retain the same information: the no-go is relative to circle-only access.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from collections import Counter
from typing import Callable

from .pinbed_oscillator_bridge import four_pole

RADIX = 16
MAX_CANDIDATES = 4096


def _index_depth(index: int, depth: int) -> None:
    if (type(depth) is not int or depth < 1 or type(index) is not int
            or not 0 <= index < RADIX ** depth):
        raise ValueError("index must belong to the declared 16**depth seed grid")


def seed(index: int, depth: int) -> Fraction:
    """A possible source seed in [0,1), not automatically the authentic zero."""
    _index_depth(index, depth)
    return Fraction(index, RADIX ** depth)


def zero_source_history(until: int) -> tuple[Fraction, ...]:
    """Exact original rational zero-seed *unwrapped* BBP history."""
    if type(until) is not int or not 0 <= until <= 200:
        raise ValueError("until must be an integer 0..200")
    hist = [Fraction()]
    for n in range(1, until+1):
        hist.append(RADIX * hist[-1] + four_pole(n))
    return tuple(hist)


def unwrapped_at(index: int, depth: int, time: int) -> Fraction:
    """Unwrapped source U_t(s), including its carry/integer component."""
    _index_depth(index, depth)
    if type(time) is not int or not 0 <= time <= 200:
        raise ValueError("time must be an integer 0..200")
    return zero_source_history(time)[-1] + RADIX ** time * seed(index, depth)


def circle_at(index: int, depth: int, time: int) -> Fraction:
    """Observable circle phase (fractional part), never the full source."""
    return unwrapped_at(index, depth, time) % 1


def calibrated_phase(index: int, depth: int, time: int) -> Fraction:
    """Relative to the known authentic zero-source reference at time t.

    This virtual phase-relative instrument presumes a source-fixed reference;
    an independently spinning gauge is not a substitute for real calibration.
    """
    return (circle_at(index, depth, time) - zero_source_history(time)[-1]) % 1


def oscillator_pin(index: int, depth: int, time: int, harmonic: int = 1,
                   bins: int = RADIX) -> int:
    """Coherent oscillator mode h then a finite bin sensor (exact Fraction)."""
    if type(harmonic) is not int or harmonic == 0 or type(bins) is not int or bins < 2:
        raise ValueError("nonzero integer mode and at least two outcome bins required")
    return _bin((harmonic * calibrated_phase(index, depth, time)) % 1, bins)


def guarded_pin(index: int, depth: int, time: int,
                error: Fraction = Fraction()) -> int:
    """Depth-calibrated 16-bin readout with a rigorous finite-grid noise margin.

    For t<depth, each candidate phase is a multiple of 16**(-(depth-t));
    offset by half that grid step, away from every bin boundary. A *total*
    phase error (source clock+readout+reference) of magnitude strictly less
    than half that grid step cannot change any declared candidate label.
    This assertion is only for the FINITE GRID and given time window.
    """
    _index_depth(index, depth)
    if type(time) is not int or not 0 <= time < depth:
        raise ValueError("guarded learner probes only before future collapse")
    if type(error) not in (int, Fraction):
        raise ValueError("exact rational error required for proof-grade tests")
    offset = Fraction(1, 2 * RADIX ** (depth-time))
    return _bin((calibrated_phase(index, depth, time)+offset+error)%1, RADIX)


def guard_margin(depth: int, time: int) -> Fraction:
    if type(depth) is not int or depth < 1 or type(time) is not int or not 0 <= time < depth:
        raise ValueError("time must precede collapse")
    return Fraction(1, 2 * RADIX ** (depth-time))


def _bin(q: Fraction, bins: int) -> int:
    scaled = bins*q
    return scaled.numerator // scaled.denominator


@dataclass(frozen=True)
class Report:
    time: int
    harmonic: int
    bin_label: int
    surviving: tuple[int, ...]


@dataclass(frozen=True)
class Learner:
    """Posterior/support learner, with complete provenance-preserving reports."""
    depth: int
    possible: tuple[int, ...]
    transcript: tuple[Report, ...] = ()

    @classmethod
    def full_grid(cls, depth: int, max_candidates: int = MAX_CANDIDATES) -> "Learner":
        if type(depth) is not int or depth < 1 or type(max_candidates) is not int or max_candidates < 1:
            raise ValueError("finite depth/candidate budget required")
        count = RADIX ** depth
        if count > max_candidates:
            raise ValueError("resource budget exceeded; theorem remains valid abstractly")
        return cls(depth, tuple(range(count)))

    def observe(self, time: int, harmonic: int, bin_label: int) -> "Learner":
        if not self.possible:
            raise ValueError("out-of-model posterior")
        if self.transcript and time < self.transcript[-1].time:
            raise ValueError("observations must be time ordered")
        if type(bin_label) is not int or not 0 <= bin_label < RADIX:
            raise ValueError("invalid bin label")
        survivors = tuple(i for i in self.possible if oscillator_pin(i,self.depth,time,harmonic)==bin_label)
        if not survivors:
            raise ValueError("report inconsistent with source/seed class")
        return Learner(self.depth, survivors,
                       self.transcript + (Report(time,harmonic,bin_label,survivors),))

    def choose_mode(self, time: int, modes: tuple[int, ...] = (1,2,3,4,5)) -> int | None:
        """Minimax next probe: maximize discrimination among current survivors.

        Only a declared permitted mode menu may be chosen. No performed physical
        experiment, source-specific energy saving, or inferred truth probability.
        """
        if type(modes) is not tuple or not modes:
            raise ValueError("nonempty finite permitted mode menu required")
        ranked = []
        for h in modes:
            if type(h) is not int or h == 0:
                raise ValueError("admissible integer oscillator modes required")
            counts=Counter(oscillator_pin(i,self.depth,time,h) for i in self.possible)
            ranked.append((max(counts.values()),sum(n*n for n in counts.values()),h))
        best = min(ranked)
        return best[-1] if best[0] < len(self.possible) else None

    def truth_verdict(self, proposition: Callable[[int], bool]) -> str:
        """Separate may from must; no default promotion of compatible to true."""
        if not self.possible:
            return "OUT_OF_MODEL"
        possible_truths={bool(proposition(i)) for i in self.possible}
        if possible_truths == {True}:
            return "INVARIANT_TRUE"
        if possible_truths == {False}:
            return "INVARIANT_FALSE"
        return "AMBIGUOUS_TARGET_TRUE_COMPATIBLE"


def learn_true_seed(depth: int, actual_index: int,
                    modes: tuple[int, ...] = (1,2,3,4,5)) -> Learner:
    """Play a lawful adaptive finite game; learn an index, not pi's normality."""
    _index_depth(actual_index, depth)
    learner = Learner.full_grid(depth)
    for t in range(depth):
        if len(learner.possible)==1:
            break
        mode = learner.choose_mode(t,modes)
        if mode is None:
            break
        report = oscillator_pin(actual_index, depth,t,mode)
        learner=learner.observe(t,mode,report)
    return learner


def learn_guarded_seed(depth: int, actual_index: int,
                       errors: tuple[Fraction, ...] = ()) -> Learner:
    """An N-step, lossless learning protocol with declared per-step noise budget.

    Zero-source reference is computed from the exact original four poles. The
    measurements remain synthetic; no real sensor provenance is implied.
    """
    _index_depth(actual_index, depth)
    if errors and len(errors)!=depth:
        raise ValueError("one exact error term per observation is required")
    learner=Learner.full_grid(depth)
    for t in range(depth):
        err=errors[t] if errors else Fraction()
        if type(err) not in (int,Fraction) or abs(err)>=guard_margin(depth,t):
            raise ValueError("calibrated error exceeds robust observation margin")
        label=guarded_pin(actual_index, depth,t,err)
        learner=learner.observe(t,1,label)
    return learner
