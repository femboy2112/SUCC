# Original four-mode Suzuki/Weil Schur: the CertifiedTrial instrument

**Date:** 2026-10-16. **Branch:** `research/original-four-schur-certified-trial-2026-10-16`.
**Status:** VERIFIED EXACT MODEL (instrument) + PROVED LOCAL (residual theorem, transport) +
**UNVERIFIED / OPEN** (the sign `S_4`). **RH PROVED: NO.**

This dossier records a rigorous, exact-interval two-sided Loewner enclosure of the **original**
four-mode Suzuki/Weil Schur complement `S_4 = A_4 − R_4` at radius `a = 1/2`, the independent
reproduction of the inherited source certificates it stands on, the honest open obstruction that
keeps a decisive sign out of reach, and the four-mode ↔ thirty-mode transport structure.

It does **not** reconstruct ζ, Γ, the Euler product, or the completed signed Weil distribution.
Those are inherited, source-authenticated, exact-interval primitives
(`observational_succ.source_weil_hierarchy`, `.suzuki_legendre_source.authentic_full_low_entry`,
pinned blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`). We decide, as far as the mathematics honestly
allows, the **sign** of an already-constructed source operator.

## 1. The object

On the original Suzuki derivative carrier `u ∈ L²₀(−1/2,1/2)`, with `F_4 = span{P₁(2t),…,P₄(2t)}`,
`H = F_4 ⊕ H_high`, the authentic completed signed Suzuki operator and inverse-Neumann metric

```
G = [[A_4, B*],[B, D_4]],   K = (−Δ_N)^{-1} = V*V,   K^{-1} = −Δ_N,
R_4(x) = sup_{z∈H_high} ( 2 Re⟨Bx,z⟩ − ⟨D_4 z,z⟩ ),   S_4 = A_4 − R_4.
```

Inherited, now independently reproduced (§3): `A_4 ≻ 0`; `D_4 ⪰ κ Q_4 K Q_4` with `κ = 1/50`
(WB4, `tate_weighted_bessel_four_schur`); `‖g′‖₁ < 11/40` (`one_object_residual_schur`); the
zero-shift cap `R_4 ⪯ (11/40)²/κ · I = 121/32` on the `L²` metric. The autocorrelation support law
at `a = 1/2` activates the genuine prime-2 atom **only** — verified from
`authenticated_prime_wavefront(1/2) == ((2,2),)`, never hard-coded.

## 2. The residual theorem (independently re-derived)

For **any** finite rational parity-respecting high response `U : F_4 → H_high`, with
`Vx = x − Ux`, `r_U = B − D_4 U`, `L_U = U*B + B*U − U*D_4 U`, and the residual derivative Gram
`T_{r_U}(x) = ‖(r_U x)′‖² = ⟨r_U x, K^{-1} r_U x⟩`:

```
            A_4 − L_U − (1/κ) T_{r_U}   ⪯   S_4   ⪯   A_4 − L_U.
```

Re-derivation (not taken on faith from the prompt):

* **Upper.** `R_4(x) ≥ 2Re⟨Bx,Ux⟩ − ⟨D_4 Ux,Ux⟩ = L_U(x)` (use `z = Ux` as a trial in the sup),
  so `S_4 = A_4 − R_4 ⪯ A_4 − L_U`. Moreover `A_4 − L_U = ⟨Vx, G Vx⟩` exactly.
* **Lower.** Complete the square `z = Ux + w`:
  `R_4(x) = L_U(x) + sup_w( 2Re⟨r_U x, w⟩ − ⟨D_4 w,w⟩ ) ≤ L_U(x) + κ^{-1}⟨r_U x, K^{-1} r_U x⟩`
  using `⟨D_4 w,w⟩ ≥ κ⟨Kw,w⟩` and the Legendre transform of a `K`-quadratic. Because
  `K^{-1} = −Δ_N`, `⟨r_U x, K^{-1} r_U x⟩ = ‖(r_U x)′‖² = T_{r_U}(x)`, and `1/κ = 50`.

`r_U x = Q_high G Vx`, so `T_{r_U}` is the derivative energy of the **true infinite** high response.

## 3. What is CERTIFIED (exact interval; module `certified_four_schur_trial`)

`CertifiedTrial(U, J, precision, rank)` returns exact rational Loewner brackets `lower ⪯ S_4 ⪯ upper`:

* **A_4 ≻ 0 — VERIFIED EXACT MODEL.** `A_4(full) ⪰ A_4^{(J)}` (omitted Gamma tail PSD); the
  interval box of `A_4^{(J)}` gives `A_4^{(J)} ⪰ mid − r·I` (Loewner, `r` = max-abs-row-sum of the
  radius matrix). At `J = 64` both parity blocks clear: odd `min-eig ≳ 2.64·10⁻⁵`, even
  `min-eig ≳ 9.25·10⁻⁸` (unnormalized `P_n(2t)` metric, vs interval radius `≈1.7·10⁻¹⁴`; sign
  coordinate-independent). At `J ≤ 48` the even-block interval lower is negative (`≈ −3.6·10⁻⁶` at
  `J = 48`) → **not** certifiable, so the reproduction records the honest trajectory: fails at
  `J = 24, 48`, certified at `J = 64`. The even parity block carries a **small** positive margin (the
  tightest direction of the original four-mode low block), comfortably above the interval radius.
* **Upper bracket — rigorous.** `S_4 ⪯ A_4 − L_U = ⟨Vx,G Vx⟩ ⪯ (mid + r·I) + τ_J · W_L2(V)`, where
  `W_L2(V)` is the exact `L²` Gram of the trial vectors and `0 ⪯ (Gamma tail) ⪯ τ_J` with
  `τ_J = authentic_positive_gamma_tail_norm(J) = 2/(4J+1)² + 16/(4J+1)³`.
* **Lower bracket — rigorous, `U`-independent (inherited WB4 cap).** `S_4 = A_4 − R_4 ⪰
  (A_4 interval lower) − (121/32) W_L2(low)`, using the inherited, repo-proved zero-shift bound
  `R_4 ⪯ (11/40)²/κ · W_L2 = 121/32 · W_L2` (`true_four_low_suzuki_interface`). This is the honest
  certified floor. The sharper per-`U` residual-theorem tightening `A_4 − L_U − 50 T_{r_U}` is **not**
  used in the certificate: it needs a certified **upper** bound on the true infinite residual Gram
  `T_{r_U}`, and the naive generalized Young step `‖(Q_high G Vx)′‖ ≤ ‖(G Vx)′‖` is **false in
  general** (an `L²` projection can raise the derivative norm). That tightening is the open Section 3C
  modulus and is emitted only as a NON-CERTIFIED diagnostic (§7).

**Result (U = 0, rank 8, `J = 48`).** Upper bracket PSD (parity-block `min-eig ≳ 5·10⁻⁶ > 0`);
lower bracket indefinite (`min-eig ≳ −1.26·10⁻³`). Verdict: **CERTIFIED AMBIGUOUS** — `S_4` is not
certified positive and not certified negative, with the exact rational gap quantified. The same
verdict holds for every numerically-discovered-then-exactly-recertified trial `U` (§5).

Verdict logic (all via exact LDL on the two 2×2 parity blocks): `lower ⪰ 0 → POSITIVE_CERTIFIED`;
`upper` not PSD (exhibited negative direction) `→ NEGATIVE_CERTIFIED`; else `AMBIGUOUS`; source /
domain / normalization / provenance failure `→ INVALID_SOURCE`.

## 4. Reproduction & comparison table (Section 4 of the campaign)

Independent reproduction of the inherited certificates (read-only probe sweep; pinned source blob
`0cc8510b…` **MATCH, no drift** throughout):

| Quantity | Prior source (claim) | This round (independent) | Status |
|---|---|---|---|
| `A_4` sign | `A_4 ≻ 0` asserted (WB4) | CERTIFIED `≻0` at `J=64`, both parity blocks (interval) | VERIFIED EXACT MODEL |
| 4-mode high coercivity `κ` | `1/50` (WB4) | reused `1/50`; recomputed cap `50·(11/40)² = 121/32` | CLASSICAL IMPORT |
| WB4 four-moment margin | `20699/1000000` | reproduced `20699/1000000` (`Γ>6097/1000`, `W<2013/10000`) | VERIFIED EXACT MODEL |
| sharper `R_0` (odd/even) | #137 `arithmetic_resolvent` | `405333569368851711757618861801/891024077979000000000000000000` (odd), `107959895025855318145227769087/127289153997000000000000000000` (even) | CONDITIONAL |
| `S_4` two-sided bracket | numerical only (`four_low_schur_proof_teeth`) | **exact interval** two-sided Loewner (this module) | VERIFIED EXACT MODEL |
| `S_4` sign | OPEN (both signs) | OPEN — CERTIFIED AMBIGUOUS | UNVERIFIED |
| #144 cofinal oracle | conditional | `cofinal_actual_source_oracle_integrated = False` (not implemented) | CONDITIONAL |
| #147 spline Gram | PD `2×2` | eigenvalues `63219/14336`, `7075/18432` (>0); cross-check, **not** a first `A_4>0` proof | PROVED LOCAL |
| 30-mode coercivity `κ_30` | `369/10000` (moment30) | reproduced; shown **not** to transport to `S_4` (§6) | PROVED LOCAL |

## 5. The binding constraint (Section 5A diagnosis)

The verdict is AMBIGUOUS, but *why* is the decisive question, and the honest answer is sharper than
"the Young cap is conservative." At the numerically optimal `U`, the **tight** (continuum) residual
bracket `A_4 − L_U − (1/κ)C_quot` is itself **negative-definite** — its four eigenvalues are all
`< 0` (`≈ −5·10⁻² … −1·10⁻⁵`). So even a perfectly tight, certified residual Gram would **not** flip
the verdict to POSITIVE under the current coercivity. The binding constraint is the **`1/κ = 50`
amplification** of the residual energy — equivalently the high-sector coercivity constant
`κ = 1/50` is too small, and/or the genuine low/high arithmetic residual coupling is too large — not
the conservatism of the `L¹` estimate. The even parity block (the tightest direction of `A_4`, §3)
is where the lower bracket is most negative.

This localizes the next decisive lever: a **sharper high-sector coercivity `κ`** (a better theorem
than `D_4 ⪰ K/50`), and/or a residual theorem that does not pay the full `1/κ`.

## 6. Four-mode ↔ thirty-mode transport (Section 6; exact finite models)

`F_4 ⊂ F_30 ⊂ H`, but the two Schur reductions cut at different modes (`≥5` vs `≥31`).
Module `four_thirty_schur_transport`, both facts PROVED LOCAL by exact rational models:

* **Transitivity (Haynsworth quotient).** `Short_{F_4}(G) = Short_{F_4}(Short_{F_30}(G))`, i.e.
  `S_4 = Short_{F_4}(S_30)`. A certified two-sided `S_30` enclosure therefore transports to `S_4` by
  an **exact finite 26-mode (modes 5..30) shorting** — a genuine acceleration **iff** `S_30` is
  easier to certify (it is not: `S_30` carries the same modes-`≥31` infinite tail).
* **Coercivity no-go.** `κ_30 = 369/10000 > κ_4 = 1/50`, but `κ_30` protects only modes `≥31`.
  Going `S_30 → S_4` shorts the **signed, unprotected** modes 5..30. Exact countermodel
  (`D_rest = diag(ε, c)`, low coupling `b` to the near-null `ε`-direction):
  `Short_{low}[0,0] = 1 − b²/ε`, **independent of the coercive `c`** — negative (`= −9` for
  `ε=1/10, b=1`) for every `c ∈ {1, 10², 10⁴, 10⁸}`. The thirty-mode coercivity does **not** decide
  the four-mode sign; the signed intermediate shorting does. Consistent with `S_4` OPEN.

## 7. The open obstruction — the §3C modulus (named wall)

A tight **certified** lower bracket needs a rigorous **upper** bound on `T_{r_U}` (the derivative
Gram of the true infinite high response). We have:

* the `U`-independent inherited WB4 cap `R_4 ⪯ 121/32 W_L2` (rigorous, used as the certified floor);
* a finite-mode exact-interval residual Gram **diagnostic** (truncated at the working `rank`,
  `tail NOT bounded`), which the module returns explicitly labeled **NON-CERTIFIED** and which never
  gates a verdict.

The missing lemma is a **certified high-Legendre-coefficient decay / effective derivative-Gram tail
modulus** for the source response: the high coefficients `c_k = ⟨P_k, G Vx⟩` are exact intervals and
the Legendre derivative Gram `⟨P_k′,P_l′⟩` is exact rational, so the only gap is a certified bound on
the `k > M` tail (governed by the explicit kinks of `g′` — the prime-2 hinge step and the `|r|`
corner, suggesting an `H^{1/2}`-type `O(1/M)` modulus). Delivering it would make the tight residual
Gram rigorous. Per §5 it would still not, alone, flip the verdict without a larger `κ` — so it is
necessary but not sufficient.

## 8. Status ledger (8-level taxonomy)

| Claim | Level |
|---|---|
| `A_4 ≻ 0` at `a=1/2` (even block margin ≈`9.25·10⁻⁸`, tightest direction) | VERIFIED EXACT MODEL |
| Residual theorem `A_4−L_U−50T_{r_U} ⪯ S_4 ⪯ A_4−L_U` | PROVED LOCAL |
| Exact two-sided certified Loewner enclosure of `S_4` | VERIFIED EXACT MODEL |
| `S_4 ⪰ 0` (sign) | UNVERIFIED / OPEN |
| `S_4 ≺ 0` in some direction (negative witness) | UNVERIFIED (none found; upper bracket PSD) |
| Binding constraint = `1/κ` amplification | NUMERICAL OBSERVATION + CONDITIONAL |
| `S_4 = Short_{F_4}(S_30)` transitivity | PROVED LOCAL |
| `κ_30` does not transport past signed mid-block | PROVED LOCAL (exact countermodel) |
| §3C certified tail modulus | CONJECTURED (named wall) |
| completed signed Weil **distribution** (CTW-08) | CLASSICAL IDENTIFICATION |
| source-derived **positive factorization** | UNVERIFIED / RH-hard |

**RH PROVED: NO.** A certified positive `S_4` would be a first-window (`a = 1/2`) theorem, not RH at
all support radii. A certified negative direction would be extraordinary and is reported with its
exact rational witness for hostile independent verification; none was found.

Instruments: `observational_succ/certified_four_schur_trial.py`,
`observational_succ/four_thirty_schur_transport.py`,
`scripts/certified_four_schur_trial_probe.py`,
`tests/test_certified_four_schur_trial.py`, `tests/test_four_thirty_schur_transport.py`.
