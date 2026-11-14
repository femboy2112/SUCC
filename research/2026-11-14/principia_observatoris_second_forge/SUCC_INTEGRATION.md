# Integration with established SUCC structures

**Second Forge, 2026-11-14.** Each row states an explicit mathematical relationship between a
result of this package and an existing SUCC structure, with its evidence level. Three levels are
used and kept apart:

- **REPLAYED** — an existing SUCC object is run through the new statement in an exact test.
- **DERIVED** — a paper proof relates the two, with no shared code.
- **UNAUDITED ANALOGY** — the structures look related; no map was checked. These are mapping
  hypotheses for future work and carry no evidential weight.

No ledger status of any existing claim is changed by this package. The foundational results
remain valid if every arithmetic application fails; none of them proves or advances arithmetic
normality, RH, Goldbach or any physical claim.

## 1. Principia ancestral relations (PAP-01 … PAP-05)

| Existing | New | Relationship | Level |
|---|---|---|---|
| PAP-01 hereditary-predicate characterisation | QG-1 | PAP-01 is QG-1 over truth values; Lean `star_propQ_iff` identifies the weighted closure over `Prop` with reflexive-transitive closure | DERIVED + kernel-checked |
| PAP-02 projection soundness | QG-2 | same statement over every value structure; over costs it reads `d_Q ≤ d_source` | DERIVED + kernel-checked |
| PAP-03 four-way exactness; selected-start form (5) | QG-3 | generalised verbatim; commutativity never used | DERIVED + kernel-checked |
| PAP-04 strict hierarchy endpoint < cost < trace | change of base (`exactAt_map`) | exactness transports along homomorphisms of value structures and not backwards; SUCC's chain `a→b→c` is exact over truth and a one-step ghost over step counts | REPLAYED (`test_observatoris_integration.AncestralChainIsACostGhost`) |
| PAP-04 three-state ghost | ghost defect | the same `Machine` is audited by `audit_ancestral_observer` and by the cost geometry; the Lean control replays it through the truth-value instance | REPLAYED |
| PAP-05 hereditary obstruction certificate | potentials | a `V`-valued potential with unit at the start that is small at the report is the weighted certificate; over costs it is a feasible potential certifying a distance lower bound | DERIVED |
| `FutureSafeForgetting.lean` (transition congruence lifts whole paths from every representative) | QG-4 | a congruence makes may- and must-quotients agree, which is sufficient (not necessary) for exactness at every value level | DERIVED (see the Causal Geometer report for the exact relation) |

New relative to the existing supplement: the must-side bound and the two-sided sandwich (QG-4);
the adjunction `Cl_Q∘q_! ⊣ q^*` and "exactness ⇔ `Sat∘Cl` idempotent" (KT-6); and the corollary
that a may-quotient geometry has no unseen ancestors (QG-5).

## 2. Finite observers and carrier-relative targets

| Existing (`docs/CARRIER_RELATIVE_TARGETS.md`) | New | Relationship | Level |
|---|---|---|---|
| behavioural partition, observer algebra | KT-1 / FO-2 | adds the sharp experiment-length bound `n+m−1`, uniqueness of the core isomorphism, and constructive reconstruction from words of length `≤ 2n−1` | DERIVED; cross-checked against `carrier_relative_targets` in the FO tests |
| `plan_target` (budget-bounded single-copy planner) | FO-10 | an exact **all-horizon** decision by a least fixed point on beliefs; agrees with `plan_target` within its budget | REPLAYED |
| §3 destructive A,B,C carrier | FO-10, CA-1 | free observation (no operation changes the behaviour class) is sufficient for single-copy access; "commuting and idempotent" is not; **executable knowledge is not closed under conjunction** (new boundary) | REPLAYED |
| §4 target oscillation radius `ω/2` | FH-10 | with a declared modulus the limit's oscillation after `N` terms is exactly `2μ(N−1)`, so the optimal radius is `μ(N−1)` | DERIVED |
| §5 compact target completion (no rate from bare compactness) | FH-10, FH-5 | supplies the missing quantitative half: a modulus gives the rate; without one, limit identification holds with no certificate | DERIVED |
| §5 "normality is not a continuous Boolean function of the prefix topology" | FH-1, FH-11 | the general statement: a readout-only protocol decides a target iff it is continuous at every point of the class | DERIVED |

## 3. Contextual zero

For a possible-state set `B`, SUCC's contextual zeros are `I(B) = {f : f|_B = 0}`. Restricting to
the observer algebra `𝒜` of all lawful experiments:

> **CZ-link (PROVED; REPLAYED).** The common zero set of `I_𝒜(B)` is exactly the behavioural
> saturation of `B`. Hence observational closure `Sat` is the Galois closure of the
> zero-ideal/zero-set connection between state sets and the observer algebra.

*Proof.* `𝒜` is the algebra of class-constant functions (inherited theorem). `f ∈ 𝒜` vanishes on
`B` iff it vanishes on every class meeting `B`, so the zero set contains `Sat(B)`; for `x ∉ Sat(B)`
the indicator of the class of `x` lies in `I_𝒜(B)` and is nonzero at `x`. ∎
*Test:* `ContextualZeroIsSaturation`, using SUCC's own `observable_algebra` rows.

So "unresolved source distinctions as exact compatible source fibres" and the saturation closure
of KT-6 are the same object. Learning (`B' ⊆ B`) enlarges the ideal; exactness (KT-6) says the
dynamics does not create new zeros that the observer cannot attribute to a reachable state.

## 4. SUCC and FUCC under observation

Successor `x ↦ x+1` and the multiplier `x ↦ 2x` on `ℤ/12`, each under a residue observation
(`x mod 3`) and a magnitude observation (`⌊x/4⌋`):

| Operation | Observation | Truth-level exact | Cost-level exact | Mechanism |
|---|---|---|---|---|
| SUCC | residue | yes | yes | the observation is a congruence |
| FUCC-2 | residue | yes | yes | the observation is a congruence |
| SUCC | magnitude | yes | **no** | a *carry*: the quotient claims one step where the source needs four |
| FUCC-2 | magnitude | **no** | no | `0` is a fixed point and `1` is not, yet both read "small"; `{0}` is the hereditary obstruction |

*Level: REPLAYED* (`SuccessorAndMultiplierUnderObservation`). This is a finite illustration of
how the two operations transport dependencies differently through a non-congruence observation:
additive transport fails only quantitatively, multiplicative transport fails qualitatively at a
fixed point. It is a statement about `ℤ/12`. Nothing is claimed about digit dynamics of any real
constant.

## 5. Computational graphs and boundary ports

| Existing | New | Relationship | Level |
|---|---|---|---|
| BPGS-04/08: hidden diamond is boundary-indistinguishable; an intervention response repairs it | RG-1c and the restoring instrument; FO-8 | the same phenomenon in two exact settings: a structurally present, behaviourally void dependency that a new intervention exposes | UNAUDITED ANALOGY (the resistor-network proofs were not re-derived) |
| BPGS-07: zero first and mixed second boundary variations, possible cubic coupling | FO-4 | an instance of the intervention-order horizon: a dependency living only above a given interaction order | UNAUDITED ANALOGY |
| edge-carrier / graph reconstruction supplements | FO-9, RG-5 | FO-9 gives an exact identifiability criterion for unrestricted network classes; RG-5 says which edge magnitudes are unit conventions | not compared |

## 6. Haar / Fourier and the positivity firewall

AGENTS.md item 6 forbids inferring source-derived positivity from physical or semantic
positivity. The response-side theorems respect and sharpen that boundary:

- positivity (more generally balance) is a **hypothesis** under which structure and response
  coincide (RG-1b, RG-4); it is never derived from observations;
- a hidden, cancelled dependency **requires** an unbalanced sign pattern, and first-order probes
  miss any dependency of higher interaction order (FO-4);
- consequently a signed cancellation question cannot be settled by structural (support)
  information alone. This is a no-go for a method, not progress on any signed estimate.

No relationship to the existing Haar-clock or Fourier–Yoneda modules was audited.

## 7. Yoneda and Scott

- *Yoneda (DERIVED, modest).* QG-1 says `x ↦ R*(x,·)` is the representable potential, and KT-1
  says `x ↦` (its response function) is injective exactly on the core. Both are the standard
  "an object is known by its responses" statement for this kernel. No comparison with
  `fourier_yoneda_pinbed` was made: UNAUDITED.
- *Scott (DERIVED, modest).* FH-11's finite-information topology is the Scott topology on finite
  prefixes: finitely verifiable properties are the open sets. The finite-surprise regime is open;
  the limit-only regime has empty interior on the promise. No comparison with the Scott-omega
  Lean lane or `research/2026-11-12/scott_relative_defect` was made: UNAUDITED.

## 8. Arithmetic source authentication

FH-6 is an exact toy of "a finite surrogate that reproduces observed data": the unique order-`n`
linear mimic of `1/(k+1)` is exact on `2n` terms and first errs by
`(n!)⁴/((2n)!(2n+1)!) ~ (π/2)·16⁻ⁿ`. It shows quantitatively that agreement with a
finite-complexity surrogate on a long prefix says nothing about membership of the true source
in the surrogate's class.

**What this does not do.** For π-normality any advance must address the authenticated
original-zero BBP source and its remaining signed cancellation obligation. Nothing here does.
By §6, the obligation is precisely of the kind that structural information cannot discharge.
New vocabulary is not progress on that theorem, and none is claimed.
