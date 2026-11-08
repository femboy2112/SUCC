# SUCC Operation JOINT CHARACTER × SOURCE-ENTROPY GYROSCOPE (2026-11-06)

**Research only — stacked on parent draft PR #525.** Original four-pole source, literal `U0=0`, `main`, all historical contracts, `formal/`, workflows, import manifest and existing files unchanged. **Base-16 π normality, selected Weyl `o(1)` and RH remain OPEN.** No claim of world novelty.

## What changed mathematically

The parent realization-gyroscope research established that the observer's action–observation joint law can reconstruct the original circle phase exactly. This round asks which realized observers can *legitimately* certify normality from their own outputs, without accidentally injecting the normality they claim to see.

**JC-02:** A fixed-period chart on an expanding ×16 orbit (or on a BBP orbit with source perturbation tending to 0) preserves the exact yes/no verdict on Haar equidistribution, **both directions**. The same holds for charts Cesàro-close to one fixed periodic schedule. Sublinear chart variation alone fails (parent's irrational staircase countermodel).

**JC-03 (CLASSICAL):** Any **rational** initial-seed shift on the authentic original source has eventually periodic circle chart `16^n s`; hence all rational-seed completions have the **same unknown** normality verdict. A periodic `β=1/5` completion requires the **irrational** shift `s=1/5−π/16`.

**JC-04:** For a deterministic finite-state observer emitting one digit per input digit and consulting an explicitly declared finite-alphabet source tape, the exact finite sample `k`-block entropy deficit is controlled by a longer `L`-block output deficit, the source's own block entropy, the finite state count, and a sharp sampling-continuity budget. With a zero-entropy auxiliary tape, normal observed output **forces** normal source input. This is a classical data-processing/finite-state consequence, with a SUCC-local finite estimate.

**JC-05:** A concrete **reversible** 16-state, period-7 **source-clock** observer is realized using the authentic BBP first-pole denominator label and selected completed hex digits. Its action `a_n=(q_n+σ_n)/16` depends on the carrier's past and its source clock, and its observed output digit is `c_n=d_n+q_n+σ_n mod16`. The inverse is exact and causal. Thus **normality of the emitted source-clock word ⇔ normality of the original π digits**, not by treating the uncompleted rational `U_n` digits as π digits.

**JC-07 (new explicit signed gate):** Finite Pinsker + entropy transfer gives a theorem relating the original source-authenticated signed joint character **directly** to the transformed observed block entropy deficit. The missing arithmetic premise is one *growing logarithmic observation-depth* output entropy bound (J20); unlike a finite histogram, it would force the actual selected Weyl sums to vanish. The premise remains entirely **UNVERIFIED**. Logarithmic depth is not arbitrary: finite sample support imposes `Δ_C(L)≥L log16−log(N−L+1)`.

## Executed source-specific mathematical receipts

- **Original-source certified digits:** 1,536 consecutive base-16 digits of completed literal-zero BBP history from rational source-tail intervals (depth 12). **Independent rigorous Machin/arctangent intervals** agree on 128 digits and overlap the original source's exact completed-phase intervals at seven selected later indices up through n=913. All 200 original four-pole values checked against an independently assembled rational numerator/denominator expression.
- **Rigorous signed Weyl bounds (not floating evaluations)** for previously explored calibration epochs `[A,2A)`: `(A=223,h=1)` 0.052672448794–0.052672448803; `(223,2)` 0.055542748280–0.055542748289; `(457,1)` 0.051686285871–0.051686285880; `(457,2)` 0.042329803610–0.042329803619. These four epoch-mode pairs were inspected in an exploratory scratch calculation **before** the first GitHub preregistration and MUST NOT be counted as blind holdouts. Two genuinely fresh commit-first pairs from the untouched addendum are `(A=239,h=3)` 0.062069108483–0.062069108492 and `(A=503,h=3)` 0.007157640762–0.007157640771, registered in `PREREG_ADDENDUM.md` at GitHub commit `66598998` before measurement. Rational phase quantization, independent Machin π interval, Taylor polynomials and Lagrange error certify the intervals. They do **not** prove any decay as A increases.
- **Hostile controls:** the uniform 16th-root grid has certified character upper `<5×10^-12`; the coherent `β=1/5` periodic completion has certified **lower** `>0.999999999995` at the tested modes. Changing the first source value by +1/37 yields a certified digit mismatch at n=2; an unlogged source tape cannot reconstruct the real digit history.
- **Failed shortcut retained:** the reversible 16-state source-clock coding actually **worsened** the measured one- and two-block entropy deficits on all three fixed finite selected samples `N=384,768,1536`. Its J19 output-based signed bounds remain **vacuous above 1** at the tested epochs. Neither finite trend can promote an asymptotic statement.

## File guide and validation

- [THEOREMS.md](THEOREMS.md): all definitions, exact proofs, conditions, quantitative Fourier bridge and classical provenance.
- [PREREGISTRATION.md](PREREGISTRATION.md): committed before the *batch* holdout runner, but after prior exploratory inspection of the four initial signed pairs; see frozen `PREREG_ADDENDUM.md` for precise chronological disclosure; SHA256 `efcefe2c71f3d9898b7dd6f6b45f3cc7ed287cbef651bae66793fd43ae10cc32`.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md), [NEXT.md](NEXT.md): status ledger, rejected framings and next source-selective arithmetic target.
- [VALIDATION.md](VALIDATION.md), [FINITE_RECEIPT.json](FINITE_RECEIPT.json), [HOLDOUT_RAW.json](HOLDOUT_RAW.json): scope, exact hashes and machine-readable finite values.
- `joint_entropy.py`: authentic Fraction source and completed-digit oracle, Mealy observer and finite entropy budget.
- `independent_oracle.py`: independent Machin arctan rational digits and high-index phase overlap.
- `signed_certificate.py`: rational sine/cosine Taylor interval certificates for selected signed Weyl sums.
- `entropy_to_character.py`: **noncertifying floating diagnostic** of exact theorem J19 (records its vacuity).
- `test_joint_entropy.py`, `test_signed_certificate.py`, `test_entropy_to_character.py`: hostile isolated tests.
- `holdout_probe.py`: deterministic calibration/entropy case runner; `fresh_holdout_probe.py`: two commit-first signed cases; outputs included in `HOLDOUT_RAW.json` and `FRESH_HOLDOUT_RAW.json`.

**Actual local scope:** Python 3.13 standard library, `compileall` PASS, isolated `unittest discover` **29/29 PASS**, full independent rational oracle PASS, preregistered holdout probe PASS. The full >12k native SUCC suite, repository provenance scripts, Lean and hosted CI are **not claimed on this child exact head**. See `VALIDATION.md` and source SHA receipts.

## The precise next mathematical obstruction

An unconditional, source-and-zero-seed-specific bound on the **transformed output** `L(A)`-block entropy deficit, with `k(A)→∞`, `k/L→0`, `kL/A→0`, and `(k/L)Δ_C(L;[A,2A+k-1))→0`, would complete the signed character proof using JC-07. No such estimate has been proved. A statistical finite sample, a normal random seed, an observer's self-consistency or an artificial high-entropy external tape cannot substitute.
