# Arithmetic place seam: continuous observers on the same rational carrier

**Date:** 2026-11-26. **Scope:** classical mathematics reconstructed in SUCC's
source-retaining observer language. **Claim IDs:** PS-01–PS-05.

This is a concrete realization of the proposed observer intermediate-value
principle. Its carrier is the fixed field `Q`; its observers are absolute
values. It proves both an explicit continuation theorem and a necessary
common null crossing. The null is a specified logarithmic-magnitude channel.
The carrier, equality relations and source memory are retained.

The external classification input is Ostrowski's theorem. The continuation,
seam, conditioning and germ arguments below are elementary deductions, with
full proofs. No academic novelty, new RH proof or identification of `R` with
`Q_p` is claimed.

## Definitions and classical input

An **absolute value** on `Q` is a map
\(\nu:\mathbb Q\to[0,\infty)\) such that

\[
\nu(0)=0,\qquad \nu(q)>0\ (q\ne0),\qquad
\nu(qr)=\nu(q)\nu(r),\qquad
\nu(q+r)\le\nu(q)+\nu(r).
\]

Let \(\mathcal A(\mathbb Q)\) be the space of all these maps, equipped with
the **pointwise topology**, inherited from \([0,\infty)^{\mathbb Q}\).
Thus a path \(t\mapsto\nu_t\) is continuous precisely when
\(t\mapsto\nu_t(q)\) is continuous for every fixed rational \(q\).
The constant-one function on all of `Q` is excluded by the zero axiom.

This topology is on the magnitude functions, **after forgetting any discrete
current-place tag**. The executable record retains a current place label,
which jumps at the seam; we do not assert continuity of that decorated record
when such labels carry the discrete topology. Retained source and endpoint
labels are bookkeeping, not additional continuity hypotheses.

The trivial absolute value is

\[
\nu_*(0)=0,\qquad \nu_*(q)=1\quad(q\ne0).
\]

For a genuine rational prime \(p\), let \(v_p(q)\) be the integer exponent
of \(p\) in a nonzero rational, including its denominator, and put
\(|q|_p=p^{-v_p(q)}\). Let \(|q|_\infty\) be the ordinary real absolute value.

**Ostrowski's classification (imported classical theorem).** The nontrivial
members of \(\mathcal A(\mathbb Q)\) are exactly

\[
\nu_{\infty,a}(q)=|q|_\infty^a\quad(0<a\le1),
\qquad
\nu_{p,a}(q)=|q|_p^a\quad(a>0).
\]

The place label is \(\infty\) or the genuine prime \(p\). Positive powers
within one such branch give the same topology on the carrier. The permitted
range \(a\le1\) at the real place matters: greater powers need not satisfy
the ordinary triangle inequality.

Primary source with the complete elementary classification proof:
[K. Soundararajan, *Ostrowski's theorem*, pp. 1–2](https://math.stanford.edu/~ksound/Math152A10/Ostrowski.pdf).
For topology and equivalent absolute values, see
[Brian Conrad, *Some basics concerning absolute values*, §§1–3](https://virtualmath1.stanford.edu/~conrad/248APage/handouts/ostrowski.pdf).

## PS-01. Continuation and a compulsory simultaneous null seam

**Status:** DISCLOSED, classical consequence of Ostrowski's theorem.

**Theorem.** Any two members of \(\mathcal A(\mathbb Q)\) can be joined by
a continuous path. For two **nontrivial** endpoints, a path avoiding \(\nu_*\)
exists if and only if the endpoints have the same place label. Every path
between different nontrivial places has an interior time \(t_*\) for which

\[
\nu_{t_*}=\nu_*,\qquad
\log\nu_{t_*}(q)=0\quad\text{for every }q\in\mathbb Q^\times.
\]

This is simultaneous nullity at one observer, not a separate root selected
for each rational input.

### Proof: existence

Let the nontrivial endpoints be \(\nu_{v,a}\) and \(\nu_{w,b}\). Define

\[
\nu_t=
\begin{cases}
\nu_{v,a(1-2t)},&0\le t<1/2,\\
\nu_*,&t=1/2,\\
\nu_{w,b(2t-1)},&1/2<t\le1.
\end{cases}
\]

At every noncentral time the exponent is positive and in its permitted
range. Each member is an absolute value. For each fixed \(q\ne0\), its
logarithm is linear on each half and tends to zero at the midpoint; the
magnitude therefore tends to one. The zero input remains zero throughout.
This proves continuity in the declared topology and gives the specified
endpoints. If one endpoint is trivial, use just one half of this construction;
if both are trivial, use the constant path.

If \(v=w\), the alternative path
\(\nu_{v,(1-t)a+tb}\) has a positive exponent throughout, in the allowed
range. It avoids \(\nu_*\).

### Proof: necessity

Ostrowski's classification identifies the branches as open subsets:

\[
U_\infty=\{\nu:\nu(2)>1\},\qquad
U_p=\{\nu:\nu(p)<1\}.
\]

Indeed, a nontrivial real power has \(\nu(2)>1\), whereas every finite-place
or trivial absolute value has \(\nu(2)\le1\). Also \(\nu(p)<1\) holds
exactly on the \(p\) branch: every other finite prime has \(|p|_\ell=1\),
and the real branch has \(|p|_\infty^a>1\). Openness follows from pointwise
continuity of evaluations.

Let \(\gamma:[0,1]\to\mathcal A(\mathbb Q)\) join different branches,
starting in \(U_v\). The first time outside \(U_v\),

\[
t_* = \min\{t\in[0,1]:\gamma(t)\notin U_v\},
\]

exists since the indicated set is nonempty and closed. It is positive because
\(\gamma(0)\in U_v\); it is less than one because the other endpoint also
has a neighborhood in its own, disjoint open branch.

For \(t<t_*\), write \(\gamma(t)=\nu_{v,a(t)}\). The exponent is
reconstructed from one evaluation:

\[
a(t)=\frac{\log\gamma(t)(2)}{\log2}\quad(v=\infty),
\qquad
a(t)=-\frac{\log\gamma(t)(p)}{\log p}\quad(v=p).
\]

At the first exit the relevant magnitude must equal one: continuity and its
strict inequality before exit give one inequality, and exclusion from the
open branch gives the reverse. Hence \(a(t)\to0\) as \(t\uparrow t_*\).
For every fixed \(q\ne0\),

\[
\gamma(t)(q)=|q|_v^{a(t)}\longrightarrow1.
\]

Continuity identifies \(\gamma(t_*)(q)=1\) for every nonzero \(q\), and its
zero value is zero by definition. Thus \(\gamma(t_*)=\nu_*\). The
same-place construction and this obstruction give the stated if and only if.
\(\square\)

**Boundary.** The path is in the **space of observers**, not a path from one
point of `R` to another point of `Q_p`. We have neither asserted nor constructed
a topological-field isomorphism \(\mathbb R\simeq\mathbb Q_p\). In particular,
this construction does not define a canonical \(|\pi|_p\). Its source domain
is rational arithmetic; any extension to other carriers needs its own field,
valuation and source-embedding hypotheses.

## PS-02. Transported agreement, finite granularity and conditioning

**Status:** DISCLOSED, elementary statements with explicit retained data.

### The source graph gives exact transport

For each \(\nu\), define the graph observer

\[
O_\nu(q)=(q,\nu(q)),\qquad
G_\nu=\{(q,\nu(q)):q\in\mathbb Q\}.
\]

Define a transport between graph reports by

\[
T_{\nu\to\mu}(q,\nu(q))=(q,\mu(q)).
\]

For all \(\nu,\mu,\lambda\) these satisfy

\[
T_{\nu\to\nu}=\mathrm{id},\qquad
T_{\mu\to\lambda}\circ T_{\nu\to\mu}=T_{\nu\to\lambda},\qquad
T_{\nu\to\mu}\circ O_\nu=O_\mu.
\]

**Proof.** Substitute an arbitrary \((q,\nu(q))\) into each side; both sides
retain exactly \(q\) and return the same declared target evaluation.
\(\square\)

Agreement is agreement on the retained carrier and its arithmetic under these
maps. It does not mean that differently typed magnitude readouts are equal.
The graph transport is elementary bookkeeping; PS-01 supplies the nontrivial
topological obstruction within the allowed magnitude laws.

Retaining the source is load-bearing. At the 3-adic place, sources 2 and 5
both have magnitude one, while their real magnitudes differ. Thus no function
of the 3-adic magnitude alone recovers the real magnitude on all of `Q`.

### Finite-probe modulus

Consider the canonical unit-exponent \(\infty\)-to-\(p\) path of PS-01.
For a nonempty finite \(F\subset\mathbb Q^\times\), set

\[
M_F=\max_{q\in F}\max\{|\log|q|_\infty|,|\log|q|_p|\}.
\]

Then for all \(s,t\in[0,1]\),

\[
\max_{q\in F}|\log\nu_t(q)-\log\nu_s(q)|
\le2M_F|t-s|.
\]

**Proof.** On each half-interval each log readout is linear with slope of
absolute value at most \(2M_F\). For endpoints on opposite halves, split at
\(1/2\) and add the two bounds. \(\square\)

The finite probe set is essential. For any nontrivial branch, choose \(q\)
with nonzero logarithmic magnitude and then the sources \(q^n\). Their log
responses grow linearly in \(n\). Consequently the distance from that branch
observer to the null log display is unbounded when measured by the supremum
over all rational sources. Pointwise continuity is not uniform continuity
over an unrestricted query bank.

### The inverse loses conditioning at the seam

On a fixed branch with exponent \(a>0\), a finite log-response vector \(r\)
is reported as \(a r\). If an inverse is defined on two distinct possible
vectors, its Lipschitz constant is at least \(1/a\): the input distance is
\(a\|r_1-r_2\|\) while the required output distance is
\(\|r_1-r_2\|\). At \(a=0\), both observations are equal, so that display
alone has no inverse on the pair. This is a proved stability obstruction,
not a claim that the retained source graph loses its first coordinate.

### Precisely which information is null?

At \(\nu_*\), the magnitude of every nonzero input is one and every finite
log-magnitude query gives zero. However,

\[
\nu_*(q-a)=0\iff q=a.
\]

An equality-query toolkit can still distinguish source points. The seam is
therefore **magnitude-null relative to the declared readout**, not universally
information-null. Full source/causal memory and its additional legal probes
must be stated before any stronger information claim.

## PS-03. An oriented germ reconstructs what the seam display hides

**Status:** DISCLOSED, exact derivatives of the constructed path.

For each \(q\in\mathbb Q^\times\) in the canonical unit-exponent path,
write \(f_q(t)=\log\nu_t(q)\). Then

\[
f_q(1/2)=0,\qquad
\partial_- f_q(1/2)=-2\log|q|_\infty,\qquad
\partial_+ f_q(1/2)=2\log|q|_p.
\]

**Proof.** The formulas on the two halves are respectively
\((1-2t)\log|q|_\infty\) and \((2t-1)\log|q|_p\). Subtract the seam
value and divide by \(t-1/2\). \(\square\)

Thus the **full indexed family** of oriented pairs, as \(q\) ranges over
\(\mathbb Q^\times\), recovers both endpoint magnitude functions, although
the displayed seam values alone do not. A germ at just one rational need not
identify a place: every prime not dividing that rational has zero local
logarithmic response. The orientation and place labels are declared; there is
no phase or derivative convention inferred from the mere word “agreement.”

This particular path already places all its extra data in the first germ.
Repeated higher derivatives are not independently new constraints: on either
open half its log readouts are linear. “More derivative labels” do not by
themselves give more arithmetic rank or multiplicity.

## PS-04. Smooth all-jet nulls and the obstruction to analytic switching

**Status:** DISCLOSED countermodel and theorem. This separates smooth
observer-time jets from analytic or integral formal-group jets.

### A genuine same-carrier smooth countermodel

Define

\[
h(t)=
\begin{cases}
\exp\bigl(4-(t-1/2)^{-2}\bigr),&t\ne1/2,\\
0,&t=1/2.
\end{cases}
\]

It lies in \([0,1]\) on \([0,1]\), equals one at both endpoints, and is
smooth with every derivative zero at \(1/2\). For distinct endpoint places
\(v,w\), with permitted positive exponents \(a,b\), set

\[
\widetilde\nu_t=
\begin{cases}
\nu_{v,a h(t)},&t<1/2,\\
\nu_*,&t=1/2,\\
\nu_{w,b h(t)},&t>1/2.
\end{cases}
\]

This is a path of genuine absolute values with the desired distinct endpoints.
For every fixed \(q\ne0\), all derivatives of
\(\log\widetilde\nu_t(q)\), including the value, vanish at the seam.
Equivalently every derivative of \(\widetilde\nu_t(q)-1\) vanishes there.

**Proof.** On each side the log readout is a constant multiple of \(h(t)\).
Each derivative of \(e^{-u^{-2}}\), away from \(u=0\), is that exponential
times a polynomial in \(u^{-1}\); it tends to zero as \(u\to0\). The
one-sided derivatives therefore join smoothly with value zero at every order.
Exponentiation yields the corresponding assertion for magnitude minus one.
The powers are permitted because \(0<h\le1\) away from the seam.
\(\square\)

This refutes the unrestricted assertion that an infinite tower of smooth
observer-time null jets forces identical global observer behavior. It does
not refute an identity theorem in an analytic or quasianalytic class, nor an
integral divisibility theorem for source-defined formal coefficients.

### Real-analytic place switching is impossible

**Theorem.** A continuous path between distinct nontrivial places cannot have
\(t\mapsto\log\nu_t(q)\) real analytic on \((0,1)\) for every fixed
\(q\in\mathbb Q^\times\).

**Proof.** Every endpoint branch is open by PS-01, so it occupies a nonempty
open time interval adjacent to that endpoint. For two different finite places
\(p,\ell\), use the source \(q=p\). Its log magnitude is nonzero throughout
the \(p\) branch and identically zero throughout the \(\ell\) branch.
For the real place and \(p\), choose any prime \(\ell\ne p\); its log
magnitude is nonzero in the real branch and zero in the \(p\) branch.
In either case an analytic scalar function on the connected interval
\((0,1)\) would vanish on a nonempty open subinterval while being nonzero
on another, contrary to the real-analytic identity theorem. \(\square\)

The usual identity theorem follows from local convergent Taylor expansions:
a nonzero analytic germ has an isolated zero, so an accumulation of zeros
forces the germ to vanish; the zero germ then propagates through a connected
interval. The flat smooth function above escapes precisely this hypothesis.

## PS-05. Product formula and the paid arithmetic capacity gate

**Status:** DISCLOSED, elementary rational arithmetic and determinant bounds.
These are separate quantitative statements; they do not follow merely from
the existence of the PS-01 null observer.

### The normalized product formula on the same source

For \(q\in\mathbb Q^\times\), unique factorization gives

\[
|q|_\infty=\prod_p p^{v_p(q)},\qquad |q|_p=p^{-v_p(q)},
\]

with finite support. Multiplying, or taking real logarithms, proves

\[
\boxed{|q|_\infty\prod_p|q|_p=1},\qquad
\boxed{\log|q|_\infty+\sum_p\log|q|_p=0}.
\]

Every term concerns the same rational and the displayed canonical
normalizations. With a different source in one channel or an unaccounted power
of one norm the identity need not hold; accidental cancellation can still
occur, so a zero sum alone does not authenticate source or normalization.
Restoring a powered observation
requires division by its exponent; PS-02 explains why that inverse is
singular at the trivial seam. Zero readout there is not itself the product
formula's arithmetic content.

### Denominator-aware capacity

Let \(x\in\mathbb Q^\times\), let \(D\) be a positive integer with
\(N=Dx\in\mathbb Z\), and let \(P\) be a finite set of distinct genuine
primes. Suppose nonnegative integers \(e_p\) satisfy \(p^{e_p}\mid N\).
Then, with \(M=\prod_{p\in P}p^{e_p}\),

\[
\boxed{|x|\ge M/D.}
\]

**Proof.** Coprimality of the distinct prime powers gives \(M\mid N\).
Since \(N\ne0\), write \(N=Mz\) with nonzero integer \(z\), whence
\(|N|\ge M\). Divide by \(D>0\). \(\square\)

If an independently proved analytic bound on this **same** \(x\) says
\(|x|\le U\), compatibility requires \(M\le DU\). A strict reverse
inequality rules out the nonzero witness. If a source construction separately
certified nonvanishing, its hypothetical inputs are inconsistent.

Duplicate copies of the certificate \(p^e\mid N\) do not yield
\(p^{2e}\mid N\). Independent constraints or actual increasing valuation
must supply any greater multiplicity. The exact implementation rejects
duplicate prime labels instead of silently multiplying them.

### Determinant version with coordinate transport paid

Let \(A\in M_r(\mathbb Q)\), \(r\ge1\), and let \(d\) be a positive
integer for which \(dA\) is integral. Suppose \(M\mid\det(dA)\), where
\(M\) is a positive integer assembled from certified distinct prime powers.
Let \(L,R\in\mathrm{GL}_r(\mathbb R)\), and set \(B=LAR\).
If \(\det A\ne0\), then

\[
\boxed{
M|\det L\det R|
\le d^r\prod_{i=1}^r\|\operatorname{row}_i(B)\|_2.
}
\]

**Proof.** The nonzero integral determinant obeys
\(M\le|\det(dA)|=d^r|\det A|\). Also
\(\det B=(\det L)(\det A)(\det R)\), and Hadamard gives
\(|\det B|\le\prod_i\|\operatorname{row}_i(B)\|_2\).
Multiply the first bound by \(|\det L\det R|\) and substitute the second.
\(\square\)

Consequently a strict violation forces \(A\) singular. The inequality cannot
be strengthened by making a chosen analytic weighting tiny while dropping
its determinant factor. Every normalizing map must be paid on both sides.

### Existing SUCC same-source calibration

At pinned Principia Genesis commit
`c5757d48a6788e1513e4276b111f7cdad075055f`,
[CM_THETA_TWO_PLACE.md](https://github.com/femboy2112/SUCC/blob/c5757d48a6788e1513e4276b111f7cdad075055f/research/2026-11-24/principia_math_of_math/CM_THETA_TWO_PLACE.md)
constructs Gaussian-shell entries
\(A_{rj}=4p^{4r}((-4)^j)^r\) for inert \(p\). For its analytic weighting
\(B=A\operatorname{diag}(q^{p^22^j})\), the exact determinant transport is

\[
\det B=q^{\sum_jp^22^j}\det A.
\]

That factor is precisely part of the paid coordinate comparison above. The
finite shell matrix is not identified with the automorphic theta-period map
in the external RH proof.

## Executable scope and hostile controls

The new module `observational_succ/principia_place_seam.py` stores
\(\log\nu(q)\) as a finite tuple of rational coefficients of \(\log p\).
For \(q=\pm\prod p^{e_p}\), real-place exponent \(a\) gives coefficients
\(ae_p\); prime-place exponent \(b\) gives the single coefficient
\(-be_p\) at that prime. Rational path parameters therefore need no floating
logarithms or irrational exponentiation. Source, place, exponent and endpoint
labels are retained separately. The product formula is an exact cancellation
of these prime-log vectors.

Run from the repository root:

```sh
python -m unittest discover -s tests -p 'test_principia_place_seam.py' -v
```

The worker observed **15/15 focused tests passing**, including 80 fresh
multiplicativity cases and 24 product-formula cases. Controls reject changed
source, unpaid norm powers, composite place labels, floats, forged reports,
false divisibility, duplicate valuation certificates and an uncleared
denominator. Equality tests survive a null magnitude display. A positive
same-place path avoids the seam, confirming that different-place hypotheses
matter.

These are finite implementation checks. PS-01–PS-05 rest on the proofs above;
the tests do not lift finite sampling into universal topological or arithmetic
claims. No full repository gate or external RH proof rebuild is asserted by
this focused receipt; the round's aggregate validation records those separately.
