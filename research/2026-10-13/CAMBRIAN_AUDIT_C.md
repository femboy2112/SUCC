# Auditor C: Lean kernel and proof-authority boundary

**Audited base:** 6fc5ae9f1a92abbab259b37440aefed23ee04e92.
**New cluster-C source:** 906de6f, formal/EODCS_CambrianRealization.lean.
**Verdict: ACCEPT the stated finite-branching kernel claims, with the paper,
topology, effectivity and source boundary retained.**

This worker did not audit its own cluster-F results. It independently read
all nine EODCS Lean modules, theorem assumptions/proofs, the compact-history
dossier, pinned workflow, and separate PR45 source. It compiled nine modules,
printed axioms for **all 65 production theorems**, and wrote independently
executed positive/countermodel controls. This is another same-model worker,
not an external mathematician or independent model family.

## Audit contract and calibration

Target: dependent source types S:Nat→Type, arbitrary time-dependent relations,
complete finite successor supersets, a supplied finite initial candidate list,
and arbitrarily deep lawful prefixes entail one compatible infinite
mathematical history. Rival: drop finite branching, swap ∀d∃s with ∃history∀t,
or treat the result as a branch-selection algorithm or topology proof.

Acceptance required an actual Lean 4.14 compiler, all nine modules accepted,
every theorem's axiom dependencies checked, no comment-stripped admitted term,
custom axiom, unsafe declaration or native-decide shortcut, false/broken
implications rejected, and valid countermodel negations themselves accepted.
Every condition passed. Raw commands, return codes, stdout/stderr, source
hashes, calibration inputs and runtime metadata are in CAMBRIAN_AUDIT_C_RAW.json.
Acceptance does not authenticate the physical source.

## What the new module actually proves

| Theorem | Exact hypotheses and authority |
|---|---|
| cambrian_can_follow_truncate | Arbitrary lawful depth-d relational prefix yields every shorter prefix. Dependent source types; no finiteness. |
| cambrian_finite_coherent_choice | Finite menu, downward closure and a menu witness at every depth give one witness surviving every depth. |
| cambrian_extendable_successor | Complete finite successor superset and extendability give an actual successor extendable at every depth. |
| cambrian_nondeterministic_history_realization | Fixed extendable start and complete finite successor supersets give an infinite dependent history starting there. |
| cambrian_finite_prefixes_realize_one_history | Different finite-depth initial witnesses can be fused when they all belong to one supplied finite initial list. |
| cambrian_countdown_depth_iff | Natural countdown supports depth d from s iff d≤s, universally in depth/time. |
| cambrian_countdown_all_finite_depths | Every finite depth is supported by some natural initial state. |
| cambrian_countdown_no_infinite_history | No single natural countdown history is lawful at every time. |

Completeness has direction R t s next → next∈menu t s. It does not require
every listed value to be an actual successor. The proof separately retains
the R witness, so extra menu values do not become invented source transitions.
The initial list defines allowed start candidates; it does not prove this
list covers every physically possible preparation.

The state type may be infinite and change with time. No uniform finite-state,
deterministic, stationary, total or invertible transition assumption appears.
The dependent history has type (t:Nat)→S t. The proof recursively chooses an
already proved infinitely extendable successor using Classical.choose.
No decidable recognition of extendability, effective selector, termination,
complexity bound or physical sensor construction is supplied.

The positive final theorem prints standard axioms only:

~~~text
propext, Classical.choice, Quot.sound
~~~

The original countdown nonexistence theorem prints:

~~~text
propext, Quot.sound
~~~

No sorryAx or custom domain axiom appears in any production theorem.
The receipt records every actual dependency, including classical choice
in some audit controls; informal constructive appearance is not substituted
for a dependency check.

## Independent kernel controls

CAMBRIAN_AUDIT_C_CONTROLS.lean is an audit appendix. The runner prepends the
byte-identical target source in a temporary compilation unit; no production
file is changed and no cached local target olean is required.

**Changing infinite source types, nondeterminism, time variation and a true
successor superset.** Set S t = Nat×Fin(t+1). Legal successor phases are zero;
their natural coordinates are s.1+t+1 or s.1+t+2. The menu additionally lists
s.1, provably not a lawful successor. This source is infinite at every time,
its phase type changes, and there are two distinct lawful choices with a
time-dependent update. Kernel controls establish completeness, the extra
menu member, actual nondeterminism, all finite depths and an infinite history.

**Remove finite branching while retaining a fixed start.** Define
R(t,x,y):=t=0∨x=y+1 on natural states. From fixed root zero, the first edge
chooses any finite countdown budget. Every finite depth exists, yet no
infinite branch does. Kernel controls prove both universal statements and
prove that no finite root menu can be complete. This directly isolates
finite branching, rather than merely varying an unbounded initial state.

**Remove downward closure while retaining a finite menu.** On [true,false],
P(0,x) means x=true, and P(d+1,x) means x=false. Every depth has a menu witness,
yet no witness survives every depth. Lack of downward closure and lack of a
uniform witness are kernel checked.

| Invalid proof/implication | Compiler verdict | Why it fails |
|---|---|---|
| 0=1 by rfl | Rejected, exit 1 | Numeral constructors are not definitionally equal. |
| Infinite-root history via an empty successor menu without completeness | Rejected, exit 1 | A lawful relation does not establish empty-menu membership. Separate accepted control proves no finite complete root menu exists. |
| Treat countdown's ∀d∃s proof as an infinite-history proof | Rejected, exit 1 | The proposition types differ. Accepted countdown nonexistence supplies the actual obstruction. |
| Treat P(d,x) as P(e,x) from e≤d alone | Rejected, exit 1 | Missing downward closure leaves different depth-indexed types. Accepted alternating control refutes the stronger implication. |

Rejected inputs are recorded as rejected; they are not verified theorem
claims. All accepted audit appendix theorem dependencies are also printed.

## Inherited eight-module authority

All **57 inherited theorems** were read, compiled and subjected to print-axioms.

| Module | Count | Exact scope retained |
|---|---:|---|
| EODCS_ActionClosure | 3 | Total deterministic actions preserve output-respecting relations along all finite words. No new sensor existence. |
| EODCS_CausalDescent | 9 | Fiber descent, surjective quotient uniqueness, pair factorization, actual-square composition and algebraic holonomy/deck identities. No minimal covering-degree construction. |
| EODCS_NerodePlateau | 4 | A globally hypothesized complete plateau for one stationary deterministic update gives all-future agreement. No finite cardinal plateau bound or general multi-action algorithm. |
| EODCS_OrderAdjunction | 5 | Relation-relative monotonicity/adjunction and sufficient quotient factorization with explicit source fibers, surjectivity and order lifting. Bare surjective monotonicity does not replace order lifting. |
| EODCS_RelationalChoice | 10 | Full successor-support fiber invariance, under surjectivity, gives set-valued descent. May/common possibility are not probabilities or must-occur outcomes. |
| EODCS_VoyagerMemoryDebt | 4 | State repetition propagates later outputs; a zero gap/pulse gives an injective Fin p source family. Cardinal inequality and bit cost require separate pigeonhole/encoding steps. |
| EODCS_VoyagerPhantom | 15 | Eventually-zero stream sources match every finite probe family while excluding the all-true completion. Adaptive-policy conclusions need additional deterministic nonanticipatory semantics. |
| EODCS_VoyagerTrace | 7 | Finite-word trace identities/naturality under actual action/readout squares; finite-source realization/refutation under complete enumeration. Probe count is not physical cost or a computability bound. |

All 65 production theorem rows use only subsets of propext, Classical.choice
and Quot.sound. No source mutation, declaration shadowing or unexpected
external domain import was used.

## Paper compactness and kernel scope

The paper theorem uses compact Hausdorff spaces, compact products, closed
relation/receipt constraints, finite joint realizability and choice. The
finite-intersection derivation is correct under those premises. Membership
in the declared original history class additionally requires that class to
be exactly those constraints, or included as a closed constraint.

The Lean module imports Std.Tactic, without a topology library. It proves
the finite-branching Kőnig specialization. Compactness, Tychonoff, closed
graphs, Hausdorff topology and physical-original identification are not
kernel checked. The dossier keeps these scopes separate and explicitly
includes noncompact/nonclosed/source-class countermodels. The topological
claim remains PROVED PAPER, rather than topology-kernel verified.

## Runtime and separate PR45

Actual version output:

~~~text
Lean (version 4.14.0, x86_64-unknown-linux-gnu, commit 410fab728470, Release)
~~~

The local locator source was inspected. It redirects only the current
process's numeric /proc/pid/exe readlink to /proc/self/exe; all other requests
delegate to the original function. It changes executable location discovery,
not proof/kernel routines. The raw receipt contains **the exact complete
locator source text and its hash**, as well as compiler-wrapper, shared-Lean
library and locator-binary hashes. An ordinary isolated CI build without
this host workaround remains a distinct check.

PR45 commit b2774ca485db4b5b4f7ce92e535220352fb3af2f has a separate
formal/obstruction_synthesis/lean-toolchain pinned to Lean 4.19.0. Its source
corresponds to inherited finite-word stability, descent, paired reports and
source-relative pruning. DiscoveredInstance instead checks a generated
Fin 27→Fin 9 table. Neither supplies the dependent history theorem.
No PR45 file was imported, rebuilt or claimed compatible with 4.14.
These are source correspondences, not an independent-discovery or
cross-version equivalence certificate.

## Reproduction and next boundary

~~~sh
python scripts/cambrian_audit_c_lean.py \
  --output research/2026-10-13/CAMBRIAN_AUDIT_C_RAW.json
python scripts/cambrian_audit_c_lean.py \
  --compare research/2026-10-13/CAMBRIAN_AUDIT_C_RAW.json \
  --output /tmp/cambrian-audit-c-replay.json
~~~

Explicit compiler/locator paths are accepted. Comparison reruns every
compiler/control and checks stable source/runtime hashes, version, verdicts
and dependency rows; temporary diagnostic paths are not byte-invariant.
No production source, shared ledger, CI or archive was edited.
These are local checks, not a remote CI assertion.

The next substantive obligations are a separately pinned topology-library
proof and an independently stated effective branch-selection theorem.
Neither follows merely from classical finite-branching existence.
