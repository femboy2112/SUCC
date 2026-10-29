"""Complete two-entry census with proved baseline-gap and center pruning.

The original census stays unchanged. This variant caches the baseline gap
set and intersects it with integer-grid good bands of each first insertion.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import lcm

from observational_succ.lonely_runner_census import (
    canonical_bytes, encode_exact, gap_velocity_cap, residual_gaps, single_band_winding,
)
from observational_succ.lonely_runner_two_entry import general_effective_bounds
from observational_succ.lonely_runner_search import cover_certificate
from observational_succ.lonely_runner_verify import verify_cover


def baseline_first_bound(n, baseline):
    if type(n) is not int or n < 5 or not baseline:
        raise ValueError("require n>=5 and a nonempty baseline gap set")
    length = max(b-a for a, b in baseline)
    if length <= 0:
        raise ValueError("positive baseline gap length required")
    return F(4*(n-2), n*(n-4)) / length


def intersect_integer_good_bands(n, baseline, velocity):
    """Exact intersection of open baseline gaps with ||velocity*t||>1/n."""
    if type(n) is not int or type(velocity) is not int or n < 3 or velocity < 1:
        raise ValueError("integer n>=3 and positive velocity required")
    if any(not 0 <= a < b <= 1 for a, b in baseline):
        raise ValueError("nonempty rational unit-interval gaps required")
    denominator = lcm(n*velocity, *(x.denominator for gap in baseline for x in gap))
    unit = denominator // (n*velocity)
    answer = []
    for a, b in baseline:
        left, right = a.numerator*(denominator//a.denominator), b.numerator*(denominator//b.denominator)
        first = velocity*a.numerator//a.denominator
        last = min(velocity-1, velocity*b.numerator//b.denominator)
        for k in range(first, last+1):
            lo = max(left, (n*k+1)*unit)
            hi = min(right, (n*(k+1)-1)*unit)
            if lo < hi:
                answer.append((F(lo, denominator), F(hi, denominator)))
    return tuple(answer)


def center_modulus(n, removed, retained, first):
    """Necessary divisor of w2 from omitted centers not already covered by w1."""
    witnesses = tuple(r for r in removed if not any(v % r == 0 for v in retained))
    return lcm(*(r for r in witnesses if first % r != 0)), witnesses


def complete_referee_census(n, *, max_domain_candidates=250000000, progress=None):
    if type(n) is not int or n < 5:
        raise ValueError("integer n>=5 required")
    if type(max_domain_candidates) is not int or max_domain_candidates < 1:
        raise ValueError("positive integer budget required")
    specs = [(r1, r2, general_effective_bounds(n, r1, r2))
             for r1, r2 in combinations(range(1, n), 2)]
    raw = sum((2*n-3)*sum(range(n, b["w1_max"]+1)) for _, _, b in specs)
    if raw > max_domain_candidates:
        raise ValueError(f"proved domain {raw} exceeds explicit budget {max_domain_candidates}")
    totals = dict(first_speeds=0, first_speeds_occupancy_rejected=0,
                  first_occupancy_rejected=0, width_rejected=0,
                  center_rejected=0, individually_tested=0, gap_rejected=0)
    pairs, survivors, certificates = [], [], {}
    full_transcript = sha256()
    for r1, r2, old_bound in specs:
        source = tuple(v for v in range(1, n) if v not in (r1, r2))
        baseline = residual_gaps(n, source)
        strict = baseline_first_bound(n, baseline)
        old_cap = old_bound["w1_max"]
        cap = min(old_cap, (strict.numerator-1)//strict.denominator)
        skipped_rows = max(0, old_cap-max(n-1, cap))
        first_reject = (2*n-3)*sum(range(max(n, cap+1), old_cap+1))
        totals["first_speeds_occupancy_rejected"] += skipped_rows
        totals["first_occupancy_rejected"] += first_reject
        row_hash = sha256()
        counts = dict(first_speeds=0, width_rejected=0, center_rejected=0,
                      individually_tested=0, gap_rejected=0)
        accepted = []
        for w1 in range(n, cap+1):
            gaps = intersect_integer_good_bands(n, baseline, w1)
            if not gaps:
                raise ArithmeticError("empty one-insertion residual contradicts Gamma")
            full_cap = 2*(n-1)*w1
            width_cap = min(full_cap, gap_velocity_cap(n, gaps))
            width_reject = full_cap-max(w1, width_cap)
            modulus, witnesses = center_modulus(n, (r1, r2), source, w1)
            width_count = max(0, width_cap-w1)
            first_multiple = (w1//modulus+1)*modulus
            candidates = range(first_multiple, width_cap+1, modulus)
            center_reject = width_count-len(candidates)
            counts["first_speeds"] += 1
            counts["width_rejected"] += width_reject
            counts["center_rejected"] += center_reject
            ranked = sorted(enumerate(gaps), key=lambda x: (-(x[1][1]-x[1][0]), x[0]))
            row_failures = [0]*len(gaps)
            row_accepted = []
            for w2 in candidates:
                counts["individually_tested"] += 1
                failure = next((i for i, (a, b) in ranked
                                if single_band_winding(n, w2, a, b) is None), None)
                full_transcript.update(canonical_bytes([r1, r2, w1, w2, failure]))
                if failure is not None:
                    row_failures[failure] += 1
                    counts["gap_rejected"] += 1
                    continue
                speeds = source+(w1, w2)
                certificate = cover_certificate(speeds, [0]*len(speeds), F(1, n), source={
                    "campaign": "referee complete two-entry census", "n": n,
                    "removed": [r1, r2], "inserted": [w1, w2]})
                verdict = verify_cover(certificate, require_counterexample=False)
                name = f"referee-n{n}-r{r1}-{r2}-w{w1}-{w2}.json"
                item = {"removed": [r1, r2], "inserted": [w1, w2],
                        "velocities": speeds, "certificate": name,
                        "independent_integer_verdict": verdict}
                survivors.append(item)
                certificates[name] = certificate
                accepted.append([w1, w2]); row_accepted.append(w2)
            row_hash.update(canonical_bytes([w1, gaps, width_cap, modulus,
                                              width_reject, center_reject, row_failures, row_accepted]))
        for key in counts:
            totals[key] += counts[key]
        pairs.append({"removed": [r1, r2], "gamma_bound": old_bound,
                      "baseline_gaps": baseline, "baseline_first_strict_bound": strict,
                      "retained_first_cap": cap, "first_rows_occupancy_rejected": skipped_rows,
                      "first_occupancy_rejected": first_reject, **counts,
                      "accepted_insertions": accepted, "rows_sha256": row_hash.hexdigest()})
        if progress:
            progress(n, r1, r2, counts)
    accounted = (totals["first_occupancy_rejected"]+totals["width_rejected"]
                 +totals["center_rejected"]+totals["individually_tested"])
    if accounted != raw:
        raise ArithmeticError("complete finite domain accounting failed")
    return encode_exact({
        "schema": "SUCC-referee-complete-census-v1", "n": n, "complete": True,
        "all_positive_inserted_speeds_covered": True,
        "authority": "Gamma paper bounds, proved baseline pruning, exact integer enumeration",
        "deletion_pair_count": len(specs), "proved_domain_count": raw, **totals,
        "survivor_count": len(survivors), "survivors": survivors, "pairs": pairs,
        "candidate_transcript_sha256": full_transcript.hexdigest(),
        "not_a_full_lean_census_proof": True, "academic_novelty_claim": False,
    }), certificates
