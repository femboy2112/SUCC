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
| IAD-04 | For `h16^ℓ ≤ (15/8)B³`: `|Σ_(n∈I) e(hΔ_ℓ(n))| ≤ cot(πλ/2) < 4401B³/(h16^ℓ)`, all subintervals and admissible progressions; `|Z-1| ≤ (π/32)h16^ℓ/B²` | PROVED LOCAL (seed-independent; untwisted) | PR-1.4: one subinterval exceeding the bound |
| IAD-04x | Power saving for `(2+δ)log_16 B ≤ ℓ ≤ K log_16 B` by higher-derivative tests | CLASSICAL IMPORT, not re-proved; source text not seen | Re-derive from a seen statement, or drop |
| IAD-05 | `A = C·conj(Z)·e(-hτ)`; `|Cov(A,Z) - E[C]| ≤ |E[Z]| + (π/32)|h|B^(-2)`; filtration inequality (5.2) | PROVED LOCAL | PR-1.5: any seed/partition violating (5.2) |
| IAD-06 | Transport `|c_d - c^U_d| ≤ (π/32)|h|B^(-2)`; sparse vdC (6.1); band of ratio `< 2` pays at most `1/2` **by this route** | PROVED LOCAL | PR-1.6 |
| IAD-06g | Sufficient mesoscopic gate: `limsup Re c^U_(jℓ_0) ≤ 0 ∀j ⟹ W_B(h) → 0` | PROVED CONDITIONAL; premise **OPEN** | Premise implies WALL-16 with `v* ≤ 1` (IAD-08b) |
| IAD-07 | For every odd prime `q`, modulus `M` coprime to `q`, horizon `K`: rational seed equal to seed 0 at all places `≠ q` (mod `Z_p`, and mod `M`), completed orbit `≤ ½·16^(n-K-2)` | PROVED LOCAL (generalizes PPP-08) | PR-1.7: exact place-by-place comparison |
| IAD-07c | No **finite-horizon** census-incomplete transfer can give a nontrivial bound on a shell; asymptotic transfers with seed-dependent threshold and Archimedean arguments are **not** excluded | PROVED LOCAL (logical consequence of IAD-07; scope corrected after audit) | Exhibit a transfer in the class with a valid conclusion |
| IAD-08 | Fixed saving `η` on all large shells (Weyl or one lag) `⟹ ‖16^B x‖ ≥ cB16^(-B)`, i.e. `v_16(π) ≤ 1` without ε | PROVED LOCAL | PR-1.8 synthetic near-dyadic points |
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
| SEAM-DENSITY | `ρ(N) = #{n<N: ε_n=1} = o(N)` for the zero seed | **OPEN** (implied by normality; strictly weaker) | — |
| SEAM-FREE | `κ_n ≠ 16`, `ε_n = 0` for all `n ≥ 0` | **CONJECTURED**; OBSERVED FINITE on the probed range only | One seam event at any `n` |
| WALL-16 | `‖16^n x‖ ≥ 16^(-v*n)` for some `v* < 6.1033` from the BBP source | **OPEN** — the named next obligation | NEXT.md |
| O-7 LP | For positive measures with vanishing coefficients on a lag band `[a,b]`, the maximal atom at 0 is `≈ 0.447` at ratio 1.5 and `0.5` for one lag: positivity alone cannot force `W→0` from a bounded-ratio band | OBSERVED FINITE (floating-point LP on a grid; existence to LP tolerance) | Exact dual certificate; closed form `1/√5` unproved |
| NORM | A source-derived bound on `R`, on any `c^U_d`, or on any `W_B(h)`; π base-16 normality | **OPEN** | Requires an all-large-shell arithmetic estimate |

**TLICA separation.** κ (contact) is high for the exact identities and the smooth innovation
estimate. φ (toolkit-relative indistinguishability): the four changes tabulated at the end of
OBSTRUCTIONS are indistinguishable to every method tried. σ (source correctness): the forcing is
imported unchanged; the literature calibration is a same-day search, labelled. ρ (commitment
coupling): the author expected the prescribed schedule to be the stronger target and a
fresh-prime mechanism to exist; both expectations are recorded as refuted (O-8, O-3).
