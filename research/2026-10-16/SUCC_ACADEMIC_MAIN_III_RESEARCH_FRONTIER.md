# SUCC Academic Main III — research frontier & proof handoff (2026-10-16)

**Status:** research frontier / dependency graph. Establishes targets and records the hostile-audit
corrections of the PDQ (Gemini/DeepSeek) megaswarm; proves nothing new about RH by itself.
**RH PROVED: NO.** `S_4 = A_4 − R_4` sign remains **OPEN (AMBIGUOUS)** at `a = 1/2`.
Companion to [`FOUR_BODY_BREAKOUT_COMPLETE_QUOTIENT_AND_COERCIVITY.md`](FOUR_BODY_BREAKOUT_COMPLETE_QUOTIENT_AND_COERCIVITY.md),
[`PDQ_MEGASWARM_AUDIT_AND_THRESHOLD_OBSTRUCTION.md`](PDQ_MEGASWARM_AUDIT_AND_THRESHOLD_OBSTRUCTION.md),
[`ORIGINAL_FOUR_SCHUR_CERTIFIED_TRIAL.md`](ORIGINAL_FOUR_SCHUR_CERTIFIED_TRIAL.md) and
[`SUCC_POST_MAIN_II_PROOF_FRONTIER.md`](SUCC_POST_MAIN_II_PROOF_FRONTIER.md).

## 0. What survived the hostile audit, and what was repaired

Five independent read-only re-derivations (different methods, able to fail differently):

| Claim | Verdict | Note |
|---|---|---|
| PDQ-04/07 complete 4-moment quotient `E*P⁻¹E = 30c₁ᵀc₁+210c₂ᵀc₂+(1/24)M₃ᵀM₃+(1/40)M₄ᵀM₄` | **VERIFIED EXACT MODEL** | Loewner (sector rank-one, Gershgorin radius), not entrywise; coefficients confirmed 3 ways |
| PDQ-08 parity-split coercivity `κ_odd=63/500`, `κ_even=153/500` | **VERIFIED EXACT MODEL (source-conditional)** | Genuine all-`f` Cauchy–Schwarz bound; same footing as WB4 `1/50`; no falsifier possible |
| PDQ-09 B1+B3 derivative-energy bracket `(−0.029159, −0.015175)` | **VERIFIED EXACT MODEL (sound but loose)** | Exact-Fraction, no float; the prime-2 kink is in the kernel `g'`, so the integrand `g'*v` is continuous/Lipschitz (no jump cells) and the midpoint-Lipschitz enclosure is sound. But `V_J≈30.4 ≫` true Lipschitz `~0.8–1.5`: radius ≈`18× H'`, `≳98%` of the gap to 0 is enclosure, grid-specific (`~1/grid²`); radius-removed residual `≈(−5e-4,−6e-4)` still negative — refinement alone cannot flip the sign |
| PDQ-01/02/03/05/11/13 | PROVED PAPER/LOCAL | Unchanged |
| **1A** off-critical parity universal sign | **REFUTED → corrected** | `4Re(E²−O²)` indefinite `(2,2)`; split is real/imag, not parity |
| **1B** `ψ_e,ψ_o` normalization | manuscript-only | fixed; no computed number affected |
| **1C** threshold `τ*` "exact rational" | **REFUTED → certified bracket** | even-block generalized eigenvalue `(6.0151736313e-7, 6.0151736314e-7)` |
| **1D** nested-Schur monotonicity necessity | **overclaim → corrected** | sufficient not necessary; obstruction is to the computed bracket, not the true complement |
| **1E** even-sector "undetectability" | **overclaim → corrected + bug fix** | bandwidth-relative non-resolution; `T≥3` guard bug fixed |

## 1. Strongest authenticated Suzuki/Weil finite-source results (now)

1. **`A_4 ≻ 0`** at `a=1/2`, certified `J=64` (CFS-03), even-block margin `≈9.25·10⁻⁸`.
2. **High-sector coercivity** (source-conditional, exact rational): global `D_4 ⪰ (1/50)Q_4KQ_4` (WB4),
   sharpened per parity to `D_{4,odd} ⪰ (63/500)K_odd`, `D_{4,even} ⪰ (153/500)K_even` (PDQ-08).
3. **Complete degree-≤3 moment subtraction** `E*P⁻¹E` as an exact Loewner lower bound (PDQ-04/07),
   capturing `~25.8%` of the odd-mode-1 derivative energy via the boundary channels.
4. **Two-sided certified enclosure** of `S_4` (CFS-02) with the B1+B3 differentiated-convolution Gram
   moving the `U=0` lower bracket to `(−0.029159, −0.015175)` (PDQ-09) — still negative, and a sound-but-
   **loose, grid-specific** bracket (radius ≈`18× H'`; radius-removed residual `≈(−5e-4,−6e-4)`). This B1
   looseness is precisely the motivation for the direct quotient-energy certification in §4.

## 2. The genuine remaining first-window sign obstruction (the exact wall)

The binding constraint is **not** coercivity and **not** the Γ-tail; it is the **absolute scale** of the
derivative-energy / polynomial-moment channel relative to the `O(1e−8)` `A_4` margin:

- Exact threshold on the scalar-Young channel: `A_4-lo − τ·W_L2 ⪰ 0` iff `τ ≤ τ*`, with the certified
  even-block generalized eigenvalue `τ* ∈ (6.0151736313e-7, 6.0151736314e-7)` (Legendre-mass metric).
  The present `121/32` cap is `≈6.286·10⁶×` too large (1C).
- Even the full 4-moment subtraction + parity coercivity leaves the lower bracket negative
  (`−0.029/−0.015`). **Only per-vector, source-attested moment data at `~1e−7` precision can decide the sign.**
- The smallest decisive lemma is unchanged from Academic Main II (now sharpened): a **source-attested
  endpoint evaluator** `h(±a)` for `h = G v` with a rigorous omitted-Γ tail, feeding the two boundary
  channels `(ψ_e, ψ_o)` of `E*P⁻¹E` at `O(1e−7)`.

## 3. Repaired spectral-sign theory (the real no-go that replaced a false lemma)

The off-critical functional-equation quadruplet `{½±Δ±iγ}` contributes, for `g = f*f̃`, the real form
`Z = 4·Re((Lf_even)(z)² − (Lf_odd)(z)²)`, `z=Δ+iγ`. This is **indefinite** of inertia `(2,2)`: positive
directions `{Re E, Im O}`, negative `{Im E, Re O}`. The on-line Weil `|F|²` positivity (`Re z = 0`) does
**not** persist off the line — and that off-critical indefiniteness **is** the obstruction any spectral RH
attack must confront, not a lemma it gets for free. (This corrects the refuted "even ≥0 / odd ≤0" claim.)
**Frontier (Track D):** effective finite negative-witness complexity — distinguish exact support,
frequency resolution, truncation error, and finite-observer bandwidth; the `submersion` certificate is
bandwidth-relative non-resolution, so the witness re-emerges at larger `T`.

## 4. New machinery and its exact scope

- **Direct quotient-energy certification (Section 3 target).** The quantity entering the Schur estimate is
  `T_quot = T*Q_poly T` with `T: x ↦ (G v_x)'`, `Q_poly = I − Π_{≤3}`. The split-and-subtract route
  (bound `H'` above, `E*P⁻¹E` below, subtract) loses cancellation. The direct bound
  `T_quot ⪯ (1+η)T_J*Q_poly T_J + (1+η⁻¹)E_J*E_J` certifies the finite-`J` projected derivative **before**
  introducing independent interval errors on the large terms that later cancel. **Status: PROPOSED — needs
  an executable source-attested error budget** (exact piecewise polynomial-exponential integration of the
  projected derivative; parity-dependent optimized rational `η`; operator-valued, not scalar, tail). This is
  the highest-leverage next instrument.
- **Anisotropic coercivity (Section 4) — partially realized.** `K|F_4` has condition number `20.31`, so no
  single scalar `κ` is tight; the exact object is operator-valued. The parity split
  `D_4 ⪰ diag(63/500·K_odd, 153/500·K_even)` **is** a realized 2-block anisotropic comparison form `C`.
  Next: a frequency-dependent `C` (parity-specific spectral multiplier) controlled by a dual `C⁻¹` sharper
  than dividing all directions by one scalar — guard every candidate with source-compatible high-Legendre
  packets and off-parity mutations (a bounded-below `C` does **not** give a bounded `C⁻¹` for free).
- **Optimized rational responses `U` (Section 5).** Headline results use `U=0`. Discover numerically,
  rationalize preserving parity/source domains, **re-certify** with the exact bracket; report odd/even
  min-eig separately. No optimizing an uncertified surrogate then reporting its eigenvalues as source-authenticated.

## 5. Independent non-RH tracks (meaningful regardless of the `S_4` sign)

- **SUCC × FUCC categorical arithmetic (PDQ-14 G).** `D_p(n)=(pn)!/(n!)^p` Gauss–Legendre `p`-torsion
  factorization; Frobenius self-carry invariance `c_p(p,p^k n)=s_p(n)`; three exact functoriality
  obstructions (carry defect, factorial non-additivity, composite-`n=6` single-prime leakage). **Frontier:**
  the affine braid `V_p S = S^p V_p` and which coherence laws hold strictly vs only up to a noninvertible
  comparison.
- **Proof-producing SUCC × YEAN (PDQ-14 I).** `SUCC_YEAN_RATIONAL_SCHUR_CAPSULE_v1`: division-free
  rational `PMPᵀ=LDLᵀ` / Schur certificates with canonical FQID enforcement, separating finite matrix
  verification from infinite analytic premises. **Frontier:** kernel-check one parity-block LDL end to end
  (separate coordinated YEAN branch; do not touch the YEAN repo from here).
- **Observer interior/boundary synergy (PDQ-12).** A two-observer join strictly exceeds the sum of parts
  (`0+4 < 24` on `P_3(2t)`), while cross-contact-gauge stitching fabricates a Bessel-violating ghost — a
  clean no-ghost compatibility condition.

## 6. Dead routes and preserved counterexamples (do not re-walk)

- "high ⇒ full" positivity transport — REFUTED (DAG firewall).
- "positive Gram ⇒ signed-form positive" — REFUTED (O12 / CTW-12).
- `κ_30=369/10000` transports through the signed 5..30 shorting — REFUTED (exact no-go, `four_thirty_schur_transport`).
- off-critical quadruplet per-parity sign-definiteness — REFUTED (1A, this round; interval-certified bump witness).
- scalar-Young-cap certifies `S_4 ≻ 0` — OBSTRUCTED (`τ* ≈ 6.015e−7`, cap `6.29e6×` too loose; 1C).

## 7. Dependency graph toward all-radius positivity

```
 [certified two-sided enclosure of S_4]  (DONE; repaired this round)
        |
   +----+--------------------+--------------------------+
   |                         |                          |
 (Sec 3) direct T_quot   (Sec 4) anisotropic C⁻¹   source endpoint evaluator h(±a) @ 1e-7
 certification           (freq-dependent coercivity)   (the smallest decisive lemma)
   \__________________________|__________________________/
                              v
                 [decisive sign of S_4 at a=1/2]  — first-window ONLY, NOT RH
                              |
                              v
                 (Sec: all-radius generalization)  --->  [RH-equivalent] OPEN. RH PROVED: NO.
```

## 8. Priority ranking (leverage × falsifiability × reuse)

1. **Source-attested endpoint evaluator `h(±a)` at `~1e−7`** — smallest lemma that moves the verdict.
2. **Direct quotient-energy certification (Sec 3)** with an executable error budget — highest-leverage instrument.
3. **Frequency-dependent anisotropic `C` (Sec 4)** beyond the realized parity split.
4. **SUCC×YEAN kernel-checked LDL (Track I)** — compounds across the whole stack.
5. **FUCC braid coherence / observer join / finite-witness complexity** — independent of the sign.

**The single smallest next theorem that would change the verdict:** a certified source-attested evaluator of
the two boundary moments `(M_{3,i}, M_{4,i})` — equivalently `h(±a)` for `h=Gv` — to `~1e−7`, feeding the
complete `E*P⁻¹E` subtraction; everything else in the chain (`A_4` lower, `W_L2`, `κ_odd/κ_even`, Γ-tail,
`τ*`) is now explicit. **Most valuable independent non-RH theorem:** one strictly-preserved FUCC braid
relation `V_p S = S^p V_p` with a finite exact witness and one explicit coherence obstruction.
