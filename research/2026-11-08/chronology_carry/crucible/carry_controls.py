"""Independent rational controls for causal carry information.

No later source-clock measurements are read. The finite partition algorithm
enumerates rational floor boundaries, independently of the learned model,
Taylor phase engine, or common-denominator source implementation.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import prod
from pathlib import Path
import json


def floor(x):
    return x.numerator // x.denominator


def forcing(n):
    if type(n) is not int or n < 1:
        raise ValueError("positive integer time required")
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def offsets(base, fs):
    values = [Q(0)]
    for f in fs:
        values.append(base*values[-1]+f)
    return values


def internal_boundaries(slope, offset):
    """All y in (0,1) at which floor(slope*y+offset) changes."""
    out = set()
    for integer in range(floor(offset), floor(offset)+slope+2):
        y = (integer-offset)/slope
        if 0 < y < 1:
            out.add(y)
    return out


def transcript(y, base, rs):
    cs = [floor(base**j*y+r) for j, r in enumerate(rs)]
    return tuple(cs[j]-base*cs[j-1] for j in range(1, len(cs)))


def cell_receipt(base, fs):
    rs = offsets(base, fs)
    depth = len(fs)
    if base < 2 or depth < 1:
        raise ValueError("base >=2 and nonempty forcing required")
    cuts = {Q(0), Q(1)}
    for j in range(1, depth+1):
        cuts.update(internal_boundaries(base**j, rs[j]))
    cuts = sorted(cuts)
    full_count = 0
    cells = 0
    seen = set()
    for left, right in zip(cuts, cuts[1:]):
        cells += 1
        key = transcript((left+right)/2, base, rs)
        assert key not in seen, "a floor transcript is one interval"
        seen.add(key)
        width = base**depth*(right-left)
        assert width <= 1
        if width == 1:
            full_count += 1
    full_mass = Q(full_count, base**depth)
    lower = 1-Q(sum(base**j for j in range(depth)), base**depth)
    assert full_mass >= lower
    return {"base": base, "depth": depth, "cells": cells,
            "full_cells": full_count, "full_mass": str(full_mass),
            "proved_lower": str(lower)}


def green_coupling_receipt(t, depth):
    fs = [forcing(t+j) for j in range(1, depth+1)]
    rs = offsets(16, fs)
    tails = [rs[-1]/16**(depth-j)-rs[j] for j in range(depth+1)]
    assert tails[-1] == 0 and all(0 <= x < 1 for x in tails)
    eta = sum(tails, Q(0))
    budget = sum(fs, Q(0))/15
    assert eta <= budget < Q(1, 15*t)
    cuts = {Q(0), Q(1)}
    for j in range(depth+1):
        cuts.update(internal_boundaries(16**j, rs[j]))
        cuts.update(internal_boundaries(16**j, rs[j]+tails[j]))
    cuts = sorted(cuts)
    mismatch = Q(0)
    bad_boundary = Q(0)
    for left, right in zip(cuts, cuts[1:]):
        y = (left+right)/2
        ordinary = transcript(y, 16, rs)
        corrected_offsets = [r+tail for r, tail in zip(rs, tails)]
        corrected = transcript(y, 16, corrected_offsets)
        bjs = [floor(16**j*y+rs[j]+tails[j])-floor(16**j*y+rs[j])
               for j in range(depth+1)]
        for j in range(1, depth+1):
            assert corrected[j-1]-ordinary[j-1] == bjs[j]-16*bjs[j-1]
        assert bjs[-1] == 0
        if any(bjs):
            bad_boundary += right-left
        if ordinary != corrected:
            assert any(bjs)
            mismatch += right-left
    assert mismatch <= bad_boundary <= eta
    return {"start": t, "depth": depth, "partition_cells": len(cuts)-1,
            "exact_word_mismatch_measure": str(mismatch),
            "exact_any_floor_mismatch_measure": str(bad_boundary),
            "union_upper": str(eta), "source_upper": str(budget),
            "asymptotic_upper": str(Q(1, 15*t))}


def unwrapped(last, seed=Q(0)):
    states = [Q(seed)]
    carries = []
    for n in range(1, last+1):
        states.append(16*states[-1]+forcing(n))
        carries.append(floor(states[-1])-16*floor(states[-2]))
    return states, carries


def phase_pair_receipt(J, h, K=7, primes=(3, 5, 7, 11, 17)):
    original, carries = unwrapped(J)
    sigma = min((1-z % 1)/16**j for j, z in enumerate(original))
    N = J
    while 16**N*sigma < 1:
        N += 1
    exact_seed = Q(1, 2*abs(h)*16**N)
    _, exact_carries = unwrapped(J, exact_seed)
    assert exact_carries == carries and exact_seed < sigma
    assert (h*16**N*exact_seed) % 1 == Q(1, 2)
    M = 2**K*prod(primes)
    q = 2*abs(h)*16**N*M+1
    odd_seed = Q(M, q)
    _, odd_carries = unwrapped(J, odd_seed)
    assert odd_carries == carries and 0 < odd_seed < sigma
    assert odd_seed.denominator == q and q % 2 == 1
    assert odd_seed.numerator % 2**K == 0
    assert all(q % p == 1 for p in primes)
    half_gap = abs(abs(h)*16**N*odd_seed-Q(1, 2))
    assert half_gap == Q(1, 2*q)
    return {"prefix": J, "h": h, "future_time": N, "sigma": str(sigma),
            "exact_antipodal_seed": str(exact_seed), "odd_seed": str(odd_seed),
            "odd_seed_half_turn_gap": str(half_gap), "two_adic_bits": K,
            "preserved_local_places": list(primes),
            "squared_minimax_radius_lower": str(1-Q(5, 2*q*q))}


def future_digit_receipt():
    states, carries = unwrapped(50)
    checks = 0
    for n in (0, 1, 2, 7, 19, 41):
        for depth in (1, 2, 4, 8):
            if n+depth >= len(states):
                continue
            source = sum((16**(depth-j)*forcing(n+j) for j in range(1, depth+1)), Q(0))
            code = sum(16**(depth-j)*carries[n+j-1] for j in range(1, depth+1))
            x = states[n] % 1
            left = Q(code-source, 16**depth)
            right = left+Q(1, 16**depth)
            assert left <= x < right
            assert states[n+depth] % 1 == 16**depth*x+source-code
            checks += 1
    return {"exact_future_digit_cylinders": checks}


def run():
    cell_cases = []
    for base in (2, 3, 5, 16):
        for depth in (1, 2, 3):
            for fs in (
                [Q(0)]*depth,
                [Q((-1)**j*(j+1), 7+j) for j in range(depth)],
                [Q(j*j+3, 11) for j in range(depth)],
            ):
                cell_cases.append(cell_receipt(base, fs))
    source_cases = [green_coupling_receipt(t, depth)
                    for t in (1, 3, 11, 37) for depth in (1, 2, 3)]
    pair_cases = [phase_pair_receipt(J, h)
                  for J in (0, 1, 3, 8, 16) for h in (1, 3, -5)]
    result = {"status": "EXACT FINITE CONTROLS; paper theorems separately scoped",
              "implementation": "independent Fraction boundary enumeration",
              "source_family": "same four-pole forcing; ensemble and labeled nonzero controls",
              "later_source_holdout_accessed": False,
              "partition_cases": cell_cases, "green_coupling_cases": source_cases,
              "future_phase_pairs": pair_cases, **future_digit_receipt(),
              "pi_normality": "OPEN", "RH": "OPEN"}
    here = Path(__file__).resolve().parent
    result["code_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    result["proof_sha256"] = sha256((here/"THEOREMS.md").read_bytes()).hexdigest()
    return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"partition_cases": len(result["partition_cases"]),
                      "green_coupling_cases": len(result["green_coupling_cases"]),
                      "future_phase_pairs": len(result["future_phase_pairs"]),
                      "future_digit_cylinders": result["exact_future_digit_cylinders"]}))
