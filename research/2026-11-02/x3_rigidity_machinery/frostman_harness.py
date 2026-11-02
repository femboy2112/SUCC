#!/usr/bin/env python3
"""
frostman_harness.py — CERTIFIED Frostman / non-concentration measurement harness
for the x16 orbit of pi, and validation controls.

Purpose
-------
Obligation (B) of the x3 rigidity route is:  dim_* mu > 0  for the empirical
accumulation  mu = lim_{N} (1/N) sum_{n} delta_{x_n}  of the completed orbit

    x_n = { 16^{n-1} pi },     x_{n+1} = { 16 x_n }  (exact).

dim_* mu > 0 is EQUIVALENT to a Frostman bound  mu(I) <= C |I|^s  for some
s > 0, uniformly over intervals I and horizons N.  This harness MEASURES the
sharpest empirical Frostman exponent

    s_N := min over dyadic intervals I of  log(mu_N(I)) / log(|I|),

where  mu_N = (1/N) sum_{n=1}^N delta_{x_n}  and I ranges over dyadic intervals
of length |I| = 2^{-k},  k = 0 .. K_max(N).

The orbit is EXACT (no floating-point error): the points x_n are the suffixes
of the base-16 digit expansion of pi, and a dyadic interval of bit-depth k is
determined by the first k binary bits of a point.  We therefore build a binary
trie over the (hex -> binary) digit string of pi and count suffix occupancies.

WHAT THIS CERTIFIES AND WHAT IT DOES NOT
----------------------------------------
CERTIFIES (exactly, unconditionally, up to the precision of the pi digits used):
  * the exact value of the finite-empirical quantity s_N for the *truncated*
    digit string of pi of the stated length (a finite computation),
  * the exact dyadic occupancy counts mu_N(I) for all dyadic I at depth <= K_max,
  * the exact values for the controls (Liouville / rational / random), which are
    generated with exact integer arithmetic or a fixed PRNG seed.

DOES NOT CERTIFY:
  * dim_* mu > 0 for the infinite orbit.  A finite horizon only produces a finite
    vector of occupancies; any finite computation can only *lower-bound* the
    apparent s at the observed scales.  It cannot rule out that some future
    (unseen) scale produces a heavier interval that drives the true liminf to 0.
  * the limit lim_{N->inf} s_N, nor that the limit equals 1 (normality), nor that
    the empirical s_N stays away from 0 at all future N.

This is a MEASUREMENT tool: it empirically locates the Frostman exponent and
validates that the trie machinery distinguishes dim_* = 1 from dim_* = 0 on
known controls.  It is not, and cannot be, a proof of dim_* > 0.

Scale convention (important)
----------------------------
For a finite empirical measure mu_N, a single point in an interval of length
2^{-k} gives mu_N(I) = 1/N, which violates mu_N(I) <= C |I|^s for ANY fixed
s>0 and C as soon as k > log2(N).  Hence the meaningful empirical Frostman
exponent is computed only over scales k <= K_max = floor(log2 N)  (i.e.
|I| >= 1/N).  As N -> inf, K_max -> inf and every scale is eventually covered.
This is the standard finite-horizon truncation of the lower Frostman dimension.

Author: Ravel.  Date: 2026-11-02.  Repo branch:
    research/x3-rigidity-machinery-2026-11-02.
"""

import argparse
import math
import random
import sys
import time
from fractions import Fraction

import mpmath as mp
from mpmath.libmp import to_man_exp

HEX_INDEX = "0123456789ABCDEF"

# Known first 64 hex digits of pi (after the point), for a cheap sanity self-check.
PI_HEX_64 = "243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89"  # first 64


# ---------------------------------------------------------------------------
# Exact base-16 digit string of frac(pi)
# ---------------------------------------------------------------------------
def pi_hex_digits(M):
    """Return the first M base-16 digits of frac(pi) = 0.hex..., EXACT.

    Uses mpmath's binary mantissa directly (no base-conversion rounding): the
    fractional part  frac = man * 2^exp  (exp < 0) has a binary expansion that is
    exactly the bit-string of `man` shifted by `exp` positions; grouping 4 bits
    gives the hex digits.  The required precision is D ~= 1.205*M decimal digits.
    """
    D = int(M * 1.205) + 32
    mp.mp.dps = D
    frac = mp.pi - 3                      # frac(pi), exact to D decimal digits
    man, exp = to_man_exp(frac._mpf_)     # frac = man * 2^exp
    L = man.bit_length()
    assert exp < 0, "expected fractional part (negative exponent)"
    lead = (-exp) - L                     # leading zero bits before top bit
    if lead < 0:
        lead = 0
    bits = "0" * lead + bin(man)[2:]      # fractional bits, MSB first
    need = 4 * M
    if len(bits) < need:
        # should not happen given the D margin, but pad defensively
        bits = bits + "0" * (need - len(bits))
    bits = bits[:need]
    out = []
    for i in range(0, need, 4):
        out.append(HEX_INDEX[int(bits[i:i + 4], 2)])
    return "".join(out)


def hex_to_bits(hx):
    """Convert a hex string to a binary bit string (4 bits per hex digit)."""
    return "".join(format(HEX_INDEX.index(c), "04b") for c in hx)


# ---------------------------------------------------------------------------
# Dyadic-trie Frostman exponent
# ---------------------------------------------------------------------------
def frostman_exponent_from_hex(hexstr, N, K_max, verbose=False):
    """Compute s_N = min_{k<=K_max} min_{dyadic I, |I|=2^-k} log(mu_N(I))/log(|I|).

    The N orbit points are the first N suffixes (in hex digits) of `hexstr`,
    i.e.  x_n = 0.hexstr[n : n+ceil(k/4)]... for the relevant prefixes.
    A dyadic interval of bit-depth k is a k-bit prefix of a point's binary
    expansion.  We build a binary trie of the N suffix bit-prefixes (to depth
    K_max bits) and count occupancy at each node.

    Returns:
      s_N            : the min over k<=K_max of (log(mu)/log(2^-k)).
      per_k          : dict k -> (min_ratio_at_scale_k, max_count_at_scale_k)
      trie           : nested dict representing counts (for inspection).
    """
    # Build the binary bit string covering enough hex digits for K_max bits.
    hex_needed = N + (K_max + 3) // 4 + 1
    hexstr = hexstr[:hex_needed]
    bits = hex_to_bits(hexstr)
    B = len(bits)

    # Trie as nested dict; node value = count of suffixes passing through.
    # We only need counts at depths up to K_max.
    # root = {}
    # Iterate over the N suffixes of the HEX string; each suffix's first K_max
    # bits come from the bit string starting at 4*n.
    counts = {}            # (depth, prefix_int) -> count
    # Use a compact per-depth dict of prefix->count.
    depth_maps = [dict() for _ in range(K_max + 1)]
    for n in range(N):
        start = 4 * n
        if start + K_max > B:
            break
        # walk bits; accumulate prefix as int
        pref = 0
        for k in range(1, K_max + 1):
            pref = (pref << 1) | (1 if bits[start + k - 1] == "1" else 0)
            d = depth_maps[k]
            d[pref] = d.get(pref, 0) + 1

    per_k = {}
    s_N = math.inf
    worst = None
    for k in range(1, K_max + 1):
        d = depth_maps[k]
        if not d:
            continue
        maxc = max(d.values())
        mu = maxc / N
        # log(mu)/log(2^-k) = log(mu) / (-k log 2)
        ratio = math.log(mu) / (-k * math.log(2.0))
        per_k[k] = (ratio, maxc)
        if ratio < s_N:
            s_N = ratio
            worst = (k, maxc)
    return s_N, per_k, worst


# ---------------------------------------------------------------------------
# Controls
# ---------------------------------------------------------------------------
def liouville_hex_digits(M):
    """Liouville-type alpha = sum 2^{-j!} (binary).  Return M hex digits of the
    fraction, computed EXACTLY as a bit string (integer arithmetic).

    Orbit of interest:  x_n = { 2^n alpha }  (the task's Liouville control).
    We return the binary expansion of frac(alpha) as hex, and the caller forms
    suffixes shifted by ONE BIT per step (base 2), not 4 bits.
    """
    # Build bit positions that are 1: those at 2^{-j!}.
    # We need bits up to 4*M.  Find max j with j! <= 4M.
    bits = ["0"] * (4 * M)
    j = 1
    fact = 1
    while True:
        # position (1-indexed fractional bit) = j!
        pos = fact
        if pos > 4 * M:
            break
        bits[pos - 1] = "1"
        j += 1
        fact *= j
    # convert to hex
    out = []
    for i in range(0, 4 * M, 4):
        out.append(HEX_INDEX[int("".join(bits[i:i + 4]), 2)])
    return "".join(out)


def rational_hex_digits(p, q, M):
    """Exact base-16 digits of the rational p/q (fractional part), via long
    division in base 16 (exact integer arithmetic).  Used as the dim_*=0 control
    (finite-support orbit)."""
    p %= q
    out = []
    for _ in range(M):
        p *= 16
        d = p // q
        p -= d * q
        out.append(HEX_INDEX[d])
        if p == 0:
            break
    while len(out) < M:
        out.append("0")
    return "".join(out)


def random_hex_digits(M, seed):
    """M uniformly random hex digits from a fixed-seed PRNG (reproducible)."""
    rng = random.Random(seed)
    return "".join(rng.choice(HEX_INDEX) for _ in range(M))


# ---------------------------------------------------------------------------
# Generic driver: build orbit suffixes from a hex string at a given base shift
# (4 bits for base-16, 1 bit for base-2 controls) and compute s_N.
# ---------------------------------------------------------------------------
def frostman_from_bitstring(bits, N, K_max):
    """Same trie as above but operating directly on a bit string, with the
    orbit being the first N suffixes of `bits` (1 bit per step).  Used for
    base-2 controls."""
    B = len(bits)
    depth_maps = [dict() for _ in range(K_max + 1)]
    for n in range(N):
        start = n
        if start + K_max > B:
            break
        pref = 0
        for k in range(1, K_max + 1):
            pref = (pref << 1) | (1 if bits[start + k - 1] == "1" else 0)
            d = depth_maps[k]
            d[pref] = d.get(pref, 0) + 1
    per_k = {}
    s_N = math.inf
    worst = None
    for k in range(1, K_max + 1):
        d = depth_maps[k]
        if not d:
            continue
        maxc = max(d.values())
        mu = maxc / N
        ratio = math.log(mu) / (-k * math.log(2.0))
        per_k[k] = (ratio, maxc)
        if ratio < s_N:
            s_N = ratio
            worst = (k, maxc)
    return s_N, per_k, worst


def hex_to_bitstring(hexstr):
    return hex_to_bits(hexstr)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Certified Frostman harness for the x16 orbit of pi")
    ap.add_argument("--N", type=int, default=10**6, help="horizon N (number of orbit points)")
    ap.add_argument("--seed", type=int, default=12345, help="PRNG seed for random control")
    ap.add_argument("--selftest", action="store_true", help="verify pi hex digits then exit")
    ap.add_argument("--controls", action="store_true", help="also run the three controls")
    args = ap.parse_args()

    N = args.N
    K_max = max(1, int(math.floor(math.log2(N))))

    if args.selftest:
        d = pi_hex_digits(64)
        ok = d == PI_HEX_64
        print(f"pi hex selftest (64 digits): {'PASS' if ok else 'FAIL'}")
        if not ok:
            print("  got   :", d)
            print("  expect:", PI_HEX_64)
        sys.exit(0 if ok else 1)

    print(f"# Frostman harness — x16 orbit of pi, N={N}, K_max={K_max}")
    print(f"#   K_max = floor(log2 N) = {K_max}  (|I| >= 2^-{K_max} = 1/{2**K_max})")
    print()

    # ---- Main orbit: pi ----
    t0 = time.time()
    hex_needed = N + (K_max + 3) // 4 + 2
    hexpi = pi_hex_digits(hex_needed)
    t_digits = time.time() - t0
    print(f"[pi] hex digits generated: {len(hexpi)}  ({t_digits:.2f}s)")

    t0 = time.time()
    s_pi, per_k_pi, worst_pi = frostman_exponent_from_hex(hexpi, N, K_max)
    t_trie = time.time() - t0
    print(f"[pi] trie built in {t_trie:.2f}s")
    print(f"[pi] s_N = {s_pi:.6f}   (worst interval: depth k={worst_pi[0]}, count={worst_pi[1]})")
    # trend summary across scales
    print("[pi] scale profile (k -> ratio):")
    for k in [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, K_max]:
        if k in per_k_pi:
            r, c = per_k_pi[k]
            print(f"    k={k:3d}  ratio={r:.6f}  maxcount={c}")

    # ---- Controls ----
    if args.controls:
        print()
        print("=" * 70)
        print("CONTROLS (validation of the tool)")
        print("=" * 70)

        # (a) Liouville-type: x_n = {2^n alpha}, alpha = sum 2^{-j!}, dim_* = 0.
        print("\n[control a] Liouville  alpha = sum 2^{-j!}   (expected s_N -> 0)")
        hexL = liouville_hex_digits(hex_needed)
        bitsL = hex_to_bitstring(hexL)
        s_L, per_k_L, worst_L = frostman_from_bitstring(bitsL, N, K_max)
        print(f"  s_N = {s_L:.6f}  (worst k={worst_L[0]}, count={worst_L[1]})")
        for k in [1, 2, 4, 6, 8, 10, 12, 15, K_max]:
            if k in per_k_L:
                r, c = per_k_L[k]
                print(f"    k={k:3d}  ratio={r:.6f}  maxcount={c}")

        # (a') rational p/q: exact periodic orbit, dim_* = 0 (theorem: finite support).
        print("\n[control a2] rational 1/17  (exact periodic orbit, dim_* = 0)")
        hexR = rational_hex_digits(1, 17, hex_needed)
        bitsR = hex_to_bitstring(hexR)
        s_R, per_k_R, worst_R = frostman_from_bitstring(bitsR, N, K_max)
        print(f"  s_N = {s_R:.6f}  (worst k={worst_R[0]}, count={worst_R[1]})")
        for k in [1, 2, 4, 6, 8, 10, 12, 15, K_max]:
            if k in per_k_R:
                r, c = per_k_R[k]
                print(f"    k={k:3d}  ratio={r:.6f}  maxcount={c}")

        # (b) random orbit: dim_* = 1.
        print("\n[control b] random iid uniform orbit   (expected s_N -> 1)")
        hexRand = random_hex_digits(hex_needed, args.seed)
        bitsRand = hex_to_bitstring(hexRand)
        s_Rand, per_k_Rand, worst_Rand = frostman_from_bitstring(bitsRand, N, K_max)
        print(f"  s_N = {s_Rand:.6f}  (worst k={worst_Rand[0]}, count={worst_Rand[1]})")
        for k in [1, 2, 4, 6, 8, 10, 12, 15, K_max]:
            if k in per_k_Rand:
                r, c = per_k_Rand[k]
                print(f"    k={k:3d}  ratio={r:.6f}  maxcount={c}")

    print()
    print("# NOTE: s_N is an EMPIRICAL lower-Frostman-exponent measurement at horizon N.")
    print("#       It does NOT certify dim_* mu > 0 for the infinite orbit (see module docstring).")


if __name__ == "__main__":
    main()
