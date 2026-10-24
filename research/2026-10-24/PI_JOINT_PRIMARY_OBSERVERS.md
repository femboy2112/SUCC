# All observers together: exact reconstruction, mixed correlations and the real limit

Date: 2026-10-24. Parent: draft #274 at
`d942c4707d750f788f39acb137a04e871a93e0a6`, inheriting draft #273.
Contract: [BBP-specific Hypothesis A](PI_HYPOTHESIS_A_HOLE_CONTRACT.md).

**Authority:** elementary paper proofs, inherited source theorems and exact
finite calibrations. No new Lean declarations or external refereeing.
**Pi normality, its selected real carry bound and a source-specific replacement
for Hypothesis A remain OPEN.** The constructions below do not change that
status. Scholarly novelty has not been established.

## 1. The faithful form of “use all of them”

The complete family of primary phases determines a rational circle point.
Every proper family can leave large real ambiguity. Thus the proposal to
retain joint observations is mathematically substantive: the missing mixed
observable can contain information absent from all its proper marginals.

There are nevertheless three different tasks:

1. reconstruct the point from a sufficiently complete family;
2. control the real distribution of the reconstructed points over time;
3. justify any exchange of increasing observer depth and increasing time.

The authentic BBP recurrence already performs the first task. The exact
formulas here identify the observable required for the second and quantify
the failure possible in the third. They also show why asking for complete
microscopic independence would be too strong even for a normal real orbit.

Keep the notation distinct:

\[
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad y_n=[U_n],
\]

where \(r(n)\) is the authentic four-pole forcing. Let \(d_n\) be the
**individual reduced denominator** of \(U_n\), and let \(D_N\) be the
**common carrier denominator** of the first \(N\) forcing values. Then
\(d_n\mid D_N\) for \(n\le N\). The function
`bbp_circle_carrier` preserves the integer source and literal carries
separately from this circle carrier.
In fact \(D_N=\mathrm{lcm}(d_1,\ldots,d_N)\): the forward recurrence
proves one divisibility, and \(r(n)=U_n-16U_{n-1}\) proves the reverse.
The common carrier is therefore not enlarged by irrelevant denominator factors.

## 2. Exact joint reconstruction and the sharp residual fiber

### JPO-1: finite primary reconstruction (PROVED PAPER)

For \(G=\mathbb Q/\mathbb Z\), write \(\pi_p\) for projection to its
\(p\)-primary subgroup. If \(x=a/b\), \(b=p^kc\), \(p\nmid c\),

\[
\pi_p([x])=\left[\frac{a c^{-1}\bmod p^k}{p^k}\right],
\]

with value zero when \(k=0\). The inverse is modulo \(p^k\).
The difference from \(x\) has denominator prime to \(p\), proving the
formula. Primary decomposition of a finite cyclic group gives

\[
[x]=\sum_{p\mid b}\pi_p([x]).
\]

This is exact joint reconstruction, not a claim about uniform distribution.
All primary phases are unchanged under an integer shift of the real lift.
Literal carries therefore still require the authenticated integer lift.

Fix a known carrier \(G[D]=\{a/D:0\le a<D\}\) and a set of observed
primes \(S\). Define

\[
Q=\prod_{p\in S}p^{v_p(D)},\qquad R=D/Q.
\]

Suppose the observed phases are compatible with this carrier and put
\(u=\sum_{p\in S}\pi_p(x)\). Then the complete fiber is exactly

\[
\boxed{\quad u+G[R]=\{u+j/R:0\le j<R\}.\quad}
\tag{JPO-1}
\]

Indeed the unobserved primary groups are precisely the prime-power factors
of \(R\), and their direct sum is \(G[R]\). Conversely every point in
that coset has the stipulated observations. No positivity or probabilistic
independence is used.

### JPO-2: sharp real ambiguity (PROVED PAPER)

The smallest worst-case real circular error of any point decoder depending
only on these observations is

\[
\boxed{\quad \inf_z\max_{x\in u+G[R]}\|x-z\|_{\mathbb T}
=\frac{R-1}{2R}.\quad}
\tag{JPO-2}
\]

For \(R=1\) this is zero. For \(R>1\), a closed circular arc containing
all \(R\) equally spaced points has length at least \(1-1/R\): its
complement cannot exceed the largest gap, of length \(1/R\). Removing
one such gap attains that length. A circle ball of radius less than one
half is such an arc of twice the radius, proving the result.

In particular any nontrivial unobserved component leaves worst-case error
at least \(1/4\). A huge observed modulus does not itself make the error
small. For example, observing the complete \(3^{20}\)-component of a
\(3^{20}\cdot101\) carrier leaves optimal error \(50/101\).

This is a worst-case statement about the declared fiber, not a lower bound
on prediction error for the authentic source with additional restrictions.
An independently proved real restriction on that source can shrink the fiber.

Under the **uniform reference law** on \(G[D]\), the conditional character
also has an exact form:

\[
\mathbb E(e(hx)\mid\pi_p(x),p\in S)
=e(hu)\,\mathbf1_{R\mid h}.
\tag{JPO-3}
\]

This follows by summing the \(R\) roots. For \(R\nmid h\), the conditional
mean-square prediction error of that unit-modulus character is one. It
illustrates the collective information gain; it does not substitute a
uniform reference law for the actual time law.

## 3. The full mixed correlation is the relevant observable

### JPO-3: temporal product identity and its missing term (PROVED PAPER)

Let \(S_N\) contain every prime factor of \(D_N\). For each fixed
integer \(h\), the true temporal Fourier mean is exactly

\[
\boxed{\quad
\frac1N\sum_{n=1}^N e(hU_n)
=\frac1N\sum_{n=1}^N\prod_{p\in S_N}e(h\pi_p(U_n)).
\quad}
\tag{JPO-4}
\]

All factors on the right have the **same time index**. Replacing this by
the product of their separate time means discards the mixed correlation.
For unit-modulus random variables \(Z_1,\ldots,Z_k\) under the empirical
time law, define \(m_j=\mathbb EZ_j\) and use the bilinear covariance
\(\mathop{Cov}(A,B)=\mathbb E(AB)-\mathbb EA\mathbb EB\). Recursing on
the last factor gives the exact decomposition

\[
\mathbb E\prod_{j=1}^kZ_j-\prod_{j=1}^km_j
=\sum_{j=2}^k\left(\prod_{i=j+1}^km_i\right)
\mathop{Cov}\left(\prod_{i<j}Z_i,Z_j\right).
\tag{JPO-5}
\]

Thus even pairwise decorrelation leaves higher interactions unbounded.
One must either bound these selected mixed terms, or use a nonnegative
joint statistic such as real coarse-cell collision counts. Complete source
identification supplies the terms, not their cancellation.

The code retains distributions of exact rational phases rather than using
floating complex sums. It separately computes the phase law obtained by
adding observations **at the same times**, and the counterfactual law obtained
by independently convolving their time marginals. The two differ already
for the genuine \(3\)- and \(5\)-primary components of the sample
\(\{0,1/15\}\). A separate four-bit parity control has every proper
three-bit marginal uniform but four-way phase product one. Four binary
copies in that control are not asserted to be disjoint primary subgroups.

### JPO-4: even all proper CRT marginals can miss clustering (PROVED PAPER)

Let \(q_1,\ldots,q_k\), \(k\ge2\), be pairwise coprime integers,
\(D=\prod_iq_i\), and let \(A\) be uniform on \(0,\ldots,L-1\),
where \(1\le L\le D\). The real phase \(A/D\) lies in an arc of
length \(L/D\). For any product \(Q\) of a proper subfamily, write
\(L=tQ+r\), \(0\le r<Q\). Directly counting the \(t\) or \(t+1\)
copies of each residue gives

\[
\boxed{\quad
\left\|\mathrm{law}(A\bmod Q)-u_Q\right\|_{\rm TV}
=\frac{r(Q-r)}{LQ}\le\frac{Q}{4L}.
\quad}
\tag{JPO-6}
\]

CRT and the invertible factors in the primary projections preserve this
distance for the corresponding joint primary marginal. Put
\(m=\min_iq_i\) and choose \(L=\lfloor D/\sqrt m\rfloor\). As
\(m\to\infty\), **every proper joint marginal** approaches its uniform
product law, uniformly over the subfamilies, since \(Q\le D/m\).
Meanwhile the real phase law converges to \(\delta_0\), and its full
joint distance from uniform tends to one.

This finite-ensemble construction is not the authenticated BBP orbit. It
is a precise falsifier for replacing the full interaction by any collection
of proper marginal conclusions, even many jointly checked ones.

## 4. Complete microscopic uniformity would overask

### JPO-5: finite-sample obstruction (PROVED PAPER)

If \(N\) samples lie in \(G[D]\), their empirical law \(\nu_N\) has at
most \(N\) support points. Consequently

\[
\boxed{\quad
\|\nu_N-u_D\|_{\rm TV}\ge1-\frac ND,\qquad
D\sum_x\nu_N(x)^2\ge\frac DN.
\quad}
\tag{JPO-7}
\]

Replace the first lower bound by zero when negative; the second is also
at least one. The support itself proves the TV bound. Cauchy--Schwarz
proves the collision bound. These statements do not assume distinct samples.

The inherited [authentic source height theorem](PI_PASCAL_PRIME_HEIGHT.md)
proves \(\log d_N\ge(3+o(1))N\), and \(d_N\mid D_N\). Thus the
authentic **complete carrier law** has TV distance tending to one from
uniform at every sampled horizon, independently of whether its real orbit
is normal. This is not a failure of real equidistribution: a weakly uniform
real law can remain supported on only \(N\) points of an exponentially
finer arithmetic grid.

Therefore a useful “all observers” proof combines the complete coordinates
and then tests **real coarse cells or low-frequency characters**. It cannot
require complete joint TV convergence to the uniform microscopic carrier.
The admissible scale must fit the number of time samples; the inherited
collision-to-entropy inequality makes that limitation explicit.

## 5. A quantitative transport contract

### JPO-6: decoder errors must be uniform in the time horizon (PROVED PAPER)

Suppose a joint observer produces decoded phases \(\widehat y_n\), and
write \(E_N=N^{-1}\sum_{n\le N}\|y_n-\widehat y_n\|_{\mathbb T}\).
The elementary character Lipschitz bound gives

\[
\left|\frac1N\sum e(hy_n)\right|
\le\left|\frac1N\sum e(h\widehat y_n)\right|+2\pi|h|E_N.
\tag{JPO-8}
\]

For pair collision probabilities \(Q_y(\rho)\) and
\(Q_{\widehat y}(\rho)\), Markov's inequality and the triangle inequality
give, for every \(\delta>0\),

\[
\boxed{\quad
Q_y(\rho)\le Q_{\widehat y}(\rho+2\delta)+2E_N/\delta.
\quad}
\tag{JPO-9}
\]

Only pairs with at least one decoding error greater than \(\delta\) are
discarded, and their fraction is at most \(2E_N/\delta\). These formulas
state the necessary rate when observer depth grows with horizon; pointwise
decoding as depth tends to infinity does not supply it.

For ordinary interval discrepancy \(D(\cdot)\), enlarging or shrinking
an interval by \(\delta\) changes its Lebesgue length by at most
\(2\delta\). Thus

\[
D(y_1,\ldots,y_N)
\le D(\widehat y_1,\ldots,\widehat y_N)+2\delta+E_N/\delta.
\tag{JPO-10}
\]

All statements are finite and source-independent. They are interfaces, not
new bounds on the authentic source.

### JPO-7: product of local precisions and the exact carry (PROVED PAPER)

Let a **chosen real residual** be \(z=m/D\), \(m\in\mathbb Z\), and
suppose \(v_p(z)\ge h_p\) for finitely many distinct primes. Then

\[
M=\prod_p p^{\max(0,h_p+v_p(D))}\mid m,
\qquad z\ne0\Longrightarrow |z|\ge M/D.
\tag{JPO-11}
\]

This follows directly by taking valuations of the numerator. It is a
genuine way to combine all specified local constraints. To exclude a
nonzero \(\rho\)-close residual one needs \(M>\rho D\).

For a circle difference, the residual is \(U_s-U_t-a\), where \(a\) is
the same chosen nearest integer/carry throughout the calculation. A
congruence of \(U_s-U_t\) does not transfer to it automatically. For example,
\(16/15\) has numerator divisible by \(16\), while its nearest residual
\(1/15\) does not. This is why adding dyadic precision without the lift
does not multiply a real separation bound for free. With exponential
\(D\), merely polynomial \(M\) still gives exponential separation.

## 6. All fixed p-adic limits can converge while real behavior differs

The following is a post-discovery strengthening of the moving-prime control
registered in the initial contract. It is a paper existence construction
for arbitrary real constants. The executable implementation takes rational
constants only; it does not purport to compute the floor of an arbitrary real.

### JPO-8: moving-prime control with absolute local precision (PROVED PAPER)

Let \(C\in\mathbb R\) and \(b\ge2\). Let \(p_n\) be the \(n\)-th
odd prime, \(q_n\) the smallest power of \(p_n\) at least \(32^n\),
and put

\[
m_n=\lfloor\log_2(n+1)\rfloor,\qquad M_n=m_n!.
\]

We have \(p_n>m_n\). Bertrand's postulate gives
\(p_n<2^{n+1}\), so

\[
32^n\le q_n<2\cdot64^n.
\tag{JPO-12}
\]

Also \(2M_n\le2^n\): use
\(m!\le2^{m(m-1)/2}\) and
\(1+m(m-1)/2\le2^m-1\le n\) for \(m\ge1\).

Choose \(k_n\) by rounding
\(q_n(b^nC-(n+1)^{-2})/M_n\) down, and subtracting one more if the
result is divisible by \(p_n\). Define

\[
H_0=0,\qquad H_n=M_nk_n/q_n,\qquad s(n)=H_n-bH_{n-1}.
\]

Then \(p_n\nmid M_nk_n\), so the exact reduced denominator is \(q_n\).
The rounding gives

\[
H_n=b^nC-\eta_n,\qquad
\frac1{(n+1)^2}\le\eta_n<\frac1{(n+1)^2}+16^{-n}.
\tag{JPO-13}
\]

For \(n\ge2\),

\[
s(n)=b\eta_{n-1}-\eta_n>0,\qquad
s(n)=\frac{b-1}{n^2}+O(n^{-3}).
\tag{JPO-14}
\]

The strict positivity follows from
\(b/n^2-(n+1)^{-2}-16^{-n}>0\). The first forcing value is unrestricted.
The telescoping series satisfies \(\sum_{n\ge1}b^{-n}s(n)=C\).

For any fixed prime \(p\), eventually \(p\ne p_n\), so

\[
v_p(H_n)\ge v_p(M_n)\longrightarrow\infty.
\]

Therefore \(H_n\to0\) in **every fixed \(\mathbb Q_p\)**; the forcing
\(s(n)\to0\) there too. Every fixed finite family, at every fixed absolute
precision, eventually sees zero. The primary phases are exactly zero there
once the moving denominator prime has left the family.

Yet the real circle sequence shadows \(b^nC\) with error tending to zero.
Its possible real occupation behavior is unrestricted by these conditions.
For \(b=16\), choosing \(C=1\) and \(C=1/3\) gives different limiting
real point masses, while all fixed local limits above are the same.

This does not contradict pointwise all-prime reconstruction. At every
finite time a different prime retains the missing component. There is no
single observer depth or finite prime set controlling all large times.
The forcing has rational values but is not asserted to be one fixed rational
function of \(n\); hence this is not a counterexample to Hypothesis A.

## 7. A stronger control: match the authentic observers and scalar height

The next construction arose from root/adversary synthesis. It sharpens the
previous theorem in the direction of the actual source, without claiming
to preserve the defining four-pole formula.

### JPO-9: source-matching moving prime (PROVED PAPER)

Keep the authentic \(U_n,r(n)\), and fix any real \(C\). Let \(p_n\)
be the least prime greater than \(16n\). Bertrand gives \(p_n<32n\).
The primes need not be distinct; \(p_n\to\infty\) is sufficient.
Use \(m_n,M_n\) from the preceding theorem and take \(q_n\) to be the
smallest power of \(p_n\) satisfying

\[
q_n\ge32n^4M_n.
\]

Round

\[
\frac{q_n}{M_n}\left(16^nC-\frac1{(n+1)^2}-U_n\right)
\]

down, adjusting by at most one more to obtain \(p_n\nmid k_n\), and set

\[
\delta_n=\frac{M_nk_n}{q_n},\qquad H_n=U_n+\delta_n,
\qquad H_0=0,\quad s(n)=H_n-16H_{n-1}.
\tag{JPO-15}
\]

The following statements hold simultaneously.

**Real shadow and positive forcing.** Exactly as before,

\[
H_n=16^nC-\eta_n,\qquad
\frac1{(n+1)^2}\le\eta_n<\frac1{(n+1)^2}+\frac1{16n^4}.
\tag{JPO-16}
\]

Hence \(s(n)>0\) for \(n\ge2\) and
\(s(n)=15n^{-2}+O(n^{-3})\). The real circle sequence has the same
occupation limits as \(16^nC\), and \(\sum16^{-n}s(n)=C\).

**Every authentic supported primary observation agrees, at every time.**
The phase of \(\delta_n\) is supported at only \(p_n>16n\), so

\[
\pi_p(H_n)=\pi_p(U_n)\quad(p\le8n).
\]

Moreover \(s(n)-r(n)=\delta_n-16\delta_{n-1}\), whose prime support is
contained in \(\{p_n,p_{n-1}\}\). For \(n\ge2\), both primes exceed
\(8n\), since \(16(n-1)\ge8n\). At the initial endpoint
\(\delta_0=0\), so \(s(1)-r(1)=\delta_1\), supported only at
\(p_1>16\). Thus

\[
\boxed{\quad
\pi_p(H_n)=\pi_p(U_n),\qquad
\pi_p(s(n))=\pi_p(r(n))\qquad(p\le8n).
\quad}
\tag{JPO-17}
\]

Here every authentic state and forcing prime lies below \(8n\). This
really preserves the complete tuple of all those phases; no marginal
factorization is involved. An extra prime beyond that conductor remains.

**Every fixed absolute p-adic observation also converges to the authentic
one.** For each fixed \(p\), eventually \(p\ne p_n\), and
\(v_p(\delta_n)\ge v_p(M_n)\to\infty\). Therefore

\[
H_n-U_n\to0,\qquad s(n)-r(n)\to0\quad\text{in }\mathbb Q_p.
\tag{JPO-18}
\]

This extends to every fixed finite translated Pascal difference:
\(\Delta^k(H-U)_n\to0\) and \(\Delta^k(s-r)_n\to0\) in \(\mathbb Q_p\),
for each fixed \(k\). It follows by finite integer linear combinations.
In particular, each fixed nonzero authentic dyadic valuation profile is
eventually unchanged, once the error valuation exceeds that fixed value.
The starting index depends on the prime, precision and order. This does
**not** retain the full all-time/all-order analytic Pascal profile uniformly.

There is a useful uniform strengthening for finite integer filters. Since
\(M_n\mid M_{n+j}\), and every subsequent new prime exceeds \(16n\),
for any \(p<16n\) and any integer polynomial \(P\),

\[
v_p\bigl(P(E)(H-U)_n\bigr)\ge v_p(M_n).
\tag{JPO-18a}
\]

Its degree may depend on \(n\); finite integer linear combinations cannot
lower that valuation. The corresponding forcing bound uses \(M_{n-1}\)
and \(p<16(n-1)\). For example, writing the authentic dyadic valuation
as \(\nu(k)=2k-s_2(k)-1\), one obtains simultaneously

\[
\nu(k)<v_2(M_n)\ \Longrightarrow\
v_2(\Delta^kH_n)=v_2(\Delta^kU_n)=\nu(k),\qquad k\ge1.
\tag{JPO-18b}
\]

For the forcing the same statement uses \(v_2(M_{n-1})\). This follows
from the strict inequality of valuations: adding a higher-valuation error
cannot change the lower valuation of the authentic value. Increasing the
depth of a finite local jet is therefore not enough without a quantitative
real transport theorem at the same depth.

**The same scalar logarithmic height bounds survive.** Since \(p_n>16n\)
does not divide \(d_n\), the reduced denominator of \(H_n\) is exactly
\(d_nq_n\). To check this, write \(U_n=a/d_n\). Its numerator over
\(d_nq_n\) is \(aq_n+d_nM_nk_n\). It is a unit at every old denominator
prime and at the new prime, so neither factor cancels. Minimality of the
chosen power gives

\[
q_n<32n^4M_np_n<1024n^5M_n,
\qquad\log q_n=O(\log n\log\log n)=o(n).
\]

Using the inherited height bounds for \(d_n\),

\[
\boxed{\quad
(3+o(1))n\le\log\mathrm{den}(H_n)\le(8+o(1))n.
\quad}
\tag{JPO-19}
\]

**General subexponential precision schedule.** In this source-matching
construction only, \(m_n=\lfloor\log_2(n+1)\rfloor\) can be replaced by
any nondecreasing integer sequence tending to infinity with \(0\le m_n\le n\)
and \(\log(m_n!)=o(n)\). Keep \(M_n=m_n!\) and choose \(q_n\) from
the same threshold \(32n^4M_n\). The rounding error remains at most
\(1/(16n^4)\), all local conclusions persist, and \(\log q_n=o(n)\).
For instance \(m_n=\lfloor\sqrt n\rfloor\) preserves dyadic source
jets of every order \(k\) with \(\nu(k)<v_2(m_n!)\), a range of order
\(\sqrt n\). This generalization is a paper theorem; the exact code
keeps the single declared logarithmic schedule.

Thus scalar height growth, an expanding authentic primary family, all fixed
local precision limits, fixed-order local Pascal limits and positive quadratic
forcing still do not force a unique real occupation law for this larger class.

**The exact exclusion is visible.** This construction violates the authentic
conductor: it introduces the new prime \(p_n>16n\), whereas the original
denominator divides the odd \(\mathrm{lcm}\) through \(8n-3\). It also
changes the fixed rational-function forcing. It does not preserve complete
monotonicity or the global all-order Pascal/Mahler source identities. The
different retained controls in this report and the older prescribed-constant
construction must not be combined into a claim that one counterfeit satisfies
all their hypotheses at once.

Conversely, if a candidate is known to have **no prime support outside the
authentic conductor**, and its entire primary tuple on that conductor agrees,
then JPO-1 reconstructs the same real phase exactly. In that setting the
counterfeit above is excluded. The next question remains the temporal
statistics of that already reconstructed phase.

### JPO-9a: the real forcing can agree to every algebraic order (PROVED PAPER VARIANT)

**Scope:** this is an additional paper construction. The executable probes
cover the preceding quadratic-target construction, not this variant.
It still introduces a new prime beyond the authentic conductor and does
not satisfy the fixed BBP rational-function forcing.

Write \(\alpha=\pi/16\), so the authenticated positive Green tail obeys

\[
U_n=16^n\alpha-T_n,\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
0<T_n<\frac1{(8n+1)(8n+2)}.
\]

Fix any real target constant \(C\), retain \(p_n>16n\) and the
factorial schedule \(M_n\), and put \(J_n=\lceil\sqrt n\rceil\).
Use the **rational** truncated authentic tail

\[
t_n=\sum_{j=1}^{J_n}16^{-j}r(n+j),\qquad
T_n-t_n=16^{-J_n}T_{n+J_n}.
\tag{JPO-20}
\]

Choose \(q_n\) to be the smallest power of \(p_n\) at least
\(32M_n16^{J_n}\). Round
\(q_n(16^nC-t_n-U_n)/M_n\) down and adjust by at most one to make
the resulting \(k_n\) a unit at \(p_n\). Set
\(H_n=U_n+M_nk_n/q_n\), \(H_0=0\), and
\(s(n)=H_n-16H_{n-1}\), as before.

There is a nonnegative rounding error \(\varepsilon_n\) such that

\[
H_n=16^nC-t_n-\varepsilon_n,
\qquad 0\le\varepsilon_n<2M_n/q_n\le16^{-J_n}/16.
\]

Relative to the exact \(C\)-orbit with the authentic Green tail, define

\[
E_n=H_n-(16^nC-T_n)
=(T_n-t_n)-\varepsilon_n.
\]

Equation JPO-20 and the tail bound show

\[
-16^{-J_n}/16<E_n<16^{-J_n}T_{n+J_n}<16^{-J_n}/2,
\qquad |E_n|\le16^{-J_n}.
\tag{JPO-21}
\]

For \(n\ge2\), the exact tail recurrence therefore gives

\[
\boxed{\quad s(n)-r(n)=E_n-16E_{n-1},\qquad
|s(n)-r(n)|\le16^{-J_n}+16^{1-J_{n-1}}.
\quad}
\tag{JPO-22}
\]

The right side is \(O(16^{-\sqrt n})\), hence \(o(n^{-A})\) for
every fixed \(A>0\). The first forcing value is not covered by that
asymptotic estimate: setting \(E_0=\alpha-C\) restores the identity
also at \(n=1\). This initial endpoint must not be omitted.

Since \(r(n)\sim15/(64n^2)>0\), the new forcing is eventually positive
and has **every algebraic-order real asymptotic coefficient** of the
authentic forcing. Every fixed finite real difference of \(s-r\) is
also \(o(n^{-A})\) for every fixed \(A\), by finite linear combination.
This is asymptotic agreement, not equality at finite times.

All primary and local-precision conclusions of JPO-17, JPO-18 and JPO-18a
still hold: they use the numerator factor, new prime and common source,
not the real target used in the rounding. The exact reduced denominator is
again \(d_nq_n\). Minimality of \(q_n\) now gives

\[
\log q_n\le J_n\log16+\log M_n+O(\log n)=o(n),
\]

so the same leading scalar height bounds survive. Finally
\(H_n=16^nC-T_n+E_n\) shadows \(16^nC\), and its real occupation
limits can still be those of any chosen \(C\).

The exact rational-function restriction has real force here. A nonzero
rational function of \(n\) has a nonzero leading power asymptotic at
infinity; it cannot be \(o(n^{-A})\) for every \(A\). Thus if the
constructed \(s(n)\) were one fixed rational function for all sufficiently
large integers, JPO-22 would force \(s(n)=r(n)\) eventually. This is
impossible in the construction: it would imply
\(H_n-U_n=16(H_{n-1}-U_{n-1})\) eventually, preserving the nonzero
odd reduced denominator of that difference, whereas its exact denominator
\(q_n\) is a power of \(p_n\to\infty\). The altered source really
leaves the rational-function class; it is not a counterexample within
Hypothesis A.

No global complete-monotonicity statement or all-time/all-order Pascal
identity is claimed for this variant. The known conductor bound and exact
rational-function identity explicitly exclude it. All of those exclusions
must remain visible when applying the countermodel.

## 8. Consequence for the Hypothesis A program

The strongest surviving reading of the proposal is to keep all authentic
source information, including the exact conductor, common time index,
integer lift and higher interactions, then establish a real coarse collision
bound or a mixed-character estimate such as JPO-4. The complete tuple is
available; the statistical bound is the open arithmetic theorem.

The present work earns exact reconstruction and transport lemmas, a sharp
decoder obstruction, calibrated higher-interaction controls, and a stronger
limit-order countermodel. It does not derive uniform frequencies from the
fixed four-pole law. A proof claiming to do so should identify which genuinely
source-specific estimate excludes these controls and then supply that estimate.

The weakest useful hypothesis need not demand all blocks be exactly uniform
at a finite stage, nor all primary coordinates become independent. It can
bound a single selected joint collision statistic at a suitable real scale.
Its derivation from the actual source, rather than its sufficiency for
normality, remains the substantive task.

## 9. Reproducibility and provenance

Implementation: [joint_primary_observers.py](../../observational_succ/joint_primary_observers.py).
Tests: [test_joint_primary_observers.py](../../tests/test_joint_primary_observers.py).
Probe: [joint_primary_observers_probe.py](../../scripts/joint_primary_observers_probe.py).
Receipt: [PI_JOINT_PRIMARY_RECEIPT.json](PI_JOINT_PRIMARY_RECEIPT.json).

The 25 focused tests include independent subgroup enumeration, complete small
fibers, exact CRT residue counts, literal four-pole reconstruction, deliberate
independent-marginal substitution, omitted-carry failure, and held-out source
indices. The standalone receipt records the exact cases and hashes of all
executable inputs. No infinite source claim is inferred from those finite runs.

Inherited source: [source path selection](PI_PATH_SELECTION_SYNTHESIS.md),
[all-time finite-prime correlation](PI_FINITE_PRIME_CORRELATION.md),
[Pascal/Lucas quotient](PI_PASCAL_LUCAS_QUOTIENT.md), and
[prime-height proof](PI_PASCAL_PRIME_HEIGHT.md). Imported archives and prior
claim authority are unchanged. Bertrand's postulate is used only for the
explicit prime-size bounds; see the primary formal library statement
[`Mathlib.NumberTheory.Bertrand`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Bertrand.html).
That citation does not grant new formal authority to the constructions here.
