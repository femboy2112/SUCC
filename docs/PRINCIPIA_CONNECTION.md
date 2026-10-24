# Principia Mathematica and the SUCC research program

**Status:** historical comparison plus a classical mathematical tool. This note records an
intellectual kinship recognized in October 2026; it does not establish direct historical
influence on SUCC, a replacement foundation for mathematics, or academic priority.

SUCC shares with Whitehead and Russell's *Principia Mathematica* the ambition to make
mathematical justification explicit. SUCC's particular emphasis is on what an observer may
infer after a source passes through a representation, quotient, computation, or limit.
The connection becomes useful when it tells us which implication needs a proof.

## The historical connection

*Principia*, Volume I (1910), develops mathematics from declared primitive ideas and
propositions. Its preface distinguishes analyzing existing mathematics for its premises
from reconstructing consequences of those premises. Chapter II uses logical types to
control expressions and avoid paradoxes. Part II, Section E treats induction through
relations: §90 defines the ancestral relation using hereditary classes; §91 studies powers
of a relation. The authors explicitly credit Frege for the ancestral construction.
[Primary text: preface](https://www.gutenberg.org/files/78050/78050-src/78050-src.htm#Page_v),
[Chapter II](https://www.gutenberg.org/files/78050/78050-src/78050-src.htm#Page_39),
[Section E](https://www.gutenberg.org/files/78050/78050-src/78050-src.htm#Page_569).

The following comparisons are our interpretation, not claims made by *Principia* about SUCC.

| Point of contact | Its use in SUCC | Boundary |
|---|---|---|
| Explicit premises and deductions | Record definitions, source hypotheses, proof dependencies, and actual theorem statements. | A claim ledger organizes evidence; it does not prove its entries. |
| Successor, induction, and ancestral relations | Prove properties of every state reachable from a specified source. | Reachability alone supplies no frequency or equidistribution law. |
| Logical type discipline | Distinguish embeddings, quotients, completions, and the operations allowed on each. | SUCC's source contracts are not Russell's ramified type theory. |
| Inspectable formal deductions | Use Lean to check the formalized portions and inspect their axiom dependencies. | Lean's modern dependent type theory is a different foundation. |

Lean elaborates statements and proofs into a core dependent type theory checked by its
kernel. That provides an operational connection to the formalization ambition, while the
meaning of a formalized statement still needs to match the intended source and target.
[Lean kernel reference](https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/#The-Lean-Language-Reference--Elaboration-and-Compilation--The-Kernel).

The [Carrier Atlas](CARRIER_ATLAS.md) gives the concrete construction side of this comparison.
The [Foundations](FOUNDATIONS.md) separate mathematical proof from physical observation and
semantic interpretation. [Observer and Proof Access](OBSERVER_PROOF_ACCESS.md) locates access
in a source–target–toolkit triple. Together these specify SUCC's research emphasis; they do
not assert that all mathematics has been reduced to SUCC primitives.

## A practical ancestral principle

**CLASSICAL; proof below.** Let \(S\) be any set and \(R\subseteq S\times S\) any relation.
Write \(R^*(x,y)\) for a finite sequence of \(R\)-steps from \(x\) to \(y\), allowing zero
steps. A predicate \(P\) is *hereditary* when

\[
\forall u,v\in S,\quad P(u)\land R(u,v)\Longrightarrow P(v).
\]

Then, for every \(x,y\in S\),

\[
R^*(x,y)\quad\Longleftrightarrow\quad
\forall P:S\to\mathrm{Prop},\quad
\bigl(P(x)\land P\text{ is hereditary}\bigr)\Longrightarrow P(y).
\]

For the forward implication, induct on the finite path length. For the reverse implication,
take \(P(z)\) to mean \(R^*(x,z)\): it contains \(x\) and is closed under one more step.
The proof is valid for infinite \(S\); checking finitely many chosen predicates is a weaker
operation than quantifying over all predicates.

Our modern convention includes an isolated state as reachable from itself. *Principia*'s
§90 restricts this reflexive case to the field of the relation. We therefore use a modern
reformulation, not a literal transcription of its definition.
[§90, pp. 576–577](https://www.gutenberg.org/files/78050/78050-src/78050-src.htm#Page_576).

This supplies two useful proof routes. A source path witnesses reachability. A hereditary
predicate containing the source and excluding the proposed endpoint witnesses
non-reachability. On a declared finite carrier, both can be checked exactly; on an infinite
carrier, a symbolic invariant can replace an unbounded search.

The [technical supplement](CLAIM_SUPPLEMENT_PRINCIPIA_ANCESTRAL.md) proves an exact
criterion for this reasoning to survive an observer quotient. It includes a Lean
formalization and an executable diagnostic using SUCC's existing source-labelled
machine model. Run `python scripts/principia_ancestral_probe.py` from the repository
root to replay the contrasting selected-source examples.

## Why the original source must remain attached

**EXACT COUNTEREXAMPLE.** Take \(S=\{a,b,c\}\), the sole edge \(bRc\), and observation
\(q(a)=q(b)=0\), \(q(c)=1\). Define an observed edge whenever some source edge realizes it.
There is then an observed path \(0\to1\), but no source path from the selected state \(a\)
to any state observed as \(1\).

The invariant \(U=\{a\}\) diagnoses the failure: it is closed under source steps. Expanding
it to every observationally indistinguishable state produces \(\{a,b\}\), which is not
closed because \(bRc\). Observing first and composing observed steps can silently change
which representative supplies the next step. A valid observation of individual edges is
therefore insufficient to authenticate a path from the selected source.

For research, this gives a concrete sequence of obligations:

1. Specify the original carrier, step relation, and selected starting state.
2. State the property to transport and prove its preservation under the actual steps.
3. If observations identify states, prove the required path or endpoint lifting property.
4. Establish the property at the selected start; an ensemble statement does not supply it.

For the π program, a finite hereditary invariant or an exact orbit representation does not
by itself bound signed Fourier averages. A normality proof still needs the authenticated
BBP initial condition and the required all-horizon cancellation. The ancestral viewpoint
helps locate an unproved transport or starting-state premise; it does not remove that
premise. This is an application of the repository's [steelman–crucible–verdict method](METHOD.md).

## Attribution and further use

The ancestral principle and induction are classical. The source and observer application
is a SUCC presentation of that tool; any claim of scholarly novelty requires a separate
literature audit. A useful next application must identify a particular representation,
prove what it preserves, and supply a source-labelled counterexample when preservation fails.

Primary historical reference: A. N. Whitehead and B. Russell, *Principia Mathematica*,
Volume I, Cambridge University Press, 1910: preface; introduction, Chapter II; Part II,
Section E, §§90–91. Section E's note 65 credits G. Frege, *Begriffsschrift* (1879), Part III,
pp. 55–87, and *Grundgesetze der Arithmetik* I (1893), §§45–46. This note checked the
Whitehead–Russell text; those Frege passages are pointers reported by that text, not an
independent audit of Frege's editions.
