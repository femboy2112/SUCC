"""Exact finite receipts for the Borwein ratchet and arithmetic readout.

The proofs, not this finite campaign, justify infinite traversal/convergence.
Numerical logarithms below are display diagnostics; no decision uses them.
Run from any directory; the report is printed as JSON and writes no files.
"""
from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))

import borwein_ratchet as br
from borwein_independent_audit import sum_interval_probability, clip_polygon, polygon_area
from cylinder import omega


def run_probe() -> dict:
    groups: dict[str, int] = {}

    def check(group: str, condition: bool) -> None:
        if not condition:
            raise AssertionError(group)
        groups[group] = groups.get(group, 0) + 1

    # Independent marking of prime-power divisibility reconstructs Omega.
    limit = 1000
    degrees = [0] * (limit + 1)
    sieve = [True] * (limit + 1)
    sieve[:2] = [False, False]
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        for multiple in range(2 * p, limit + 1, p):
            sieve[multiple] = False
        power = p
        while power <= limit:
            for multiple in range(power, limit + 1, power):
                degrees[multiple] += 1
            power *= p

    bank = (Q(1, 3), Q(1, 5))
    eigenvalues = {}
    for n in range(1, limit + 1):
        check("source_degree_vs_prime_power_marking", omega(n) == degrees[n])
        eigenvalues[n] = br.integer_charge_filter(bank, omega(n) - 1)
        check("prime_fixed_labels_vs_marking_sieve", (eigenvalues[n] == 1) == sieve[n])
    for rounds in (1, 2, 3, 7, 16):
        error = max(abs(eigenvalues[n]**rounds - int(sieve[n]))
                    for n in range(2, limit + 1))
        check("finite_operator_norm_attains_exact_bound",
              error == br.integer_filter_error(rounds))
    check("unit_extension", eigenvalues[1] + Q(1, 2) == 1)
    check("unit_extension_mutation", eigenvalues[1] + 1 == Q(3, 2))
    check("readout_successor_commutator", eigenvalues[4] - eigenvalues[3] == -Q(1, 2))
    check("readout_successor_commutator", eigenvalues[5] - eigenvalues[4] == Q(1, 2))

    # Production CDF vs an independently calibrated polygon-clipping oracle.
    pairs = ((Q(1, 7), Q(2, 5)), (Q(1, 3), Q(2, 3)),
             (Q(7, 4), Q(1, 9)), (Q(2), Q(2)))
    for a, b in pairs:
        for half_window in (Q(1, 2), Q(1), Q(3, 2)):
            for shift in (Q(j, 3) for j in range(-9, 10)):
                actual = br.window_mass((a, b), half_window, shift)
                expected = sum_interval_probability(
                    a, b, -half_window - shift, half_window - shift)
                check("production_window_vs_polygon", actual == expected)
                check("plateau_iff_boundary", (actual == 1) == (a + b + abs(shift) <= half_window))
                check("zero_iff_boundary", (actual == 0) == (abs(shift) >= a + b + half_window))

        # Direct geometry in the four original sign quadrants. The negative
        # quadrant is a retained atom, not a continuous-density endpoint.
        for threshold in (Q(j, 5) for j in range(-2, 21)):
            if threshold < 0:
                expected = Q(0)
            else:
                positive_square = [(Q(0), Q(0)), (a, Q(0)), (a, b), (Q(0), b)]
                area = polygon_area(clip_polygon(positive_square, (Q(1), Q(1), threshold)))
                expected = (Q(1, 4) + min(threshold, a) / (4*a) +
                            min(threshold, b) / (4*b) + area / (4*a*b))
            check("rectified_cdf_vs_sign_quadrants",
                  br.rectified_cdf((a, b), threshold) == expected)

    state = br.RatchetState()
    events = []
    for step in range(1, 419):
        update = state.advance(Q(1, 2*step + 1))
        check("odd_clock_no_skipped_tooth", len(update.releases) <= 1)
        for tooth in update.releases:
            cert = update.certificate(tooth)
            check("strict_first_crossing", update.before.radius <= tooth < update.after.radius)
            check("automatic_shallow_cap", Q(0) < cert.excess <= cert.smallest_width)
            exact_loss = cert.deficit()
            check("exact_loss_is_probability", Q(0) < exact_loss < 1)
            if tooth == 1:
                widths = tuple(Q(1, 2*j+1) for j in range(1, step + 1))
                check("classic_loss_vs_full_cdf", exact_loss == 1 - br.window_mass(widths))
            events.append({
                "tooth": tooth, "stage": step, "last_denominator": 2*step+1,
                "previous_radius": str(update.before.radius),
                "radius": str(update.after.radius),
                "formula": "excess**step / (2**(step-1) * step! * width_product)",
                "excess": str(cert.excess), "width_product": str(cert.width_product),
                "loss_numerator_bits": exact_loss.numerator.bit_length(),
                "loss_denominator_bits": exact_loss.denominator.bit_length(),
                "approximate_log10_loss_display_only": cert.approximate_log10_deficit(),
            })
        state = update.after
    check("first_three_releases", [(e["tooth"], e["stage"]) for e in events] == [(1, 7), (2, 56), (3, 418)])

    # A constant rational clock demonstrates the same productive interface
    # without spending an exponential odd-width budget for each source label.
    state = br.RatchetState()
    labels, prime_reports = [], []
    for _ in range(180):
        update = state.advance(Q(1, 2))
        for tooth in update.releases:
            label = tooth + 1
            labels.append(label)
            if br.integer_charge_filter(bank, omega(label)-1) == 1:
                prime_reports.append(label)
        state = update.after
    check("constant_clock_visits_each_intermediate", labels == list(range(2, 91)))
    check("constant_clock_reports_authentic_primes",
          prime_reports == [n for n in range(2, 91) if sieve[n]])
    for circumference in (2, 5, 11):
        for n in labels:
            address = br.LiftedAddress.from_label(n, circumference)
            check("retained_lift_recovers_source", address.label == n)
            for multiplier in (2, 3, 5):
                check("source_braid", address.successor().multiply(multiplier) ==
                      address.multiply(multiplier).successor(multiplier))

    null = br.RatchetState()
    for stage in range(1, 65):
        null = null.advance(Q(1, 2**stage)).after
    check("summable_null", null.radius == 1-Q(1, 2**64) and null.clicks == 0)

    paths = [HERE / name for name in ("borwein_ratchet.py", "borwein_probe.py",
             "borwein_independent_audit.py", "cylinder.py")]
    paths.append(ROOT / "observational_succ/borwein_prime_clock.py")
    return {
        "schema": "borwein-ratchet-probe-v1", "status": "PASS", "failures": 0,
        "explicit_checks": sum(groups.values()), "checks_by_group": groups,
        "source_label_range": [1, limit], "first_releases": events,
        "constant_width_observer": {"width": "1/2", "stages": 180,
            "visited_labels": [2, 90], "prime_reports": prime_reports},
        "scope": {"infinite_claims_supported_by_written_proofs": True,
                  "finite_run_is_universal_proof": False,
                  "new_beta_reduction_trace": False,
                  "physical_ratchet_tested": False,
                  "asymptotic_speedup_claimed": False},
        "sha256": {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                   for path in paths},
    }


if __name__ == "__main__":
    print(json.dumps(run_probe(), indent=2, sort_keys=True))
