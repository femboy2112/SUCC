# Future-safe forgetting with partial actions and exact resource thresholds

Date: 2026-10-18. Lane A of Academic Transmutation. Baseline:
`f309d9104ba480c1999c962af1df7c50f19e1bfe` (PR #177 lineage).

**Verdict.** The appropriate deterministic object is a source-typed partial
Moore/Mealy machine whose state contains sufficient history. Its behavioral
quotient is classical. The useful increment here is a complete, executable
contract for costs, partial availability and designated task outcomes; the
separation of task recoverability from autonomous representation updates; an
exact minimum distinguishing-budget theorem; and independently replayable
minimality/obstruction certificates. Academic priority of the specialized
resource theorem is **UNVERIFIED**. No new general coalgebra theorem is claimed.

## 1. Prior work and project delta

The repository already contains the total deterministic quotient theorem in
[B15](../2026-10-13/SWARM_ATLAS/B15.md), one-step source-change descent and
minimal pair repair in `observational_succ/causal_nerode_succ.py`, and Lean
proofs of action closure and a globally verified stationary partition plateau
in `formal/EODCS_ActionClosure.lean` and `formal/EODCS_NerodePlateau.lean`.
Those are prerequisites, not results discovered here.

Primary sources checked on 2026-10-18:

* E. F. Moore, *Gedanken-Experiments on Sequential Machines*, 1956,
  pp. 129–153, especially the partition refinement argument of Theorem 6:
  [original chapter scan](https://www.cs.cmu.edu/~cdm/resources/Moore1956-gedanken-experiments.pdf).
  The chapter treats deterministic experimental equivalence and finite
  distinguishing experiments. Its step-count convention includes observations;
  our lengths count requested actions.
* J. J. M. M. Rutten, *Universal coalgebra: a theory of systems*,
  *Theoretical Computer Science* 249 (2000), 3–80, §3.8, Theorems 7.4 and 9.3:
  [primary paper](https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf),
  [institutional record](https://ir.cwi.nl/pub/48/).
  Moore/Mealy systems, behavioral quotients and their factorization are existing
  coalgebraic mathematics.
* A. Silva, F. Bonchi, M. Bonsangue and J. Rutten,
  *Generalizing determinization from automata to coalgebras*:
  [author paper record](https://arxiv.org/abs/1302.1046).
  Its examples already include partial Mealy machines. Adding partiality or
  decorating outputs with source/proof labels is not a novelty argument.

The new code changes none of these older modules. It provides a finite exact
instance of the classical functor

\[
 F(X)=Y\times\bigl(1+(\mathbb Q_{\ge0}\times X)\bigr)^A.
\]

The resource threshold below is a shortest-path calculation on a synchronized
pair graph. Comparison with weighted-testing and resource-bisimulation
literature remains necessary before claiming originality. It is not a POMDP
abstraction theorem: this contract has deterministic transitions, exact
reports, and no probabilities or approximation bounds.

## 2. Minimal declared object and observation contract

Fix a set of states/histories \(X\), an action alphabet \(A\), a source-index
set \(I\), an ordinary report set \(O\), and designated task result sets
\((T_j)_{j\in J}\). Let

\[
 y:X\longrightarrow Y=I\times O\times\prod_{j\in J}T_j,
 \qquad D_a\subseteq X,\quad
 \delta_a:D_a\to X,\quad c_a:D_a\to\mathbb Q_{\ge0}.
\]

Every field is a mathematical premise. The source index is **mandatory
preserved output** in this version, so differently indexed states cannot be
identified. Cross-source transitions are permitted when an actual table edge
declares them; no undeclared source transport is inferred. If a different
application treats source identity as hidden, it has chosen a different
output map and must recompute the quotient.

The state must make the transition contract stationary. It may contain an
original source, a current carrier, past receipts, a clock, and remaining
resources. Full histories always provide a formal Markovization when the
history law is deterministic; whether a *finite* sufficient summary exists is
a separate problem. Membership in the mathematical history space does not
assert that a history occurred, that it is resettable, or that two mutually
exclusive continuations can both be actualized.

An enabled action emits its exact cost and the target report. An unavailable
request has a distinguished rejection response and ends that trial. Thus a
word denotes a **specification experiment**. Interpreting it as a lawful
physical experiment additionally requires a request/rejection or menu
interface: requesting an unavailable source operation must be permitted and
must reveal rejection without performing that operation. Without this
interface, an availability mismatch is a structural lawfulness obstruction,
not an experimentally observed difference. Rejection cost is zero in this
contract; nonzero probing or rejection costs require an expanded machine.

Let \(\tau_x(w)\) be the finite transcript for \(w\in A^*\): initial
\(y(x)\), followed by action/cost/target-report records until the word ends
or an unavailable request is rejected. Define

\[
 x\simeq z\quad\Longleftrightarrow\quad
 \forall w\in A^*,\ \tau_x(w)=\tau_z(w).
\]

The task fields can record a specified proof checker's response, a formally
given derivability predicate, or a mathematical target value. The theorem
preserves exactly the fields supplied. A string `accepted` is not a proof of
soundness; a supplied derivability table is not an algorithm for arbitrary
derivability. Preserving all future *designated* proof tasks is not preserving
all mathematical truth, all future changes of theory, or all possible new
instruments. New tasks/actions change the equivalence relation.

## 3. Future-safe forgetting and autonomous quotient theorem

**Theorem A (CLASSICAL specialization, full proof below).** Under §2's
deterministic contract:

1. \(\simeq\) is the greatest equivalence relation \(R\) such that
   \(xRz\) implies equal current outputs and, for every \(a\), equal
   availability; when enabled, equal costs and
   \(\delta_a(x)R\delta_a(z)\).
2. The projection \(\pi:X\to Q=X/{\simeq}\) carries a uniquely induced
   output, partial action and cost structure. It preserves every transcript.
3. For any surjection \(q:X\to R\), the following are equivalent:
   every \(\tau_{(-)}(w)\) factors through \(q\);
   \(\ker q\subseteq\simeq\);
   there is a unique map \(f:R\to Q\) with \(\pi=f\circ q\).
4. The representation \(q\) itself admits exact autonomous outputs,
   availability, costs and deterministic updates iff **\(\ker q\) itself
   satisfies the congruence conditions in part 1**. In this case \(f\) is
   a structure-preserving map onto the behavioral quotient.

Here a representation is autonomous when its next value is determined by
its current value and requested action, without recovering omitted source
information. This is set-theoretic well-definedness; effective computation
requires additional assumptions and is supplied here only for complete finite
tables. Part 3 alone does not promise such updates.

**Proof.** Equality of all transcripts is an equivalence relation. Evaluating
the empty word gives equality of outputs. Evaluating one-letter words forces
equal availability and, when both actions are enabled, equal costs and target
outputs. For any suffix \(v\), equality on \(av\) after the common first
record yields
\(\tau_{\delta_a(x)}(v)=\tau_{\delta_a(z)}(v)\), so successors are
equivalent. Conversely, if \(R\) satisfies the local conditions, induction
on word length proves equality of transcripts for related starts: the empty
case uses outputs; a rejected first request terminates equally on both sides;
an accepted first request emits equal costs and applies the induction
hypothesis to related successors. Hence \(R\subseteq\simeq\).

The quotient output \(\bar y([x])=y(x)\), domain
\(\bar D_a=\{[x]:x\in D_a\}\), transition
\(\bar\delta_a([x])=[\delta_a(x)]\), and cost
\(\bar c_a([x])=c_a(x)\) are well-defined by these local conditions.
They are forced by surjectivity of \(\pi\), proving uniqueness and part 2.

If all transcript maps factor through \(q\), two states with the same
\(q\)-value have every transcript equal, proving the kernel inclusion.
Given that inclusion define \(f(q(x))=[x]\). It is well-defined, unique
because \(q\) is onto, and gives \(\pi=fq\). Conversely this identity
forces equal quotient classes on every \(q\)-fiber, hence equality of all
transcripts. This proves part 3. Notice the direction: **the canonical
quotient factors through every sufficient representation**.

For part 4, any descended output/domain/cost/update has the same value on each
\(q\)-fiber; in particular
\(q\delta_a(x)=q\delta_a(z)\) on enabled fibers. This is exactly the
congruence condition for \(\ker q\). Conversely those conditions define
the descended data by representatives, with no ambiguity. The equations for
\(f\) follow by composing with the surjection \(q\). \(\square\)

**Corollary (adaptive experiments).** The relation preserves every finite
adaptive request policy whose next action/stopping decision depends only on
the transcript. Inductively equal transcripts force the same decision; the
local conditions then give the same next record. A word witness is already a
nonadaptive policy. This statement supplies no reset or parallel-copy access.

**Countermodel: safe refinement is not autonomous (PROVED LOCAL).** All three
states \(u,v,w\) have output 0 and one everywhere-enabled zero-cost action:
\(u\mapsto u\), \(v\mapsto w\), \(w\mapsto w\). Every state has
the same behavior. Yet \(q(u)=q(v)=0\), \(q(w)=1\) is future-safe and
has no descended update: the same compressed value 0 would have to update to
both 0 and 1. The unique factor to the behavioral quotient is the constant
map. Thus the claim “every refinement of the behavioral quotient is a
congruence” is **REFUTED**.

## 4. Finite obstruction certificates and a stopping theorem

Assume the **entire** model has \(n\) states and finitely many actions. Set
\(R_0=\ker y\), and define

\[
 xR_{k+1}z\iff y(x)=y(z)\ \land\
 \bigwedge_{a\in A}
 \begin{cases}
 x,z\notin D_a, &\text{or}\\
 x,z\in D_a,\ c_a(x)=c_a(z),\
 \delta_a(x)R_k\delta_a(z).
 \end{cases}
\]

**Theorem B (CLASSICAL specialization).** \(R_k\) is exactly agreement on
all transcripts of at most \(k\) requests. If \(r_0\) is the number of
initial output classes, \(R_{n-r_0}=\simeq\). Every inequivalent pair has
a distinguishing specification word of length at most \(n-r_0\), hence at
most \(n-1\). A global verified partition plateau certifies all future
words; a plateau in sampled trajectories does not.

**Proof.** The description of transcripts and induction on \(k\) identify
the recurrence with bounded-word agreement. Thus \(R_{k+1}\subseteq R_k\).
If equality occurs, the defining recurrence makes \(R_k\) a congruence;
Theorem A gives \(R_k\subseteq\simeq\), while the reverse inclusion holds
by bounded agreement. Otherwise the number of classes strictly increases.
Starting at \(r_0\), there can be at most \(n-r_0\) strict increases.
At that bound the relation has either stabilized earlier or is equality on
states, which is itself stable. A pair excluded by \(R_k\) has a word of
length at most \(k\) by the bounded-word characterization. \(\square\)

The implementation uses partition refinement to generate blocks and
breadth-first pair search to generate shortest words. A certificate consists
of a disjoint exhaustive partition plus one separating word for every pair of
distinct blocks' representatives. Verification has two logically independent
parts:

* Check all local squares inside each block: output, availability, cost and
  successor class. Induction proves no pair inside a block can be separated.
* Replay every declared separating word between blocks. Since each block is
  already behaviorally homogeneous, this proves that no two blocks can merge.

Together these prove the partition is **exactly** \(\simeq\), without
trusting the refinement algorithm or enumerating all words. Removing the
second part would certify a potentially over-refined quotient, not minimality.
The Python in-module checker shares the transcript implementation; the
separately implemented checker in `scripts/check_academic_certificate.py`
provides a second implementation route. Kernel coverage is recorded in the
integration report rather than inferred from Python tests.

## 5. Residual budgets: the correct closure law

For a nonnegative rational budget \(b\), the lawful residual state is
\((x,b)\). Define the lifted partial action

\[
 (x,b)\xrightarrow{a,c_a(x)}
 (\delta_a(x),b-c_a(x))
 \quad\Longleftrightarrow\quad x\in D_a\text{ and }c_a(x)\le b.
\]

The output remains \(y(x)\); remaining budget is stored but is **not** an
additional observed field. Unavailable and unaffordable requests both return
the same rejection. Prices of unaffordable actions are not revealed. This is
one precise interface choice; free price quotations would define a different
equivalence. Let \(x\simeq_b z\) mean equality of all transcripts starting
from \((x,b)\) and \((z,b)\).

**Theorem C (PROVED LOCAL specialization of Theorem A).** The family of
relations satisfies exactly the residual law: equal current outputs; for each
action, both starts are affordable-enabled or neither is; if both are, their
costs equal some \(c\) and

\[
 \delta_a(x)\simeq_{b-c}\delta_a(z).
\]

Equivalently, future equivalence is an ordinary congruence on the augmented
state space, with no requirement that the same relation \(\simeq_b\) be
preserved on unaugmented successors. The family is monotone:
\(b'\ge b\Rightarrow\simeq_{b'}\subseteq\simeq_b\), and

\[
 \bigcap_{b\in\mathbb Q_{\ge0}}\simeq_b\ =\ \simeq.
\]

**Proof.** Apply Theorem A to the augmented machine; each successful action
subtracts the same cost from both residual resources. A transcript available
at the lower budget can be recovered from a higher-budget transcript by
stopping at the first step exceeding the lower residual resource and recording
rejection. This proves monotonicity. Unbounded equivalence preserves all
costs, availability and outputs, so it implies every bounded equivalence.
Conversely, an unbounded word witness is finite and has finite cumulative
costs on both valid prefixes. Choose a rational budget at least both totals.
Every action before the first discrepancy is then affordable, and the same
word distinguishes at that budget. \(\square\)

For a finite rational-cost machine and a fixed initial rational \(B\), the
reachable lift from all \((x,B)\) is finite, including zero-cost cycles.
Choose a positive integer \(D\) divisible by denominators of \(B\) and
all costs. Every residual belongs to
\(\{0,1/D,\ldots,B\}\), so there are at most \(n(BD+1)\) lifted
states. This is a finiteness proof, not an efficiency claim: a large common
denominator can cause a huge expansion. The implementation has an explicit
state cap; exceeding it raises `UNKNOWN`, never “equivalent”.

**Countermodel: restarting the budget is unsound (PROVED LOCAL).** Give all
states the same source, and outputs 0 except \(q\), whose output is 1:

\[
 x\xrightarrow{a,1}u\xrightarrow{b,1}p,
 \qquad z\xrightarrow{a,1}v\xrightarrow{b,1}q.
\]

Other actions are unavailable. At budget 1, \(x\simeq_1z\): after the
common first action no budget remains. However \(u\not\simeq_1v\),
whereas \(u\simeq_0v\). The two-step word \(ab\) separates at budget
2. Thus same-budget successor congruence on bare states is **REFUTED**;
the residual-budget repair is exact.

## 6. The exact minimum distinguishing-budget theorem

This adds a useful quantitative answer: *how much resource makes discarded
information relevant?* It does not identify monetary, energetic or physical
cost unless the supplied cost function actually models that quantity.

For a finite machine construct a graph with unordered state-pairs as vertices
and an extra terminal vertex \(\dagger\). At pair \(\{x,z\}\):

1. If \(y(x)\ne y(z)\), add an edge of weight 0 to \(\dagger\).
2. If exactly one side enables action \(a\), add an edge to \(\dagger\)
   of weight equal to its enabled cost.
3. If both enable \(a\) with unequal costs, add an edge to \(\dagger\)
   of weight \(\min(c_a(x),c_a(z))\).
4. If both enable \(a\) with equal cost \(c\), add an action-labelled
   edge of weight \(c\) to
   \(\{\delta_a(x),\delta_a(z)\}\).

Let \(d(x,z)\) be the shortest-path weight from \(\{x,z\}\) to
\(\dagger\), with \(d=\infty\) if no path exists.

**Theorem D (PROVED LOCAL; academic novelty UNVERIFIED).** Under precisely
the budget interface of §5, for every \(B\in\mathbb Q_{\ge0}\),

\[
 \boxed{\quad x\not\simeq_B z\quad\Longleftrightarrow\quad
 d(x,z)\le B.\quad}
\]

A finite threshold is an attained nonnegative rational number and has an
explicit word witness. An optimal-budget witness need not have the fewest
actions. A witness can be chosen with at most \(\binom n2\) actions.
The threshold is computable directly on the pair graph, without expanding the
budget lattice.

**Proof, path implies witness.** Truncate the path at its first unequal-output
pair if necessary; its weight can only decrease. Along its case-4 prefix, both runs have
equal outputs, execute the same actions and spend the same cumulative amount
\(C\). A terminal edge in case 1 needs only budget \(C\). A terminal
edge in case 2 of weight \(c\) needs budget \(C+c\): one action then
executes and the other rejects. For case 3, suppose \(c_x<c_z\). At budget
\(C+c_x\), the cheaper action executes and the other rejects, so the
transcripts differ. At larger budgets either that affordability difference
remains or both execute and reveal different costs. Nonnegative costs ensure
every preceding common prefix was affordable. Thus the word associated to a
path of weight \(r\) distinguishes at every \(B\ge r\).

**Proof, witness implies path.** Take the first discrepancy in a bounded
distinguishing transcript. Before it, all requests must have succeeded on
both sides with identical costs: a shared rejection would end both traces
without a later discrepancy. The preceding common actions therefore follow
case-4 edges, with total cost \(C\le B\). If the first discrepancy is an
output, case 1 closes the path at weight \(C\). If only one side has an
available source action, its successful execution implies its cost is at
most \(B-C\), so case 2 closes at weight at most \(B\). If both actions
exist but have unequal costs, either one succeeds or both succeed with
different cost receipts; hence at least the smaller cost is at most
\(B-C\), and case 3 again closes at weight at most \(B\). These cases
exhaust the first discrepancy. Therefore \(d\le B\).

All graph weights are nonnegative rationals and the graph is finite. Any
successful walk can have repeated-vertex cycles removed without increasing
weight; a minimum over the finitely many simple terminal paths exists. A
separating path cannot pass through a diagonal pair \(\{x,x\}\), from
which no discrepancy is reachable. A simple path visits at most
\(\binom n2\) non-diagonal vertices. At most one requested action is
needed per visited vertex, proving the word-length bound. Dijkstra's
algorithm applies, including zero-weight edges. \(\square\)

**Sharp interface distinction.** A pair with action costs \(1/3\) and
\(1/2\), otherwise identical, has threshold \(1/3\), not \(1/2\):
affordability itself separates. If a quotation interface revealed both
prices before paying, the threshold could instead be zero. If rejection were
not lawfully observable, this case would require a different testing model.

**Cheapest versus shortest control.** One action separates after cost 7; a
two-action route separates after costs \(1/3\) and \(1/2\). Breadth-first
search chooses the first route. The resource theorem chooses the second and
certifies threshold \(5/6\). Exact tests compare that threshold with
independent residual-lift behavior below, at, and above the boundary.

## 7. Strict obstructions and what they actually rule out

**No rejection oracle: a nontransitivity obstruction (PROVED LOCAL).**
Suppose one tries to avoid the interface assumption by comparing only words
that are lawful from *both* starting states. Define
\(x\mathrel{\bowtie}z\) to mean equality of all such common-lawful
transcripts, without requiring the lawful languages themselves to agree.
This relation need not be transitive. Four same-source states \(x,y,z,q\)
have reports \(0,0,0,1\). The only edges are the zero-cost actions
\(x\xrightarrow a x\) and \(z\xrightarrow a q\). State \(y\) has
no nonempty lawful word, so \(x\bowtie y\) and \(y\bowtie z\) hold:
their only common word is empty. But \(x\not\bowtie z\), witnessed by
\(a\). Thus common-lawful agreement cannot simply replace behavioral
equivalence in a quotient theorem. Taking its transitive closure would merge
\(x,z\) and erase an actual common experiment. The obstruction is proved
by these complete tables; it is not inferred from a bounded word search.

This does not force rejection access into every physical observer model.
It shows that removing it requires changing the semantic object, for example
to policies admissible across an entire uncertainty set, rather than silently
retaining a pairwise equivalence quotient.

| Tempting claim | Exact receipt | Verdict and repair |
|---|---|---|
| Current report alone is future-sufficient | Histories 00 and 10 both display 0; the next action repeats their first bit | REFUTED; retain sufficient history or recompute its behavioral quotient |
| Same output and successor structure suffice even if costs differ | Two output-0 self-loops cost \(1/3\) and \(1/2\) | REFUTED for cost-sensitive tasks; exact costs belong to the contract |
| Omitting unavailable actions is harmless | One state has a zero-cost loop, the other rejects | REFUTED as structural quotient claim; experimental interpretation needs a lawful rejection interface |
| Comparing only mutually lawful words automatically gives an equivalence | The four-state \(x,y,z,q\) model above | REFUTED; common-lawful agreement is not transitive |
| Any sufficient refinement updates autonomously | The three-state model of §3 | REFUTED; require congruence of the actual representation kernel |
| Budget \(B\) can be reused after each action | The two chains of §5 | REFUTED; retain and subtract residual resource |
| Preservation of declared proof outcomes certifies semantic truth | Both states may carry the same unsound checker's `accepted` value | No implication; proof authority/soundness is a separate premise |
| Same finite receipts establish source authentication | Two external origins may be assigned the same declared source tag | No implication; table equality does not authenticate provenance |

The last two rows are boundaries, not claims that a new cryptographic or
logical impossibility theorem has been proved. They identify information
absent from the mathematical input.

The first three obstructions are strict failures of weakened contracts. They
do not make decorated coalgebra into a new theory. The useful engineering
result is that a proposed compression now either has an exact future-safe
certificate, an explicit local update defect, or a finite distinguishing
request with an exact resource threshold.

## 8. Executable and adversarial evidence

Files owned by this lane:

* `observational_succ/future_safe_quotient.py`: immutable exact finite contract;
  shortest-word search; partition minimization; local-square/separator checker;
  compression audit; rational budget lift; exact minimum-budget search; portable
  JSON-compatible certificate schema.
* `tests/test_future_safe_quotient.py`: independent direct-word interpreter,
  exhaustive finite corpus, held-out machines and hostile controls.

Focused baseline, before modifications:

```sh
python -m unittest discover -s tests -p 'test_eodcs_causal_nerode.py'
# 12 tests, OK
```

Focused result after the new implementation:

```sh
python -m unittest discover -s tests -p 'test_future_safe_quotient.py'
# 18 tests, OK
```

The 18 tests include all 2,744 three-state unary machines with binary outputs,
partial edges and costs 0 or 1; 120 fresh four-state, two-action machines
(seed `202610184791`) checked against direct bounded-word enumeration; and
70 fresh threshold/lift comparisons (seed `202610186113`) at five budgets
each. The exhaustion, float, nondeterminism, source-tag, proof-task, history,
zero-cost-loop, missing-separator, false-separator, redundant-split and
cost-mutation controls are explicit. The initial test expected two exhausted
states with different hidden budgets to remain separate; this was corrected
to the mathematically correct merged class, since residual budget is stored
but not observed. No theorem was altered to fit that test.

The word-enumeration oracle has different code and an exhaustive bound
justified by Theorem B; it does not derive equivalence by calling the
production partition refiner. The threshold implementation uses Dijkstra on
state pairs, whereas its holdout comparison expands actual rational residual
states and computes behavior there. These are distinct algorithmic routes,
although both are implementations of the same declared model rather than
independent empirical source witnesses. Full repository validation and the
independent checker/Lean receipts belong to the integration report.

## 9. Claim ledger and dominance boundary

| ID | Exact scope | Status | Support | Next falsification opportunity |
|---|---|---|---|---|
| FSF-A | Greatest deterministic output/cost/availability congruence and quotient factorization | CLASSICAL | Theorem A proof; Moore/Rutten; existing B15 | Nondeterministic or stochastic extension needs a new semantics |
| FSF-B | Full finite-table stopping and bounded witness theorem | CLASSICAL specialization | Theorem B proof; exhaustive oracle | Supply an omitted source state to invalidate an incomplete table certificate |
| FSF-C | Residual-budget family law and intersection over all budgets | PROVED LOCAL, classical specialization | Theorem C proof; chain countermodel | Add credit/replenishment, hidden pricing or nonzero rejection costs |
| FSF-D | Exact rational minimum distinguishing budget under the declared interface | PROVED LOCAL; novelty UNVERIFIED | Theorem D proof; pair-distance versus residual-lift holdouts | Check weighted-testing literature; independent formalization of threshold characterization |
| FSF-R1 | Safe refinement need not be dynamically autonomous | PROVED LOCAL counterexample | Three-state receipt; exact test | Any proposed strengthening must exclude this model |
| FSF-R2 | Fixed-budget equivalence on bare states need not be a congruence | PROVED LOCAL counterexample | Two-chain receipt; exact test | Explicitly track a different resource semantics |
| FSF-R3 | Agreement on common-lawful words need not be transitive | PROVED LOCAL counterexample | Four-state complete-table proof in §7; exact test | Replace pairwise comparison by uncertainty-set lawful policies |
| FSF-P | Declared task-output preservation implies sound proof or source authentication | UNVERIFIED / not entailed by contract | Missing premises identified in §§2,7 | Supply and verify the task authority and source-to-table map |

This frame dominates the prior total-action implementation for the declared
finite deterministic **resource-sensitive** use case: it recovers the old
case when all actions are total and costs are irrelevant/constant, explains
the history/cost/availability failures, and supplies exact falsifiers. It
does not dominate relational trace semantics, POMDP approximations,
uncomputable proof tasks, or physically inaccessible experimental menus.

The highest-value next foundational step is to characterize compression under
**lawful common-action policies without a rejection oracle**, especially when
history uncertainty makes availability itself unknown. In that model a
structural mismatch need not admit a common admissible discriminating test.
Conflating those two models would erase the exact observer-access obstruction
the present contract makes visible.
