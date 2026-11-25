# Knowledge volume, computational paths, and quantitative arithmetic capacity

**Date:** 2026-11-24. **Status:** exact classical linear-algebra theorem, executable finite examples, and an explicitly conjectured extension to quantitative arithmetic/analytic observer theory. This is a continuation of Principia #619, #633, not a replacement.

## 1. A mathematical object is not identical to the observer's accessible representation

Let \(V\) be a finite-dimensional \(\mathbb Q\)-vector space, \(P:V\to W\) a readout and \(A_a:V\to V\) admissible linear actions. A legal word \(w=a_1\cdots a_k\) applies \(A_{a_k}\cdots A_{a_1}\). The full *counterfactual* source-report bank through horizon \(m\) contains \(PA_w\) for all such words of length at most \(m\).

Define

\[
\mathcal K_m=
\operatorname{span}_{\mathbb Q}
\bigl\{\lambda PA_w:\lambda\in W^*,\,|w|\le m\bigr\}
\subseteq V^*.
\]

Then \(\mathcal K_m\subseteq\mathcal K_{m+1}\). Its dimension is an exact, toolkit-relative *linear* knowledge volume, not a probability of truth, a physical computation measure, or the number of path names.

A target \(t\in V^*\) is determined by all mathematically available reports through \(m\) iff \(t\in\mathcal K_m\). If \(t\notin\mathcal K_m\), annihilator duality gives a nonzero hidden witness \(v\) such that every admitted report vanishes on \(v\) but \(t(v)\ne0\). The source states 0 and \(v\) are indistinguishable to that observer but disagree on the target.

**Policy/firewall:** all-counterfactual report identification is not automatic joint *execution*. Destructive actions, finite resources and an actual source interaction require the separate Principia policy-leaf/attestation theorems.

## 2. An explicit lawful path reveals a hidden coordinate

Take \(V=\mathbb Q^3\), initial readout

\[
P=\begin{bmatrix}1&0&0\end{bmatrix},
\quad
A=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}.
\]

Then the legal chronological path reports are

\[
P=(1,0,0),\quad PA=(0,1,0),\quad PA^2=(0,0,1).
\]

Therefore

\[
(\dim\mathcal K_0,\dim\mathcal K_1,\dim\mathcal K_2,\dim\mathcal K_3)
=(1,2,3,3).
\]

The third coordinate was real in the source from the beginning but inaccessible to the initial readout. Two lawful operations transport it into the observable coordinate. No information was fabricated. The independently checked executable model retains the path words that first added new rank.

**Mutation:** duplicating an already accessible report or installing multiple differently named identity actions does not add rank. This is a concrete stop condition against counting correlated computational paths as independent proof multiplicity.

## 3. Exact independence is not analytic mass

Take \(V=\mathbb Q^2\), \(P=(1,0)\), and, for any integer \(N\ge1\),

\[
A_N=\begin{bmatrix}1&1/N\\0&1\end{bmatrix}.
\]

The source-generated report matrix is

\[
E_N=\begin{bmatrix}P\\ PA_N\end{bmatrix}
=\begin{bmatrix}1&0\\1&1/N\end{bmatrix},
\qquad \det E_N=\frac1N.
\]

For every finite \(N\), \(\dim\mathcal K_1=2\): an exact rational oracle can identify both coordinates. But its quantitative inverse is badly conditioned as \(N\to\infty\). On the hidden direction \(v=(0,1)\), the new observation is just \(1/N\). A finite-precision sensor must resolve this scale.

Thus **full knowledge rank does not imply a uniform detection bound**. Counting paths, rank increments and certified arithmetic multiplicity are different measurements.

For a linear report \(E\) on a symmetric unit-ball source and a target functional \(t\), Principia's previous minimax theorem gives the unresolved target error \(\|t|_{\ker E}\|\); this can be zero despite arbitrarily bad numerical conditioning when E is injective. Quantitative finite-precision recovery requires singular-value/source-noise bounds separately.

## 4. Correlated zero relations have their own proof-relevant geometry

A source path difference \(c\) can satisfy \(\partial c=0\) yet pair nontrivially with a cochain \(\omega\), because zero at the endpoint is not zero in the free source chain module. An exact cochain \(dg\) necessarily vanishes on every endpoint-null cycle; an arbitrary source-supported cochain may not.

There are at least four distinct mathematical observables:

1. Endpoint/snapshot readout \(P(x)\).
2. Full lawful word/history report \(PA_w(x)\).
3. Path-cycle/connection defect \(\langle\omega,c\rangle\) after endpoint cancellation.
4. Arithmetic or analytic quantitative constraints on a source-identified nonzero path construction (integer valuations, norms, covolume, rank and signed estimates).

Only a declared interpretation/naturality theorem permits transport between them. The category, coefficient ring and source's actual constraints are part of the mathematical statement, not optional metadata.

## 5. From observer volume to proof obstruction

The potential foundational advance is a **typed obstruction certificate**: suppose a hypothetical source state \(x\) induces a nonzero integral object \(F_x\), and source-faithful observations force it into a high-codimension null class while an independent source bound constrains its norm. If the null class has a proven minimal nonzero cost exceeding that bound, then no such \(x\) exists.

Theorem T4 gives an exact model. Let \(F_x\in\mathbb Z[z]\setminus\{0\}\), with a source-zero root, \(d\) distinct radix roots \(b^{-1},\ldots,b^{-d}\), and all Hasse coefficients divisible by \(p^m\). Then

\[
\|F_x\|_1\ge p^m b^{d(d+1)/2}.
\]

If the actual source separately enforces \(\|F_x\|_1<M<p^m b^{d(d+1)/2}\), this source state is excluded. The substantive step in applications is **constructing \(F_x\)** from the *hypothetical* forbidden condition, including its nonvanishing and the source-confirmed lower/upper constraints.

This is a mathematics-of-mathematics mechanism: observation/report zeros, their lawfully retained construction paths, and arithmetic capacity combine into a *logical exclusion*.

## 6. Why this relates to the RH multiplicity proof

In the released Alpöge–Claude proof, repeated CM theta-period constructions create arithmetic multiplicity and a global contradiction via p-adic and Archimedean constraints. For a native Principia reconstruction, the corresponding knowledge objects are the source spaces, each theta/period lift as a legal map, the new independent image directions, the same nonzero integral minors, their local valuation restrictions, and their real-side norm/covolume bounds.

**The analogy becomes a valid mathematical reconstruction only when every one of those maps and bounds is defined and proved in a common source model**. The old source-prime zeta zero-multiplicity tower (#72), Witt carry (#240), theta/Laguerre (#553) and integral polynomial capacity (#689) show relevant source constructions but are not a proved intertwiner to CM theta periods.

Do not compress knowledge rank, valuation, conditioning, source authentication, logical proof and completion into one scalar “knowledge volume.” Treat volume as a relative family of constructible directions together with a typed vector of quantitative access and obstruction diagnostics.

## 7. Executable controls

Native module: observational_succ/principia_knowledge_volume.py.
Focused tests: tests/test_principia_knowledge_volume.py.

Cases include:
- positive 2D hidden-coordinate exposure by a swap;
- positive 3D nilpotent chain with ranks 1,2,3,3;
- duplicate identity/report no-growth control;
- exact rational Gaussian-elimination rank;
- non-square/malformed source rejection;
- forged reported knowledge volume rejected by replay against the actual declared action matrices;
- full rank with arbitrarily small determinant \(1/N\), a negative control for “rank alone gives analytic mass.”

The mathematical source is stipulated as rational linear algebra. This does not prove that a particular source is physically accessible, or that a real CM theta lift has comparable rank and norm behavior.

## 8. Verdict-changing next instrument

Build a joint typed **arithmetic knowledge volume** for actual normalized CM theta-period maps where:
- rank increments are authenticated by nonzero minors;
- the same minors have integral source passports and growing p-adic valuation bounds;
- a separate Archimedean norm/covolume theorem bounds those minors;
- repeated/linearly dependent lifts and nonintegral normalization mutants fail.

Only then can “the missing analytic mass lives in the computational paths” be promoted from a useful conjecture to a proof-bearing mathematical construction.
