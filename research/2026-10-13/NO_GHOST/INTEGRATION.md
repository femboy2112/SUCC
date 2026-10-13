# NO-GHOST integration and reproduction map

## Stable entry points

- [MANUSCRIPT.md](MANUSCRIPT.md): principal scoped theorems and corrected verdict.
- [FRONTIER_AUDIT.md](FRONTIER_AUDIT.md): immutable prior results and acceptance states.
- [COHERENCE.md](COHERENCE.md): detailed schedule proofs and actual comparison maps.
- [GLUING_REPAIR.md](GLUING_REPAIR.md): site, join-tree specialization, repair/no-go proofs.
- [PRIOR_ART.md](PRIOR_ART.md): five required full papers plus seven further primary PDFs.
- [FORMAL_VERIFICATION.md](FORMAL_VERIFICATION.md): exact declarations/axioms and compiler.
- [claim supplement](../../../docs/CLAIM_SUPPLEMENT_NO_GHOST.md): disjoint `NG` namespace.
- [VALIDATION.json](VALIDATION.json): executed checks and content fingerprints.

## Extending existing attachments

| Existing structure | Added layer | Boundary |
|---|---|---|
| `carrier_indexed.py` original/current joint law | `FiniteContract` explicit source/history kernel and occurrence IDs | No conversion of private source into public input; model rows remain declarations |
| CAR lawful quotient and stable refinement | Explicit countermodels and finite declared repair-cost search | Mathematical partition is not a licensed sensor |
| C22 outcome-channel commutation | `check_diamond`, source-Dirac witness, continuation counterexample | Existing theorem credited; complete future histories not inferred from a two-step row |
| F48 incidence history sheaf | Constraint-complete Lean gluing core; paper schedule-presentation descent | No imported WIP files, no general sheafification-to-source realization |
| Nonabelian graph holonomy | Permutation-valued selected private-history transports and braid witness | Faithful branch-value preservation is stricter than weight preservation |
| C17/C18 stochastic histories/couplings | Exact legal-atom marginal LP and fixed-kernel prefix equations | Arbitrary tuple space and arbitrary atom reweighting are excluded from operational conclusions |
| Public adaptive policies | `no_ghost_policy.py` finite realization-plan compiler and independent replay | Finite fixed decision horizon, perfect public recall, one controller; no decentralized theorem |
| VOYAGER/Cambrian source realization | Countermodel boundary retained | No claim finite support solves infinite source completion |
| Lean4.14 core | New `formal/NoGhost.lean`, isolated verifier and CI | Inherited topology4.14/mathlib and separate EOS4.19 remain distinct |

The implementation is additive; it does not replace `Engine`, `ActualHistory`,
`ControlledCarrier`, historical defaults, imported archives, or existing formal
environments. The new closed-world finite tables are an explicit research
contract. Missing rows mean unavailable actions. If rows are merely *unknown*,
the user must report UNRESOLVED rather than interpret the table's mathematical
negative as an empirical impossibility.

## Reproduction

From the repository root:

```sh
python -m unittest discover -s tests -p 'test_no_ghost*.py' -v
python scripts/no_ghost_probe.py --output /tmp/no_ghost_exact_receipt.json
cmp /tmp/no_ghost_exact_receipt.json research/2026-10-13/NO_GHOST/examples/no_ghost_exact_receipt.json
scripts/verify_no_ghost_lean.sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Lean requires the checked-in `leanprover/lean4:v4.14.0` toolchain. The formal
report documents an optional self-executable-path compatibility adapter needed
only in this execution container. Normal CI uses the official pinned compiler
without it. Python has no new package dependency.

## API contract

1. Build `FiniteContract` using exact `Fraction` weights, declared source/basis,
   full preparation, carrier states/epochs, event dependencies and kernel rows.
2. Use `enumerate_schedule` to produce all positive possible paths of a specified
   complete schedule. Its access failures have replayable witnesses.
3. Use `check_diamond` on an explicit Dirac input domain. It tests complete joint
   outcome/endpoint law, not branch identity or future policy equivalence.
4. `event_context_problem` projects enumerated paths to retained occurrence
   receipts. `couple_contexts` returns **support-only** primal/dual certificates.
5. Add `operational_equations` for a fixed schedule, or compile all public
   choices with `compile_public_policy(model,horizon)` and use
   `operational_coupling` for a finite adaptive protocol.
6. Use `verify_policy_solution(model,system,plan,restrictions,laws)` to bind a
   positive plan to freshly source-derived equations and independent policy
   replay. `verify_policy_obstruction` similarly rebuilds the operational
   equations before checking a dual. The lower-level `verify_dual` only checks
   its supplied matrix; an arbitrary matrix is not a source certificate.
7. `minimum_declared_repair` optimizes only a previously certified legal menu.
   Costs and legal implementation of modifications are separate inputs.

Core terminal statuses distinguish lawful witnesses, diamond discrepancies,
chosen higher-coherence failures, source/interface/access failures, probability
duals, certified finite-menu repairs, and unresolved bounds. Internal compilation
is not a positive feasibility result. A `LAWFUL_GLUING` result from the generic
linear solver certifies only its supplied equations; the call's scope determines
whether they encode support, fixed kernels, or a complete public policy.

The frozen odd-parity negative is a *requested* incompatible marginal family,
not a claim those marginals were empirically collected under the fixed uniform
source. Its positive control uses the actual declared uniform preparation.
Likewise the hidden-oracle law is a falsifying request, not an observed event.

## Integration order and remaining gates

This branch is stacked on frozen PR #53. A future consolidation must still
reassess #49 and its child branches rather than merging their WIP transitively.
The F48 child at `8dacc56cec68b2e998529caf31f34fb5beeaa1d3` was additionally
inspected: A03 core review accepted, final principal artifact review pending.
It is a later child snapshot than the pinned PR49 parent. No acceptance status
is silently transferred across those two commits.

Before a main integration, run the full suite and both actual formal lanes
on the resulting integration commit, preserve each ancestry/provenance record,
deduplicate equivalent theorem names by attribution, and reconcile API types.
The present user authorized a draft contribution, not a main merge.

Next mathematical gate: a decomposition theorem for the operational policy
polytope across causal interfaces, with information-set compatibility retained.
Ordinary join-tree marginal gluing does not establish that gate. Also open:
mechanize the full finite-poset coherence presentation and the policy LP theorem;
implement general constraint sites; prove an adapter to causal-function/event-
structure semantics; authenticate physical kernels if actual instruments exist.
