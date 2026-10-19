# Partial-source quotients and certified causal descent

**Status:** RH-independent technical paper candidate; classical mathematics,
new project implementation/formal integration. No academic novelty established.
**Claim family:** `INS-CAUSAL-Q1`, `INS-CAUSAL-G1`, `INS-CAUSAL-P1`,
`INS-CAUSAL-R1`, `INS-CAUSAL-X1`. **RH proved: NO.**

## 1. Source contract and exact scope

Fix sets of private states S, actions A, public reports O, and transition
labels L. A deterministic partial source is

\[
  \delta:S\times A\longrightarrow 1+(L\times S),\qquad o:S\to O.
\]

The distinguished `none` in the disjoint union means an unavailable action.
A label may be a tuple of outcome, exact nonnegative causal cost, and event
occurrence token. The Python instance uses outcome and rational cost; the
action word retains order. If occurrence-sensitive identity matters it must
be present in the declared action or state grammar. An immutable original
source tag \(\sigma:S\to\Sigma\) obeys
\(\delta(s,a)=(\ell,t)\Rightarrow\sigma(s)=\sigma(t)\).
The tag is private metadata, not a newly available public probe.

A realized history would require an external execution receipt. All paths
constructed here are **possible paths of the declared mathematical model**.
The source ID and basis identify that model; they do not authenticate a
physical apparatus. A source-table digest binds calculations to declared
bytes, not to empirical truth. Arbitrary semantic transformations carry no
proof authority. Lean establishes universal propositions from the declared
hypotheses; finite exhaustive Python runs establish only their finite cases.

Source-faithful comparison squares commute with the partial labelled action
map and retain the chosen source representative along its whole path. They
need not preserve private-state identity after quotienting. There is no
topology in these finite-word statements. Infinite paths, gluing of arbitrary
covers, completion, convergence and probability couplings need separate
assumptions and proofs.

## 2. Lawful quotient theorem (`INS-CAUSAL-Q1`)

Let q:S→Q be onto. Extend q to \(\widehat q:1+(L\times S)\to
1+(L\times Q)\) by preserving `none` and labels. The following are equivalent:

1. For all s,t,a, \(q(s)=q(t)\) implies
   \(\widehat q\delta(s,a)=\widehat q\delta(t,a)\).
2. There exists a quotient action \(\bar\delta:Q\times A\to1+(L\times Q)\)
   satisfying \(\bar\delta(q(s),a)=\widehat q\delta(s,a)\); for every finite
   action word w and every s, the exact optional run result commutes with q,
   retaining the complete label word when accepted; every accepted quotient run from q(s) lifts from
   **that same s** with the same labels and the required terminal q-value.

This statement includes all sets S,A,L,Q, not only finite carriers. A current
report descends too exactly when o is constant on q-fibers; in that case
\(o=\bar o\circ q\). This additional report factorization is tested by
`audit_quotient`; the Lean Q1 statement formalizes action/label descent, and
does not include o. The existing `source_transport_iff_fiber_compatible` in
`formal/EODCS_CausalDescent.lean` supplies the general report factorization.

**Proof.** Necessity follows by replacing \(\widehat q\delta\) with
\(\bar\delta q\). For sufficiency choose one s_y above each y∈Q and set
\(\bar\delta(y,a)=\widehat q\delta(s_y,a)\). Fiber compatibility makes this
independent of the choice. Induct on the word. The empty word preserves its
starting point. For a nonempty word, the commuting one-step square gives
simultaneous failure, or equal first labels and q-related successors. Apply
the induction hypothesis to the tail. If a quotient word is accepted,
the original run cannot be `none`, so unpacking the commuting equation gives
the required endpoint and label word. This proves the lift without choosing
new source representatives along the run. ∎

**Kernel authority:** `lawful_quotient_iff`, with supporting
`quotient_exists_iff_fiber_congruent`, `run_naturality`,
`every_representative_lifts` in `formal/InstituteCausal.lean`.
The general quotient construction uses `Classical.choice`. On accepted runs
the label list is preserved exactly; therefore any declared fold of its costs is preserved.
If a later action fails, `run` returns `none` and does not export the earlier
successful prefix labels. A failure-prefix journal requires a richer run type;
no preservation theorem for that additional output is asserted here.
No injectivity on discarded private histories is claimed.

For deterministic adaptive policies using only the retained observation
history, equal histories select equal next actions. Applying Q1 inductively
therefore preserves every finite branch of the same such policy. This is a
paper corollary, not a separately mechanized strategy-synthesis theorem.
A mathematically refined q need not be an implementable observation instrument.

## 3. Source-indexed gluing and dual exclusion (`INS-CAUSAL-G1`)

This theorem allows a **nondeterministic** relation
\(E\subseteq S\times L\times S\). For any initial support I⊆S and finite
label word \(w=(\ell_0,\ldots,\ell_{m-1})\), define

\[
B_0=I,\qquad B_{i+1}=\{t:\exists s\in B_i,\ E(s,\ell_i,t)\}.
\]

Then \(z\in B_m\) iff there is **one** path
\(s_0,\ldots,s_m=z\) with \(s_0\in I\) and
\(E(s_i,\ell_i,s_{i+1})\) for all i. If every E-edge preserves σ,
every point on the path has the same original source tag.

An impossibility certificate consists of sets \(C_0,\ldots,C_m\subseteq S\)
such that \(I\subseteq C_0\), \(C_m=\varnothing\), and

\[
  s\in C_i\ \land\ E(s,\ell_i,t)\quad\Longrightarrow\quad t\in C_{i+1}.
\]

Such a certificate exists iff no path from I realizes w. Empty I and empty w
are included. No source cardinality or branching hypothesis is needed for
the mathematical equivalence; effective construction here uses finite S.

**Proof.** The forward statement follows by induction on w, expanding one
existential image and keeping the same intermediate state when adjoining
the tail path. Source preservation follows by transitivity along edges.
For soundness of a cut certificate, a putative path starts in C₀ and the
closure condition forces its final state into the empty C_m. For completeness
let C_i be the states admitting no path for suffix \(\ell_i\cdots\ell_{m-1}\).
An empty suffix is realized from every state, hence C_m is empty. Any matching
edge from C_i must land in C_(i+1), otherwise appending a suffix path gives
a forbidden path. ∎

**Kernel authority:** `reachable_iff_single_source_path`,
`path_preserves_source`, `exclusion_refutes_path`, `no_path_iff_excluded`.
The latter two use an inductive exclusion proof equivalent to the displayed
cut condition. `no_path_iff_excluded` is constructive. The Python instance
uses deterministic transitions and filters by action, outcome, exact cost and
next public report. Its forward search, backward cut search, and direct raw
certificate verifier are separate code paths. Cartesian path enumeration in
the tests is a fourth algorithm, but all implementations share this model
specification and authoring session; this is implementation diversity, not
an independent source authentication or blind mathematical review.

The dual is logical exclusion, **not Farkas duality**. Existing
`no_ghost.py` retains its separate rational probabilistic primal/Farkas
certificates; this work changes none of their assumptions or code.

## 4. Public safety is an additional quantifier (`INS-CAUSAL-P1`)

For a deterministic source and a candidate public transcript, let B_i be
exactly the support of all initial states consistent with its **whole**
observed prefix. At step i a public action a_i is safe precisely when

\[
  \forall s\in B_i,\quad\delta(s,a_i)\ne\mathrm{none}.
\]

The transcript is a possible branch of a safe public policy permitted to
stop off-branch iff its final support is nonempty and this condition holds
at every prefix. The initial support must lie in one current-report fiber.

**Proof.** A public policy has the same information at every source state in
the prefix fiber, hence it cannot choose different actions among them; a
missing transition makes the choice unsafe. Conversely, use the specified
action after each proper prefix of this transcript, and stop after every
other prefix. Universal availability makes this policy safe; a path in the
nonempty final support realizes the transcript. ∎

This paper theorem is implemented and exactly tested, **not Lean-formalized**.
It does not synthesize a policy required to continue to a fixed horizon on
all branches. The existing `no_ghost_policy.py` retains its stronger
fixed-preparation, fixed-kernel, full-public-tree feasibility problem.

## 5. Counterexample-guided refinement (`INS-CAUSAL-R1`)

On a finite deterministic source, start with partition ker(o). At each round
split a block according to the previous block and the vector, over **all**
actions, of either `none` or (outcome, exact cost, successor block). If a
partition is not congruent it strictly gains a block. Hence after at most
\(|S|-|o(S)|\) strict refinements it is stable.

The stable equivalence is the coarsest lawful refinement of ker(o). Indeed
any congruence refining ker(o) refines every round by induction; the stable
partition itself is a congruence. Two states are in one final block iff all
finite experiments have equal retained traces: one direction is Q1; in the
other direction, the first differing signatures supply an action followed
by the finite distinguishing continuation from an earlier round. Availability
and exact costs are observable parts of this experiment language.

`refine_quotient` implements this finite theorem. A separate breadth-first
search on the complete ordered state-pair graph emits a shortest
distinguishing word for every failed candidate. Exhaustion proves equivalence
only for the **fully declared finite model**. This is a concrete EODCS-style
counterexample-guided theorem-search primitive. It does not infer a new
infinite source law from sample success. The termination/minimality proof
above is paper authority; it has not been mechanized in this change.

## 6. Preserved failed claims (`INS-CAUSAL-X1`)

**Refuted:** an acyclic public report chain whose individual edges each lift
must have a source lift. Take authorized edges

\[
 L_0\xrightarrow{a,\mathrm{ok},1}L_1,
 \qquad R_1\xrightarrow{b,\mathrm{ok},1}R_2,
\]

with o(L₀)=start, o(L₁)=o(R₁)=middle, o(R₂)=end. The private original tags are
L on the first pair and R on the second. From initial source L₀, the public
word a;b has no source path: after a the state is L₁, where b is unavailable.
Each public edge separately exists and the middle public report agrees.
Choosing R₁ for the second edge silently changes the actual source.
`splice_counterexample` and its backward exclusion certificate retain this
receipt. This does not contradict acyclic-join theorems: the public overlap
has discarded the private separator variable required by their hypotheses.

**Refuted:** a supported path certifies a publicly available action. Let
two initially possible states 0,1 report the same value, and enable a only
at 0. The path starting at 0 exists, but public a is unsafe because 1 remains
possible when a must be chosen. A later revealing outcome cannot retroactively
provide private information at decision time. Both controls are exact tests.

## 7. Scholarly comparison and novelty boundary

The algebraic criterion is a coalgebra-homomorphism/kernel-congruence
specialization. Rutten's *Universal coalgebra: a theory of systems* (2000)
provides the broad setting; [CWI's primary record](https://ir.cwi.nl/pub/48/)
was checked. More directly, Silva–Bonchi–Bonsangue–Rutten, *Generalizing
determinization from automata to coalgebras* (2013), discusses partial Mealy
machines in §3.1.1, partiality in §2.2, and powerset determinization in §2.1.
Those mechanisms subsume Q1/G1; [primary full text](https://arxiv.org/html/1302.1046v2).

The finite coarsest future-equivalence construction is in the classical
Nerode/automaton-minimization lineage, not a new SUCC theorem. The comparison
with Blackwell is limited: deterministic report factorization is one
zero-noise information comparison, while Blackwell's theorem concerns
statistical decision experiments and randomization. Q1 does not prove that
theorem or identify support equivalence with statistical equivalence.
See Blackwell, *Equivalent Comparisons of Experiments* (1953),
[original publisher record](https://doi.org/10.1214/aoms/1177729032).
The publisher full-text route was attempted but returned no extractable text;
no claim to a full independent re-audit of that article is made here.

The source-history join is a path-shaped constraint join. Acyclic-join
literature already explains the importance of complete separators; see
Beeri–Fagin–Maier–Mendelzon–Ullman–Yannakakis, *Properties of acyclic database
schemes* (1981), [publisher article](https://doi.org/10.1145/800076.802489).
The failed public projection is an information-loss counterexample, not a
refutation of those results. Likewise Abramsky–Brandenburger (2011) analyze
obstructions to global sections on measurement covers; the present model
adds declared temporal source transitions and availability as inputs and
does not derive them from a sheaf of public reports.
[Primary paper record](https://arxiv.org/abs/1102.0264).

The public belief-state quantifier belongs to established partial-observation
control/game theory. Chatterjee–Doyen–Henzinger–Raskin (2007) study observation-
based strategies and much stronger omega-regular objectives;
[primary paper record](https://arxiv.org/abs/0706.2619).
No new complexity separation or stronger synthesis theorem is claimed.

The contribution is an auditable integration: arbitrary partial labelled
quotients with every-representative lifting, explicit source-preserving paths,
independent finite primal/exclusion certificates, public-safety separation,
counterexample-guided finite refinement, and kernel/paper boundaries.
This supports an explanatory/formal-methods artifact; it does not currently
meet a claim of new significant mathematics.

## 8. Provenance, checks and remaining proof debt

Starting commit: `610efacf02556e1c5922bc5d4e87d0087f19b446`.
No preserved source was edited. Relevant preexisting Git blobs:

| Source path | Git blob |
| --- | --- |
| `observational_succ/no_ghost.py` | `e9c6f479f51ef2ccf08ae0b1eb1b0fb259b37d11` |
| `observational_succ/no_ghost_policy.py` | `1a84ff3c0dfa1c9dbeea8d47e80da8ef2d39e52b` |
| `observational_succ/no_ghost_coherence.py` | `7ea1891dca052d6c348d330ce4f1d62813fc8a07` |
| `observational_succ/causal_nerode_succ.py` | `23ec18dc94326b9d78cd20691fff31cddf69fe62` |
| `observational_succ/field_history_lift.py` | `7e1012b5af5752e0fcbb8255af194cdde575da2f` |
| `formal/EODCS_CausalDescent.lean` | `a8a7878dcb9ccce53d5555998caf35dc9a4763a9` |
| `formal/EODCS_NerodePlateau.lean` | `660f38cb2e2f85489c98b0a29c2a0a4e466a41e0` |

Replay: `python research/2026-10-18/institute/causal/replay.py`.
The recorder writes actual commands, return codes, compiler/Python versions,
source hashes, outputs and exact counterexample data next to itself. The
focused Python suite includes 800 three-step feasibility cases checked by
Cartesian path enumeration, 81 cost/outcome/partiality models checked by
independent finite-experiment search, and 81 two-action models checked by
direct quotient/source word replay from every representative. These counts
are explicit finite scope.

Core Lean is pinned by repository `lean-toolchain` to 4.14.0. All eight public
theorems print axiom reports. Only `Classical.choice` and `propext` occur, in
the declarations listed in the actual compiler output; four declarations
use no axioms. A transient warning-cleanup edit failed to compile, then was
repaired; its diagnostic and repair remain recorded as development history.
Only the subsequent clean compiler output supports kernel-authority claims.

Remaining debts: independent mathematical review; a Lean equivalence between
public strategy realizability and belief-safe transcript execution; a Lean
termination/minimality proof for the finite refinement implementation; and
explicit bridges to stochastic kernels, general constraint covers and
infinite closed-source admission. Existing cube/hexagon and operational
probability obligations are not discharged by a deterministic path quotient.

The smallest verdict-changing next probe is a fully declared nondeterministic
source where trace equivalence holds but bisimulation quotienting fails:
extend the oracle to relational support while preserving the distinction
between existential trace lifting and every-representative branching behavior.
Any mathematical generalization must survive that discriminator before
the deterministic theorem is promoted.
