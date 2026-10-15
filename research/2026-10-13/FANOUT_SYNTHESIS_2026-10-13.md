# Fan-out synthesis — 2026-10-13 (six tracks, reconciled)

**Branch:** `research/dsv4-periodic-tail-enclosure-2026-10-13`. **RH PROVED: no.**
Six parallel tracks: one write (source detectability), one red-team (adversarial), one numerics (optimal error), one literature recon (Nyman/Suzuki rates), one conjecture slate, one (recon) failed on model availability and was folded into the others' coverage. This note reconciles their outputs into ledger-ready conclusions.

## 1. New proved theorem — source-defect detectability horizon (SD-01/SD-02)

`observational_succ/source_detectability.py` (fleshes out C08/C12). For a single source defect `b'(d) = mu(d) + delta`:

- the finite interpolant `F_K(k) = sum_{m<=k} sum_{e|m} b'(e)` deviates from 1 **iff** `K >= d`;
- the **first** visible cell is exactly `k = d`, with `F_K(d) = 1 + delta` exactly (proof: the mutation contributes `delta * floor(k/d)`);
- **non-identifiability corollary:** for every finite horizon `K`, infinitely many distinct sources agree with `mu` on `1..K` — a finite observer can never rule out open-world differences.

Reproduces ZCR-08's `F_6(6) = -1` (delta = −2) as a special case. Status PROVED LOCAL; boundary = finite-horizon only (this is *not* global source identification — SD-02 is the negative half of the same coin).

## 2. Red-team findings — all three fixed

`evil-morty` attacked PTE-01/TS-01/MS-01 + the Lean. **No invalid bound, no over-estimate, no Lean unsoundness** was found (the sqrt refinement, tail bounds, and `B_low`/`B_high` directions all verified rigorous). Three real defects, now fixed with regression tests:

- **F1 (Medium, real bug):** `lcm > 1e6` crashed inside `residue()` (declared `L`-cap 1e8 vs `k`-cap 1e6). Fixed: `L`-cap lowered to 1e6 consistently.
- **F2 (Low, over-claim):** PTE-01 "strictly sharper for every nonempty family" fails for the all-zero family (`M = (1+0)^2 = 1`). Docstring corrected to "with at least one nonzero coefficient."
- **F3 (Low, over-claim + real regression):** TS-01 "lower strictly sharper for every nonempty family" fails when `m' = 1` (e.g. `a_2 = 4`, `F in {0,2}`): both bounds degrade by the truncation remainder `1/(J L^2)`. Docstring corrected.

## 3. Literature recon — the Nyman–Beurling rate is KNOWN (stop guessing)

`citadel-rick` pinned the published quantitative state (the SUCC `E_N*` is the classical squared distance `d_N^2` in the equivalent Dirichlet form):

- **Lower bound (unconditional):** `liminf d_N^2 log N >= sum_{Re rho = 1/2} m(rho)^2/|rho|^2` (Báez-Duarte–Balazard–Landreau–Saias, Adv. Math. 149 (2000); sharpened by Burnol, Adv. Math. 170 (2002)). Under RH this reads `d_N^2 log N >= 2 + gamma - log 4pi`.
- **Upper bound (conditional on RH):** `d_N^2 << (log log N)^{5/2+delta} (log N)^{-1/2}` (Balazard–de Roton, arXiv:0812.1689).
- **Sharp constant (RH + a mean-value hypothesis on `1/|zeta'(rho)|^2`):** `d_N^2 ~ (2+gamma-log 4pi)/log N` (Bettin–Conrey–Farmer, arXiv:1211.5191), attained by `V_N(s) = sum_{n<=N} (1 - log n/log N) mu(n)/n^s`.

So **`E_N* = Theta(1/log N)`** (not `(log N)/N`), and `E_N* -> 0` unconditionally is exactly RH — no unconditional upper bound can exist.

Suzuki 2606.09096 §7 is titled "Heuristic considerations" and proves only structural facts **under `A_∞>0` (RH)** about the infinite-interval limit space; it does NOT prove (1.12). The precise missing theorem is the finite-interval de Branges convergence `E_a -> E` carrying (1.11) to (7.6). Suzuki himself notes proving (1.12) would need `lambda = 0` for all large `a`, which is RH-equivalent — so Corollary 1.6 is not a short route.

## 4. Numerics — optimal error E_N* (TESTED MODEL, not a proof)

`daniel` computed the exact (high-precision, dps=60) optimal error, calibrated against `E_2* = 1 - ln 2` (recovered to 60 digits):

| N | E_N* |
|---|---|
| 2 | 0.30685281944005469058276787854182343192449986563974 |
| 3 | 0.09574778392775402661430811934014709003105690882873 |
| 4 | 0.06595169421556965355895907941992572044740051585557 |
| 5 | 0.03631901793818696047422749135750981806394372955267 |
| 6 | 0.03620803463690562840174885320818928103914413705004 |
| 7 | 0.02438836788524400644614166028424866093103525218641 |
| 8 | 0.02424452530652267314820583316791120499527793638106 |

Consistency: `E_N*` is non-increasing; the optimal coefficients are NOT the source-first `-mu(n)/n` family (which is much worse: 0.697 vs 0.307 at N=2, 0.429 vs 0.024 at N=7). The slow decay is consistent with `1/log N`, NOT with `(log N)/N`.

## 5. Conjecture slate — reconciled

`goldbach` produced a ranked slate; the key correction is applied here:

- **Rank 4 (`E_N* = Theta((log N)/N)`) is REFUTED** by the Burnol unconditional lower bound (`E_N* = Omega(1/log N)`) and by daniel's data. Correct target: `E_N* -> 0` at rate `(2+gamma-log 4pi)/log N` (conditional), lower bound `1/log N` (unconditional).
- **Rank 1** (single Mellin probe detection horizon `~ k^{s+1}`, polynomial) — cheap to confirm, worth doing.
- **Rank 3** (Möbius family not L²-optimal) — **confirmed by daniel's data** (`-mu(n)/n` is strictly worse than the optimizer at every N tested).
- **Rank 5/6/7** (ghost realizers generic; integer Mellin probes blind to Euler structure; blackout lattice = whole kernel) — open, attackable, valuable for C08/A08/C06.

This is the point of the fan-out: two same-model agents disagreed on the *most important number* (the E_N* rate), and the literature + data settled it against the naive guess. The conjecture slate is corrected, not silently promoted.

## Reproduce

```sh
python3 -m unittest tests.test_source_detectability tests.test_periodic_tail_enclosure tests.test_tail_split_enclosure
python3 research/2026-10-13/dsv4_periodic_tail_residue_ls.py   # daniel's numerics (mpmath)
```

Status labels: SD-01/SD-02 PROVED LOCAL; E_N* numerics TESTED MODEL; literature claims PROVED (unconditional/conditional as stated); slate CONJECTURED (with Rank 4 refuted).
