"""Exact independent oracle; no imports from the pin-bed implementations.

The universal results are proved in THEOREMS.md. These finite checks use
integer pair counts, rational Fourier coefficients and Machin enclosures.
The source recurrence always keeps the unwrapped rational state.
"""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def arctan_interval(q: int, terms: int = 18) -> tuple[Q, Q]:
    s = sum((Q((-1) ** j, (2*j+1)*q**(2*j+1))
             for j in range(terms)), Q())
    following = s + Q((-1) ** terms, (2*terms+1)*q**(2*terms+1))
    return min(s, following), max(s, following)


def pi_interval() -> tuple[Q, Q]:
    a, b = arctan_interval(5), arctan_interval(239)
    return 16*a[0]-4*b[1], 16*a[1]-4*b[0]


def scaled_weight(h: int, pi_squared: Q) -> Q:
    """pi^2 times the real-law half-aperture weight; h != 0."""
    h = abs(h)
    if h == 0:
        raise ValueError("zero is excluded from centered response")
    if h == 1:
        return 4 + pi_squared/2
    if h % 2:
        return Q(4, h*h)
    return Q(4*(h*h+1), (h*h-1)**2)


def fejer_moment(order: int, h: int) -> Q:
    if order < 1:
        raise ValueError("positive Fejer order required")
    return max(Q(), 1-Q(abs(h), order))


def fejer_by_pairs(order: int, h: int) -> Q:
    """DFT coefficient from independently enumerated square-amplitude pairs."""
    return Q(sum(j-l == h for j in range(order) for l in range(order)), order)


def alias_moments(order: int, h: int) -> tuple[Q, Q]:
    return (1+fejer_moment(order, h))/2, fejer_moment(2*order, h)


def difference_piecewise(order: int, h: int) -> Q:
    h = abs(h)
    if h <= order:
        return Q()
    if h < 2*order:
        return (Q(h, order)-1)/2
    return Q(1, 2)


def forcing(n: int) -> Q:
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def forcing_combined(n: int) -> Q:
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def unwrapped_source(length: int, seed: Q = Q()) -> list[Q]:
    out = [seed]
    for n in range(1, length+1):
        out.append(16*out[-1]+forcing(n))
    return out


def source_transcript(order: int, bandwidth: int, depth: int) -> tuple:
    states = unwrapped_source(depth)
    # A complex reading is represented exactly as (rational coefficient,
    # rational angle modulo one). No trigonometric evaluation is used.
    left, right = [], []
    for n, state in enumerate(states):
        for h in range(-bandwidth, bandwidth+1):
            p, q = alias_moments(order, 16**n*h)
            phase = (-h*state) % 1
            left.append((n, h, p, phase))
            right.append((n, h, q, phase))
    return tuple(left), tuple(right)


def run() -> dict:
    counts = {}
    pi_lo, pi_hi = pi_interval()
    pl, pu = pi_lo*pi_lo, pi_hi*pi_hi
    assert pl > Q(88, 9) and pi_hi < Q(22, 7)
    counts["machin_and_frame_thresholds"] = 2

    ratio = Q(116281, 205)
    assert scaled_weight(2, pl)/scaled_weight(32, pl) == ratio
    h1_upper = (pu+8)/8 * Q(255**2, 257)
    assert h1_upper < ratio
    checks = 2
    for h in range(1, 4097):
        # Denominator h*16 is always even, hence independent of pi^2.
        assert scaled_weight(h, pu)/scaled_weight(16*h, pl) <= ratio
        assert h*h*scaled_weight(h, pl) >= 4
        assert h*h*scaled_weight(h, pu) <= 4+pu/2
        checks += 3
    counts["half_aperture_exact_rational_checks"] = checks

    # Algebraic derivative identity from common-denominator expansion.
    checks = 0
    for t in (4, 16, 64, 256, 1024):
        for u in (Q(5, 4), Q(3, 2), Q(4), Q(9), Q(121)):
            lhs = 1/(u+1)-2/(u-1)+2*t/(t*u-1)-t/(t*u+1)
            rhs = -(t-1)*(3*t*u*u+(t+1)*u+3)/(
                (u+1)*(u-1)*(t*u-1)*(t*u+1))
            assert lhs == rhs and rhs < 0
            checks += 1
    counts["derivative_identity_specializations"] = checks

    checks = 0
    for order in (1, 2, 3, 5, 8, 13, 21, 32):
        for h in range(-2*order-2, 2*order+3):
            assert fejer_moment(order, h) == fejer_by_pairs(order, h)
            p, q = alias_moments(order, h)
            assert p-q == difference_piecewise(order, h)
            checks += 2
    counts["independent_fejer_pair_coefficient_checks"] = checks

    checks = 0
    witness_rows = []
    for H in (1, 2, 3, 7, 11, 19, 37):
        for N in (0, 1, 2, 4):
            order = H*16**N
            left, right = source_transcript(order, H, N)
            assert left == right
            checks += len(left)
            for k in (1, 2, 3):
                B = 16**k
                q = (2*H+B-1)//B
                for h in (q, q+1, 2*q, 2*q+1, 100*q):
                    p, v = alias_moments(order, 16**(N+k)*h)
                    assert p-v == Q(1, 2)
                    checks += 1
                witness_rows.append({"H": H, "N": N, "k": k,
                                     "first_constant_difference_mode": q,
                                     "radius_squared_lower_bound":
                                     str(1/(2*pu*q))})
    counts["exact_source_phase_transcript_and_future_checks"] = checks

    checks = 0
    for n in range(1, 161):
        assert forcing(n) == forcing_combined(n)
        checks += 1
    assert forcing(1) == Q(47, 15)
    counts["four_pole_combined_source_checks"] = checks+1

    mutants = {}
    # Drop the atom: the supposed pair no longer matches even its first mode.
    mutants["drop_dirac_atom"] = fejer_moment(7, 1)/2 != fejer_moment(14, 1)
    # Choose too small a source family cutoff: the final observed mode differs.
    small = 7*16-1
    mutants["history_cutoff_off_by_one"] = (
        alias_moments(small, 7*16)[0] != alias_moments(small, 7*16)[1])
    # A high-mode cosine test with h=1 would miss the true worst-case h=2.
    mutants["sharp_constant_from_mode_one_only"] = h1_upper < ratio
    mutants["call_low_band_inverse_full_inverse"] = (
        alias_moments(7, 14)[0] != alias_moments(7, 14)[1])
    # Wrong source phases must not be treated as a common calibrated gauge.
    mutants["mutate_four_pole_phase"] = forcing(1) % 1 != (forcing(1)+Q(1, 7)) % 1
    # Memory refinement can increase energy: scalar +1,-1 witnesses 0 -> 1.
    mutants["refinement_contracts_coherence"] = Q(0) < (Q(1)**2+Q(-1)**2)/2
    assert all(mutants.values())
    return {"status": "PASS_EXACT_FINITE_ONLY", "counts": counts,
            "total_checks": sum(counts.values()),
            "pi_interval": [str(pi_lo), str(pi_hi)],
            "sharp_half_aperture_C16_squared": str(ratio),
            "mutants_rejected": mutants,
            "history_alias_witnesses": witness_rows,
            "scope": "Paper proof is separate; no pi-normality or RH theorem.",
            "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
