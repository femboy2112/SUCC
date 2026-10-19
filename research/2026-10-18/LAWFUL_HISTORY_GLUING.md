# Source-preserving history lifting: exact cuts, integral flows, uniform audit

**Baseline:** `f309d9104ba480c1999c962af1df7c50f19e1bfe`.
**Authority:** full paper proofs below; exact finite implementation and adversarial
tests. **No new Lean kernel acceptance is claimed. Academic novelty UNVERIFIED.**
The core ingredients are **CLASSICAL** subset construction, abstract-trace
validation, directed path/flow decomposition, and contextuality. The assembled source-indexed certificate
contract and its explicit bounds are **PROVED LOCAL**, with those dependencies.

## 1. What was already known, and the precise addition

The repository already contains:

* [CAMBRIAN C18.2](../2026-10-13/CAMBRIAN_C_GEOMETRY.md): exact history-support
  recursion; implemented by `FiniteHistorySystem.support_history` in
  `observational_succ/cambrian_c_geometry.py`.
* [NO-GHOST NG-G1/G2/G3](../2026-10-13/NO_GHOST/GLUING_REPAIR.md):
  constraint-complete private assignment sheaves, coherent schedule descent,
  and source-backed join-tree gluing. `formal/NoGhost.lean` contains the
  constraint-complete core. It must not be rediscovered as a new theorem.
* NO-GHOST NG-P0/P1/P2: a supported distribution is not necessarily the law of
  the fixed instruments or of a source-blind public policy.
* [X06](../2026-10-13/SWARM_ATLAS/X06.md): every-representative path lifting for
  suitable cost-preserving deterministic residuals; partial availability was
  recorded as a next boundary.

The addition is a finite **uniform** test of whether *every* locally admissible
projected history lifts, with a source/report-sensitive finite obstruction bound
and independently checkable positive and negative certificates. For a fixed
history it gives an explicit private-interface integrality theorem and a binary
Farkas certificate. This certifies something report-level static gluing does
not: compatibility of the actual private states used in successive events.

It is **not** claimed to strengthen the general classical assignment-sheaf
theorem after all private transitions have already been encoded as constraints.
The gain is an effective criterion that checks this missing interface property,
instead of assuming that projected compatibility supplies it.

## 2. Contract and four different questions

Let `Sigma`, `X`, `A` be finite sets, with an immutable original-source map
`s:X -> Sigma`, an observation `q:X -> Y`, an allowed initial set `I subset X`,
and action relations `R_a subset X x X`. Require

\[
 (x,z)\in R_a\quad\Longrightarrow\quad s(x)=s(z). \tag{2.1}
\]

The report image is finite. `X` must retain every private variable needed to
determine available transitions, including resource and history dependence.
A fixed original-source label means provenance/realization identity. Current
carrier states, physical source configurations, and epochs may change and must
be represented in `X`; equation (2.1) does not demand a stationary physical
carrier. Unlicensed re-preparation or a change of original is not introduced.
A bounded history-dependent contract can be expanded into complete prefixes.
An arbitrary unbounded history-dependent system need not have such a finite
presentation; the uniform theorem does not manufacture one.

For a fixed original `sigma`, put `X_sigma=s^{-1}(sigma)` and `I_sigma=I cap
X_sigma`. Define the report relation by existential projection:

\[
y\mathrel{\bar R_a^\sigma}z
\iff \exists x\in X_\sigma,\;x'\in X_\sigma:
q(x)=y,\ q(x')=z,\ (x,x')\in R_a. \tag{2.2}
\]

Fix a report/action path `w=(y_0,a_0,y_1,...,a_{n-1},y_n)`. It is locally
admissible if `y_0 in q(I_sigma)` and each edge belongs to (2.2).
A private lift is `(x_0,...,x_n)` with `x_0 in I_sigma`, `q(x_i)=y_i`, and
`(x_i,x_{i+1}) in R_{a_i}`. All vertices then have the same original source.

| Question | Exact mathematical object | What it does not provide |
|---|---|---|
| Compatible local reports? | Each projected edge of `w` has a witness | A shared middle private state |
| Global report? | The single report tuple `w` glues its overlapping report pairs | A private lift |
| One source realizes it? | At least one private lift of the whole `w` | Evidence that it occurred; an available preparation/policy |
| Effective construction/certification? | On supplied finite tables, a terminating path/cut computation | A lawful physical experiment that forces this path |

The last distinction remains even when all report paths lift. Existential
private choices made with a complete future word are not causal online choices.

## 3. LH1: private lift / nonempty support / unit flow / absence of cut

For any fixed `sigma,w`, define

\[
B_0=I_\sigma\cap q^{-1}(y_0),\qquad
B_{i+1}=q^{-1}(y_{i+1})\cap R_{a_i}[B_i]. \tag{3.1}
\]

Build a directed layered graph with vertices `(i,x)` for `x in X_sigma` and
`q(x)=y_i`, a supersource `alpha`, and a supersink `omega`. Its edges are
`alpha -> (0,x)` for `x in B_0`, `(i,x) -> (i+1,z)` for allowed `R_{a_i}`
transitions between the specified fibers, and `(n,x) -> omega` for every final
vertex. The layer index distinguishes repeated occurrences of the same state.

**Theorem LH1 (PROVED LOCAL; classical finite graph mechanism).** The following
are equivalent:

1. `w` has a private lift from original `sigma`.
2. `B_n` is nonempty.
3. The layered graph has a nonnegative real unit source-to-sink flow.
4. It has a rational unit flow, and it has a `0/1` unit flow.
5. There is no family `C_0,...,C_n` of subsets of the corresponding private
   fibers such that `B_0 subset C_0`, `R_{a_i}[C_i] cap q^{-1}(y_{i+1}) subset
   C_{i+1}` for every `i`, and `C_n` is empty.

Moreover, every unit flow is a finite convex combination of private path
flows. An infeasible instance has a `0/1` Farkas dual potential. Both a private
lift and a cut can be checked directly against the source tables without
trusting the algorithm that generated the certificate.

**Proof.** By induction, `B_i` is exactly the endpoints of private lifts of
the prefix through time `i`. The base case is the initial-condition definition.
For the induction step, appending one allowed edge gives the forward inclusion;
each element of (3.1) has a predecessor in `B_i`, whose induction witness can
be extended, giving the reverse inclusion. This proves 1 iff 2.

A private path supplies a `0/1` flow and hence 1 implies 4 implies 3. Conversely
take a nonnegative unit flow. Some edge out of `alpha` has positive flow. At
each nonterminal reached vertex, conservation supplies a positive outgoing
edge. Layers strictly increase, so this process reaches `omega` after exactly
the prescribed number of private transitions. It gives a private lift, proving
3 implies 1. This proof does not require rational approximation or an LP solver.

Subtract the minimum positive flow on that path. Conservation remains valid;
at least one positive edge vanishes. Continue. Finitely many edges imply
termination, and acyclicity prevents a positive residual circulation. The
subtracted coefficients sum to one. Thus every unit flow is a convex
combination of path flows, and the unit-flow polytope has integral vertices.
This last statement concerns this exact network polytope, not arbitrary
additional marginal, resource, or instrument-law constraints.

If a family `C_i` from 5 existed, induction would give `B_i subset C_i`, hence
`B_n` empty. If `B_n` is empty, take `C_i=B_i`, obtaining just such a family.
This proves 2 iff 5.

For an explicit linear dual, let `U={alpha} union {(i,x):x in C_i}`. The cut
conditions say there is no directed edge from `U` to its complement and that
`omega` is not in `U`. Put `p=1_U`. With incidence convention
`A_e=e_head-e_tail` and demand `b=e_omega-e_alpha`, we have

\[
 p^TA\ge0,\qquad p^Tb=-1.
\]

If `Af=b` and `f>=0`, then `-1=p^Tb=p^TAf>=0`, a contradiction. This is an
exact Farkas certificate for **that linear flow problem**. The earlier path
decomposition is the separate reason that, here, linear feasibility and
discrete private realizability agree. QED.

**Boundary.** No chance kernels were prescribed. The flow certifies support,
not a production probability. Source labels are private bookkeeping; the
theorem does not give the observer an oracle for `sigma` or an available reset.

## 4. LH2: uniform all-path lifting and a finite obstruction bound

For a fixed original, a configuration is a pair `(y,B)` with nonempty
`B subset X_sigma cap q^{-1}(y)`. For each projected edge `y --a--> z`, define

\[
 T_{a,z}(B)=R_a[B]\cap q^{-1}(z). \tag{4.1}
\]

The initial configurations are `(y,I_sigma cap q^{-1}(y))` for reports of
allowed initial states. An edge with empty (4.1) is a failure. Otherwise it
leads to `(z,T_{a,z}(B))`.

**Theorem LH2 (PROVED LOCAL; Rabin--Scott subset construction specialization).**
Every finite locally admissible report path from `q(I_sigma)` has a private
lift if and only if no failure is reachable in this configuration graph.
Equivalently, there exists a finite set `K` of nonempty configurations which
contains every initial configuration and is closed under every projected edge
using exactly the update (4.1).

If a spurious report path exists, a shortest one has at most

\[
 N_\sigma=\sum_{y\in q(X_\sigma)}
   \bigl(2^{|X_\sigma\cap q^{-1}(y)|}-1\bigr) \tag{4.2}
\]

action edges. Breadth-first search therefore gives either a shortest spurious
path and an LH1 cut, or a finite closed configuration certificate proving
uniform lifting. Exhaustion of an imposed resource budget yields `UNRESOLVED`.

**Proof.** Induction along a report path identifies its configuration support
with (3.1). Thus a reachable empty update is exactly a locally admissible
prefix without a lift, by LH1. Conversely the first empty support of any
spurious path produces a reachable failure. This proves the first equivalence.

If failure is unreachable, all reachable configurations constitute the finite
set `K`. Conversely closure of `K`, its initial containment, and nonemptiness
show by word induction that every locally admissible path keeps a nonempty
support; LH1 supplies its lift.

There are at most `N_sigma` nonempty configurations: choose the report and a
nonempty subset of its private fiber. Suppose a shortest failed path has `m`
edges. Its `m` configurations before the final empty update are nonempty. If
two of them agreed, delete the intervening action/report segment. The repeated
configuration includes its report, so the remaining quotient path is still
admissible; the deterministic support update makes it fail as before. This
contradicts shortestness. Hence `m<=N_sigma`. Ordinary breadth-first search
over the complete finite graph finds a shortest failure or exhausts it. QED.

**Quantifier distinction.** LH2 is an existential lift for each entire path,
not a lift from every private representative. Requiring for every `x` and every
quotient edge leaving `q(x)` some matching outgoing private edge is sufficient
by induction, but unnecessary: two initial same-report states `good,dead`,
with only the self-loop `good --a--> good`, lift every abstract path using
`good`; `dead` fails the stronger back condition.

No source-size-independent local window can replace LH2. For any `k>=1`, take
states `0,...,k`, all with the same report, initial state `0`, and only the
edges `i --tick--> i+1`. The quotient has a self-loop, every word of at most
`k` actions lifts, and the word of `k+1` actions does not. Every contiguous
`k`-action report window of that failed word is itself realizable. This is an
exact family of counterexamples, not evidence of infinite undecidability.

## 5. Strict separations and exact arithmetic receipts

### 5.1 Matching report interfaces do not match private interfaces

One original has states `p,u,v,q`, reports `P,M,M,Q`, initial state `p`, and
exactly `p --a--> u` and `v --b--> q`. The projected local sections `(P,M)`
and `(M,Q)` agree on their overlap, and uniquely glue as the report `(P,M,Q)`.
Both edges have true-source witnesses. No private history glues: `u != v`.
The exact reachable layers are `{p},{u},empty`. At the middle report, projection
has replaced an empty private fiber product by a nonempty report fiber product.

There is a unit flow on the report graph but none on the private graph. Adding
the actual transition `u --b--> q` repairs the obstruction; the previous cut
fails verification. This is the negative/positive mutation control.

### 5.2 Fractional local feasibility does not imply discrete gluing

Impose on binary variables the three equations

\[
x_0+x_1=x_1+x_2=x_2+x_0=1. \tag{5.1}
\]

The exact rational vector `(1/2,1/2,1/2)` satisfies every equation and every
bound `0<=x_i<=1`. No binary vector does: summing yields
`2(x_0+x_1+x_2)=3`. The equality matrix has determinant `2`, so this is not
the integral path-flow polytope. Farkas cannot certify this rational LP as
infeasible; it is feasible. Its integer infeasibility requires the parity
argument or a discrete solver/certificate.

The same cycle also has compatible local probability laws: on each variable
pair put mass `1/2` on `01` and `1/2` on `10`. Every singleton marginal is
fair, yet no joint nonnegative law has these three pair marginals. To certify
this *different*, global-coupling LP obstruction, note that every binary
assignment satisfies

\[
 [x_0\ne x_1]+[x_1\ne x_2]+[x_2\ne x_0]\le2,
\]

whereas the prescribed pair laws give expectation `3`. The test enumerates
all eight assignments to independently verify the bound. This is the classical
contextuality distinction between compatible local distributions and a global
distribution. It does not refute LH1, whose full private network contains no
cyclic consistency constraint omitted from its interfaces.

### 5.3 All report paths lift, but no public action is safely available

One original has initially possible states `zero,one`, both reporting
`unknown`, and a terminal state reporting `done`. The only edges are
`zero --a0--> end` and `one --a1--> end`. Every projected path lifts. A public
observer who knows only `unknown` nevertheless has no non-stopping action
enabled on every compatible private state. Choosing an existential witness
with advance knowledge of the requested path does not supply a robust public
policy. NO-GHOST's policy machinery remains a distinct required gate.

### 5.4 Every word has a lift, but no online lift resolver exists

The distinction persists even with a **known unique initial private state**.
Take `p,u,v`, all with report `y`, initial state `p`, and actions `a,b`. For
either action, `p` has both successors `u,v`. State `u` has both successors
`u,v` under `a` and none under `b`; state `v` has both successors `u,v` under
`b` and none under `a`. The complete reachable support configurations are
exactly `{p}` and `{u,v}`. Either action sends either reachable support to
`{u,v}`. LH2 therefore proves that **every finite action word has a lift**.

An online resolver receives the current requested action and must choose its
next private state before seeing the next request. After the first request
`a`, it must choose `u` or `v`. If it chooses `u`, the next request `b` is
impossible. If it chooses `v`, the next request `a` is impossible. Thus

\[
 (\forall\text{ finite words }w)(\exists\text{ private lift of }w)
 \quad\not\Longrightarrow\quad
 (\exists\text{ online resolver})(\forall\text{ requests})\text{successful lift}.
\]

This defeats even a resolver with complete private-state knowledge, so granting
only public reports cannot fix it. The adversary observes the selected state;
randomization cannot guarantee success against such an adversary either.
The finite test independently checks the exact closed powerset certificate,
all words through length five, and the hostile second action for both possible
first successors. The all-length result uses the two-configuration proof.
The distinction is classical history determinism, not a newly discovered
obstruction; see Boker--Lehtinen in the comparison below.

## 6. Primary-source comparison and contribution boundary

| Closest source | Relationship to this dossier | Status of contribution |
|---|---|---|
| Rabin--Scott, *Finite Automata and Their Decision Problems*, IBM J. Res. Dev. 3 (1959), 114--125, [DOI](https://doi.org/10.1147/rd.32.0114) | Powerset memory and finite language checking; LH2 is an explicit source/report-specialized construction | CLASSICAL mechanism; no automata novelty |
| Ford--Fulkerson, *Maximal Flow Through a Network*, Canad. J. Math. 8 (1956), 399--404, [original PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5D6E55D3B06C4F7B1043BC1D82D40764/S0008414X00036890a.pdf/div-class-title-maximal-flow-through-a-network-div.pdf), Theorem 1 | Cut/flow duality; the acyclic unit-flow proof and binary dual above are elementary specializations | CLASSICAL mechanism; no optimization novelty |
| Abramsky--Brandenburger, *The Sheaf-Theoretic Structure of Non-Locality and Contextuality*, [arXiv:1102.0264v7](https://arxiv.org/html/1102.0264v7), sections 3, 4.3, 6 | Compatible local distributions, global sections, linear systems, and support obstructions | Odd-cycle control is CLASSICAL contextuality |
| Gogioso--Pinzani, *The Sheaf-Theoretic Structure of Definite Causality*, [arXiv:2103.13771](https://arxiv.org/abs/2103.13771), Proposition 8 | Causal sections and gluing for a specified causal scenario | General causal sheaf novelty is not claimed |
| Clarke--Grumberg--Jha--Lu--Veith, *Counterexample-Guided Abstraction Refinement*, CAV 2000, [original paper](https://web.stanford.edu/class/cs357/cegar.pdf), introduction and abstract-path validation | Existentially projected transition systems admit spurious paths; their concrete prefixes are checked before refinement | The projected/private distinction and path-validity test are CLASSICAL, not new SUCC discoveries |
| Boker--Lehtinen, *Token Games and History-Deterministic Quantitative Automata*, [arXiv:2110.14308](https://arxiv.org/abs/2110.14308), introduction and section 4 | Resolving nondeterminism from prefixes is a stricter requirement than existence of accepting runs; finite-word history determinism has established game characterizations | Section 5.4 is a concrete CLASSICAL separation; no new general synthesis theorem is claimed |

The five sources after Rabin--Scott were read in primary full-text form in this round.
The Rabin--Scott publisher record and bibliographic identification were
retrieved, but two hosted scanned full-text retrievals failed; no specific
unread numbered theorem is attributed to it. LH2 is proved fully above.

The implemented gain for SUCC is a usable audit contract: declaration of a
complete source carrier, preservation of the original label, separate report
and private interfaces, explicit all-path quantifiers, a short obstruction
certificate, and an integrality boundary. This is mathematically more useful
than declaring a report assignment to be a source realization. It is not
evidence that these elementary ingredients constitute a new published theorem.

## 7. Reproduction, claim ledger, and next falsification

Code: [`lawful_history_gluing.py`](../../observational_succ/lawful_history_gluing.py).
Tests: [`test_lawful_history_gluing.py`](../../tests/test_lawful_history_gluing.py).

Before changes, the NoGhost/source-field baseline passed **51 tests** with:

```sh
python -m unittest tests.test_no_ghost tests.test_no_ghost_gluing_examples tests.test_source_field_gluing -q
```

`python -m pytest ...` was attempted first and could not run because pytest is
not installed; the repository's unittest runner was then used. The new suite
contains **13 tests**, including all **192** two-state one-action table/report/
initial-support combinations, a separate Cartesian-product path oracle,
**1,000** fixed-seed four-state/two-action holdout words, exact rational flow
checks, and forged-certificate mutations. The combined relevant run passed
**64 tests**. These finite tests validate code and examples; the universal
statements derive their authority from the displayed proofs.

| Claim | Label | Next verdict-changing probe |
|---|---|---|
| LH1 equivalence and binary cut dual for complete private layered networks | PROVED LOCAL / CLASSICAL core | Independently reconstruct incidence signs and test a malformed middle interface |
| LH2 uniform criterion and bound (4.2) | PROVED LOCAL / CLASSICAL core | Independent finite-language checker, or Lean proof of repeated-configuration shortening |
| Pairwise projected compatibility suffices for a private lift | REFUTED | Four-state counterexample; repair must add an actual transition or preserve the interface |
| Arbitrary fractional feasibility suffices for discrete gluing | REFUTED | Odd-cycle rational witness and exact parity obstruction |
| All pathwise existential lifts yield a safe public experiment | REFUTED | Two hidden initial states with disjoint enabled-action menus |
| `forall word exists lift` yields one online resolver | REFUTED | Three-state fixed-initial model; adversarial second request |
| Academic originality beyond this integration | UNVERIFIED | Broader trace-abstraction/path-lifting literature comparison |
| Tables are a complete/authentic physical source model | UNVERIFIED | An independent source acquisition and model-validation procedure |

**Dominance boundary.** This framework explains old full-interface gluing
successes and the projected-interface failure without weakening either.
The highest-value next theorem is a source-indexed **online strategy lifting**
criterion with partial availability and explicit probe/resource costs. It must
preserve the `for every compatible private state` information-set quantifier;
reusing LH2's `for every word, there exists a private path` would be invalid.
This is a target for integration with established history-deterministic
automata, imperfect-information games, and the existing NO-GHOST policy
contract, not a claim that finite online synthesis is an open classical problem.
