"""Independent integer-only verifier for shifted lonely-runner circle covers.

No generator/search code is imported. Rational values are canonical integer
pairs and all comparisons use cross multiplication. A chain can contain only
the source-labelled closed arcs needed for a cover; full arc enumeration is
unnecessary for soundness. The optional exact max-min solver uses a separately
proved finite set of opposite-slope breakpoints, not sampling.
"""
from __future__ import annotations

import hashlib
import json
from math import gcd


SCHEMA = "SUCC-shifted-cover-v1"


class CertificateError(ValueError):
    """A purported mathematical certificate failed exact validation."""


class CandidateBudgetExceeded(ValueError):
    """Exact optimization was not attempted beyond a declared finite budget."""


def _integer(value, label):
    if type(value) is not int:
        raise CertificateError(f"{label}: an exact integer is required")
    return value


def _rat(value, label):
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise CertificateError(f"{label}: expected [numerator, denominator]")
    a, b = (_integer(value[0], label), _integer(value[1], label))
    if b <= 0 or gcd(a, b) != 1:
        raise CertificateError(f"{label}: denominator must be positive and pair reduced")
    return a, b


def _reduce(a, b):
    if b <= 0:
        raise ArithmeticError("internal rational denominator must be positive")
    g = gcd(a, b)
    return a // g, b // g


def _le(left, right):
    return left[0] * right[1] <= right[0] * left[1]


def _lt(left, right):
    return left[0] * right[1] < right[0] * left[1]


def _exact_json(value):
    """Reject floating-point and non-JSON payloads, including hidden metadata."""
    if value is None or type(value) in (str, int, bool):
        return
    if isinstance(value, list):
        for item in value:
            _exact_json(item)
        return
    if isinstance(value, dict) and all(type(key) is str for key in value):
        for item in value.values():
            _exact_json(item)
        return
    raise CertificateError("certificate payload must be JSON without floating-point values")


def payload_digest(certificate):
    """Canonical binding hash; provenance text itself remains an external claim."""
    if not isinstance(certificate, dict):
        raise CertificateError("certificate must be a JSON object")
    payload = {k: v for k, v in certificate.items() if k != "payload_sha256"}
    _exact_json(payload)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=True, allow_nan=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _configuration(velocities, shifts):
    if not isinstance(velocities, (list, tuple)) or not velocities:
        raise CertificateError("a nonempty velocity list is required")
    speeds = tuple(_integer(v, "velocity") for v in velocities)
    if any(v <= 0 for v in speeds) or len(set(speeds)) != len(speeds):
        raise CertificateError("velocities must be distinct positive integers")
    if not isinstance(shifts, (list, tuple)) or len(shifts) != len(speeds):
        raise CertificateError("one shift is required for each velocity")
    phases = tuple(_rat(s, "shift") for s in shifts)
    if any(not _le((0, 1), s) or not _lt(s, (1, 1)) for s in phases):
        raise CertificateError("each shift must lie in [0,1)")
    return speeds, phases


def _source_interval(velocity, shift, delta, winding):
    a, b = shift
    p, q = delta
    denominator = b * q * velocity
    left = _reduce(winding * b * q - a * q - p * b, denominator)
    right = _reduce(winding * b * q - a * q + p * b, denominator)
    if _lt(left, (0, 1)):
        left = (0, 1)
    if _lt((1, 1), right):
        right = (1, 1)
    if not _le(left, right):
        raise CertificateError("declared winding has an empty clipped source interval")
    return left, right


def verify_cover(certificate, *, require_counterexample=True):
    """Verify an all-time closed-arc cover and optionally its strict threshold.

    The default certifies gamma <= delta < 1/(n+1). With the option false,
    coverage at a non-strict or larger radius is allowed, explicitly labelled.
    There are no modular inverses or gcd-based time reductions in this proof.
    """
    fields = {"schema", "n", "velocities", "shifts", "delta", "threshold",
              "velocity_gcd", "source", "intervals", "ordering", "inequalities",
              "payload_sha256"}
    if not isinstance(certificate, dict) or set(certificate) != fields:
        raise CertificateError("unexpected or missing certificate fields")
    if certificate["schema"] != SCHEMA:
        raise CertificateError("unsupported certificate schema")
    digest = payload_digest(certificate)
    if certificate["payload_sha256"] != digest:
        raise CertificateError("payload SHA256 mismatch")
    if type(require_counterexample) is not bool:
        raise CertificateError("require_counterexample must be a boolean")
    n = _integer(certificate["n"], "n")
    speeds, shifts = _configuration(certificate["velocities"], certificate["shifts"])
    if n != len(speeds):
        raise CertificateError("n does not equal the number of moving runners")
    delta = _rat(certificate["delta"], "delta")
    threshold = _rat(certificate["threshold"], "threshold")
    if threshold != (1, n + 1):
        raise CertificateError("threshold must be 1/(n+1), counting moving runners")
    if not _le((0, 1), delta) or not _le(delta, (1, 2)):
        raise CertificateError("delta must lie in [0,1/2]")
    strict = _lt(delta, threshold)
    if require_counterexample and not strict:
        raise CertificateError("delta is not strictly smaller than 1/(n+1)")
    actual_gcd = 0
    for v in speeds:
        actual_gcd = gcd(actual_gcd, v)
    if _integer(certificate["velocity_gcd"], "velocity_gcd") != actual_gcd:
        raise CertificateError("declared velocity gcd is incorrect")
    if not isinstance(certificate["source"], dict) or not certificate["source"]:
        raise CertificateError("nonempty source/provenance metadata is required")

    intervals = certificate["intervals"]
    ordering = certificate["ordering"]
    inequalities = certificate["inequalities"]
    if not isinstance(intervals, list) or not intervals:
        raise CertificateError("a nonempty covering chain is required")
    count = len(intervals)
    if not isinstance(ordering, list) or len(ordering) != count:
        raise CertificateError("ordering must index every supplied interval once")
    if any(type(i) is not int for i in ordering) or set(ordering) != set(range(count)):
        raise CertificateError("ordering is not a permutation of interval indices")
    if not isinstance(inequalities, list) or len(inequalities) != count:
        raise CertificateError("one cross-product inequality per ordered interval is required")

    checked = []
    for item in intervals:
        if not isinstance(item, dict) or set(item) != {"runner", "winding", "left", "right"}:
            raise CertificateError("invalid source interval fields")
        runner = _integer(item["runner"], "runner index")
        winding = _integer(item["winding"], "winding")
        if not 0 <= runner < n:
            raise CertificateError("runner index out of range")
        left, right = _rat(item["left"], "left endpoint"), _rat(item["right"], "right endpoint")
        actual = _source_interval(speeds[runner], shifts[runner], delta, winding)
        if (left, right) != actual:
            raise CertificateError("endpoint does not match its runner, winding, shift and radius")
        checked.append((left, right))

    frontier = (0, 1)
    for step, index in enumerate(ordering):
        left, right = checked[index]
        claim = inequalities[step]
        if not isinstance(claim, dict) or set(claim) != {"left_cross", "right_cross"}:
            raise CertificateError("invalid cross-product inequality fields")
        actual_left = left[0] * frontier[1]
        actual_right = frontier[0] * left[1]
        if (_integer(claim["left_cross"], "left_cross") != actual_left or
                _integer(claim["right_cross"], "right_cross") != actual_right):
            raise CertificateError("declared cross-product inequality is incorrect")
        if actual_left > actual_right:
            raise CertificateError("uncovered open gap before an interval")
        if not _lt(frontier, right):
            raise CertificateError("cover chain must strictly advance its right frontier")
        frontier = right
    if frontier != (1, 1):
        raise CertificateError("cover chain does not reach time 1")
    return {
        "accepted": True,
        "authority": "exact integer interval certificate; not a Lean kernel claim",
        "all_time_cover": True,
        "strict_shifted_counterexample": strict,
        "n": n,
        "delta": list(delta),
        "threshold": list(threshold),
        "checked_intervals": count,
        "payload_sha256": digest,
    }


def _distance(velocity, shift, time):
    p = shift[0] * time[1] + velocity * time[0] * shift[1]
    q = shift[1] * time[1]
    r = p % q
    return _reduce(min(r, q-r), q)


def exact_maxmin(velocities, shifts, *, max_candidates=250000):
    """Exact gamma=max_t min_i ||s_i+v_i*t|| at all required breakpoints.

    Every maximum occurs where (v_i+v_j)t+s_i+s_j is integral, with i<=j.
    The raw candidate count is (n+1)*sum(v). The explicit budget is an
    execution limit, never a mathematical negative result. No floats, random
    search, LP solver, or cover-generator helper enters this computation.
    """
    speeds, phases = _configuration(velocities, shifts)
    _integer(max_candidates, "max_candidates")
    if max_candidates < 1:
        raise CertificateError("positive exact-candidate budget required")
    raw_count = (len(speeds) + 1) * sum(speeds)
    if raw_count > max_candidates:
        raise CandidateBudgetExceeded(f"{raw_count} raw candidates exceed budget {max_candidates}")
    candidates = {(0, 1)}
    for i, vi in enumerate(speeds):
        ai, bi = phases[i]
        for j in range(i, len(speeds)):
            aj, bj = phases[j]
            w = vi + speeds[j]
            denominator = bi * bj * w
            offset = ai * bj + aj * bi
            for k in range(w):
                candidates.add(_reduce((k * bi * bj - offset) % denominator, denominator))
    best, witness = (-1, 1), (0, 1)
    # Exact iteration order makes ties reproducible without rational float keys.
    for time in sorted(candidates):
        value = (1, 2)
        for velocity, phase in zip(speeds, phases):
            distance = _distance(velocity, phase, time)
            if _lt(distance, value):
                value = distance
            if _le(value, best):
                break
        if _lt(best, value):
            best, witness = value, time
    active = [i for i, (v, s) in enumerate(zip(speeds, phases))
              if _distance(v, s, witness) == best]
    return {
        "gamma": list(best),
        "maximizing_time": list(witness),
        "active_runners": active,
        "raw_breakpoint_bound": raw_count,
        "distinct_candidates_checked": len(candidates),
        "authority": "exact finite breakpoint evaluation with paper completeness proof",
    }
