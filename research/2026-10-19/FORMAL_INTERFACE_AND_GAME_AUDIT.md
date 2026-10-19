# Forge II: semantic adapters and game-certificate soundness

**Status: KERNEL-CHECKED, classical mechanisms, academic priority UNVERIFIED.**
Base PR179 commit `81684b4b8956f9f5da56c376ba7e4339277eb665`; local lane
`research/forge-ii-formal-2026-10-19`. The provenance gate verified all 72
inherited import entries before development; 13 inherited independent-checker
tests passed. No toolchain or historical source was modified.

## 1. Two interfaces, not two names for one semantics

The PR178 source was inspected at commit
`e42096ec0186228dd0f748767599e470f2ca2e1d`. Its exact single file
`formal/InstituteCausal.lean` is selectively copied, byte for byte, to
`formal_inputs/InstituteCausal.PR178.lean`. Its Git blob is
`360ba66fc1a271d2411fb7c7a0942e350b9fa8ad`, verified against the actual Git
commit object. The containing branch is a sibling input, not an ancestor theorem.
The PR179 dependency `formal/FutureSafeForgetting.lean` has Git blob
`b0b1a395de924f343777da728fb56fdb1a558c32`, also checked against its commit.
The replay script pins both Git blob hashes and SHA-256 digests.

| Contract | PR178 `InstituteCausal` | PR179 `FutureSafeForgetting` |
|---|---|---|
| Single step | `State → Action → Option (Label × State)` | `Action → State → Option (State × Cost)` |
| Current report | No separate field | `observe : State → Report` |
| Successful execution | label list and terminal state | cost list and terminal state, swapped product order |
| Failed execution | whole `run` becomes `none` | whole `execute` becomes `none` |
| Failed-prefix record | Not in `run` | retained by the separate `trace` type |
| Quotient representatives | surjectivity plus classical choice | supplied section, constructive |
| Source identity | separate path-preservation premise | can be retained in report; no automatic immutable-origin law |

`formal/ForgeQuotientAdapters.lean` imports both exact compiled modules through
the isolated checker. It defines a cost-label adapter by swapping the two
components of a successful step. It then proves:

1. Projection commutes with this adapter, retaining partiality and exact labels.
2. PR179 fiber safety is equivalent to **current-report agreement plus** PR178
   label congruence on the adapted transitions.
3. For every finite word and starting state, PR178 `run` equals the swapped
   result of PR179 `execute`.

These statements require no finiteness, no chosen representatives, and no
assumption that a cost is a real number; labels are arbitrary exact data.
They do not silently identify PR178 `run` with PR179's richer `trace`.

Two kernel-checked countermodels enforce the boundary:

* A transitionless Boolean state machine satisfies PR178 label congruence under
  constant forgetting, yet fails PR179 safety when its current report is its
  Boolean state. Absence of transition receipts cannot preserve an omitted
  initial report.
* Two initial states emit different first-step costs and both fail on the second
  request. PR178 returns `none` in both cases. PR179 `trace` retains the unequal
  cost receipts. Thus equal failed runs do not imply equal failed-prefix traces.

Occurrence tokens, proof-verifier outputs, epoch labels and source tags are
preserved only if placed in the retained data. The adapter does not manufacture
those fields. Preserving a displayed current source tag is also different from
proving that every actual edge preserves an immutable original source.

## 2. Source-realization certificate theorem

`formal/ForgeGameCertificates.lean` starts with an arbitrary state set and
request set. A request predicate declares which abstract transition the
environment may select at a private state; a response relation declares all
source-faithful successor choices available to the resolver.

A **positive certificate** gives a region `safe` and positional resolver
`resolve(s,r)` such that every requested `r` has that actual response and the
response stays in `safe`. The theorem `positive_policy_is_lawful` proves by
induction that every finite environment-request history under this resolver
is an actual lawful path and stays inside the region. The independent theorem
`lawful_path_preserves_origin` retains original source identity when every
response edge has the declared source-preservation law.

A **negative certificate** gives a region `losing`, a positional environment
request `challenge(s)`, and a natural-number rank. At every losing state:

\[
0<r(s),\qquad \mathrm{requested}(s,\mathrm{challenge}(s)),
\]

and **every** matching resolver response remains losing and strictly lowers
the rank. If a response history has length \(n\), induction proves
\(n<r(s_0)\). Consequently the environment forces a failure within
\(r(s_0)\) requests, without a fairness assumption. A separate well-founded
induction proves that positive and ranked-negative certificate regions cannot
overlap.

The local conditions are finite-verifiable for supplied finite tables, but the
proofs themselves do not assume the state carrier is finite. No correctness of
the fixed-point search, no rank bound by carrier cardinality, and no claim of
algorithmic completeness is smuggled into these theorem types.

## 3. Alternating command/outcome certificate theorem

The public-belief lane uses a second quantifier order. The environment selects
a request, the resolver selects a public command, then the environment selects
an allowed command outcome. `AlternatingGame` makes these three relations
separate:

\[
\forall\text{ requested }r\quad\exists\text{ enabled }c\quad
\forall\text{ outcomes }t.
\]

An alternating positive certificate selects a command with a **nonempty**
outcome set and requires every outcome to remain safe. A negative certificate
selects a requested transition and, for **each** enabled resolver command,
selects an actual outcome that remains losing and strictly lowers the rank.
The alternating rank theorem again bounds every response history by its initial
rank, and the two certificate types cannot overlap.

This distinction is load-bearing: one safe possible command outcome does not
establish safety against every possible outcome. The checker compiles a positive
all-outcomes control and rejects the mutated claim whose command permits both
Boolean successors but whose proposed safe set contains only one.

The separate belief compiler must justify its interpretation of private states,
public commands, observable outcomes and source identity. It must rule out
state-dependent response functions unavailable to the public resolver and must
retain all possible outcomes before conditioning on a signal. **That compiler
and its correctness theorem are not formalized here.** Once a correct compiled
game is supplied, these generic certificate theorems apply to its declared
relations. The finite-game implementation independently rejects empty enabled
outcome sets, matching the formal positive contract.

## 4. Actual kernel receipt and exact assumptions

The unchanged official Lean 4.14.0 release, compiler commit `410fab728470`,
compiled both historical dependencies and both new modules. The temporary
module directory avoids adding build products to the repository. This container
uses the already documented self-path shim; the compiler and kernel are not
modified. Normal hosts do not require the shim.

| Module | Declarations checked | Axiom audit |
|---|---:|---|
| inherited PR179 `FutureSafeForgetting` | 6 | exact previously recorded sets |
| pinned PR178 `InstituteCausal` | 8 | exact sets, including declared `Classical.choice` for representative choice |
| new `ForgeQuotientAdapters` | 7 | six use no axioms; failed-trace countermodel uses standard `propext`, `Quot.sound` |
| new `ForgeGameCertificates` | 8 | all eight use no axioms |

All 29 declarations were compiled with warnings treated as errors; every printed
axiom set matched exactly. The checker rejects undeclared imports, placeholders,
custom axioms, unsafe definitions and `native_decide`. The new adapter imports
only the two explicitly pinned modules; the game kernel has no imports.

`formal_inputs/KERNEL_RECEIPT.json` records the real compiler version, source
digests, all printed axiom sets, source text for calibration controls and their
actual outputs. One positive control was accepted. Four false controls were
rejected with exit 1 and the expected `decide` diagnostic: `False`, one-safe-
outcome mistaken for universal safety, nonstrict rank `1 < 1`, and erased
Boolean current-report equality. These controls calibrate the actual compiler,
not merely a source scanner or version string.

Reproduction on a host with pinned Lean:

```sh
python scripts/verify_forge_formal.py --lean lean --output /tmp/forge-formal.json
```

The `.lean` adapter is compiled through this script because the repository uses
standalone pinned sources, not a root Lake package. No Mathlib dependency or pin
was introduced. Directly running the adapter without building its two modules
will correctly report missing imports.

## 5. Claim boundary and next discriminator

**CLASSICAL / KERNEL-CHECKED:** typed product-order adapter, output-preserving
congruence criterion, successful-execution compatibility, source-path
preservation, positive strategy closure, ranked finite adversarial failure and
disjoint positive/negative certificate regions.

**REFUTED with checked countermodels:** identifying PR178 label congruence with
PR179 report safety without an output law; identifying collapsed failure with
the richer failure-prefix trace; replacing universal command-outcome safety by
existential safe-outcome availability.

**UNVERIFIED in this kernel:** fixed-point algorithm completeness, finite minimal
memory count, optimal probe cost, the public-belief compiler, infinite Euler
rigidity and all analytic/operator results. The formal work does not certify
the research framework as a whole or imply any Weil positivity statement.

The highest-value next formal lemma is a semantics theorem for the explicit
public-command belief compiler: each reachable belief must be exactly the set
of private states compatible with the source, command history and observed
signals. Only that theorem can connect an abstract winning game certificate to
an information-limited source resolver without hiding extra access.
