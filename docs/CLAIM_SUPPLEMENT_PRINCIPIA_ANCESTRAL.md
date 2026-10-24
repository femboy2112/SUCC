# Principia ancestral relations: source-relative reachability

**Status:** classical elementary mathematics, proved below; new-to-project
assembly and implementation. Scholarly novelty is not claimed. The historical
connection is documented in [Principia and SUCC](PRINCIPIA_CONNECTION.md).
Formal and executable validation are separate authorities. The
[kernel receipt](../research/2026-10-24/principia_receipts/kernel.json) exports
nine actual Lean theorem types, each with no axiom dependencies, and two
positive/negative mutation pairs. The [finite model receipt](../research/2026-10-24/principia_receipts/exact-model.json)
and [focused test log](../research/2026-10-24/principia_receipts/focused-tests.log)
record their separate executable authority.

This supplement makes one part of that connection operational. A hereditary
predicate is an invariant of a successor relation. Such an invariant can prove
that an apparent future of an observed state is unavailable from the particular
source state that produced the observation.

## 1. Domains and conventions

Let \(X,Y\) be arbitrary sets (or types), \(R\subseteq X\times X\) a relation,
and \(q:X\to Y\) an observation map. No finiteness, surjectivity, deterministic
transition, probability distribution, or choice of a fiber representative is
assumed. Write \(R^*\) for the **reflexive transitive closure**: zero or finitely
many \(R\)-steps. Define

\[
\begin{aligned}
\operatorname{Reach}_R(x)&=\{z:xR^*z\},\\
\operatorname{Closed}_R(U)&\iff
   \forall u,v\;(u\in U\land uRv\Rightarrow v\in U),\\
\operatorname{Sat}_q(U)&=q^{-1}(q(U)),\\
aQb&\iff \exists u,v\;(q(u)=a\land uRv\land q(v)=b).
\end{aligned}
\]

\(Q\) is the existential observation relation. Each of its edges has a
source witness, but consecutive edges may use incompatible representatives
of the same observation fiber. This is precisely the defect to audit.

The historical convention needs care. In *Principia Mathematica*, Volume I,
Section E and \(*90\), the ancestral relation includes reflexivity for a point
belonging to the **field** of the original relation. Our modern \(R^*\) includes
\(xR^*x\) for every \(x\in X\), including isolated states. They agree on the
field; the distinction matters for empty relations and isolated states.
The present construction is a modern application of hereditary-predicate
reasoning, not a literal transcription of *Principia*'s foundations.

All quotient comparisons below start at an actual observation \(q(x)\).
An arbitrary \(b\notin q(X)\) has \(bQ^*b\) by reflexivity, but has no source
representative. No global off-image reconstruction is asserted.

## 2. PAP-01: the hereditary-predicate characterization

For every \(x,z\in X\),

\[
xR^*z\quad\Longleftrightarrow\quad
\forall U\subseteq X\;
  (x\in U\land\operatorname{Closed}_R(U)\Rightarrow z\in U).
\tag{1}
\]

**Proof.** A finite path preserves membership in every forward-closed set,
by induction on its length. Conversely, take
\(U=\operatorname{Reach}_R(x)\). It contains \(x\), and appending one edge
shows it is forward closed. The right side therefore gives \(xR^*z\).
This proof works without enumerating \(X\) or its subsets. The universal
quantifier over predicates is mathematical; it is not an instruction to
execute infinitely many tests. \(\square\)

This is the useful ancestral idea: a reachability assertion is constrained
by **every invariant containing the selected start**, not just by an
unrooted picture of possible transitions.

## 3. PAP-02: projection is always sound in one direction

For every \(x,z\in X\),

\[
xR^*z\ \Longrightarrow\ q(x)Q^*q(z).
\tag{2}
\]

**Proof.** Project each edge of a source path, using that edge's actual
endpoints as the existential witnesses defining \(Q\). An empty path
projects to an empty path. \(\square\)

The converse must be stated as existence of some reachable representative
of an endpoint observation. It cannot require reaching every representative
in that fiber.

## 4. PAP-03: exactly when no endpoint is invented

The following four conditions are equivalent:

1. **All-start endpoint exactness.** For every \(x\in X,b\in Y\),
   \[
   q(x)Q^*b\iff
   \exists z\;(xR^*z\land q(z)=b).
   \tag{3}
   \]
2. **Reachable observation supports are constant on fibers.** For every
   \(x,x'\in X\),
   \[
   q(x)=q(x')\Longrightarrow
   q(\operatorname{Reach}_R(x))=q(\operatorname{Reach}_R(x')).
   \tag{4}
   \]
3. **Images preserve hereditary predicates.** For every forward-closed
   \(U\subseteq X\), its image \(q(U)\) is forward closed under \(Q\).
4. **Saturation preserves hereditary predicates.** For every
   forward-closed \(U\subseteq X\),
   \(\operatorname{Sat}_q(U)\) is forward closed under \(R\).

**Proof.**

\((1)\Rightarrow(2)\): if \(q(x)=q(x')\), the two source reachable images
equal the same quotient reachable set by (3).

\((2)\Rightarrow(4)\): let \(s\in\operatorname{Sat}_q(U)\) and \(sRt\).
Choose the witness \(u\in U\) with \(q(u)=q(s)\). Since
\(q(t)\in q(\operatorname{Reach}_R(s))\), (4) supplies a \(v\) reachable
from \(u\) with \(q(v)=q(t)\). By (1), \(v\in U\), so
\(t\in\operatorname{Sat}_q(U)\). This eliminates an existential witness;
it does not require a global choice function.

\((4)\Rightarrow(3)\): let \(a\in q(U)\) and \(aQb\). A source edge
\(sRt\) witnesses \(q(s)=a,q(t)=b\). Then
\(s\in\operatorname{Sat}_q(U)\), so by (4),
\(t\in\operatorname{Sat}_q(U)\), hence \(b\in q(U)\).

\((3)\Rightarrow(1)\): take \(U=\operatorname{Reach}_R(x)\). Its image
contains \(q(x)\) and is \(Q\)-forward-closed. Formula (1), now applied to
\(Q\), gives \(q(x)Q^*b\Rightarrow b\in q(U)\). The reverse implication
is (2). \(\square\)

The pointwise condition (3) for **one chosen** \(x\) is weaker than its
all-start version. A failure at another source state does not establish
failure at the selected start. The executable audit therefore identifies
the start attached to each result or obstruction.

There is also an exact **selected-start criterion**:

\[
\bigl[\forall b,\;q(x)Q^*b\iff b\in q(\operatorname{Reach}_R(x))\bigr]
\iff\operatorname{Closed}_R\bigl(\operatorname{Sat}_q(\operatorname{Reach}_R(x))\bigr).
\tag{5}
\]

For the forward direction, a source edge out of the saturated reachable set
projects to one more quotient step from \(q(x)\). Exactness supplies a reachable
representative of its endpoint. For the reverse direction, the image of the
reachable set is \(Q\)-closed, by the same source-edge argument used above;
induction along quotient paths completes the proof. Thus one chosen source
requires only its own saturated reachable-set closure, not the all-start law.
Lean checks this as `selected_endpoint_exact_iff_saturated_reach_closed`.

## 5. PAP-04: a smallest false endpoint and a strict hierarchy

### An invented endpoint

Let \(X=\{a,b,c\}\), with the single edge \(bRc\). Set
\(q(a)=q(b)=A\), \(q(c)=B\). The observation relation has \(AQB\), but
\(\operatorname{Reach}_R(a)=\{a\}\). The selected start \(a\) cannot reach
report \(B\). Its invariant \(U=\{a\}\) is forward closed, while
\(\operatorname{Sat}_q(U)=\{a,b\}\) is not: the edge \(bRc\) escapes it.
From the other start \(b\), endpoint exactness does hold.

Three states are minimal for this false **endpoint report** phenomenon.
On a set of at most two states, either \(q\) is injective, in which case
quotient paths lift uniquely on the image, or \(q\) is constant, in which
case the only quotient endpoint from an actual observation is already
realized by the zero-step source path. One edge is minimal as well: with
no edges, both reachable report sets consist only of the starting report.

### Unpointed closure commutation can still hide the selected start

Define the direct image of a source relation by
\(q_*S=\{(q(u),q(v)):uSv\}\), restricting abstract identity pairs to
\(q(X)\). In the same three-state example,

\[
q_*(R^*)=(q_*R)^*
 =\{(A,A),(A,B),(B,B)\}.
\]

Thus even exact commutation of the two **unpointed** constructions fails
to authenticate the endpoint from the particular start \(a\). The pair
\((A,B)\) on the left is witnessed by \(bRc\), not by a path from \(a\).
Condition (3) retains the source root; an existential union over all
representatives loses it. This is an exact source-selection obstruction,
even when the unpointed relation diagram commutes.

### Exact endpoints do not preserve steps, time, or traces

Change the relation to the two-edge chain \(aRbRc\), keeping the same
observations. Both \(a\) and \(b\) can eventually reach reports \(A,B\),
and \(c\) can reach only \(B\). Thus (3) holds for every start.
Nevertheless, \(AQB\) cannot be lifted to **one step** beginning at \(a\):
its only immediate successor is \(b\), whose report is \(A\).

Equip both edges with the same action and cost \(1\), and all states with
one common source label. This is a valid partial deterministic instance
of the existing `Machine` contract. The quotient can suggest reaching
\(B\) in one action and cost \(1\); the source starting at \(a\) requires
two actions and cost \(2\). Endpoint exactness has deliberately forgotten
both quantities. This example has two observation values; a two-state,
one-report example already separates endpoint exactness from preservation
of enabledness, so no minimality of the three-state strictness example
is claimed.

These are fully specified finite source models, not numerical margins or
counterexamples to a BBP source contract.

## 6. PAP-05: a checkable obstruction certificate

Suppose a finite audit supplies:

- a selected state \(x\) and a proposed endpoint report \(b\);
- a finite quotient path from \(q(x)\) to \(b\);
- a set \(U\subseteq X\) containing \(x\), closed under every declared
  source edge, with no \(u\in U\) satisfying \(q(u)=b\).

Then the quotient endpoint is reachable but has **no source lift from
\(x\)**. This follows directly from PAP-01: any source endpoint reached
from \(x\) lies in \(U\). The quotient path is the positive witness; the
closed set is an independently checkable nonreachability witness.

A breadth-first search may choose \(U=\operatorname{Reach}_R(x)\).
The certificate's validity does not depend on trusting that search:
checking membership of the root, closure under the supplied complete
edge table, absence of the endpoint report, and the quotient path is
enough. A truncated edge table is not a certificate for a larger system.

The adapter [ancestral_observer.py](../observational_succ/ancestral_observer.py)
uses SUCC's existing finite `Machine` source model. Its reachability
analysis forgets action names, costs, and intermediate trace values.
It certifies a claim about that declared table, not the empirical
authenticity of its source labels or a real system beyond the table.

## 7. Existing authority and the useful division of work

[FutureSafeForgetting.lean](../formal/FutureSafeForgetting.lean) already
proves the stronger statement that exact partial-action descent lifts
whole quotient paths from **every representative**, preserving every
charged cost. Its Python companion
[future_safe_quotient.py](../observational_succ/future_safe_quotient.py)
checks enriched deterministic transition congruence and distinguishing
words. PAP-03 does not replace those contracts.

[EODCS_RelationalChoice.lean](../formal/EODCS_RelationalChoice.lean) and
[MetaChoiceRelationalDescent.lean](../formal/MetaChoiceRelationalDescent.lean)
already characterize descent of observable successor supports. Applying
their support perspective to \(R^*\) motivates condition (4). The
ancestral bridge here supplies the hereditary-predicate characterization,
its equivalence with exact reachability for the **iterated existential
one-step quotient**, and an invariant obstruction certificate. Existing
frozen sources are not modified.

Use endpoint analysis for an existential eventual-access question.
Use the stronger future-safe interface when the task includes a chosen
action sequence, elapsed steps, costs, rejection behavior, or the complete
observation history. Reachability alone supplies no probabilities,
visit frequencies, fairness, or universal liveness claim.

## 8. Claim ledger and remaining obligation

| ID | Claim and scope | Authority | Hostile control / next check |
|---|---|---|---|
| PAP-01 | Arbitrary-relation finite reachability equals satisfaction of every forward-closed predicate containing the selected start | CLASSICAL; paper proof in §2; Lean declaration in `PrincipiaAncestral.lean`, kernel receipt linked above | Empty relation and isolated-state reflexivity; preserve the historical field convention |
| PAP-02 | Actual finite paths project to quotient paths | CLASSICAL; paper proof in §3; Lean declaration, kernel receipt linked above | The converse without extra premises fails at §5 |
| PAP-03 | All-start endpoint exactness iff saturation preserves all hereditary predicates; equivalently the reachable report support is constant on fibers | CLASSICAL ELEMENTARY SYNTHESIS; paper proof in §4; main equivalence formalized in `PrincipiaAncestral.lean`, kernel receipt linked above | Three-state false endpoint; exhaust finite relations and partitions independently |
| PAP-04 | Endpoint exactness is strictly weaker than exact one-step/path lifting; unpointed closure commutation does not imply selected-root exactness; three states are minimal for a false endpoint report | PROVED PAPER; exact finite source models in §5 | Chain passes endpoint condition but fails one-step and cost preservation; the minimal ghost has a commuting unpointed closure diagram |
| PAP-05 | A rooted forward-closed set and quotient path certify a spurious selected-start endpoint | PROVED PAPER; Lean invariant lemmas; executable adapter and focused test receipt linked above | Reject altered root, escaping source edge, endpoint membership, or invalid quotient path |
| PAP-06 | This bridge by itself proves selected-source frequency cancellation, π normality, RH, or a foundation equivalent to *Principia* | NOT ESTABLISHED; no such implication asserted | Need an independent theorem for the actual source and target observable |

### Reproduce and use the bridge

From the repository root:

```sh
python -m unittest discover -s tests -p 'test_ancestral_observer.py' -v
python scripts/principia_ancestral_probe.py
python scripts/check_principia_lean.py --output /tmp/principia-kernel.json
```

The tests compare BFS with independent Boolean-matrix transitive closure and
enumeration of every hereditary subset for all 2,594 relation/partition models
with one to three states. They also reject a forged path which escapes a closed
set's observed image and returns to a genuinely reachable endpoint. These are
finite validation cases; the arbitrary-type theorem is the separate paper/Lean
result. The checker uses the repository's pinned Lean 4.14 and needs no mathlib.

For an existing `Machine`, keep the chosen source state explicit:

```python
from observational_succ.ancestral_observer import audit_ancestral_observer
from observational_succ.future_safe_quotient import audit_representation

# labels is a tuple of strings aligned with machine.states.
endpoint = audit_ancestral_observer(machine, labels, selected_start)
if not endpoint.endpoint_exact:
    print(endpoint.obstruction)  # quotient path plus hereditary obstruction
trace_contract = audit_representation(machine, labels)
```

`endpoint.endpoint_exact` answers only the chosen finite-table endpoint question.
`trace_contract` separately checks the existing stronger observer contract. Neither
Boolean authenticates the original source or grants an infinite-time conclusion.

**Next useful question.** For a particular proposed SUCC observer, can a
source-defined hereditary invariant containing the authenticated start
exclude an apparent abstract continuation, or can PAP-03 justify its
eventual endpoint claims? That is a specific diagnostic, with either a
path or an invariant certificate as evidence. The π application would
additionally require control of the actual selected orbit's signed
correlations. Existential eventual reachability has no such quantitative
content, so this result does not change the normality verdict.
