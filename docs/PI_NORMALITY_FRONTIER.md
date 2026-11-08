# π base-16 normality — the current frontier (single entrypoint)

**Maintained entrypoint, as of Operation Main XXI (2026-11-07); first established in Main XX (2026-11-05).** Start here for any π-normality work. Older dated front documents stay valid as historical records under their own provenance; they are listed in §7. Main XXI additions are marked **[XXI]**; their audited labels and scope notes are in [`CLAIM_SUPPLEMENT_MAIN_XXI.md`](CLAIM_SUPPLEMENT_MAIN_XXI.md) (`MXXI-*`).

**Status: π base-16 normality — OPEN. Selected signed Weyl gate `S_N(h)=o(N)` — OPEN. RH — OPEN (separate program).**

## 1. The authenticated source and the zero-seed recurrence

- **Source (immutable).** `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_{n-1}+r(n)`, `x_n=\{U_n\}`. The original four signed poles, the literal zero seed and the integer carries are frozen.
  - Provenance: [`provenance/IMPORT_MANIFEST.json`](../provenance/IMPORT_MANIFEST.json), verified by `scripts/verify_provenance.py`.
  - Exact arithmetic core: [`observational_succ/duck_bbp.py`](../observational_succ/duck_bbp.py), with its analytic tail bound Lean-checked in [`formal/duck_pi/`](../formal/duck_pi).
- **Gauge.** With `T_n=\sum_{j\ge1}16^{-j}r(n+j)` (positive, seed-independent, `≈1/(64n^2)`), we have `U_n(s)+T_n=16^n(s+π/16)` (#521 CT7). Every selected observable is therefore an observable of the completed ×16 orbit of the single number `α=s+π/16`. For the true seed that is `\{16^{j-1}π\}`. Source: [critical_carry_jets/CRITICAL_CARRY.md](../research/2026-11-05/critical_carry_jets/CRITICAL_CARRY.md).
- **The gate.** `c_A(h)=A^{-1}\sum_{n=A}^{2A-1}e(hU_n)`. π base-16 normal ⟺ `c_A(h)\to0` for every fixed `h\ne0`. This is the only proved biconditional on this front (#293/SGO-09 Green tail). The equivalent fixed-radius form is `Q_{1/2}(μ_A)=\sum_{h\ge1}2^{-h}|c_A(h)|^2/h\to0`.
- **Shared framework for new work.** [`observational_succ/selected_orbit.py`](../observational_succ/selected_orbit.py) provides:
  - exact states for rational seeds;
  - `S_k(n)` and Lean-backed `T_n` enclosures;
  - the critical carry bit by definition and by the CB-1 window;
  - the innovation `J`;
  - `c_A(h)` at locally scoped precision;
  - admissibility checks;
  - a receipt writer that records sha256 dependencies and rejects unknown status labels.

  Use it instead of re-implementing the source; 136 files currently do.
- **[XXI] Canonical exact APIs (census at Main XXI; every listed duplicate is value-identical on `n=1..399`).**
  - Forcing and lifted orbit: `duck_bbp.forcing`, `lifted_orbit` and `forced_orbit`. This module is Lean-backed.
  - Integer engine with literal carries `(16·rem+c)//q`: `integer_bbp_carrier.forcing_pair`, `step` and `source_states`. The new pin-bed modules use it.
  - Seeded, reduced orbit: `selected_orbit.SelectedOrbit`.
  - Tail enclosure: `duck_bbp.tail_interval`.
  - 2-adic zero, isometry and odometer: `bbp_binwindow_conjugacy` and `bbp_two_adic`.
  - Prime births: `bbp_cyclotomic_birth.birth_index`.

  Two things here are different objects and must not be swapped in for one another. `selected_orbit.carry_by_definition` is the #522 critical-carry *bit*, not the integer carry. `gamma_bbp_signed_coherence.green_tail_interval` is strictly *tighter* than `duck_bbp.tail_interval`.

## 2. Proven exact source / geometry / carry / observation theorems (selection)

| Result | Statement | Where |
|---|---|---|
| CT1/CT2 | `0<r(n)-15/(64n^2)<1/n^3`; `\|S_m(n)-(16^m-1)/(64n^2)\|<16^m/(10n^3)` for all `m` | [#521](../research/2026-11-05/critical_carry_jets/CRITICAL_CARRY.md) |
| RENORM-1 | `c_A(h)=c_A(16h)+ε_A(h)`, `\|ε_A(h)\|\le2/A+15π\|h\|/(4A(8A-15))`; corrected common-depth barrier | [#491](../research/2026-11-03/renorm_transport/PROOFS.md) |
| HS-01…HS-07 | Two-cell shell identity; odd-torsion unique-but-discontinuous inverse; non-lumpability of Haar resets (HS6); Haar-seed digits are i.i.d. for any forcing (HS8); point-evaluation barrier (HS12) | [#522](../research/2026-11-05/history_shell/PROOFS.md) |
| **CB-1** | The critical carry bit is exactly `1[S_m(n+k)\le x_{n+d}<S_d(n)]` (any seed, any positive forcing). Admissible ⟺ `A\ge2^{2d-3}`, certified for `d\le200`. | [Main XX front B](../research/2026-11-05/main_xx_forge/front_b/PROOFS.md) |
| **FA-1** | `P_{A,2A,r}=-Q_r(μ_A)+O(1/A)` exactly: #520's finite causal Clausen cut *is* the Clausen gate | [Main XX front A](../research/2026-11-05/main_xx_forge/front_a/PROOFS.md) |
| **FA-3** | A ×b-invariant measure that dominates Lebesgue on any open arc is Haar | front A |
| **C1/C2 de-sourcing** | Mixed angular–radial sums: `\sup_{V(a)\le1}\|\sum a_ne(hU_n)\|=\max_L\|S_L\|` exactly. Every source label is a function of `(n,z_n)`. χ₋₄ content is a period coordinate of `α`. | [Main XX front C](../research/2026-11-05/main_xx_forge/front_c/PROOFS.md) |
| AC1–AC4 | Carry-correction count `E=O_m(A/\log A)` (seed-uniform) | [#520](../research/2026-11-05/selected_orbit_final_pin/SELECTED_CARRY.md) |
| **[XXI] PF7** | `log d_n=Θ(n)`: `5≤\liminf\log d_n/n≤\limsup\le8` for the odd reduced denominator `d_n` of `U_n` (unconditional PNT/AP). This is **not** zero-seed selective, and #534 HT20's `≥2` is the weaker sibling. | [#532](../research/2026-11-06/prime_frobenius_spectral/THEOREMS.md) (MXXI-13/14) |
| **[XXI] ET1** | `\|\sqrt{C^z_{A,H}}-\sqrt{C^x_{A,H}}\|\le(π/(15A^2))\sqrt{H(H+1)(H+2)/6}`: critical Fejér **transport error** `O(A^{-1/2})` at `H=A`. It is **not** `o(1)` for the gate. | [#538](../research/2026-11-06/epoch_critical_transfer/THEOREMS.md) (MXXI-20) |
| **[XXI] GA1–GA5** | Golden aperture `a=φ^{-1}`, `b=a^2`: `E_a=bE_b`; the exact triangle `E_a(μ_N)=(1/(bN^2))\sum(b-d_T)_+-b`; the characteristic kernel; source-to-π unsquared transport `≤1/(15bA^2)` | [#540](../research/2026-11-07/golden_aperture_fejer/THEOREMS.md) (MXXI-22/23) |
| **[XXI] FG10/FG11** | At fixed `N`, return energy is monotone **nondecreasing** under dyadic refinement, so refinement cannot contract | [#535](../research/2026-11-06/fejer_gamma_split/THEOREMS.md) (MXXI-15) |
| **[XXI] RS8 / RS-06** | The state-only 2-adic decoder has a floor of `1/34` (true for every irrational seed); no odometer→×16 Haar factor exists | [#528](../research/2026-11-06/adelic_return_bridge/THEOREMS.md) (MXXI-11) |

## 3. Sufficient but unproved gates (and what each is worth)

- **Fixed-h Weyl `S_N(h)=o(N)`.** Equivalent to normality.
- **`Q_{1/2}(μ_A)\to0`.** Equivalent to normality. #520's finite-cut inequality is the same statement (FA-2).
- **Band/J/E chain.** `band=o(K_A)⟹J=o(K_A)⟹E=o(\log m)⟹`normal. This is **one-directional** sufficiency; the converse `J⟹band` is false (#491 RT-00).
- **Carry factorization (CB-4/FA-5).** normal ⟺ (LS) log-scale stationarity ∧ (H2\*) uniformity at the source lattice. Both conjuncts are strictly weaker than normality, and both are OPEN for the zero seed.
- **Pair budgets.** A mesoscopic budget, or a single Poisson-scale budget with a log rate, is equivalent to normality (Front C, C3-1/C3-2). The PF7/Fekete energy and every all-scale budget are strictly stronger.
- **[XXI] Critical Fejér energy.** Either of the following implies normality (#538 ET3/ET4a). Both premises are OPEN.
  - `C^x_{A,A}=o(\log A)` along all `A`, or along `A_j` with `A_{j+1}/A_j\to1`.
  - All-radius anticlustering `B_A(δ)≤A+KA^2δ` for all large `A`, on the BBP orbit itself. ET4a then bounds `C^x_{A,A}≤2K+4(A+1)/(3A)`, and ET3 applies. ET3 uses the orbit's *proved* ×16 frequency-ray rigidity; that rigidity is not a premise. The same `K=3` bound on a configuration that is not a ×16 orbit forces nothing (GA-09 receipt, §4).

  The finite certificates `K≤3` at `A=191, 319` (#538) and the all-radius certificates up to `N=4096` (#536) are finite only.
- **[XXI] One-scalar golden gate.** π normal ⟺ `E_a(μ_A^x)\to0` (#540 GA4; #539 CIRCLE_WINDOW). This is an equivalent reformulation, not progress.
- **[XXI] Joint-entropy deficit.** J9/J19 turn a finite empirical-entropy deficit into a joint-Weyl bound. The J20 premise is OPEN, and at the tested epochs the right-hand side exceeds 1 (#526).

## 4. No-go theorems and countermodels (do not re-walk these)

| Obstruction | Kills | Receipt |
|---|---|---|
| Coherent wrong seed `s_*=-π/16` (`U_n=-T_n`) | any seed-uniform or forcing-only argument; carry-density lower bounds | #521 CT-03, Main XIX Laurent sharpness `(1-(d+1)/c)^2` |
| **CB-3** non-stationary calibrated seed (same forcing) | "critical-carry `J`-family ⟹ normality"; "Clausen energy ≤ C·carries" (FL) | Main XX front B §CB-3, front A FL |
| Haar-seed ensemble / virtual fields (HS8, HS12) | any proof from seed-averaged concentration; evaluation at `s=0` costs `\sqrt A` | #522 |
| Rational seed `1/5` | being treated as a nonnormal contrast: it is a rotation (`16\equiv1\bmod5`) | #491, front A FA-8 |
| Fixed point `x=1/5` (unforced) | universal high-band smallness | #491 |
| Nearby periodic completions `k/(16^p-1)` | finite-window inference: they match long prefixes yet are nonnormal | #520 alpha AC3, front A FA-7 |
| Microscopic pair exclusion | "Pauli/Fekete exclusion ⟹ normality": a nonnormal 15-symbol orbit has no pairs closer than `A^{-2.05}` | Main XX front C C3-3 |
| χ₋₄ / Frobenius orientation | its use as a sign lever: it is arithmetic of `α`, killed by the reflection gauge and by `\sum16^{-k!}` | Main XX front C C2 |
| Odd-torsion inverse | stable inversion: unique but discontinuous | #522 HS-03 |
| RENORM-2 / common-depth barrier | single-frequency transport reducing the band moment | #491 |
| **[XXI] GA-09 receipt** — uniform `A`-grid on an arc of length 2/3 | "all-radius `K=3` anti-clustering ⟹ golden `E_a\to0`": `B_A(t)\le A+3A^2t` for all `t`, yet `E_a\to\sqrt5/9-1/6>0` | [main_xxi_receipts R1](../research/2026-11-07/main_xxi_receipts/README.md) (MXXI-24) |
| **[XXI]** 2-adic zero + 2-adic Haar (DB-06/DB-07); the `H(n)=n/(2n-1)^4` shadow | "2-adic Haar or a commuting hologram forces real Haar" | #527, #540 GA-10 |
| **[XXI]** Denominator growth + Galois-orbit Haar | "exponential `d_n` plus Galois Haar ⟹ real time Haar"; `y_n=1/Q_n` has both, yet its phase tends to 0 | #532 `FAILED_SCRATCH.md` |
| **[XXI]** Dyadic refinement monotonicity (FG11) | contraction of the return energy by refining the time fibers | #535 |
| **[XXI]** Zero forcing in the learning pin bed | "a learning observer that pins the digits forces normality": the learner behaves identically on a maximally non-normal source | #542 (adversarial audit, MXXI-06) |

## 5. Orthogonal tracks (separate status, not π progress)

- **RH / Weil prime-jet:** [prime_jet_reservoir](../research/2026-11-05/prime_jet_reservoir) (#517) and [prime_jet_volterra](../research/2026-11-05/prime_jet_volterra) (#519). A local H¹/Volterra bound is **not** completed Weil positivity, and no operator identification is asserted.
- **Gamma Prybar / critical chirp:** [gamma_prybar](../research/2026-11-04/gamma_prybar) (#501), [critical_chirp_source](../research/2026-11-04/critical_chirp_source) (#503→#505), [gamma_pigeonhole](../research/2026-11-04/gamma_pigeonhole) (#498).
- **Observer foundations:** [operational_foundations](../research/2026-11-04/operational_foundations) (#494), [source_sound_calculus](../research/2026-11-04/source_sound_calculus) (#495), the observer bridge (#493), and the #522 observer policy (HS-08: low predictive error is not arithmetic typicality).
- **[XXI] Fourier–Yoneda pin beds (observer architecture, not π progress).** Three **non-interchangeable** formalisms (MXXI-01…07):
  - **#541:** Bernoulli `B₂` continuous surfaces with an exact inverse `μ=λ−½D²F`.
  - **#543:** a forward-window driven observer with a first-order inverse, the sharp half-aperture ×16 constant `341/√205` (real laws only; it is `31` on complex inputs), and lock-in/phase calibration.
  - **#542:** finite two-tone windows plus *backward* continuous convolutions with conjugated multipliers, and a historical learning observer whose `4N`-bit memory is pigeonhole-tight.
  - The sign conventions of #543 and #542's continuous surfaces differ by complex conjugation. Do not compose them verbatim.
  - Every normality statement in these PRs is an equivalent reformulation.
- **[XXI] Quadratic Pisot / harmonic–Pisot.** QR-01…QR-07 with a genuine RH firewall (#537), and HPB-01…05 (#539). Their "anti-normality" applies only to sequences with finite weighted square-distance energy. It is elementary for Pisot powers and does not transfer to the BBP orbit.
- **Physics-analogy explorations** ([zero_object_casimir](../research/2026-11-05/zero_object_casimir), [unit_pair_bell](../research/2026-11-05/unit_pair_bell), [infinite_qubit_field](../research/2026-11-05/infinite_qubit_field), [gamma_sphere_solenoid](../research/2026-11-05/gamma_sphere_solenoid), [gauge_sphere_tower](../research/2026-11-05/gauge_sphere_tower), [tau_saddle](../research/2026-11-05/tau_saddle)). These are classical mathematics with analogy vocabulary; no physical quantum or Casimir claim is made.

## 6. The precise next theorem whose proof would be a genuine advance

**(LS) for the zero seed.** Prove

\[
Λ_A=\sup_{1\le a<b\le8,\ b-a\ge1/4}\ \sup_t\ \bigl|μ_{[aA,bA)}([0,t))-μ_{[A,2A)}([0,t))\bigr|\ \longrightarrow\ 0 .
\]

- **Why it would matter:** by CB-2′, it reduces π normality to a single uniformity statement at the source lattice, (H2\*).
- **Equally valuable:** a proof of (H2\*) for the zero seed, which would reduce normality to (LS).
- **Validity test for any proposed proof:** it must **fail** on the CB-3 seeds, which share the forcing. It must therefore use a seed-selective input, such as exact zero-seed rationality.
- **[XXI] Same target, sharper tools.** Main XXI adds two more sufficient scalar targets: the critical Fejér energy `C^x_{A,A}=o(\log A)` (#538 ET3) and the golden energy `E_a(μ_A^x)\to0` (#540 GA4). It also adds an unconditional transport that makes the original zero-seed orbit interchangeable with `\{16^{n-1}π\}` at cost `O(A^{-1/2})` (√-norm) or `O(A^{-2})` (golden energy). The validity test now has **three** hostile controls, and any proposed proof must fail on all of them:
  - the coherent counterseed `s_*=−π/16`;
  - the CB-3 same-forcing seeds;
  - the GA-09 arc-grid configuration, which satisfies every finite `K=3` certificate.
- The ranked next experiments are in [Main XX README](../research/2026-11-05/main_xx_forge/README.md#next-moonshot-three-experiments-ranked-by-how-sharply-they-separate-genuine-zero-seed-cancellation-from-coherent-wrong-seed-and-virtual-ensemble-effects).

## 7. Historical front documents (preserved, superseded as entrypoints)

- [PI_BRANCH_CURRENT_FRONTIER_2026-11-03](PI_BRANCH_CURRENT_FRONTIER_2026-11-03.md)
- [PI_SELECTED_CATEGORICAL_FRONTIER](PI_SELECTED_CATEGORICAL_FRONTIER.md)
- [PI_FRONTIER_CONTRACT](PI_FRONTIER_CONTRACT.md)
- [PI_GEARBOX_ATLAS](PI_GEARBOX_ATLAS.md)
- [selected-current front (#489)](../research/2026-11-03/selected_current_front/PROOFS.md)

Integration provenance: [SUCC_MAIN_XXI_INTEGRATION_AUDIT_2026-11-07](SUCC_MAIN_XXI_INTEGRATION_AUDIT_2026-11-07.md) (this round); [SUCC_MAIN_XX_INTEGRATION_AUDIT_2026-11-05](SUCC_MAIN_XX_INTEGRATION_AUDIT_2026-11-05.md) (previous).
