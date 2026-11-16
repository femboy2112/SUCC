# Exact local validation and limitations — 2026-11-15

**Scope:** isolated standard-library research scripts, independent of the rest of SUCC, under a directory later proposed for a draft PR. Source baseline is `main` `db9fb4b84672050efa79b13377f1e73364598a14`. No original source, default, archived text, manifest or workflow changed.

## Executed commands and results

- `python -m unittest -v test_probe.py`: **24 tests PASS**, using the exact production `probe.py` imported by `test_probe.py` (see `TEST_OUTPUT.txt`).
- `python probe.py`: **PASS**; produced `FINITE_REPORT.json` for preselected finite shells `B=[8,16,32,64,96]`, literal `U_0=0`, authentic four poles, strictly rational Green enclosures, and exact signed critical-frequency phase jumps.
- Exact 2-adic stable-clock residue permutations: **16/16, 256/256, 4096/4096 distinct** for stable clock and zero-seeded original recurrence from the literal first block; corroborates the proved all-depth isometry and newly proved `F(0)=0`, not constituting those analytic proofs.
- Exact origin modular sanity check: `F(0) ≡ 0 (mod 16^256)` **OBSERVED-FINITE**. The infinite identity is proved separately by a source-root-filter/p-adic logarithm paper derivation in `THEOREMS.md` §2a, independently algebraically checked against the eight roots using SymPy (NOT an independent theorem prover).
- Independent-formula comparisons: polynomial forcing vs four partial-fraction poles, modulo-4096 valuation checks, global-root BBP interval vs shifted rational source/tail intervals, direct DFT vs digit-product Fourier matrix, selected Gram-row unitarity, exact source seam identity vs complex numerical evaluation, and high-depth sample-floor calibration, plus odd-denominator/source-winding transport, the source polynomial root list and cancellation identities, the pole-coefficient mutation counterexample, 32 exact backward-source rational predecessor/valuation controls (through 2^32-adic precision), and the source-attached mixed Fourier Parseval noncollision floor.

## Independent symbolic algebra oracle (executed)

An external SymPy polynomial oracle, **not imported into the pure-standard-library test suite**, checked that `Q(z)=4-2z^3-z^4-z^5=(1-z)(z²+2)(z²+2z+2)` and all eight roots `±sqrt(2), ±i sqrt(2), ±1±i` satisfy `alpha^8=16`; `Q(alpha)=0` for `±i sqrt(2)` and `-1±i`; `alpha Q(alpha)=-16` at both `±sqrt(2)`; and `(1-sqrt(2))(1+sqrt(2))=-1`. The 2-adic convergence, root-filter identity and torsion logarithm law are supplied as **paper derivations**, not established by the SymPy algebra checks. A finite modular check and an algebraic audit are distinct from a blind independent mathematical referee.

## Exact negative-index carrier / valuation observations

The origin proof plus source isometry yields the *all-m* paper identity `v2(sum_{j=0}^{m-1}16^j r(-j)) = 4m+v2(m)`. Its finite checks independently evaluate the same original rational formula with negative 2-adic indices and compare 32 exact source predecessors to 2-adic stable clocks at depths 1,2,3,8. `F(-1)=-1/21` and `F(-2)=-2/231` are exact rational identities; no p-adic floating-point approximation is used. These tests do not establish the infinite theorem by themselves.

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
5. The critical-depth high-resolution positive Fourier norm has unavoidable diagonal floor `q/B-1`, verified on independent distinct-prefix controls. The **mixed** arithmetic/real Fourier bank has exact total norm `q/B` whenever `B<=q`, **including a coherent real phase control**; this is a further positive-energy no-go, not a normality theorem.

## What was NOT run or established

- Full 13k+ native SUCC test discovery and mandatory root provenance/observer/ordinal gates (the connected GitHub environment provides source access but not a runnable checkout of the entire repository here).
- Hosted CI at the eventual PR commit, Lean kernel certification, or an independent mathematical referee.
- Any original-zero source-selected all-large-shell signed Fourier saving, a bound for the joint observable (N-1), R0, or pi normality.
- Independent referee review, Lean kernel certification, or a separate proof from a different source of the infinite 2-adic origin identity `F(0)=0`. The included paper proof is not machine-checked at the infinite analytic step.

All generated diagnostics and code are research-only. Reproduction: `cd research/2026-11-15/bbp_circle_2adic_defect && python -m unittest -v test_probe.py && python probe.py`.
