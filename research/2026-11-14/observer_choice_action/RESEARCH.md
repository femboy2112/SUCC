# Principia Observatoris — Observer-relative choice, T-actions and unpinnable history

**Date:** 2026-11-14. **Origin:** Leah's observer-relative AOC thesis following the pre-activation distinction axiom and ideal identity observer. **Interpretation:** AOC here means *Axiom of Choice* (AoC), with an operational refinement. A separate SUCC proposal uses the same abbreviation for *Adaptive Observer Closure*; the two must not be conflated.

**Scope:** finite, source-labelled causal systems and group actions; elementary paper proofs and exact finite controls. No claim to derive the global set-theoretic AoC, an arbitrary stochastic law, physical quantum mechanics, or Einstein dynamics.

## OC-1. Choice is not source-identification (CLASSICAL)

Let q:X→Y be a surjective observation map. AoC in Set is equivalent to the existence of a right inverse s:Y→X for each surjection, satisfying q∘s=id_Y. This is a *representative choice*, not a source-discovery procedure. The stronger identity s∘q=id_X holds only if q is injective. Indeed, if q(x)=q(x'), then s(q(x))=s(q(x')) would force x=x'. For finite X, a section can be constructed from any declared enumeration even without assuming global AoC. A representative may be different from the actual hidden state.

A category has identity morphisms; it does not generally have sections of all epimorphisms. A declared T-action (a monoid/group action, or another specified functorial structure) supplies *transport*, not an automatic selector, probability measure, or inverse causal history.

## OC-2. Finite nondisturbing operational-choice theorem (PROVED PAPER)

Let B_y=q^{-1}(y) be a finite nonempty source fibre. Let {p_i:X→O_i} be a finite family of total, repeatable, deterministic probes with source update t_i=id_X. The observer memory changes to record each output; the source state does not change.

**Theorem.** There exists a finite lawful probe schedule that identifies the actual x∈B_y for *every* possible x if and only if every distinct pair in B_y is separated by some allowed probe:

    ∀x≠x' in B_y, ∃i: p_i(x)≠p_i(x').

**Proof:** If no probe separates a pair, their entire adaptive output histories coincide, so no decoder distinguishes them. Conversely, select one separating probe for each of the finitely many unordered source pairs. Identity updates allow executing the resulting finite list on a single carrier without destroying earlier information. Its joint report E:B_y→∏O_i is injective and can be inverted by a finite lookup table. QED.

For a particular target P, source injectivity is unnecessary; exact target knowledge holds if and only if P is constant on each fibre of the *joint evidence* map E (existing SUCC target descent). This theorem does not automatically extend to infinite fibres, uncomputable probes, or disturbance. The four-state/two-bit exact example needs both independent readouts, while either alone merges states.

**Destructive control (inherited SUCC):** X={A,B,C}, probe a outputs 1 only on A, probe b outputs 1 only on B, and either probe resets all states to A. Counterfactual outputs jointly distinguish every initial state. Nevertheless a single-copy policy cannot determine the initial target 1_C: an a-first output 0 merges B,C; b-first output 0 merges A,C. Nondisturbing versions repair the defect. Our independent exact test replays this existing result.

## OC-3. Nontrivial T-action forbids equivariant point selection (PROVED COUNTEREXAMPLE)

Take G=Z/2 acting on X={a,b} by swap τ(a)=b, τ(b)=a. Let Y=X/G={*} carry the trivial G-action and q:X→Y be the orbit map. There are two strictly distinct source objects, a lawful nontrivial reversible T-action and no separating observer report (constant q).

Ordinary sections exist: s(*)=a or s(*)=b. But neither is *equivariant*: equivariance requires τ(s(*))=s(τ(*))=s(*), contradicting the absence of fixed points. Thus the unqualified claim "T-action exists, so a coherent source-respecting point choice exists" is **REFUTED**.

More generally, for a group acting on a set X with its orbit quotient Y=X/G and trivial quotient action, an equivariant section exists if and only if every orbit is a singleton: each selected representative would have to be fixed by the whole group. For finite orbits this requires no global axiom of choice. A general functor/monad denoted T does not, without additional definitions, repair this obstruction.

## OC-4. Strong versus weak stochastic sections (PROVED for finite group orbits)

For a finite G-orbit fibre F_y=q^{-1}(y), define the **uniform stochastic section**

    K(y,x)=1/|F_y| for x in F_y, and 0 otherwise.

Then q_*K=id_Y as a probability kernel. The action permutes each finite orbit, so K is G-equivariant. In the two-state swap example K(*,a)=K(*,b)=1/2, the unique invariant probability distribution on that orbit. Thus an invariant **randomized choice** exists even though an equivariant **deterministic** choice is impossible.

This is a mathematically precise, restricted *weak observer choice* principle: the observer can coherently maintain a distribution of compatible states without pinning actual source identity. A sample from that kernel need not be the hidden actual state. **The actual state need not be physically random.**

There is no unconditional probabilistic choice theorem for arbitrary actions: the shift action of Z on itself has no countably additive translation-invariant probability, because every singleton must receive the same mass c and the sum over all integers cannot equal one. Arbitrary probability weights require a declared prior, preparation law, likelihood or other additional structure.

With a finite prior μ on source histories Ω and evidence map E:Ω→Y, the posterior is

    Pr(γ | E=y) = μ(γ) 1[E(γ)=y] / Σ_{E(γ')=y} μ(γ'),

when the denominator is positive. Priors (1/4,3/4) and (1/2,1/2) with the same uninformative readout produce different posteriors. The existing [SUCC EODCS III PR #47](https://github.com/femboy2112/SUCC/pull/47) already formally distinguishes *possible successor supports* from probabilities: matching MAY/COMMON sets does not fix likelihoods.

## OC-5. Current state does not identify actual history (PROVED FINITE)

Two source histories γ_a=(a→c) and γ_b=(b→c) can have distinct origins and identical present states. Even a perfect classical nondisturbing probe of c has the same report in both cases. There is no evidence-based source-history selector unless the observer retained an earlier record, a source-marked history tag, or some authentic discriminating additional instrument.

The canonical description without probability is a set-valued compatible-history fibre E^{-1}(y). A posterior over that fibre is available only if a prior/likelihood is supplied. Even if a model has deterministic transitions, observer ignorance can still be probabilistic.

## OC-6. Identity observer is a reference, not omniscience (CLASSICAL CONDITIONAL)

A classical read-only probe updates source and observer jointly by (x,m)→(x,p(x)). The source update is id_X, but the composite update is not an identity because memory changes.

A quantum instrument whose sum of outcome operations equals the identity channel on *all* density matrices cannot extract information about an unknown state: each outcome operation is a nonnegative scalar multiple of the identity channel. Restricted commuting/pointer-state families do permit nondemolition information. Thus a physical “God observer” with T=id on every unknown quantum state is not automatically an informative observer.

## Ledger and next proof obligation

| ID | Verdict | Receipt | Boundary |
|---|---|---|---|
| OC-1 | Classical; proved algebraically | q∘s=id vs s∘q=id | AoC ≠ operational discovery |
| OC-2 | Proved finite nondisturbing | pairwise separation⇔finite list; four-state bit model | destructive single-copy probes violate composition premise |
| OC-3 | Literal action⇒equivariant selector REFUTED | two-point swap with no fixed point | arbitrary non-equivariant section exists |
| OC-4 | Proved finite group-orbit stochastic | uniform kernel and equivariance | no universal probabilities on arbitrary T-actions |
| OC-5 | Proved finite model | histories a→c and b→c | initial history not recoverable from c |
| OC-6 | Classical qualified result | identity quantum channel / CP instrument | restricted state families may behave differently |

**Validation:** ten exact standard-library Python tests in `observer_choice_probe.py`, independently rerunnable with `python observer_choice_probe.py`. The finite code checks positive/negative/mutation-style examples, not universal paper proofs; no full SUCC suite or Lean certificate claimed for this research-only package. No main, archived BBP source, or historical theorem changed.

**Next verdict-changing probe:** construct two initially distinct, causally related prepared sources with a declared T-action and identical post-activation readouts. Compare an identity probe, a destructive probe, and an independently calibrated history-marked probe. Determine the minimal executable distinguishing policy and whether the observational quotient supports a point section, a T-equivariant point section, a T-equivariant stochastic section, or only a set-valued relation. Include a hidden-history holdout and quantum noncommuting control. Keep source-map adequacy and all classical-vs-quantum premises explicit.
