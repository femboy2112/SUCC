# SUCC Mathematical Atlas

This atlas organizes the 2026-10-13 many-worlds research swarm above VOYAGER.
The mathematical center is a declared source with lawful interventions, an
explicit record of original and current state, and proofs relative to that
source contract. Completion, inference, execution, and physical authentication
are distinct operations. A successful completion theorem does not supply a
reset, an unavailable experiment, or an authenticated source model.

Read [REGISTRY.json](REGISTRY.json) for all 48 assignments and their earned
statuses, [BRANCH_MAP.md](BRANCH_MAP.md) for the verified DAG, and the individual
numbered dossiers for definitions, proofs, prior art, hostile controls and next
obstructions. The dossiers use a ten-field contract. `SWM-*` claims supplement
the existing ledger; they do not renumber or promote historical claims.

## The architecture that survived

| Object or arrow | Exact type | Validity condition and meaning |
|---|---|---|
| Preparation | i:O→C | Original labels O remain explicit even when current states C merge. |
| Deterministic instrument | (e_a,r_a,U_a):C→Bool×R_a×C' | Availability, report timing and source-changing update are declared; an inaccessible action is not a free observation. |
| Actual history support | P(h)⊆O | Replay one ordered sequence of performed action/outcome events; prefix restriction retains original labels, not an inverse physical evolution. |
| Stochastic instrument | I_a:C→Δ(R_a×C') | Joint report/current law; the current state must include persistent latent memory. |
| Conditional belief | J_h∈Δ(O×C) | Update the joint law and retain O; normalize only on a positive-probability event. Marginals or support alone lose information. |
| Deterministic carrier quotient | q:C→D | Outcomes, enabled actions and updates commute; retain O and use preparation q∘i. Costs need an additional descent condition. |
| Source reindexing | f:X→Y | For all actions, fT_a=T'_af; original-target transport across f additionally needs target factorization. This differs from retaining O while quotienting only C. |
| Observational repair | I_A(R)=⋂_{w∈A*}(T_w×T_w)⁻¹R | Greatest stable equivalence contained in R, hence coarsest lawful refinement of the report. A coreflection under relation inclusion. |
| Observable algebra | q*:ℝ^D→ℝ^C | Invariant under every Koopman pullback exactly when q supports autonomous deterministic dynamics. |
| Completion | closure(tr(S))⊆O^W | Product topology, discrete reports; finite compatibility gives a completion point, with actualization exactly when the source image is closed. |
| Proof at h | target constant on nonempty P(h) | A deductive certificate for the declared source; empty support signals inconsistency. Stochastic positive-support certainty excludes zero-prior alternatives. |
| Policy | actual history→action or answer | A legal decision tree must preserve continuation opportunities; counterfactual branch intersections do not establish executable gluing. |

There is no universal sheaf theorem in this atlas. F48 constructs a genuine
presheaf over event prefixes and its discrete fibration. C17 constructs the
category of elements of an unconditioned stochastic pushforward functor and a
split **opfibration**. Their variance and normalization domains differ. Calling
both “source awareness” does not identify them. A topology for history descent
and a lawful stochastic comparison remain mathematical work to do.

## Strongest established steps

**Source repair and exact base change — kernel checked.** For arbitrary types
and a common alphabet of total actions, a strict intertwiner f gives
I_X(f*R)=f*(I_YR) for every relation R, without injectivity or surjectivity.
The repair is stable, deflationary and idempotent, and satisfies the right
adjoint law for stable relations. [A01](A01.md), [A06](A06.md) and
[the independent review](reviews/RA_AUDIT.md) give the hypotheses and limits.
The independent all-relation-lattice audit covered 986,718 action-pair/relation
cells on up to four states. Enumeration is bounded; the general base-change
and coreflection proofs are in `formal/Swarm_Repair.lean`.

**Actual topological completion — kernel checked.** [B09](B09.md) closes the
old formalization gap: finite-coordinate compatibility is precisely product
closure; source actualization for every compatible profile is precisely
closedness of the trace image; admissible coherent finite rows and compatible
profiles have mutually inverse continuous maps. Finite alphabets yield compact
completion, and a compact source with continuous coordinates realizes every
compatible profile. The isolated mathlib package pins both compiler and
library. These are classical topology results with an explicit SUCC interface.

**A fixed total causal policy on a compact continuous source has bounded
stopping depth — paper proof, compactness core kernel checked.** Terminal
history cylinders are open; pointwise finite termination gives an open cover;
a finite subcover bounds depth. Correct Boolean targets are clopen. The policy
history induction remains paper mathematics. [Root proof and three falsifiers](ROOT_POLICY_COMPACTNESS.md)
separate noncompact sources, discontinuous readouts and destructive information
loss. Clopenness does not guarantee that the available instruments can execute
a correct policy.

**Original-state histories survive lawful current-carrier quotients — paper
proof.** F48's all-history induction preserves original supports, target
homogeneity and robust policies when availability, outcomes and updates
commute. Cost preservation adds a cost hypothesis. The implementation checks
actual finite replay and refuses forged prefixes. Its history enumerator lists
existentially feasible event words; it is not a robust policy solver. See
[F48](F48.md) and its cross-domain review.

**Stochastic continuation needs the joint output — paper proof and exact
rational implementation.** [C17](C17.md) retains J(o,current), composes joint
instruments, and characterizes law descent by fiber constancy. [C20](C20.md)
proves readout simulation by source-independent garbling but refutes its use
as a continuation order. [C21](C21.md) proves the finite-horizon zero-error
expected-cost recursion and attainment. None of these probability statements
adds omitted zero-prior sources to a certainty claim.

**Finite memory and delay bounds — paper proofs with scoped kernels.**
[B16](B16.md) gives the exact smallest stationary autonomous generator for a
finite word w by minimizing μ+p over prefix-consistent eventual cycles.
An arbitrary-alphabet marker-exclusion state lower bound is kernel checked.
[D32](D32.md) proves sharp N−1 delay stabilization on a complete N-state
source; reconstruction of the original state still requires injectivity.
These are automata/partition-refinement facts, not evidence of physical
infinite computation or generic delay reconstruction by an arbitrary sensor.

**Arithmetic source authentication has a sharp phase-blind obstruction.**
[E36](E36.md) proves that the formal Dirichlet logarithm has prime-power support
iff the coefficient sequence is coprime multiplicative, including the correctly
quantified finite-prefix version. [E38](E38.md) supplies zeta coefficients and
the mutation a(6)=−1: their |a(n)|²-weighted valuation covariance is identical,
while the composite logarithmic coefficient is 0 versus −2. No classifier on
that covariance can authenticate this arithmetic property. The result blocks
a proposed input channel; it proves neither Weil positivity nor its failure.

## Counterexamples that changed the representation

| Failed shortcut | Exact witness | Surviving repair |
|---|---|---|
| Separately repair two action families once | Four-state A/B actions with a mixed-word separator, A06 | Joint word closure; exact one-pass criterion requires preservation of the other family's stable equivalences. |
| Pairwise local agreement entails global gluing | Binary triangle x=y, y=z, z≠x, A03 | A genuine global section test and a retained obstruction. |
| Abelian parity detects all transport obstructions | Even nonidentity S₃ holonomy, A04 | Full group action and fixed-point intersection. |
| Finite compatibility supplies an actual source | Eventual-zero streams admit the missing all-one limit, B09/B10 | Closed trace image or another proved actualization hypothesis. |
| A finite witness yields an effective uniform horizon | Computable halting-time source family, B11 | Enumerated effective refutation semidecision; silence stays unresolved. |
| Equal support determines probability | Same support, 1/4 versus 3/4 event probabilities, C17 | Exact joint law and provenance. |
| Equal one-step readout means equal future value | Read a while preserving b versus erasing b, C20 | Joint instrument/continuation simulation. |
| Reuse marginal likelihoods for correlated data | Duplicated report gives false wealth expectation 7/3, C23 | Conditional likelihoods under a calibrated path law. |
| Invisible filtered velocity has invisible nonlinear force | Two high Fourier modes differ by (1,0), D30 | Explicit unresolved stress; adding stress alone still needs a closure test. |
| A lossy factor preserves Conley-type information | H₀ rank 2 collapses to rank 1, D29 | Conjugacy or a proved invariant-specific transport theorem. |
| Gamma recurrence and integers uniquely choose Gamma | Periodic multiplicative correction, E37 | Additional analytic hypotheses and completion data. |
| Counterfactual branch overlap supplies execution | Destructive two-bit reads share original 11 but no ordered joint event, F48 | Actual history support and legal policy semantics. |

For D30, on T² take k=(N,1), l=(N−1,1), a=(1,−N), b=(1,−N+1),
and w=a cos(k·x)+b cos(l·x), N≥2. The spectral cutoff to |k|≤1 has Pw=0,
yet Leray div P(w⊗w)=(0,(2N−1)/2)sin(x₁). Thus pressure removal does not
kill the generator-level counterexample. No Navier–Stokes regularity claim is
being made.

## Classical mathematics, new SUCC results, and novelty

The atlas explicitly uses classical product topology, compactness, automata
minimization, relation coreflections, finite Markov kernels, Blackwell garbling,
belief-state dynamic programming, partial commutation, Koopman factors, strong
lumpability, Fourier filtering, Dirichlet convolution and group holonomy.
Re-deriving or kernel-checking these in SUCC is useful integration work, not
an academic priority claim.

Potential research candidates include the exact mixed-family repair criterion,
the particular simultaneous source-history/representation contracts, and the
specific cross-domain countermodels. Their priority is **UNVERIFIED**. A fresh
same-model agent and an independently written oracle provide procedural and
methodological separation, not independent human peer review. All finite
experiments are labeled as such; infinite statements rest on displayed proofs
or the exact named kernel declarations.

The sibling Heisenberg result was reproduced and challenged on characteristic
2, characteristic 5, zero coupling and a different dihedral family. The miner
still receives a supplied constructor grammar and complete finite transition
oracle. Opaque labels do not turn that into unrestricted mathematical concept
invention. [F41](F41.md)–[F43](F43.md) record the preregistration and holdouts.
