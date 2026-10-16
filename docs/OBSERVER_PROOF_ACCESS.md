# Observer and Proof-Access Foundations

How a finite embodied observer's **access to a global mathematical target** is classified, kept
separate from the carrier algebra ([CARRIER_ATLAS.md](CARRIER_ATLAS.md)) and from the RH
application ([RESEARCH_FRONTIER_2026-10-15.md](RESEARCH_FRONTIER_2026-10-15.md)).

The governing rule: **a field label is never intrinsic to a mathematical object.** It is a property
of a triple `FieldClass(Source, Target, Tools)` — what the lawful source is, what global interface
is requested, and which effective toolkit is allowed. The same target can be Simple under one
toolkit and IdealHard under another. Status vocabulary follows [AGENTS.md](../AGENTS.md).
**RH remains OPEN and is NOT classified here.**

Canonical definitions: `observational_succ/field_limit_compactness.py:172-185`
(`source_dependent_field_frontier`); proof development in
`research/2026-10-15/FIELD_LIMIT_TRICHOTOMY.md` §0.

## 1. The four-class taxonomy

- **SimpleField** — *a verified finite program supplies the interface.* A finite, source-faithful
  symbolic description plus a query program returns any requested finite coordinate of the
  (possibly infinite) global target in finite time, with a proof of lawful source compatibility.
  (Finite program + proof — **not** an enumeration of all coordinates.)

- **IdealHardField** — *provable, but no computable witness.* The source laws give a finite classical
  proof that the global target exists / is true, yet the declared effective toolkit has **no
  computable selector** for an exact global witness. The impossibility of a computable selector must
  itself be *proved* — mere slowness does not qualify.

- **FuckedField** — *a proved impossibility or a nonidentifiable fiber,* in three disjoint modes:
  - **nonexistence** — the specified global source provably does not exist, though every finite
    horizon is satisfiable;
  - **nonidentifiability (toolkit)** — the permitted action/readout closure identifies distinct
    source states that carry different target values;
  - **phantom source-map** — every finite observation is matched by *some* source, but no single
    source realizes the whole tower (quantifier order `∀N ∃z`, not `∃z ∀N`).

- **Unresolved (toolkit-relative dark)** — none of the above is *proved*: "we cannot currently prove
  or disprove this within this toolkit." This is explicitly **not** a theorem of mathematical
  impossibility. (The module header `field_limit_trichotomy.py` summarizes the first three classes;
  the fourth, `Unresolved`, is the complete-taxonomy class defined in `field_limit_compactness.py:172-185`
  and used at `field_limit_trichotomy.py:341`.)

## 2. Calibration examples actually present

| Class | Calibration | Location | Status |
|---|---|---|---|
| Simple | 2-adic point x_n = seed mod 2^n, uniform coordinate decoder + modular coherence | field_limit_trichotomy.py:51; source_field_inverse_limits.py:53 | PROVED ELEMENTARY |
| IdealHard | decidable finitely-branching Kleene binary tree: every level inhabited (König path exists), no computable path (self-diagonalization) | field_limit_trichotomy.py:124,143,166; source_field_inverse_limits.py:105 | CLASSICAL / PROVED PAPER |
| IdealHard boundary | effective compactness + UNIQUE path ⇒ computable path; so a no-computable-path tree has ≥2 paths | field_limit_trichotomy.py:272; field_limit_compactness.py:149 | PROVED CLASSICAL |
| Fucked / nonexistence | noncompact tail X_n={m≥n}; strictly-decreasing-naturals tree — every finite level inhabited, empty global limit by well-foundedness | field_limit_trichotomy.py:188; source_field_inverse_limits.py:148 | PROVED ELEMENTARY |
| Fucked / source-map (phantom) | profinite CRT ghost (x_2=1, x_p=0 odd p): ∀N∃z_N matching N stages, ¬∃z∀N; even-coordinate phantom 0^ω vs (01)^ω | field_limit_trichotomy.py:210; source_field_inverse_limits.py:174 | PROVED EXACT (quantifier-correct) |
| Fucked / toolkit | hidden-tag source {(x,t)}; action flips x, readout reads x only; (0,0),(0,1) indistinguishable for all words; new-tag probe repairs | field_limit_trichotomy.py:244 | PROVED EXACT |
| Unresolved | Tate/Suzuki completed Weil sign: proved high-sector coercivity, uncertified all-radii low-Schur sign → not classifiable | field_limit_trichotomy.py:326; source_field_inverse_limits.py:254 | UNVERIFIED / not classifiable |

## 3. Supporting proof-access foundations

- **Compact gluing (positive counterpart), conditional.** Compact Hausdorff X + closed observation
  fibers with the finite-intersection property ⇒ nonempty global intersection; separation ⇒ at most
  one source. `field_limit_compactness.py:42`; FIELD_LIMIT_TRICHOTOMY.md §6. Explicitly **not
  constructive** (`construction_algorithm_delivered=False`).
- **Operator/Hilbert compactness gate.** WOT unit-ball Banach–Alaoglu proves all finite constraints
  *would* glue, but feasibility of those constraints is not proved, and it cannot be used across
  differing widths without coherent source-labeled embeddings. FIELD_LIMIT_TRICHOTOMY.md §11.
- **Finite interface ≠ finite information.** Ω4 = Σ 4^−(e+1)·1[φ_e(e)↓] is a provably noncomputable
  real with exact rational enclosures; a finite observer handed Ω4 would hold unbounded halting
  information as an assumed oracle. `field_limit_trichotomy.py:349`; §10.
- **Ordinal proof-access firewall.** Goodstein/ε₀ well-foundedness gives *sure* pathwise finite
  termination; ranking supermartingales give *almost-sure* termination (a summable-hazard stuttering
  countermodel and an infinite-expected-length example show these are distinct); **neither yields a
  signed Schur/Weil sign.** `ordinal_ranked_succ.py`, `ordinal_epoch_supermartingale.py`,
  `ordinal_martingale_boundary.py` (negative control at :130 — a terminating normalizer reaches
  schur=−3, so `ordinal_termination_implies_original_Weil_PSD = False`).
- **No-ghost gluing.** Exact-rational Farkas primal/dual certificates with independent
  re-verification; model-relative, never empirical ("checks a declared mathematical model, not its
  empirical authenticity"). Braid/holonomy failures are failures of a *chosen* map family, not of
  the existence of coherent families. `no_ghost.py`, `no_ghost_coherence.py`, `no_ghost_policy.py:171`.

## 4. Firewall

RH is **not** labeled IdealHard / impossible / undecidable / Fucked anywhere:
`"RH_is_mathematically_unprovable": "NOT_ESTABLISHED"` (field_limit_trichotomy.py:340);
`"RH_intrinsic_field_type": "UNVERIFIED"` (field_limit_compactness.py:183);
`"not_authorized_to_label_RH_FuckedField": True` (source_field_inverse_limits.py:286);
`"RH_intrinsically_unprovable": "NOT_ESTABLISHED"` (ordinal_martingale_boundary.py:168). The one
"if every anchored Gram is PSD … then RH follows" statement
(ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES.md:181) is the **classical Weil criterion as a conditional**, not
a proof. A positive source covariance is never identified with the signed completed Weil form; that
identification is flagged as the missing typed morphism. **RH remains OPEN.**
