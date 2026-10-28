#!/usr/bin/env python3
"""Independent exact finite oracle for reverse revelation and phase feedback.

Uses only the Python standard library and imports no SUCC production modules
or tests.  Root sums are evaluated in Q[X]/(X^(N/2)+1), for the declared
powers-of-two fibers.  Every calculation is rational; no complex floating
point or transcendental approximation is used.

The accompanying paper supplies the general theorem.  These finite checks
calibrate conditional character sums, selected likelihood innovations,
backward-state filtrations, and the adaptive coboundary counterexample.
They do not prove a new selected Weyl estimate or pi normality.

Run without arguments to emit the deterministic JSON receipt.  Pass
--verify PATH to independently recompute and compare a saved receipt.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path


BASELINE = "79344c62c39c96755b742700b3d4d22fa60d86da"


def root_vector(frequency, index, size):
    """Exact zeta_size**(frequency*index), for size a power of two."""
    if size < 2 or size & (size-1):
        raise ValueError("This independent root oracle requires size=2**d, d>=1")
    exponent = (frequency*index) % size
    return {exponent % (size//2): Q(1 if exponent < size//2 else -1)}


def add_scaled(left, right, scale=Q(1)):
    """Add sparse quotient-ring vectors, deleting exact zero coefficients."""
    for power, coefficient in right.items():
        left[power] = left.get(power, Q()) + scale*coefficient
        if not left[power]:
            del left[power]
    return left


def conditional_table(radix, depth, frequency, level):
    """Enumerate each residue class; do not use the claimed visibility test."""
    size, modulus = radix**depth, radix**level
    result = {}
    for residue in range(modulus):
        value = {}
        for index in range(residue, size, modulus):
            add_scaled(value, root_vector(frequency, index, size), Q(modulus, size))
        result[residue] = value
    return result


def visibility_level(radix, depth, frequency):
    """Small integer formula, compared with enumerated conditional sums."""
    if frequency % (radix**depth) == 0:
        return None
    reduced, order = abs(frequency), 0
    while reduced % radix == 0:
        reduced //= radix
        order += 1
    return depth-order


def check_inverse_fibers():
    conditional_checks = covariance_checks = square_checks = 0
    coverage = []
    configurations = [(2, depth) for depth in range(1, 9)] + [(16, 1), (16, 2)]
    for radix, depth in configurations:
        size = radix**depth
        frequencies = sorted(set((0, 1, -1, 2, -8, 4, 8, 16, 24,
                                  size//2, size, 2*size)))
        selected_indices = sorted(set((0, 1, size//2, size-1)))
        coverage.append({"radix": radix, "depth": depth, "fiber_size": size,
                         "frequencies": frequencies,
                         "selected_indices": selected_indices})
        for frequency in frequencies:
            tables = [conditional_table(radix, depth, frequency, level)
                      for level in range(depth+1)]
            for level, table in enumerate(tables):
                visible = frequency % (radix**(depth-level)) == 0
                for residue, value in table.items():
                    expected = root_vector(frequency, residue, size) if visible else {}
                    assert value == expected
                    conditional_checks += 1
            for selected in selected_indices:
                total_pairing, total_square = {}, Q()
                for level in range(1, depth+1):
                    term, square, mean = {}, Q(), Q()
                    for index in range(size):
                        current = (radix**level if index % (radix**level)
                                   == selected % (radix**level) else 0)
                        previous = (radix**(level-1) if index % (radix**(level-1))
                                    == selected % (radix**(level-1)) else 0)
                        increment = current-previous
                        delta = dict(tables[level][index % (radix**level)])
                        add_scaled(delta, tables[level-1][index % (radix**(level-1))], Q(-1))
                        add_scaled(term, delta, Q(increment, size))
                        mean += Q(increment, size)
                        square += Q(increment*increment, size)
                    expected_term = (root_vector(frequency, selected, size)
                                     if frequency % (radix**(depth-level)) == 0
                                     and frequency % (radix**(depth-level+1)) != 0
                                     else {})
                    assert term == expected_term
                    assert mean == 0
                    assert square == (radix-1)*radix**(level-1)
                    add_scaled(total_pairing, term)
                    total_square += square
                    covariance_checks += 1
                    square_checks += 1
                expected_difference = dict(root_vector(frequency, selected, size))
                add_scaled(expected_difference, tables[0][0], Q(-1))
                assert total_pairing == expected_difference
                assert total_square == size-1
    examples = [{"frequency": frequency,
                 "binary_depth": 8,
                 "single_observable_innovation_level": visibility_level(2, 8, frequency)}
                for frequency in (0, 1, 2, 4, 8, 16, 24, 128, 256, -8)]
    assert [row["single_observable_innovation_level"] for row in examples] == [
        None, 8, 7, 6, 5, 4, 5, 1, None, 5]
    return {
        "conditional_root_sum_checks": conditional_checks,
        "selected_covariance_increment_checks": covariance_checks,
        "likelihood_increment_mean_and_square_checks": square_checks,
        "coverage": coverage,
        "binary_visibility_examples": examples,
        "translation_scope": "Arbitrary common a factors out as the unit phase e(h*a/size).",
    }


def original_forcing(index):
    """Direct four-pole formula, with no production import."""
    return (Q(4, 8*index-7)-Q(2, 8*index-4)
            -Q(1, 8*index-3)-Q(1, 8*index-2))


def check_forced_filtrations():
    cases = [
        ("authentic_two_macrosteps", 16,
         (original_forcing(1), original_forcing(2)), Q(1, 17)),
        ("authentic_first_macrostep_binary_refinement", 2,
         (Q(), Q(), Q(), original_forcing(1)), Q(2, 15)),
        ("signed_rational_forcing", 2, (Q(1, 3), Q(-2, 5), Q(7, 11)), Q(3, 7)),
    ]
    checks, records = 0, []
    for name, radix, forcing, terminal in cases:
        depth, size = len(forcing), radix**len(forcing)
        accumulated = sum((radix**(depth-i-1)*value
                           for i, value in enumerate(forcing)), Q())
        offset = terminal-accumulated
        histories = {}
        for index in range(size):
            states = [((offset+index)/size) % 1]
            for value in forcing:
                states.append((radix*states[-1]+value) % 1)
            assert states[-1] == terminal
            histories[index] = tuple(states)
        for level in range(depth+1):
            residue_state = {}
            for index, states in histories.items():
                residue, value = index % (radix**level), states[depth-level]
                if residue in residue_state:
                    assert residue_state[residue] == value
                residue_state[residue] = value
                checks += 1
            assert len(set(residue_state.values())) == radix**level
        record = {"name": name, "radix": radix, "depth": depth,
                  "forcing": [str(x) for x in forcing],
                  "terminal": str(terminal), "raw_offset": str(offset),
                  "fiber_size": size, "all_reverse_state_partitions_match": True}
        if name == "authentic_first_macrostep_binary_refinement":
            selected = next(index for index, states in histories.items() if states[0] == 0)
            raw_digits = tuple((selected//radix**level) % radix for level in range(depth))
            states = histories[selected]
            reduced_labels = []
            for step in range(depth, 0, -1):
                candidates = [digit for digit in range(radix)
                              if ((states[step]-forcing[step-1]+digit)/radix) % 1
                              == states[step-1]]
                assert len(candidates) == 1
                reduced_labels.append(candidates[0])
            canonical_tail = offset % 1
            canonical_index = (selected+offset.numerator//offset.denominator) % size
            assert (selected, raw_digits, tuple(reduced_labels)) == (
                3, (1, 1, 0, 0), (1, 0, 0, 0))
            assert canonical_tail == 0 and canonical_index == 0
            assert ((canonical_tail+canonical_index)/size) % 1 == states[0]
            record["digit_convention_control"] = {
                "raw_fiber_index": selected,
                "raw_fiber_digits_low_first": raw_digits,
                "literal_reduced_state_backward_labels": reduced_labels,
                "canonicalized_forcing_stripped_tail": str(canonical_tail),
                "canonicalized_fiber_index": canonical_index,
                "literal_and_raw_digits_equal": False,
                "first_t_generated_sigma_fields_equal": True,
            }
        records.append(record)
    return {"forced_backward_filtration_checks": checks, "cases": records}


def matrix_product(left, right):
    return tuple(tuple(sum((x*y for x, y in zip(row, column)), Q())
                       for column in zip(*right)) for row in left)


def check_coboundary():
    probability = Q(3, 4)
    kernel = ((probability, 1-probability), (probability, 1-probability))
    twisted = ((probability, probability-1), (-probability, 1-probability))
    assert matrix_product(twisted, twisted) == twisted
    assert tuple(sum(row, Q()) for row in twisted) == (Q(1, 2), Q(-1, 2))
    records, enumerated_paths = [], 0
    for depth in range(1, 7):
        mean, conditional_masses, conditional_weighted = Q(), {}, {}
        for word in product((1, -1), repeat=depth):
            weight, phase, previous = Q(1), 1, 1
            for sign in word:
                weight *= probability if sign == 1 else 1-probability
                phase *= sign*previous
                previous = sign
            assert phase == word[-1]
            mean += weight*phase
            prefix = word[:-1]
            last_increment = word[-1]*(word[-2] if depth > 1 else 1)
            conditional_masses[prefix] = conditional_masses.get(prefix, Q())+weight
            conditional_weighted[prefix] = conditional_weighted.get(prefix, Q())+weight*last_increment
            enumerated_paths += 1
        for prefix, mass in conditional_masses.items():
            previous = prefix[-1] if prefix else 1
            assert conditional_weighted[prefix]/mass == Q(1, 2)*previous
        assert mean == Q(1, 2)
        proposed = Q(1, 2)**depth
        assert (abs(mean) > proposed) == (depth > 1)
        records.append({"depth": depth, "exact_product_expectation": str(mean),
                        "local_conditional_modulus": "1/2",
                        "product_of_local_moduli": str(proposed),
                        "instance_violates_modulus_product_bound": depth > 1})
    return {
        "reference_kernel": [[str(x) for x in row] for row in kernel],
        "twisted_kernel": [[str(x) for x in row] for row in twisted],
        "exact_matrix_identities": 2,
        "path_depths_checked": 6,
        "complete_paths_enumerated": enumerated_paths,
        "path_enumeration": records,
    }


def receipt():
    if not __debug__:
        raise RuntimeError("Do not disable the oracle assertions with python -O")
    inverse = check_inverse_fibers()
    forced = check_forced_filtrations()
    coboundary = check_coboundary()
    assert inverse["conditional_root_sum_checks"] == 15390
    assert inverse["selected_covariance_increment_checks"] == 1722
    assert forced["forced_backward_filtration_checks"] == 880
    return {
        "schema_version": 1,
        "status": "PASS: INDEPENDENT EXACT FINITE REVELATION CALIBRATION",
        "baseline_commit": BASELINE,
        "oracle_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies": "Python standard library only",
        "production_imports": [],
        "test_imports": [],
        "arithmetic": "Fraction and exact power-of-two cyclotomic polynomial reduction",
        "inverse_fiber_checks": inverse,
        "forced_filtration_checks": forced,
        "adaptive_coboundary_control": coboundary,
        "scope": {
            "finite_checks_replace_paper_proofs": False,
            "literal_branch_digits_identified_with_canonical_fiber_digits": False,
            "moving_terminal_reference_laws_assumed_projectively_consistent": False,
            "selected_Weyl_saving_proved": False,
            "pi_normality_proved": False,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    actual = receipt()
    if args.verify is not None:
        # Normalize tuple/list distinctions to exactly the emitted JSON schema.
        normalized = json.loads(json.dumps(actual))
        if json.loads(args.verify.read_text()) != normalized:
            raise SystemExit("SEINFELD_REVELATION_ORACLE_RECEIPT_MISMATCH")
        print("SEINFELD_REVELATION_ORACLE_RECEIPT_VERIFIED")
    else:
        print(json.dumps(actual, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
