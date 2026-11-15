# Exact local validation and limitations — 2026-11-15

**Scope:** isolated standard-library research scripts, independent of the rest of SUCC, under a directory later proposed for a draft PR. Source baseline is `main` `db9fb4b84672050efa79b13377f1e73364598a14`. No original source, default, archived text, manifest or workflow changed.

## Executed commands and results

- `python -m unittest -v test_probe.py`: **18 tests PASS**, using the exact production `probe.py` imported by `test_probe.py` (see `TEST_OUTPUT.txt`).
- `python probe.py`: **PASS**; produced `FINITE_REPORT.json` for preselected finite shells `B=[8,16,32,64,96]`, literal `U_0=0`, authentic four poles, strictly rational Green enclosures, and exact signed critical-frequency phase jumps.
- Exact 2-adic stable-clock residue permutations: **16/16, 256/256, 4096/4096 distinct**, corroborating the proved all-depth isometry, not constituting that proof.
- Exact origin candidate: `F(0) ≡ 0 (mod 16^256)` **OBSERVED-FINITE ONLY**; no proof that `F(0)=0` in `Z_2`.
- Independent-formula comparisons: polynomial forcing vs four partial-fraction poles, modulo-4096 valuation checks, global-root BBP interval vs shifted rational source/tail intervals, direct DFT vs digit-product Fourier matrix, selected Gram-row unitarity, exact source seam identity vs complex numerical evaluation, and high-depth sample-floor calibration.

## Original-zero finite shell observations (not asymptotic evidence)

| B | 16-adic depth k | q=16^k | Source seam hits | Global -1→0 seam hits | Signed parity sum | Exact moving h=q/2 jump |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 256 | 0 | 0 | 0 | 0 |
| 16 | 3 | 4096 | 3 | 0 | 1 | -1/8 |
| 32 | 3 | 4096 | 2 | 0 | 0 | 0 |
| 64 | 4 | 65536 | 8 | 0 | 0 | 0 |
| 96 | 4 | 65536 | 4 | 0 | 4 | -1/12 |

Every `D_{n,k}` and prefix is resolved using a finite **rigorously enclosed rational** original source tail. `max_future_terms_for_certification` is stored in the raw receipt. The *signed phase jump* is exactly rational because `h=q/2` reduces the grid characters to ±1. The strong claim `R0` remains unproved.

## Hostile and mutation controls

1. Arithmetic 2-adic U and real-digit reversal must **not** be identified: actual `U_1=47/15` yields `U_1 mod16=1`, real first hex digit `2`.
2. Original source and `s=1/16` rational alias have identical later circle phases, while literal seed passport differs and the 2-adic arithmetic difference is `16^(n-1)` at n≥1.
3. Same-forcing coherent counterseed `s=-pi/16` yields *every* critical seam `q-1 -> 0`, though its completed orbit is **constant 0** and nonnormal. This control's unwrapped state is irrational, not an odd-denominator rational element of Z_2.
4. A real-prefix increment is not generally the 2-adic adding machine on reversed code; only the global all-F seam has the compatible endpoint `-1 -> 0`.
5. The critical-depth high-resolution positive Fourier norm has unavoidable diagonal floor `q/B-1`, verified on independent distinct-prefix controls. It cannot be treated as a normality obstruction.

## What was NOT run or established

- Full 13k+ native SUCC test discovery and mandatory root provenance/observer/ordinal gates (the connected GitHub environment provides source access but not a runnable checkout of the entire repository here).
- Hosted CI at the eventual PR commit, Lean kernel certification, or an independent mathematical referee.
- Any original-zero source-selected all-large-shell signed Fourier saving, a bound for the joint observable (N-1), R0, or pi normality.
- A proof of the tempting infinite 2-adic identity `F(0)=0`; 256 finite modular precision levels do not imply it.

All generated diagnostics and code are research-only. Reproduction: `cd research/2026-11-15/bbp_circle_2adic_defect && python -m unittest -v test_probe.py && python probe.py`.
