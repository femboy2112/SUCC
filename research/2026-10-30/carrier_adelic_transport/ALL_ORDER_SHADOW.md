# Same complete polar data, different selected boundary

**Status: PROVED LOCAL (paper theorem); exact finite regression tests are
separately scoped.** This theorem changes the source after a declared prefix.
It does not disprove normality of pi. It identifies exactly what an observer
of all asymptotic coefficients / all spectral pole residues still forgets.

## 1. A constructive general theorem

Let b >= 2 be an integer radix and let r(n) be a strictly positive,
strictly decreasing rational sequence
with r(n)=O(n^-2). Choose an arbitrary prefix length M >= 0 and integer
K >= 1. Put

\[
q=\sum_{j=1}^{M+K}b^{-j}r(j),\qquad
L_n=\begin{cases}M+K-n,&0\le n\le M,\\K+n-M,&n\ge M,\end{cases}
\]

\[
d_n=\sum_{j=1}^{L_n}b^{-j}r(n+j),\qquad
\widetilde U_n=b^n q-d_n.
\]

All quantities at finite time are rational and use only finitely many values
of the original source. No irrational boundary value or digit of pi enters
the construction. In particular d_0=q, so **the initial seed is exactly zero**.

Define the changed forcing by
`r_tilde(n)=b*d_(n-1)-d_n`. Telescoping finite sums gives the explicit law

\[
\widetilde r(n)=\begin{cases}
r(n),&n\le M,\\
r(n)-b^{-\ell}r(n+\ell)-b^{-\ell-1}r(n+\ell+1),&n>M,
\end{cases}\qquad \ell=K+n-M-1.\tag{F1}
\]

For n<=M the two finite sums have the same terminal source index; every
term except r(n) cancels. For n>M the second sum has two new terminal
terms, giving F1. Consequently

\[
\widetilde U_0=0,\qquad
\widetilde U_n=b\widetilde U_{n-1}+\widetilde r(n).\tag{F2}
\]

The source and selected orbit agree exactly with the original through M.
For n>M, monotonicity and ell>=K give

\[
0<\frac{r(n)-\widetilde r(n)}{r(n)}
<b^{-\ell}(1+b^{-1})\le b^{-K}(1+b^{-1})<1.\tag{F3}
\]

Thus the changed source stays strictly positive and can be made arbitrarily
close in **uniform relative error**, while retaining any prescribed finite
prefix. At fixed M,K its difference from the original is O(b^-n n^-2).
It is smaller than every inverse power of n.

Since `0<d_n<=r(n+1)/(b-1)`, one has d_n -> 0 and

\[
\sum_{n\ge1}b^{-n}\widetilde r(n)
=\lim_{N\to\infty}b^{-N}\widetilde U_N=q\in\mathbb Q.\tag{F4}
\]

The completed orbit is therefore rational and eventually periodic in
base b. Every asymptotic coefficient of the source, whenever such an
expansion exists, has been retained,
but the completed boundary is nonnormal.

## 2. Authentic BBP realization, with an explicit signed failure

Instantiate b=16 and

\[
r_u(n)=R(8n-7+u),\quad
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}.
\]

For real |u|<1, a>0 and
`R(a)=6/[a(a+3)]+4/[a(a+4)]+5/[a(a+5)]`, so positivity and strict
decrease hold. For the remainder of this section fix u=0, so all finite
values are rational. Let h be the positive
denominator of q in lowest terms. Then

\[
e(h\widetilde U_n)=e(-h d_n),\qquad e(x)=\exp(2\pi i x).
\]

Since `R(a)<15/a^2`, the original future tail bounds d_n by
`1/(8n+1)^2` for n>=1. In particular
`sum_(n>=1) d_n < (1/64) sum_(n>=1)n^-2 < 1/32`.
The elementary inequality `|e(x)-1|<=2*pi*|x|` now proves

\[
\boxed{\left|\sum_{n=1}^N e(h\widetilde U_n)-N\right|
<\frac{\pi h}{16}\quad\text{for every }N\ge1.}\tag{F5}
\]

This is an actual all-horizon signed noncancellation theorem for the
explicit changed source. The test character h depends on M,K; it is fixed
as N tends to infinity. This dependence must not be suppressed.

### A minimal explicit member: the literal carry becomes 3,2,2,2,...

For M=0,K=1, the entire construction reduces to

\[
\widetilde r(n)=r(n)-16^{-n}r(2n)-16^{-n-1}r(2n+1),
\qquad q=r(1)/16=47/240.\tag{F7}
\]

The two correction sums remove, respectively, every even-indexed and every
odd-indexed term after the first from the weighted boundary series. This
is a direct independent proof that its completed value is q.
Since 16 is 1 modulo 15,
`{16^n q}=2/15` for every n>=1. The bound `0<d_n<1/(8n+1)^2<2/15`
implies `{U_tilde_n}=2/15-d_n`. The literal carry from the zero state is 3
at the first step and exactly 2 at every subsequent step. For every fixed
nonzero integer h,

\[
\left|\sum_{n=1}^N e(h\widetilde U_n)-N e(2h/15)\right|
<\pi |h|/16.\tag{F8}
\]

Thus every fixed character is asymptotically fully coherent in this
small explicit member, while its complete spectral polar data remain the
authentic data. The source has changed exactly as displayed in F7.

## 3. The entire remainder invisible to every pole residue

Let `D(s,u)=sum n^-s r_u(n)` initially on Re(s)>-1 and |u|<1, and define
`D_tilde` with the changed source F1 at every u. On each compact subset of
|u|<1, each fixed u-derivative of the difference satisfies

\[
\partial_u^a[\widetilde r_u(n)-r_u(n)]
=O_{a,M,K}(16^{-n}n^{-a-2}).\tag{F6}
\]

This follows directly by differentiating the four rational poles; their
leading cancellation is preserved by derivatives. Even the weaker
O(16^-n n^-a-1) bound would suffice. Multiplication by n^-s and any finite
power of log n preserves uniform summability on compact subsets of the
entire s-plane. Thus

\[
E(s,u)=\sum_{n\ge1}n^{-s}[\widetilde r_u(n)-r_u(n)]
\]

is jointly holomorphic on C x {|u|<1}, and
`D_tilde(s,u)=D(s,u)+E(s,u)` meromorphically.

**Every pole location, every polar Laurent coefficient, and every
u-derivative of every residue agrees exactly.** All complete algebraic
asymptotic jets agree as well. But E is not zero: for real s and real |u|<1,
every nonzero summand is strictly negative, so E(s,u)<0. In particular
**regular Laurent finite parts differ**. This is not equality of the full
analytic germ or the full function.

The distinction is decisive: all polar data can lose an entire function;
the complete analytic source has not been retained by that projection.

## 4. Compatibility with finite source reconstruction

The four-pole residue reconstruction in SPECTRAL_SOURCE_TRANSPORT.md assumes
a rational function of time with a bounded number of fixed poles. F1 has
an exponentially decaying time-dependent correction and is outside that
class. There is no contradiction:

- bounded rational pole class + sufficient exact residues identifies source;
- unrestricted positive rational-valued sequence + every asymptotic residue
  does not identify source or selected boundary;
- entire analytic germ equality is stronger than equality of polar data.

This extends the **finite-jet** mutation axis in
`research/2026-10-24/PI_SOURCE_GENESIS_NONCOBOUNDARY.md` and the finite
prefix/moment cubature controls of PRs #408/#415. It does not replace their
positive Hausdorff-measure hypotheses: no common fixed positive Laplace
measure is claimed for this new changed source. It also does not preserve
the original four rational poles, full prime-place behavior, all finite
moments, or the source's complete analytic germ.

## 5. Verdict and next falsifier

The inference “complete asymptotic / zeta polar matching plus zero seed
forces the authentic selected statistics” is REFUTED in the declared
positive rational-sequence class by F1–F5. Pi normality remains OPEN.
An acceptable next source theorem must retain the full fixed-pole law or
control the missing entire remainder at the exponentially magnified
selected phase. The explicit family is a regression control for any such
proposed estimate.
