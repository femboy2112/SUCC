# NO-GHOST: primary-literature audit and novelty boundary

**Status:** primary-source comparison, not an academic-priority claim. Retrieved
2026-10-13. Repository work began at commit
`9e7589e522aff990189aa8a14f6ee2fa5a28dd81`, on the separate
`research/no-ghost-causal-gluing-2026-10-13` branch. Read `AGENTS.md` and
`docs/METHOD.md` before writing. This file does not change the status of an
existing SUCC result.

## 1. Verdict that must constrain the manuscript

The general ideas **causal histories as presheaves**, **causal sheaf failure**,
**cube conditions for asynchronous execution**, **probabilistic event structures**,
**marginal feasibility**, and **policy information constraints** already have
substantial primary literature. Source-indexing alone does not establish novelty:
an immutable source can be represented by a parameter, initial variable, or an
unchanged wire in those formalisms.

The defensible contribution of this research round is therefore a finite,
explicit, source-relative synthesis and independently checkable obstruction
implementation, plus whatever particular refinement the accompanying proofs
actually establish. A new theorem about composing legal repairs, a new exact
decomposition respecting source and information restrictions, or an equivalence
with existing causal presheaves could become academically interesting. Such a
claim requires further comparison and proof.

One correction is especially consequential: a probability distribution supported
on executable paths need not itself be obtainable from the declared stochastic
instruments and public policies. **Support, fixed-kernel dynamics, and allowed
information are three different restrictions.** The operational feasibility
theorem must say which of them it certifies.

## 2. The five required sources

### [AB] Abramsky and Brandenburger

[The Sheaf-Theoretic Structure of Non-Locality and Contextuality,
arXiv:1102.0264v7](https://arxiv.org/pdf/1102.0264v7).

Read the full-paper text, especially §§2–4, §6, §8. The event presheaf consists
of outcome assignments and is a sheaf (§2.2, p.5); distributions form a presheaf
whose restriction is marginalization (§2.3, pp.5–6). Measurement covers already
encode which sets of measurements are jointly performable (§2.4, p.6).
Proposition 4.1 (p.12) identifies solutions of the augmented incidence-matrix
system with global distributions. Theorem 8.1 (p.23) equates global sections
with factorizable hidden-variable realizations.

**Boundary for SUCC:** changing columns from all assignments to declared legal
histories is a useful specialization of incidence-matrix feasibility. It is not
a new Farkas theorem, and the global assignment in this literature must not be
misreported as a performed experiment. The stronger SUCC question is whether a
matching is supported by its specified preparation, transitions, and policy.

### [GP-T] Gogioso and Pinzani

[The Topology of Causality,
arXiv:2303.07148v2](https://arxiv.org/pdf/2303.07148v2).

Read §§2.2–2.5 and the proofs in §2.7. Theorem 2.26 (p.28) relates causality to
continuity. Definition 2.22 and Theorem 2.30 (p.29) give a separated presheaf of
causal functions: a compatible family glues precisely when its compatible join
is causal. The explicit failure on p.30 has contexts with no common input
history but incompatible outputs at the same tip event. Theorem 2.34 (p.31),
assuming at least two outputs per event, characterizes sheafhood by absence of
solipsistic contextuality; tightness is sufficient. Proposition 2.35 (p.32)
gives a naturally isomorphic extended-function presentation.

**Boundary for SUCC:** this is the nearest prior art to a proposed causal
no-ghost descent theorem. It already separates compatible local data from a
globally causal function. A claimed extension must compare the actual sites,
restriction maps, source labels, and instrument contracts. Its theorem does not
automatically validate SUCC's physical realization interpretation.

### [GP-G] Gogioso and Pinzani

[The Geometry of Causality,
arXiv:2303.09017v2](https://arxiv.org/pdf/2303.09017v2).

Read §§2.1–2.4 and §2.8. Definition 2.12 (p.21) specifies causal marginal
equations; Definition 2.13 (p.22) intersects their solution space with a product
of probability simplices. Theorem 2.25 (p.23; proof §2.10.16) identifies the
resulting causaltope with the empirical-model space. §§2.2 and 2.4 formulate
linear programs for supported components and causal decompositions. The
introduction (p.4) distinguishes these convex constructions from constraints
involving independent common sources, whose correlation spaces can fail to be
convex.

**Boundary for SUCC:** causal polytopes and exact linear causal restrictions
already exist. Fixed original preparations, concrete kernels, observation
quotients, and allowed public policies supply additional model-specific
constraints; their mere presence does not establish priority. Do not claim an
arbitrary causal correlation is realizable by a particular laboratory carrier.

### [F] Fritz

[A Synthetic Approach to Markov Kernels, Conditional Independence and Theorems
on Sufficient Statistics,
arXiv:1908.07021v8](https://arxiv.org/pdf/1908.07021v8).

Read §§2–4, §11, §§14–16. Markov categories supply compositional probability
semantics; §4 gives kernels. Proposition 11.17 (p.48) proves disintegration
under existence of conditionals. Definition 14.3 (p.84) defines sufficiency by
a reconstruction witness. Lemma 14.4 (p.85) proves composition of sufficient
statistics; Theorem 14.5 adds a characterization under strict positivity.
Section 16 treats minimal sufficiency relative to an informativeness preorder.

**Boundary for SUCC:** retaining an original-source wire and proving a
kernel-composition identity are classical constructions. SUCC's concrete
future-availability and proof-support predicates must be stated separately;
statistical sufficiency of a quotient is not automatically sufficiency for
every future intervention. A conditional kernel that exists mathematically
also is not automatically an available experimental instrument.

### [CCRW] Castellan, Clairambault, Rideau, and Winskel

[Games and Strategies as Event Structures,
arXiv:1604.04390](https://arxiv.org/pdf/1604.04390), retrieved LMCS 13(3:35)
(2017), pp.1–49.

Read §§2–4. Theorem 3.20 (p.31) characterizes strategies using courtesy and
receptivity, equivalently discrete-fibration conditions on configurations.
Section 4 constructs the bicategory of concurrent games. Lemma 4.9 (p.38)
is a zipping lemma for hiding and interaction; Lemma 4.13 (p.41) checks a
unitor coherence diagram through the actual configuration maps.

**Boundary for SUCC:** concurrency with private events, hiding, lawful
composition, and explicitly proved coherence is established mathematics.
The relevant comparison is with maps on event occurrences and configurations,
not merely endpoint reports. A source-preserving refinement must show exactly
which hypotheses or witnesses are added. Calling the result a new category of
causal histories without that comparison would overstate its scope.

## 3. Directly relevant additional prior art

### [MM] Melliès and Mimram: asynchronous cube and coherence laws

[Asynchronous Games vs. Concurrent Games, author
manuscript](https://www.irif.fr/~mellies/papers/asynchronous-concurrent-journal.pdf).
Also inspected the earlier [Asynchronous Games: Innocence Without
Alternation](https://www.irif.fr/~mellies/papers/MelliesMimram07.pdf).

The journal manuscript §1.4, Definitions 1–2 (pp.11–12), distinguishes the cube
property from a further coherence property for asynchronous tiles.
Proposition 5 (p.13) reconstructs an event-structure configuration graph from
a rooted, simply connected asynchronous graph satisfying both. Corollary 6
relates homotopy classes of paths to linearizations; its surrounding text says
the corollary does not need the additional coherence property. Their proof
discussion uses distributive intervals and Birkhoff representation (p.14).

**Boundary for SUCC:** the need for compatibility beyond individual interchange
tiles is established. SUCC's chosen fiber bijections introduce another level:
equality of composite comparison *maps*, not just existence of tiled paths.
Identify this distinction explicitly rather than claiming the generic cube
obstruction is newly discovered. The authors themselves trace the cube
condition to earlier concurrency research.

### [ES] Earnshaw and Sobociński: categorical trace semantics

[String Diagrammatic Trace Theory,
arXiv:2306.16341v1](https://arxiv.org/pdf/2306.16341v1).

Definitions 12–13 (§4, p.6) define a trace monoid by quotienting words by swaps
of independent letters. Lemma 21 (p.8) and Theorem 22 (p.9) compare this with
endomorphisms in the appropriate free prop and identify the corresponding
language classes. Theorem 31 (p.11) recalls Zielonka's recognizable-trace
characterization by asynchronous automata.

**Boundary for SUCC:** schedule independence of a semantics respecting the
generating interchange relations is the quotient's classical universal
property. A state/history-dependent independence relation requires a typed
asynchronous structure, not an unqualified application of one fixed trace
monoid. Preservation of the full source/receipt law is a concrete choice of
semantics to which the quotient argument can be applied.

### [CW] Cattani and Winskel: presheaves of computation paths

[Presheaf Models for Concurrency, BRICS RS-96-35
(1996)](https://www.brics.dk/RS/96/35/BRICS-RS-96-35.pdf).

Read §§1–3 and the event-structure model discussion. The paper develops
presheaf semantics on path categories, relates traditional concurrency models
to these presheaves, and studies preservation of open maps and bisimulation
by operations. Theorem 18 (printed p.14; PDF p.18) compares the denotational
operations with event-structure interpretations.

**Boundary for SUCC:** a presheaf whose elements are private executions and
whose maps forget portions of a path is not novel merely because it is a
presheaf. A useful contribution must justify why the chosen restrictions are
defined on actual histories and why they preserve the source/ancestry data.

### [W] Winskel: probabilities on event structures

[Distributed Probabilistic and Quantum Strategies, MFPS 2013 author
manuscript](https://www.cl.cam.ac.uk/~gw104/mfps13-probstrats.pdf).

Definition 3.3 (p.6) uses nonnegative inclusion-exclusion drops to characterize
configuration valuations. Theorems 3.4–3.5 (p.7) extend them to continuous
valuations and probability measures. Section 4.2 (p.11) makes a race-freedom
restriction explicit because unspecified rates do not determine race outcomes.
Theorem 4.8 (p.16) gives a bicategory of race-free games with probabilistic
strategies.

**Boundary for SUCC:** source-supported weights on concurrent configurations
and probability-preserving strategy composition have predecessors. The
declared instrument/rate contract is load-bearing; concurrent conflict cannot
be repaired by silently inserting a stochastic scheduler. The finite
certificate engine is a practical specialization rather than a replacement
for this semantics.

### [KMS] Koller, Megiddo, and von Stengel: policy information restrictions

[Efficient Computation of Equilibria for Extensive Two-Person Games,
Games and Economic Behavior 14 (1996), 247–259, author
PDF](https://ai.stanford.edu/~koller/Papers/Koller%2Bal%3AGEB96.pdf).

Section 2 (journal pp.249–250; PDF pp.3–4) defines information sets, perfect
recall, and realization plans. The constraints normalize the empty sequence
and conserve probability across choices at each information set. The paper
explains reconstruction of behavioral probabilities by ratios on
positive-mass sequences and arbitrary choices on zero-mass ones. This is the
primary sequence-form comparison used here; the companion von Stengel paper,
*Efficient Computation of Behavior Strategies*, DOI
10.1006/game.1996.0050, was located, but its full text was not successfully
retrieved in this run.

**Boundary for SUCC:** encoding what a policy knows is classical. An LP over
individual terminal trajectories discards that information constraint unless
it is restored. A policy-column or suitable sequence-form implementation is a
correct operational refinement, not a newly discovered policy-polytope theorem.

### [AMB] and [C]: cohomology is not generally complete

[Abramsky, Mansfield, and Barbosa, The Cohomology of Non-Locality and
Contextuality, arXiv:1111.3620](https://arxiv.org/pdf/1111.3620).
Proposition 4.3 (p.6) supplies a sufficient nonvanishing obstruction; §5
exhibits a Hardy example where the obstruction vanishes without the required
support extension. A compatible family of formal integer combinations need
not be an actual section.

[Carù, On the Cohomology of Contextuality,
arXiv:1701.00656](https://arxiv.org/pdf/1701.00656).
Section 4 (PDF pp.7–8; printed pp.27–28) gives a strongly contextual
counterexample on a symmetric, connected `(2,2,4)` Bell-type scenario that
still evades the obstruction. Its explicit model appears in Appendix A.

**Boundary for SUCC:** an abelianized or scalar diagnostic cannot be promoted
to a complete global-gluing characterization. The complete finite check may
be a constraint/coupling problem even when cohomology offers useful partial
certificates. Nonabelian comparison-map holonomy and these abelian
contextuality obstructions are different constructions.

### [Stacks]: descent data versus effectiveness

[Stacks Project, Definition 8.3.1, tag
026B](https://stacks.math.columbia.edu/tag/026B), and [§8.5, tag
02ZH](https://stacks.math.columbia.edu/tag/02ZH), read 2026-10-13.

Descent data include specified isomorphisms on double fiber products satisfying
a cocycle condition on triple fiber products. Stack-in-groupoids conditions
separate descent of isomorphisms from effectiveness of object descent.

**Boundary for SUCC:** pairwise isomorphisms, cocycle coherence, and existence
of a global object are distinct requirements. A stackification supplies a
formal effective completion relative to its site; identifying the new objects
with admissible physical histories requires a separate realization theorem.
For a nonregular cover, deck invariance must not substitute for full
fiber-product descent data.

## 4. A necessary operational correction, proved directly

These examples and the lemma below are elementary reconstructions for this
audit. They are **PROVED LOCAL** mathematical observations, with no priority
claim.

### 4.1 Support is weaker than fixed dynamics

Take a single stipulated fair-coin instrument with source-independent outcomes
`0` and `1`. Both trajectories are lawful and have positive evidence.
Consequently a support-only simplex allows the point mass on outcome `0`.
The fixed instrument produces probability `1/2`, so that point mass is not an
unconditioned output law of the declared experiment. Conditioning or rejection
sampling would change the contract and must be represented explicitly.

### 4.2 Even the correct source marginal does not remove hidden-state access

Let the original source be an unobserved fair bit `S`. At one public information
state the observer chooses a guess `G` in `{0,1}`. All four pairs `(S,G)` can
occur under some legal blind policy. The coupling

\[
p(0,0)=p(1,1)=\tfrac12,\qquad p(0,1)=p(1,0)=0
\]

has legal support and the correct source marginal. But an allowed policy has
`Pr(G=0 | S=s)=q` for both source values, because it cannot read `S`. Therefore

\[
\Pr(G=S)=\tfrac12q+\tfrac12(1-q)=\tfrac12,
\]

whereas the proposed coupling has success probability one. This is a
policy-information obstruction, not a source-support obstruction. It persists
under any private random seed independent of `S`.

### 4.3 Exact finite policy-column repair

Fix a finite horizon, source preparation, all transition kernels, finite public
information histories, and enabled action menus. Assume perfect recall of the
public history. Let `Pi` be the finite set of deterministic public-history
policies and let `v_pi` be the resulting exact trajectory law, computed using
the declared kernels. Source labels may enter kernels but never a policy's
input. If source-independent random selection and retention of a policy is
allowed, the operational laws are exactly

\[
\operatorname{conv}\{v_\pi:\pi\in\Pi\}.
\]

**Proof.** Randomly selecting policy `pi` with weights `lambda_pi` directly
produces `sum lambda_pi v_pi`. Conversely, a randomized public-history policy
can have its action randomizations sampled for every possible public history
before execution, independently of the source and instrument noise. Each
complete sampled action table is a deterministic public policy. Because a
public history in the finite tree is visited at most once, this construction
reproduces every conditional action probability and hence every trajectory
probability. Grouping sampled tables by their deterministic policy gives the
convex representation. The same conclusion is immediate for a permitted
retained random seed by conditioning on it. ∎

For a report-marginal map `A`, operational compatibility is therefore
`A V lambda = b`, `lambda >= 0`, `sum lambda = 1`, where the columns of `V`
are **laws** of policies, not bare paths. Rational inputs give rational columns.
Finite LP/Farkas alternatives apply. The conclusion is conditional on the
declared randomization resources; it does not authorize a new sensor, memory,
reset, source-dependent seed, or postselection. With restricted memory,
imperfect recall, or independent distributed policy agents, a different policy
class may be required, and convexity must be checked rather than assumed.

This lemma is classical mixed-policy semantics. Its role here is to prevent a
specific overclaim in the proposed source-supported gluing theorem.

## 5. What this round may and may not call new

| Result under consideration | Defensible classification |
| --- | --- |
| Dirac-preparation test for equality of finite labelled kernels | Classical linearity, reconstructed for source/receipt types |
| Adjacent-swap invariance of distribution semantics | Classical trace/rewriting argument with SUCC-specific hypotheses |
| Chosen branch bijections can fail braid coherence | Classical coherence phenomenon; concrete lawful model may be new to SUCC |
| Unique lift/common faithful history representation forces coherence | Standard uniqueness/naturality mechanism, to be proved for the chosen model |
| Complete-constraint incidence gluing | Existing SUCC/F48 baseline and ordinary constraint descent |
| Causal presheaf can fail to be a sheaf | Already explicit in [GP-T] |
| Source-supported marginal LP and Farkas certificate | Classical finite convex feasibility with restricted atoms |
| Support-feasible but policy-impossible coupling | Classical information restriction; essential correction to engine scope |
| Exhaustive finite repair search | Exact bounded optimization; novelty requires structural insight beyond enumeration |
| Multiple incomparable lawful repairs | Elementary order-theoretic no-go; useful SUCC regression example |
| Integrated engine preserving source, receipts, policy, and coherence certificates | Potentially useful research software; academic originality unestablished |

The smallest potentially verdict-changing next result is a **non-tautological
decomposition theorem**: identify a useful class of causal covers for which
locally certified, source-preserving, policy-compatible factors can be glued
without enumerating all global histories or all policies. Its hypotheses must
control separator memory, information flow, executable interfaces, and chosen
transport coherence. It must also distinguish itself from junction-tree,
event-structure, and sequence-form decompositions. No such novelty theorem is
certified by this literature audit alone.

## 6. Retrieval provenance and limitations

All five required papers were retrieved as complete PDFs and converted with
`pdftotext -layout`. The load-bearing sections listed above were inspected;
the abstract alone was not used as evidence. Rendered PDF pages were also
inspected for [GP-T] p.30 and [CCRW] p.41, where causal/coherence diagrams
matter. Additional full texts were retrieved for [MM], [ES], [CW], [W],
[KMS], [AMB], and [C]. Third-party PDFs are not redistributed in this patch.

The SHA-256 hashes below identify the bytes inspected. Unversioned links can
change; hashes are therefore more precise than claiming a latest-version
audit. The review is substantial but not exhaustive; it does not establish
absence of closer prior art.

| Source | SHA-256 of inspected PDF |
| --- | --- |
| AB | `a06560481dd4dfdd91f0d031221be1aa1152e3cd5d15300e1a08c9f8df7f1f48` |
| GP-T | `40766ea0cf0db3b68291599e54087d6f6af408e3b7e4b80ee19c60ffaa2823e4` |
| GP-G | `cdbfdae000b18bd1d30e4e367f346d8d288ef6bd77402544f94b04f9be2d2cb8` |
| F | `99ee420f2e620a1e40e23d7dd8b3608c01f9f07bb32850703d33b9e03d48cb4e` |
| CCRW | `8865595e34e9f840c673aca839914a3f79617e49b78bf16c13a65500c9a6b6a2` |
| MM journal manuscript | `e455f9c221809602e02e5e04a8dd33e85db7a85ca38f4d81b7449439e9a34a66` |
| ES | `6385828f0a217f51cf0338c848748c2c92fd138eda45c5f474091cf18f983399` |
| CW | `a53db089031e7eefc41d9baa76f8c77ee3d454330de28b2271f326e16d392abc` |
| W | `5b2ad18021eb0f05f3bb53d265307b1a513604086e9ff1d99a4de12c986ffc5b` |
| KMS | `1164f4896f25771234525c1b3e4e302c90734c1db71929470b1ae148fa1ecfc1` |
| AMB | `c096b58eb49350bacd49df857a5d0baff152d22676fcef5216e450f81ebcfadc` |
| C | `8613fa536cc493737a36b142ebe7df65a3ee918b7700d835c02139cb3f652e91` |
