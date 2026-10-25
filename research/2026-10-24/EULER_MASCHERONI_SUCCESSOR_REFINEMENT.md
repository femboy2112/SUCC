# Euler–Mascheroni successor refinement

## Status, scope, and source

**Paper proofs; exact finite implementation; no RH or π-normality theorem.**

This note turns the proposed identity

$$
\gamma=\lim_{r\downarrow1}\sum_{k\ge1}\left(k^{-r}-r^{-k}\right)
$$

into explicit finite successor operations, boundary corrections, and integer
dilation laws. The analytic ingredients are classical: Euler summation,
Hurwitz zeta, digamma reflection, and positive Laplace transforms. The SUCC
contribution is their assembly into a finite source interface with exact
coherence, error budgets, and adversarial controls. Scholarly novelty is not
claimed.

The original integer source is retained throughout the proved constructions.
The positive counterfeits in §8 are deliberately changed sources. They test
which observations fail to identify the original source; they are never
substituted into a claim about ζ or π.

Implementation:

- [`euler_mascheroni_succ.py`](../../observational_succ/euler_mascheroni_succ.py)
- [`test_euler_mascheroni_succ.py`](../../tests/test_euler_mascheroni_succ.py)

The finite tests verify their stated finite domains. Infinite identities,
convergence, and positivity below have paper-proof authority, not Lean or
proof-by-enumeration authority. Full-suite and hosted-CI status belong to the
separate validation receipt.

## 1. The regularized function behind the proposed limit

For real $r>1$, both sums converge absolutely and

$$
\sum_{k=1}^{\infty}r^{-k}=\frac1{r-1}.
$$

Consequently the expression in the question is exactly

$$
G(r)=\zeta(r)-\frac1{r-1}.
$$

The removable value is $G(1)=\gamma$. The usual analytic continuation of ζ
has no other pole, so $G$ extends to an entire function. These are classical
facts; see [DLMF §25.2](https://dlmf.nist.gov/25.2), especially its Laurent
expansion. The positive integral representation in §6 is used only on
$\Re s>0$; entire continuation does not extend that positivity argument to
arbitrary complex parameters.

The useful object is the function and its source construction, including
rational-offset versions, rather than only its scalar value at $1$.

## 2. Equal cutoffs can converge to γ − 1

For $r>1$ and integer $N\ge1$, define

$$
T_N(r)=\sum_{k=1}^N k^{-r}-\sum_{k=1}^N r^{-k},
\qquad
B_N(r)=\sum_{k=1}^N k^{-r}-\int_1^N x^{-r}\,dx.
$$

Write $H_N=\sum_{k=1}^N1/k$ for the ordinary harmonic number.

### Proposition 2.1 — Exact two-clock boundary correction

For every such $r,N$,

$$
\boxed{
B_N(r)=T_N(r)+\frac{N^{1-r}-r^{-N}}{r-1}.
}
\tag{2.1}
$$

**Proof.** The finite geometric sum is $(1-r^{-N})/(r-1)$, and
$\int_1^N x^{-r}\,dx=(1-N^{1-r})/(r-1)$. Subtract the two expressions. ∎

Both boundaries matter. Their combined removable value at $r=1$ is

$$
\lim_{r\to1}\frac{N^{1-r}-r^{-N}}{r-1}=N-\log N.
$$

Thus the raw finite expression tends to $H_N-N$, while the compensated one
tends to $H_N-\log N$. Dropping the correction does not preserve the finite
source observable.

### Proposition 2.2 — Uniform compensated remainder

For $\sigma=\Re s>0$, including the removable value at $s=1$,

$$
B_N(s)-G(s)
=s\int_N^\infty\{x\}x^{-s-1}\,dx,
\qquad
|B_N(s)-G(s)|\le\frac{|s|}{\sigma}N^{-\sigma}.
\tag{2.2}
$$

For positive real $s$ the remainder is strictly between $0$ and $N^{-s}$.
In particular, the bound is at most $1/N$ for every real $s\ge1$.

**Proof.** The first Euler summation formula is

$$
\zeta(s)=\sum_{k=1}^N k^{-s}+\frac{N^{1-s}}{s-1}
-s\int_N^\infty\{x\}x^{-s-1}\,dx.
$$

Subtract $1/(s-1)$ and use the definition of $B_N$. The integral is
absolutely and locally uniformly convergent when $\Re s>0$, because
$0\le\{x\}<1$. Its modulus is bounded by
$|s|\int_N^\infty x^{-\sigma-1}\,dx$. For real positive $s$, the
fractional part is strictly between its extremal bounds on sets of positive
measure, giving the strict inequalities. Continuity at $s=1$ follows from
the same domination. ∎

This is the classical Euler-summation representation recorded in
[DLMF 25.2.8](https://dlmf.nist.gov/25.2.E8). It also verifies the claimed
removable value constructively: first keep $N$ fixed while $r\downarrow1$,
then let $N\to\infty$, using the uniform $1/N$ error and
$H_N-\log N\to\gamma$.

### Proposition 2.3 — A concrete wrong cofinal limit

For integers $m\to\infty$,

$$
\boxed{T_{m^m}(1+1/m)\longrightarrow\gamma-1.}
\tag{2.3}
$$

**Proof.** Put $r=1+\epsilon$. Equations (2.1)–(2.2) give

$$
T_N(1+\epsilon)-G(1+\epsilon)
=-\frac{N^{-\epsilon}}{\epsilon}
 +\frac{(1+\epsilon)^{-N}}{\epsilon}+R_N,
\quad 0<R_N<N^{-1-\epsilon}.
\tag{2.4}
$$

At $\epsilon=1/m$ and $N=m^m$, the first term equals $-1$ exactly. The
last term is smaller than $m^{-(m+1)}$. Since
$\log(1+1/m)\ge1/(m+1)$, the geometric term is at most

$$
m\exp\left(-\frac{m^m}{m+1}\right)\longrightarrow0.
$$

Finally $G(1+1/m)\to\gamma$. ∎

More generally, if $\epsilon\downarrow0$, $N=N(\epsilon)$ is integral, and

$$
\epsilon\log N-\log(1/\epsilon)\longrightarrow c\in\mathbb R,
$$

then (2.4) gives $T_N(1+\epsilon)\to\gamma-e^{-c}$. The geometric
remainder vanishes because this hypothesis forces $N$ to grow much faster
than $1/\epsilon$; the compensated remainder vanishes by (2.2). If the
displayed expression instead tends to $+\infty$, the raw construction
converges to γ. These are stated sufficient schedules, not a classification
of every possible cutoff path.

**What this proves:** even two cutoffs tending to their desired boundaries
can produce a false constant when their relationship is uncontrolled. The
compensated construction supplies a uniform finite error. This proposition
concerns the two sums in the question; finite-prime Euler products require
their own tail analysis.

## 3. Certified gamma and Hurwitz boundary intervals

### Proposition 3.1 — The sharper gamma remainder used by the code

For every integer $N\ge1$,

$$
\frac1{2(N+1)}<H_N-\log N-\gamma<\frac1{2N}.
\tag{3.1}
$$

**Proof.** Telescope the finite differences of $H_N-\log N$ to obtain

$$
E_N:=H_N-\log N-\gamma
=\sum_{k=N}^{\infty}
\left(\log(1+1/k)-\frac1{k+1}\right).
$$

For $f(x)=1/x$, strict convexity gives the trapezoid bound

$$
\int_k^{k+1}f(x)\,dx
<\frac12\left(\frac1k+\frac1{k+1}\right).
$$

Hence each summand is smaller than
$1/[2k(k+1)]$, whose sum is $1/(2N)$.

For the lower bound, the tangent line at $k+1$ gives

$$
\frac1x\ge\frac1{k+1}+\frac{k+1-x}{(k+1)^2}
\quad(k\le x\le k+1).
$$

After integration and subtraction of $1/(k+1)$, the summand is at least
$1/[2(k+1)^2]$, which is strictly larger than
$1/[2(k+1)(k+2)]$. The latter series telescopes to $1/[2(N+1)]$. ∎

If $\ell_N\le\log N\le u_N$ are rational bounds, (3.1) gives a rational
certificate

$$
H_N-u_N-\frac1{2N}
<\gamma<
H_N-\ell_N-\frac1{2(N+1)}.
$$

The logarithm routine uses binary scaling and

$$
\log x=2\sum_{j=0}^{L-1}\frac{z^{2j+1}}{2j+1}+R_L,
\quad z=\frac{x-1}{x+1},
\quad
0\le R_L\le\frac{2z^{2L+1}}{(2L+1)(1-z^2)}
$$

for $1\le x\le2$, so $0\le z\le1/3$. The tail bound follows by replacing
all remaining denominators by $2L+1$ and summing the resulting geometric
series. Arguments below one are handled by $\log(1/x)=-\log x$. Every
certificate endpoint is a `Fraction`; no floating value is promoted to an
outward interval.

### Proposition 3.2 — Rational-offset differences without a gamma input

For $a,b>0$,

$$
G(1,a)-G(1,b)
=\sum_{n=0}^{\infty}
\left(\frac1{n+a}-\frac1{n+b}\right).
\tag{3.2}
$$

Let $d_N=(N+a)^{-1}-(N+b)^{-1}$. The tail after the first $N$ terms lies
between the two endpoints

$$
\log\frac{N+b}{N+a},
\qquad
\log\frac{N+b}{N+a}+d_N.
\tag{3.3}
$$

**Proof.** The coefficient difference is $O(n^{-2})$, so the series is
absolutely convergent. Its limit follows by subtracting the finite Hurwitz
constructions in §4. If $b>a$, the difference is positive and decreasing;
the ordinary integral comparison brackets its tail between its integral
and its first term plus that integral. The integral is the logarithm in
(3.3). If $b<a$, apply the same proof to the negative difference and reverse
the endpoints; if $a=b$, every term is zero. ∎

For rational offsets, the prefix and $d_N$ are rational, and the preceding
logarithm bounds make (3.3) an executable certificate. Taking $b=1$ and
adding (3.1) encloses $G(1,a)$ itself.

## 4. Exact finite successor and FUCC refinement

Fix $a>0$. Define

$$
G(s,a)=\zeta(s,a)-\frac1{s-1},
\qquad
B_N(s,a)=\sum_{n=0}^{N-1}(n+a)^{-s}-I_N(s),
\quad I_N(s)=\int_1^N x^{-s}\,dx.
$$

**The upper endpoint of $I_N$ is $N$, not $N+a$.** This choice matters for
the exact finite refinement law below. At $s=1$, $I_N(1)=\log N$ and
$G(1,a)=-\psi(a)$. The Hurwitz source and its classical recurrence are
recorded in [DLMF §25.11](https://dlmf.nist.gov/25.11); the digamma series
and identities appear in [§5.7](https://dlmf.nist.gov/5.7) and
[§5.5](https://dlmf.nist.gov/5.5).

### Convergence and domain

For every fixed $a>0$, $B_N(s,a)\to G(s,a)$ locally uniformly on
$\Re s>0$. To verify this directly, subtract the $a=1$ construction. The
resulting coefficient differences have locally uniform size
$O(|s||a-1|n^{-\sigma-1})$ for $n\ge1$. More explicitly, for $N\ge1$,

$$
|B_N(s,a)-G(s,a)|
\le\frac{|s|}{\sigma}N^{-\sigma}
 +|s||a-1|\left(N^{-\sigma-1}+\frac{N^{-\sigma}}{\sigma}\right),
\quad \sigma=\Re s>0.
\tag{4.1}
$$

Indeed the shifted tail difference is bounded by integrating the derivative
of $u^{-s}$ between $n+a$ and $n+1$, whose smaller endpoint is at least
$n$; summing $n^{-\sigma-1}$ gives (4.1). The absolutely convergent
difference agrees with the Hurwitz series for $\Re s>1$, then throughout
the right half-plane by analytic continuation.

### Proposition 4.1 — Successor with its endpoint retained

For $N\ge1$,

$$
B_N(s,a+1)-B_N(s,a)=(N+a)^{-s}-a^{-s}.
\tag{4.2}
$$

**Proof.** All common terms of the two finite shifted sums cancel, and the
continuum terms are identical. ∎

Taking the limit gives $G(s,a+1)=G(s,a)-a^{-s}$. At finite $N$, discarding
$(N+a)^{-s}$ is a false mutation detected by the exact tests.

### Proposition 4.2 — Exact normalized integer refinement

For every integer $p\ge1$, $N\ge1$, and $a>0$,

$$
\boxed{
\frac1p\sum_{j=0}^{p-1}B_N\left(s,\frac{a+j}{p}\right)
=p^{s-1}B_{pN}(s,a)+D_p(s),
}
\tag{4.3}
$$

where

$$
D_p(s)=\frac{p^{s-1}-1}{s-1}
=\int_0^{\log p}e^{(s-1)t}\,dt,
\qquad D_p(1)=\log p.
\tag{4.4}
$$

**Proof.** The finite reindexing $m=pn+j$ gives

$$
\sum_{j=0}^{p-1}\sum_{n=0}^{N-1}
\left(n+\frac{a+j}{p}\right)^{-s}
=p^s\sum_{m=0}^{pN-1}(m+a)^{-s}.
$$

The normalized continuum discrepancy is

$$
p^{s-1}I_{pN}(s)-I_N(s)
=\frac{p^{s-1}-1}{s-1}.
$$

Subtract the shared counterterms to obtain (4.3). The exponential integral
in (4.4) proves removability at $s=1$. All finite expressions are entire in
$s$, so the finite law itself has no right-half-plane restriction; that
restriction enters only when identifying its infinite boundary. ∎

### Proposition 4.3 — The boundary anomaly is coherent under multiplication

Let

$$
A_p(s):x\longmapsto p^{s-1}x+D_p(s).
$$

Then for all positive integer $p,q$,

$$
A_p(s)\circ A_q(s)=A_{pq}(s)=A_q(s)\circ A_p(s),
\qquad D_{pq}(s)=D_p(s)+p^{s-1}D_q(s).
\tag{4.5}
$$

**Proof.** Multiplying the scales gives $(pq)^{s-1}$. Adding the two
affine offsets gives

$$
\frac{p^{s-1}-1+p^{s-1}(q^{s-1}-1)}{s-1}
=\frac{(pq)^{s-1}-1}{s-1}.
$$

The same equality at $s=1$ is $\log(pq)=\log p+\log q$. ∎

At the seam, FUCC refinement therefore acts by literal translation through
$\log p$. The law holds for composite multipliers as well as primes;
composite multipliers are not independent prime Euler factors.

Differentiating the limiting version of (4.3) gives the full jet law:

$$
\frac1p\sum_{k=0}^{p-1}\partial_s^jG\left(1,\frac{a+k}{p}\right)
=\sum_{\ell=0}^j {j\choose\ell}(\log p)^{j-\ell}
  \partial_s^\ell G(1,a)
 +\frac{(\log p)^{j+1}}{j+1}.
\tag{4.6}
$$

This follows from the product rule and differentiation of (4.4); local
uniform convergence permits the boundary differentiation. These are
classical generalized Stieltjes multiplication identities expressed as an
explicit coherent finite-source interface.

## 5. Reflection reaches π; the common gamma term cancels

The classical digamma reflection relation

$$
\psi(1-a)-\psi(a)=\pi\cot(\pi a)
$$

implies, for $0<a<1$,

$$
G(1,a)-G(1,1-a)=\pi\cot(\pi a).
$$

In particular,

$$
\boxed{G(1,1/4)-G(1,3/4)=\pi.}
\tag{5.1}
$$

See [DLMF 5.5.4](https://dlmf.nist.gov/5.5.E4). Equation (3.2) supplies
the direct successor representation: (5.1) is the grouped Leibniz series.
The code encloses it by (3.3) and compares that enclosure with an independent
rational Machin arctangent bracket.

**The source distinction matters.** Each offset boundary contains the same
gamma normalization, which cancels from their difference. The identity
shows that the rational-offset family contains π; it does not show that
knowing the scalar γ determines π or its digit statistics.

### The geometric member of the family contains the original BBP formula

For $|z|<1$ and $a>0$, define the classical Lerch series

$$
\Phi(z,s,a)=\sum_{n=0}^{\infty}\frac{z^n}{(n+a)^s}.
$$

Absolute convergence allows exact residue subdivision:

$$
\Phi(z,s,a)=p^{-s}\sum_{j=0}^{p-1}z^j
\Phi\left(z^p,s,\frac{a+j}{p}\right).
\tag{5.2}
$$

This follows immediately by writing the original index as $pn+j$. For
real $z\uparrow1$,

$$
\Phi(z,1,a)+\log(1-z)\longrightarrow G(1,a)-\gamma.
\tag{5.3}
$$

To prove (5.3), subtract
$\Phi(z,1,1)=-\log(1-z)/z$. The remaining coefficient difference is
absolutely summable by (3.2), while
$(1-1/z)\log(1-z)\to0$. The Lerch source is described in
[DLMF §25.14](https://dlmf.nist.gov/25.14).

The authentic four-pole BBP formula is

$$
\pi=\frac18\left[
4\Phi(1/16,1,1/8)-2\Phi(1/16,1,1/2)
-\Phi(1/16,1,5/8)-\Phi(1/16,1,3/4)
\right].
\tag{5.4}
$$

This is an exact re-expression of the unchanged BBP offsets and signs.
The source identity is Theorem 1 of Bailey, Borwein, and Plouffe,
[*On the Rapid Computation of Various Polylogarithmic Constants*](https://www.davidhbailey.com/dhbpapers/digits.pdf),
*Mathematics of Computation* 66 (1997), 903–913.
The weights sum to zero, cancelling the common singular normalization at
the $z=1$ boundary too. **Changing $z$ from $1/16$ to $1$ changes the
observable.** The value at $z=1$ cannot be called π on the strength of
(5.4). The common family does not supply the unproved cancellation of the
selected lacunary orbit.

## 6. A positive sawtooth Mellin kernel

Let $w(x)=1-\{x\}$; values at integer endpoints do not affect its integrals.

### Proposition 6.1 — The positive transform

For $\Re s>0$,

$$
\boxed{
F(s):=\frac{G(s)}s
=\int_1^\infty w(x)x^{-s-1}\,dx
=\int_0^\infty w(e^y)e^{-sy}\,dy.
}
\tag{6.1}
$$

**Proof.** On the successor cell $[n,n+1]$, the fundamental theorem of
calculus and interchange over a bounded triangular region give

$$
n^{-s}-\int_n^{n+1}x^{-s}\,dx
=s\int_n^{n+1}(n+1-x)x^{-s-1}\,dx.
$$

The sum of the right side is absolutely and locally uniformly convergent
on $\Re s>0$. For $\Re s>1$, the left side sums to
$\zeta(s)-1/(s-1)$. Analytic continuation proves the identity on the stated
half-plane. Substitute $x=e^y$ for the second representation. ∎

This is a rearrangement of the classical fractional-part Euler-summation
representation, not a positivity assumption.

### Consequences and finite tail bounds

For real $s>0$,

$$
(-1)^jF^{(j)}(s)
=\int_0^\infty y^j w(e^y)e^{-sy}\,dy\ge0.
$$

Thus $F$ is completely monotone. For any finite complex parameters with
$\Re z_i>0$, the matrix $[F(z_i+\overline{z_j})]$ is PSD, because its
quadratic form is an integral of the modulus squared of a finite
exponential sum against the positive measure $w(e^y)\,dy$.

Define the finite kernel by integrating only $1\le x\le N+1$:

$$
F_N(s)=\frac1s\sum_{n=1}^N
\left(n^{-s}-\int_n^{n+1}x^{-s}\,dx\right).
$$

It is itself a positive Gram kernel, and for real $s>0$,

$$
0\le F(s)-F_N(s)\le\frac{(N+1)^{-s}}s.
\tag{6.2}
$$

At integer exponents $s\ge2$, all finite cell integrals and the Gram entries
are rational. The code compares these with an independently integrated
cell formula; exact determinants, quadratic forms, repeated-exponent null
directions, and an off-diagonal negative mutation calibrate the verifier.

Every fixed logarithmic derivative has an explicit tail as well. If
$L=\log(N+1)$ and $\sigma>0$, then

$$
\int_L^\infty y^j e^{-\sigma y}\,dy
=(N+1)^{-\sigma}
\sum_{\ell=0}^j
\frac{j!}{(j-\ell)!}\frac{L^{j-\ell}}{\sigma^{\ell+1}}.
\tag{6.3}
$$

Repeated integration by parts proves (6.3), and $0\le w\le1$ makes it an
upper bound on the discarded log moment.

**RH boundary:** this is an unconditional positive Mellin/Laplace kernel.
It has not been identified with the authentic completed signed Weil form.
Its positivity does not supply that missing identification or RH.

## 7. The infinite Stieltjes moment hierarchy determines its measure

Use the standard convention

$$
G(1+z)=\sum_{k=0}^{\infty}\frac{(-1)^k\gamma_k}{k!}z^k,
\qquad \gamma_0=\gamma,
$$

and define the finite positive measure with density

$$
v(y)=w(e^y)e^{-y},\qquad y\ge0.
$$

### Proposition 7.1 — Exact moments and determinacy

Its moments are

$$
\boxed{
m_j:=\int_0^\infty y^jv(y)\,dy
=j!\sum_{k=0}^j\frac{\gamma_k}{k!},
\qquad 0<m_j\le j!.
}
\tag{7.1}
$$

The full infinite sequence $(m_j)_{j\ge0}$ determines this measure uniquely
among positive Borel measures on $[0,\infty)$ with those moments.

**Proof of the formula.** Equation (6.1) gives

$$
F(1+z)=\int_0^\infty v(y)e^{-zy}\,dy.
$$

On $|z|<1$, multiply the Taylor expansion of $G(1+z)$ by that of
$1/(1+z)$ and compare coefficients with this integral. Differentiation is
dominated by an integrable exponential on every smaller disk. This proves
the moment formula. Since $0\le v(y)\le e^{-y}$, its moment is at most
$\int_0^\infty y^je^{-y}\,dy=j!$, and positivity is strict. ∎

**Proof of determinacy.** Suppose a positive measure $\nu$ has the same
moments. Its total mass is $m_0<\infty$. For $0\le t<1$, monotone
convergence gives

$$
\int e^{ty}\,d\nu(y)
=\sum_{j=0}^{\infty}\frac{t^jm_j}{j!}
\le\frac1{1-t}.
$$

Therefore its transform $\int e^{-(s-1)y}\,d\nu(y)$ is holomorphic on
$\Re s>0$. Its derivatives at $1$ agree with those of $F$, so the identity
theorem identifies the transforms throughout that half-plane. In particular
the Laplace transforms agree at every nonnegative integer.

Push both measures forward by $x=e^{-y}$ and regard them as finite measures
on $[0,1]$ with zero mass at $0$. Equality of the integer Laplace values
gives equality of every polynomial integral in $x$. Polynomials are uniformly
dense in continuous functions on $[0,1]$, so the two finite measures agree;
the original measures agree under the inverse map. ∎

All moment Hankel matrices $[m_{i+j}]$ are consequently PSD. This statement
and determinacy use the **entire infinite sequence**. They do not imply
that any fixed finite list of jets identifies the source.

## 8. Positive counterfeits preserve any fixed finite list of jets

Fix an arbitrary integer $M\ge0$. Let $P_{M+1}$ be the Legendre polynomial
and put

$$
v_\pm(y)=v(y)\pm\frac14
P_{M+1}(8y-1)\mathbf1_{[0,1/4]}(y).
\tag{8.1}
$$

### Proposition 8.1 — Finite-jet nonidentification

Both densities in (8.1) are positive, their moments agree with those of
$v$ through order $M$, and their moments of order $M+1$ differ. Therefore
their corresponding regularized transforms have the same γ and first
$M$ derivatives at $1$, while they are different analytic source families.

**Proof of positivity.** On $0\le y\le1/4$, we have $1\le e^y<2$ and
$v(y)=2e^{-y}-1>1/2$. Indeed
$e^{1/4}<\sum_{j\ge0}(1/4)^j=4/3$. Also
$|P_m(x)|\le1$ for $-1\le x\le1$. For completeness this bound follows
from the classical Laplace integral representation

$$
P_m(\cos\theta)=\frac1\pi\int_0^\pi
\bigl(\cos\theta+i\sin\theta\cos\phi\bigr)^m\,d\phi:
$$

the modulus of the integrand is at most one. See
[DLMF 18.10.4](https://dlmf.nist.gov/18.10.E4), specialized at $\alpha=0$.
Thus the perturbation has magnitude at most $1/4$, and
the modified density stays positive. Outside that interval it is unchanged.

**Proof of the moment claims.** Put $m=M+1$ and $L=1/4$. The shifted
Rodrigues identity is

$$
P_m(2t-1)=\frac1{m!}\frac{d^m}{dt^m}\left[t^m(t-1)^m\right].
$$

Integrating $t^j$ against this expression and integrating by parts $m$
times gives zero for $j<m$. All boundary terms vanish because the bracketed
polynomial has zeros of order $m$ at both endpoints. For $j=m$, the result
is

$$
\int_0^1 t^mP_m(2t-1)\,dt
=\int_0^1 t^m(1-t)^m\,dt
=\frac{(m!)^2}{(2m+1)!}>0.
$$

Rescaling $y=Lt$ proves

$$
\int_0^{1/4}y^jP_{M+1}(8y-1)\,dy=0\quad(0\le j\le M),
$$

with a strictly positive value at $j=M+1$. If
$F_\pm(s)=\int v_\pm(y)e^{-(s-1)y}\,dy$ and $G_\pm(s)=sF_\pm(s)$,
the product rule shows that their derivatives through order $M$ at $1$
are unchanged, and their derivative of order $M+1$ changes. ∎

The perturbing polynomial has exact rational coefficients:

$$
P_m(8y-1)=\sum_{k=0}^m
(-1)^{m-k}{m\choose k}{m+k\choose k}4^k y^k.
$$

This supplies an executable all-order constructor. The tests verify the
finite cases they enumerate and reject a deliberately altered coefficient;
the Rodrigues argument proves the statement for every order.

For $M=0$, the perturbation polynomial is $8y-1$. Its total mass is zero,
and its first moment, including amplitude $1/4$, is exactly $1/384$.
The scalar γ is therefore preserved while the next Stieltjes coefficient
changes.

These positive families **change the integer-floor source law**. Their
purpose is to refute source identification from any fixed finite list of
jets or from generic positive-kernel structure alone. They do not satisfy
all authentic Hurwitz refinement and BBP source obligations merely because
their low-order observations agree.

## 9. What has advanced, and the unproved bridges

The finite construction now has:

- an explicit false diagonal limit and a uniform repair;
- certified γ and rational-offset boundary intervals;
- exact successor endpoints and an integer-refinement affine cocycle;
- a genuine rational-offset π identity and the unchanged Lerch–BBP member;
- a positive kernel with rational finite Gram matrices and explicit tails;
- an infinite determinate moment hierarchy and exact finite-jet counterfeits.

These results organize classical analytic machinery into auditable SUCC
operations. They do not establish the source-selected signed Fourier bounds
needed for π normality. They also do not identify the positive kernel in
§6 with the completed signed Weil form needed by the RH program.

The next useful dependency cut is to transport an actual signed BBP
observable through (4.3) while retaining its selected orbit and all
boundary costs, then prove a quantitative cancellation that fails for the
existing countercontrols. A claim based only on γ, a fixed finite list of
jets, or generic positivity is rejected by §8.

## References and reproducibility

Classical primary reference pages used for this note:

- [NIST DLMF §25.2: Riemann zeta definitions, Laurent expansion, Euler summation](https://dlmf.nist.gov/25.2)
- [NIST DLMF §25.11: Hurwitz zeta](https://dlmf.nist.gov/25.11)
- [NIST DLMF §5.5: digamma recurrence, reflection, and multiplication](https://dlmf.nist.gov/5.5)
- [NIST DLMF §5.7: gamma and digamma series](https://dlmf.nist.gov/5.7)
- [NIST DLMF §25.14: Lerch transcendent](https://dlmf.nist.gov/25.14)
- [NIST DLMF §18.10: classical orthogonal-polynomial integral representations](https://dlmf.nist.gov/18.10)
- [Bailey, Borwein, and Plouffe (1997): the original four-pole BBP identity](https://www.davidhbailey.com/dhbpapers/digits.pdf)

Focused execution performed during this construction:

```sh
python -m unittest tests.test_euler_mascheroni_succ -v
```

**18 test methods passed:** seventeen exact arithmetic, interval, and hostile
control methods, plus one optional high-precision special-function
calibration method. This is an implementation receipt, not an infinite
proof certificate. The independent Machin and piecewise-integral oracles
can fail differently from the production formulas; the mathematical
derivations remain explicit above.
