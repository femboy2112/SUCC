# X07 independent crucible by D26

**Verdict: SURVIVES / PROVED LOCAL** for X07-T's stated mathematical hypotheses. No counterexample to that theorem was found; its proof is reconstructed below. The category and physical interpretation remain conditional on the complete, common source interfaces and globally coherent selected-branch maps. Three clarifying amendments are recommended; none repairs a defect in the theorem.

Author inspected: `57618f394b9f1aab9fd2c5c06483f98a36751afc`, file `research/2026-10-13/SWARM_ATLAS/X07.md`, Git blob `aec843c1c706ba4dd7188021887c7b7b45b780eb`. Reviewer worktree: `/home/leah/succ_lab/swm-d26`, branch `research/swm-d26-2026-10-13`, pre-review parent `e7bedd04eb27c0d7928e924b3e9fd1d58ff5861d`. This is an extra review assignment by the existing D26 worker, not a newly spawned agent. The reviewer read the author dossier only, not its probe or receipt. The principal supplied the scaffold to the author; this non-deriver review therefore tests the displayed theorem rather than claiming independent discovery or a blind hypothesis origin.

## Reconstructed theorem and proof

The essential algebraic input is a directed poset D and a functor with total positive linear maps `R_IJ:K_I→K_J`. Each cone has a nonnegative linear mass `u_I`; masses are faithful on the images needed below. Fix one original cone K_0 and one original candidate set `C⊆K_0`. Let `T_I=R_0I`, `ℓ_I=u_I T_I`, `Z_I={x∈K_0:ℓ_I(x)=0}`. Assume the attained zero faces have finite height. X07's finite height of the entire original face poset is a stronger sufficient hypothesis.

1. **Zero-facehood.** Positivity ensures `ℓ_I≥0` on K_0. Its zero set is convex and conic. If `x+y∈Z_I` with `x,y∈K_0`, then `0=ℓ_I(x)+ℓ_I(y)` forces both summands to vanish. Thus Z_I is a face. This is a statement about the original source cone, not the normalized poststate.
2. **Zero absorption.** If `ℓ_I(x)=0`, positivity gives `T_Ix∈K_I`, and faithfulness gives `T_Ix=0`. Functoriality and linearity yield `T_Jx=R_IJ(0)=0` for `I≤J`. Therefore `Z_I⊆Z_J`. Alternatively `0≤u_JR_IJ≤u_I` alone establishes this nesting; faithfulness is sufficient, not necessary when contraction is assumed.
3. **Maximal attained face exists.** Give each attained face the greatest number of strict inclusions in a chain of attained faces ending at it. The integer ranks are bounded by finite height. Choose an attained face of maximal attained rank. Strict containment in another attained face would increase rank, so it is maximal among attained faces. No countable indexing or compactness is used.
4. **Maximal becomes greatest.** For any J, directedness provides U above J and I_*. The inclusion `Z_I*⊆Z_U` and attained maximality imply equality. Since `Z_J⊆Z_U`, every attained Z_J lies in Z_I*. In the ideal model U is exactly the finite downward ideal `I_*∪J`.
5. **Exact intersection.** For x in the fixed C, being outside Z_I* implies being outside every Z_J. Nonnegative likelihood then implies positive likelihood. Being inside Z_I* fails the I_* test. Hence the stated intersection equals `C\Z_I*`. The premise supplies an x outside Z_I* by applying it to that one attained ideal. Every extension of I_* has the same zero face.

Normalization and nonemptiness of C are state/premise conventions, not additional algebraic work: the equality holds for any C⊆K_0, including empty C; the witness implication is then vacuous for empty C. Convexity and closure of C are unnecessary.

For finite ideals, any adjacent swap of incomparable occurrences has a common prefix where both occurrences are eligible in the poset sense. The correctly typed *selected-branch* square equates the two composed maps. Connectedness of finite linear extensions under these swaps therefore gives the ideal functor. Operational enabledness persistence is needed to identify those abstract schedules with real executable schedules. Mere equality of report labels or total channels does not supply this functor.

## Cone instances and prior art

For a finite-dimensional convex cone, every proper nonempty face has smaller dimension. If F⊊G had equal affine spans, a point in `relint F` would be in `relint G`; writing that point inside a segment from an arbitrary y∈G to another point in G forces y∈F, contradiction. Consequently nonempty face chains have at most `dim(span K)` strict inclusions. Faithful mass also makes K pointed, so `{0}` is a face. No closedness assumption is needed here. This classical dimension fact is discussed in [Weis, *A Note on Touching Cones and Faces*, §§1.1,3](https://arxiv.org/pdf/1010.2991).

For `R_+^d`, faces correspond to coordinate subsets; a strict inclusion adds a coordinate. For Hermitian PSD_d, positive functionals are `ℓ(ρ)=tr(Eρ)` with E≥0. The identity `tr(Eρ)=||E^(1/2)ρ^(1/2)||_HS²` shows that zero likelihood is exactly support containment in ker E. Faces correspond to support subspaces, giving at most d strict inclusions, or d+1 faces when endpoints are counted. The real-symmetric version is independently documented in [Laurent–Vallentin, *Semidefinite Optimization*, §6.1.2](https://homepages.cwi.nl/~monique/master_SDP_2016.pdf). The bound uses the original space, regardless of later output-space growth. Infinite-dimensional trace-class cones generally do not satisfy that finite-height premise.

## Hypothesis removals and hostile receipts

The following countermodels refute weakened statements, not X07-T. Finite matrix witnesses are independently executed; infinite families are explicitly derived.

| Removed obligation | Minimal countermodel or consequence |
|---|---|
| Directed joint ideals | On `R_+²`, C={e_0,e_1}, index only root,a,b with maps P_0,P_1. Each available ideal has a witness; their compatible-source sets are disjoint. Adding their union forces map zero and exposes the missing premise. |
| Faithful current mass, without contraction | Chain maps `R_01=id`, `R_12=P_1`; masses `u_0=u_2=(1,1)`, `u_1=(1,0)`. e_1 has zero intermediate mass but positive final mass. C={e_0,e_1} supplies each individual test and no common source. All maps remain positive. |
| Positive maps | With all masses `(1,1)`, use `R_1=[[1,1],[0,-1]]`, `R_2=[[0,-1],[0,0]]`. Likelihood rows are `(1,0)` then `(0,1)`. Intermediate e_1 becomes `(1,-1)`, a nonzero zero-mass vector outside the cone. Separately the signed row `(1,-1)` has a nonfacial zero hyperplane: e_0+e_1 is zero, neither summand is. |
| Finite height | On `c_00(N)_+`, let T_n discard coordinates k<n; mass is the finite coordinate sum; C={e_k}. Each n has witness e_n, but every e_k dies at n=k+1. The common positive diagram has zero faces of unbounded height. |
| Fixed original C | Identity maps on `R_+²`, but classes C_0={e_0}, C_1={e_1}. Individual normalized witnesses exist; their class intersection is empty. This is no longer a theorem about one candidate class. |
| Common linear source maps / complete original interface | Use fixed normalized points `p_k=(1/(k+1),k/(k+1))` in `R_+²`. The branch *chosen for source k* is identity through time k, then zero. Each selected branch is positive and contractive, every finite prefix has some k, and no k passes all. There is no common linear diagram on the declared 2D cone. Restoring the hidden classical label gives the unbounded-height original cone above. |
| Full selected-report squares | Z/X total dephasing channels commute on all four matrix basis units. Their selected P_0/P_+ Lüders branches give ordered masses `1/2` and `1/4` on P_0. Equal coarse labels and commuting total channels hide different branch maps. |
| Operational enabling | Starting at 0, a flip is enabled and a probe restricted to state 0 is enabled. Flip-then-probe is undefined; probe-then-flip is defined. A vacuous partial-domain comparison or a fictitious total extension does not create an executable ideal square. |
| All ideal witnesses | P_0 and P_1 commute and each thread has a source, but their joint ideal has zero map. This directly violates the actual all-ideal premise. |
| Finite-past event coverage | In poset `ω+1`, the top event has infinite past and belongs to no finite downward ideal. Positive identity reports on every finite ideal say nothing about a killing branch at that uncovered event. X07 already limits its coverage correctly. |

Dropping optional mass contraction preserves the face theorem but loses probability bounds: the scalar branch `x↦2x` has mass 2 on a normalized source. Dropping CP also preserves this abstract positive-cone theorem: matrix transpose is positive and trace-preserving, but its Choi swap has exact quadratic value −2 on `(0,1,−1,0)`. It cannot thereby be promoted to an admissible quantum instrument.

## Infinite-index and operational boundaries

Take an uncountable antichain P. Any countable family of finite ideals has countable union, so an occurrence outside that union has a singleton ideal not contained in any member. No countable cofinal chain exists. Nevertheless the scalar diagram `T_I=2^(-|I|)id` has a single original source passing every finite ideal. The proof above uses directed upper bounds, not a purported chronological enumeration of all occurrences.

On a countable chain, `T_n=2^(-n)id` similarly has constant zero face and positive likelihood at every finite depth. In the ordinary fair-coin model these are the all-heads prefix probabilities, whose intersection probability is zero. The theorem gives neither a positive lower likelihood bound nor positive probability of an infinite report event, nor any actual infinite observation record.

There is also no uniform stabilization deadline from face height. On `R_+²`, take identities for N−1 steps, P_0 at step N, then identities. Every finite ideal has source e_0 and only one strict face growth occurs, but the first ideal attaining the greatest zero face has N occurrences. N is arbitrary; the probe uses 37. A witnessed plateau, even a long one, is not a certificate that no future face growth is possible.

## Amendments and acceptance boundary

1. State the theorem's direct input as a common, total positive **ideal functor**, then state full selected-branch squares and enabling persistence as sufficient operational construction obligations. This prevents readers from substituting marginal or total-channel commutation.
2. Define height as the number of strict inclusions. Orthant_d and PSD_d have at most d such steps and d+1 nonempty faces in a maximal chain. Add the finite-dimensional cone dimension argument; do not apply the PSD_d bound to unrestricted infinite original memory.
3. Replace “preserving mass” for arbitrary nonnegative B with: `tr(Jp)=sum p`, and the *matched branch masses* satisfy `tr(Φ_BJp)=sum Bp`. B is mass preserving only when column sums equal one; it is mass contractive when column sums are at most one. Restrict the claimed identity-preserving functor to diagonal algebras, as the author already correctly does.

These are exposition and scope amendments. **PROVED LOCAL** is warranted for the displayed conditional theorem, independently of its probe. **TESTED MODEL** applies only to the finite exact cases in the review receipt. Source authentication, infinite actualization, effective deadlines, quantum copying and original-target decoding are outside acceptance. The next useful probe is a declared apparatus-memory model checked for a common selected-branch ideal functor before any physical claim.

κ: exact matrix/cone contact, not measurement; φ: independently reconstructed proof plus hostile witnesses; σ: fixed author SHA and separately implemented finite maps; ρ: scaffold dependence disclosed. This worker shares model/tool environment with the author workflow, so the review is a non-deriver bearing, not independent hardware evidence.

## Deliverables and commands

Only this review and `X07_D26_probe.py`, `X07_D26_RECEIPT.json` were added. The probe uses standard-library Fractions, eight directed ideals with incomparable faces, separately composed report branches, five PSD fixtures and hypothesis mutations; it does not import repository modules or author artifacts.

Generation: `PYTHONDONTWRITEBYTECODE=1 timeout 25s python research/2026-10-13/SWARM_ATLAS/reviews/X07_D26_probe.py > research/2026-10-13/SWARM_ATLAS/reviews/X07_D26_RECEIPT.json` — **exit 0**. Infinite-family conclusions above are proofs, not extrapolations from those finite fixtures. Receipt SHA-256: `df17926d8fe2eea1d04c9fb3910f124c6883f8fc640df9d4e2fc2f7438bc0e1d`. Replay command: `PYTHONDONTWRITEBYTECODE=1 timeout 25s python research/2026-10-13/SWARM_ATLAS/reviews/X07_D26_probe.py > /tmp/X07-D26-replay.json`; byte comparison: `cmp research/2026-10-13/SWARM_ATLAS/reviews/X07_D26_RECEIPT.json /tmp/X07-D26-replay.json` — both **exit 0**. No full suite, compiler, children, shared writes or push.
