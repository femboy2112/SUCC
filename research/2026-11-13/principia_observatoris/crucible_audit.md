# Principia Observatoris: adversarial mathematical and implementation audit

**Scope.** This is a separately assigned same-model audit within the founding
round. It uses direct proof inspection, exact finite enumeration and an
independently written matrix oracle. It is not external peer review, a second
model family, a proof-assistant check, or a physical experiment. Agreement
between agents does not supply independent source authentication.

The reviewed parent is PR #618 at
`ab31057590a59b2bfbd5dbcd7126b2aefc7a2b55`. The manuscripts and native module
reviewed here are additions on top of that parent. The final receipt/manifest
identifies the exact delivered bytes; this document does not claim a separately
pinned historical implementation version.

## 1. Pass/fail criteria fixed before the checks

The main mathematical proposals fail if any of the following is found:

- a nonzero switched-linear response first appears beyond the claimed bound,
  despite the supplied exact dimension/rank promise;
- breadth-first span pruning loses a shortest separating word;
- the proposed predictive refinement fails action closure or adds more linear
  coordinates than the independently enumerated observable span;
- a predictor beats the stated hidden-fiber minimax error;
- the defect sum uses a wrong multiplication order or omits cancellation;
- a quotient certified as an action congruence invents a word response;
- an individually invariant commutative instrument family gives a different
  coarse-state or transcript law from its derived classical kernel.

A positive result is restricted to the precise model class of the written
proof. Passing finite enumeration alone cannot establish the universal claim.

## 2. Proof audit

| Claim | Independent check and verdict | Necessary boundary |
|---|---|---|
| PO-H2/H3 finite discrimination | **SURVIVES.** The reachable span begins at rank `b`; every nonstable stage strictly increases rank. Stabilization by `r−b` follows, and the direct-sum comparison gives `n+m−1`. | Exact authenticated linear realization, common action/preparation/readout types. Not inferred from a finite Hankel block. |
| Shortest-word implementation | **SURVIVES.** Queue depths are nondecreasing. At each depth, retained vectors span all reachable vectors generated through that depth. A discarded dependent vector cannot have a first nonzero readout unless an already retained vector of no greater depth does. The same argument applies to its successors. | The native routine uses exact rational rank and retains preparation/word provenance. |
| PO-Q1/Q2/Q3 source and joint-law quotients | **SURVIVES after a nonempty-source-label repair.** Deterministic fiber constancy lifts each word from every representative. Stochastic outcome/current-state joint rows must be constant on fibers; point-mass priors establish necessity. | Source-label set must be nonempty for the converse. Marginal or support matching is weaker than joint-law matching. |
| PO-K1–K5 knowledge interfaces | **SURVIVES.** Factorization, terminal leaf constancy, common-support obstruction, retained-record monotonicity and joint-image intersection all use the declared source class and access contract. | Semantic sufficiency is not executable acquisition; two correlated reports are not two independent constraints. |
| CG-02 action descent | **SURVIVES.** `PA` factors through surjective `P` exactly when it vanishes on `ker P`; representing a fiber by a different source state is harmless precisely under that condition. | Present target descent alone is weaker than dynamics descent. |
| CG-03 minimax prediction | **SURVIVES.** For every hidden unit vector `z`, the same datum comes from `z` and `−z`; the triangle inequality lower-bounds one of the errors by `||Fz||`. The orthogonal section attains the bound. This also proves the claim against arbitrary nonlinear predictors. | Hilbert source norm, the stated symmetric ball prior, and a linear target. A generic right inverse need not be norm-optimal. |
| CG-04 predictive completion | **SURVIVES.** Closure of the row space under all right action multiplications gives the least invariant row space containing the initial readouts. Every other closed refinement contains every `PA_w`. | Added mathematical coordinates may be inaccessible on one disturbed carrier. |
| CG-05 defect transport | **SURVIVES.** Expansion of each `E_i=P_iA_i−B_iP_{i−1}` cancels adjacent terms with the stated product ordering. | Small stage defects can amplify; nonzero stage defects can cancel. No curvature interpretation follows. |
| CG-07/08/09 geometry | **SURVIVES in stated scope.** Whole connected fibers justify the differential test; pulled-back bounded metrics give a pseudometric; nonnegative matrix walks yield the latency/graph bridge. | A baseline derivative does not determine a finite contrast. Signed path cancellation destroys transitivity of earliest endpoint response. |
| PO-C1 instrument quotient | **SURVIVES.** Individual outcome dual maps preserve the commutative algebra exactly when every unnormalized coarse branch factors through its probability vector. This iterates under arbitrary common finite feedback policies. | Summed-channel closure and immediate effect closure are each weaker. No hidden ontology or spatial metric is recovered. |
| PO-C2/C3 robustness and nondisturbance | **SURVIVES.** Unnormalized branch masses avoid division by rare-outcome probabilities; the classical joint outcome/state kernel contracts `l1`, giving the additive horizon bound. | Error bound must be uniform over all states actually reachable under policies; the inserted measurement outcome is ignored in the nondisturbance comparison. |
| PA-01–04 arithmetic stress test | **SURVIVES.** Positive moment density gives every BBP Hankel block full rank. The invertible leading block fixes the rival recurrence; its next residual is the positive Schur complement. An inverse-norm kernel-vector bound supplies a conservative rational separation margin. | Fixed finite-dimensional stationary rivals and consecutive exact moments. Neither rank nor the discriminator gives the missing signed orbit estimate. |
| PO-H8/H9 horizons and completion | **SURVIVES.** The halting reduction uses total finite-step simulators; continuity plus supplied moduli gives the displayed source-faithful bound. | Description length alone gives no computable universal horizon. Continuity does not certify finite equality, nor uniformity for moving probes. |

This audit does not certify bibliographic priority or the empirical adequacy of
any source map. Those remain separate obligations.

## 3. Exact finite crucible

Reproduce from repository root:

```sh
python research/2026-11-13/principia_observatoris/independent_audit.py
```

The independent oracle uses integer/Fraction arithmetic and a fraction-free
rank computation. It does not reuse the native row-reduction implementation.
A separately counted differential section imports the native module and
compares its returned certificates against brute-force words and direct
matrix calculations.

| Check family | Completed finite coverage |
|---|---:|
| Independent two-action 2×2 matrices with entries in `{−1,0,1}` | 6,561 ordered matrix pairs |
| Readout cases for that family | 19,683; 729 all-zero-prefix closure cases |
| Sharp delayed nilpotent response | Dimensions 2 through 8, first response exactly `d−1` |
| One-row observation/action pairs | 1,944 |
| Exact candidate-predictor norm comparisons | 9,720 |
| Ordered defect expansion | 250 cases; word lengths 1 through 6 |
| Complete deterministic three-state/two-action tables | 729; exactly 225 preserve the chosen two-class quotient |
| Rational quantum states and branch paths | 13 initial states, 10,140 subnormalized branch comparisons through depth 4 |
| Native separator against all ternary 3×3 single-action matrices | 19,683 matrices |
| Native switched, multi-preparation separator cases | 400 |
| Native minimal predictive completion cases | 400 |
| Two-realization direct-sum comparisons | 150 |
| BBP finite Hankel LDL checked against the independent rational-polynomial formula | 30 blocks, starts 1–5 and sizes 1–6 |
| Native malformed input controls | 9 rejected contracts |

These counts overlap in their mathematical content. They are coverage counts,
not votes or estimated probabilities of correctness. The universal statements
are supported by the written proofs, not by adding these counts.

## 4. Retained hostile receipts

1. **A nonorthogonal section is not optimal.** For `P=(1,0)` and
   `A=[[0,1],[0,0]]`, the orthogonal section gives squared residual norm `1`.
   The right inverse `(1,1)^T` gives predictor `B=1` and squared residual norm
   `2`. The condition `PS=I` alone does not prove minimax optimality.
2. **Relational projection invents a path.** With edges `0→1`, `2→3` and
   `q(0)=0`, `q(1)=q(2)=1`, `q(3)=2`, the projected graph has a two-edge
   `0→1→2` path with no such source path. This supplements, and does not
   replace, the older minimal selected-start PAP-04 counterexample.
3. **Averaged closure loses instrument outcomes.** X-projective measurement
   on a qubit maps diagonal observables to diagonal observables after summing
   its branches. Individual branches do not preserve the diagonal algebra.
   The states `|+><+|` and `|−><−|` have the same diagonal and opposite certain
   X outcomes. The retained quantum oracle detects this exact failure.
4. **The finite horizon is sharp.** A nilpotent shift of dimension `d` has
   zero responses through length `d−2` and nonzero response at `d−1`.
   Shortening the horizon by one fails even for integer data.

## 5. Defect found and repaired during the audit

The initial native `bbp_hankel_ldl` accepted `start=True`: adding integer
indices converted the Boolean to the integer `1` before the underlying
forcing validator saw it. This contradicted the module's strict integer
contract. The root agent added entry validation, and the independent malformed
control now explicitly rejects this case. No theorem or source value depended
on that malformed-input acceptance.

PO-Q3 initially allowed an empty original-source-label set `S`. Then every joint
table is empty and update commutation is vacuous, so the stated converse need
not hold. The author added `S≠∅`, which is exactly the condition used by the
point-mass necessity argument. PO-D2 was also clarified: a one-state controller
cannot remember nonconstant outcomes through a state-only report map or both
act and stop autonomously without a stage distinction. A single externally
scheduled instrument can instead expose its immediate output port without
persistent memory.

Book II initially contained damaged inline LaTeX escapes. Its author repaired
the formatting; the mathematical statements were unchanged. These are retained
repair records, not suppressed initial failures.

## 6. Remaining audit debt

No general physical classicality criterion is established. Mathematical
predictive completion is not a single-carrier acquisition policy. No uniform
noise/separation theorem is supplied by dimension alone. The independent
quantum tests use real rational qubit matrices; the complex finite-dimensional
claim rests on the written proof. The full repository suite, provenance gate,
formal-assistant checks and hosted CI are separate authorities recorded by the
principal agent; this audit does not claim any unobserved run.

The next discriminating extension is a resource- and disturbance-aware
acquisition theorem for the minimal predictive coordinates. A counterexample
where every required coordinate exists as a formal readout but no lawful
joint policy acquires it would prevent the linear reconstruction theorem from
being mistaken for an observer-execution theorem.

## 7. Follow-up blind audit: deterministic adaptive linear acquisition

**Verdict: CG-11 survives in its stated model class.** This follow-up began
from the statement supplied by the principal agent, before inspecting the
constructor's proof. It is a separate derivation using the same model family,
not an independent external reasoner or priority verification.

Let the source be a finite-dimensional Hilbert space with full initial unit
ball; let a finite family of total homogeneous linear actions have positive
state-independent costs. The observer passively reads a fixed linear map `P`
initially and after each action. It retains its actual history. A deterministic
policy must stop within worst-case budget `B`. The target is a fixed linear
function `Fx₀` of the **initial** state; its decoder may be nonlinear.
For a fixed word `w`, let `H_w` stack all readouts along that word.

The exact assertion is

\[
\inf_{\pi}\sup_{\|x_0\|\le1}
 \|Fx_0-\operatorname{answer}_\pi(x_0)\|
 =\min_{\operatorname{cost}(w)\le B}\|F|_{\ker H_w}\|.
\]

**Independent proof.** Execute an arbitrary candidate policy from the zero
source and call its finite action word `w₀`. Every vector `z∈ker H_w₀` has
zero readouts along this entire word. Induct on the action index: the initial
record agrees with the zero run, hence determinism chooses the same action;
the next readout is zero by kernel membership, so the next choice and final
stopping decision also agree. Both `z` and `−z` therefore reach the same
terminal answer `b`. The triangle inequality gives

\[
\max(\|Fz-b\|,\|-Fz-b\|)\ge\|Fz\|.
\]

All hidden unit vectors are in the promised prior. Taking their supremum
lower-bounds the policy's error by the fixed-word radius for `w₀`. Its cost is
feasible on every source because it depends only on the labels, so this is at
least the best fixed-word radius. Conversely, the decoder `FH_w†` for each
fixed word attains its radius by orthogonal projection. Positive minimum action
cost and finite alphabet make the word set finite; hence its minimum is attained.
The empty alphabet has only the empty word. No statistical or empirical premise
enters this argument.

This also validates the exact-identification corollary and finite rational
obstruction certificates: every feasible word can be checked for
`ker H_w ⊆ ker F`; failure supplies a nonzero rational hidden target pair,
scaled rationally into the unit ball. There is no claimed efficient bound on
enumerating all feasible words.

### Executed assumption-deletion controls

Run:

```sh
python research/2026-11-13/principia_observatoris/adaptive_linear_probe.py
```

The standalone probe passed all its exact checks. Its finite prior control
enumerates **all 13 fixed schedules** of length at most two. It computes fiber
balls by rational linear solves over affinely independent support sets; the
critical best-radius comparison also has the explicit pair lower bound below.

| Changed premise or objective | Exact outcome and receipt |
|---|---|
| Full ball replaced by a seven-point symmetric nonconvex subset | With readout register `r`, hidden target `(a,b,c)`, and unit-cost coordinate queries, query `a` then `b` if `a=0`, otherwise `c`. All seven states are identified. Best fixed error is `1/4`, squared radius `1/16`; every fixed schedule fails. |
| Linear actions replaced by continuous nonlinear actions | On unit disk `(s,t)`, read `s`; actions return `max(0,1±2s)t`. Choose the sign of `s` and divide by the known positive multiplier to recover initial `t` exactly. Each fixed action loses the pair `s=∓3/5, t=±4/5`, forcing error at least `4/5`. |
| State-independent costs replaced by state-dependent costs | Two labels implement the same linear hidden-coordinate query. One costs 1 on `r≥0` and 2 otherwise; the other reverses these costs. Budget 1 allows an exact adaptive policy, but no nonempty fixed schedule is uniformly feasible. The best fixed schedule is empty, with error 1. |
| Deterministic worst-case loss replaced by worst-case expected squared loss under private randomization | With two hidden unit-ball coordinates and one affordable coordinate query, deterministic error squared is 1. Uniformly choosing the queried coordinate gives expected squared error `(a²+b²)/2`, with worst value `1/2`. The probe checks the three possible zero-path choices and 25 rational hidden points. |

For the first row the seven hidden points are

\[
0,\quad\pm(0,\tfrac12,0),\quad\pm(\tfrac12,0,0),\quad
\pm(\tfrac12,0,\tfrac12).
\]

Fixed queries `(a,b)` retain signed pairs differing by `1/2` in `c`, so their
radius is exactly `1/4`. Fixed `(a,c)` or `(b,c)` retains an opposite hidden pair
with radius `1/2`. Repeated queries cannot improve information; the exhaustive
probe confirms all shorter and repeated schedules too. Thus mere symmetry and
containment in the ball are insufficient repairs of the full-ball assumption.

A **current-state** target is a different optimization objective. For the
prescribed schedule, replace the fixed initial `F` by `QM_w` as in CG-10. Erasing
hidden data can make the current state predictable without recovering initial
history. A known affine offset does not by itself defeat the center-run argument:
subtracting its known fixed-schedule offset leaves the same linear hidden-fiber
comparison. The homogeneous condition is sufficient, not claimed necessary.

The theorem does not extend this proof to randomization, nonlinear targets,
unknown affine offsets, partial instruments with hidden enabledness signals,
state-dependent costs, or noisy observation simply by retaining the same words.
Those modifications require their own objective, record map and proof.

## 8. Further paper additions checked

**CG-10:** actual-schedule current-target factorization and its conservative
noise bound survive. One typing refinement was requested: the Moore–Penrose
inverse must be defined on the full record space, extending by zero on the
orthogonal complement of `im H`, because noisy records need not lie in that
image. The author repaired this clarification.

**PA-05:** the two-sided beta/Jacobi bound survives independent algebraic
inspection. The exponent `α=N−7/8`, source-density constants `15/64` and `1/2`,
Rodrigues leading coefficient, and boundary orders are consistent. At degree
one the weight norm reduces to
`2/[(α+1)(α+2)^2(α+3)]`, agreeing with direct moment elimination. Strict
minimization bounds use the source minimizer for the lower inequality and the
beta-weight minimizer for the upper inequality. This is a source-specific
precision estimate; it remains separate from signed phase cancellation.
