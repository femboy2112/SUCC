# SWM-X11 — Positive proofs, evidence ideals, and the partial report boundary

**Verdict: CLASSICAL / PROVED LOCAL + TESTED MODEL.** This second-generation
bridge combines B12's evidence domain, B13's finite proof supports, B14's
relative clopenness, and the existing checkpoint/ordinal report modules.
Parent: `71eaf11e48ca3ccb349858bba64abf36b59ee6f5`. Independent assignment:
`/root/cross11_domain_prooflimits`; isolated worktree `cross-X11`.

## 1. Original question

Exactly which claims about an ideal limit can be justified by finite, licensed
proofs using the evidence contained in that limit? When can the converse be
implemented, and when does a purported omega+1 answer add a new commitment?
The target is an explicit typed correspondence, including undefined answers
and source-admissibility, rather than an identification of limit truth with
proof or computation.

## 2. Existing mathematical context

Ideal completion, compact elements, Scott opens, and partial Boolean domains
are classical domain theory. Primary references read during this assignment:
Abramsky and Jung, *Domain Theory*, Handbook of Logic in Computer Science 3
(1994), corrected author manuscript, sections 2.2.6 and 2.3:
https://www.cs.ox.ac.uk/people/samson.abramsky/handbook.pdf .
Abramsky's 1988 thesis *Domain Theory and the Logic of Observable Properties*
already explicitly connects finite observations, domain semantics, and logic;
author abstract/metadata: https://arxiv.org/abs/1112.0347 . No priority claim
is made for that connection. The proofs below are supplied independently.

Repository predecessors are B11–B14, `swarm_completion.PartialEvidence`,
`checkpoint_meta_tower.HornTheory` and its monotone theory checkpoints,
and `ordinal_succ_report.exact_bounded_time_horizon`. Their source/basis,
evidence-versus-prediction, and Gamma-completion boundaries remain premises.

## 3. Proposed SUCC objects

Fix a source/basis context and a nonempty declared source set `X ⊆ O^W`, where
`O` is discrete and `W` is an arbitrary address set. For a finite partial map
`p : W ⇀ O`, write `C_X(p) = {x ∈ X : p ⊆ x}`. Let `K_X` be the poset of
finite `p` with `C_X(p) ≠ ∅`, ordered by extension. The empty report is bottom.
Its ideal completion `D_X = Idl(K_X)` consists of nonempty, downward closed,
directed sets of finite reports, ordered by inclusion. Put

`η(x) = {p ∈ K_X : p ⊆ x}` and `↓p = {q ∈ K_X : q ⊆ p}`.

An ideal has a consistent partial-map union; every finite restriction of that
union is source-admissible. Its entire union need not have one original-source
realizer. Fix a catalog `L` of rule licenses; licensed evidence lives in
`D_X × P(L)`. Both source/basis identity and the catalog's semantic meaning
are fixed. Available licenses may grow monotonically. Retraction or a new
source requires a separately proved transport map.

A certificate `c` has a finite proof, conclusion `φ`, finite evidence support
`p_c ∈ K_X`, and finite license support `ℓ_c ⊆ L`. A fixed checker decides or
specifies whether this particular proof is legal. It is available at `(I,A)`
exactly when `p_c ∈ I` and `ℓ_c ⊆ A`. Legality may not secretly consult an
absence test or a global property of the later ideal. Proof soundness means
that, under the declared semantics of its licenses, every `x ∈ C_X(p_c)`
satisfies its conclusion. Openness does not establish that semantic premise.

## 4. Candidate theorem

**A — Exact support correspondence.** For every such fixed certificate system
and every conclusion `φ`, its availability set

`U_φ = {(I,A) : ∃ legal c concluding φ, p_c ∈ I and ℓ_c ⊆ A}`

is Scott-open in `D_X × P(L)`. Consequently, for every nonempty directed family
`(I_j,A_j)`, certification at `(⋃ I_j, ⋃ A_j)` already occurs at one stage.
Conversely, every Scott-open subset of this domain has a presentation as a
union of such finite-support cylinders, regarded as abstract certificate
schemas. This converse supplies a set of certificates, not an effective
enumeration, proof of a pre-existing formula, or authentication of `X`.

**B — Partial Boolean representation.** Let `B⊥ = {⊥,0,1}`, ordered only by
`⊥ ≤ 0` and `⊥ ≤ 1`. For any `P ⊆ X`, there exists a Scott-continuous map
`f : D_X → B⊥` satisfying `f(η(x)) = 1_P(x)` for every `x ∈ X` if and only if
`P` is clopen in the subspace product topology of `X`. No compactness,
countability, or effective access is needed for this set-theoretic theorem.

**C — Effective qualification.** If the finite basis, legal certificates,
and the arrival stream of evidence/licenses have effective encodings and
the certificate family is recursively enumerable with decidable finite
support matching, positive certification is a semidecision. Scott openness
alone does not imply these access hypotheses or any computable time bound.

## 5. Proof attempt: complete paper proofs

**The domain.** Directed unions of ideals remain nonempty, downward closed,
and directed: two chosen members lie together in a sufficiently large ideal
of the directed family. Thus `D_X` is a dcpo. The principal ideal `↓p` is
compact, since `↓p ⊆ ⋃ I_j` implies `p ∈ I_j` for one `j`. Every ideal is the
directed union of its `↓p`, `p ∈ I`; compactness applied to this representation
also proves that every compact ideal is principal. A finite license set is
compact in `P(L)`, by the same finite-support argument. Their pairs are the
compact basis of the product; directedness combines finitely many licensing
stages with the one supplying `p`.

**A forward.** A certificate remains available under extension. If it is
available at a directed supremum, its evidence support belongs to one ideal
stage and each of its finitely many licenses belongs to some license stage.
Directedness supplies a single stage above all of these. The same exact proof
then verifies there. This proves upper closure and inaccessibility by directed
suprema, hence Scott openness. Equivalently its positive answer is a
continuous map to the Sierpinski domain `{⊥ < yes}`. Soundness, if supplied,
transfers the syntactic positive answer to all original sources compatible
with the support, by induction through the finite derivation.

**A converse.** If `U` is Scott-open and `(I,A) ∈ U`, express `(I,A)` as the
directed union of compact pairs `(↓p,ℓ)` with `p ∈ I` and finite `ℓ ⊆ A`.
Some such pair is in `U`; upper closure puts its entire cylinder inside `U`.
Use each compact pair belonging to `U` as one abstract certificate schema.
Their cylinders give exactly `U`. This is a representation theorem for an
already supplied `U`; it is not a procedure for deciding which compact pairs
belong to an unknown set.

**B forward construction.** Define `f_P(I)=v` if some `p ∈ I` has
`C_X(p) ⊆ P_v`, where `P_1=P` and `P_0=X\P`; otherwise define `f_P(I)=⊥`.
Both values cannot occur: directedness would give a common extension
`r ∈ I ⊆ K_X`, and any original source in nonempty `C_X(r)` would be in both
`P` and its complement. The map is monotone. If its value at a directed
supremum is `v`, its witnessing finite report belongs to one stage, so that
stage already has value `v`. This proves Scott continuity. If `P` is clopen,
every original `x` has a finite cylinder within its side of the partition;
that cylinder's support belongs to `η(x)`, yielding the required total answer
on original-source points.

**B reverse.** A basis Scott-open set `{I : p ∈ I}` pulls back under `η` to
the relative cylinder `C_X(p)`, so `η` is continuous for the product topology.
The sets `{0}` and `{1}` are Scott-open in `B⊥`. Thus the pullbacks of their
inverse images under `f` are respectively `X\P` and `P`, both open. This
proves the converse. A report need not be defined on phantom ideal points.

**C.** Dovetail the enumeration of certificates with arrival of evidence and
licenses. Revisit enumerated certificates until their finite support has
arrived. An available proof is found eventually, and no unsupported one is
accepted. For the failure of the converse take a non-r.e. set `H ⊆ N` and
the partial-map domain on `N` with singleton alphabet. The set
`U_H = {p : dom(p) ∩ H ≠ ∅}` is a union of compact cylinders, hence Scott-open.
A uniform semidecider for it on finite evidence would semidecide `n ∈ H`
by running on the singleton report at `n`, contradiction. No nonexistent
oracle is implemented by the finite probe.

## 6. Crucible

**Scattered phantom ideal.** Let `X` be eventual-zero binary streams and let
`P` say that the first zero has even address. Both `P` and its complement are
open in `X`: the finite prefix through the first zero decides parity. For
every finite, possibly scattered `F ⊆ N`, let `p_F(n)=1` for `n ∈ F`.
These reports form a directed basis family, since `p_F ∪ p_G = p_(F∪G)`.
Choose an even `e` and odd `o` above `max F`. The original sources
`1^e 0^∞` and `1^o 0^∞` extend `p_F` and have opposite answers. The ideal
`I∞={p_F : F finite}` has total union `1^∞`, which lies outside `X`, and its
canonical partial report is `⊥`. Forcing either answer at `I∞`, while staying
correct on all originals, would require a compact support and contradict
these two extensions. This is a genuine limit barrier, not just a prefix
example; the probe tests 154 arbitrary scattered supports.

**Kripke persistence is weaker than finite observability.** On all binary
partial maps, let `Z` mean that some observed coordinate is zero. `Z` is
Scott-open. Its order/Kripke negation is true at `p` exactly when no extension
of `p` lies in `Z`. This happens only at the *total* all-one map: any undefined
coordinate could instead be extended by zero. The negation is persistent,
yet not Scott-open, because the total map is the directed union of finite
all-one restrictions. Thus full future-quantified Kripke implication/negation
cannot be silently included in the positive finite-certificate theorem.
An observed literal `x(n)=0` is itself positive finite evidence; it differs
from inferring a negative global claim from unsuccessful search.

**Totalization.** Total maps are not Scott-open for infinite `W` and nonempty
`O`. Also every Scott-continuous map from the whole bottomed domain `D_X`
to the *discrete* two-point order is constant: monotonicity forces its value
at bottom to equal its value everywhere. The partial Boolean codomain avoids
this false demand without weakening correctness on actual source points.

**Source-relative joins.** For `X={(0,1),(1,0)}`, the separate reports
`{2↦0}` and `{7↦0}` are admissible, but their conflict-free union is not.
The code rejects certification from an empty source fiber. Replacing `D_X`
by only partial reports with a whole-source extension loses directed
completeness for nonclosed `X`; the eventual-zero example has no upper bound
there. Ideal completion preserves finite compatibility, not actualization.

**Finite exact controls.** At addresses `(2,7,19,43)`, three licensed Horn
rules have target condition
`(r0∧r1∧x2=1∧x19=0∧x43=1) ∨ (r2∧x7=0)`.
The independent direct formula matches proof search on all 648 evidence/license
stages. All six rule orders agree (3,888 checks). A separate embedding into
the pre-existing Horn checker agrees on all 648 stages. All 16,875 comparable
stage pairs preserve certification; 1,139 actual proof transports replay.
Removing necessary leaves/licenses, changing source/basis, and forging an
inference gives eight rejected mutations. All 16 properties of a complete
four-world source produce 144 partial report states with 400 lawful comparable
pairs. All seven ideals of the two-world admissible finite basis are principal.
An unsound licensed rule still has finite support, demonstrating explicitly
that syntactic continuity alone does not establish semantic truth.

## 7. Verdict

**CLASSICAL / PROVED LOCAL:** the precise ideal/support correspondence,
partial-Boolean representation, effective qualification, and all no-go
arguments have complete paper proofs above. **TESTED MODEL:** the frozen exact
controls reproduce the finite instances and integration map. No theorem in
this assignment is claimed Lean-kernel checked, academically original, a
reflection principle, an incompleteness theorem, or an RH result.

The independent B12/B13 audit is in `X11_REVIEW.md`. Their theorem statements
survive. B13's phrase “exactly under” finitary assumptions must be read as
“under these sufficient assumptions”: redundant infinitary rules can leave
the same continuous closure.

## 8. Remaining obstruction

For a concrete new report, exhibit its finite supports and supplied rule
licenses, or prove its specified map is discontinuous. For effectivity, give
an r.e. support presentation and an operationally available evidence stream.
For original-source realization, separately establish the source-image
closedness/compactness conditions from B09–B10. None is supplied by relabeling
a report omega+1. The smallest next falsifier is an alleged legal proof whose
acceptance changes when a previously absent report arrives: that exposes a
hidden negative premise or nonmonotone source/basis revision.

## 9. Cross-domain connection: actual maps and invariants

The evidence map is `p ↦ ↓p`; source embedding is `x ↦ η(x)`; the preserved
invariant is one unchanged finite evidence/license support for each positive
conclusion. The licensed proof map into existing `HornTheory` sends a rule
`a1,...,ak → b` with license `r` to the ordinary Horn rule
`license:r,a1,...,ak → b`, and adds exactly the available license atoms to
the evidence. Forward derivations translate step for step in both directions.
Source and basis identifiers are fixed, and the probe checks this concrete
embedding rather than merely comparing labels.

For a fixed finite rational query set in `ordinal_succ_report`, the function
`exact_bounded_time_horizon` already supplies a finite arithmetic dependency
horizon. Its completed Gamma/pole term is a separately declared analytic
premise. X11 says that any *sound finite certificate* using those dependencies
and premises transports to a common evidence stage. It does not turn mpmath
values into rigorous certificates, supply Gamma completion, or prove positivity
for all test functions. Some numerical postprocessing can be continuous in
a suitable approximation codomain; the obstruction here concerns specified
discrete positive or total Boolean claims, not all possible limit reports.

## 10. Deliverables and exact verification

- `observational_succ/swarm_x11_proof_limits.py`
- `scripts/swarm_x11_proof_limits_probe.py`
- `tests/test_swarm_x11_proof_limits.py`
- `research/2026-10-13/SWARM_ATLAS/X11_REVIEW.md`
- `research/2026-10-13/SWARM_ATLAS/X11_RECEIPT.json`

Executed in the isolated branch:

```sh
python -m unittest discover -s tests -p 'test_swarm_x11_proof_limits.py'
python scripts/swarm_x11_proof_limits_probe.py
```

All 10 dedicated tests pass. The second command reproduces the receipt.
Full-repository validation is reserved for the principal's integrated
checkpoint; this assignment does not claim that it ran the full suite.
