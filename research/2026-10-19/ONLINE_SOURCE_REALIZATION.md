# Online source realization, public commands, and repair obstructions

**Base:** PR179 `81684b4b8956f9f5da56c376ba7e4339277eb665`.
**Separately inspected sibling:** PR178
`e42096ec0186228dd0f748767599e470f2ca2e1d`; its causal dossier and extracted
manifest were read, without merging its history. **RH PROVED: NO.**

**Verdict:** exact finite safety-game and belief-state criteria are established
with full proofs and independently checked certificates. Their mechanisms are
**CLASSICAL**. Two sharp model-identification/repair obstructions are proved:
the source transition relation alone does not determine public online
realizability, and online-safe observation repairs need not have a coarsest
member. No new academic-priority claim is made.

## 1. The mathematical interface and provenance boundary

Retain PR179's finite `SourceGraph`: private states `X`, reports `q:X->Y`,
original-provenance labels `sigma:X->Sigma`, allowed initial states `I`, and
partial nondeterministic labelled edges `x --a--> x'`. Every edge preserves
`sigma`. Current physical carrier, epoch, resource, and history information may
change inside `x`. A fixed original label does not impose a fixed current
carrier, and its storage does not make it public.

Supply a finite abstract relation `y --a--> y'`. It may be the existential
projection of the source graph, but is an explicit input: refusing a required
request is not permitted to silently shrink the specification.

In the perfect-information game, both players know the current `x` and hence
its original label. The environment requests any abstract `q(x) --a--> y'`;
the resolver must immediately choose a genuine `x --a--> x'` with `q(x')=y'`,
without knowing later requests. No matching successor is a refusal and a loss.
No abstract request is a safely terminated play; no liveness is asserted.

Public-only control requires a different object: an alphabet `C` of declared
commands and complete implementation rows `T_{a,c}(x) subset X`. Every listed
outcome must be a lawful source edge. A row may be empty (unavailable), and
nonempty rows may have adversarial nondeterminism. A public action is the name
`c`; it is not an arbitrary, privately chosen function `x -> x'`.

This object adds responsibility for choices to the relation, as in alternating
transition systems. PR178's deterministic labelled quotient and PR179's
offline support recursion remain distinct special cases. Neither supplies
these public commands for free.

## 2. G1: exact perfect-information winning region and certificates

We prove the slightly more general finite arena used by both compilers.
Let `V` be a finite position set. At `v`, the environment chooses a request
`r in Req(v)`. The resolver selects a response `c in Resp(v,r)`. The environment
then chooses any next position from a **nonempty** set `Out(v,r,c)`. A response
with an empty outcome set is disallowed, not winning by vacuity. Empty `Resp`
means immediate failure; empty `Req` means safe termination.

Put

\[
 F(Z)=\{v:\ \forall r\in\operatorname{Req}(v)\ \exists c\in
 \operatorname{Resp}(v,r),\ \operatorname{Out}(v,r,c)\subseteq Z\}. \tag{G1}
\]

**Theorem G1 (PROVED / CLASSICAL).** `W=nu F` is exactly the set of positions
from which the resolver has a pure sure-winning strategy, including against
arbitrary history-dependent environment choices. A positional resolver
strategy suffices. Every losing position has a positive integer rank at most
`|V|`, a chosen spoiling request, and for each possible response a chosen
lower-rank outcome. This positional counterstrategy forces a refusal within
at most the initial rank many requested rounds.

A complete certificate consists of:

* a proposed winning set `W` and one response for each `v in W,r in Req(v)`,
  whose nonempty outcome set is contained in `W`;
* ranks `rho:V\W->{1,...,|V|}`;
* for each losing `v`, a request `r_v`, and for every response to it one outcome
  `v'` outside `W` satisfying `rho(v')<rho(v)`.

These conditions can be checked against the original arena without rerunning
the fixed-point algorithm. Any certificate satisfying them identifies the
**exact** winning set, not merely a sound subset.

**Proof.** `F` is monotone. Starting with `Z_0=V`, set `Z_{k+1}=F(Z_k)`.
The sequence decreases and stabilizes after at most `|V|` strict deletions;
write its limit `W`. It is a fixed point. If `K subset F(K)`, induction gives
`K subset Z_k` for every `k`, so `W` contains every postfixed set. Hence it is
the greatest fixed point.

At every `v in W` and legal request, fix a witnessing response from (G1).
All possible outcomes remain in `W`. Induction over the number of rounds
proves that the resulting positional strategy never refuses a request.
Terminating plays are safe; every nonterminating play is safe because every
finite prefix is safe.

For `v` first removed in round `k`, define `rho(v)=k`. There is a request with
no response whose outcomes all lie in `Z_{k-1}`. Consequently each response
has some outcome outside `Z_{k-1}`, necessarily removed at a smaller rank.
For `k=1`, because all outcomes are in `V` and nonempty, this means there is
no response at all. Choose those requests and lower-rank outcomes. They defeat
every resolver, regardless of its memory: the positive rank strictly decreases
on each completed round, and at rank one no response is possible. This also
proves certificate soundness for any supplied ranks, without trusting the
elimination process. The positive and negative certificate regions partition
`V`, so together they establish exactness. QED.

For the private-source game, positions are `(x,q(x))`, represented by `x`;
each matching successor `x'` is a response with singleton outcome `{x'}`.
Thus G1 specializes exactly to the requested `forall abstract edge exists
matching private edge` formula, without replacing later requests by foreknowledge.

### Exact offline/online separation

PR179's three-state example has one report, initial state `p`, and states
`p,u,v`. Either request `a,b` sends `p` to either `u,v`. Only `a` is available
at `u`, and only `b` at `v`; those enabled actions again allow both successors.
The offline supports are `{p}` then `{u,v}` forever, so every finite word has
a private lift. The online certificate has `rho(u)=rho(v)=1`, `rho(p)=2`, and
`W=empty`. After seeing the chosen first successor, the environment requests
the other action. Adding genuine `a,b` self-loops at `p` makes `p` winning and
invalidates the old losing certificate. This is an exact mutation control.

## 3. G2: public-only sure safety, with complete implementation semantics

Let `h:X->O` be a public observation refining `q`. The resolver knows its
observation/request/command history, not `x` or `sigma` unless `h` exposes them.
The environment sees the private state, request, and chosen command. Initial
uncertainty is an explicitly specified nonempty `h`-homogeneous set `B`.
For an initially mixed observation, split by the actually received signal.
An unknown original is allowed: `B` can contain several original labels.

Given `B` and a request `(a,y')`, a command is admissible precisely when

\[
 \forall x\in B:\quad T_{a,c}(x)\ne\varnothing
 \quad\text{and}\quad T_{a,c}(x)\subseteq q^{-1}(y'). \tag{G2a}
\]

In particular, it is invalid to discard wrong-report outcomes before checking
legality. Such filtering would turn a requested deterministic report into
undeclared postselection. For an admissible command define

\[
 P(B,a,c)=\bigcup_{x\in B}T_{a,c}(x),\qquad
 B_o=P(B,a,c)\cap h^{-1}(o)\ne\varnothing. \tag{G2b}
\]

The belief arena's positions are all nonempty homogeneous subsets; its requests
are the abstract edges from their common base report; its responses are exactly
the admissible commands; its adversarial outcomes are all nonempty `B_o`.
There are at most `sum_o(2^{|h^{-1}(o)|}-1)` positions.

**Theorem G2 (PROVED / CLASSICAL subset construction).** A pure, public-history
dependent strategy is surely safe from `B` iff the belief arena's G1 winning
set contains `B`. A strategy depending only on the current exact belief and
current request suffices. This is finite memory in the original source,
although it need not be memoryless in the current public report.

**Proof.** For every finite public history, induction using (G2b) identifies
its belief exactly with the endpoints of its compatible private histories.
The same command is used along all those histories. Condition (G2a) is
necessary: otherwise some compatible private history has no implementation
or a forbidden report outcome. It is sufficient for the next response to be
lawful at every such history. After the next public signal the set of possible
endpoints is exactly (G2b), including every adversarial outcome.

A winning belief strategy can therefore be implemented by updating the exact
belief from the public record; all real outcomes yield winning beliefs. In
the converse direction, fix any public strategy and a losing initial belief.
Use the finite G1 rank certificate to choose requests and successor observation
blocks. If the proposed command violates (G2a), choose a witnessing compatible
private history and its unavailable or wrong-report continuation. Otherwise
follow a rank-decreasing observation block. Eventually such a failure occurs.
The final finite public history has a compatible private history by the support
induction; choose that concrete witness from the initial support. Thus the
policy fails on at least one initial private state and one legal adversarial
evolution. No switching of actual source representatives is licensed: the
whole finite counterplay is reconstructed as a single source-faithful path.
This refutes sure safety, proving the converse. QED.

The negative belief certificate asserts `for every public policy, some initial
state and adversarial history defeat it`; it need not defeat every initial
state. The theorem is about pure **sure safety**. No almost-sure, probability,
reachability, parity, or general stochastic belief-sufficiency claim follows.

### Two sharp public-interface countermodels

**G2-X1 (PROVED obstruction).** Private edges, observation and initial support
alone do not determine public online realizability. Take indistinguishable
initial states `zero,one`, one terminal `done`, and lawful edges
`zero --serve--> done`, `one --serve--> done`. Interface A has one command
`serve` enabled on both states; it wins. Interface B has `left` enabled only
at `zero` and `right` only at `one`; it loses. Both command interfaces have
exactly the same union of private labelled edges. A truthful probe distinguishing
the initial states repairs B, but that probe must be supplied as a lawful
instrument, not inferred from the existence of a mathematical partition.

**G2-X2 (PROVED memory separation).** Two separately observed initial states
move to private states with the same current report; the required final command
is `left` in one original and `right` in the other. Retaining the initial signal
gives a singleton belief and wins; a controller using only the current merged
report cannot choose safely. The transitions preserve the respective original
labels. The test contains a six-state exact example.

## 4. G3: structural no-go and minimal lawful one-step probe repair

**Theorem G3a (PROVED no-go).** Adding any truthful nondestructive observation,
with arbitrary public memory, cannot make a private state winning if it is
losing in the perfect-information private-successor game, provided the source
edges and abstract requests remain fixed and every public implementation uses
only those edges.

**Proof.** A fully informed private resolver can emulate any public controller,
its observations and memory. After a command is selected it can select a legal
private outcome. If the public policy were surely safe, every such emulated
history would succeed, giving a winning private resolver. This contradicts G1's
losing rank certificate. Equivalently, every chosen private edge still decreases
the rank under the spoiling request in the singleton-outcome game. Observation
does not create a missing edge. QED.

This is a necessary condition, not a sufficient public-controller condition:
G2-X1 has only private-winning states yet one public command interface loses.
The three-state offline/online example remains losing even after a perfect
state probe, so information acquisition alone cannot repair it. A state-changing
intervention, restricted request protocol, or enlarged command/transition menu
changes the contract and lies outside this no-go.

For a sharp positive repair theorem, fix a one-step, one-request interface:
private states `X` have one public report, and `E_x subset C` is the set of
commands which are legal at `x` and terminate successfully. All outcomes are
already accounted for in that declaration. Define the minimal conflict
hypergraph

\[
 \mathcal H=\{H\subseteq X:\ \bigcap_{x\in H}E_x=\varnothing,
 \text{ and every nonempty proper subset has nonempty intersection}\}. \tag{G3}
\]

Let `P` be a finite menu of declared total truthful nondestructive probes,
each with output map `p:X->O_p` and exact nonnegative acquisition cost `c_p`.
A selected bundle is acquired before the request, and all outputs are retained.
This is a fixed probe bundle, not adaptive acquisition or a physical energy law.

**Theorem G3b (PROVED; CLASSICAL hypergraph/set-cover mechanism).** A bundle
`S subset P` permits a surely successful public command iff for every
`H in H` some `p in S` is nonconstant on `H`. Consequently minimum legal
acquisition cost is exactly the finite weighted hitting-set optimum on the
sets of hyperedges split by each available probe. If some hyperedge is split
by no supplied probe, no bundle repairs the interface. A singleton hyperedge
cannot be split by any observation and is an absolute one-step information
repair obstruction.

**Proof.** The joint probe output partitions `X` into blocks. A safe public
command exists on a block `B` iff `intersection_{x in B} E_x` is nonempty.
If that intersection is empty, finite inclusion minimization produces a
hyperedge `H subset B`; conversely a block containing a hyperedge has empty
intersection. A hyperedge is contained in one output block iff every selected
probe is constant on it. Negating gives the criterion. Every feasible bundle
therefore covers exactly all hyperedges, with its stated additive cost, proving
the optimization equality. QED.

**G3-X (PROVED: no coarsest policy repair; pairwise tests insufficient).** Let

\[
 E_0=\{a,b\},\qquad E_1=\{b,c\},\qquad E_2=\{a,c\}.
\]

Every pair has a common command, but the triple does not: the only minimal
hyperedge is `{0,1,2}`. Both partitions `{0,1}|{2}` and `{0}|{1,2}` are adequate.
Any common coarsening identifies `0~1` and `1~2`, hence is the constant partition,
which fails. Thus there is no coarsest adequate observation refinement, even
though a future-safe autonomous congruence has a coarsest refinement under its
different contract. The distinction is disjunctive capability versus exact
autonomous behavior preservation. A minimum-cost legal probe bundle can still
exist; it is not a canonical least information object.

The exact test menu has a constant probe of cost zero, a triple-splitting probe
of cost `2/3`, and another of cost `3/2`. Direct raw observation-block checks
independently verify the minimum `2/3`. Omitting all splitting probes gives
an exact no-repair certificate. No general minimum sensor synthesis or new
hypergraph theorem is claimed.

## 5. Primary-source comparison

| Source inspected this round | Closest result and exact relation |
|---|---|
| Alur, Henzinger, Kupferman, Vardi, *Alternating Refinement Relations*, CONCUR 1998, [author-hosted original](https://www.cs.huji.ac.il/~ornak/publications/concur98.pdf), introduction and section 3 | Alternating simulation and game-based refinement with fixed-point checking. G1 is a finite safety specialization; the offline/online split is not novel. |
| Chatterjee, Doyen, Henzinger, Raskin, *Algorithms for Omega-Regular Games with Imperfect Information*, LMCS 3(3:4), 2007, [arXiv:0706.2619](https://arxiv.org/abs/0706.2619), section 3.1 and Theorem 7 | Knowledge/subset reduction for deterministic observation-based sure winning. G2 is its safety-specific, explicit-command specialization. The paper's wider objective results are not asserted by our compiler. |
| Boker, Lehtinen, *Token Games and History-Deterministic Quantitative Automata*, [arXiv:2110.14308](https://arxiv.org/abs/2110.14308) | Prefix-only nondeterminism resolution differs from offline word acceptance. G1 resolves the finite safety case used by PR179; no new history-determinism theory is claimed. |
| PR178 causal dossier at the pinned sibling commit | Its safe-transcript criterion checks universal action availability on an original/current prefix fiber. G2 adds an explicit all-continuation safety objective and public command realization; it does not identify this game with the sibling's whole quotient semantics. |

The original alternating and imperfect-information papers were read in full-text
retrieval; the Boker--Lehtinen publisher/arXiv record was reread and the full-text
paper was inspected in the prior round. Mathematical correctness here rests on
the complete proofs above. Academic novelty of the source-indexed integration
and countermodel packaging remains **UNVERIFIED**; the dominant mechanisms
are known.

## 6. Implementation, independent checks, and remaining theorem

Files: `observational_succ/online_source_games.py`,
`tests/test_online_source_games.py`, and the Paper A section fragment
`research/2026-10-19/paper_a_online_realization.tex`.

Baseline before modification: **25 tests passed** from
`tests.test_lawful_history_gluing` and `tests.test_no_ghost_policy`.
New targeted suite: **12 tests passed**; combined relevant suite: **37 passed**.
Commands:

```sh
python -m unittest tests.test_online_source_games -v
python -m unittest tests.test_online_source_games tests.test_lawful_history_gluing tests.test_no_ghost_policy -q
```

The checks include all **256** two-state/two-command arenas and **60** seeded
three-state/two-request arenas against explicit positional-strategy enumeration
and reachable-graph traversal, with no fixed-point elimination in the oracle.
The public compiler is checked on **256** raw command tables and **768** initial
belief cases using a separately written finite public-policy tree over complete
private path records. The tree oracle does not use the compiler or solver.
Tests also mutate ranks, strategies, transitions, outcomes, and datatype guards;
reject wrong-report postselection; and compare sensor optimization against direct
observation-block intersections. These are method-diverse exact finite checks,
not independent source authentication or a blind external mathematical review.

The separate formal lane at commit `3f263c0` supplies
`formal/ForgeGameCertificates.lean` and an actual Lean 4.14 receipt. Its eight
printed declarations are axiom-free. The source and receipt were inspected
here: `positive_policy_is_lawful`, `lawful_path_preserves_origin`,
`adversary_run_shorter_than_rank`, `ranked_certificate_forces_finite_failure`,
`positive_and_ranked_regions_disjoint`,
`alternating_adversary_run_shorter_than_rank`,
`alternating_ranked_forces_finite_failure`, and
`alternating_certificates_disjoint`. This lane does not copy or modify that
file; the principal integrates it separately. The formal certificate theorems
are more general in carrier size than the finite implementation, but do not
prove fixed-point generation, the cardinality rank bound, or the belief compiler.

Configuration exhaustion raises `GameBudgetExceeded` with `UNRESOLVED`, never
an empty winning set. No probability is inferred from an edge, and no computed
possible trajectory is called an observed event. The certificate checker does
not call the generating solver.

| Claim | Truth/authority state | Boundary |
|---|---|---|
| G1 exact finite safety region, strategy/rank certificates | PROVED; CLASSICAL mechanism; TESTED EXACT MODEL | Finite complete arena, safety/termination convention |
| G2 public sure-safety belief reduction | PROVED; CLASSICAL mechanism; TESTED EXACT MODEL | Declared commands, complete outcome rows, pure sure safety |
| G2-X1 source edges do not identify public winner | PROVED exact counterexample | Command interface must be part of the model |
| G3a observation cannot fix private structural loss | PROVED no-go | Probes nondestructive, requests and source edges fixed |
| G3b fixed probe acquisition equals hyperedge hitting set | PROVED; CLASSICAL mechanism; TESTED EXACT MODEL | One-step terminal control, supplied lawful total probe menu |
| G3-X coarsest online repair need not exist | PROVED exact counterexample | Different from coarsest autonomous congruence |
| Generic positive/negative certificate soundness | KERNEL-CHECKED in separate formal lane, eight axiom-free declarations | No Lean check of Python's fixed-point algorithm, cardinality bound, or belief compiler |
| Academic novelty / physical source completeness | UNVERIFIED / SOURCE-CONDITIONAL | Requires wider prior-art and empirical/model checks respectively |

**Next verdict-changing target:** a combined retention/acquisition/online-control
Pareto theorem for *destructive*, costly probes on source/current belief pairs.
It must preserve the command interface and action order, not merely color a
static graph; the one-step fixed-bundle hitting-set theorem cannot substitute
for adaptive control. Foundations develops the original-state acquisition
component separately. This dossier supplies the causal strategy and no-coarsest-
repair boundary that the unified theorem must respect.
