# Exact local-clock agreement permits compensating phase correlation

Date: 2026-10-24. Paper-only corollary of PCC-15 in
`research/2026-10-24/PI_PASCAL_PRESCRIBED_CONSTANT.md`, parent
`6e8fa8b77886b13f1f533ed8083fd88c849d14b3`.

**Status:** elementary proved corollary of the prescribed-constant
construction. The constructed source changes the authentic BBP forcing.
No code, numerical test, or normality theorem is asserted.

## 1. The exact local phase projection

Put \(G=\mathbb Q/\mathbb Z\). For a prime \(p\), let

\[
G_p=G[p^\infty]
=\{z\in G:p^kz=0\text{ for some }k\ge0\}.
\]

Every rational phase has finite order, so the elementary primary
decomposition of a finite cyclic group gives

\[
G=\bigoplus_{q\ {
m prime}}G_q.
\]

Write \(\pi_p:G\to G_p\) for the associated additive projection. This is
a phase projection in the torsion group, not a real-continuous projection
from the full circle to a finite-prime coordinate.

Explicitly, for \(x=a/b\) in lowest terms, \(b>0\), write
\(b=p^kc\) with \(p\nmid c\). If \(k=0\), then \(\pi_p([x])=0\).
If \(k>0\), choose \(j\) modulo \(p^k\) with

\[
j\equiv ac^{-1}\pmod {p^k}.
\]

Then \(\pi_p([x])=[j/p^k]\): the difference
\((a-jc)/(p^kc)\) has denominator dividing \(c\), so has order prime to
\(p\). Since \(p\nmid a\), the displayed \(p\)-primary component has
exact order \(p^k\).

Consequently, with
\(\mathbb Z_{(p)}=\{a/b\in\mathbb Q:p\nmid b\}\),

\[
\boxed{
\pi_p([x])=\pi_p([z])
\quad\Longleftrightarrow\quad
x-z\in\mathbb Z_{(p)}
\quad\Longleftrightarrow\quad v_p(x-z)\ge0.}
\]

The zero difference has valuation \(+\infty\). Equivalently,
\(\ker\pi_p=\mathbb Z_{(p)}/\mathbb Z\). This proves the assertion
without confusing congruence of rational phases with equality of real lifts.

## 2. Applying PCC-15 at every integer time

Fix a finite prime set \(S\) containing 2 and a precision \(L\ge1\).
Let \(U_n\) be the authentic unwrapped BBP source, with \(U_0=0\) and
\(U_n=16U_{n-1}+r(n)\). Apply PCC-15 with its authenticated reference
Newton coefficients. The resulting rational states \(H_n\), also with
\(H_0=0\), and changed rational forcing \(s(n)=H_n-16H_{n-1}\) obey

\[
H_n-U_n\in p^L\mathbb Z_{(p)}\quad(n\ge0),\qquad
s(n)-r(n)\in p^L\mathbb Z_{(p)}\quad(n\ge1)
\]

for every \(p\in S\). Since \(p^L\mathbb Z_{(p)}\subset\mathbb Z_{(p)}\),
the boxed equivalence proves

\[
\boxed{
\pi_p([H_n])=\pi_p([U_n])\quad(n\ge0),\qquad
\pi_p([s(n)])=\pi_p([r(n)])\quad(n\ge1),\qquad p\in S.}
\]

Thus every selected local primary source clock, including its complete
time history, agrees **exactly**. Every joint or cross-time observable
determined solely by these selected primary coordinates also agrees.
There is no finite-time cutoff here. The additional positive \(p\)-adic
precision remains the fixed \(L\); agreement at arbitrarily high positive
\(p\)-adic precision is not asserted.

In the observer notation, define the residual phase

\[
w_n=[H_n-U_n].
\]

Then

\[
\pi_p(w_n)=0\quad(p\in S),\qquad
w_n\in\bigoplus_{q\notin S}G_q,
\]

while the full real phase satisfies \([H_n]=[U_n]+w_n\). Each individual
\(w_n\) has finite prime support, but the unobserved support is allowed to
grow with time. The source difference also satisfies the exact recurrence

\[
H_n-U_n=16(H_{n-1}-U_{n-1})+[s(n)-r(n)].
\]

The residual is therefore an all-time coherent changed-source trajectory,
not an arbitrary collection of independently assigned phases.

## 3. These same finite clocks coexist with a nonnormal real law

Choose the fixed constant

\[
C=\sum_{j\ge2}16^{-j!}.
\]

PCC-1 through PCC-3 construct the above rational states with

\[
H_n=16^nC-\eta_n,\qquad 0<\eta_n=O(n^{-2}),
\]

while retaining the positive analytic moment density, full dyadic difference
profile, and the declared finite-prime congruences. The sparse factorial
digits give empirical circle law \(\delta_0\) for \(\{16^nC\}\); the
vanishing tail transfers that law to \([H_n]\). The prescribed-constant
paper also proves central retention tending to one on the stated expanding
windows and radii much larger than \(n^{-2}\).

Hence exact agreement with **every chosen finite collection of authentic
primary clocks at every time**, even together with the additional retained
properties, does not force Haar occupation or a central-branch saving for
the full real source. It places the unresolved information in the jointly
evolving complementary coordinates. It does not prove that the actual pi
orbit has a different occupation law from this control; that arithmetic
question remains open.

There is an exact signed-correlation consequence inside this control. Put
\(u_n=\sum_{p\in S}\pi_p([U_n])\) and
\(v_n=[H_n]-u_n\); then \(v_n\) has no primary coordinate in \(S\).
For every fixed integer \(h\), with \(e(t)=\exp(2\pi it)\),

\[
\frac1N\sum_{n<N}e(hu_n)e(hv_n)
=\frac1N\sum_{n<N}e(hH_n)\longrightarrow1,
\]

and hence

\[
\frac1N\sum_{n<N}|e(hv_n)-e(-hu_n)|^2\longrightarrow0.
\]

Thus disjoint primary supports and complete local-clock agreement permit
asymptotically perfect compensating phase correlation. They do not supply
a decorrelation bound. This assertion concerns the constructed source and
does not assign that correlation to the authentic BBP complement.

## 4. Whole-prime and integer-lift boundaries

If two rational phases agree under \(\pi_p\) for **every prime** at a fixed
time, their difference has every primary component zero, hence is zero in
\(\mathbb Q/\mathbb Z\). Their rational real lifts can still differ by an
integer. Equality of all phase projections therefore determines the full
circle phase, not its chosen integer lift or literal carry.

The stronger PCC-15 requirement at every prime, with positive absolute
precision, would force the rational lift difference itself to vanish:
any nonzero rational has valuation zero at some prime and cannot belong
to \(p^L\mathbb Z_{(p)}\) for every prime when \(L\ge1\).

Neither all-prime statement follows from the finite-set construction.
The quantifier is

\[
\text{for every fixed finite }S,\ \text{there exists a corresponding
changed source},
\]

not existence of one changed source satisfying the same positive-precision
constraints simultaneously for all primes. No compatible limit over those
different sources is supplied.

Finally, exact original forcing together with initial zero already fixes
\(U_n\) uniquely. This construction changes \(r(n)\) to \(s(n)\); it does
not preserve the fixed BBP four-pole rational function, its global height
restrictions, or all of its defining data.

## 5. Next falsifier and useful theorem

A proposed inference from local observer agreement to real carry saving
must distinguish this control using an explicitly retained hypothesis.
The next useful test is whether the argument uses the **fixed four-pole
forcing and its global denominator/height restrictions** to control the
unobserved coordinates or their real signed correlations. If it only reads
a fixed finite set of primary clocks, even over their complete histories,
this construction passes those observations and defeats the claimed
inference.

An argument that genuinely uses an expanding or entire prime family needs
a uniform real transport/error theorem and its own limit proof. Replacing
the finite-set quantifier by an all-prime assertion is not such a theorem.
The selected-source correlation or frequency estimate remains necessary.

See the [source path synthesis](PI_PATH_SELECTION_SYNTHESIS.md),
[claim supplement](../../docs/CLAIM_SUPPLEMENT_SOURCE_PATH_SELECTION.md)
and [prescribed-constant parent proof](PI_PASCAL_PRESCRIBED_CONSTANT.md).
