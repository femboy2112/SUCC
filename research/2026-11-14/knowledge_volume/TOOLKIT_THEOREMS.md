# When a new operation closes an infinite prediction hierarchy

**Status:** elementary paper proofs with exact rational implementations.
The source is supplied mathematically. No empirical law is inferred from a
few agreeing values. Symbols K=Q or R below denote infinite fields; the
statements about polynomial functions do not silently transfer to finite fields.

## KV-T1 — The explored front in a declared function class

Let V be a supplied finite-dimensional K-vector space of functions on a
query domain Q. An unknown source is f∈V. Observations at a finite set
S⊂Q determine f(q), uniformly over f∈V, exactly when

\[
\operatorname{ev}_q\in\operatorname{span}_K\{\operatorname{ev}_s:s\in S\}
\quad\text{inside }V^*.
\]

**Proof (CLASSICAL / PROVED LOCAL).** A dependence
ev_q=Σc_s ev_s gives the executable certificate f(q)=Σc_s f(s).
If ev_q is outside the span, elementary finite-dimensional duality supplies
g∈V with g|_S=0 and g(q)≠0. The sources f,f+g agree on all observations
and disagree at q. ∎

Thus cl(S)={q:ev_q∈span(ev_S)} is the precise set of points already
determined by the explored front. This closure is extensive, monotone and
idempotent; it satisfies exchange. Indeed, if
ev_q=v+c ev_p with v∈span(ev_S) and ev_q∉span(ev_S), then c≠0,
so solve for ev_p. Each new independent query raises rank by one. This
is vector-matroid/linear-interpolation structure, not a new general theory
of geometry.

For polynomials of degree at most d, d+1 distinct samples determine every
point by the nonzero Vandermonde determinant. Without the authenticated
degree bound, f and f+c∏_(s∈S)(z−s) agree on S and disagree at every
new q when c≠0. Even an assumption of entire analyticity does not rescue
finite samples: for derivative observations of orders 0,…,r_i−1 at a_i,
the polynomial c∏(z−a_i)^(r_i) is invisible to every such observation.
At a new point it is nonzero. Example: 0 and z²(z−1)² share values and
first derivatives at 0 and 1, but give 0 and 4 at 2.

The algebra of a source class determines the reach of the map. Finite
samples alone do not authenticate that class. These controls are against
an explicitly broader class, not against a completely specified source.

## KV-T2 — Two reports suffice, but polynomial closure never stabilizes

Fix the source and primitive report

\[
T(x,y)=(xy,y),\qquad h(x,y)=x,\qquad (x,y)\in K^2.
\]

Its time-n report is h_n(x,y)=xy^n. Let T*f=f∘T and let the allowed
polynomial hierarchy be

\[
A_0=K[h],\qquad A_{m+1}=K[A_m,T^*A_m].
\]

**Theorem (PROVED LOCAL).** For every m≥0,

\[
A_m=K[x,xy,\ldots,xy^m]\subsetneq A_{m+1}.
\]

**Proof.** Pullback sends xy^j to xy^(j+1), which gives the displayed
algebra by induction. Every product of r listed generators has x-degree r
and y-degree at most rm. Conversely every integer y-degree from 0 to rm
is obtained by a sum of r integers between 0 and m. Thus the monomial
x^r y^s belongs exactly when 0≤s≤rm. A polynomial combination cannot
create a missing monomial because distinct monomials are linearly independent.
In particular xy^(m+1) is absent when r=1. Over an infinite field,
polynomial equality agrees with functional equality on K². ∎

The union A_∞ is not finitely generated: finitely many candidate generators
all lie in some A_M, which still misses xy^(M+1). This does not contradict
Noetherianity of K[x,y], which concerns ideals, not arbitrary ascending
chains of subalgebras. Two coordinates of source state do not force a
finite polynomial prediction algebra.

Now retain the first two reports:

\[
E(x,y)=(a,b)=(x,xy),\qquad
\mathcal M=E(K^2)=\{(a,b):a\ne0\}\cup\{(0,0)\}.
\]

**Theorem (PROVED LOCAL).** On this exact image,

\[
G_n(a,b)=
\begin{cases}
a(b/a)^n,&a\ne0,\\
0,&(a,b)=(0,0)
\end{cases}
\quad\text{satisfies}\quad h_n=G_n\circ E
\]

for every n≥0. If a≠0, b/a recovers y. If a=0, the source forces every
report to be zero regardless of hidden y. This proves the formula and the
singular branch directly. The pair (0,b≠0) is outside the source image,
not a special input to be guessed. ∎

One report already determines the complete future on the x=0 fiber. On
any fiber x≠0, states (x,1),(x,2) share the present report and differ next.
Two reports determine the complete output future globally. Hidden y remains
unidentified on the zero fiber, but that ambiguity does not affect the target.

**What changes at the higher step:** polynomial expressions in any fixed
finite list of reports cannot express the entire future. Permitting a
justified division operation and a valid zero branch supplies an exact
finite description. This is an increase in deductive/representational reach
relative to a specified toolkit. No new source measurement is created.

If the starting SUCC programming language is already universal, division on
encoded rational numbers can itself be programmed from its primitives.
This example therefore proves no increase in the class of Turing-computable
functions. The strict hierarchy is the declared **polynomial report algebra**;
the practical gain can be a newly justified subroutine, a shorter expression,
or a better resource bound. A stronger logical/computability hierarchy would
need its own explicit restrictions or oracle contract.

### A reusable law, rather than separately guessed future values

The descriptor evolves by

\[
\overline T(a,b)=
\begin{cases}(b,b^2/a),&a\ne0,\\(0,0),&(a,b)=(0,0).
\end{cases}
\qquad E\circ T=\overline T\circ E.
\]

It maps M to M, including a regular point with b=0 entering the singular
origin. Induction gives E T^n=\overline T^n E for every n. This is the
concrete bridge from a representation of observed points to a representation
of their lawful transformations.

**Clock convention:** G_n is the report at time n from the original time
zero. After the second report has arrived at time 1, a request for n more
steps uses G_(n+1). The algorithm cannot receive a report before it occurs.

## KV-T3 — The algebraic shadow can admit a false future

The first three reports obey ac=b². The tuple (0,0,1) satisfies that
polynomial relation but cannot be (x,xy,xy²): its first coordinate forces
x=0 and hence its third coordinate to be zero.

The exact image is

\[
\{(a,b,c):a\ne0,\ ac=b^2\}\cup\{(0,0,0)\}.
\]

Replacing the source image by the polynomial relation alone introduces
false completions at the singular fiber. This is a precise source-adequacy
failure, not a failure of the actual source law. The executable module
separates `satisfies_report_relation` from `in_three_report_image` so the
wrong substitution can fail visibly. It is an elementary analogue of the
repository's source-preservation discipline; no BBP source is altered.

## KV-T4 — Exact prediction need not tolerate finite precision

Over R, for each fixed n≥2 set x=ε^n,y=1/ε, ε>0. Then

\[
E(x,y)=(\varepsilon^n,\varepsilon^{n-1})\longrightarrow(0,0),
\qquad G_n(E(x,y))=1,
\]

while G_n(0,0)=0. Thus G_n is discontinuous at the origin on the
unrestricted report image. Exact information can determine the answer
while finite-precision information supplies no corresponding uniform guarantee.

The same counterexample identifies the missing hypothesis: y becomes
unbounded. Suppose instead the source guarantees |y|≤M for known M≥0.
Its exact report image is C_M={(a,b):|b|≤M|a|}. For two points of C_M,

\[
\boxed{|G_n(a,b)-G_n(a',b')|
\le(n-1)M^n|a-a'|+nM^{n-1}|b-b'|\quad(n\ge2).}
\]

At n=0 use |a−a'|, and at n=1 use |b−b'|.

**Proof.** On a regular branch, put y=b/a. The partial derivatives are
∂_aG_n=(1−n)y^n and ∂_bG_n=ny^(n−1). A line segment within either
same-sign cone stays within that convex cone; integrate the derivative
bounds. Its endpoint at the origin follows by continuity along that cone,
or directly from |G_n|≤M^n|a|. For opposite signs of a,a',

\[
|G_n-G_n'|\le M^n(|a|+|a'|)=M^n|a-a'|,
\]

which is bounded by the displayed right side because n−1≥1. The
singular origin and M=0 are included. ∎

The coefficients grow with the requested horizon and source bound. This
formula is a conditional error certificate; neither knowing a source hash
nor observing a few small multipliers proves an external bound |y|≤M.

## KV-T5 — Knowing each future point and controlling the entire future differ

If 0≤M<1, the entire sequence map G:C_M→ℓ∞ is Lipschitz. A conservative
explicit bound is

\[
\|G(a,b)-G(a',b')\|_\infty
\le \max\!\left(1,\frac{M^2}{(1-M)^2}\right)|a-a'|
+\frac{1}{(1-M)^2}|b-b'|.
\]

To prove it, bound each nonnegative coefficient in KV-T4 by the corresponding
sum: Σ_(n≥1)(n−1)M^n=M²/(1−M)² and
Σ_(n≥1)nM^(n−1)=1/(1−M)². Include n=0 using the maximum with 1.
Each source sequence is bounded, so the ℓ∞ codomain is valid.

At M=1 this whole-future continuity fails in general. The report pairs
(1,1−ε) approach (1,1) for 0<ε<1, but

\[
\sup_{n\ge0}|1-(1-\varepsilon)^n|=1.
\]

Every fixed future coordinate is still continuous on C_1. Convergence at
each finite horizon cannot be exchanged for uniform convergence of the
whole future. For M>1, sequences need not even belong to ℓ∞ and fixed-
horizon error coefficients can grow exponentially. These statements give
an exact boundary for the proposed passage from many finite points to one
completed object of understanding.

## KV-T6 — A genuine shortcut with an explicit cost model

Given consistent a,b and n in binary, the regular-branch formula uses one
division and binary exponentiation. The implemented algorithm, for n≥1,
performs

\[
\lfloor\log_2n\rfloor+\operatorname{popcount}(n)+1
\le2\lfloor\log_2n\rfloor+2
\]

multiplications, counting squarings and the final a factor. It returns the
origin or horizon-zero value directly when those branches apply. Direct
source walking takes n transitions. This is a real logarithmic-versus-linear
comparison **in unit-cost exact field operations**, after the source law
and input reports are supplied.

It is not constant bit complexity. With x=1,y=2, the answer is 2^n and
its expanded binary output has n+1 bits. The compressed expression is short;
printing the expanded answer still pays for its length. The receipt records
field-operation counts separately from the mathematical value.

## Representation comparison and prior art

For T(x)=x² on R, a single coordinate generates an invariant polynomial
algebra R[x]; yet x,x²,x⁴,x⁸,… are linearly independent. Thus even finite
polynomial closure differs from finite linear observable closure. The
two-coordinate construction above adds a second strict separation:
finite exact report determination can hold without finite polynomial closure.

The existing SUCC RFO-07 theorem concerns a **finite set of source states**,
not merely a finite number of coordinates. It is not contradicted. The
classical invariant-linear-span framework appears in Brunton et al.,
[PLoS ONE 2016](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0150171),
“Koopman invariant subspaces and exact finite-dimensional models,” equations
(8)–(13). We use only the elementary invariant-span implication. The
counterexamples and source-image/stability proofs here are established
directly; no broad global impossibility claim is imported from that paper.

## Next lamp

For a proposed higher construction, name the admitted operations and source
domain, exhibit a target outside the old closure, provide a verified evaluator
in the enlarged toolkit, and test its singular cases and error modulus.
This supplies a falsifiable meaning of one further level. A claimed new
physical dimension or formal logical-hierarchy jump requires a separate
definition and theorem; successful extrapolation alone does not provide it.
