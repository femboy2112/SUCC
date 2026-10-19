# Formal and independent certificate audit

Baseline: `f309d9104ba480c1999c962af1df7c50f19e1bfe`, branch
`research/academic-transmutation-2026-10-18`. This is an additive audit; preserved
imports and historical formal sources were not modified. The 72-item provenance
gate passed: 17 byte-identical archives and 55 mechanical namespace migrations,
originating at `ba075348b7bcc66d938b3e0ca96c26e95bba340a` in the import manifest.

## Verdict and exact coverage

**PROVED LOCAL / actual Lean kernel acceptance.**
`formal/FutureSafeForgetting.lean` proves exact descent and every-representative
path lifting for partial deterministic systems with costs. The six declarations
below were compiled successfully with warnings as errors on the repository's
standalone Lean **4.14.0**, compiler commit `410fab728470`.

This is a classical quotient/congruence construction specialized to the explicit
SUCC interface. Mathematical priority and a strict extension of published
coalgebra/automata theory are **UNVERIFIED**. The useful contribution is a checked
contract with partial-action, cost, report and path-lifting obligations, not a
claim to have invented quotient descent.

| Declaration in `ObservationalSUCC.FutureSafeForgetting` | Exact axiom dependencies |
|---|---|
| `fiber_safe_iff_descent` | none |
| `descended_structure_unique` | none |
| `finite_trace_preserved` | `propext` |
| `availability_reflected` | `propext` |
| `quotient_step_lifts_from_each_representative` | none |
| `quotient_path_lifts_from_each_representative` | `propext` |

`propext` is Lean's standard propositional extensionality; there are no custom
domain axioms, placeholders, `native_decide`, or domain-library imports. The
reported sets come from actual `#print axioms` output, not source inspection alone.

The formal source SHA-256 at this validation is
`986609101f0efafdf56453edc6da4919971ad00f34d4d76b417ecb234cd087f6`.

## Mathematical statement and noncircularity

Let a system consist of arbitrary types `State`, `Action`, `Report`, `Cost`, with
an observation map and a partial deterministic transition

\[
o:S\to O,\qquad d:A\times S\to\operatorname{Option}(S\times C).
\]

Let `forget : S → Q` have a supplied section `r : Q → S` satisfying
`forget (r q) = q`. Write `mapStep forget` for the map that preserves `none` and
sends `some (s,c)` to `some (forget s,c)`. Then the following are equivalent:

1. Whenever `forget s = forget t`, the reports agree and, for **every** action,
   the mapped partial transitions agree.
2. A quotient system on `Q` exists with exactly commuting observation and
   partial-transition maps.

The forward proof constructs the quotient using the section. The backward proof
uses the commuting maps to establish the local fiber laws. Thus existence of the
quotient is a conclusion, not a target hidden in a hypothesis. Its reports and
transitions are unique pointwise. No classical choice is needed because the
representative section is supplied explicitly.

Induction on an arbitrary finite word then proves equality of its entire
structural trace, including intermediate reports and exact costs. A second
induction proves: **every executable quotient path lifts from every source
representative of its initial state**, with matching final quotient state and
the same complete cost list. This is stronger than lifting a step from some
convenient representative.

The state can encode source identity, complete history, and residual budget, and
the report can bundle source tags and declared proof-task results. Adequacy of
that encoding, truth of task results, and source authentication are not theorems
of this file. The `Cost` type is an exact label; ordered budget arithmetic is not
formalized here. Nonstationary/history-dependent phenomena must first be modeled
with sufficient state. Nondeterministic and probabilistic transitions require a
different contract.

**Critical distinction:** merely retaining enough information to recover all
future observable behavior does not guarantee that a chosen finer representation
updates autonomously. Its own kernel must be a transition congruence. The formal
theorem requires precisely that stronger local condition.

**Availability boundary:** `none` and the trace constructor `blocked` record
mathematical lawfulness. They do not assert that trying an unavailable action is
physically permitted or observable. A rejection/menu instrument is a separate
assumption. The checker labels an availability-only separator
`STRUCTURAL_LAWFULNESS`.

## Independent finite certificate checker

`scripts/check_academic_certificate.py` uses only the Python standard library.
It imports neither `future_safe_quotient.py` nor any generator, partition-refiner,
or witness-search implementation. It consumes the public JSON table containing
states, actions, exact rational edges, blocks and distinguishing words.

It verifies two independent obligations:

1. **Soundness:** every block has equal source/report/task outputs, equal enabled
   action domains, exact equal costs, and successors in the same quotient block.
   These finite squares instantiate the local descent law above.
2. **Maximal merging:** one replayed separating word exists for every distinct
   pair of block representatives. Replay cannot cross a jointly unavailable
   action and must end at the first difference along the supplied word. A word
   need not be globally shortest to prove separation.

Local squares imply all-word preservation by induction. Pairwise separators
exclude any further merging while preserving the **declared** structural trace
contract. Exact fractions are reconstructed independently; floating costs,
booleans-as-integers, zero denominators, hidden nondeterminism, incomplete
partitions, forged separators and unused witness suffixes are rejected.

The public schema permits empty observation/task-result strings, requires
nonempty source/state/action/task identifiers, and requires the same ordered task
schema at every state. A dedicated round-trip regression checks this interface.
The checker authenticates the finite table, not its claimed relationship to a
physical experiment or to an analytic signed Weil form.

**Observed validation:** 13 standalone checker tests passed. The independent
checker also accepted all 2,744 three-state unary models with binary outputs,
optional edges and costs in `{0,1}` generated by an external harness; that corpus
used empty output/task-result strings as a schema control. A separate fresh
holdout of 128 five-state, three-action tables with rational costs and source/task
labels passed, with deterministic seed `718320261018`. The generator is called
only by the external test harness, never by the checker. These finite checks do
not turn the Python implementation into a kernel-verified program.

## Calibrations and toolchain receipt

No Lean executable was initially available in PATH or the bounded workspace/root
toolchain search. The official release was downloaded from
<https://github.com/leanprover/lean4/releases/download/v4.14.0/lean-4.14.0-linux.tar.zst>.
The locally recorded archive SHA-256 is
`320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a`;
this is a download-integrity receipt, not an independently authenticated release
checksum. A truncated initial transfer was resumed; final extraction completed
successfully. No repository pin was changed.

This container required the existing compatibility adapter documented in
`scripts/verify_no_ghost_lean.sh`: it normalizes only the current process's
`/proc/<own-pid>/exe` path to `/proc/self/exe`. It does not alter the compiler or
kernel. The exact compiler reported:

```text
Lean (version 4.14.0, x86_64-unknown-linux-gnu, commit 410fab728470, Release)
```

The new source compiled with exit 0 using `-DwarningAsError=true`. Three separate
false-theorem controls exited 1 with the diagnostic that `decide` proved the
proposition false:

```lean
theorem false_claim : False := by decide
theorem phantom : (none : Option (Bool × Nat)) = some (false, 0) := by decide
theorem cost_erasure : (some (true, 1) : Option (Bool × Nat)) = some (true, 2) := by decide
```

The inherited `scripts/verify_no_ghost_lean.sh` also ran successfully: its false
proof was rejected, all 12 declared theorems were kernel checked, and its exact
axiom manifest matched. This is fresh baseline evidence for that kernel, not a
claim that every historical formal artifact was recompiled.

Reproduce on a host with the pinned compiler:

```sh
lean --version
lean -DwarningAsError=true formal/FutureSafeForgetting.lean
bash scripts/verify_no_ghost_lean.sh
python -m unittest tests.test_academic_certificate_checker -v
python scripts/check_academic_certificate.py PATH_TO_EXPORTED_CERTIFICATE.json
```

## Historical coverage audit and remaining debt

The inspected `EODCS_ActionClosure`, `EODCS_NerodePlateau`, `NoGhost`,
`InfiniteGammaGeometric`, `GaussianTwoSuccessor`, and obstruction-synthesis
headers scope their results explicitly. The Gamma kernel formalizes denominator
arithmetic and a finite recursive prefix; it does **not** formalize Carleman,
essential spectrum, or infinite signed positivity. The Gaussian kernel proves
integer identities, not a Fourier/Weil identification. No contrary status
promotion is justified by this audit.

There are intentionally separate pins: root and `formal/swarm_topology` use Lean
4.14.0, while `formal/obstruction_synthesis` uses 4.19.0. The existing Mathlib
project remains unchanged and was not rebuilt in this lane. The new theorem
uses the standalone root project because no analytic/topological imports are
needed; this does not count as new Mathlib formalization.

`source_proof_certificate.py` correctly describes its authority records as
structure/hash auditing, not theorem proving. Merely supplying `LEAN_RECEIPT`
and `AXIOM_MANIFEST` files to that schema cannot establish their truth. Fresh
kernel execution remains a distinct obligation and has been performed for the
six declarations here.

**Next falsification opportunity:** preserve the independent JSON boundary in
CI, mutate each local descent square and each separator, and require these six
exact axiom sets. A semantic extension to nondeterministic or probabilistic
sources must supply an appropriate relation/coupling lift before inheriting
the every-representative path theorem. No signed analytic positivity or RH
conclusion is licensed by these finite/system-theoretic results.
