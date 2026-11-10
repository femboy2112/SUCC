"""Independent rational containment oracle for the root fixed-point phases.

The reference uses no quadrant reduction, no root interval arithmetic, and a
separately rounded Machin series. Its narrow rational enclosure must be wholly
inside the root enclosure, not merely overlap it. Finite calibration only.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
NAMESPACE = HERE.parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT))


def load_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def ceiling(x):
    return -((-x.numerator)//x.denominator)


@lru_cache(None)
def independent_pi():
    grid = 10**80
    def atan(q):
        low, high = 0, 0
        for j in range(80):
            term = Q((-1)**j, (2*j+1)*q**(2*j+1))*grid
            low += term.numerator//term.denominator
            high += ceiling(term)
        # An even-length alternating partial sum is below atan(1/q).
        high += ceiling(Q(grid, 161*q**161))
        return Q(low, grid), Q(high, grid)
    a, b = atan(5), atan(239)
    return 16*a[0]-4*b[1], 16*a[1]-4*b[0]


def independent_character(turn):
    turn = Q(turn)%1
    if turn > Q(1, 2):
        turn -= 1
    low, high = independent_pi()
    x = (low+high)*turn
    angle_error = abs(turn)*(high-low)
    cosine, sine, cterm, sterm = Q(1), x, Q(1), x
    for k in range(1, 43):
        cterm *= -x*x/Q((2*k-1)*(2*k))
        sterm *= -x*x/Q((2*k)*(2*k+1))
        cosine += cterm
        sine += sterm
    # cos through degree 84 is also degree 85; sin degree 85 is also degree 86.
    ec = abs(cterm*x*x/Q(85*86)) + angle_error
    es = abs(sterm*x*x/Q(86*87)) + angle_error
    return cosine-ec, cosine+ec, sine-es, sine+es


def run():
    observed = load_file("covariance_forge_intervals_hostile", NAMESPACE / "intervals.py")
    source = load_file("covariance_forge_source_hostile", NAMESPACE / "source.py")
    turns = [Q(n, 31) for n in range(-17, 49)]
    turns += [Q(k, 8)+Q(e, 10**50) for k in range(-8, 9) for e in (-1, 0, 1)]
    turns += [Q(1, 10**100+267), Q(10**100+266, 10**100+267)]
    count = 0
    for turn in turns:
        result = observed.phase(turn.numerator, turn.denominator)
        lo, hi, bottom, top = independent_character(turn)
        for interval, a, b in ((result.re, lo, hi), (result.im, bottom, top)):
            assert Q(interval.lo, observed.SCALE) <= a <= b <= Q(interval.hi, observed.SCALE)
            count += 1
    # Unreduced common denominators, including negative numerators and p powers.
    from observational_succ.selected_orbit import SelectedOrbit
    source_checks = 0
    history = source.common_history(91)
    values = SelectedOrbit()
    for n in range(92):
        assert Q(history["residues"][n], history["denominator"]) == values.state(n)
        source_checks += 1
    for p in (3, 5, 7, 17):
        for exponent in (1, 2, 3):
            for numerator in (-p*p, -1, 0, 1, p*p):
                denominator = (p**exponent)*11
                first = Q(*source.principal_pair(numerator, denominator, p))
                reduced = Q(numerator, denominator)
                second = Q(*source.principal_pair(reduced.numerator, reduced.denominator, p))
                assert first == second
                assert (reduced-first).denominator%p != 0
                source_checks += 2
    return {"status": "CERTIFIED-FINITE", "phase_containments": count,
            "phase_inputs": len(turns), "source_checks": source_checks,
            "method": "independent rational Taylor + separate integer-rounded Machin; containment",
            "root_files": {p.name: sha256(p.read_bytes()).hexdigest() for p in
                           (NAMESPACE/"intervals.py", NAMESPACE/"source.py",
                            NAMESPACE/"run_experiment.py", NAMESPACE/"test_instrument.py",
                            NAMESPACE/"run_spectral_probe.py")},
            "pi_normality": "OPEN", "RH": "OPEN"}


if __name__ == "__main__":
    receipt = run()
    (HERE/"INSTRUMENT_AUDIT.json").write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
    print(json.dumps(receipt, sort_keys=True))
