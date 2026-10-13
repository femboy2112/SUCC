# NO-GHOST: exact causal descent, operational laws, and lawful repair

**Status:** proved finite paper statements and exact countermodels. The statements
below are not Lean declarations. Classical ingredients are identified explicitly;
no mathematical-priority claim is made. Integration does not promote an unmerged
swarm's status. This contribution is over the source model, not empirical source
authentication, and never declares a possible path to have been performed.

Primary-literature comparison and exact inspected source references are in
[PRIOR_ART.md](PRIOR_ART.md), especially Gogioso--Pinzani's established causal
sheaf failure, asynchronous cube coherence, and Koller--Megiddo--von Stengel's
perfect-recall realization plans. The standard ingredients below inherit those
priority boundaries. The independent fixture command
`python -m unittest discover -s tests -p test_no_ghost_gluing_examples.py -v`
was executed: **8 tests passed**; this is finite exact verification, not Lean.

**Inspected immutable inputs:** carrier branch/base
`9e7589e522aff990189aa8a14f6ee2fa5a28dd81`; F48 branch
`8dacc56cec68b2e998529caf31f34fb5beeaa1d3`, especially
`F48_PHASE2_ARCHITECTURE.md`; the inherited A03, X03, VOYAGER and carrier
dossiers. F48's finite-incidence sheaf and extendable-prefix theorem are prior
SUCC results, not new results here. F48 records its phase-2 paper proofs as
accepted by a fresh A03 review while final principal artifact acceptance remains
pending. The inherited finite quotient/repair work already separates mathematical
refinement from an available physical sensor.

## 1. First repair to the question: three kinds of local datum

A **section** is one complete assignment. A **support** is a set of possible
assignments. A **law** is a weighted family. Pairwise equal support projections
are not pairwise matching sections. Equal law marginals are weaker still than a
single compatible selection of witnesses. These distinctions explain why the
ordinary assignment-sheaf theorem coexists with parity contextuality.

A causal context is also not automatically an independently executable
experiment. Restricting a record to an event after deleting its ancestors must
retain its actual input interface and the provenance of that interface. It is a
**fragment of a witnessed run**, not permission to recreate that interface.
Restriction removes coordinates; it never re-prepares a source.

## 2. Constraint-complete causal incidence site

Fix finite typed variables V with finite domains D_v, and finite named
constraints j in Q with scopes S_j subset V and relations
R_j subset product_(v in S_j) D_v. Variables include, as required by the
contract, the immutable original index, initial preparation, action occurrence
IDs, outcomes, private branch tokens, carrier states, resource/memory wires,
epochs, bases, and causal boundary data. A transition constraint contains its
actual input and output interface. Preparation is a separate constraint. A
global resource or admission predicate is a constraint too; its scope cannot be
silently reduced. Zero-weight stochastic atoms are forbidden in support
constraints. Public-policy constraints refer to public history only.

An object U=(V_U,Q_U) satisfies S_j subset V_U for j in Q_U. Inclusions are
coordinate/constraint inclusions, and intersections take both intersections.
A family {U_i -> U} covers exactly when union V_i=V_U and union Q_i=Q_U.
Thus a transition or a global constraint is covered only if that constraint
itself is present in some member, with its full scope. Identity, pullback, and
transitive composition of such covers follow directly from union/intersection,
so these families are a Grothendieck pretopology on the finite incidence poset.

Define H(U) to be assignments x to V_U satisfying every j in Q_U. Restriction
is coordinate restriction. Source coordinates and interface witnesses are
included in the intersections where they are shared. Contexts may instead be
restricted to ancestry-closed fragments; deleting ancestry then requires typed
boundary variables rather than inventing a new preparation.

**NG-G1 (constraint-complete causal sheaf; reconstructed F48 baseline).** H is
a sheaf. A family x_i in H(U_i) has a unique global x exactly when its
assignments agree on every complete overlap.

**Proof.** Set x(v)=x_i(v) for any i containing v. Coverage makes this total and
overlap equality makes it independent of i. For j in Q_U, choose i containing
j. All of S_j is then contained in V_i, and x on that scope equals x_i, hence
lies in R_j. Uniqueness is coordinatewise. Conversely restrictions of a global
assignment agree. The source, legal preparation, transition, branch and resource
claims are precisely among the checked constraints, not additional conclusions
inferred from report compatibility. QED.

If these finite constraints are a complete encoding of lawful executions under
the declared contract, H(U) is exactly the set of lawful private witnesses.
This last encoding equivalence is an explicit hypothesis, not a theorem that
every proposed physical model is complete. Empty H(U) is permitted. The theorem
does not assert there is a matching local family.

## 3. Adding concurrent schedule comparisons without adding ghosts

For each context U let S(U) be its finite nonempty set of permitted schedule
presentations. In particular the full context must have a presentation; local
charts alone do not establish one. Give S(U) an authorized comparison graph.
Require this graph to be connected at every context used by the coverage.
Equivalently for the proof below, after fixing a full presentation s, every
local presentation appearing in a proposed matching family must be connected
by authorized comparisons to s|U_i, and the corresponding overlap charts must
lie in the same comparison component. All permitted adjacent swaps between
linear extensions of a finite poset supply this connectedness; an arbitrarily
restricted exchange graph need not. For each s in S(U), let H_s(U) be its full
private assignment set. Suppose:

1. For every s,t the authorized comparison paths induce a source-preserving bijection
   T^U_(s,t):H_s(U)->H_t(U), with T_(s,s)=id and
   T_(t,u) T_(s,t)=T_(s,u), independent of comparison path. The required
   inverse, disjoint-square and braid relations on a full adjacent-swap system
   are one way to obtain this. Arbitrary unlicensed fiber bijections do not.
2. Every global schedule s restricts to s|W in S(W), and restriction maps
   rho^s_(U,W) preserve actual boundary witnesses. Schedule restriction and
   these maps satisfy identity and composition for nested contexts. They commute with transport:
   rho^t T^U_(s,t)=T^W_(s|W,t|W) rho^s.
3. For each global presentation s and every allowed cover, the diagram
   W -> H_(s|W)(W) is a constraint-complete assignment sheaf as in NG-G1.

Define Hbar(U) as the disjoint union of H_s(U) modulo x~T_(s,t)x. Condition 1
means each orbit has exactly one representative in each H_s(U), including when
the sets are empty. Condition 2 defines its restrictions without choices.

**NG-G2 (coherent-presentation descent).** Under the nonempty, connected-chart
assumptions and 1--3, Hbar is a sheaf. Its
sections correspond to lawful executions in any one presentation, and no
additional source, event, or branch is introduced by schedule descent.

**Proof.** Choose any s in the nonempty S(U). Authorized chart connectedness
and path independence let us transport each local orbit to its unique
representative in H_(s|U_i)(U_i). On W=U_i intersection U_j both resulting
restrictions lie in the same fixed fiber H_(s|W)(W). Naturality says they have
the original matching orbit, and uniqueness of the representative in this
fixed fiber makes them equal. Apply NG-G1 to get unique
x in H_s(U). Its orbit is the desired glue. A different s gives T_(s,t)x by
naturality and uniqueness, hence the same orbit. Each orbit has an actual
private witness by construction. QED.

This is a narrow sufficient theorem, not an unrestricted causal-descent
characterization. Cube coherence alone does not supply comparison-graph
connectedness, restriction naturality, cover completeness, or a lawful global
schedule. If authorized local comparison graphs have disconnected components,
an orbit in one component may have no representative in the chosen restricted
full chart; the displayed proof then does not apply. For a history with
state-changing events, the intermediate current state before b differs between
ab and ba. A claimed restriction to b must explain how its input interface is
transported. Identifying both with a freshly prepared b experiment is invalid.
For restrictions that erase noncommuting boundary data, hypothesis 2 can fail.

## 4. Stronger local-support theorem on a join tree

Let {U_i} have a tree T such that contexts containing any variable form a
connected subtree (running intersection). Let nonempty local relations R_i
have exactly equal projections on each adjacent separator U_i intersection U_j.
Assume the actual global lawful set is exactly their natural join:

    Omega = {x : x|U_i in R_i for every i}.

The equation requires every global constraint, including original-source and
resource constraints, to be represented. It is not licensed by pairwise tests.

**NG-G3 (source-backed join-tree extension; classical).** Every r in every R_i
extends to some omega in Omega. If exact rational laws mu_i supported in R_i
have matching separator marginals, they have a rational coupling on Omega.

**Proof for supports.** Root the tree at i and fix r. At each neighboring child
j select an element of R_j with the prescribed separator values; projected
support equality guarantees one. Repeat outward. Running intersection ensures
that agreements along tree edges imply agreements on every shared coordinate,
so the union assignment exists and lies in Omega. This also proves every local
section extends, rather than merely proving Omega nonempty.

**Proof for laws.** Draw the root from mu_i. Given a parent/child separator value
y of positive common mass nu(y), draw the child's remaining coordinates with
probability mu_j(child assignment)/nu(y). Values of zero separator mass are
never reached and need no conditional definition. Induction gives each child
marginal mu_j while preserving all earlier marginals. Running intersection
provides one assignment. Every positive atom lies in the natural join, hence
in Omega. All arithmetic is rational. Equivalently, on positive atoms the law
is product_i mu_i divided by product_edges nu_ij. QED.

This is the classical acyclic database/junction-tree gluing mechanism with the
additional explicit obligation that the join equals the lawful carrier set.
It establishes a supported coupling, not operational production of that law
under already fixed chance kernels. The next section supplies that missing gate.

## 5. Support coupling is weaker than operational realizability

Let Omega be all positive-probability finite private terminal paths of a fixed
source and instrument contract. The feasibility problem A p=b, p>=0,
sum p=1 decides whether observed laws have some coupling supported on Omega.
It does **not** generally decide whether the fixed contract can produce p.

**NG-P0 (counterexample).** A forced fair coin with outcomes 0,1 has both paths
in Omega. The law p=delta_0 belongs to Delta(Omega), but its unconditional
operational law is (1/2,1/2). A postselection-on-0 instrument or a changed
preparation is a different contract. Positive probability of a single recorded
0 does not turn that one receipt into a population law delta_0.

**NG-P1 (hidden-source oracle counterexample).** Sigma={0,1} is fair and the
empty public history is identical for both originals. The only actions are
guess0 and guess1; receipt success equals [guess=Sigma]. All four
(source,guess) pairs are lawful. A supported distribution assigning 1/2 to
(0,guess0) and 1/2 to (1,guess1) preserves the source prior and succeeds surely.
It is still not operational: a source-blind public policy chooses guess0 with
one common probability q, giving success (q+(1-q))/2=1/2. Even conserving
private-prefix probability flow is insufficient if it allows action choices to
depend on hidden source coordinates. Public information sets are load-bearing.

### Exact public realization-plan polytope

Fix a finite public perfect-recall history tree of bounded horizon, with a stop
option/terminal leaves specified explicitly. At each public decision history h,
A_h is a declared menu safe on **all** positive private alternatives under h.
The preparation and complete rational kernels are fixed. Include branch tokens
in private paths only when they are actual model process data. The policy may
randomize using independent private coins but sees only h, including its own
past actions. Nature chance branches and action decisions are distinct nodes.

For each complete private path omega define the rational constant

    n_omega = J_empty(sigma,c0) times product of its kernel atom weights.

No policy factors occur in n_omega. Let h(omega) be its public terminal word.
Introduce nonnegative controller realization weights r_h and r_(h,a):

    r_empty=1;
    sum_(a in A_h) r_(h,a)=r_h;
    r_(h,a,z)=r_(h,a) for every public outcome z successor.

The same controller weight is copied across chance outcomes: it is not divided
as if the controller selected nature's result. Set

    p_omega = n_omega r_h(omega).

**NG-P2 (finite operational realization theorem).** A path law p is realizable
by a lawful source-blind behavioral public policy if and only if such r exists.
Consequently any requested local-law equations A p=b can be decided by an
exact rational linear feasibility problem with these additional equations.

**Proof, forward.** Set r_empty=1 and multiply along each history only its
policy action-selection probabilities. The action sum equation is normalization
of the policy; observing nature adds no controller factor. The multiplication
rule for a private path is exactly p_omega=n_omega r_h(omega).

**Proof, reverse.** At r_h>0 choose pi(a|h)=r_(h,a)/r_h. At r_h=0 choose any
allowed distribution; such nodes have zero realized probability, and all
descendant realization weights vanish. Induction gives the prescribed
controller products. Multiplication by the unchanged preparation and kernels
gives p. Menus guarantee safe actions without hidden-state sensing. Finite
normalization of nature and policy shows sum_omega p_omega=1. QED.

All constants are rational, so a nonempty polytope has a rational point. An
exact rational infeasibility witness can be obtained by Farkas' lemma after
eliminating signed/free variables or splitting them into positive parts; a
verifier checks the matrix identity and strict negative scalar exactly. This
is classical extensive-form realization-plan/sequence-form mathematics, now
applied to the retained source-indexed carrier law. It is a correction to an
overstrong operational interpretation of the ordinary supported-coupling LP.

**Equivalent finite characterization.** The operational laws form the convex
hull of laws of finitely many deterministic public policies. Forward: sample
in advance an action independently for every public decision history using
its behavioral probabilities; the resulting distribution on deterministic
policies induces the same path law. Reverse: a random deterministic policy
chosen independently of nature has behavioral action probabilities conditioned
on full public history. Perfect recall makes all hidden paths sharing h have
the same compatible policy choices, so this conditional policy is source-blind
and reproduces the path law. Alternatively the same conclusion follows from
the realization equations above. This equivalence fails without the declared
information/recall assumptions. Initial random policy choice is not correlated
with Sigma unless the contract explicitly supplies such access.

## 6. Mandatory countermodels and their precise meanings

**Destructive experiments (executability).** Prepare original (x,y)=(1,1).
Action a reports current x then sets current y to 0; action b reports current y
then sets current x to 0. Both single-event report-1 histories are lawful.
After a, b reports 0; after b, a reports 0. There is no one-carrier history with
both requested report-1 events, despite a common original witness. No reset
has been declared. This reproduces the established F48 obstruction.

**Projected source/interface overlap.** Original Sigma is a single label;
one private preparation chooses current bit t in {0,1}. The coarse interface
forgets t. A left fragment requires actual boundary t=0; a right fragment
requires that same boundary t=1. Their public interface reports coincide,
while their private fiber product over the true interface is empty. Gluing
through the quotient manufactures an unsupported shared boundary. Retaining t
correctly rejects the proposed glue; it does not execute either fragment anew.

**Odd parity triangle (support/law obstruction).** The contexts xy,yz,xz
carry supports x=y, y=z, x!=z, each with uniform mass on its two assignments.
Every singleton marginal is uniform, yet no global tuple exists. For any
global bit tuple, [x=y]+[y=z]+[x!=z]<=2; the proposed local expectations sum
to 3. This is a direct rational dual inequality. The local supports agree
after projection, but there is no matching family of individual assignments.

**Nonregular cover (deck tests incomplete).** Take a bouquet of two loops
with a connected three-sheet cover whose monodromies are r=(12), b=(23)
on {1,2,3}. Its deck group is the centralizer of the generated S3 action,
hence trivial. Take the local system with the same fiber/action. On the cover,
the assignment s(i)=i is a parallel section: s(g i)=g s(i) for g=r,b.
It is deck-invariant vacuously. A descended base section would be one x fixed
by both transpositions, and none exists. Full fiber-pair descent, rather than
deck invariance on an arbitrary cover, is required. A regular cover's deck
action is transitive on each fiber, explaining the stronger valid special case.

**Omitted global resource constraint.** Three event occurrences each consume
one resource unit, preparation has two units, and no replenishment exists.
Every two-event set is executable and root-level pairwise exchanges can be
lawful; the three-event set is not executable. A cover retaining only local
cost labels and preparation identity omits the constraint sum costs<=2.
It is not constraint-complete. If all current resource wires are retained,
the contradictory local fragments need not even match. Thus neither pairwise
diamond tests only at the root nor the assertion “all authorized diamonds
hold” implies existence of a global execution: beyond two events there are
no authorized continuations. This does not contradict NG-G1/G2.

**Finite completion outside the original source class.** Let originals be
eventually-zero infinite bit streams and the instrument read/delete their
first bit. Every finite all-one receipt word has an allowed original, but no
allowed original realizes all-one forever. Alternatively all binary prefixes
extend to streams with infinitely many 1s, while their inverse limit contains
forbidden all-zero forever. A nonclosed admission class is not recovered from
all its finite projections. These are inherited VOYAGER/F48 distinctions;
mathematical infinite-path existence is not physical infinite execution.

**Chosen transport holonomy.** The three-event comparison model and exact
branch permutations are supplied in the companion coherence contribution.
Existence of some coherent family is separate from coherence of a chosen
family. This dossier does not promote the abstract bit involution into an
instrument countermodel by assertion.

## 7. A precise sheafification no-go

Let F be a presheaf of source-supported private fragments for a proposed site.
Suppose there is a matching local family f_i over U with no f in F(U).
For example, a single declared stochastic source permits only outcome pairs
00 and 11; singleton contexts report 0 and 1 respectively, while their common
source label agrees. A cover omitting the correlation constraint admits this
matching family although the actual source has no such pair.

**NG-G4 (no source-realization retraction).** For sheafification eta:F->aF,
there is no natural map R:aF->F with R eta=id_F.

**Proof.** The eta(f_i) are matching sections of the sheaf aF, hence glue to g.
Naturality and R eta=id imply R_U(g)|U_i=R_(U_i)(eta(f_i))=f_i. This supplies
the forbidden F(U) witness, contradiction. QED.

The result does not say sheafification is mathematically invalid. It says its
formal completion cannot be interpreted by such a source-preserving realization
map. One may retain only the image eta_U(F(U)) as admissible; that image need
not be a sheaf. Alternatively restrict coverage to families satisfying actual
effective descent, such as the complete incidence coverage. Adding sheaf axioms
alone does not create experiments, resources, original sources or event receipts.

## 8. Finite lawful repair: what can and cannot be canonical

A repair is a finite explicitly presented contract M_r, a cost k(r)>=0, an
allowed implementation/access witness, and a declared comparison with the
original model. The goal specifies whether the repair preserves a task,
changes the task, rejects a previously unsound claim, or physically expands
the instrument menu. These are different goals. Restricting an independence
relation can repair a comparison theorem while giving up a requested reordering;
it cannot be reported as executing both events in the original contract.

Fix a finite catalog R and budget B. Let V(r) be an exact verifier for the
desired finite property (kernel equality, source-supported glue, operational
LP feasibility, or an explicitly bounded horizon), together with the legal
implementation certificate.

**NG-R1 (finite menu feasibility and optimum).** A legal repair exists within
B exactly when some r in R satisfies k(r)<=B and V(r). Exhaustive finite
enumeration yields a minimum-cost feasible repair, or a complete family of
verified rejection certificates. This is exact bounded search, not a universal
repair constructor. If the catalog/horizon is incomplete, failure is only
relative to that catalog/horizon and must be reported UNRESOLVED for a broader
claim. Verification of positive output includes the modified contract itself,
not merely a named sensor or an assertion that memory is accessible.

**Proof.** The feasible subset is finite; a nonempty finite set of exact costs
has a minimum. Enumeration checks each member. A negative certificate consists
of the declared exhaustive catalog plus a verifiable failure for each member.
No statement about unlisted actions follows. QED.

**NG-R2 (conservative labels cannot cure impossible coupling).** Suppose a
purported repair only replaces Omega by Omega' with a surjection pi:Omega'->Omega
and unchanged local observation maps r_i pi. Then its source-supported marginal
polytope is exactly the original one. More generally, without surjectivity its
polytope is contained in the original one.

**Proof.** Push any probability law forward along pi. Conversely, for finite
Omega and surjective pi choose one lift of each omega and lift each atomic
mass to that representative. All local marginals are unchanged. QED.

Hence adding inaccessible branch labels or duplicating histories cannot repair
an infeasible original marginal request. An operational extension preserving
all original projected laws likewise cannot realize a law outside that set.
Retaining memory can repair lossy *representation* and avoid false claims;
to enable previously impossible control it must change the legally available
information or dynamics through a declared physical mechanism.

**NG-R3 (least lawful repair need not exist).** Minimum cost is not a least
object in the order of available capabilities or information. A finite legal
catalog can contain baseline 0 and two optional accessible sensors A,B, each
adequate and neither implementable from the other, while their common available
subcontract is only 0, which is inadequate. Both repairs are minimal; no least
adequate repair exists, even with exact models and equal costs.

An explicit finite information example uses source states {0,1,2} and the
requested distinction between 0 and 2: legal sensor A has partition
{0}|{1,2}, B has {0,1}|{2}. Both separate the requested pair; neither partition
refines the other, and their common coarsening is the indiscrete partition,
which does not. No unspecified omniscient joint sensor is part of the menu.
This is a pair-discrimination task, not factorization of a total deterministic
target on all three states; the latter has a different canonical quotient.

**Conditional canonical exception.** For a complete finite stationary action
table, fix an observation quotient and require exact enabledness plus complete
outcome/next-block laws to descend for every future action. Partition refinement
produces a unique coarsest stable refinement, as already proved by the carrier
work. It is the least *mathematical* adequate information partition. It is the
least lawful repair only if a legal implementation of that partition is
available and the repair order/cost contract respects that implementation.
The theorem does not provide its sensor for free.

### Auxiliary memory lower bound

Fix coarse q:C->D. Let a graph G on C encode pairs that the repaired task must
distinguish. A retained memory encoding m:C->M is adequate for these necessary
distinctions only if q(c)=q(c') and {c,c'} in E(G) imply m(c)!=m(c').

**NG-R4.** Every adequate memory has

    |M| >= max_(d in D) chi(G[q^-1(d)]),

and thus needs at least ceil(log2 of that maximum) binary memory bits. If all
finite encodings are mathematically allowed, this bound is attained for this
static distinction task, by choosing a proper coloring within each q fiber
and reusing color labels between fibers.

**Proof.** Restriction of m to each fiber is a proper graph coloring, proving
the lower bound; fiberwise optimal colorings give the stated construction.
QED. The construction is not necessarily an available sensor, an online
updatable encoding, or a stable future-action quotient. Those obligations can
increase required memory or make a repair unavailable.

For destructive a that keeps x but erases y, recovering original y afterward
for every fixed x requires at least two retained memory states: the two y
values are adjacent in the same x fiber. A legally supplied apparatus may
copy y into a one-bit register *before* erasure and retain it, attaining the
bound. Without that declared source access, calling the register “memory”
does not license obtaining y after erasure.

## 9. Obstruction relationships and integration boundary

The layers are gates, not an asserted independent/exhaustive taxonomy.

* A strict matching family on a complete incidence cover has no separate
  finite source/interface or executability obstruction: those are already
  constraints in NG-G1. Projecting away witnesses reintroduces them.
* Coherent schedule transport permits canonical identifications only among
  already lawful presentations. It neither constructs a missing execution nor
  forces a particular probability law.
* An operational law is a supported coupling, hence operational infeasibility
  can occur even when ordinary coupling succeeds (NG-P0/P1).
* A supported coupling implies each positive local atom has a global extension;
  compatible local supports alone need not admit a coupling with prescribed
  weights. NG-G3 gives a sufficient acyclic exception.
* Finite admissible gluing does not imply realization of a complete infinite
  original source. Additional closedness/compactness or the exact F48 locally
  legal infinite-path contract is required.
* Source-preserving bijections that preserve full constraints, restrictions,
  kernels, menus and public information sets transport these finite existence
  and obstruction statements. A report-only quotient need not.

The integration edge is: F48 complete incidence constraints -> NG-G2 coherent
schedule presentations; carrier exact joint law -> NG-P2 public realization
plans; A03/X03 supported joins -> NG-G3 classical acyclic decomposition;
nonabelian holonomy -> complete fiber-pair descent and explicit comparison
coherence; existing categorical repair -> NG-R1 catalog bounds and NG-R2
conservative-refinement no-go. No existing machinery is replaced.

**Novelty verdict:** G1, G3, G4, the memory-coloring argument and finite-search
optimization use classical mathematics; P2 is sequence-form/perfect-recall
control specialized to source-indexed instruments. G2 is a conditional descent
assembly, not yet an academically new causal site theorem. Its substantive next
lemma is to construct restriction-natural adjacent-history transports for a
useful class of changing carrier interfaces without assuming the needed maps.
The operational-versus-supported gap is a concrete correctness improvement to
the proposed SUCC engine, not a priority claim about probability or causality.
