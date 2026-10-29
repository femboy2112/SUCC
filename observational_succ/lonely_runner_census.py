"""Complete two-entry census from proved bounds and exact source-band gaps.

Negative decisions use the rational gap criterion in CENSUS.md, never a
certificate generator's failure. Positive decisions receive an independently
checked interval chain and a separate exact max-min computation.
"""

from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
from math import lcm

from observational_succ.lonely_runner_two_entry import all_retained, general_effective_bounds
from observational_succ.lonely_runner_search import cover_certificate
from observational_succ.lonely_runner_verify import exact_maxmin, verify_cover


def _integer(value):
    if type(value) is not int:
        raise TypeError("an exact integer excluding booleans is required")


def encode_exact(value):
    if type(value) is F:
        return [value.numerator, value.denominator]
    if isinstance(value, dict):
        return {key: encode_exact(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode_exact(item) for item in value]
    return value


def canonical_bytes(value):
    return (json.dumps(encode_exact(value), sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")


def residual_gaps(n, speeds, *, max_intervals=250000):
    """Exact open complement components, using a common INTEGER time grid.

    The grid denominator is n*lcm(speeds). Each bad-band endpoint is an
    integer on that grid. This implementation does not use either existing
    Fraction band sweep or the independent certificate generator.
    """
    _integer(n)
    _integer(max_intervals)
    speeds = tuple(speeds)
    for velocity in speeds:
        _integer(velocity)
    if n < 3 or not speeds or min(speeds) < 1 or len(set(speeds)) != len(speeds):
        raise ValueError("require n>=3 and distinct positive speeds")
    if max_intervals < 1 or sum(speeds) + len(speeds) > max_intervals:
        raise ValueError("explicit source-band enumeration budget exceeded")
    denominator = n * lcm(*speeds)
    intervals = []
    for velocity in speeds:
        unit = denominator // (n * velocity)
        for winding in range(velocity + 1):
            intervals.append((max(0, (n * winding - 1) * unit),
                              min(denominator, (n * winding + 1) * unit)))
    frontier, gaps = 0, []
    for left, right in sorted(intervals):
        if left > frontier:
            gaps.append((F(frontier, denominator), F(left, denominator)))
        frontier = max(frontier, right)
    if frontier < denominator:
        gaps.append((F(frontier, denominator), F(1)))
    return tuple(gaps)


def single_band_winding(n, velocity, left, right):
    """A winding covering the whole open gap, or None; endpoint equality counts.

    Continuity makes covering (left,right) equivalent to containing its
    closure in one closed bad band. Bands are separated since n>=3.
    """
    _integer(n)
    _integer(velocity)
    if type(left) not in (int, F) or type(right) not in (int, F):
        raise TypeError("exact rational endpoints required")
    left, right = F(left), F(right)
    if n < 3 or velocity < 1 or not 0 <= left < right <= 1:
        raise ValueError("require n>=3, positive velocity and a nonempty unit-interval gap")
    lower = velocity * right - F(1, n)
    upper = velocity * left + F(1, n)
    first = -((-lower.numerator) // lower.denominator)
    last = upper.numerator // upper.denominator
    return first if first <= last else None


def gap_velocity_cap(n, gaps):
    """Largest possible speed covering every supplied gap, by maximum width."""
    _integer(n)
    if n < 3 or not gaps:
        raise ValueError("a nonempty residual gap list and n>=3 are required")
    lengths = []
    for left, right in gaps:
        if type(left) not in (int, F) or type(right) not in (int, F):
            raise TypeError("exact rational endpoints required")
        if not 0 <= left < right <= 1:
            raise ValueError("invalid residual gap")
        lengths.append(F(right) - F(left))
    bound = F(2, n) / max(lengths)
    return bound.numerator // bound.denominator


def complete_census(n, *, max_domain_candidates=1000000, progress=None):
    """Return a complete deterministic receipt and independently checked covers.

    The domain budget raises before enumeration: it cannot return a complete
    label for a truncated run. The finite domain itself comes from GAMMA-05.
    """
    _integer(n)
    _integer(max_domain_candidates)
    if n < 5 or max_domain_candidates < 1:
        raise ValueError("require n>=5 and a positive explicit execution budget")
    bounds = [(r1, r2, general_effective_bounds(n, r1, r2))
              for r1, r2 in combinations(range(1, n), 2)]
    domain_count = sum((2 * n - 3) * w1
                       for _, _, bound in bounds for w1 in range(n, bound["w1_max"] + 1))
    if domain_count > max_domain_candidates:
        raise ValueError(f"proved domain has {domain_count} candidates, exceeding budget {max_domain_candidates}")
    pairs, survivors, certificates = [], [], {}
    total_tested = total_width_rejected = total_first_speeds = 0
    transcript = sha256()
    for r1, r2, bound in bounds:
        source = all_retained(n, r1, r2)
        rows = []
        for w1 in range(n, bound["w1_max"] + 1):
            gaps = residual_gaps(n, source + (w1,))
            if not gaps:
                raise ArithmeticError("empty residual set contradicts GAMMA-05's one-insertion hole theorem")
            theorem_cap = 2 * (n - 1) * w1
            width_cap = gap_velocity_cap(n, gaps)
            cap = min(theorem_cap, width_cap)
            rejected_by_width = theorem_cap - max(w1, cap)
            total_width_rejected += rejected_by_width
            total_first_speeds += 1
            ranked = sorted(enumerate(gaps), key=lambda item: (-(item[1][1] - item[1][0]), item[0]))
            failures = [0] * len(gaps)
            accepted = []
            tested = 0
            for w2 in range(w1 + 1, cap + 1):
                tested += 1
                failure = next((index for index, (left, right) in ranked
                                if single_band_winding(n, w2, left, right) is None), None)
                transcript.update(canonical_bytes([r1, r2, w1, w2, failure]))
                if failure is not None:
                    failures[failure] += 1
                    continue
                velocities = source + (w1, w2)
                filename = f"census-n{n}-r{r1}-{r2}-w{w1}-{w2}.json"
                certificate = cover_certificate(velocities, [0] * len(velocities), F(1, n), source={
                    "campaign": "complete two-entry census", "n": n,
                    "removed": [r1, r2], "inserted": [w1, w2],
                    "source_family": "unshifted positive distinct integer speeds; gcd unrestricted",
                })
                verdict = verify_cover(certificate, require_counterexample=False)
                maximum = exact_maxmin(velocities, [[0, 1]] * len(velocities))
                if maximum["gamma"][0] * n > maximum["gamma"][1]:
                    raise ArithmeticError("gap criterion and independent max-min evaluation disagree")
                status = "tight" if maximum["gamma"] == [1, n] else "strict ordinary counterexample"
                item = {"removed": [r1, r2], "inserted": [w1, w2],
                        "velocities": list(velocities), "classification": status,
                        "certificate": filename, "certificate_sha256": sha256(canonical_bytes(certificate)).hexdigest(),
                        "independent_cover_verdict": verdict, "exact_maxmin": maximum}
                survivors.append(item)
                certificates[filename] = certificate
                accepted.append(w2)
            total_tested += tested
            rows.append({"w1": w1, "gaps": gaps, "maximum_gap": max(b-a for a, b in gaps),
                         "theorem_w2_cap": theorem_cap, "gap_width_w2_cap": width_cap,
                         "enumerated_w2_count": tested, "width_rejected_count": rejected_by_width,
                         "first_failed_gap_counts": failures, "accepted_w2": accepted})
        pairs.append({"removed": [r1, r2], "bounds": bound,
                      "first_speed_count": len(rows),
                      "proved_finite_domain_candidate_count": sum(row["theorem_w2_cap"] - row["w1"] for row in rows),
                      "width_rejected_count": sum(row["width_rejected_count"] for row in rows),
                      "gap_tested_count": sum(row["enumerated_w2_count"] for row in rows),
                      "gap_rejected_count": sum(sum(row["first_failed_gap_counts"]) for row in rows),
                      "accepted_insertions": [[row["w1"], w2] for row in rows for w2 in row["accepted_w2"]],
                      "largest_gap_width_cap": max((row["gap_width_w2_cap"] for row in rows), default=0),
                      "first_speed_transcript_sha256": sha256(canonical_bytes(rows)).hexdigest()})
        if progress is not None:
            progress(n, r1, r2, len(rows), sum(row["enumerated_w2_count"] for row in rows))
    if total_tested + total_width_rejected != domain_count:
        raise ArithmeticError("finite domain accounting is incomplete")
    receipt = {"schema": "SUCC-lonely-runner-complete-census-v1", "n": n,
               "complete": True, "all_positive_inserted_speeds_covered": True,
               "authority": "paper GAMMA-05 bound plus exact finite enumeration; not a full Lean kernel proof",
               "source_family": "([n-1] minus two distinct speeds) union {w1,w2}, n<=w1<w2, zero shifts; gcd unrestricted",
               "deletion_pair_count": len(pairs), "first_speed_count": total_first_speeds,
               "proved_finite_domain_candidate_count": domain_count,
               "width_rejected_count": total_width_rejected, "gap_tested_count": total_tested,
               "gap_rejected_count": total_tested - len(survivors),
               "survivor_count": len(survivors), "survivors": survivors,
               "negative_and_positive_transcript_sha256": transcript.hexdigest(), "pairs": pairs,
               "no_general_lonely_runner_claim": True, "academic_novelty_claim": False}
    return encode_exact(receipt), certificates
