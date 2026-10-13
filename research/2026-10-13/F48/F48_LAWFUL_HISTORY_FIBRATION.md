# F48: lawful histories, interface sheaves, and typed variance

**Initial independent phase; 2026-10-13.** Immutable parent:
`5eb09e7cba36ec01b8f9d6834b78b5766fd93935`; branch
`research/swm-f48-2026-10-13`. Only these new F48 files are modified.
Final acceptance requires the later independent swarm crucible.

## 1. Original question

Can original sources, changing carriers, actual records, observer models,
legal policies, proof supports, and ideal limits inhabit one mathematical
host without confusing their arrows? The faithful ambition is a composable
theory of lawful observation, rather than declaring every compatible report
family jointly executable. The gap is structural: which retained interface
makes gluing valid? Domain: explicitly declared mathematical transition
systems, possibly nondeterministic, with source/version contracts. Actual
physical authentication, cognition, and arithmetic sign conclusions are
outside this investigation.

## 2. Existing mathematical context

The [Stacks sheaf definition](https://stacks.math.columbia.edu/tag/00VL)
requires a unique glue for every matching cover family; its
[Grothendieck construction](https://stacks.math.columbia.edu/tag/02XU)
turns contravariant data into a split fibration. These are CLASSICAL.
[Abramsky–Brandenburger](https://arxiv.org/abs/1102.0264) distinguish event
sections and distributional global-section obstructions. That comparison
does not make carrier destruction a Bell theorem.
[Gogioso–Pinzani, The Topology of Causality](https://arxiv.org/html/2303.07148v2)
already show causal-function presheaves can fail sheafness. Their input-history
spaces differ from the fixed-run transition complexes below. The earlier
[definite-causality paper](https://arxiv.org/abs/2103.13771) is withdrawn and
explicitly identifies an inadequate definition; it is not an authority for
this construction. Scholarly novelty is UNVERIFIED.

## 3. Proposed SUCC objects

Fix original source set Σ, prepared carriers Q₀, preparation relation
P⊆Σ×Q₀, epoch-indexed carrier sets Qᵢ, outcome sets, and declared instruments
with branch tokens β and transition relation
Rₐ⊆Qᵢ×Oₐ×Qᵢ₊₁×Βₐ. Tokens preserve distinct causal choices even when endpoints
coincide. Add resource/contract state to Q when future legality depends on it.
Preparation is a root condition; a reset exists only as a declared instrument.

A public prefix h retains action names, outcomes, epochs and basis/source
contracts. H(h) consists of complete private lifts
(σ,q₀,β₁,q₁,…,βₙ,qₙ) satisfying P and every transition. Truncation
r:H(h′)→H(h) for h≤h′ is strictly compositional, giving a presheaf on the
prefix category. Its category of elements has arrows p→p′ precisely when
p=r(p′), and projects as a discrete fibration. A chosen future private lift
has a unique past; a past generally has multiple or zero futures.

The observer model M(h), complete endpoint belief
B(h)={(σ,qₙ):p∈H(h)}, and legal menu L(h) remain distinct. Require an action
enabled on every candidate current state, accepted by M, and within budget.
Offered menus are not free observations. A deterministic policy chooses an
action or termination from public h only. Reachable prefixes depend on that
policy; private σ is never a policy input.

## 4. Candidate theorem

**F48-T1, PROVED LOCAL (paper).** For every fixed typed public run h of length
n, form its incidence complex Kₕ: vertices v₀,…,vₙ and edges eᵢ with both
endpoints. Objects U are subsets closed under including an edge's endpoints;
arrows are inclusions; covers have union U. Define Fₕ(U) as assignments of
vertex labels (σᵢ,qᵢ) and branch tokens to included cells, with source equality
and the specified transition on every included edge, and preparation on v₀
when present. Then Fₕ is a sheaf and Fₕ(Kₕ)≅H(h). Cover gluing is the
equalizer universal property, not a promise that global sections exist.

**F48-T2, PROVED LOCAL.** A middle-interface report q:I→O can replace exact
middle-state equality for *every* pair of arbitrary typed transition
relations without admitting spurious joins iff q is injective. Compression
therefore requires a separately proved restriction on the relation class.

## 5. Proof attempt

For T1, matching sections agree on every shared vertex and edge token.
Their union defines one assignment. Every root/edge constraint belongs
to a covering member, so the union satisfies it. Every cell is covered,
giving uniqueness. Restriction identities and composition are literal
forgetting of assignments. This argument handles arbitrary covers and
parallel branch tokens. For adjacent intervals it gives the actual bijection
F(left∪right)≅F(left)×F(overlap)F(right).

For T2, injectivity makes equal q-reports imply equal interfaces, hence
lawful concatenation. Conversely choose distinct x,y with q(x)=q(y), left
relation {(a,x)} and right relation {(y,b)}. Their reported interfaces
match, but their exact fiber product is empty. This two-edge witness
refutes universal compressed-interface gluing. The proof supplies the
quantifiers; finite enumeration only checks its small-model implementation.

## 6. Crucible

The independent standard-library probe enumerates all 256 pairs of binary
edge relations and 1,024 local section pairs, comparing joins against a
separate enumeration of all global triples. Each exact compatible pair has
one glue. With left {(0,0)}, right {(1,0)}, and constant middle report,
both public local images exist and match, while the global image is empty.
Adding left (1,1) creates a genuine global path (1,1,0), but the coarse
local family (0,0,0) still cannot extend. Covers cannot cover an edge merely
by covering its vertices: each transition constraint must itself be covered.
Thus pointwise existential projection of this sheaf need not be a sheaf.
Sheafification would add an abstract glue, not an original-source history.

A nondeterministic P→L/R→Z has two private paths but one (σ,Z) endpoint
pair: endpoint beliefs support Markov control, but cannot faithfully replace
path objects or define their private truncations. Destructive bit probes
A(a,b)=(a,(a,0)), B(a,b)=(b,(0,b)) independently permit readings 1,1 on
prepared source 11; neither ordered one-carrier run returns both. A/B-first
opposite-parity shadows reproduce the baseline no-go. Nondestructive probes
repair it. No re-preparation is inserted.

## 7. Verdict

T1 SURVIVES as a source-conditioned interface theorem; T2 gives a minimal
REFUTED receipt for universal report-only gluing. The fibration is actual
mathematics, not an already complete sheaf on all observer worlds. Model
compression, instrument feasibility, mathematical proof authority, and
source realization retain independent gates. Tests have TESTED MODEL status;
no Lean/compiler or full suite was run. No theorem status is promoted by
the number of examples.

## 8. Remaining obstruction

For predicates, a restriction r:H(h′)→H(h) induces inverse-image r* and
adjoints ∃r⊣r*⊣∀r; exact fibers define existential/universal claims.
This transports old original-source predicates to longer histories,
without acquiring new premises. For expanding bit support A⊆B,
T_B⇒T_A and ¬T_A⇒¬T_B; T_A⇒T_B fails at a newly activated 1.
Changing carriers require the separate predicate square, for every branch.
Syntactic proofs additionally require a specified inference-preserving
translation, not just semantic truth tables.

Normalized stochastic kernels run forward and compose by summing intermediate
weights. Their support relation supplies no weights. Exact positive
full-support joint laws (1/4 each) and (3/8 on equal bits, 1/8 otherwise)
have identical fair marginals but disagree globally. Three pairwise fair
anticorrelations have no global joint law because three Boolean values
cannot all differ. Independence and probability gluing are separate premises.

## 9. Cross-domain connection with actual maps

Version-preserving source/current maps and branch-token maps preserving
preparation, transitions, and outcomes induce H(h)→H′(h), commuting with
truncation; their compositions induce the composed natural transformation.
On a fixed run they map cell assignments and commute with sheaf restriction.
Policy transport further needs reflected enabled domains and target labels;
one-way forward simulation alone is insufficient.

This adapts native `noncommuting_proof_transport`, `adaptive_proof_policy`,
`proof_backaction_debt`, `causal_nerode_succ`, and `eodcs_relational_choice`;
it changes none of them. The probability attachment is optional additional
data. For finite observation families F, the source-image stages X_F restrict
backward; their inverse limit is the product-topological closure of the
full trace image when outputs are finite discrete, as established in the
native VOYAGER dossier. Surjectivity from original sources requires closed
image, e.g. compact source with continuous reports. Eventual-zero streams
finitely realize the all-one profile but never globally realize it.
Conversely, coherent *private* path prefixes retain the same prepared σ;
they are not independently selected finite realizers. Neither mathematical
limit executes infinite elapsed observation or creates a finitary proof.

## 10. Deliverables

The accompanying probe and JSON receipt preserve exact witnesses, command
exit, immutable-parent equality and SHA-256 hashes of consulted source files.
The import manifest fixes archival origin
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`; archives remain untouched.
κ is mathematical contact only; φ is relative to declared probes; σ includes
the completeness premise; ρ warns against committing to one universal sheaf.
There is no operational phasor basis. Next falsification: independently
audit the incidence topology and test whether a restricted, proven
continuation congruence permits compressed gluing. Then reconcile the
reviewed swarm countermodels before final F48 acceptance.
