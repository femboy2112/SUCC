#!/usr/bin/env python3
"""Current reconstruction of the documented independent review grids.

This is NOT the original temporary review script. Its source and stdout were
not persisted. The available review note records the sine parameter families
and exact-orbit grid; this script makes a new run of those families replayable.
The original 1,750-case Fejer grid is not reconstructed or rerun here.

Run from any directory. Output is one JSON receipt with the actual UTC time,
dependency hashes, declared grids and finite results. Sine comparisons use a
100-digit mpmath diagnostic, not a formal interval oracle. Orbit checks use
only exact Fraction arithmetic and an independent 16-root enumeration.
"""
from __future__ import annotations

from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import platform
import sys
from time import perf_counter

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO))

import mpmath as mp
from observational_succ import duck_bbp
from observational_succ import parity_boundary_certificate as certificate


def require(condition, context):
    if not condition:
        raise AssertionError(context)


def mpq(value):
    return mp.mpf(value.numerator) / value.denominator


def open_arc_hit(point, center, radius):
    """Independent periodic membership, including strict wrap endpoints."""
    offset = (point-center) % 1
    return offset < radius or offset > 1-radius


def sine_diagnostics():
    denominators = (1, 2, 4, 8, 16, 31, 32, 33, 64, 127)
    terms_grid = (1, 2, 4, 8, 16)
    count = 0
    plo, phi = duck_bbp.pi_interval(24)
    require(plo > 0, "source pi lower endpoint must be positive")
    require(phi + Q(1, 2**16) < Q(22, 7), "compact Taylor guard")
    with mp.workdps(100):
        tolerance = mp.mpf('1e-90')
        for denominator in denominators:
            # This declared numerator range is consistent with the recorded
            # families and case count; the original script was not recovered.
            for numerator in range(-denominator, denominator+1):
                phase = Q(numerator, denominator)
                reference = mp.sin(2*mp.pi*mpq(phase))
                for terms in terms_grid:
                    lo, hi = certificate.sine_turns_enclosure(
                        phase, bits=16, terms=terms)
                    require(lo <= hi, ("empty sine enclosure", phase, terms))
                    require(mpq(lo)-tolerance <= reference <= mpq(hi)+tolerance,
                            ("sine diagnostic failed", phase, terms, lo, hi))
                    count += 1
    require(count == 3230, ("sine parameter-case count", count))
    return {
        'status': 'PASS', 'parameter_cases': count,
        'denominators': denominators,
        'numerators': 'all integers -d through d inclusive for each denominator d',
        'taylor_terms': terms_grid, 'bits': 16,
        'mpmath_decimal_digits': 100, 'comparison_tolerance': '1e-90',
        'positive_pi_and_22_over_7_guards': 'PASS (exact rational)',
        'authority': 'finite high-precision diagnostic; not a universal proof',
    }


def orbit_recursion_checks():
    length, depth = 7, 4
    count = endpoint_rows = other_fiber_rows = 0
    for denominator in range(1, 66):
        for numerator in range(denominator):
            phases = [Q(numerator, denominator)]
            for _ in range(length):
                phases.append(16*phases[-1] % 1)
            result = certificate.stationary_boundary_recursion(phases, depth)
            us = [8*phase % 1 for phase in phases]
            sample = us[:-1]
            independent_masses, independent_contrasts = [], []
            for level in range(depth+1):
                radius = Q(1, 4*16**level)
                a = Q(sum(open_arc_hit(u, Q(), radius) for u in sample), length)
                b = Q(sum(open_arc_hit(u, Q(1, 2), radius) for u in sample), length)
                independent_masses.append(a+b)
                independent_contrasts.append(a-b)
                if level == depth:
                    continue
                endpoint = Q(
                    int(open_arc_hit(us[-1], Q(), radius))
                    - int(open_arc_hit(us[0], Q(), radius)), length)
                # Enumerate the fourteen distinct roots individually; the
                # implementation instead subtracts two fibers from a preimage.
                other = Q(sum(
                    open_arc_hit(u, Q(root, 16), radius/16)
                    for u in sample for root in range(16)
                    if root not in (0, 8)), length)
                all_roots = Q(sum(
                    open_arc_hit(u, Q(root, 16), radius/16)
                    for u in sample for root in range(16)), length)
                require(all_roots == a+endpoint,
                        ("stationarity endpoint identity", numerator, denominator, level))
                row = result['rows'][level]
                require(row['boundary_mass'] == a+b,
                        ("open boundary mass", numerator, denominator, level))
                require(row['signed_half_turn_contrast'] == a-b,
                        ("half-turn contrast", numerator, denominator, level))
                require(row['endpoint'] == endpoint,
                        ("endpoint sign", numerator, denominator, level))
                require(row['other_fourteen_fibers'] == other,
                        ("fourteen-fiber mass", numerator, denominator, level))
                require(row['identity_residual'] == 0,
                        ("recursion residual", numerator, denominator, level))
                endpoint_rows += int(endpoint != 0)
                other_fiber_rows += int(other > 0)
            for level, row in enumerate(result['rows']):
                require(row['next_boundary_mass'] == independent_masses[level+1],
                        ("next open boundary mass", numerator, denominator, level))
                require(independent_masses[level+1] == (
                    (independent_masses[level]+independent_contrasts[level])/2
                    + row['endpoint']-row['other_fourteen_fibers']),
                    ("independent exact recursion", numerator, denominator, level))
            contrast_payment = sum((
                abs(independent_contrasts[level])/2**(depth-level)
                for level in range(depth)), Q())
            upper = min(Q(1), independent_masses[0]/2**depth
                        + contrast_payment + Q(2, length)*(1-Q(1, 2**depth)))
            require(result['upper_bound'] == upper,
                    ("iterated endpoint payment", numerator, denominator))
            require(result['boundary_mass'] == independent_masses[-1] <= upper,
                    ("final boundary bound", numerator, denominator))
            count += 1
    require(count == 2145, ("orbit parameter-case count", count))
    require(endpoint_rows > 0 and other_fiber_rows > 0,
            "grid must exercise nonzero endpoint and fourteen-fiber terms")
    return {
        'status': 'PASS', 'parameter_cases': count,
        'denominators': 'all integers 1 through 65 inclusive',
        'numerators': 'all integers 0 through d-1 for each denominator d',
        'orbit_length_excluding_final_endpoint': length, 'recursion_depth': depth,
        'nonzero_endpoint_rows': endpoint_rows,
        'positive_other_fourteen_fiber_rows': other_fiber_rows,
        'arithmetic': 'exact Fraction; zero numerical tolerance',
        'authority': 'finite exact identities; not an asymptotic theorem',
    }


def file_hash(relative_path):
    return sha256((REPO / relative_path).read_bytes()).hexdigest()


def main():
    started = datetime.now(timezone.utc).isoformat()
    timer = perf_counter()
    files = (
        'observational_succ/parity_boundary_certificate.py',
        'observational_succ/duck_bbp.py',
        'observational_succ/selected_orbit.py',
        str(Path(__file__).resolve().relative_to(REPO)),
    )
    receipt = {
        'run_kind': 'CURRENT_RECONSTRUCTION_RERUN_NOT_ORIGINAL_REVIEW_RUN',
        'started_utc': started,
        'python_version': platform.python_version(),
        'mpmath_version': mp.__version__,
        'sha256': {path: file_hash(path) for path in files},
        'sine_diagnostics': sine_diagnostics(),
        'exact_orbit_recursions': orbit_recursion_checks(),
        'original_fejer_review': {
            'reported_parameter_cases': 1750,
            'status': 'NOT_RERUN_OR_RECONSTRUCTED',
            'reason': 'Original grid source and stdout were not persisted.',
        },
        'completed_utc': datetime.now(timezone.utc).isoformat(),
        'elapsed_seconds': round(perf_counter()-timer, 6),
    }
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
