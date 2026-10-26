# Carrier-relative indistinguishability and target descent

**Research stage, October 25, 2026.** Pinned common parent: `461942c0bf616518e668d236d1c6b1596665a7dd` (draft PR #296). This companion to [Contextual Zero](CONTEXTUAL_ZERO_BACKBONE.md) and [Observer / Proof Access](OBSERVER_PROOF_ACCESS.md) develops the author's **indistinguishable-from-true-relative-to-carrier** idea without requiring complete hidden-state reconstruction. Classical mathematics is given explicit proofs; original scholarly priority is not claimed. These are declared mathematical models, not a theory of physical vacuum particles or a proof of pi normality.

## 1. The correction to the previous architectural requirement

The requirement that all observers jointly identify the entire hidden state was too strong. For a stated target, the correct condition is **target-relative separation**.

Let C be an admissible source class, let E collect specified observations, and write

$$x\sim_E y\iff E(x)=E(y).$$

An observation value is a class [x], not a uniquely reconstructed ontic state. A target P:C->Y is reconstructible from E exactly when

$$\boxed{x\sim_Ey\Longrightarrow P(x)=P(y).}$$

Equivalently, there is a unique function on the image of E such that

$$\boxed{P=\overline P\circ E.}$$

**Proof.** If the factorization holds, equal E-values give equal P-values. Conversely define the factor on a realized observation by the common P-value of its nonempty fiber. The hypothesis makes that definition independent of the representative. Nothing requires the fiber to be a singleton. The factor is defined on the **actual joint image**, not arbitrary unphysical tuples of eye readings.

This theorem does not say that agreement with some true model makes every unobserved claim true. For a Boolean target, a nonempty surviving fiber K has three distinct possibilities: P is identically 1 (identified true in the declared model), identically 0 (identified false), or takes both values (unresolved). An empty fiber is **INCOHERENT / OUT OF MODEL**, not a license for vacuous truth. A true representative and an observationally equivalent false representative prove target nonidentifiability for that toolkit.

The author's operational intuition is retained: once lawful observers cannot separate members of a class, no usable observation in that declared closure demands choosing one member. The quotient can be enough to act or prove an invariant. It is not necessary to recover details that the goal does not depend on.

### Two differently typed eyes; hidden identity remains free

The executable model has C={(x,y,h): x,y,h in {0,1}}. One eye reports 7+2x in unit A; another reports 3y-1 in unit B. The target is x XOR y. Both readings jointly determine the target but leave two possible values of h. The readings are neither numerically equal nor in the same unit. Their relation is justified by their common source. Every value of h is still available after target identification.

Joint realizability cannot be inferred from pairwise compatibility. On the even-parity carrier {000,011,101,110}, every pair of reports x=y=z=1 is separately realizable, but their triple is not. The implementation intersects all source fibers and refuses the empty intersection.

## 2. A matrix algebra of all lawful finite experiments

For a finite deterministic carrier C with n states, each instrument a has a source readout o_a and a total next-state function t_a. An instrument can disturb its source. Its output alphabet/chart and positive cost are explicit. Every finite word of instruments produces a transcript, with each output recorded before that instrument's transition.

Define x~y when **all finite words have the same transcripts** from x and y. This is also indistinguishability under every finite deterministic adaptive policy: until a transcript differs, the policy chooses the same next instrument. Conversely, a fixed word is a policy. This does not assert a reset is available.

Represent scalar functions on C as exact rational row vectors in Q^n. For each a, its transition pullback is a zero-one matrix acting as

$$T_a^*f(x)=f(t_a(x)).$$

Generate an algebra A from 1 and every readout indicator 1[o_a=v], closed under rational linear combinations, pointwise products, and all T_a^*. These are source-typed operations; it would be wrong to compare raw numerical outputs in unrelated eye charts as though they had identical meaning.

**Finite observer-algebra theorem.**

$$\boxed{\mathcal A=\{f:C\to\mathbb Q:f\text{ is constant on every }\sim\text{-class}\},\quad
\dim\mathcal A=|C/{\sim}|.}$$

**Proof.** Each seed is constant on behavior classes, and pullbacks preserve this because equivalent states have equal outputs and equivalent successors. Products and linear combinations preserve class constancy. Conversely, if two classes differ, some finite transcript separates them; a pulled-back readout indicator separates the corresponding states. For a fixed class, multiply finitely many separating zero-one functions (or their complements), one for each other class. This constructs its indicator. The disjoint class indicators span all class-constant functions and are linearly independent.

Thus target descent is an exact **row-span membership test**, but only after including nonlinear joint-observer products and future readout pullbacks. The pointwise products retain the correlations that ordinary scalar marginal comparisons discard. For the two-eye XOR example, a product adds the missing cross term; the algebra has dimension four, not eight. The inaccessible tag remains inaccessible.

The code supplies two independently implemented routes: stable partition refinement, and a rational linear-algebra closure with replayable row-construction recipes. Every added basis row records its readout, pullback or product origin. A verifier checks each recipe, independence, seeds and final closure. Its fingerprint binds the source transition/readout tables, not merely their names. A fingerprint verifies a declared model's bytes; it is NOT empirical source attestation.

This finite observation-algebra formulation is a source-typed application of classical behavioral equivalence / coalgebra and finite function algebras. It is not a claim to have invented those theories. See Rutten, *Universal coalgebra: a theory of systems*, CWI report CS-R9652, https://ir.cwi.nl/pub/4802.

## 3. Counterfactual joint knowledge is not always executable knowledge

There is a further boundary that matters for the author's physical-carrier intuition. A function can lie in the all-experiment observation algebra while no single-copy policy can discover it. Different eyes can interact with their common carrier destructively.

Take states A,B,C and two instruments:

| Instrument | Outputs on A,B,C | State after any output |
|---|---|---|
| a | 1,0,0 | A |
| b | 0,1,0 | A |

Every pair of initial states has a separating one-step experiment. The all-word behavior quotient is therefore discrete, and the observation algebra has dimension three. The Boolean target P=1[C] belongs to that algebra.

But **no single-copy policy can always identify P**, at any horizon. If the first instrument is a and the output is zero, B and C have become the same state A although their original target values differ. If the first instrument is b and the output is zero, A and C merge with opposite original targets. No subsequent experiment can repair either loss. The code returns a finite witness for each possible first action, which is an all-horizon impossibility certificate for this declared model, not just a finite-budget failure.

Changing only the interventions so that the two probes leave the state unchanged makes a two-step policy sufficient. A resettable copy would also change the access problem, but reset is **not** assumed by default.

The planner retains pairs (original state,current state) and branches on actual modeled outcomes. It minimizes worst-case cost within a finite budget. It never replaces the original target with the target of a reset state. Its independently implemented verifier executes the returned policy for every possible initial state. Failure by a finite budget is reported as such; it is not a universal impossibility claim.

This gives three separate obligations:

1. Is the target invariant under observational ambiguity?
2. Is there a lawful jointly executable policy that reveals it?
3. Are the declared source, tools, and readout semantics adequate for the intended actual source?

The first two are checkable in the finite model. The third is not obtained by simulation.

## 4. Optimal finite target error, rather than full-state error

For a nonempty finite fiber K and a real-valued target P, define its target oscillation

$$\omega_P(K)=\max_{x\in K}P(x)-\min_{x\in K}P(x).$$

The smallest worst-case absolute error of any scalar answer based only on this fiber is

$$\boxed{\inf_a\sup_{x\in K}|P(x)-a|=\frac12\omega_P(K).}$$

The midpoint attains this, while the two extreme target values force the lower bound. This gives an exact rational target-error certificate, even when many hidden source coordinates remain unknown. It is an error radius, **not a truth probability or a scalar TLICA score**.

Approximate similarity is not automatically an equivalence relation: at tolerance 1, 0 is close to 3/4 and 3/4 to 3/2, but 0 is not close to 3/2. Noisy versions should retain compatible fibers or pseudometric balls and exact error moduli; they must not silently take transitive closures that enlarge the tolerance.

Invertible changes of readout units preserve the observation partition when their codomains and comparison maps are transported. Merely writing identical numbers in two unrelated units does not establish agreement.

## 5. Completion can identify a target while leaving the carrier unresolved

**Compact target-completion theorem.** Let K_0 contain a nested family of nonempty closed sets K_n, with K_0 compact Hausdorff. Set K_infinity=intersection K_n. Let f:K_0->R be continuous. Then K_infinity is nonempty and

$$\boxed{\lim_n\max_{K_n}f=\max_{K_\infty}f,\qquad
\lim_n\min_{K_n}f=\min_{K_\infty}f.}$$

In particular, if f is constant on K_infinity, then the target oscillation tends to zero, **even if K_infinity has multiple or infinitely many states**.

**Proof.** Compactness gives a nonempty intersection and attained extrema. The maxima decrease to some L at least the maximum on the intersection. If a smaller intersection maximum existed, choose a threshold strictly between them. The closed sets K_n intersect {f at least threshold} nontrivially and are nested in a compact set, so their intersection is nonempty: contradiction. Apply the same argument to -f for the minima.

This is target completion, not whole-state identification. No algorithmic rate follows from bare compactness. An effective finite certificate needs a proved modulus for the target oscillation (or sufficient source-specific quantitative bounds).

On a compact inverse limit of finite discrete observer spaces, a continuous Boolean target factors through some finite stage: continuity supplies a cylinder around each point on which the target is constant; compactness gives finitely many such cylinders; a common refinement of their levels settles the target. This is the familiar clopen finite-observer phenomenon. It fails for discontinuous targets and does not assert that the requisite stage has a known computational bound.

Classical prerequisites: Stacks Project, compact finite-intersection lemma https://stacks.math.columbia.edu/tag/0059 and profinite finite-cylinder refinement https://stacks.math.columbia.edu/tag/08ZW.

### Why this does not trivialize pi normality

On the space of all radix-16 digit sequences, every finite prefix has periodic nonnormal extensions and normal extensions (prepend the fixed finite prefix to any normal sequence; finite changes do not change limiting block frequencies). Hence normality is not a continuous Boolean function of the prefix topology. Complete knowledge of the infinite digit sequence determines its normality as a mathematical property, but no finite prefix alone identifies it among arbitrary extensions.

That is a limitation of the **prefix-only observation class**, not a proof of unprovability or of ambiguity in the fully specified BBP sequence. The original zero-initial BBP law fixes its entire source. Sound algebraic and analytic theorem certificates can impose constraints much stronger than finite prefix matching; those are legitimate additional tools. The parallel pi research is trying to obtain exactly such an all-horizon signed estimate.

## 6. Two unequal analytic eyes can cancel their common divergence

A concrete carrier-completion instrument implements the author's units/eye analogy. Suppose a common source has

$$F(s)=a/s^2+b+R(s),\qquad 0\le R(s)\le C s^2$$

at s=t and s=2t. Neither a nor b needs to be known. Each eye sees a different divergent value. The exact paired contrast is

$$\widehat b_t=\frac{4F(2t)-F(t)}3
=b+\frac{4R(2t)-R(t)}3.$$

Therefore

$$\boxed{\widehat b_t-\frac{16Ct^2}3\le b\le
\widehat b_t+\frac{Ct^2}3.}$$

This interval has width 17Ct^2/3. It is sharp given only the two separate remainder inequalities: the extreme permitted residual pairs attain each endpoint. Exact outward intervals for the two eye readings are transported by the same signed linear contrast. No recovery of the full function R is required; the finite-part target is what becomes identified. Source-label or scale mismatches are rejected rather than freely equated.

For the authentic exponential Abel family

$$F(t)=\sum_{n\ge1}n e^{-nt}=\frac{e^{-t}}{(1-e^{-t})^2},$$

classical hyperbolic partial fractions imply the all-t estimate

$$\boxed{0<F(t)-t^{-2}+1/12\le t^2/240\qquad(t>0).}$$

**Derivation.** Put c_k=2 pi k. Differentiate the normally convergent partial-fraction expansion of coth(t/2), giving

$$F(t)=t^{-2}-2\sum_{k\ge1}\frac{c_k^2-t^2}{(c_k^2+t^2)^2}.$$

Since 2 sum c_k^{-2}=1/12, its remainder is

$$2t^2\sum_{k\ge1}\frac{3c_k^2+t^2}{c_k^2(c_k^2+t^2)^2},$$

which is positive and at most 6t^2 sum c_k^{-4}=t^2/240. Termwise differentiation is justified locally away from the poles by uniform convergence. The constants use the classical zeta(2) and zeta(4) evaluations. Source: NIST DLMF 4.36.3, https://dlmf.nist.gov/4.36, and zeta special values https://dlmf.nist.gov/25.6.

The executable instrument encloses e^{-t} with rational alternating Taylor sums and then applies monotonicity of q/(1-q)^2, for 0<t<=1. It uses two scale readings and the proved residual cap to enclose the classical finite part -1/12. This is a **calibration and finite realization of a known analytic result**, not a new derivation of zeta regularization from no premises. The ordinary positive series remains divergent. The counterterm and common scale are essential.

## 7. Matrix targets already have nontrivial quotient structure

In the internal Fourier matrix research, rotating every observed phase by a gives

$$A_{N,H}^{(a)}=D_a A_{N,H}D_a^*,\qquad
\operatorname{tr}[(A_{N,H}^{(a)})^2]=\operatorname{tr}(A_{N,H}^2).$$

Thus spectral purity descends to the quotient by the unobservable global phase origin. We do not have to reconstruct that origin to bound purity. Native integration tests verify this using the actual original BBP rational states and the repo's exact phase algebra.

But the target's descent under this gauge does not establish the desired all-horizon purity bound. The larger question is whether a specified collection of *source-justified arithmetic constraints* controls the target oscillation or an upper envelope of the remaining signed innovation. In the separate PR #298, conductor-growth steps have a proved vanishing contribution while the conductor-flat signed sum remains open; that is a target-specific reduction, not complete recovery of every hidden phase.

Do not import PR #297/#298 conclusions on the authority of their discussion alone. Their source, domain, proof and validation remain separately reviewable. This branch does not modify either concurrent workstream.

## 8. TLICA diagnostics and status boundaries

The implementation never computes a universal truth score. Keep distinct: contact kappa; toolkit-relative truth-indistinguishability/pathway phi; source-map adequacy sigma; identity coupling rho; probe availability mu; closure of tools; independence; and discrimination. High agreement inside a wrong source model does not certify sigma. A currently unavailable execution path is not a false mathematical statement. A finite-budget failure is not an impossibility theorem.

Classical propositions proved above: target factorization, finite observer-algebra completeness, bounded exact policy recursion, the destructive-access counterexample, minimax target radius, compact target completion, finite-stage Boolean continuity, and the two-scale residual certificate. The finite code checks declared rational models; it does not certify physical instrumentation, absolute ontology, pi normality, RH, or a new theory of quantum vacuum phenomena.

**The corrected SUCC principle:** preserve an admissible equivalence class of sources; prove that the desired target is invariant on it (or has controlled oscillation); separately establish an executable access path and justified boundary completion. Full hidden-state reconstruction is optional unless the target itself demands it.
