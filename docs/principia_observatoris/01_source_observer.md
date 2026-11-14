# Liber Primus — De Fonte et Observatore

## 1. Scope and authority

This book gives a small **operational kernel**, not new foundations for set theory
or a claim that every physical system has already been modeled. The ambient
mathematics is ordinary sets, functions, finite lists and relations. The kernel
supports exact preservation statements; geometry, effective computation and
physical source adequacy require extra hypotheses.

The organizing distinction inherited from [SUCC Foundations](../FOUNDATIONS.md)
and [Architecture](../ARCHITECTURE.md) is retained: a carrier, a possible
interaction, an actual record, an interpreted model and a proof are different
objects. No axiom identifies them. Sections below give full elementary proofs;
these are not new Lean formalizations. Existing Lean declarations are explicitly
identified where used. No scholarly priority is claimed.

## 2. A typed interaction kernel

**Definition PO-D1 (carrier signature).** A relational carrier is

\[
\mathcal C=(X,A,O,R),\qquad
R\subseteq X\times A\times O\times X.
\]

Here \(X\ne\varnothing\) is the state set; \(A\) consists of declared
interventions, including their settings and contexts; \(O\) is a disjoint union
of typed output alphabets. The tuple \((x,a,o,x')\in R\) means that intervention
\(a\), applied at \(x\), may return \(o\) and leave \(x'\). The source identity,
clock, environment, exhausted instruments and remaining budget must be included
in the state when future legality depends on them. Omitting them is a substantive
model choice, not a Markov theorem. The relation contains no probability or
amplitude information.

A **possible finite execution** is a path

\[
x_0\xrightarrow{a_1/o_1}x_1\cdots
 \xrightarrow{a_n/o_n}x_n
\]

whose edges lie in \(R\). Its public transcript is the finite list
\(h=((a_1,o_1),\ldots,(a_n,o_n))\), with settings, clock labels and provenance
retained whenever relevant. The empty execution is permitted. Concatenation is
associative on executions with matching boundary states; this follows from
concatenation of lists. It is **not** an additional causal axiom. Two lists of
locally possible observed edges need not have a common source lift.

**Evidence-admissibility convention PO-E1.** A *realized record* is a separately
supplied record of a performed interaction, with its intended source and output
interpretation. Mathematical consistency requires a possible execution that
realizes it. A proposed path, simulated path or nonzero predicted probability
is not thereby a performed external event. In an exact finite simulator, executing
the transition rule realizes an event *of that simulation*. An external use also
requires a justified source/instrument map, discussed in Book III.

This convention cannot be manufactured from a theorem about \(R\): the same
abstract \(R\) is compatible with different claims about what was performed.
The theory can audit record consistency; it cannot establish external contact
merely from its own symbols. A **causal contact in this model** is the selected
interaction edge together with its realized receipt, not just the existence of
an edge somewhere in \(R\).

### What is primitive, and what is optional?

| Item | Exact type and role | Model / countermodel | Dependence |
|---|---|---|---|
| Typed state and interaction data | Sets \(X,A,O\), relation \(R\); structural declaration | Any finite transition table; an output in the wrong alphabet is ill typed | All operational statements |
| Record consistency | A finite record has a witnessing \(R\)-path; observational premise when the record is used | A replayed lawful path; a purported edge absent from the table fails | Claims conditional on that record |
| Determinism | At most one pair \((o,x')\) for each \((x,a)\); optional structural assumption | Bit flip satisfies it; a coin relation with two outputs violates it | Deterministic quotient and controller results |
| Totality | Every \((x,a)\) has a successor; optional | Total bit flip versus a once-only probe | Not required for PO-Q1 |
| Finite/effective presentation | Enumerated finite sets and decidable transition table, or a separately specified computable presentation | Rational finite machine; arbitrary real-valued source parameters need not have such a presentation | Executable verification, not abstract factorization |
| Persistent memory | Earlier record entries remain available; optional computational assumption | Append-only journal versus a one-bit overwriting register | Monotonicity of knowledge of fixed past targets |
| Nondisturbing observation | A designated observation leaves specified future target laws invariant; optional | Reading a classical bit versus resetting it after reading | Joint executability and effective classical descriptions |
| Source adequacy | Intended external interactions are represented by the declared source map and laws; separate observational/physical premise | A calibrated instrument can support it; a mislabeled wire can violate it while the formal model remains consistent | Application of a model theorem to the intended source |

Typing constraints are definitions, not independent physical axioms. The finite
models below establish consistency relative to the ambient mathematics. The
countermodels show that the listed optional assumptions do not follow from the
kernel. The kernel supplies no metric, spacetime, reset operation, infinite
memory, oracle or universal proof rule.

## 3. Deterministic, stochastic and quantum semantics remain distinct

The relation is a common **possibility interface**, not a claim that the three
following structures have the same operations.

* A deterministic instrument is a partial function
  \(F_a:X\rightharpoonup O\times X\). Its graph gives \(R\).
* A finite stochastic instrument specifies nonnegative numbers
  \(K_a(x;o,x')\), summing to one over \((o,x')\) for every enabled \((x,a)\).
  Sequential probabilities are obtained by multiplication along paths and
  summation over hidden intermediate states. Its support gives a relation,
  but that relation forgets probability distinctions.
* On a finite-dimensional Hilbert space, a quantum instrument is a family of
  completely positive maps \(\mathcal I^a_o\) whose sum is trace preserving.
  At density operator \(\rho\),
  \[
  p(o\mid a,\rho)=\operatorname{tr}\mathcal I^a_o(\rho),\qquad
  \rho'={\mathcal I^a_o(\rho)\over p(o\mid a,\rho)}
  \quad(p(o\mid a,\rho)>0).
  \]
  Unnormalized branches compose linearly; normalization after conditioning is
  nonlinear. Zero-probability branches do not define a posterior. Passing to a
  classical support relation forgets these linear, convex and tensor structures.

For stochastic or quantum sources, equality of *all transcript laws* is a
reasonable theoretical equivalence. It is not exact identification from a finite
sample. Book III supplies the elementary positive-support obstruction. Equality
of one-point means is weaker still. Neither correlation nor entanglement alone
is an intervention channel.

**Concrete models.** Let \(X=\{0,1\}^2\); an action flips the first coordinate,
and a nondisturbing action reads it. The second coordinate is permanently hidden.
This finite model is deterministic, total and exactly implementable. A different
carrier may flip the hidden coordinate at every action and give exactly the same
public transcripts. Thus public behavior does not determine hidden dynamics.
A stochastic extension flips the first bit with rational probability \(1/3\).
A qubit instrument with branches \(P_o\rho P_o\), for the two orthogonal
computational-basis projections \(P_o\), provides the quantum model. Repeating
that measurement has stable same-basis outcomes; this does not expose arbitrary
coherence or make every intervention nondisturbing.

## 4. What an observer is

**Definition PO-D2 (operational observer).** Relative to \(\mathcal C\), an
observer is a declared interaction/readout role, optionally implemented by a
controller

\[
\mathcal O=(M,m_0,\pi,\delta,\eta).
\]

Here \(M\ne\varnothing\) is a memory set, \(m_0\in M\), the policy
\(\pi:M\to A\cup\{\mathrm{stop}\}\) selects an intervention, the memory
update \(\delta:M\times A\times O\to M\) processes a returned outcome, and
\(\eta:M\to Z\) is a declared interpretation/report map. For a single externally
scheduled measurement, the instrument's immediate output \(o\in O\) is already
a readout; no autonomous controller or stored memory is needed to define that
role. If a controller must retain the variable outcome and later report it via
\(\eta\), its memory must distinguish those outcomes; if it must act and then
stop autonomously, its memory must also distinguish the two control stages. A target
\(P\) is required to assess **what the observer can determine**. Resource bounds
restrict allowable controllers/executions; they are not inferred from finiteness
of an output alphabet.

A controller is *finite-memory* when \(M\) is finite. A finite-stage observer
merely has a finite record at the stage in question. The two notions differ:
writing an unbounded append-only journal requires an enlarging record carrier,
even when each individual update is finite. No finite register is silently
identified with the complete history.

The combined source/controller state is \((x,m)\in X\times M\); a lawful edge
with \(a=\pi(m)\) updates it to \((x',\delta(m,a,o))\). The combined system is
another carrier of the same relational type. Thus an observer can be inside the
model without a circular definition or an infinitely nested observer. A subsystem
is an observer *for this theory* when a declared boundary, interaction menu and
readout interpretation give it this role. There is no further theorem asserting
that some special intrinsic substance distinguishes observers from subsystems.

A policy chosen under uncertainty must be lawful at every surviving state unless
an actual rejection interface is included. The observer does not gain hidden-state
information merely because a simulator can inspect \(x\).

## 5. Exact action descent, with source and costs intact

For this theorem use SUCC's existing partial deterministic **Moore** convention:

\[
r:X\to Y,\qquad S_a:X\to 1+(X\times K).
\]

Here \(r\) is a report; \(1\) denotes a blocked action; \(K\) is an exact cost
label set. A successful step returns its next state and charged label. The finite
structural trace includes the initial/intermediate reports, every charge and any
blocked marker. Costs need no addition for the preservation theorem. Additive
nonnegative costs and budget states are extra structure for optimization.

A structural report or blocked marker is operationally available only if the
instrument contract says so. In particular, structural enabledness is not an
observed event merely because it appears in the table. This is the same caveat as
in [FutureSafeForgetting.lean](../../formal/FutureSafeForgetting.lean).

**PO-Q1 (exact quotient criterion; EXISTING CLASSICAL SUCC RESULT).** Let
\(q:X\twoheadrightarrow\bar X\), with \(\bar X=q(X)\). An exact quotient
\((\bar r,\bar S_a)\), satisfying

\[
r=\bar r q,\qquad (1+q\times\mathrm{id}_K)S_a=\bar S_a q,
\tag{Q1}
\]

exists if and only if, for every \(x,x'\) with \(q(x)=q(x')\), their reports
coincide and their projected partial step results coincide for every \(a\).
It is unique on \(q(X)\). Every successful quotient path lifts from **every**
representative of its initial class with the same action word and cost sequence;
all finite structural traces agree.

**Proof.** Necessity follows by substitution in (Q1). For sufficiency, define
\(\bar r(qx)=r(x)\) and \(\bar S_a(qx)=(1+q\times\mathrm{id}_K)S_a(x)\).
Fiber constancy makes each value well defined, including blocked status.
Surjectivity gives uniqueness. For a successful quotient edge from \(q(x)\),
(Q1) excludes a blocked source result and supplies a source edge from that very
\(x\) with the specified successor class and cost. Induct on the remaining word
to lift the whole path. The same induction, including the blocked case, preserves
structural traces. This is quotient factorization, not an empirical experiment.
\(\square\)

The existing formalization supplies a section to construct representatives
without a choice axiom. Exact declarations are `fiber_safe_iff_descent`,
`descended_structure_unique`, `finite_trace_preserved`, `availability_reflected`,
and `quotient_path_lifts_from_each_representative`. The current book does not
upgrade their historical kernel receipt into a new run. The Python interface is
[future_safe_quotient.py](../../observational_succ/future_safe_quotient.py).

**Why the full condition is necessary.** Let \(a\to b\to c\), with unit-cost
steps of the same action, and \(q(a)=q(b)=A,q(c)=B\). Every representative of
\(A\) eventually reaches the same report set \(\{A,B\}\), but from \(a\) the
report \(B\) needs two steps and from \(b\) it needs one. Endpoint agreement
therefore loses time, costs and traces. This is exactly existing **PAP-04**.
With only the edge \(b\to c\), the same quotient invents endpoint \(B\) from
selected start \(a\). Existing **PAP-03** proves that endpoint exactness is
equivalent to saturation preserving hereditary predicates; it is weaker than Q1.
See the [ancestral supplement](../CLAIM_SUPPLEMENT_PRINCIPIA_ANCESTRAL.md).

## 6. Behavioral equivalence and the surviving reconstruction statement

For the deterministic report/step convention above, write \(x\equiv x'\) if
every finite requested action word has the same structural trace from \(x,x'\).
When some structural markers are not observable, use only the actual operational
trace alphabet; the following structural theorem must not be misreported as
physical distinguishability.

**PO-Q2 (behavior quotient; CLASSICAL / existing SUCC specialization).** The
relation \(\equiv\) is an equivalence and satisfies Q1's fiber condition. It is
the coarsest equivalence that satisfies that condition. Consequently the quotient
preserves every declared finite future report/cost/rejection trace, but need not
preserve hidden states, hidden topology or probabilities absent from the contract.

**Proof.** Equality of every trace is reflexive, symmetric and transitive. The
empty word gives equal current reports. One-letter words give equal enabledness
and charge. When the action succeeds on both sides, equality of traces for every
word \(av\) implies equality of the tail traces for every \(v\); their successors
are therefore equivalent. Q1 applies. Conversely, Q1's trace preservation puts
every fiber of any lawful quotient inside \(\equiv\). \(\square\)

For total deterministic instruments with finite state set \(X\), the existing
[carrier-relative target theorem](../CARRIER_RELATIVE_TARGETS.md), §2, identifies
the algebra generated by readout indicators, their transition pullbacks and
pointwise products with all functions constant on behavioral classes. Its
dimension is \(|X/{\equiv}|\). This is the finite algebraic realization of Q2;
products retain joint distinctions that marginal linear statistics omit. The
present kernel does not rename this theorem as a new discovery.

The familiar coalgebra view packages deterministic dynamics as
\(X\to Y\times X^A\); the partial/cost version changes the functor. Rutten's
[primary CWI report](https://ir.cwi.nl/pub/4802), §§2–3 and 7–9, develops systems,
homomorphisms and bisimulation. It is an antecedent, not a source of automatic
physical interpretation. Our explicit finite-path proof is enough for Q1–Q2.

## 7. The existing stochastic source-indexed interface

The relational kernel does not replace the stronger joint-law interface already
in [carrier_indexed.py](../../observational_succ/carrier_indexed.py) and the
[carrier-indexed history dossier](../../research/2026-10-13/CARRIER_INDEXED_HISTORY_THEORY.md).
Their permanent original-source labels must remain attached when current
states change. The precise prior claim identifiers are
[O663/ST1–2 and O664/ST3](../CLAIM_LEDGER.md): all-prior joint-kernel descent
and its finite-history composition, respectively.

**PO-Q3 (finite joint-law descent; EXISTING SUCC RESULT).** Let \(X,S,O\) be finite with \(S\ne\varnothing\),
\(q:X\twoheadrightarrow Y\), and let an enabled stochastic instrument have
joint kernel \(K_a(x;o,x')\). A kernel \(\bar K_a(y;o,y')\) preserves the joint
original-source/observed-current update for every nonnegative initial table
\(J:S\times X\to\mathbb R_{\ge0}\) iff

\[
\sum_{x':q(x')=y'}K_a(x;o,x')
\]

is constant as \(x\) varies in each \(q\)-fiber, for every \(o,y'\). For partial
instruments, enabledness must also be constant on fibers. Under these conditions,
each actual-outcome branch preserves its total probability and its original-source
posterior whenever that probability is nonzero.

**Proof.** Write the displayed common value as \(\bar K_a(qx;o,y')\). For outcome
\(o\), the projected updated table satisfies

\[
\begin{aligned}
(q_*J'_o)(s,y')
&=\sum_xJ(s,x)\sum_{x':q(x')=y'}K_a(x;o,x')\\
&=\sum_y(q_*J)(s,y)\bar K_a(y;o,y').
\end{aligned}
\]

This is exactly update after projection. Conversely, applying update commutation
to point-mass priors at each \((s,x)\) proves row constancy. Summing the identity
over \(s,y'\) preserves branch probability; summing only over \(y'\) and dividing
by that positive probability preserves the posterior on \(S\). Induction gives
all finite compositions. \(\square\)

Passing from the full joint kernel to its support loses weights; passing to
separate next-state and outcome marginals can lose their correlation. Neither
operation licenses Q3's converse. No arbitrary noncommutative quantum quotient
is asserted here. Book V treats a restricted commuting-algebra quantum case.

## 8. The corrected dependency order

There is no compulsory linear chain from carrier to proof. The verified arrows
are:

* A typed carrier and a declared interaction yield a *possible* execution law.
* A performed, correctly interpreted interaction yields an actual record.
* A record plus source hypotheses yields a compatible-source fiber.
* A target constant on that fiber is mathematically identified; an executable
  decoder and source adequacy are additional obligations.
* An exact action quotient transports specified dynamics and histories; an
  arbitrary observation map need not do so.
* Geometry requires additional response/cost/topological structure; proof uses
  premises and valid inference and can justify source laws before sampling them.

Book III makes the identification/execution/source split exact. Book II adds
linear causal transport and operational geometries. Neither is a consequence of
causal contact alone. The next reusable problem is to certify the relevant
quotient and target on a source whose complete transition table is unavailable,
using sound structural laws and quantitatively sufficient probes.
