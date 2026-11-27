# Recursive Differential Toolkit Closure: the Grokking Abiogenesis bridge

**2026-11-26. Authorial seed: Leah. Status:** conditional elementary mathematical results plus conjectural interpretation, not an amendment to the SUCC kernel. No claims about RH, pi normality, biological or cognitive mechanisms. Companion: TLICA's [First Atomic Connection](https://github.com/femboy2112/TLICA/blob/main/research/grokking_as_toolkit_closure_2026-08-29.md), P11 nested grokking; [recursive ratchet](https://github.com/femboy2112/TLICA/blob/main/research/recursive_epistemic_ratchet_2026-10-02.md).

## Steelman

A finite observer acquires local tools, masters them, then reaches a plateau relative to its available network. A subsequent observation or experiment discloses a law of interaction among mastered tools. This may create a new accessible generator. An optimizer might spend many low-loss steps before the interaction becomes usable, especially when discriminating witnesses or receptive configurations are rare. The task is to distinguish source-identification debt from route-search, representation, cost and deployment debt.

## Typed action and causal contrast

Fix a source X, observation P:X->Y, and family of admissible partial actions on X. Define a word by chronological order w=(a1,...,ak) and A_w=A_ak ... A_a1; only defined paths count. Fix shared preparation, intervention, horizon, observation and any transport before comparing outputs.

For a real/vector output and common domain, D_B A(x)=A(B(x))-A(x); the order contrast is B(A(x))-A(B(x)) if actions and outputs live on the same additive space. More generally compare PBA versus PAB. Neither arbitrary representational differences nor correlations alone establish causality. Use intervention labels, not conditioning on endogenous tool use. For differentiable paths use the chain rule in [CG-01](../../../docs/principia_observatoris/02_causality_geometry.md); for discontinuous tools use finite contrasts.

### GA-01: action-saturation lemma (DISCLOSED, finite linear case)

Let X=F^n, P rank r, and finitely many linear source actions A_a. Define V_k as the span of rows P A_w for words of length at most k. By existing CG-04,
V_(k+1)=V_k+sum_a V_k A_a. Equality at one stage gives right invariance under every A_a and hence equality forever. Starting at rank r, at most n-r strict dimension increases are possible. Thus exact predictive refinement has a finite saturation boundary under fixed actions. This is an import/rephrasing of CG-04, not new priority. A mathematical row space is not automatically executable memory; retain the separate observation-policy acquisition debt. New accessible actions, observation or cost may change the observer, without changing source truth.

### GA-02: observational equivalence under fixed experiments (DISCLOSED, finite rival set)

Let H be a finite set of candidate source laws, E a set of allowed experiments, and deterministic readout F(h,e). Define h~g iff F(h,e)=F(g,e) for every e in E. Any adaptive finite transcript whose next experiment is a function of preceding readouts and an independent random seed has identical readouts for equivalent h,g: induction on transcript length, using the same seed. Thus no such protocol identifies which member generated the transcript. A new experiment can strictly refine an equivalence class iff some currently equivalent pair yields different outputs. No inference about universal truth follows; the result is relative to E and the rival class. In a stochastic version the relevant assumption is equality of conditional response kernels for all reachable histories, not merely equal marginals.

Counterexample to rare-example sufficiency: a uniformly repeated single indistinguishable observation cannot resolve a hidden binary offset; a single valid discriminating observation can. Conversely, if observations already distinguish the rivals but search has not recovered their alignment, new information is unnecessary in principle.

### GA-03: bounded compilation (DISCLOSED, conditional)

Let C_T(f) be the infimum of nonnegative realization costs for semantic function f using typed toolkit T (infinite when no realization exists). Define accessible closure at budget B as functions with a realization costing at most B. Adding a semantics-preserving macro M that expands to an existing valid word does not enlarge the unrestricted semantic closure; substitution proves equality. If original routes remain available, bounded closure cannot shrink. Strict inclusion holds if there exists f with a new realization costing at most B but no original realization costing at most B. For an explicit instance, let the only primitive on integers be x->x+1, cost one per application, composition only. For budget 2, x->x+3 is inaccessible; adding an exact increment-by-three macro at cost one makes it accessible without enlarging unrestricted closure. Include macro construction and maintenance costs in amortized evaluation; a wrapper with unchanged cost need not help. Finite cost gain is not a theorem about human cognition or neural weights.

### GA-04: finite bridge contrast and order countermodel (DISCLOSED, direct algebra)

For A(x)=x+a, B(x)=b*x on reals, B(A(x))-A(B(x))=a*(b-1). Independent of x; reversing order has a predictable effect. Additive translations commute yet their composition is useful. A nonzero order contrast is neither necessary nor sufficient for valuable new access. To claim a mixed intervention interaction require all four observations O_11-O_10-O_01+O_00 in a shared basis; nuisance nonlinearities can also generate nonzero contrast.

### GA-05: first-passage survival (DISCLOSED, discrete stochastic model)

Given a process S_t with first entry tau into predeclared set N and t>=1, define h_t=Pr(tau=t given tau>=t) where survival is positive. By conditional probability Pr(tau>k)=product_{t=1..k}(1-h_t). Constant independent Bernoulli success p gives mean 1/p by summing the geometric survival series. No independence is required for the conditional-hazard product itself. Actual optimizer states may be correlated, deterministic given seed, or gradually moving toward N. A long wait does not demonstrate stochastic escape, sparse evidence, or a phase transition.

## Crucible: classify the obstruction

Use finite rival/probe sets and report pair partitions, unresolved ambiguity, cost of new observation, and provenance. Distinguish:
- E-gap: a true bridge is absent as discriminating evidence;
- pathway-gap: constructible route is not discovered;
- representation/access gap: basis/transport or executable resource missing;
- dominance gap: useful circuit exists but is not selected;
- actual boundary: proved invariant closure or equivalence under stated experiments.

No declared transport, no phase. No hidden-state decoder taken as a causal witness without interventions. No arbitrary scalar collapse of TLICA coordinates. No retrospective selection of N from final test success. No conclusion that differential operators are the sole generating family.

## Probe and verdict

Reproduce the finite gauge theorem and CG-04 under exact arithmetic. Build opaque-source examples with identical local mastery but different hidden relative offsets; valid bridge, within-component redundant, corrupted bridge, complete-information and random-label controls. Split whole generator families, not only examples. Record source law, intervention, basis, readouts and all factorial cells. Follow with paired learning checkpoints: fixed-evidence exploration versus valid bridge exposure, separately test macro compilation at matched cost. Distinguish first functional access, sustained use and transfer. A successful observation strategy is a claim about that source class only.

GA-01 through GA-05 are scoped deductions above (GA-01 imported); generalization to recursive learning and rare-semantic-witness nucleation remains CONJECTURED. The neural/human correspondence and autonomous growth are UNVERIFIED. Next verdict-changing test: exhibit a fixed-evidence learner that can access the bridge under one intervention but not another, then test whether a new evidence intervention has an independent effect. Existing proof and validation suite were not executed for this documentation-only branch; do not promote anything based on it.

## Addendum — Basis emergence from correlated action histories (2026-11-26)

**Authorial seed (Leah):** the two low-growth regimes of a sigmoid staircase (initial ignorance and saturation within a mastered predictive lattice) both look stuck. The next grokking nucleation might correspond to a 90-degree change in observational frame when mastered tools interact, revealing previously unseen structure in their correlated future histories: "we have constructed a basis through emergence."

**Steelman:** distinguish the old accessible observational span from the new residual revealed by a mixed action. A plot of accuracy against steps does not determine a metric, basis, rotation or causal structure. In particular, the two tails of a sigmoid do not imply a 90-degree rotation; swapping axes or units changes plotted slopes. A coordinate rotation within a fixed span cannot enlarge it. The defensible 90-degree object is the orthogonal innovation *after* subtracting the old span, once an inner product is declared. Novelty itself is a metric-free quotient/rank condition. Two individually useful or even orthogonal first-order response directions need not yield a new mixed direction.

### GA-06: metric-free novelty and orthogonal innovation (DISCLOSED; finite linear source)

Let X=F^n, P a linear readout, and W a subspace of X* spanned by already accessible readout rows (possibly from pure and mixed action histories). Let l be an additional executable readout row. Then the following are equivalent:

1. l is not in W (the augmented row rank increases).
2. There exist x and y with identical W-readouts but l(x) != l(y).
3. l restricted to the common kernel W^perp_ann is nonzero; here W^perp_ann denotes the annihilator, not an inner-product orthogonal projection.

Proof: choose a row basis Q of W. Its kernel is the common kernel of W. A row vanishing on ker Q factors through Q (define the induced functional on im Q by l(x)), so belongs to W. Conversely a row in W vanishes on ker Q. A nonvanishing z in ker Q gives the witness pair x=0, y=z. This uses the full vector-space domain; on restricted source support require a witness pair in that support. If future data are constrained so the additional coordinate is already determined by old readouts, no new discrimination follows there.

For real finite-dimensional X* with a *declared* positive-definite inner product, write l = proj_W(l)+r. Then l is novel iff r != 0, and r is orthogonal to every row in W. The quotient class [l] in X*/W is intrinsic to the chosen W and l; the residual and its 90-degree angle depend on the metric. Orthogonality does not imply statistical independence, physical uncoupling, or mutually exclusive causal pathways. It is a construction of coordinates, not creation of a new underlying source dimension.

Given an action family A, if W A_a is contained in W for all a, no finite word of those fixed actions escapes W (induct on word length). Conversely failure of invariance gives some w in W and a with w A_a outside W. If W is spanned by accessible word-readouts, at least one such generator row has a successor outside W. Realizability still requires actual admissible source preparation, action and readout (CG-04 and CG-05; see [Liber Secundus](../../../docs/principia_observatoris/02_causality_geometry.md)). A previously unavailable composite may extend an accessible subspace even if the complete unrestricted closure already contains it.

### GA-07: mixed causal histories reveal a hidden dimension (DISCLOSED; exact constructed example)

Use real column states x=(x1,x2,x3,x4), the row P=e1^T, and E_ij the matrix with a single 1 at row i, column j. Let

```text
A = I + E12 + E34
B = I + E13 + E24
```

P A = e1^T+e2^T; P B = e1^T+e3^T. Each increment squares to zero, so for all nonnegative integers m, P A^m = e1^T+m e2^T and P B^m = e1^T+m e3^T. The entire pure-history span is W=span(e1^T,e2^T,e3^T). Perfect knowledge of these readouts does not distinguish states differing only in x4. This is mastery of separate observable histories, not an assumption that the observer has been handed the full hidden matrices or source state.

Direct multiplication gives (A-I)(B-I)=(B-I)(A-I)=E14, hence AB=BA. The four same-preparation cells are

```text
O00 = P x                  = x1
O10 = P A x                = x1+x2
O01 = P B x                = x1+x3
O11 = P A B x              = x1+x2+x3+x4
O11-O10-O01+O00            = x4
```

With column states PAB means chronological B then A; the reverse is equal here. Thus the mixed functional is e4^T, genuinely outside W, and in the standard Euclidean row metric perpendicular to W. Witness x=0 and y=e4: all pure histories agree, mixed histories disagree. Require reset/repeatable preparations or an equivalent calibrated source interface for actual factorial interventions; the formulas alone do not guarantee physical access.

The mixed residual is not merely a correlation of endpoints. It is an experimentally specified combination of causal action histories. It can be generated even when actions commute. **Noncommutativity is not necessary; a nonzero commutator is not sufficient for new rank.** Controls:
- Additive null A0=I+E12, B0=I+E13: identical pure histories; first-order innovations e2^T,e3^T are orthogonal, but mixed contrast zero and rank stays 3.
- Order-sensitive positive A1=I+E12, B1=I+E13+E24: PAB has e4^T contribution, PBA does not; same pure histories.
- In-span nonzero contrast: one-dimensional P=1, A=2, B=3. PAB-PA-PB+P=2, but all rows lie in the original one-dimensional span. Interaction magnitude alone is not new accessible structure.

For general linear A,B, PAB-PA-PB+P=(PA B) modulo W when W already contains P,PA,PB. Mixed novelty is therefore equivalently nonzero quotient class, not merely a nonzero contrast. For nonlinear, categorical or stochastic readouts do not transplant rank blindly: compare admissible history partitions or conditional response kernels, and use finite differences only in a declared common additive basis.

### GA-08: an exact Boolean-lattice hierarchy of emergent observable directions (DISCLOSED; constructed family)

For m primitives, take a source of dimension 2^m, with row basis e_S indexed by subsets S of {1,...,m}, initial readout P=e_empty, and define N_i by its right action

```text
e_S N_i = e_(S union {i})   if i not in S
e_S N_i = 0                otherwise
A_i = I + N_i
```

The N_i square to zero and commute: if neither i nor j is present, either order adds both, otherwise both products vanish. For T a subset of tools, P times the product of A_i for i in T equals sum_{S subset T} e_S by expanding the product. The complete signed factorial contrast (Boolean Möbius inversion) is

```text
sum_{U subset T} (-1)^(|T|-|U|) P product_{i in U} A_i = e_T .
```

Proof: the coefficient on e_S for S subset T is the alternating sum over S subset U subset T, which is (1-1)^(|T|-|S|), hence one for S=T and zero otherwise. Every required cell is declared. A repeated action satisfies A_i^a=I+a N_i; therefore a word supported on at most k distinct tools only has terms e_S with |S|<=k. Conversely inversion realizes every such basis row using words supported on at most k tools. The exact accessible row space at that support depth has dimension

```text
d_k = sum_{j=0..k} binomial(m,j).
```

In particular, six tools produce ranks 1,7,22,42,57,63,64. Mastering all histories involving at most k distinct tools leaves higher subset coordinates unobserved, even if lower-layer predictions are perfect. Repetition within one support family cannot disclose them. A higher-order bridge exposes an additional basis row. There is no universal claim of exponential intelligence, sample efficiency or sigmoid training; the carrier dimension was constructed to be 2^m, the full factorial requires 2^|T| cells, and observations/actions must actually be accessible. The result gives a precise existence model for recursive basis emergence, not a theorem about arbitrary neural nets. A nested tool compiler may reuse certified mixed operators, but must count construction, storage and validation cost.

### Reproducible calibration and verdict

[Exact BigInt probe](basis_emergence_probe.mjs) and [raw JSON receipt](basis_emergence_receipt.json) preserve the actual standalone function executed in the connector's JavaScript environment (the Node wrapper itself and repository suite were not run). Three matrix controls gave pure/mixed ranks 3/4, 3/3, 3/4; commuting/order-sensitive statuses matched the proof; the scalar nonzero-in-span control stayed rank 1. For m=1 through 6, all signed subset inversions recovered the corresponding basis rows and exact integer row elimination matched every predicted rank. These are finite engineering checks of a constructed family; GA-06–08 are supported by the stated proofs, not by extrapolation.

**Load-bearing consequence:** separate lack of an initial basis from saturation within a current basis. A new functional distinction can arise in mixed future history while all old histories remain perfectly predictable. At empirical grokking, test for a previously unavailable *functional* mixed direction and a subsequent transfer gain, with matched old mastery and exact null/mutation/within-span controls. A high latent rank, learned decoder, nonzero interaction or geometric picture alone is insufficient. For neural learning distinguish observer readout rank from parameter-space rank, cost/expressibility, causal intervention and deployment; use independent calibration and fresh tasks. When no mixed word escapes the full invariant span, the proposed escape is impossible under fixed assumptions. Human/neural 90-degree mechanism and correspondence to the sigmoid staircase remain CONJECTURED / UNVERIFIED. No new arithmetic frontier result or foundation amendment.
