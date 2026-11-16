# Period-four algebra and the authentic carry argument

**Status:** exact algebraic translation and diagnostic construction. The
source-specific carry-density theorem is still open. Parent source snapshot:
`fec5cdda24ca36328e123b0b367a0628491e1eb8`.

## 1. The two signs and their domains

For every integer `n`, including negative integers, define

\[
s(n)=(-1)^{\lfloor n/2\rfloor},\qquad
w(n)=\Re((1+i)i^n).
\]

The table is exact and completely specifies these periodic functions:

| `n mod 4` | bit pair `(n_1,n_0)` | `s(n)` | `w(n)` | source slope residue `d(n)` |
|---|---|---|---|---|
| 0 | (0,0) | +1 | +1 | 11 |
| 1 | (0,1) | +1 | -1 | 11 |
| 2 | (1,0) | -1 | -1 | 3 |
| 3 | (1,1) | -1 | +1 | 3 |

Here `d(n)` is the least nonnegative representative of the original rational
forcing derivative modulo 16. It is not the real derivative. Indeed

\[
r'(n)=-\frac{32}{(8n-7)^2}
 +\frac1{(2n-1)^2}+\frac8{(8n-3)^2}
 +\frac2{(4n-1)^2}
\equiv10+(2n-1)^{-2}\pmod {16}.
\]

Every denominator in this displayed derivative is odd. The first term vanishes
modulo 16, the third is 8, and the fourth is 2. Directly examining the four
residues of `n` gives the user-selected decomposition

\[
\boxed{d(n)=7+4s(n).}
\]

The code `observational_succ/bbp_spatial_haar_lift.py:derivative_slope` already
computes this residue. The new observation is its explicit sign decomposition.
The real derivative is negative for `n>=1`, as established by the inherited
positive moment representation. No real positivity follows from the residues.
Both residue values have 2-adic norm one. Modulo 8 they both reduce to 3.
Consequently their distinction first appears in this fourth binary bit.

Two further finite-ring identities, not new analytic estimates, are

\[
d(n)^2\equiv9\pmod {16},\qquad
d(n)^{-1}\equiv7-4s(n)=d(n+2)\pmod {16}.
\]

## 2. Walsh character in one addition law, quadratic sign in another

For all integers `m,n`,

\[
\boxed{
s(n)=(-1)^{n(n-1)/2}=i^{n(n-1)}
 =\cos(\pi n/2)+\sin(\pi n/2),
}
\]

\[
s(m+n)=s(m)s(n)(-1)^{mn},\qquad
w(n)=s(n+1)=(-1)^n s(n)=(-1)^{n(n+1)/2}.
\]

**Proof.** If `n=2k`, then `n(n-1)/2=k(2k-1)` has parity `k`. If
`n=2k+1`, then `n(n-1)/2=k(2k+1)` also has parity `k`. This includes negative
`k`. The addition identity follows from
`binom(m+n,2)=binom(m,2)+binom(n,2)+mn`. The remaining assertions follow
from the four residue classes.

Writing `n=n_0+2n_1 mod4` gives

\[
s(n)=(-1)^{n_1},\qquad w(n)=(-1)^{n_0+n_1}.
\]

Thus both are linear Walsh characters for bitwise XOR on two bits. For ordinary
integer addition, the carry changes the rule: the sign has the explicit
bilinear defect `(-1)^(mn)`. Equivalently `q(n)=binom(n,2) mod2` is a
quadratic refinement of `b(m,n)=mn mod2` on `Z/4Z`. It does not descend to
`Z/2Z`, since `q(n+2)=q(n)+1`. The pairing is degenerate on `Z/4Z`; no
nondegenerate quadratic Gauss-sum claim is being made.

For `|z|<1`, the ordinary generating function is

\[
\sum_{n\ge0}s(n)z^n=\frac{1+z}{1+z^2}.
\]

Its finite Fourier support is exactly the two quarter-turn frequencies:

\[
s(n)=\frac{1-i}{2}i^n+\frac{1+i}{2}(-i)^n.
\]

## 3. The exterior/Clifford interpretation is literal

Take mutually orthogonal Clifford generators, so distinct generators
anticommute. Reversing the order of a grade-`k` basis blade requires
`binom(k,2)` swaps. Therefore reversion acts by

\[
\widetilde{A_k}=s(k)A_k.
\]

Grade involution acts by `(-1)^k`; composing it with reversion gives Clifford
conjugation, with grade sign `w(k)`. This is also the sign of reversal in an
exterior product. In a positive orthonormal Clifford basis the square of
`e_1...e_k` is `s(k)`; for another signature its square additionally contains
the product of the generator squares. The grade interpretation is for
nonnegative grades; the numerical residue identities themselves extend to all
integers.

Primary reference: Douglas Lundholm and Lars Svensson, *Clifford algebra,
geometric algebra, and applications*, [arXiv:0907.5356](https://arxiv.org/abs/0907.5356),
§2.3, Definition 2.7 and Table 2.1 (printed pp. 16–17). Their table explicitly
has reversion `++--`, grade involution `+-+-`, and conjugation `+--+`.

This identifies the same algebraic sign operation. It does not establish a
physical spin system or entanglement in the BBP process.

## 4. Haar functions and the exact clock/cofactor gate

On `0<=x<1`, define the two Rademacher functions

\[
a(x)=(-1)^{\lfloor2x\rfloor},\qquad
b(x)=(-1)^{\lfloor4x\rfloor},\qquad c(x)=a(x)b(x).
\]

Their four-quarter patterns are respectively `++--`, `+-+-`, and `+--+`.
Each is a Walsh function; `a` is the top Haar wavelet, while `b` and `c` are
specified sums/differences of the next two Haar wavelets. For residues `j`,
`s(j)=a(j/4)` and `w(j)=c(j/4)`.

For the authentic source, put `U_n=C_n+y_n`, with real `C_n=floor(U_n)` and
`0<=y_n<1`. Its inherited source identity is `[U_n]_4=n mod4`, where brackets
mean the dyadic residue of an odd-denominator rational. Consequently, writing
`j=n mod4` and `k=[y_n]_4`, the **actual carry** satisfies `C_n=j-k mod4`.

The signed gate is the following exact ordered table:

| clock `j` / cofactor `k` | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | +1 | +1 | -1 | -1 |
| 1 | -1 | +1 | +1 | -1 |
| 2 | -1 | -1 | +1 | +1 |
| 3 | +1 | -1 | -1 | +1 |

Equivalently, with `W(j,k)=w(j-k)`,

\[
\boxed{W(j,k)=s(j+1)s(k)(-1)^{jk}.}
\]

For `j=j_0+2j_1`, `k=k_0+2k_1`, this becomes

\[
\boxed{W(j,k)=(-1)^{j_0+j_1+k_1+j_0k_0}.}
\]

The mixed bit term is explicitly retained. The source clock `j` alone is
uniform across blocks of length four; this does not set the joint distribution
of `(j,k)`. No source uniformity or independence is assumed here.

Using `a_j=s(j)` and `c_j=w(j)`, another exact decomposition is

\[
W=\tfrac12(a\otimes a+c\otimes c-a\otimes c+c\otimes a).
\]

The symmetric part is `cos(pi(j-k)/2)` and the antisymmetric part is
`-sin(pi(j-k)/2)`. The matrix has rank two; its only nonzero circulant Fourier
eigenvalues have modulus `2 sqrt(2)`. Thus the carry gate has an explicitly
ordered, antisymmetric component, not only a positive radial component.

## 5. A joint-law control aligned with this very gate

On the continuous unit square, let

\[
f(x,y)=a(x)c(y)-c(x)a(y),\qquad
p_\varepsilon(x,y)=1+\varepsilon f(x,y),\quad |\varepsilon|\le\tfrac12.
\]

Since `f` takes values in `{-2,0,2}`, this is a nonnegative density. Its
marginals are uniform because `a` and `c` have zero integral. Moreover
`f(y,x)=-f(x,y)`. Every integrable symmetric observable has the same expectation
as for two independent uniforms, and the full unordered pair distribution is
identical. In particular the maximum has CDF `r^2` for every `0<=r<=1`.

Nevertheless set `J=floor(4X)`, `K=floor(4Y)`, and evaluate exactly the ordered
carry sign `W(J,K)`. Orthogonality of `a,c` and the displayed decomposition give

\[
\boxed{\mathbb E_\varepsilon W(J,K)=-\varepsilon,
\quad
\Pr_\varepsilon((J-K)\bmod4\in\{1,2\})
=\tfrac12+\tfrac\varepsilon2.}
\]

For `epsilon=-1/2` and `+1/2`, all symmetric observable laws agree but the carry
gate frequencies are respectively `1/4` and `3/4`. This control is a joint
probability model, not another solution of the authentic BBP recurrence.

There is an explicit constructive weave. Draw independent uniforms `U,V`, put
`R=sqrt(U)` and `L=RV`, then select the ordered pair `(R,L)` with conditional
probability `(1+epsilon*f(R,L))/2`, and `(L,R)` otherwise. On the triangle
`0<L<R<1`, the unordered coordinates have density 2: the transformation
`(R,V)->(R,L)` has Jacobian `R`, and the radial density is `2R`. Multiplying
by the chosen orientation probability gives exactly `p_epsilon`. When
`epsilon=0`, the orientation is a fair coin and `(X,Y)` is a pair of independent
uniforms, with `max(X,Y)=sqrt(U)` holding pathwise in this coupling. Changing
only the conditional orientation coin produces the dependent controls, retaining
the entire unordered law. Thus a radius, a ratio, and a declared orientation rule
provide an exact positive construction behind the user's weaving intuition.

An important calibration: if `c` is replaced by `b` in `f`, the density remains
a valid antisymmetric control, but its perturbation is orthogonal to `W` and
does not change this carry-gate expectation. A probe must be aligned with the
actual sign being tested. Generic orientation sensitivity is not sufficient.

## 6. A stochastic successor model, with its law declared

If `N_t` is a Poisson count with rate one, its probability generating function
gives

\[
\mathbb E s(N_t)=e^{-t}(\cos t+\sin t),\qquad
\mathbb E w(N_t)=e^{-t}(\cos t-\sin t).
\]

These follow directly by separating even and odd terms in
`e^(-t) sum s(n)t^n/n!`. Deterministic unit waiting times instead give
`N_t=floor(t)`; independent unit-rate exponential waiting times give the Poisson
count and Gamma-distributed arrival times. This is one precise way to couple
Gamma volumes, a successor count, and the period-four sign. The random law is
an input and has not been derived for BBP.

## 7. Verification, novelty, and remaining edge

During construction an independent exact-rational scratch check performed
17,214 assertions: integer identities on `[-64,64]`, all addition pairs in
that interval, all 16 gate entries, and all probability controls at
`epsilon=-1/2,-1/4,0,1/4,1/2`. These are finite receipts; the proofs above
establish the universal algebraic statements. The integrated root audit is the
reproducible receipt for the dossier.

The slope calculation, original source clock, and carry target are inherited.
The Walsh/quadratic/Clifford translations and aligned ordered control clarify
their common algebra. They do not close a new asymptotic density edge.

The remaining exact source obligation is to prove `delta>0` and `B_0` such that
for every integer `B>=B_0`,

\[
\frac1B\sum_{B\le n<2B}
\frac{1-W(n\bmod4,[y_n]_4)}2\ge\delta.
\]

Replacing `[y_n]_4` by an independent random sample would discard the
load-bearing source coupling. A verdict-changing next result must constrain
this particular joint sign for the original four-pole recurrence and zero seed.

Prior-art caution: the original positive BBP moment kernel and its `(1-z)`
factor already occur in `research/2026-11-11/innovation_arithmetic_decoupling/`
under IAD-03. A Beta/Gamma expansion of that kernel should cite the inherited
moment construction and distinguish a new representation from a new estimate.
