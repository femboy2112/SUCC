# NO-GHOST formal verification receipt

**Status: DISCLOSED within the explicit Lean hypotheses.** Twelve named
declarations in `formal/NoGhost.lean` were actually compiled and kernel-checked
using the repository's **Lean 4.14.0** lane on 2026-10-13. The compiler reported:

```text
Lean (version 4.14.0, x86_64-unknown-linux-gnu, commit 410fab728470, Release)
```

The worktree base was `9e7589e522aff990189aa8a14f6ee2fa5a28dd81`.
The independent complete output is `LEAN_CHECK.log` in this directory.
No file in the inherited `formal/swarm_topology` Lean 4.14/mathlib package was
modified, imported, or used to check these declarations. The independent EOS
PR #45 Lean 4.19 lane is a different branch/package and was not imported.

## Exact statements and boundaries

All names below have prefix `ObservationalSUCC.NoGhost.`.

| Declaration | Kernel-checked content | Axioms printed |
|---|---|---|
| `ConstraintCover.glue_restricts` | A compatible local family agrees on every context with the owner-selected global assignment. | None |
| `ConstraintCover.glue_unique` | Any assignment with these restrictions is that global assignment. | `Quot.sound` |
| `ConstraintCover.glue_preserves_complete_constraints` | A compatible family satisfying each context's constraints glues to an assignment satisfying every constraint, provided every constraint's full variable support occurs in a context. | None |
| `ConstraintCover.source_supported_constraint_gluing` | Over a **given admissible original source**, the matching family has a unique global source/assignment pair satisfying all restrictions and all declared constraints. | `Quot.sound` |
| `CompleteKernel.complete_kernel_implies_all_prior_laws` | Equality of complete source/current/output kernels preserves every finite unnormalized prior mixture, separately for each immutable source row. | None |
| `CompleteKernel.source_indexed_all_priors_iff_complete_kernel` | The converse follows by a one-atom Dirac prior; hence equality for every finite prior is equivalent to pointwise kernel equality. | None |
| `RigidTransport.path_preserves_invariant` | A finite path of authorized history comparisons preserves a common retained invariant if each edge does. | None |
| `RigidTransport.invariant_transport_path_independent` | When every target history embeds injectively in that common invariant, **any two** authorized comparison paths with the same endpoints induce the same map. | None |
| `RigidTransport.invariant_comparisons_are_inverse` | Invariant-preserving opposite comparisons are mutual inverses under the same injectivity hypothesis. | None |
| `Countermodels.bit_comparison_involutive` | The specified Boolean pair map is an involution. | None |
| `Countermodels.bit_comparisons_fail_braid` | Its two three-step braid words differ at `(false,true,false)`. | None |
| `Countermodels.omitted_joint_constraint_blocks_gluing` | Singleton reports `x=false,y=true` cannot have a global assignment satisfying the omitted law `x=y`. | None |

`Quot.sound` arises through Lean's function extensionality in equality of
assignments. No `Classical.choice`, `propext`, custom axiom, `sorryAx`, unsafe
declaration, or `native_decide` is used. The Boolean calculation uses `decide`,
whose result is checked by the kernel.

The gluing theorem is constructive given an explicit owner for every variable.
It actually holds beyond finite systems; finite complete covers are an intended
application. The source and its admissibility proof are inputs. Each constraint
comes with a support and an explicit proof that its truth depends only on that
support. The application must enumerate **every** law required by its source,
enabledness, transition, evidence, ancestry, and resource contract. The theorem
does not certify that a human-chosen constraint encoding captures physical
reality. Local records are total functions for convenience; their values outside
the context are ignored by the hypotheses and conclusion.

The kernel criterion uses an abstract coefficient object with only the laws
`1*x=x` and `x+0=x`. Nonnegative rational arithmetic is a valid mathematical
specialization. This file does not mechanize rational positivity or
normalization, construct the two-event product kernels from instruments, or
verify that a source's real preparation menu provides all Dirac preparations.
The reverse implication must be restricted when those preparations are absent.
The output atom must contain all event-labelled receipts and whatever full
carrier/future interface is claimed to be preserved; choosing a smaller output
type proves only a smaller equality.

The rigidity theorem proves coherence for arbitrary finite paths, so braid,
disjoint-square and loop coherence follow **when** its injective-invariant
hypothesis holds. It does not show that arbitrary source-induced diamonds
possess that invariant, nor that arbitrary pairwise bijections are coherent.
It also does not formalize the presentation of a poset's linear-extension graph
by squares and hexagons. The finite Boolean theorem is the abstract calibration;
the operational typed model is separately implemented and described in the
research manuscript.

## Reproduction and the isolated startup workaround

On a normal host with the pinned compiler on `PATH`:

```sh
scripts/verify_no_ghost_lean.sh
```

The exact invocation used here was:

```sh
NO_GHOST_LEAN=/tmp/succ-lean414/bin/lean \
NO_GHOST_SELF_PATH_COMPAT=1 \
scripts/verify_no_ghost_lean.sh
```

The available compiler initially failed before elaboration with
`error: failed to locate application`. The runtime allows reading the current
process's executable via `/proc/self/exe`, but rejects the equivalent numeric
`/proc/<own-pid>/exe` spelling used by Lean 4.14. This was reproduced independently
with Python's `os.readlink`. The optional, fully printed-in-source compatibility
adapter normalizes **only this process's executable path** to the permitted
spelling. It does not change the Lean executable, library, elaborator, kernel,
proof terms, or access to other processes. Ordinary hosts should omit it.

The script enforces the checked-in Lean 4.14.0 pin and runtime version, rejects
placeholders/custom axioms/unsafe code/native proof shortcuts, compiles an
`.olean` into a temporary directory, and compares all twelve actual `#print
axioms` outputs against the exact expected sets. It rejects missing or extra
axiom reports and unexpected compiler output. The `.olean` is deliberately
ephemeral; source and reproducible checks are the artifact.

An actual compiler negative control runs before the positive gate. The script
creates temporary source `theorem noGhostFalse : False := by decide`, invokes
the same compiler, and requires both exit status 1 and Lean's expected
diagnostic that `decide` proved the proposition false. This calibration actually
ran and passed; its normalized diagnostic is retained in `LEAN_CHECK.log`.
Startup errors, unrelated parse failures, a crash, or acceptance of the false
theorem would fail the control. The deliberately rejected source is deleted
with the temporary directory and is not packaged as an accepted proof.

SHA-256 of the checked files/binaries:

```text
formal/NoGhost.lean
9cca103f016e051e71aa98fe092cceec8cf7cdeb50c962ba737ce47c586c768a
scripts/verify_no_ghost_lean.sh
9455142c5792d436d595553249a9977b9f64caf921470cf08f4c5a7b6adbdb8a
/tmp/succ-lean414/bin/lean
eacf754d25ae86ea076882a34b9444f2485659d9df4266b821443b28ca95a215
/tmp/succ-lean414/lib/lean/libleanshared.so
c28977f1409a88f7d8ccf20beb24bbece5f573aeaabcdb5a6352a14f9f325bd9
```

## Relationship to prior SUCC formal work

The existing `EODCS_CarrierIndexed.lean` proves finite deterministic report and
endpoint transport under actual commuting source squares. This contribution
does not alter it. The new exact-kernel equivalence isolates the algebra used
by the finite stochastic two-event criterion; the gluing proof supplies a
mechanized complete-constraint baseline; the arbitrary-path rigidity theorem
states a sufficient carrier retention condition for coherence.

These are formalized elementary mathematical consequences of explicit
hypotheses, not academic-priority claims. The fixed-constraint gluing result
overlaps the F48 incidence-sheaf baseline and is not advertised as a new sheaf
theorem. The new file is not covered by the existing `EODCS_*.lean` or
`Swarm_*.lean` workflow globs; its independent verifier must be run explicitly
or added as a separate CI step by the integrator.

## Remaining paper mathematics

The following are **not** claimed Lean-verified by this receipt: full
stochastic causal-model adequacy; all linear extensions connected by lawful
adjacent swaps; presentation completeness by disjoint squares and braid
hexagons; source-supported Farkas alternatives; probabilistic repair
optimization; nonregular-cover descent; and infinite-source realization.
Their manuscript arguments, exact finite checks, or certificates must be
assessed independently. A Python enumeration is not a Lean proof.
