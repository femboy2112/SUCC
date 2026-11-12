# Claim ledger — innovation × arithmetic decoupling

`PROVED LOCAL` = proof in this branch (same-model authorship and audit; not external refereeing,
not Lean). `CLASSICAL IMPORT` = cited published result. `OBSERVED FINITE` = exact/certified finite
computation with stated scope. Every row names its falsifier. **No row promotes π normality, the
source-selected signed estimate, parity balance or RH; all remain OPEN.**

| Claim | Exact scope | State | Falsifier / next probe |
|---|---|---|---|
| IAD-01 | `R_(B,L,h) = (B/L)(E_L/L - S) = σ_B(γ_L - 1/L)`; `|B_B(h)|² ≤ 4/L + 2R⁺`; the `B ≥ 16^10` threshold of the prescribed schedule belongs to the coarse constant 4 only (sharp form informative from `L = 2`) | PROVED LOCAL (verification of the Main XXIV §4 identity) | PR-1.1: any sequence violating the identity |
| IAD-02 | `√γ_L ≤ √γ_J + J/L` for every finite-support sequence; for every `L(B)→∞`, `L ≤ B`: `[∀h≠0: R⁺→0] ⟺` base-16 normality | PROVED LOCAL | PR-1.2; a normal sequence with `R_(B,L(B),h) ↛ 0` would refute |
| IAD-03 | `Δ_ℓ(n) = 16^ℓT_n - T_(n+ℓ)`; moment representation; brackets for `r`, `-r'`; `δ(m)` positive decreasing | PROVED LOCAL | PR-1.3 exact rational grid |
| IAD-04 | For `h16^ℓ ≤ (15/8)B³`: `|Σ_(n∈I) e(hΔ_ℓ(n))| ≤ cot(πλ/2) < 4401B³/(h16^ℓ)`, all subintervals and admissible progressions; `|Z-1| ≤ (π/32)h16^ℓ/B²`. Conditional-expectation corollary **repaired**: requires occupied cells `1 ≤ q ≤ B-ℓ`, bound `8802B²/((1-ℓ/B)h16^ℓ)`; the earlier display was false at `(B,ℓ,h,q) = (100,1,1,1000)` | PROVED LOCAL (seed-independent; untwisted) | PR-1.4; ZC-10 and `test_iad04_progression_occupied_cells` |
| IAD-04x | Power saving for `(2+δ)log_16 B ≤ ℓ ≤ K log_16 B` by higher-derivative tests | CLASSICAL IMPORT, not re-proved; source text not seen | Re-derive from a seen statement, or drop |
| IAD-05 | `A = C·conj(Z)·e(-hτ)`; `|Cov(A,Z) - E[C]| ≤ |E[Z]| + (π/32)|h|B^(-2)`; filtration inequality (5.2) | PROVED LOCAL | PR-1.5: any seed/partition violating (5.2) |
| IAD-06 | Transport `|c_d - c^U_d| ≤ (π/32)|h|B^(-2)`; sparse vdC (6.1); band of ratio `< 2` pays at most `1/2` **by this route** | PROVED LOCAL | PR-1.6 |
| IAD-06g | Sufficient mesoscopic gate: `limsup Re c^U_(jℓ_0) ≤ 0 ∀j ⟹ W_B(h) → 0` | PROVED CONDITIONAL; premise **OPEN** | Premise implies WALL-16 with `v* ≤ 1` (IAD-08b) |
| IAD-07 | For every odd prime `q`, modulus `M` coprime to `q`, horizon `K`: rational seed equal to seed 0 at all finite places `p ≠ q` (mod `Z_p`, and mod `M`), completed orbit `≤ ½·16^(n-K-2)` | PROVED LOCAL (generalizes PPP-08) | PR-1.7: exact place-by-place comparison |
| IAD-07c | No **finite-horizon** census-incomplete transfer (data at finite places `p ≠ q`) can give a nontrivial bound on a shell, for `W_B` or for a lag `1 ≤ d ≤ B-1`, at any `η > 0` (horizon `K = 2B + t`; **repaired after the second audit**, which blocked the `K = 2B` form for lags near `B` and the empty lags `d ≥ B`). Asymptotic transfers are addressed by ZSC-06(f)5 | PROVED LOCAL | Exhibit a transfer in the class with a valid conclusion |
| IAD-08 | Fixed saving `η` on all large shells `⟹ ‖16^B x‖ ≥ cB16^(-B)` for the Weyl sum and for a lag `ℓ(B) ≤ (1-θ)B`; for a general lag the factor is `B-ℓ` (**regimes declared after the second audit**). Sharpened by ZSC-01 | PROVED LOCAL | PR-1.8 synthetic near-dyadic points |
| IAD-08k | Refereed record `v_16(π) ≤ 6.1033`; no base-restricted improvement known | CLASSICAL IMPORT + literature search (absence not provable) | A published restricted-denominator bound would recalibrate |
| IAD-09 | Births `β(p)`; event separation `≥ (p-5)/8`; fresh `p`-component `= ρ/p`; inequation under `ℓ ≤ n/4`; place weld (pole `4m-1` only from age 1, corrected after audit) | PROVED LOCAL | PR-1.9 brute force over all primes `≤ 16B+200` |
| IAD-09e | Mean births per window `(6+o(1))ℓ/ln B` (`≈ 2.164c` at `ℓ = c log_16 B`) | PROVED LOCAL given PNT in progressions (IMPORT) | PR-2.7 finite counts |
| SWT-00 | No nonempty Scott-open set inside the normal sequences or their complement; normality Borel (Π⁰₃-complete: IMPORT) | PROVED LOCAL + IMPORT | — |
| SWT-01 | Density-zero edits of sliding-block images transport block frequencies; normality itself is transported by density-zero edits (not by arbitrary invertible block codes: corrected after audit) | PROVED LOCAL | PR-1.11 |
| SWT-02 | `κ_n ∈ {0..16}`, `x = Σκ_j16^(-j)`: redundant radix-16 name from rational arithmetic | PROVED LOCAL | PR-1.10 |
| SWT-03 | Seam law items 1–5; look-ahead characterization `ε_n = 1 ⟺ κ` continues `15^a 16` | PROVED LOCAL (finiteness of runs imports irrationality of π) | PR-1.10 incl. forced-seam seed |
| SWT-04 | `π/16` normal `⟺` shifted rational carry stream normal over `{0..15}`; `|occ(w;d) - occ(w;κ⁺)| ≤ 2kρ(N+k)` | PROVED LOCAL (an equivalence, not an estimate) | PR-1.10 |
| SWT-05 | One-sided interchange: antitone ⟹ every schedule; isotone ⟹ only a diagonal schedule | PROVED LOCAL | Instance checks PR-1.2 (A), probe (B) |
| SWT-06 | Limits of transport (by reference to IAD-07, RS-04, O-6) | PROVED LOCAL by reference | — |
| ZSC-01 | For every real `ξ`: if `Re W_B(h;ξ) ≤ 1-η` for all `B ≥ B_0` then `‖16^m ξ‖ ≥ (15η/(512π|h|))·16^(-((2-η)/(2+η))m)` for `m ≥ max(2B_0,(2+η)/η)`; so a fixed saving needs `v_16 < 1`, which no bound on `μ` supplies | PROVED LOCAL (Shallit witness `μ = 2`, `v_16 = 1`: IMPORT, seen) | ZC-1, ZC-2; a point with a saving and larger exponent |
| ZSC-02 | `c_B/3321 ≤ 1 - Re W_B(15) ≤ 2(k-1)(c_B+(k-1)/B)+450π²16^(-2k)`; `|W_B(1)| ≤ 1-(c_B-1/B)/65793`; density `c` of changes forces exponent `≤ (1-c)/(1+c)` at `15·16^m` | PROVED LOCAL (every real `ξ`) | ZC-3, ZC-4 |
| ZSC-03 | Every seed: `κ_(n+1) = 16 ⟹` the next `J(n) ≥ ⌊log_4 2n⌋` carries are 0; `#{κ_n = 16, B ≤ n < 2B} ≤ 1 + B/log_4 B`. Zero seed: `|c^κ_B - c_B| ≤ 3(2+B/log_4 B)/B` | PROVED LOCAL (sharpens RIO-10; makes the letter-16 clause of SWT-04 unconditional) | ZC-5, ZC-6 incl. forced-seam seeds |
| ZSC-04 | For all `n ≥ 2`: equal-digit runs `≤ 41n`; `⌊16^(n-1)π⌋ = ⌊C_(n+J)/16^J⌋` for `J ≥ 41(n-1)`; `≥ log_42 N - 2` changes | PROVED LOCAL from Mahler 1953 Thm 1 (CLASSICAL IMPORT, seen) | ZC-7 (look-ahead checked for `n ≤ 40` by two routes) |
| ZSC-05 | W1 (`v_16 = 0`, no saving, seam density 1), W2 (seam-free, `v_16 = ∞`, no saving), W3 (change density `1/2`, saving, seam density `1/2`): for seeded carriers the seam target is independent of the wall and of (CH) in both directions; (CH) implies the wall (ZSC-02(d)), not conversely (**"pairwise independent" in the first draft was false; corrected after audit**) | PROVED LOCAL | ZC-8 |
| ZSC-06 | Gauge `(g,s) ↦ (g-(16-z⁸)h, s+∫h)` (phase statistics invariant; seed, poles, **carries and seam are not** — corrected after audit); proper form with invariant seed; elementary null relation `∫_0^1 (z²-4z+2)/m = 0`; `{A : L(A) ∈ Q} = Q·A_0` (rank 7, exact); hostile source `g_H` (zero seed, positive, `O(n^(-2))`, completed point 2); `A_π + ρA_0` all complete to `π/16` | PROVED LOCAL; the rigidity clause uses Baker's theorem (CLASSICAL IMPORT, **not re-read this round**) | ZC-9; a second null vector or a rational `L(A)` off the null line |
| CH | Positive lower shell density of digit changes of π in base 16 (`⟺` of carry changes of `⌊U_n⌋`) | **OPEN** — the named next obligation (NEXT.md) | A shell sequence with `c_B → 0` would refute; a proof would give `limsup |D_(B,1)| < 1` |
| SEAM-DENSITY | `ρ(N) = #{n<N: ε_n=1} = o(N)` for the zero seed | **OPEN**, demoted (ZSC-05/07: independent of (CH) and of the wall; only `N - ρ(N) ≫ log N` is known) | — |
| SEAM-FREE | `κ_n ≠ 16`, `ε_n = 0` for all `n ≥ 0` | **CONJECTURED**; OBSERVED FINITE on the probed range only | One seam event at any `n` |
| WALL-16 | `‖16^n x‖ ≥ 16^(-v*n)` for some `v* < 6.1033` from the BBP source | **OPEN** — necessary first rung; by ZSC-01 the relevant wall is `v* < 1` | NEXT.md |
| O-7 LP | For positive measures with vanishing coefficients on a lag band `[a,b]`, the maximal atom at 0 is `≈ 0.447` at ratio 1.5 and `0.5` for one lag: positivity alone cannot force `W→0` from a bounded-ratio band | OBSERVED FINITE (floating-point LP on a grid; existence to LP tolerance) | Exact dual certificate; closed form `1/√5` unproved |
| NORM | A source-derived bound on `R`, on any `c^U_d`, or on any `W_B(h)`; π base-16 normality | **OPEN** | Requires an all-large-shell arithmetic estimate |

**TLICA separation.** κ (contact) is high for the exact identities and the smooth innovation
estimate. φ (toolkit-relative indistinguishability): the changes tabulated at the end of
OBSTRUCTIONS are indistinguishable to every method tried. σ (source correctness): the forcing is
imported unchanged; the literature calibration is a same-day search, labelled. ρ (commitment
coupling): the author expected the prescribed schedule to be the stronger target and a
fresh-prime mechanism to exist; both expectations are recorded as refuted (O-8, O-3).
