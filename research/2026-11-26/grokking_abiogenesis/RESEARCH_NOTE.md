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
