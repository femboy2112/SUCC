# Exact finite selected Fourier and signed cross-block certificates

**Status: PROVED LOCAL finite interval algorithm; no infinite cancellation theorem.**
Parent source: PR #310 at `a8c7c85b7a1900d422090f1757c174e7aac69f44`.

This instrument evaluates the actual source-selected characters, rather than a
phase-blind coefficient or auxiliary packet character. It imports the existing
literal carry adapter `pi_lag_carry.bbp_carry_path`; that adapter uses the original
four-pole forcing and zero initial state. Tests compare it with the independent
existing unwrapped-state adapter. The sources and probe are SHA-256 pinned in the
receipt. No frozen imported file is modified.

## Sound enclosure proof

The arctangent alternating-series theorem gives rational brackets for
`atan(1/5)` and `atan(1/239)`. The exact tangent addition identities give
`tan(4 atan(1/5))=120/119` and
`tan(4 atan(1/5)-atan(1/239))=1`; the latter angle is between zero and pi/2.
Thus `pi=16 atan(1/5)-4 atan(1/239)` provides a separate rational enclosure
for the universal circle-character normalization. This does not use pi digits
as orbit inputs or assume anything about their distribution.

For a rational phase `p`, reduce it to `[-1/2,1/2)`, round downward to the
`2^-b` grid, and round its angle `2 pi_mid p` to the same grid. The true angle
differs from the chosen rational angle by at most

`(2 pi_upper + 1) 2^-b + |p_grid| (pi_upper-pi_lower)`.

Real sine and cosine are 1-Lipschitz. Their Taylor polynomials through degrees
`2K+1` and `2K` have Lagrange errors bounded by
`|angle|^(2K+3)/(2K+3)!` and `|angle|^(2K+2)/(2K+2)!`, respectively (the
missing next coefficients vanish). Add the angle error and round the resulting
interval outward. These operations give certified rational rectangles for each
character. Endpoint and quarter-circle values are treated exactly.

Interval addition encloses the signed sum. Squaring an interval uses lower zero
if it straddles zero and otherwise the lesser endpoint square. Hence the sum of
the squared real and imaginary intervals encloses the squared modulus. Every
reported endpoint is rational; no floating-point decision certifies a bound.

For arbitrary disjoint consecutive blocks, the instrument retains

$$C=|S|^2-\sum_B|S_B|^2
  =\sum_{B\ne B'}S_B\overline{S_{B'}}.$$

This is the **real signed ordered off-diagonal sum**. It need not be positive.
Dependency loss in interval subtraction can widen its enclosure, but cannot
invalidate it. The exact two-phase control `(0,1/2)` gives total energy zero,
within-block energy two, and cross term minus two; dropping that term fails.

## Verification and boundary

The tests include exact roots of unity, a coherent positive control, a complete
17-point grid null control, an algebraic cosine/sine-square calibration at 1/3,
independent high-precision endpoint/prime-denominator holdouts, invalid inputs,
and a deliberately displaced enclosure. High-precision comparisons are
diagnostics; the rational remainder proof supplies soundness.

The deterministic receipt uses horizons 32 and 96 and fresh horizon 257,
frequencies 1, 2, 3, 7 as specified in the file, and retains the actual signed
cross-block intervals. These are finite observations only. A normal-looking
receipt cannot extend its quantifier from these horizons to all horizons.

Reproduce with the repository's Python environment and `PYTHONPATH` set to its root:

```sh
python -m unittest discover -s tests -p 'test_oily_signed_certificate.py' -v
python scripts/oily_signed_certificate_probe.py --write
python scripts/oily_signed_certificate_probe.py --verify
```

The next useful test is to evaluate a proposed source-derived **all-horizon**
cross-block inequality against these enclosures and coherent controls. This
calculator can falsify a proposed inequality at a finite horizon. It cannot
replace its proof.
