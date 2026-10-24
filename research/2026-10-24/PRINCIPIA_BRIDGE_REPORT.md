# Principia connection: visible history and an operational ancestral criterion

## Outcome

The README, foundations, Carrier Atlas, and claim ledger now expose the
[Principia connection](../../docs/PRINCIPIA_CONNECTION.md). The historical note
cites Whitehead and Russell's primary text, credits Frege, and distinguishes
intellectual kinship from documented direct influence. It does not claim that
SUCC replaces mathematical foundations or reproduces Principia's type theory.

The useful mathematical addition is the [ancestral observer criterion](../../docs/CLAIM_SUPPLEMENT_PRINCIPIA_ANCESTRAL.md).
For an arbitrary source relation R and observation q, let Q be the existential
one-step observation relation. Then

\[
\forall x,b:\quad q(x)Q^*b\iff\exists z\;(xR^*z\land q(z)=b)
\]

holds exactly when saturating every R-forward-closed predicate along q's fibers
keeps it R-forward-closed. For one selected start x, it suffices and is necessary
to check closure of the saturation of Reach(x) alone. Equivalently in the
all-start case, the entire set of reachable reports must
be constant inside every observation fiber. No finiteness, surjectivity, or
axiom of choice is assumed in this theorem.

This is classical elementary mathematics assembled for SUCC, with independent
paper derivation and core Lean formalization. Scholarly novelty is unclaimed.

## Practical use and hostile controls

`audit_ancestral_observer(machine, labels, selected_start)` uses the existing
source-labelled `Machine`. It compares complete finite reachability before and
after observation. On failure it supplies a shortest spurious observed path,
actual source witnesses for its individual edges, and a hereditary source set
excluding its endpoint report. Consecutive edge witnesses are not falsely
presented as one executable source path.

The three-state model with only b→c and q(a)=q(b)=A, q(c)=B fails from a and
passes from b. Even the unpointed equality between the image of closure and
closure of the image holds in this example; that equality loses the chosen root.
Three source states are minimal for a spurious endpoint report.

The chain a→b→c with the same observation passes the endpoint test from every
start, yet the abstract A→B edge cannot lift in one step from a. The existing
future-safe observer audit correctly rejects its stronger trace contract.
The new endpoint tool therefore supplements that interface without weakening it.

Hostile review also supplied a forged certificate A→B→A with a valid escaping
boundary but a genuinely reachable final report. The independent finite verifier
now explicitly excludes that final report from the invariant's observed image,
and the forged certificate is a regression test.

## Proof and validation authority

- [Core Lean source](../../formal/PrincipiaAncestral.lean): nine declarations,
  including hereditary reachability, forward projection, the selected-root and all-start saturation
  equivalence, the fiber-support equivalence, and invariant refutation.
- [Kernel receipt](principia_receipts/kernel.json): actual theorem types and
  **empty axiom dependency lists** under Lean 4.14.0. Two paired controls reject
  removing hereditary closure and claiming the false three-state endpoint lift.
  No mathlib build, imported domain theorem, `sorry`, or new axiom is used.
- [Focused tests](principia_receipts/focused-tests.log): nine tests, including
  all 2,594 finite relation/partition models with one to three states. Independent
  Boolean-matrix closure and exhaustive hereditary subsets agree with BFS.
  These computations verify the finite implementation, not the infinite theorem.
- [Exact probe](principia_receipts/exact-model.json): deterministic replay on the
  actual existing `Machine` type, retaining source-file hashes and stronger trace
  controls. Run `python scripts/principia_ancestral_probe.py` to reproduce it.
- Required full-suite validation is reported separately in the delivery PR,
  with exact command statuses and local logs retained alongside the workspace.
  The local full suite was discovered before the final test-only hostile
  cases and selected-root assertion were added; the final nine-test focused run includes them. No
  production-module change occurred during that suite. Hosted validation runs
  the complete final test set.
- [Documentation link check](principia_receipts/docs-links.json): 398 local file
  destinations resolve. Historical page anchors were checked against the primary
  text separately.

The focused GitHub workflow checks both Python 3.10 and 3.13, replays the exact
probe, freshly compiles the core Lean source, and uploads its theorem exports.
Hosted results must be read at the delivered commit; local logs are not hosted CI.

## Source and repository boundary

This work starts independently from live main
`b116841f12b41aaf7600da39bbb40577f25b6295`, on
`research/principia-ancestral-bridge-2026-10-24`. The preexisting π draft #259 was
rechecked at `a777aa99f541df2a0e2a0b8d57fef3f0940e465c` and is not a dependency or
merge parent. Original worktrees and all archived imports are preserved.

The [base CI receipt](principia_receipts/base-ci.json) distinguishes the successful
main validation run from subsequent cancelled runs on that same commit. A cancelled
run is not reported as a pass. The GitHub connector exposes PR-triggered runs only,
so main's push-triggered history was read through the GitHub API using `gh`.

Independent derivation, implementation, and hostile-review workstreams shared the
same research context and model family; they are not independent scholarly referees.

## Remaining mathematical boundary

The result concerns existential finite-path endpoints. It supplies no elapsed-time,
cost, probability, visit-frequency, or universal liveness theorem. A finite table
does not authenticate its source or certify an unmodelled infinite system.

For the π program, the practical gain is a precise selected-source transport test
and a counterexample to substituting an unpointed commuting diagram. No new signed
BBP cancellation is proved here. π normality and RH remain open. A next application
must specify a concrete source observer and either exhibit its hereditary
obstruction or prove the required selected-root transport; a frequency claim
additionally needs its own quantitative theorem.
