# RX — Independent adversarial audit of X01, X04, X05, X08, X10 and X12

## Scope and result

**SURVIVES WITH STATED HYPOTHESES.** I independently read all six complete
dossiers, reconstructed the central arguments, inspected both associated
formal modules, and wrote fresh exact controls importing no SUCC code. No
theorem-breaking counterexample or actionable mathematical defect was found.
This is a separate model-agent review, not independent academic peer review,
priority verification, or a certificate for unexamined implementations.

The requested starting snapshot was `7405aba`. The integration branch advanced
while this read-only review ran; the six dossier hashes below identify precisely
what was reviewed. Root source files were not edited.

| Claim | Verdict | Load-bearing gate independently checked |
|---|---|---|
| X01 | Survives | Injective completion map **and** a lift of every target source via surjective f are both used to reflect actualization. |
| X04 | Survives | A finite trace-language surrogate chooses a continuation; it is not thereby a commuting factor of the original source. |
| X05 | Survives | T transports unnormalized joint laws but is never sampled from an unobserved actual state; G uses only an observed report. |
| X08 | Survives | Full cyclic successor, total actions and equivalence are sufficient for subgroup congruence; arbitrary nonlinear actions are excluded. |
| X10 | Survives | Multiplicative observable-algebra closure, rather than invariant linear span alone, gives the exact finite quotient. |
| X12 | Survives | Reachable event-domain cross-stage squares preserve replay; separate static quotients alone do not. |

## X05: stochastic T, partial menus, and derandomization

For each original o and simulated history h, the induction is genuinely on
`mu_Y(o,y,h) = sum_x mu_X(o,x,h) T(y|x)`. Summing in y preserves the complete
original/history law. It does not merely preserve report marginals. Multiplying
the one-step square by mu_X and summing x proves the next induction step without
conditioning on a sampled hidden y. The actual controller needs only an actual
action and its report-dependent G coin. This is an implementable protocol under
the dossier's explicit authorization of finite randomization.

If the virtual support lies in its enabled set, positivity implies that each
positive actual x has its entire T-row supported in that set. The stated
availability-lifting premise then makes the action legal for the actual belief.
Retaining actual reports and past coin records can only shrink the relevant
support, so legality survives the finer actual filtration. Conditioning at an
impossible history is never needed.

The derandomization argument is valid for the finite horizon and finite alphabets
specified. At a controller coin node, condition on its actual report/history and
internal record. Its coin is independent of the unknown source conditional on
that record. Every positive coin option has a feasible continuation, because an
infeasible positive option would create positive failure probability. Fixing an
option with no greater conditional continuation cost preserves correctness and
availability. Backward selection through the finite tree eliminates every coin.
Once fixed, internal beta memory is a deterministic function of the actual
history, so this is an admissible deterministic history policy. The proof does
not assert that a hidden sampled T-state becomes available or establish an
infinite-horizon measurable-selection result.

Fresh exhaustive probe: all 20,736 combinations of deterministic binary actual
and virtual instruments and half-integral binary channels T,G were checked against
the displayed joint square. Exactly 944 satisfy it, including 272 with stochastic
T. An unequal original prior correlated with the initial actual state was replayed
through depth 3. All 56,640 original/current path equalities passed. An additional
108 support/menu combinations verified the exact availability implication. This
finite control does not itself prove the universal theorem or derandomization.

## X12: history-local representation changes

The source identity `R_k = U_a(R_h,a,y)` is correct: every current state in an
event-domain fiber has at least one original whose already fixed history reaches
it, and those originals are exactly the ones surviving that event. Consequently
the quotient transition is both well-defined and onto its next reachable carrier.
Support induction preserves original identities even when distinct originals
have collided at the same current state.

Composition uses the second transition W on `p_h q_h(c)` and obtains
`p_k q_k U_a(c)`. It does not erroneously compose two temporal transitions or
require an inverse to physical erasure. The same argument applies only to a
schedule fixed from the recorded history, and target preservation keeps the same
map T on original indices. The document correctly rejects changing the target
or using a representation schedule selected by an unobserved original.

The fresh two-state probe checks 352 candidate local schedules after guard and
report descent. It accepts 344 and rejects eight specifically because the
cross-stage transition cannot factor. All accepted schedules preserve the exact
original event supports and transported current states. This is a one-transition
test; arbitrary finite histories are covered by the written induction, not by
an unperformed exhaustive infinite test.

## X01: completion and actualization

T1 has the correct direction: continuous coordinate coding sends closure of the
actual trace image into closure of the transported trace image. For T2, finite O
makes K_X compact; its image is closed in the Hausdorff target product. Both
inclusions in the image equality therefore hold. The target alphabet need not
be finite. With exact report preservation and surjective f, the actual trace
images already coincide, so no compactness premise is needed for that special
case.

For T3, the disagreeing-pair subset of K_X squared is closed: agreement or
disagreement on a finite discrete coordinate set is clopen. Compactness gives a
finite coded separator set uniformly over that subset. Conversely, separate
finite-compatibility witnesses matching each of p and q on F union G suffice;
they need not be the same original. The proof's quantifier order is correct.

T4 then lifts an actual Y witness y to x, equates the two completion images, and
uses injectivity. A completion homeomorphism alone does not provide that source
lift, as the finite-support/full-stream inclusion counterexample correctly shows.

I inspected `SwarmX01CompletionTransport.lean`. Its actualization-reflection
theorem has both surjectivity and injectivity hypotheses, and the completion
construction explicitly assumes the trace intertwiner. The dossier accurately
leaves action-word induction, compact image equality and the uniform finite
recovery theorem outside this module's kernel scope. I did not recompile this
mathlib module in RX and claim no additional independent compilation for it.

## X04: generation, coverage, and factoring

A length-m word emitted by a source state must have an overlap successor emitted
by the next source state. Conversely, choosing one overlap successor for each
word creates a total deterministic source with exactly those m-words. Repeated
overlap gives the original word's j-th symbol at step j for j<m. Since one state
has only one emitted m-word, |L| is the sharp state lower bound. The proof is
independent of input-language Myhill–Nerode recognition, where input words can
come from outside the counted system.

The full-shift factor impossibility follows from requiring one fixed finite Q to
cover 2^m distinct words for every m. It does not contradict a fresh finite
surrogate for each m or a one-state constant observer. The cylinder-resolution
bound explicitly restricts the admissible report fibers; the separate arbitrary
future-bin sensor has the smaller stated count. The restriction is substantive.

All 273 nonempty binary languages of lengths 1 through 3 were independently
enumerated. Exactly 125 satisfy the no-dead-end condition. The selected-successor
construction emitted exactly its input language in every accepted case.

## X08 and X10: algebraic bridges

For X08, successor stability on the finite cyclic carrier implies stability
under every translation, including inverses. The zero equivalence class is a
subgroup, so every stable relation is a congruence modulo a divisor. All integer
affine maps preserve that congruence. Therefore successor repair is already
dilation-stable, giving both displayed repair-composition identities. This does
not make the induced successor and dilation commute. The arithmetic commutator
centrality test `m | (a-1)^2` for unit a follows by conjugating a translation by
D_a; nonunit slopes are correctly excluded from the group-loop statement.

I independently checked all 1,155 partitions of cyclic carriers of sizes 1–7.
The 16 successor-stable partitions have exactly the stated congruence form, and
all 367 corresponding affine maps preserve them. I read and successfully
recompiled `Swarm_X08AffineRepair.lean` with the official Lean 4.14.0 wrapper.
Its three theorems prove natural-source translation/dilation/affine stability;
they do not claim the finite cyclic classification. The wording matches this.

For X10, all word-report generators of depth at most k are R_k-constant. Finite
products of separating word-report indicators construct every R_k-class
indicator, and linear combinations give every R_k-constant function. Thus the
generated algebra has the stated dimension. At each strict step its dimension
increases, proving stabilization by n-b. If r is any lawful augmentation of q,
its equal fibers stay equal after every action word, so ker(r) is contained in I;
this gives the correctly directed unique map from its observer to S/I.

The four-state swap example correctly distinguishes an invariant linear span
from the full function algebra. The finite-jet counterexample uses x^(m+1),
which has the same m-jet as zero and a different next derivative and translated
value. It refutes that specified hierarchy, not all possible finite real-valued
encodings or a general finite-dimensional PDE closure theorem. No such larger
claim is made in the reviewed dossier.

## Validation and precise boundaries

Executed successfully:

```sh
python /workspace/scratch/79b9e8091cb9/reviews/RX_cross_bridges_probe.py > /workspace/scratch/79b9e8091cb9/reviews/RX_cross_bridges_receipt.json
/workspace/scratch/79b9e8091cb9/lean-root/lean-4.14.0-linux/bin/lean formal/Swarm_X08AffineRepair.lean
```

The probe and receipt are separate deliverables. No repository-wide suite was
run by this reviewer. No formal proof is supplied for X04, X05, X10 or X12; the
verdict is paper-proof survival with finite independent controls. No empirical
source authentication, priority claim, or RH consequence follows.

Reviewed SHA-256 values:

```text
X01.md a72b8bf4d726f02bf7fec298aa9e5794cc00011bfaadcbb383467da160db969d
X04.md bd5cfb8e03f42a98e36636006ef7526fa9087f2641b9b835b6bda9d80feebcec
X05.md 7ae5973691e6002c14e90ccb1032dead061087c52fb6332d2f272b27e7eca9f7
X08.md 559b8ffc57a7c87d0d6f10300150a31c456eff0327283b325ccee9ac6ed2af41
X10.md 1985fb451a24bc65fcc720a202c80a03062037526c3c0bbf923e58560f43dd48
X12.md 291668cc6b44a9c511508d5d8e922c6977ccf809791648a504bbdd6160f66e24
SwarmX01CompletionTransport.lean 1510cfaca83bcbc5a30d128110525d8df2328a46d44d702036f245e455261141
Swarm_X08AffineRepair.lean f315b95b37ef85d9a1efebdbc12c46552f3ceec045f1348ab4b36dc5e0e23775
```
