# Which boundary phase dynamics admit finite linear reconstruction?

Date: 2026-11-12. Parent: Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`.
Authority: elementary paper proofs below; finite implementation checks are
separate. Classical polynomial root counting, finite linear algebra and the
classical irrationality of pi are used. No academic priority, formal-kernel
verification, normality or statistical saving is asserted.

## The dependency cut

PR #605's ordered closure theorem reconstructs an entire accessible sector
when a finite word span closes under every declared generator. That is a
useful conditional instrument. Can the actual completed BBP phase readout
itself have an exact finite-dimensional stationary linear realization?

**Answer: no.** This obstruction follows from irrationality alone, without
assuming any digit statistics. It does not forbid a finite description,
nonlinear dynamics, time-dependent linear dynamics, or finite-horizon fits.
The completed circle phase already has the one-complex-coordinate nonlinear
update `a_(n+1)=a_n^16`.

We distinguish three ranks throughout: the rank-four signed index-pole
model, the infinite-rank positive Green-memory model, and the phase-Hankel
rank studied here. The first two were established in the archive; their
different observation maps do not transfer ranks or positivity between them.

## HBC-01: finite phase-Hankel rank is exactly rationality

Let `b>=2` be an integer, `h` a nonzero integer, and `x` a real number. Put

\[
 a_n=e(hb^n x),\qquad e(t)=\exp(2\pi i t),\qquad n\ge0.
\]

The infinite Hankel matrix is `(a_(n+j))_(n,j>=0)`; its rank means the
supremum of the ranks of its finite submatrices, over the complex numbers.

**Theorem.** The following are equivalent:

1. `x` is rational.
2. The sequence `a_n` is eventually periodic.
3. The phase Hankel matrix has finite rank.
4. On some tail the sequence obeys a nonzero constant-coefficient linear
   relation `sum_(j=0)^d c_j a_(n+j)=0` for every sufficiently large `n`.
5. On some tail there is a finite-dimensional stationary linear realization
   `a_(N+n)=C A^n v`, with fixed complex matrix `A`, row `C` and vector `v`.

**Proof.** If `x` is rational, multiplication by `b` acts on a finite set of
residues modulo a denominator, so the phase sequence is eventually periodic.
If its preperiod and period are `m` and `p`, then the Hankel columns satisfy
`column_(j+p)=column_j` for all `j>=m`, so rank is at most `m+p`.
The same eventual relation supplies item 4. Conversely, finite rank makes
some finite initial collection of columns linearly dependent and hence
supplies item 4, even from `n=0`.

Suppose now that `x` is irrational and item 4 holds. The points
`z_n=e(hb^n x)` are pairwise distinct: equality for `n>m` would imply
`h(b^n-b^m)x` is an integer, making `x` rational. The relation is

\[
 P(z_n)=0,\qquad P(z)=\sum_{j=0}^{d}c_j z^{b^j}.
\]

The exponents are distinct, so `P` is a nonzero polynomial whenever the
coefficient vector is nonzero. A nonzero polynomial cannot vanish on the
infinitely many distinct points of any tail. Thus item 4 is impossible for
irrational `x`. This also shows directly that eventual periodicity implies
rationality. Item 5 implies item 4 by the characteristic-polynomial identity
for `A`. An eventual recurrence with nonzero highest coefficient has its
usual finite companion realization, proving the converse. This completes
the equivalences. The zero sequence is not an exceptional case here because
every `a_n` has modulus one. QED.

**BBP corollary.** At the unchanged zero seed, the classical BBP identity gives

\[
 U_n+T_n=16^n\pi/16.
\]

Hence the completed readout `e(h(U_n+T_n))` has infinite Hankel rank for
every nonzero integer `h`, by classical irrationality of pi. This statement
is about the *completed* readout. It does not silently replace it by the
rational raw phase `e(hU_n)`; the latter needs its own argument or a paid
approximation bound. No new irrationality theorem is claimed.

## HBC-02: a finite rectangular rank certificate with an explicit horizon

**Theorem.** For every irrational `x`, every `N>=0`, and every `d>=0`, the
matrix

\[
 H_{n,j}=e(hb^{N+n+j}x),\qquad
 0\le n<b^d,\quad 0\le j\le d,
\tag{1}
\]

has full column rank `d+1`. Thus every proposed order-`d` homogeneous
recurrence fails at some one of these `b^d` consecutive starting positions.

**Proof.** A nonzero column dependence gives `P(z_n)=0` with the polynomial
of HBC-01 and `b^d` distinct nonzero points. Divide by `z`: the resulting
nonzero polynomial has degree at most `b^d-1`, too small for `b^d` distinct
roots. This includes `d=0`, when it is a nonzero constant. More generally,
if the first and last nonzero coefficients occur at indices `k` and `l`,
division by `z^(b^k)` gives degree `b^l-b^k`; a dependence on more than that
many distinct points is impossible. QED.

The horizon in (1) is a sufficient uniform root-count bound. Optimality is
not claimed. It is exponential in the order. No assertion is made that
every square leading Hankel section is nonsingular for every irrational
`x`. The largest clock index used in (1) is `N+b^d-1+d`.

## HBC-03: the obstruction persists for finite Fourier filters

Let `f(t)=sum_(k=k_-)^(k_+) alpha_k e(kt)` be a nonconstant trigonometric
polynomial, with fixed complex coefficients. For irrational `x`, the
sequence `f(b^n x)` has infinite Hankel rank and no eventual nonzero
constant-coefficient linear recurrence.

**Proof.** Write `F(z)=sum alpha_k z^k`. A recurrence with largest nonzero
coefficient `c_d` would give the Laurent polynomial

\[
 L(z)=\sum_{j=0}^{d}c_j F(z^{b^j})
\]

vanishing at all the distinct `e(b^n x)` on a tail. It is nonzero: if `F`
has a positive frequency, its largest positive frequency multiplied by
`b^d` occurs only in its last summand and has nonzero coefficient. If it
has no positive frequency, nonconstancy gives a negative frequency; its
most negative frequency multiplied by `b^d` is unique for the same reason.
Multiplication by a suitable power of `z` turns `L` into a nonzero ordinary
polynomial, which cannot have infinitely many roots. QED.

For rational `x`, every such readout is eventually periodic. A constant
filter is excluded: it has rank at most one for every source. A stationary
linear filter whose output happens to be constant therefore does not
reconstruct the discarded nonconstant phase dynamics.

## HBC-04: full rank does not buy uniform stability

For arbitrary `M>=1`, use the matrix (1) with `0<=n<M`, and put
`A(x)=H(x)/sqrt(M)`. For any real `x,y`, the chord bound gives

\[
 \|A(x)-A(y)\|_{\rm op}
 \le \|A(x)-A(y)\|_{\rm F}
 \le 2\pi |h|\sqrt{d+1}\,b^{N+M-1+d}|x-y|.
\tag{2}
\]

This is intentionally a simple worst-clock bound. At `y=0`, every entry
of `H(y)` is one, so for `d>=1` it has rank one and a nonzero column kernel.
For a unit vector `c` in that kernel,

\[
 \sigma_{\min}(A(x))\le\|A(x)c\|
 \le2\pi |h|\sqrt{d+1}\,b^{N+M-1+d}|x|.
\tag{3}
\]

Here `sigma_min` means the minimum over all unit column vectors, and is
zero for a matrix with a column kernel. Irrational `x` can approach zero
arbitrarily closely. Even when `M>=b^d` and HBC-02 guarantees exact full
column rank, its least singular value therefore has no uniform positive
lower bound over irrational sources.

The square of this number is the least eigenvalue of the normalized Gram:

\[
 \lambda_{\min}(G)=
 \min_{\|c\|_2=1}\frac1M\sum_{n=0}^{M-1}
 \left|\sum_{j=0}^{d}c_j a_{N+n+j}\right|^2,
 \qquad G=A^*A.
\tag{4}
\]

It is the smallest normalized recurrence residual at that finite horizon.
Exact irrationality proves strict positivity at the horizon of HBC-02;
it supplies no source-uniform quantitative margin. Equation (3) is a
concrete countermodel to that stronger inference. It does not say a
specific certified finite Gram for pi cannot have a good margin.

## HBC-05: a Gram lower bound displays the unpaid signed estimate

Let `W_(N,M)(q)=M^-1 sum_(n=0)^(M-1) e(q b^(N+n)x)`. With inner products
conjugate-linear in their first entry, the exact Gram entries are

\[
 G_{ij}=W_{N,M}\big(h(b^j-b^i)\big),\qquad G_{ii}=1.
\tag{5}
\]

For any certified bounds `|G_ij|<=u_ij` on off-diagonal entries,

\[
 \lambda_{\min}(G)\ge
 1-\max_i\sum_{j\ne i}u_{ij}.
\tag{6}
\]

To see this directly, expand `c*Gc`, bound each off-diagonal real part by
its absolute value, and use `2|c_i c_j|<=|c_i|^2+|c_j|^2`. A common bound
`u` gives `lambda_min>=1-du`. This is a useful **finite certificate** when
the right side is positive. It is not an automatic consequence of full
rank. For growing `d`, the frequencies in (5) also grow; a fixed-frequency
limit theorem cannot be invoked uniformly without further work.

For `d=1`, `lambda_min=1-|W_(N,M)(h(b-1))|` exactly, while the fixed
coefficient vector `(-1,1)/sqrt(2)` has residual
`1-Re W_(N,M)(h(b-1))`. At `b=16,h=1`, a positive all-large-shell lower
bound on this particular residual is precisely the existing (CH) rung.
Adding a separate constant reference column to the single-phase column
instead gives residual `1-Re W_(N,M)(h)`; at `h=1` this is R0. These are
identities locating the target, **not** new sufficient source estimates.

## HBC-06: infinite rank can coexist with maximal signed coherence

The source-independent irrational control

\[
 \xi=\sum_{j\ge0}16^{-2^j}
\]

has an unbounded-gap, non-eventually-periodic hexadecimal expansion, so
is irrational. HBC-01 gives infinite phase-Hankel rank. Nevertheless,

\[
 \frac1B\sum_{n=B}^{2B-1}e(16^n\xi)\longrightarrow1.
\tag{7}
\]

Here is a direct elementary proof, consistent with the stronger archived
sparse-selector theorem. Take `w=ceil(log_16 B)` for `B>=16`. Except at
indices `n` with a power of two in `(n,n+w]`, the fractional part of
`16^n xi` is at most `16^-w/15`. In the interval `[B,2B)` the exceptional
indices number at most `2w`: the interval `(B,2B+w]` contains at most two
powers of two because `w<B`. Thus the distance of the average in (7)
from one is at most

\[
 \frac{4w}{B}+\frac{2\pi}{15}16^{-w}\longrightarrow0.
\]

The non-eventual periodicity used above is elementary: an eventually
periodic digit sequence with infinitely many ones has bounded gaps between
ones, contrary to the gaps between consecutive powers of two. There is no
terminating/recurring-15 ambiguity in this all-zero/one expansion.

For a same-forcing BBP control set `s=xi-pi/16`. The exact completed state
is `U_n(s)+T_n=16^n xi`; the original four-pole forcing is unchanged, but
the initial seed is not zero. Infinite phase rank therefore cannot itself
authenticate the desired zero seed or imply R0. This control does not
refute R0 for the genuine source; it refutes a rank-only implication.

## Verdict, scope and next lamp

The finite stationary linear reconstruction route is closed for the
nonconstant completed BBP phase readout by HBC-01. This is a genuine
restriction of the proposed instrument, not a statistical advance toward
normality. HBC-02 identifies a finite discriminating horizon; HBC-04 pays
the missing conditioning boundary; HBC-05 exposes the exact signed
quantities a stable finite approximation would need to control.

A useful next construction may use growing dimension, nonlinear dynamics,
nonautonomous/source-labelled operators or target-specific certificates.
It must retain the actual seed and supply an independently proved error or
signed margin. Merely assuming a uniform Gram gap restates another part of
the arithmetic problem. Pi normality, R0, Goldbach and RH remain OPEN.

Repository antecedents and exact inspected donor heads are recorded in
[ARCHIVE_MAP.md](ARCHIVE_MAP.md). None of the preserved source files or
imported statements is modified by this dossier.
