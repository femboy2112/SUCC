# Academic Main VII: integration and research receipt

Observed 2026-10-20. This is the post-merge coordinator record; earlier campaign
reports retain their own historical commits and are not relabelled as current.

## Mainline result and history

[PR #210](https://github.com/femboy2112/SUCC/pull/210) merged as
`b5f9591033db2022bda6a2f16a935c06466f9eff`. The actual main tree is
`47f36179aa08416b7e2107d438df4b24b4fe71be`, identical to the tested candidate
`950e2aaf3b59d5c19837c2a20cf70b014ead8845`. See the machine-readable
[main receipt](main_merge_receipt.json) and the complete
[incoming-head/ancestry/file-intersection audit](live_dag_and_coverage.json).

Initial main was `0e56e0ae26f3d52a2ea34c0a4288478139fcb634`. All ten live heads
matched the supplied snapshot. PR200 branched from the pre-merge Main VI tip
`c1a8cfb403fdec0f25a0917b83d04bb3875ad5cc`; the literal supplied main→200 edge
was inaccurate. The 200→201→209 chain was valid. Eight explicit merge commits
preserve that terminal stack and the seven independent cloud branches.
All ten original heads were verified as ancestors of the actual new main.
GitHub marked 200 and 202–208 merged; stacked 201/209 were closed as incorporated
with explicit cross-references. Every original branch remains available.

No source archive or licensing decision changed. All 72 provenance entries
remain valid: 55 mechanical namespace migrations and 17 byte-identical archives.
Manifest SHA-256:
`2eec9a3a730afdca338f92fbaf195e65130cec21efc68062206163f9f6a0d57f`.
The provenance anchor is `ba075348b7bcc66d938b3e0ca96c26e95bba340a`.

## Exact integration gates

All eight candidate workflows passed before the merge. The full suite ran on
Python 3.10 and 3.13: **6,496 tests on each**, followed by every required replay.
No required job step failed or was skipped. The exact full-suite run is
[39506818938](https://github.com/femboy2112/SUCC/actions/runs/39506818938).
Source cancellation/Schur 39506818866, collective source 39506818907, core
Lean 39506818974, orbit 39506818883, bidirectional 39506818922 and source-minimality
39506818879 all passed. Exact-candidate local provenance, foundation, ordinal,
namespace, import, wheel and navigation checks also passed.

The actual pinned formal build
[39506818873](https://github.com/femboy2112/SUCC/actions/runs/39506818873)
rechecked ten complete theorem types, source hashes, dependency revisions and
axioms. Lean 4.14.0 and mathlib
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84` are pinned. Actual admitted axioms
are `propext`, `Classical.choice`, `Quot.sound`; accepted sources contain no
sorry/admit/native_decide. Admission digest:
`9de79bcbe52c79f1829361c611d97a77b82dc08d9a5fe6181931b78865c8a9f4`.
The source-bound record is archived in `formal/kernel_audit/admitted/`.

Historical failed formal run 39504844561 is preserved: a wrapper incorrectly
scanned intentionally rejected mutation diagnostics for an error-recovery token.
The repaired gate distinguishes rejected controls from accepted proof logs;
accepted source/axiom requirements were not weakened. Superseded CI runs were
canceled rather than counted as successful. Two local unittest invocations named
nonexistent modules; discovery errors were corrected to the actual test modules
and were not counted as passing tests. Local Lean execution was unavailable
in this cloud container, so actual kernel verification used hosted pinned builds.

## Certification repairs and independent verification

Typed finite propositions bind the exact rational matrix and predicate. Typed
formal propositions bind complete kernel types and the admitted source/environment.
Unrelated English claims, theorem-name swaps, forged success JSON and caller
callbacks do not confer authority. Legacy contracts are immutable research
metadata; source Level D remains unavailable without a genuine checked transport.
The threat model trusts reviewed installed Python/dependencies and catalogue
admission; it does not claim protection against hostile code in the same interpreter.

Exact algebraic eigenvalue ordering replaces float sorting. Strict integer
singular-series cutoffs, the additional P=2 boundary, BBLT layer attribution,
the canonical sharper CRT bound and the abc dominance threshold are repaired.
Clean historical 201 exposes all nine hostile findings; 209 fixes two; the
repaired target fixes all nine. Additional exact matrix and authentic formal
holdouts passed. A finite hostile suite is supporting evidence, not a universal
proof that all future bugs are impossible.

The abc review reconstructs powerful-divisor positivity, primitive determinant
separation, low-weight singleton absorption, the radical-pair tail, global
Möbius primitivity and uniform-integrability limit. Separate implementations
check lattice/divisor counts, while the new Lean project checks the discrete
invariant. Same-model internal reviewers are not external mathematical referees.

## Post-main independent draft branches

Every branch below has the actual main commit above as its parent; no stacked
dependency on another new research branch is needed. The original reviewed code
heads are recorded here; later receipt-only commits do not silently relabel
historical builds as checks of new source content.

| Draft | Branch / initially published code head | Mathematical gain and validation |
|---|---|---|
| [211](https://github.com/femboy2112/SUCC/pull/211) | `astra-cloud/vii-slope-2026-10-20`, `e3d01df4a53a4e291d0e16a20d530493c10c6901` | Nine actual Lean declarations; determinant divisibility, reduced injectivity and modulus gap; two false mutations rejected |
| [212](https://github.com/femboy2112/SUCC/pull/212) | `astra-cloud/vii-arithmetic-2026-10-20`, `3519212c96085e62633ccdcb03074d43c7e8fedb` | Effective mean rate, uniform primitive divisor count and t≥1 obstruction ; 11 tests, 1,729 exact cases; self-contained manuscript |
| [213](https://github.com/femboy2112/SUCC/pull/213) | `astra-cloud/vii-operator-2026-10-20`, `d3e0ccf671b2ddc2a9e94549db77f60955ee7580` | Exact parity moment-Gram gains and fixed-budget impossibility ; 17 tests, 60 independent symbolic cases, held-out source receipts |

The actual slope run
[39508738928](https://github.com/femboy2112/SUCC/actions/runs/39508738928)
passed on its first attempt. Its record SHA-256 is
`094a35e5ed7dae06d99efb159e6283a674862f5441499f6f60e0efa12614cdc1`.
Its exact source hashes and all nine actual theorem types are exported. Axioms
are subsets of the same three documented axioms. Status is
KERNEL_CHECKED_NOT_AUTHORITY_ADMITTED: this research build does not modify the
trusted proposition catalogue. The full real spacing/count theorem and full
analytic mean theorem are not Lean-formalized.

For 0≤t<2/3 the arithmetic manuscript proves, with explicit constants,
`|S_t(X)/X²−C_t| ≤ C_(t,δ)X^(-δ)` for every 0<δ<(2−3t)/5.
At t=1 it proves liminf S_1(X)/(X²logX)≥1/(4ζ(2)log2), and for t>1 it gives
an explicit X^(t+1) lower bound. Thus [2/3,1) is the remaining moment interval.
The rate and divergence are complete paper proofs, not just exponent heuristics.
The [claim supplement](../CLAIM_SUPPLEMENT_ABC_EFFECTIVE.md) and
[draft manuscript](../../research/2026-10-20/ABC_EFFECTIVE_MEAN.md) state the
exact domains and constants. Academic novelty remains unverified; the manuscript
has not been submitted or published.

The operator gain retains source blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`; source receipt SHA-256
`321d80b0dc38aeddf52f6c0b0c398370b3b18fae285c6fbd1751acc999bc28f9`.
Both parity gains are positive definite at J=10, M=96, with independent certified
quadrature and separate J=6, M=72 source holdout. Even maximal two-moment correction
leaves the fixed budget's four diagonal ceilings negative. This refutes only
the sufficiency of that fixed budget, not the positivity of the actual source.

## Integration readiness and next decisive steps

Main VII is integrated and validated. The three new families remain drafts;
their current hosted check states are visible on their PRs and are not assumed
green from the mainline run. They introduce disjoint scientific files. Only the
arithmetic draft carries coordinator-owned registry/roadmap/receipt updates.
Recommended eventual order is slope invariant, arithmetic theorem, then source
refinement; the DAG permits any order after each family passes its own gates.
No conflict with an active Claude branch was introduced.

- **Arithmetic pathway:** sharpen the weighted divisor-boundary sum or constants;
  the requested first effective rate is now established in the draft.
- **Moment endpoint:** prove a stronger additive estimate on high-determinant
  singleton strata. The current y^(-2/3) majorant fails at 2/3; this is a method
  boundary. The separate t≥1 divergence is a genuine theorem boundary.
- **Formalization:** transport the checked determinant gap to finite real spacing
  and cardinality; then consider the analytic steps separately.
- **Signed source:** improve the ambient/error/trial budget or change the trial
  family. Refining this same two-moment inverse alone has a proved ceiling.
- **Proof authority:** a new source claim needs a separately checked implication
  with a source/form-core theorem; metadata cannot supply that missing proof.
- **Academic assessment:** obtain an external referee and complete priority
  comparison with primitive-lattice and multiplicative-correlation literature.

RH, integer abc, binary Goldbach, authentic signed S4 and the t=2/3 moment
endpoint remain OPEN. No release or paper publication occurred.
