# The Proof Forge — core (Academic Main VI)

**Date:** 2026-10-20. **Branch:** `research/proof-forge-mason-stothers-2026-10-20` (off `main` post-#192–#198).
**Thesis.** Move SUCC from *constructing and transporting objects* to *establishing global assertions about
them*. The pipeline is **CONSTRUCT → COUPLE → FIND INVARIANT → PROVE RIGIDITY → TRANSPORT → CERTIFY**; each
stage is a real mathematical obligation, not a software step.

**Discipline honored (§7).** No dozens of empty abstractions. Exactly three new modules were built, each
load-bearing for a *real* theorem; anything that could not carry a theorem was not written. Every new
theorem is classical or clearly labeled; exact arithmetic throughout; a green suite is not a proof.

## Modules (all new, all exercised by real theorems)

| module | stage | carries |
|--------|-------|---------|
| `observational_succ/arithmetic_interactions.py` | COUPLE | additive vs Dirichlet(multiplicative) convolution as *typed, non-interchangeable* operations; the `illegal_interchange_witness` firewall (smallest witness `N=5`). Carries the **Goldbach BS-G3 correction** and the abc work. |
| `observational_succ/proof_contracts.py` | CERTIFY | quantifier-aware proof obligations; mechanically forbids the `∀N∃C_N → ∃C∀N` swap (`assert_not_uniformized_from`). Carries the **Mason–Stothers** (clean `∀`) and **abc** (`∀ε∃K_ε∀triple`) contracts. |
| `observational_succ/mason_stothers.py` | FIND INVARIANT + PROVE RIGIDITY | the Wronskian `W=A'B−AB'` invariant, the divisibility `(ABC)/rad(ABC) \| W`, and the full degree-bound **certificate** with hostile controls and the integer-transfer obstruction. |

Plus `formal/MasonStothersDegreeDescent.lean` (the mathlib-free, `omega`-closed, choice-free arithmetic
core of the degree descent, with the polynomial lemmas disclosed as formalization debt).

## The five capabilities (§3) — built to the depth a real theorem needed

- **§3.1 additive–multiplicative interaction calculus.** `arithmetic_interactions`. **Cross-structure
  result delivered:** the exact separation `(Λ*+Λ)(5)=2log2log3 ≠ 0=(Λ*×Λ)(5)=[5^{-s}](−ζ'/ζ)²`, which
  *refutes* the BS-G3 phrasing "the Dirichlet series of R_Λ is `(ζ'/ζ)²`-type" (corrected in
  `black_sun_goldbach.py`; regression test added). The hostile counterexample to the illegal interchange
  is the `N=5` witness.
- **§3.4 invariant discovery & rigidity.** The Wronskian is the worked example: it has a source
  (derivation on `K[x]`), transformation law (three cyclic forms agree up to sign), preserved information
  (vanishes ⟺ linear dependence / char-p), lost information (constants), and a **rigidity consequence**
  (the degree bound). This is a genuine proof-producing invariant, not a reformulation.
- **§3.5 quantifier-aware certificates.** `proof_contracts`. The abc contract records `K` depends on `ε`
  but is uniform in the triple; the uniformization guard rejects the forbidden swap.
- **§3.2 uniform quantitative descent / §3.3 defect budgets.** *Deferred* — not forced into existence. The
  existing `parity_repair_cost` (#193, `C*=|E|−MaxCut`) already is a signed-defect/repair-cost object, and
  the abc re-derivation is the first transport-of-inequality example; a standalone module was not written
  because no *new* theorem yet needs one. (Per §7: if an abstraction cannot support a real theorem, it is
  not built.)

## First real boss — Mason–Stothers (polynomial abc): **DEFEATED**

Complete classical proof + exact SUCC certificate + char-`p` counterexample + Lean arithmetic core +
integer obstruction. Two independent verification routes (certificate via `factor_list`+Wronskian vs the
committed seeded oracle `tests/test_mason_stothers_oracle.py` via gcd-squarefree radical + direct bound
check, 380 triples, 0 violations) — the disagreement between them caught a real backwards-divisibility
bug. See `MASON_STOTHERS_PROOF.md` and `MASON_STOTHERS_CERTIFICATE.json`. Status **CLASSICAL** (no
mathematical novelty; the contribution is the reusable certificate). Completion criterion met: expressing,
verifying, generalizing, and interrogating the theorem is now one module, not ad-hoc scripts.

## Second application — Goldbach additive/multiplicative firewall

The BS-G3 correction (above) is the "at least one different theorem" the core must support besides
Mason–Stothers: a *different* mathematical setting (analytic number theory, not polynomial algebra) using
the same `arithmetic_interactions` + `proof_contracts` machinery. Legitimate Goldbach Fourier identities
(BS-G1/G2/G4) and their tests are retained unchanged.

## Firewall

**RH PROVED: NO. ABC OPEN. Integer abc OPEN** (the derivation/size-drop mechanism has no archimedean
integer counterpart — `integer_transfer_obstruction`). No zeta-zero construction input. Classical theorems
labeled CLASSICAL; nothing synthetic promoted to proved. The Proof Forge demonstrates the pipeline on
established mathematics and states its own limits; it does not claim to discover new mathematics.
