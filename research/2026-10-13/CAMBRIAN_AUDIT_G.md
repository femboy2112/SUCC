# CAMBRIAN audit G — fresh generalization and hostile source gates

**Verdict:** the audited D19/D20 learner/memory constructor, D22 finite-horizon
cost solver, F32 discrete hidden-memory law, and F34 incompressible low-mode
obstruction survived the fresh exact tests below at their stated scopes. No
incorrect target theorem or target computation was found in these probes.
The deliberately weakened source/oracle/initialization controls fail as predicted.
These controls defend the stated hypotheses; they do not refute the conditioned
theorems by violating their premises.

This auditor previously owned cluster C, which is deliberately **not audited
here**. This is one same-model-family worker using different derivations and
implementations, not an external independent or fully blinded referee.

## Freeze, domains, and pass/fail

Before reading the target sources or dossiers, the auditor wrote
`CAMBRIAN_AUDIT_G_PREREGISTRATION.json` with explicit pass/fail outcomes:

- D19/D20: compare generated predictive state with complete source-product
  behavior and independently counted reachable residual classes. Fail any
  finite-sample-to-all-word promotion or undeclared reset/teacher assumption.
- D22: compare cost against complete public strategy-tree execution on every
  original source, retaining destructive transitions and disabled actions.
- F32: compare eliminated memory against full rational source trajectories,
  including nonnormal, singular, nilpotent, and initialized hidden states.
- F34: compute exact tensor Fourier convolution, divergence, and Leray
  projection on fresh high integer frequencies. Fail a vanished residual,
  pressure artifact, or an unjustified uniform amplitude conclusion.

The actual target constructions were frozen before the new holdout generators
were executed. The coordinator supplied the final D commit before execution.
Target worktrees remained read-only throughout this audit.

| Target | Exact frozen commit | Audited module SHA256 |
|---|---|---|
| D computation | `810128e8fdd1f32a17852d828ee16e4b7ffb50f3` | `eb303fd34eadcc041af54aa9c330aa960e648acf4429357f8d3d8c177faa4a74` |
| F physics/logic | `21ef59994f11d488a31632f731f4e4d7d9adbc77` | `acc31e8357cea00387023341e6af883676699b9058c4b29d52e3eff88410e91a` |

The audit runner loads only the target implementations under test. It does not
call their validation routines, teacher implementation, partition/minimum-state
oracle, strategy-tree oracle, matrix arithmetic helpers, trigonometric checks,
or stored campaign results to generate a verdict.

## G1. D19/D20: variable source size, partial actions, inaccessible interiors

**New source generator:** seed `79192026`, 96 cases, one through ten original
states, one through three actions, and up to three ordinary output labels.
Every fifth case has randomly disabled source actions and uses the target's
explicitly observable enabledness/failure adapter; 20 such cases execute.
Every fourth ordinary case deliberately traps the prepared root in a proper
interior subset. Other transitions are independently sampled total maps.

The learner sees only membership responses and an independently implemented
exact counterexample oracle. That oracle uses **backward pair separation** on
the entire source/hypothesis product, rather than the target teacher's forward
reachable-product BFS. Initially mark source/model state pairs whose output
differs. Iteratively mark each unmarked pair with a literal prepended-action
witness whenever its successor is marked. Fixed-point exhaustion certifies
all-word equality of unmarked pairs in the finite declared model. Returned
counterexample words are actual action words, not oracle status labels.

The same separation relation, restricted to independently computed root
reachability, determines the minimum reachable residual count. This is compared
to the learner's number of states. Its full-source version is compared separately
to `construct_memory`, whose access contract includes every source state.

**Outcome: 96/96 PASS.** Every accepted predictor agrees under all finite words
in its supplied complete source model; every learned state count is minimal
for the prepared root. All complete-table memory constructors agree with the
independent full-source residual count. In **56 cases**, minimum prepared-root
memory differs from the complete source-class count, so the holdouts exercise
the reachable-versus-all-interiors quantifier rather than merely reproducing
the target's fully reachable generator.

This is a finite exact product certificate, not a statement that a bounded
word sample suffices on an unknown or unbounded source.

### Exact teacher mutation

A unary source reports 0 before depth 19, then 1 forever. A counterfeit teacher
tests only depths 0 through 7. The learner returns `EXACT_TEACHER_CERTIFIED`
for a one-state all-zero hypothesis, which fails at the actual word `a^19`.

The target explicitly assumes a correct terminating exact equivalence teacher;
the counterfeit violates that premise. The control shows why the returned
status cannot be independently authenticated merely by substituting random or
bounded tests for that teacher. No status promotion beyond the teacher contract
is warranted. An exact source-state product audit supplies the missing lamp
only because its finite source table is complete and trusted as a model input.

### Reset-access mutation

Consider a single carrier with states `0→1→2→2`, reports 0,1,2, and only the
advance action. After the first probe, allowed action words can reach states
1 or 2, never the prepared root 0. Empty-word membership at the original root
would report 0; the same readout at the current carrier reports 1. Oracle reset
membership therefore requires independent repreparation, another prepared
carrier, or additional source-law authority in this example. No reset path is
provided by the original intervention menu.

This tests the target's declared access boundary, not an alleged physical
execution by its learner. Stored historical receipts remain legitimate facts;
they do not magically restore the carrier for new counterfactual word queries.

## G2. D22: independent complete public strategy trees

**New generator:** seed `79222026`, 120 carriers, one through six states, one
through three actions, binary outcomes, rational positive action costs,
independently sampled destructive transition maps, state-dependent enabled
menus, and up to three original-target labels. Run horizons 0,1,2 on each:
**360 source/horizon cases**.

The oracle constructs complete public action/outcome trees syntactically before
examining the source. It retains impossible outcome branches rather than
pruning using a belief recursion. Then it executes every tree separately from
every original state, using the raw transition/output/enabled arrays. A tree
is valid precisely when every encountered action is legal and original-target
labels are constant on each terminal public transcript. Its cost is the
largest original-state path expenditure. The optimum is the smallest cost
among all valid trees. No Bellman recurrence, memoized belief update, target
oracle, or greedy pruning enters this calculation.

**Outcome: 360/360 PASS**, across **2,702 full public trees**. The independent
oracle finds 130 feasible and 230 losing source/horizon cases; the target's
finite-horizon worst-case cost matches exactly in every case. Disabledness is
checked on the evolving current carrier; labels remain attached to the original
state. No reset action is inserted by the oracle.

**Source completeness mutation:** with original states 0,1,2, a nondestructive
read reports `(0,0,1)` while target labels are `(0,1,1)`. The complete model has
no successful policy. Omit source state 1 and preserve the other two read/target
rows: a cost-one read suddenly appears sufficient. The target correctly returns
different answers for these two different declared models. A tested sample
cannot certify its own source completeness.

No unbounded-horizon optimality, expected-cost result, or approximation guarantee
is inferred. These exact tests cover the specified finite-horizon theorem and
its source/availability gates.

## G3. F32: cross-domain rational matrices and hidden initialization

**New generator:** seed `79032026`, **72 block-linear systems**, resolved
dimension 1–3, hidden dimension 1–6, and input dimension 1–2. Cases include:

- rational upper-triangular nonnormal hidden dynamics;
- singular upper-triangular matrices with a zero diagonal mode;
- nilpotent upper-shift delay chains;
- decoupled hidden modes with zero input/resolved excitation;
- zero boundary coupling as a positive closure control.

Initial hidden vectors are retained, including nonzero vectors; fresh rational
input sequences have length `h+5`. The independent simulator assembles the
single full matrix `[[A,B],[C,D]]` and input matrix `[[E],[H]]`, and advances the
joint source directly. It never constructs a memory kernel or imports the
target matrix helpers. Every target `memory_successor` is compared to the
resolved part of that complete source trajectory.

The zero-initial closure certificate is independently challenged with all
resolved basis initializations and all one-step basis input impulses, directly
simulated through `h+2` steps and compared to the candidate `Ax+Eu` recurrence.
The all-hidden-initial certificate is challenged with every hidden basis vector.
These tests distinguish a homogeneous input kernel from an initialization forcing
term without recomputing the target's `BD^kC/H` criterion.

**Outcome: 72/72 PASS**, every successor and both certificate flags. There are
26 positive zero-hidden-initial closures and 10 positive unrestricted-initial
closures in the new family; the remaining cases exhibit actual source effects.
All matrices, initial values, inputs, and complete independent resolved/hidden
trajectories are saved in the raw JSON.

**Hidden-initial mutant:** let `A=0`, `B=(1,0)`, `C=H=E=0`,
`D=[[0,1],[0,0]]`, `z0=(0,1)`. Every convolution coefficient vanishes,
yet the resolved sequence is exactly `0,0,1,0,0`. Dropping the initial forcing
term predicts the false all-zero sequence. The target retains it and distinguishes
zero-initial closure from unrestricted-initial closure correctly.

The audit covers discrete successors. It does not execute continuous-time
exponentials, establish passive circuit positivity for arbitrary matrices,
identify physical interiors, or independently mechanize Cayley–Hamilton.
The universal finite-dimensional paper theorem still relies on its stated
dimension bound and source law; these holdouts verify its implementation.

## G4. F34: high integer frequencies with pressure removed

Fresh frequencies are
`N=5,17,97,257,4099,65537,1000003,1000000007`.
The oracle stores the four real cosine Fourier coefficients at
`±(N,0),±(N,1)` and first verifies divergence-free source amplitudes.

It computes every retained low-mode tensor coefficient by the full convolution

\[
T_{ij}(q)=\sum_{p+r=q}\widehat w_i(p)\widehat w_j(r),
\]

then divergence `i q_j T_ij(q)`, then subtracts its exact longitudinal Leray
component. Coefficients are stored divided by `i`, with all arithmetic rational.
The sine amplitude follows from the actual pair of Fourier coefficients.
This calculation does not use the target's trigonometric cross-advection
formula or target projection helper.

**Outcome: 8/8 PASS:** at `q=(0,1)` the retained divergence-free advection sine
coefficient is `(-1/2,0)`, agreeing with the target. Viscosity and the zero field
have no projected low velocity to supply this source-dependent residual at the
initial instant. The exact instantaneous closure obstruction survives very high
integer wave numbers, without numerical precision concerns.

Three additional rationally scaled, sloped mode pairs remain divergence-free
and have nonzero pressure-projected low-mode coefficients:

| Modes `k`, `ell` | Projected sine coefficient |
|---|---|
| `(29,-3)`, `(29,-2)` | `(5/203,0)` |
| `(113,5)`, `(113,6)` | `(3/226,0)` |
| `(997,-41)`, `(997,-40)` | `(81/25922,0)` |

These source families are outside the target's displayed parameterization.
They test orientation, rational amplitude scaling, and pressure elimination.
They do not establish a broader PDE theorem by finite sampling.

### Energy/amplitude boundary

For the target's unnormalized family, mean squared velocity is
`(N^2+2)/2`, so the constant `-1/2` residual does not establish a uniform
bounded-energy nonzero limit. Normalize the second amplitude to `(1/N,-1)`:
mean squared velocity becomes `1+1/(2N^2)`, and the exact low-mode sine coefficient
becomes `(-1/(2N),0)`. It is nonzero for every tested finite N but tends to zero.

The target claims an instantaneous source-fiber counterexample for every finite
N, which this audit supports. It does not claim the stronger bounded-energy
uniform lower bound, and none is added here. No continuum compactness conclusion,
finite universal fluid-memory representation, 3D regularity, or existence result
is inferred.

## Reproduction and evidence boundary

Audit files are additive and confined to the audit G dossier, preregistration,
raw JSON, and runner. No target module, shared ledger, README, CI, architecture,
roadmap, or provenance archive was modified.

Actually executed twice, including exact saved-receipt replay:

```sh
python scripts/cambrian_audit_g_holdouts.py \
  --computation-root /workspace/scratch/6d134115e8ca/d_computation \
  --physics-root /workspace/scratch/6d134115e8ca/f_physics

python scripts/cambrian_audit_g_holdouts.py \
  --computation-root /workspace/scratch/6d134115e8ca/d_computation \
  --physics-root /workspace/scratch/6d134115e8ca/f_physics --check
```

Both exited zero. On a branch containing the frozen D and F modules, the replay
command is simply `python scripts/cambrian_audit_g_holdouts.py --check`.
The runner records exact target-module hashes so later source changes cannot
silently inherit this audit. Integrated full tests and GitHub CI remain separate
coordinator checks; no CI success is asserted by this auditor.

The earned verdict is **exact finite generalization evidence plus calibrated
hypothesis-removal countermodels**. Existing paper theorem quantifiers survive
only under their explicit source, access, initialization, and finite-dimension
contracts. No new academic-priority claim or physical source authentication is
attached to these passing results.
