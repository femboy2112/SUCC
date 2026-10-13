# SUCC Mathematical Atlas

This atlas organizes the 2026-10-13 many-worlds research swarm above VOYAGER.
The mathematical center is a declared source with lawful interventions, an
explicit record of original and current state, and proofs relative to that
source contract. Completion, inference, execution, and physical authentication
are distinct operations. A successful completion theorem does not supply a
reset, an unavailable experiment, or an authenticated source model.

Read the [mission index](MISSION_INDEX.md) and [REGISTRY.json](REGISTRY.json) for all 48 assignments and their earned
statuses, [BRANCH_MAP.md](BRANCH_MAP.md) for the verified DAG, and the individual
indexed dossiers for definitions, proofs, prior art, hostile controls and next
obstructions. The dossiers use a ten-field contract; B09–B16 combine related
fields under shared headings and state their verdicts in the opening metadata.
`SWM-*` claims supplement
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
both “source awareness” does not identify them. X05 supplies a sufficient
stochastic continuation comparison and X07 relates forward measures to backward
support. A topology and a general gluing theorem for history descent remain open.

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

## Ranked unresolved obstructions and the next decisive checks

| Rank | Missing statement | Smallest useful proof or falsifier |
|---|---|---|
| 1 | Compress actual history into a finite controller without losing original-target support or future options | Characterize equivalence of two history beliefs by every authorized continuation; find two identical current endpoints with different original support, then test a proposed finite congruence. |
| 2 | Characterize policy comparison, beyond sufficient instrument simulation squares | A finite pair with value domination for every target/prior/horizon but no common carrier intertwiner/report garbling would prove strictness of X05's sufficient criterion. |
| 3 | Give a genuine sheaf/site theorem for lawful causal histories | Declare covers and a concurrent diamond condition; prove existence and uniqueness of lawful amalgamation. Destructive two-bit histories are a mandatory negative control. A presheaf name alone closes no gap. |
| 4 | Fully formalize policy-cylinder semantics and finite-coordinate recovery | Add Lean action/history replay induction to the compact stopping core; formalize X01's compact disagreeing-pair proof. Neither is claimed by the current scoped files. |
| 5 | Bound closure error under adaptive source-changing policies | Replace D27's fixed δ by validated per-history/action defects and prove an accumulated path-law bound while retaining original indices; test adversarial latent-memory omission. |
| 6 | Source-faithful finite closure for a continuum generator | Specify an invariant source class and report r; test whether Dr(u)X(u) is constant on each r-fiber and prove the regularity needed for a flow factor. The LES and finite-jet counterexamples forbid generic shortcuts. |
| 7 | Arithmetic covariance → actual completed Weil/Suzuki pairing | Construct the exact source-derived operator, Gamma/pole completion, conductor/phase and test-function transport, then defeat the matched phase/composite mutations. Covariance authentication already fails; this bridge remains blocked. |
| 8 | Broad renormalization and genuinely expanding discovery grammars | Name one new typed constructor with a semantic checker and inherited counterexamples; independently test a source family outside the supplied grammar. F42 does not implement unrestricted concept invention. |

The three broad requested destinations still explicitly blocked/open are D26's
general renormalization bridge, E38's completed Weil identification, and F48's
universal history sheaf. F42's unrestricted constructor invention remains a
conjectural extension. Their investigations are complete for this round; the
dossiers give the surviving narrower theorem and exact next obstruction.

RH-facing arithmetic work here is diagnostic: formal Euler-log source gates,
phase-aware countermodels, finite Gamma defects and authentic finite Gaussian
components. It uses no nontrivial zero locations as construction inputs and
does not establish a completed positive Weil form or an RH advance.


## Second-generation bridges

Each row is a separately dispatched research assignment after the initial
cohorts. The universal statements are paper proofs unless the last column names
a narrower kernel-checked scope. Exact finite controls are linked in the dossier.

| Bridge | Actual construction or new boundary | Status |
|---|---|---|
| [X01](X01.md) Repair × completion | Continuous completion transport; source-surjective plus completion-injective maps reflect actualization. A completion homeomorphism alone does not. | Paper proof; transport and reflection core kernel checked |
| [X02](X02.md) Holonomy × stochastic transport | Invariant law sections form orbit simplexes. A global random point section requires support on common fixed points, a strictly stronger condition. | Paper proof |
| [X03](X03.md) Gluing × typed CEGIS | Original-retaining maps pull back section sets; source-verified obstruction cores survive grammar extensions. Grammar-relative cores need a coverage gate. | Paper proof; corrected after fresh audit |
| [X04](X04.md) Memory × symbolic chaos | A no-dead-end m-word language has a minimal cardinality(L) stationary surrogate; finite-horizon coverage generally supplies no source factor. | Paper proof |
| [X05](X05.md) Blackwell × adaptive policies | Joint instrument squares with an unsampled stochastic carrier intertwiner transport original-history laws and dominate finite-horizon policy cost. | Paper proof |
| [X06](X06.md) Resource geometry × memory | Exact weighted fiber composition; a known finite deterministic chain needs a reusable buffer of final maximum-fiber rank, with original-access and reachable-image conditions. | Paper proof |
| [X07](X07.md) Joint laws × causal partial orders | Outcome diamonds descend unnormalized original/current measures to traces; normalization is partial; original support is contravariant. Posterior equality alone loses likelihood. | Paper proof |
| [X08](X08.md) Prime clocks × action repair | Successor repair on cyclic clocks absorbs every affine dilation, while quotient actions can remain noncommutative. | Paper proof; natural affine-stability lemmas kernel checked |
| [X09](X09.md) Analytic completion × actualization | Closed coefficient-bounded holomorphic sources realize approximately compatible finite value reports. Unbounded interpolation and nonclosed polynomial sources fail separately. | Paper proof |
| [X10](X10.md) Koopman × universal repair | On finite sources the least invariant unital observable algebra is the full function algebra of the repaired quotient. Invariant linear span alone can be smaller. | Paper proof |
| [X11](X11.md) Partial evidence × proof limits | Finite-support certificate presentation and Scott-open positive properties; effective enumeration is an additional gate and limit truth need not have finite support. | Paper proof |
| [X12](X12.md) Histories × representation updates | History-indexed quotient changes preserve original supports through cross-stage squares. Individually valid static quotients cannot be switched arbitrarily. | Paper proof |

The most coherent common construction now has three layers: forward weighted
history evolution, backward original-support restriction, and representation
comparisons commuting with the actual instruments. X07 supplies the first two;
X05 and X12 give distinct stochastic and deterministic comparison theorems.
This is a defensible combined architecture. It does not yet supply the site,
covering families or gluing theorem required for the full F48 sheaf target.

## Execution, independent review, and validation

All **48 first-generation missions and 12 cross-domain assignments** completed
their investigations and were integrated. There were **21 genuine child agents**:
six cohort investigators, each owning eight missions; twelve independently
dispatched synthesis investigators; and three fresh adversarial reviewers.
The principal performed integration. This is not a claim of 48 independently
spawned investigators, independent human peer review, or 60 proved conjectures.
No assignment is unfinished; the three broad targets named above remain open.

| Review | Scope | Verdict and retained correction |
|---|---|---|
| [RA](reviews/RA_AUDIT.md) | Category repair, base change, beliefs and report comparisons | Scoped claims survived. Invalid actions must be rejected before empty-support filtering; fixed with a regression. Independent relation proofs compiled in Lean. |
| [RX](reviews/RX_CROSS_BRIDGES_AUDIT.md) | X01, X04, X05, X08, X10, X12 | Scoped bridge theorems survived fresh exact controls and hypothesis attacks. |
| [RY](reviews/RY_AUDIT.md) | X02, X03, X06, X07, X09, X11 | Two substantive scope corrections independently verified: X03 source-wide cached cores need source certification; X07 deterministic-history recovery needs deterministic preparation. The stronger counterclaims remain refuted. |

The final local integration passed **1,816 tests**, reproduced **18 exact
cohort/bridge receipts**, and verified **72 provenance items**. Both required
foundations and ordinal probes completed. **Seven new Lean modules** compiled
with Lean 4.14.0; the topology package pins mathlib at
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. The eight baseline EODCS modules
remain unchanged. A separate own-source guard rejects proof placeholders and
local axioms; it does not prohibit mathlib's standard classical foundations.
See [FINAL_VALIDATION.json](FINAL_VALIDATION.json) for source fingerprints,
commands and raw logs, and [FINAL_KERNEL_RECEIPT.json](FINAL_KERNEL_RECEIPT.json)
for exact file hashes and the limited formal scopes.

The final X07 correction added one test after the first 1,815-test pass; the
complete suite was rerun. Receipt collection also exposed an empty refreshed
X03 JSON file, which was regenerated before all eighteen comparisons passed.
These are recorded execution failures and recoveries, not omitted successes.

[Draft PR50](https://github.com/femboy2112/SUCC/pull/50) is based on VOYAGER;
its description records final-head CI and the published checkpoint. The branch
map distinguishes investigator commits from connector-created publication
commits, whose trees are checked for equality. Main, archival provenance,
release state, and existing defaults were not changed. PR45 remains a sibling,
with its theorem-by-theorem comparison retained in [F41](F41.md).
