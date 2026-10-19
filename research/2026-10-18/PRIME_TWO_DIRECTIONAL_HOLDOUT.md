# TARGET C — Prime-two normalized directional inverse on a fresh high-mode holdout

**Status:** VERIFIED-EXACT-MODEL. **RH proved:** NO. **S4 first-window sign:** OPEN (AMBIGUOUS).
**Verdict:** REFUTED — a fresh high-mode holdout does **not** flip the S4 first-window sign.

Module: `observational_succ/prime_two_directional_holdout.py`
Test: `tests/test_prime_two_directional_holdout.py` (16 tests, all pass)

## Question

The single number claimed to "move S4" is the **B-normalized minimum eigenvalue** of the
#181 full-prime-two corrected first-window signed Schur lower, evaluated on a high-mode
window **distinct** from the one used to fit the comparator metric B. If that number were
`>= 0` on a fresh holdout, the first-window S4 sign would be certified positive there.

## Construction (all exact `fractions.Fraction`)

- **Inputs (provenance-pinned #181 certificates).**
  - FIT window: `research/2026-10-18/ROUND2_FULL_PRIME_J8.json` (J=8, M=80, P=18).
  - HOLDOUT window: `research/2026-10-18/ROUND2_FULL_PRIME_J24.json` (J=24, M=192, P=18).
  - Both carry `source_blob = 0cc8510b71d178fc79e8d410a86d8b6014cf9178` (== `original_continuum_residual.SOURCE_SHA`),
    `RH_proved: false`, `new_lower_PSD: false`, `first_window_sign_certified: false`.
  - The windows are genuinely distinct (M=80 vs M=192); the module raises if asked to fit
    and evaluate on the same window.
- **Comparator metric B.** B = the FIT-window high-mode source Gram
  (`continuum_residual_Gram`). It is strictly positive definite in both parity sectors
  (`B00 > 0` and `det(B) > 0`), so PSD in the B metric is equivalent to ordinary PSD — the
  independent-metric cross check is built in and asserted.
- **Corrected holdout lower.** `corrected = old_lower + C_hat`, where `C_hat` is the
  **single better enclosure** of the operator excess `C = D - kappa*I`.

### Never-sum rule (Academic Main IV audit), enforced in code

The #181 **center/edge resolvent** saving `C >= w0 (I - A_b)` (JSON `gain`) and the
#182-style **directional inverse** saving `C >= Z G^-1 Z*` (JSON `source_inverse_saving_lower`)
are two lower bounds on the **same** excess `C`. They must **not** be added. The module:

- selects `C_hat` as the one with the **larger exact Gershgorin floor** (`better_single_enclosure`);
- `reject_double_count(...)` raises `PrimeTwoHoldoutError` on any bound equal to the
  elementwise sum `gain + source_inverse_saving_lower`;
- a regression test confirms the returned `corrected` is `old + C_hat`, never `old + gain + direct`.

In both sectors the **directional inverse** has the better floor, so it is chosen.

## Exact certificate (holdout J24, B fit on J8)

For each sector, the B-normalized spectrum of `corrected` solves
`det(B) λ² − T λ + det(corrected) = 0`, `det(B) > 0`,
`T = trace(B⁻¹ corrected) · det(B)`. The matrix is PSD in the B metric **iff**
`det(corrected) ≥ 0` **and** `T ≥ 0`. Both sectors give `det(corrected) > 0` with `T < 0`,
so both B-normalized eigenvalues are strictly negative (`corrected` is negative-definite).

| sector | κ | chosen enclosure | resolvent floor | directional floor | det(corrected) | T | B-norm min-eig | min-eig rational lower bound |
|---|---|---|---|---|---|---|---|---|
| odd  | 63/500  | directional_inverse | ≈ −6.749e−5 | ≈ −5.399e−5 | > 0 | < 0 | **negative** | ≈ −92.47 |
| even | 153/500 | directional_inverse | ≈ −9.174e−5 | ≈ −7.339e−5 | > 0 | < 0 | **negative** | ≈ −905.63 |

The `min_generalized_eigenvalue_rational_lower_bound` is an exact Fraction `(T − r)/(2 det B)`
with `r = sqrt_up(discriminant) ≥ √disc` a rigorous rational over-estimate, so it is a sound
lower bound on the true min generalized eigenvalue. (Decision of negativity does not depend on
the square root: `det > 0 ∧ T < 0` is already exact.)

The published #181 `new_lower` (= `old + gain`) is **also** non-PSD under the same metric B,
confirming the holdout outcome is not an artifact of the enclosure choice.

## Reading (firewall)

- The negative B-normalized min-eigenvalue is a **valid conservative lower** leaving the S4
  first-window sign AMBIGUOUS. It is **not** a negative Weil witness and says **nothing** about RH.
- A positive Gram / directional-inverse saving is **not** the completed Weil form; they are not
  identified.
- `Λ(p^k) = log p`; one real Archimedean Gamma; no nontrivial zeta-zero ordinate is a construction
  input; the whole pipeline reads frozen source-pinned certificates only.
- Finite exact-rational agreement is a VERIFIED-EXACT-MODEL instance check, **not** a proof.

## Outcome

The fresh high-mode holdout keeps the corrected first-window signed Schur lower strictly
non-PSD in both parity sectors. Therefore the S4 first-window sign is **uncertified** on the
holdout, and **S4 = A4 − R4 remains OPEN**. This **REFUTES** the hypothesis that a fresh
holdout flips the sign. No PSD event occurred, so no independent-metric stress escalation was
needed (the ordinary-metric cross check already agrees: non-PSD).

**Next falsification opportunity:** sharpen the even-parity-block κ′ (the binding constraint per
the Four-Body / CertifiedTrial note is the `1/κ = 50` amplification, not Young slack) and re-run
on a third independent (M,P) holdout; or replace the directional-inverse enclosure with a tighter
single Krein/Schur complement bound — still single, still never summed, still first-window only.
