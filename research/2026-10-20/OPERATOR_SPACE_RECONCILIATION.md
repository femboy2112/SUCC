# Operator-space reconciliation: K-relative vs absolute gaps, and whether the rigidity core moves S₄

> **Academic Main VII correction:** the fixed-interval no-gap inference in
> sections 1.3–1.4 is refuted by the exact bound Γ₀ ≥ 3I on L²([−1/2,1/2]).
> See [the superseding operator audit](ACADEMIC_VII_OPERATOR_AUDIT.md) for the
> proof, source normalization and current coercivity dependencies. The full signed
> source and S₄ sign remain unresolved. Historical numerical statements below
> are retained as records of the earlier argument, not current validation receipts.

**Operation Proof Forge III — Lane C (functional analysis).**
**Date:** 2026-10-20. **Worktree branch:** `research/pf3-lane-operator-2026-10-20`.
**Nothing merged; nothing pushed.** No nontrivial zeta-zero ordinate is a construction input
anywhere in this note. Γ-factor, pole/contact, true prime-power source, phase convention,
half-density and the no-zero-input policy are **preserved, not modified**.

This dossier reconciles a documented tension —

> *"The authentic high block is **gapless** because the original Suzuki kernel is compact"*
> (`research/2026-10-20/RH_RIGIDITY_LANE.md:29–35`)

versus

> *"`D ≥ κ I_E` in the primitive Hilbert realization"*
> (`research/2026-10-19/DIRECTIONAL_ORIGINAL_INVERSE.md:21–29`,
> `research/2026-10-19/ORIGINAL_SOURCE_FORM_CLOSURE.md:121–135`)

— and then answers one RH-specific question: **does the corrected quantitative-rigidity
machinery (`observational_succ/quantitative_rigidity.py`, now with the high-block-PSD
obligation) change an actual bound for the original first-window `S₄ = A₄ − R₄`?** The answer,
proved below, is **no**, with a precise no-go.

Status labels are AGENTS.md: CLASSICAL / PROVED LOCAL / HYPOTHESIS / CONJECTURED / UNVERIFIED /
REFUTED.

---

## 1. Source-attested OPERATOR DICTIONARY

Two carriers appear in the repository, linked by the integration (primitive) map `V`. The single
most important reading error this dossier exists to prevent is conflating the **two distinct
objects both written `K`**, and conflating **absolute** with **K-relative** gaps.

### 1.1 The two carriers and the map V

| Object | Symbol | Definition | Carrier / norm | Attestation |
|---|---|---|---|---|
| Derivative carrier | `H_d` | `L²₀(−1/2,1/2)` = mean-zero derivatives `u` | `L²` inner product `⟨·,·⟩` | `certified_four_schur_trial.py:10–16`; `.py:1` |
| Primitive carrier | `H_p`, `E` | `H_p = L²(I)`, `I=(−1/2,1/2)`; `E = (deg ≤ 3 polys)^⊥` | `L²(I)` inner product | `DIRECTIONAL_ORIGINAL_INVERSE.md:21`; `ORIGINAL_SOURCE_FORM_CLOSURE.md:1,13` |
| Integration map | `V` | `(Vu)(x) = ∫₋½ˣ u`, primitive with left-endpoint 0; `Vu = f` | `V : H_d → H_p` | `ORIGINAL_SOURCE_FORM_CLOSURE.md:141`; `DIRECTIONAL_…:31` (`Fᵢ = V(Pᵢ(2x))`) |
| Inverse-Neumann metric | `K` **(metric)** | `K = V*V = (−Δ_N)^{-1}`, so `K^{-1} = −Δ_N` | positive, **compact** on `H_d` | `certified_four_schur_trial.py:14`; `suzuki_moment_schur.py:128,149` |
| Bounded source part | `K` **(bounded)** | `K = −C·I − w·A_b + 2(c⊗c) − 2(s⊗s)`, `C = log(8π)+γ+π/2` | bounded self-adjoint on `H_p` | `ORIGINAL_SOURCE_FORM_CLOSURE.md:26–36` |

> **Naming-collision hazard (flag, not a renaming).** `K = V*V` (the inverse-Neumann *metric* on the
> derivative carrier, compact, positive) and `K = −C·I − w·A_b + 2(c⊗c) − 2(s⊗s)` (the *bounded
> source part* of the primitive form) are **different operators on different carriers**. Throughout
> this dossier I write `K_metric` and `K_bdd`. Any statement that silently composes one `K` where the
> other is meant is a category error. (This is an observation about documentation, not a code change.)

### 1.2 The signed form and its high-sector restriction, in EACH representation

| Representation | Signed operator | Blocks / high restriction | Norm in the coercivity statement |
|---|---|---|---|
| **Derivative** (`H_d`) | `G = [[A₄, B*],[B, D₄]]`, authentic completed signed Suzuki operator | `H_d = F₄ ⊕ H_high`, `F₄ = span{P₁(2t),…,P₄(2t)}`; high restriction `D₄ = Q_high G Q_high` | `D₄ ⪰ κ · Q₄ K_metric Q₄` — a **K_metric-relative** bound, explicitly **"not a derivative-L² spectral gap"** |
| **Primitive** (`H_p`, `E`) | `H∞`, completed primitive source form `q = qΓ + ⟨K_bdd·,·⟩` | `D` = form operator of `q` restricted to `E`; `Γⱼ = (4/dⱼ)I − Eⱼ`, `dⱼ = 4j+1` | `D ≥ κ I_E` — an **absolute** `L²(I)` gap |

Attestation of the two coercivity statements and their EXACT constants:

- Derivative, K-relative: `tate_weighted_bessel_four_schur.py:431–526`
  (`source_parity_split_four_moment_coercivity_certificate`): `D_{4,odd} ⪰ (63/500) K_odd`,
  `D_{4,even} ⪰ (153/500) K_even`, `D₄ ⪰ (63/500) Q₄ K_metric Q₄` (`:434–436`); constants
  `KAPPA_ODD_LOWER = 63/500`, `KAPPA_EVEN_LOWER = 153/500`, `KAPPA_GLOBAL_SHARPENED = 63/500`
  (`:318–320`); the coarse global constant `κ = 1/50` is `certified_four_schur_trial.py:73`.
- The explicit statement that the derivative bound is K-relative, **not** an L²-gap:
  `DIRECTIONAL_ORIGINAL_INVERSE.md:29` — *"Its derivative version is D4>=kappa Q4 K Q4, with K=V\*V.
  It is **not** a derivative-L² spectral gap."*
- Primitive, absolute: `DIRECTIONAL_ORIGINAL_INVERSE.md:21–27` (`D ≥ κ I_E`);
  `ORIGINAL_SOURCE_FORM_CLOSURE.md:121–135` (Consequence: IF `q(h) ≥ κ‖h‖²` on the compact-smooth
  core of `E`, THEN `D ≥ κI` and `D^{-1}` is bounded with `‖D^{-1}‖ ≤ κ^{-1}`).

### 1.3 Which operators are compact; which inverses are bounded

- `K_metric = V*V = (−Δ_N)^{-1}` is **compact and positive** with `0 ∈ σ(K_metric)` in the limit
  (`inverse_neumann_entry`, `suzuki_moment_schur.py:128,149`). Hence `K_metric^{-1} = −Δ_N` is
  **unbounded**. [CLASSICAL]
- The Γ-form multiplier satisfies `0 ≤ m(ξ) ≤ 5|ξ|` with `m(ξ) → 0` as `ξ → 0`
  (`ORIGINAL_SOURCE_FORM_CLOSURE.md:76–83`, Theorem C1). The low-frequency vanishing of `m` is the
  analytic face of the kernel's compactness: **`qΓ` has no absolute `L²` gap**. [CLASSICAL / PROVED (paper)]
- The authentic high block `D₄` is therefore **gapless in the derivative-L² metric**: every finite
  compression is strictly PD yet `inf σ = 0` — the `diag(1,1/2,1/3,…)` phenomenon
  (`RH_RIGIDITY_LANE.md:29–35`; `quantitative_rigidity.py:424–428` `inverse_decay_block`,
  `:468–472` `uniform_gap_profile`). So `D₄^{-1}` is **unbounded in the derivative-L² metric**.
  [PROVED LOCAL (exact witness family)]
- `D^{-1}` is **bounded (`≤ κ^{-1}`) in the primitive-L² metric ONLY IF** the absolute gap `D ≥ κ I_E`
  holds — which is itself the inherited, **unproven** hypothesis (next row). [HYPOTHESIS]

### 1.4 Which asserted gaps are ABSOLUTE, which are K-relative — and their status

| Statement | Metric | Kind | Status | Attestation |
|---|---|---|---|---|
| `A₄ ≻ 0` at `J = 64` (both parity blocks) | derivative `L²`, finite | absolute, **finite only** | VERIFIED EXACT MODEL | `ORIGINAL_FOUR_SCHUR_CERTIFIED_TRIAL.md:95,158` |
| `D₄ ⪰ κ Q₄ K_metric Q₄`, `κ∈{1/50; 63/500; 153/500}` | derivative, `K_metric` | **K-relative** | TESTED EXACT SOURCE DATA (inherited-source authority) | `tate_weighted_bessel_four_schur.py:431–526` |
| `D₄ ⪰ κ I` (derivative-L² absolute gap) | derivative `L²`, ∞-dim | absolute | **REFUTED** (gapless) | `RH_RIGIDITY_LANE.md:29–35` |
| `D ≥ κ I_E` (primitive-L² absolute gap) | primitive `L²`, ∞-dim | absolute | HYPOTHESIS (inherited, conditional) | `DIRECTIONAL_…:21–29`; `CLOSURE.md:121–135` |
| `qΓ ≥ κ‖·‖²` on `L²` (Γ-form absolute gap) | `L²` | absolute | **REFUTED** (`m(ξ)→0`) | `CLOSURE.md:76–83` |

### 1.5 Source-identification maps and their UNRESOLVED hypotheses

1. **Derivative→primitive transfer ("PR174 bridge").** Carries `D₄ ⪰ κ Q₄ K_metric Q₄` to
   `D ≥ κ I_E` on `E`. Its author explicitly **retains the inherited-source authority label rather
   than upgrading to a kernel proof** (`DIRECTIONAL_…:29`). Unmet hypothesis: a kernel-level proof of
   the four-moment coercivity on the authentic source. [HYPOTHESIS]
2. **Form-core closure (`ORIGINAL_SOURCE_FORM_CLOSURE`).** Theorem C2 (`CLOSURE.md:88–143`) proves
   `C_c^∞(I) ∩ E` is a genuine **form core**, so an estimate on the core transports to all of `Q∩E`.
   This is a conditional: *"conditional on the correctness of those independently derived source/core
   inequalities"* (`CLOSURE.md:134–135`). It does **not** prove the estimate; `CLOSURE.md:3–10`
   states it proves neither the numerical coercivity, nor its source identification, nor the Schur
   sign, nor RH. [PROVED LOCAL (closure step only); the coercivity premise is HYPOTHESIS]
3. **Completed signed Weil identification (CTW-08).** `G`/`H∞` = the completed signed Weil
   distribution: CLASSICAL IDENTIFICATION. The **source-derived positive factorization**
   (what RH needs) is UNVERIFIED / RH-hard (`ORIGINAL_FOUR_SCHUR_CERTIFIED_TRIAL.md:167–168`;
   AGENTS.md §6 forbids silently asserting it).

---

## 2. The exact commuting diagram — and where it STOPS commuting

### 2.1 The diagram that DOES commute (no defect): V intertwines the two metrics

**Proposition R1 (metric intertwining). [CLASSICAL]** For `w ∈ H_high` with `f = Vw ∈ E`,

```
    ⟨D₄ w, w⟩_{H_d}   =   d(f)              (same physical signed form, two carriers)
    ⟨K_metric w, w⟩_{H_d}  =  ‖f‖²_{L²(I)}   (because K_metric = V*V)
```

*Proof.* `K_metric = V*V` (`certified_four_schur_trial.py:14`) gives
`⟨K_metric w,w⟩ = ⟨V*Vw,w⟩ = ⟨Vw,Vw⟩ = ‖f‖²_{L²(I)}`. The first line is the definition of `d` as the
restriction of the primitive form to `E` pulled back along `V` (`CLOSURE.md:146–168`,
`DIRECTIONAL_…:31–45`). ∎

**Corollary R2 (the reconciliation). [PROVED LOCAL]** Dividing the two lines of R1,

```
  ( D₄ ⪰ κ Q₄ K_metric Q₄  in H_d )   ⇔   ( d(f) ≥ κ ‖f‖²_{L²(I)}  for f = Vw, i.e. D ≥ κ I_E in H_p ).
```

The K-relative derivative gap and the absolute primitive gap are **the same inequality written in two
metrics**. The diagram

```
        (H_high, ⟨K_metric·,·⟩)  --V-->  (E, ‖·‖_{L²(I)})
               |  D₄ ⪰ κ K_metric              |  D ≥ κ I_E
               v                               v
             scalar κ    ===== identical =====  scalar κ
```

**commutes exactly.** There is **no** transport defect between these two *representations of the gap*.

### 2.2 Why "gapless" and "`D ≥ κ I_E`" are NOT in contradiction

The tension dissolves once the metric is tracked:

- **"Gapless"** (RH_RIGIDITY_LANE) = *no absolute gap of `D₄` in the **derivative-`L²`** metric*:
  `D₄ ⋡ κ I_{H_d}` for every `κ > 0`. **REFUTED to claim otherwise** — this is true, the compact
  kernel forces it (`RH_RIGIDITY_LANE.md:29–35`).
- **"`D ≥ κ I_E`"** (DIRECTIONAL/CLOSURE) = an absolute gap in the **primitive-`L²`** metric, which by
  R2 is exactly the K_metric-relative derivative gap. [HYPOTHESIS]

Both hold simultaneously with **no contradiction**, precisely because `V` is **not** a metric
isomorphism: `K_metric = V*V` is compact, so `V` is not bounded below as a map
`(H_d, ‖·‖_{L²}) → (H_p, ‖·‖_{L²})`. The same operator is gapless in one metric and gapped in the
other. This is the rigorous content of the standing SUCC caution restated in the task:

> **a compact operator in one space does NOT imply absence of coercivity in a differently-normed
> representation.** [PROVED LOCAL — witness below]

### 2.3 The transport defect that is REAL: K-relative ↦ absolute is UNSOUND

The commuting diagram of §2.1 moves the gap *between metrics faithfully*. The **forbidden** move is to
feed a K-relative gap into a theorem that requires an **absolute** gap — e.g. into the bounded-inverse
Schur surrogate `A − κ^{-1} B B*` (`conservative_surrogate`, `quantitative_rigidity.py:562–569`),
which is a valid lower bound for `A − B D^{-1} B*` **only when `D ⪰ κ I` holds in the complement's own
metric**.

**Theorem R3 (exact sign-flip witness). [PROVED LOCAL]** There is an exact rational block `M` and a
genuine K-relative gap that, misread as an absolute gap, flips the certified Schur sign.

Take `M = [[2,0,1],[0,1,0],[1,0,1/10]]`, `n_A = 1`, high block `D = diag(1, 1/10)`, `κ = 1`,
`K = D`. Then (all exact, machine-checked):

- `D ⪰ κ K` **holds** (`D − 1·K = 0`): a real, uniform K-relative gap.
- `D ⪰ κ I` **fails** (`D − I = diag(0, −9/10) ⋡ 0`); `‖D^{-1}‖ = 10 > 1`: no absolute gap at `κ=1`.
- absolute surrogate `A − κ^{-1} B B* = [1] ≻ 0` — would **certify POSITIVE**;
- true Schur `A − B D^{-1} B* = [−8] ≺ 0` — actually **NEGATIVE**;
- exact negative vector of `M`: `v = (1, 0, −10)`, `vᵀ M v = −8 < 0`.

The sign flips. This is implemented and tested exactly in
`observational_succ/operator_space_dict.py::k_relative_misread_as_absolute`
(`tests/test_operator_space_dict.py::TestTransportDefect`), and it reuses the repository's own
`schur_complement`, `conservative_surrogate`, `negative_witness`, `coupling_negative_vector`
(`quantitative_rigidity.py:279,562,241,409`). It is the clean echo of the paper counterexample
`D = [[2,9/5],[9/5,2]]` with `(D^{-1})₂₂ > 1` (`DIRECTIONAL_ORIGINAL_INVERSE.md:73`) and of Gemini 1.1
(`RH_RIGIDITY_LANE.md:20–26`).

**Companion witness (gapless yet K-coercive). [PROVED LOCAL]** For `D_N = diag(1,1/2,…,1/N)`
(`inverse_decay_block`), the absolute least eigenvalue is `1/N → 0` (no uniform absolute gap) while
`D_N ⪰ 1·K_N` with `K_N = D_N` is a **uniform** K-relative gap `κ = 1` for every `N`
(`operator_space_dict.py::gap_notion_witness`, `tests…::TestGapNotionsAreDistinct`). Exactly the
authentic phenomenon in miniature.

> These are **generic exact linear-algebra witnesses**. They are **not** the authentic signed source;
> `source_form_identified = False`, so `operator_space_dict.transport_defect_diagnostics()` returns
> `certificate_status = REFUTED` (and would be INAPPLICABLE even if PSD). No signed-Weil positivity is
> manufactured here.

---

## 3. RH-SPECIFIC DELIVERABLE — does the rigidity core move the `S₄` bound?

**Verdict: UNCHANGED. `S₄` stays CERTIFIED AMBIGUOUS.** The corrected quantitative-rigidity machinery
sharpens the *obstruction accounting* (it makes the absolute-vs-K-relative hazard an exact, tested
statement) but supplies **no** new estimate on the authentic first-window `S₄ = A₄ − R₄`. Below is the
precise no-go, by obligation.

Recall the live object (`ORIGINAL_FOUR_SCHUR_CERTIFIED_TRIAL.md:22–26`,
`certified_four_schur_trial.py:10–31`): `S₄ = A₄ − R₄`,
`R₄(x) = sup_{z∈H_high}(2Re⟨Bx,z⟩ − ⟨D₄z,z⟩)`, with the already-proved residual theorem
`A₄ − L_U − (1/κ) T_{r_U} ⪯ S₄ ⪯ A₄ − L_U` (`ORIGINAL_FOUR_SCHUR…:37–54`).

### NO-GO 1 — the bounded-inverse Schur needs an ABSOLUTE gap the authentic block lacks (sharpest)

The finite Schur theorem (`quantitative_rigidity.py:19–31,279–285`) and its bounded surrogate
`A − κ^{-1} B B*` (`:562–569`) require `D > 0` / `D ⪰ κ I` **in the complement's own metric**, giving a
**bounded** inverse response `κ^{-1} I`. The authentic `D₄` has **no** such absolute gap in the
derivative-`L²` metric (gapless; §1.3, §2.2). The only gap available is **K_metric-relative**
(`D₄ ⪰ κ Q₄ K_metric Q₄`). Substituting it into the absolute surrogate is **exactly the unsound move
Theorem R3 refutes** (sign flip `[1]≻0` vs `[−8]≺0`). The *correct* inverse response under a
K-relative gap is `κ^{-1} K_metric^{-1} = κ^{-1}(−Δ_N)`, i.e. the derivative-energy residual Gram
`κ^{-1} T_{r_U}` — which is **already** the residual theorem's lower bracket
(`certified_four_schur_trial.py:23–31,425–436`). quantitative_rigidity's bounded-inverse Schur
therefore yields **nothing sharper** than the term the certified trial already carries.
[PROVED LOCAL — the no-go; the authentic sign stays UNVERIFIED]

### NO-GO 2 — the new high-block-PSD obligation does not upgrade to a usable gap

`RigidityDiagnostics.high_block_psd` (`quantitative_rigidity.py:499,525–529`) is a load-bearing check
that `D ⪰ 0`. For the authentic block `D₄ ⪰ 0` but `inf σ(D₄) = 0` (PSD, not uniformly PD). The
singular route — `shorted_complement` with range inclusion `ran(B*) ⊆ ran(D)`
(`:288–306`) — needs (a) that range inclusion for the authentic arithmetic coupling `B` (not
established) and, decisively, (b) a **bounded** shorted inverse response, which is again the unbounded
`κ^{-1} K_metric^{-1}` term. The finite-compression PD facts (`A₄ ≻ 0` at `J=64`) are precisely the
`inverse_decay_block` trap — *every* finite block PD, *no* uniform gap
(`:424–428`; `RH_RIGIDITY_LANE.md:29–33`). The obligation is consistent with, and reinforces,
CERTIFIED AMBIGUOUS; it flips nothing. [PROVED LOCAL]

### NO-GO 3 — form-core transport is conditional, not a positivity generator

Theorem 2.3 (`quantitative_rigidity.py:606–665`; `QUANTITATIVE_RIGIDITY.md:79–107`) transports
`q ≥ 0` **from** a genuine form core **to** the whole domain. It needs (a) a true form core for the
*authentic* form — `ORIGINAL_SOURCE_FORM_CLOSURE` Theorem C2 supplies this closure step but **only
conditional** on an independently-proved `q(h) ≥ κ‖h‖²` on the core (`CLOSURE.md:121–135`) — and (b)
an actually-proved pointwise positivity on that core. Positivity of the authentic **signed**
first-window form on the core is **the open question itself**; 2.3 cannot supply it. The
`form_core_negative_control` (`:630–665`) is an exact reminder that `L²`-density ≠ form-core density —
it blocks a bogus transport, it does not enable a real one. [PROVED LOCAL]

### NO-GO 4 — the source-identification obligation is unmet (ultimate wall)

`RigidityDiagnostics.source_form_identified` (`:498,535–536`) is load-bearing: a perfectly real
positivity fact about a *proxy* Gram is `INAPPLICABLE` as a source certificate (`certificate_status`,
`:507–537`). A positive auxiliary Gram / source-independent covariance is **not** the completed signed
Weil form (`RH_RIGIDITY_LANE.md:37–45`; AGENTS.md §6). quantitative_rigidity operates on
already-given matrices; it neither asserts nor can assert the missing **source→positive-Weil
factorization** (UNVERIFIED / RH-hard, `ORIGINAL_FOUR_SCHUR…:167–168`). My
`transport_defect_diagnostics()` demonstrates the verdict machinery itself returns REFUTED/INAPPLICABLE
on a generic PSD surrogate, not VERIFIED. [PROVED LOCAL]

### 3.5 What actually binds — unchanged

The binding constraint remains the **`1/κ = 50` amplification on the even-parity block**
(`ORIGINAL_FOUR_SCHUR_CERTIFIED_TRIAL.md:105–118`; `RH_RIGIDITY_LANE.md:53–60`). At the numerically
optimal `U`, the tight continuum residual bracket `A₄ − L_U − (1/κ)C_quot` is itself
**negative-definite** (all four eigenvalues `< 0`, `ORIGINAL_FOUR_SCHUR…:108–115`): even a perfectly
certified residual Gram would not flip the verdict POSITIVE under `κ = 1/50`. **No theorem in
`quantitative_rigidity.py` touches `κ`.** Hence no bound on `S₄` changes.

The single sharpest statement: **the authentic high block offers only a K_metric-relative gap, and a
K-relative gap is not an absolute gap** (Theorem R3 / NO-GO 1). Every route in the corrected rigidity
core that could sharpen `S₄` silently assumes an absolute gap the authentic block does not possess;
feeding the real (K-relative) gap in is exactly the sign-flipping error the core now flags.

---

## 4. Status ledger

| Claim | Status | Receipt |
|---|---|---|
| R1 metric intertwining `⟨K_metric w,w⟩ = ‖Vw‖²`, `⟨D₄w,w⟩ = d(Vw)` | CLASSICAL | `certified_four_schur_trial.py:14`; `CLOSURE.md:146–168` |
| R2 K-relative derivative gap ⇔ absolute primitive gap (same inequality, two metrics) | PROVED LOCAL | §2.1; `DIRECTIONAL_…:29` |
| "gapless" and "`D ≥ κI_E`" are consistent (different metrics; `V` not bounded below) | PROVED LOCAL | §2.2; `CLOSURE.md:76–83` |
| R3 K-relative-misread-as-absolute flips the Schur sign (`[1]≻0` vs `[−8]≺0`) | PROVED LOCAL | `operator_space_dict.py`; 8 tests OK |
| gapless family `D_N` yet uniform K-relative `κ=1` | PROVED LOCAL | `operator_space_dict.py::gap_notion_witness` |
| `D₄ ⋡ κ I` in derivative-`L²` (absolute gap claim) | REFUTED | `RH_RIGIDITY_LANE.md:29–35` |
| `D ≥ κ I_E` in primitive-`L²` (inherited) | HYPOTHESIS | `DIRECTIONAL_…:21–29`; `CLOSURE.md:134–135` |
| quantitative-rigidity core changes an `S₄` bound | **REFUTED (no change)** | §3 NO-GO 1–4 |
| `A₄ ≻ 0` at `J=64` (finite) | VERIFIED EXACT MODEL | `ORIGINAL_FOUR_SCHUR…:95` |
| residual theorem `A₄−L_U−(1/κ)T_{r_U} ⪯ S₄ ⪯ A₄−L_U` | PROVED LOCAL | `ORIGINAL_FOUR_SCHUR…:37–54` |
| §3C certified derivative-Gram tail modulus | CONJECTURED (named wall) | `ORIGINAL_FOUR_SCHUR…:137–152` |
| source-derived positive Weil factorization | UNVERIFIED / RH-hard | AGENTS.md §6 |

---

**RH: OPEN. S₄ sign: CERTIFIED AMBIGUOUS (unchanged).**
