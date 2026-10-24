# Source Genesis: Green operator audit, Pell beta envelopes, and their boundary

**Status: PROVED LOCAL, PAPER**, except where a different status is explicit.
These are source-specific derivations new to this research branch, built from
classical analysis. Scholarly priority is not asserted. No new declaration in
this document has Lean authority merely because an upstream related theorem
was kernel checked. **PI NORMALITY PROVED: NO.**

The audited source is PR #252 at
`364962ac0c0e8fb4d06c37468a5d50336d68a9ee`. The independent derivation below
read the repaired source dossier, its code and tests, both the corrected and
historical CYC03 reports, and the source declarations in
`formal/duck_pi/{BaileyCrandall,BBPIntegral,PiSource}.lean`. The original
BBP formula also agrees with Theorem 1 of the
[Bailey--Borwein--Plouffe author-hosted paper](https://www.davidhbailey.com/dhbpapers/digits.pdf).
This is a shared-model mathematical review with a separate derivation and
finite exact implementation, not an independent human or model family.

## 1. Definitions, domains, and the source audit

For integers $n\geq1$, set

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

For $0\leq t\leq1$, define

\[
g(t)=4-2t^3-t^4-t^5=(1-t)H(t),\qquad
H(t)=4+4t+4t^2+2t^3+t^4,
\]

\[
h(t)=\frac{H(t)}{16-t^8},\qquad
T_n=\int_0^1t^{8n}(1-t)h(t)\,dt\quad(n\geq0).
\]

All integrals in the $t$ variable here are ordinary integrals of continuous
functions on a compact interval. The denominators are at least 15. The exact
pole data are

\[
(a_i,\rho_i)=(7/8,1/2),(1/2,-1/4),(3/8,-1/8),(1/4,-1/8).
\]

Direct summation gives $\sum\rho_i=0$ and
$\sum\rho_i a_i=15/64$. These poles are poles of the complex index
variable, not circle states.

**G1, source identity and positivity.** Elementary monomial integration gives

\[
r(n)=\int_0^1t^{8(n-1)}g(t)\,dt>0.
\]

The identity $g(t)=2(1-t^3)+(1-t^4)+(1-t^5)$ proves strict positivity
on $[0,1)$. Tonelli applies to the nonnegative functions

\[
16^{-k}t^{8(n+k-1)}g(t),\quad k\geq1,
\]

and their geometric sum is integrable, since $16-t^8\geq15$.
Consequently

\[
T_n=\sum_{k\geq1}16^{-k}r(n+k),\qquad
16T_n=r(n+1)+T_{n+1}.
\tag{1}
\]

The source identification $16T_0=\pi$ is classical. One direct check is
that the derivative of

\[
2\log(2-t^2)-2\log(t^2-2t+2)+4\arctan(t-1)
\]

is $16g(t)/(16-t^8)$; its endpoint difference is $\pi$.
No digit sample is an input to this argument. The analogous source identity
and recurrence already have declarations in the upstream Lean project;
the current run's compiler receipts, rather than this prose, determine their
current kernel authority.

**G2, Hausdorff structure.** The substitution $u=t^8$ gives

\[
d\mu(u)=w(u)\,du,
\qquad w(u)=\frac{g(u^{1/8})}{8u^{7/8}(16-u)},\qquad
T_n=\int_0^1u^n\,d\mu(u).
\tag{2}
\]

The density is strictly positive on $(0,1)$. Near zero it is
$O(u^{-7/8})$, and near one it is
$(1-u)/64+O((1-u)^2)$; hence it is integrable. For every pair of
integers $n,k\geq0$, finite expansion, requiring no infinite interchange,
proves

\[
(-1)^k\Delta^k T_n=\int_0^1u^n(1-u)^k\,d\mu(u)>0.
\tag{3}
\]

For a nonzero complex polynomial $p(u)=\sum_{j=0}^m c_j u^j$,

\[
\sum_{i,j=0}^m\overline{c_i}c_jT_{i+j}
=\int_0^1|p(u)|^2\,d\mu(u)>0.
\tag{4}
\]

A nonzero polynomial has only finitely many roots, while the density is
positive on an interval. This proves strict positivity of every finite
Hankel matrix, without any finite determinant extrapolation. A realization

\[
T_n=v^*A^nz
\]

with a fixed finite-dimensional matrix $A$ would bound all Hankel ranks
by its dimension and is therefore impossible. This says nothing about
nonlinear realizations or explicitly time-dependent finite descriptions.

**G3, the repaired beta bounds are valid.** On $(0,1)$, $1/4<h(t)<1$.
Also $H(1)=15$, $H'(1)=22$, and

\[
0<1-h(t)=\frac{15-H(t)+1-t^8}{16-t^8}\leq2(1-t).
\]

The last inequality follows by $15-H(t)\leq22(1-t)$,

$1-t^8\leq8(1-t)$, and $16-t^8\geq15$. Thus, for every $n\geq0$,

\[
\frac{B_n}{4}<T_n<B_n,
\qquad 0<B_n-T_n\leq
\frac4{(8n+1)(8n+2)(8n+3)},
\quad B_n=\frac1{(8n+1)(8n+2)}.
\tag{5}
\]

The inequalities prove $n^2T_n\to1/64$. They agree with the independent
pole calculation: the leading forcing term is $15/(64n^2)$, and its
Green sum divides that coefficient by 15. No mathematical error was found
in these repaired analytic claims. Their prior finite tests are checks of
examples; (1)--(5) supply the infinite proofs.

## 2. A source-specific all-order theorem: Pell coefficients and signed errors

**G4, exact rational cancellation.** Polynomial multiplication gives

\[
H(t)(4-4t+2t^3-t^4)=16-t^8,
\qquad
h(t)=\frac1{4-4t+2t^3-t^4}.
\tag{6}
\]

In particular, in a neighborhood of $s=0$,

\[
h(1+s)=\frac1{1-2s-2s^3-s^4}=\sum_{j\geq0}a_js^j.
\tag{7}
\]

Here $a_j=h^{(j)}(1)/j!$, $a_0=1$, $a_j=0$ for negative indices,
and, for every $j\geq1$,

\[
a_j=2a_{j-1}+2a_{j-3}+a_{j-4}.
\tag{8}
\]

Thus all $a_j$ are strictly positive integers. The first values are

\[
1,2,4,10,25,60,144,348,841,2030,4900,11830,28561.
\]

Let the Pell numbers be $P_0=0,P_1=1,P_{m+2}=2P_{m+1}+P_m$. Then

\[
\boxed{a_{2m}=P_{m+1}^2,\qquad
a_{2m+1}=P_{m+1}P_{m+2}.}
\tag{9}
\]

Proof: the proposed sequence has the four initial values in (8). For an
even index $2m\geq4$, put $p=P_m,q=P_{m-1}$; the right side of (8)
becomes $2p(2p+q)+2qp+q^2=(2p+q)^2$. For an odd index $2m+1\geq5$
it becomes $2(2p+q)^2+2p^2+pq=(2p+q)(5p+2q)$. These are exactly the
proposed even and odd values. Recurrence uniqueness proves (9).

**G5, global derivative positivity.** Independently of expansion (7),

\[
h(t)=\frac1{16}H(t)\sum_{\ell\geq0}(t^8/16)^\ell
\tag{10}
\]

has nonnegative power-series coefficients. Its radius of convergence is
at least $\sqrt2>1$; every fixed number of termwise derivatives converges
uniformly on $[0,1]$. It follows that

\[
h^{(j)}(t)\geq0\quad(0\leq t\leq1),
\]

and each derivative is strictly positive on $(0,1]$, because the series
has arbitrarily high nonzero powers. In particular $h^{(j)}$ is strictly
increasing on $(0,1]$.

For positive real $x,y$, write
$\mathrm B(x,y)=\int_0^1t^{x-1}(1-t)^{y-1}\,dt$.
For integers $K,n\geq0$, define the rational approximation

\[
A_K(n)=\sum_{j=0}^{K-1}(-1)^j a_j\mathrm B(8n+1,j+2),\qquad A_0(n)=0,
\tag{11}
\]

where

\[
\mathrm B(8n+1,j+2)=\frac{(j+1)!}{\prod_{\ell=1}^{j+2}(8n+\ell)}.
\]

**G6, signed beta remainder, all (n,K).** Define

\[
E_K(n)=(-1)^K\bigl(T_n-A_K(n)\bigr).
\]

Then, for every $n,K\geq0$,

\[
\boxed{0<E_K(n)<a_K\mathrm B(8n+1,K+2).}
\tag{12}
\]

Moreover $E_K$ is itself a strict Hausdorff moment sequence, and for
each **fixed** $K$,

\[
\frac{E_K(n)}{\mathrm B(8n+1,K+2)}\longrightarrow a_K.
\tag{13}
\]

Proof for $K\geq1$: Taylor's integral remainder on the real segment

$[t,1]$ gives

\[
R_K(t):=(-1)^K\left[h(t)-\sum_{j<K}(-1)^ja_j(1-t)^j\right]
=\frac1{(K-1)!}\int_t^1(v-t)^{K-1}h^{(K)}(v)\,dv.
\tag{14}
\]

It is strictly between zero and $a_K(1-t)^K$ for $0\leq t<1$.
For $K=0$, put $R_0=h$; then $0<R_0(t)<a_0=1$ on $[0,1)$.
Multiplication by $t^{8n}(1-t)$ and integration proves (12).
The representation

\[
E_K(n)=\int_0^1t^{8n}(1-t)R_K(t)\,dt
\tag{15}
\]

proves the strict Hausdorff assertion by the same substitution as in (2).
In particular all $E_K(n)$ are strictly decreasing in $n$. The ratio

$R_K(t)/(1-t)^K$ extends continuously to $t=1$ with value $a_K$.
Normalizing the weight $t^{8n}(1-t)^{K+1}$ to have integral one, its mass
outside every fixed neighborhood of 1 tends to zero. This follows from
an exponentially decaying numerator away from 1 and a denominator of
polynomial size. Boundedness in (12) then proves (13).

For example, $A_1=B_n$, $A_2=B_n-4/\prod_{\ell=1}^3(8n+\ell)$,
and

\[
A_2(n)<T_n<A_3(n)
=A_2(n)+\frac{24}{\prod_{\ell=1}^4(8n+\ell)}.
\tag{16}
\]

These are exact rational brackets for the authentic source. For fixed $K$
they give error $O_K(n^{-K-2})$; the constant is source-derived through
(6)--(9).

**Quantifier guard.** This does not assert convergence as $K\to\infty$
at fixed $n$. The closest pole of $h(1+s)$ is $s=\sqrt2-1$, so its
Taylor radius is less than one. Formula (14) is a finite real Taylor
formula and is valid on the whole interval; it does not require a
convergent infinite Taylor series there. Successive bounds need not improve
indefinitely at a fixed $n$.

## 3. What the hierarchy buys for the actual selected trajectory

Let $y_0=0$, $y_{n+1}=\{16y_n+r(n+1)\}$, and

\[
x_j=\{16^j\pi\}=\{y_{j+1}+T_{j+1}\},\qquad
q_j^{(K)}=y_{j+1}+A_K(j+1).
\]

The numbers $y_n,A_K(n),q_j^{(K)}$ are rational; only their circle
classes are used in the following formulas. We have exactly

\[
x_j=q_j^{(K)}+(-1)^KE_K(j+1)\pmod1.
\tag{17}
\]

Consequently the circle distance is at most the right side of (12), with

$n=j+1$. When $E_K(j+1)\leq1/2$, the distance is exactly

$E_K(j+1)$. This sharpens the original quadratic shadowing to arbitrary
fixed polynomial order using a completely explicit rational correction.
It is quantitative source-selected approximation, not a cancellation
theorem.

**G7, a lag-uniform signed transport with arbitrary polynomial offset decay.**
For integers $h\ne0$, $M\geq0$, $L\geq1$, $d\geq1$, let

\[
C_{h,d}(M,L)=\sum_{j=M}^{M+L-1}
e^{2\pi ih(16^d-1)16^j\pi},
\]

\[
Q_{h,d}^{(K)}(M,L)=\sum_{j=M}^{M+L-1}
e^{2\pi ih(q_{j+d}^{(K)}-q_j^{(K)})}.
\]

Then

\[
\boxed{
|C_{h,d}(M,L)-Q_{h,d}^{(K)}(M,L)|
\leq\frac{\pi|h|a_K}{4}\mathrm B(8M+2,K+1).
}
\tag{18}
\]

The bound is independent of both $d$ and $L$, and is

$O_{h,K}((M+1)^{-K-1})$. The complex characters retain their actual
signs; no prime-factor path is substituted for a signed sum.

Proof: by (17), the difference between the two phase arguments modulo one
is $(-1)^K(E_K(j+d+1)-E_K(j+1))$. The character is $2\pi|h|$-Lipschitz,
and $E_K$ is decreasing. Therefore the difference in sums is at most

\[
2\pi|h|\sum_{j=M}^{M+L-1}
\bigl(E_K(j+1)-E_K(j+d+1)\bigr)
\leq2\pi|h|\sum_{n=M+1}^{\infty}E_K(n).
\]

Using (12), Tonelli, and

$1-t^8=(1-t)\sum_{i=0}^7t^i\geq8t^7(1-t)$, the final sum is bounded by

\[
a_K\int_0^1\frac{t^{8M+8}(1-t)^{K+1}}{1-t^8}\,dt
\leq\frac{a_K}{8}\mathrm B(8M+2,K+1).
\tag{19}
\]

All interchanges have nonnegative integrands, and the last beta integral
is finite including $K=M=0$. Equations (18)--(19) follow.
For $K=0$, this already bounds the error by

$\pi|h|/[4(8M+2)]$, uniformly in lag and horizon. The proof is a
transfer theorem; it does **not** bound $Q_{h,d}^{(K)}$ below its trivial
size $L$. No cancellation of $C$ has thereby been proved.

## 4. The correctly typed forward/backward operators

Let $X=\ell^\infty(\mathbb N_0;\mathbb C)$, let $S:X\to X$ be the
left shift $(Sf)_n=f_{n+1}$, and set $f_n=r(n+1)$. The backward
Green operator is the bounded resolvent

\[
R=(16I-S)^{-1}=\sum_{k\geq0}16^{-k-1}S^k,
\qquad \|R\|=1/15,\qquad T=Rf.
\tag{20}
\]

The operator series converges in norm. The upper norm bound is its
geometric sum; the constant sequence attains equality. The shift has
spectrum the closed unit disk: its norm gives one inclusion, and every

$|\lambda|\leq1$ is an eigenvalue with eigenvector

$(1,\lambda,\lambda^2,\ldots)$. Resolvent spectral mapping gives

\[
\operatorname{spec}(R)
=\left\{\frac1{16-z}:|z|\leq1\right\}
=\left\{w:\left|w-\frac{16}{255}\right|\leq\frac1{255}\right\}.
\tag{21}
\]

The same resolvent formula restricts to $c_0$; its norm is also $1/15$,
by applying it to increasingly long initial blocks of ones. It commutes
with $S$, which is the genuine time-shift covariance $RS=SR$.
Bounded solutions of $16T_n-f_n=T_{n+1}$ are unique: their difference
is $16^n$ times its initial value.

For a spectral source formulation, let

\[
d\nu(u)=(16-u)d\mu(u),\quad
\mathcal H=L^2(\nu),\quad (Uv)(u)=uv(u),\quad
(Jv)_n=\int u^nv(u)\,d\nu(u).
\]

Here $J:\mathcal H\to X$ is bounded by Cauchy--Schwarz,

$JU=SJ$, and

\[
f=J1,\qquad T=J(16I-U)^{-1}1,
\qquad RJ=J(16I-U)^{-1}.
\tag{22}
\]

The self-adjoint multiplication operator $U$ has spectrum $[0,1]$
and no eigenvalues because $\nu$ has a positive nonatomic density.
Every spectral neighborhood of an endpoint has positive measure, so the
endpoints belong to its spectrum even though they carry no atoms. Thus

\[
\operatorname{spec}((16I-U)^{-1})=[1/16,1/15].
\]

For each $v\in\mathcal H$, dominated convergence proves

$U^nv\to0$, while $\|U^n\|=1$ for every $n$. The individual modes

$u^n$, $0<u<1$, contract, but there is no uniform contraction factor
less than one for this full continuum. This distinction prevents falsely
inferring exponential decay from a positive spectral representation.

The forward state space is a different object: the clocked circle with

\[
F_n(y)=\{16y+r(n+1)\},\quad
H_n(y)=\{y+T_n\},\quad E_{16}(x)=\{16x\}.
\]

Equation (1) gives the exact time-dependent conjugacy

\[
H_{n+1}\circ F_n=E_{16}\circ H_n.
\tag{23}
\]

For an arbitrary initial state $s$, its selected circle phase is

$\{s+T_0\}$, and the corrected orbit is

$\{16^n(s+T_0)\}$. Selecting $s=0$ is therefore essential. Selecting

$s=1/3$ gives $y_1=7/15$, not the unforced fixed point $1/3$.

There is no claimed operator taking forcing-index poles to circle states.
The maps in (20)--(23) are explicitly between source sequences, source
spectral functions, and clocked circle states.

**Stability.** For bounded forcing perturbations,

\[
\|\delta T\|_\infty\leq\|\delta f\|_\infty/15.
\]

If $\delta f_k=0$ for $k<M$, then for $n<M$,

\[
|\delta T_n|\leq16^{-(M-n)}\|\delta f\|_\infty/15.
\]

A prescribed terminal error at $M$, with the intervening forcing exact,
propagates backward as $\delta T_n=16^{-(M-n)}\delta T_M$.
Forward lifted initial-state errors instead propagate as $16^n\delta s$.
For initial circle distance $\epsilon$, the forward distance is at most

$\min(1/2,16^n\epsilon)$, with equality $16^n\epsilon$ before the
first wrap when this quantity is at most $1/2$. The resolving power of a
stable tail representation does not automatically control an expanding
phase readout at arbitrarily late times.

## 5. Orthogonal polynomials, determinacy, and the limit of this information

The generating function

\[
F(z)=\sum_{n\geq0}T_nz^n
=\int_0^1\frac{d\mu(u)}{1-zu},\quad |z|<1,
\tag{24}
\]

follows by an integrable geometric majorant. The integral continues
analytically to $\mathbb C\setminus[1,\infty)$, by domination on compact
subsets away from the cut. It is not rational, because rational coefficient
generating functions have finite Hankel rank. The moment problem is
determinate: equality of all moments implies equality on polynomials;
uniform polynomial approximation of continuous functions on $[0,1]$
then implies equality of the finite measures.

For every $m\geq1$, strict positivity (4) gives a unique monic polynomial

$p_m$ orthogonal to $1,u,\ldots,u^{m-1}$. Its $m$ zeros are distinct
and lie in $(0,1)$. To prove this, multiply $p_m$ by the product of its
sign-changing interior factors; if there were fewer than $m$, the
product would have constant nonzero sign except at finitely many points,
contradicting orthogonality against a polynomial of degree less than $m$.

Let these zeros be $\xi_i$, and let $\ell_i$ be their Lagrange basis.
The Gaussian weights are

\[
\omega_i=\int\ell_i\,d\mu=\int\ell_i^2\,d\mu>0.
\]

The equality follows because $\ell_i^2-\ell_i$ is $p_m$ times a
polynomial of degree at most $m-2$. Polynomial division then proves
Gaussian quadrature is exact through degree $2m-1$. This is classical
orthogonal-polynomial geometry applied to the authenticated BBP measure.

For $w>1$, define

\[
q_{m-1}(w)=\int\frac{p_m(w)-p_m(u)}{w-u}\,d\mu(u).
\]

Orthogonality yields the exact Markov/Padé error identity

\[
\int\frac{d\mu(u)}{w-u}-\frac{q_{m-1}(w)}{p_m(w)}
=\frac1{p_m(w)^2}\int\frac{p_m(u)^2}{w-u}\,d\mu(u)>0.
\tag{25}
\]

Indeed, subtracting the two fractions first gives

$p_m(w)^{-1}\int p_m(u)/(w-u)\,d\mu(u)$. The difference between this
and (25) is the integral of $p_m(u)$ times a polynomial of degree

$m-1$, hence zero. For $0<z<1$, multiply (25) at $w=1/z$ by $w$
to obtain a strict lower Padé approximation to (24).

**Specific obstruction, not a universal no-go.** The exact Gaussian weights
already satisfy $\sum_i\omega_i=T_0$, because quadrature is exact on
constants. Also every moment satisfies

\[
T_n=16^nT_0-\sum_{k=1}^n16^{n-k}r(k).
\tag{26}
\]

Consequently computing the exact moment-based coefficients from the
unknown scalar $T_0$, then reading $16\sum\omega_i$ as an independent
evaluation of $\pi$, is circular. A useful arithmetic result would need
independent source-certified approximations to the weights or a new bound
on the phase-selected sums. Formula (25) provides approximation geometry,
but no estimate on those sums is presently derived from it. This does not
rule out a future use of source-specific orthogonal polynomials.

## 6. Hostile controls: even arbitrarily many matching tail terms can fail

**G8, a counterfeit matching the leading coefficient.** The source

\[
T_n^*=\frac1{64(n+1)(n+2)}
=\int_0^1u^n\frac{1-u}{64}\,du
\]

has all strictly positive Hankel matrices and $n^2T_n^*\to1/64$, exactly
the authentic leading coefficient. Its forcing

$r^*(n)=16T_{n-1}^*-T_n^*$ is a positive rational function, its bounded
Green solution is $T^*$, and with $y_0=0$ its selected phase is

$16T_0^*=1/8$. Its next circle iterate is zero and stays zero. This is
a full member of the positivity/rational-forcing/asymptotic-leading-term
class, but not of the fixed four-pole BBP source class.

**G9, arbitrary finite endpoint-jet counterfeit.** Write, near $u=1$,

\[
w(u)=(1-u)k(u),\qquad
k(u)=\frac{h(u^{1/8})}{8u^{7/8}\sum_{i=0}^7u^{i/8}}.
\]

The function $k$ is analytic near 1, all its Taylor coefficients there
are rational, and $k(1)=1/64$. Fix any integer $M\geq0$, and let

$q_M(u)$ be its Taylor polynomial of degree $M$ about 1. Write

$q_M(u)=\sum_{j=0}^M b_j(1-u)^j$, and set

\[
B=\sum_{j=0}^M|b_j|,\qquad
\delta=\min\left(1,\frac{b_0}{2(B+1)}\right),\qquad
C=\frac{B+1}{\delta^{M+1}},\qquad
p(u)=q_M(u)+C(1-u)^{M+1}.
\tag{27}
\]

Every coefficient and constant is rational. On $1-\delta\leq u\leq1$,

$q_M(u)\geq b_0-B\delta\geq b_0/2>0$. On the remaining interval,

$q_M(u)\geq-B$ while the added term is at least $B+1$. Thus $p>0$
on all of $[0,1]$. The measure

\[
d\mu_M^*(u)=(1-u)p(u)\,du
\]

has rational mass and all positive Hankel ranks. Its moments are rational
functions of $n$, and its forcing

\[
r_M^*(n)=\int_0^1u^{n-1}(16-u)(1-u)p(u)\,du>0
\]

is a rational function of $n$. The Green identity holds exactly and the
selected initial phase is rational, so its base-16 orbit is eventually
periodic and is not normal.

Nevertheless

\[
T_{M,n}^*-T_n=O_M(n^{-M-3}).
\tag{28}
\]

To prove (28), the density difference is $O((1-u)^{M+2})$ near 1, whose

$n$-th moment is $O(n^{-M-3})$. Away from a fixed neighborhood of 1,
the integral of its absolute value is finite and its $n$-th moment
decays geometrically. This proves (28), including the original integrable
singularity at zero. Therefore the counterfeit matches any prescribed
finite number of authentic tail asymptotic terms.

For an explicit small example, the authentic expansion begins

\[
k(1+s)=\frac1{64}-\frac{17}{1024}s+
\frac{141}{8192}s^2-\frac{4575}{262144}s^3+O(s^4).
\]

The positive polynomial

\[
p_2(u)=\frac1{64}+\frac{17}{1024}(1-u)+
\frac{141}{8192}(1-u)^2
\]

already needs no added stabilizing term. Its mass is

$1735/98304$, its selected phase is $1735/6144$, and its tail differs
from the authentic tail by $O(n^{-5})$. After exactly three base-16
shifts, its selected phase is fixed at $2/3$; every positive-lag character
is then 1. This is an exact eventual-resonance control.

**Class-membership guard.** These rational-moment counterfeits are rational
coboundaries, because $T_{M,n}^*$ is itself rational in $n$. They do not
refute a conjecture whose premises additionally demand a nonzero rational
pole-coboundary invariant. They also do not retain the exact BBP pole
positions and residues. Their theorem is precisely that strict moment
positivity, rational forcing, and any fixed finite asymptotic jet are
insufficient together. The distinct positive families

$K!/[n(n+1)\cdots(n+K)]$, already audited in PR #252, show that
non-coboundary invariants alone do not force a particular tail decay power;
they are not being declared nonnormal here.

The subsequent [non-coboundary counterfeit theorem](PI_SOURCE_GENESIS_NONCOBOUNDARY.md)
goes further: one explicit positive rational source can retain a nonzero
rational-coboundary invariant, match arbitrarily many prescribed authentic
tail terms, and still select a rational periodic phase. Its full source
membership and additional pole class are proved there.

## 7. Geometric circle moments: an exact bridge with an explicit missing bound

For a circle phase $x$, put

$D(x)=|1-e^{2\pi ix}|^2=2-2\cos(2\pi x)$. The universal Chebyshev
identity is

\[
D(mx)=2-2T_m^{\rm Cheb}(1-D(x)/2).
\tag{29}
\]

It applies to the selected $\pi$ orbit and to every counterfeit. For
every integer $k\geq1$, $D(x)^k$ is $\pi k4^k$-Lipschitz: differentiate

$D^k$, use $|D'|\leq4\pi$, and $0\leq D\leq4$. Equations
(17),(19) therefore give the explicit selected-orbit estimate

\[
\left|\frac1L\sum_{j=M}^{M+L-1}
\bigl(D(16^j\pi)^k-D(q_j^{(K)})^k\bigr)\right|
\leq\frac{\pi k4^k a_K}{8L}\mathrm B(8M+2,K+1).
\tag{30}
\]

On Haar measure, the constant Laurent coefficient of

$(2-z-z^{-1})^k=(1-z)^k(1-z^{-1})^k$ is

$\sum_{j=0}^k\binom{k}{j}^2=\binom{2k}{k}$, proving the stated target
Haar moments. This is classical finite algebra. It places the rational
source-corrected orbit and the geometric moments on one quantitative
scale, but (30) does not show that either temporal average tends to its
Haar value. The unforced fixed circle phase $1/3$ has $D=3$ forever,
already disagreeing with the Haar first moment 2; its source type is
unforced. The positive rational Green counterfeit in G8 has $D=0$
eventually and meets the declared broader source class. Kummer carry
identities or Wallis reconstruction of $\pi$ do not remove this missing
temporal estimate by themselves.

## 8. Proof-status and falsification ledger

| Claim | Status and source requirements | Boundary / next falsification |
|---|---|---|
| G1--G3: BBP integral, Hausdorff positivity, beta audit | Classical tools; source-specific proof checked above | Does not address digit frequencies; mutate a residue to test source dependence |
| G4--G6: Pell endpoint coefficients, all-order signed beta errors | PROVED LOCAL, PAPER; exact $H/(16-t^8)$ | Not an infinite-in-$K$ convergent expansion at fixed $n$ |
| G7: lag-uniform transport (18) at every horizon | PROVED LOCAL, PAPER; actual source state and complete monotonicity of its residual | Still needs a nontrivial signed bound on the explicit rational-phase sum $Q$ |
| (20)--(23): typed resolvent and cocycle | Classical operator theory with source instantiation | No map sends forcing-index poles to digit-circle states |
| (24)--(25): determinacy, orthogonal polynomials, Padé sign | Classical; follows from authenticated positive measure | Exact quadrature weights already contain the source mass |
| G8--G9: finite-asymptotic-data normality implication | REFUTED in the explicitly stated rational-forcing class | Counterfeits do not preserve BBP fixed poles or non-coboundary invariant |
| (30): geometric selected-orbit transport | PROVED LOCAL, PAPER | Haar target values still require a temporal source theorem |
| Normality or $o(L)$ signed cancellation | UNPROVED | An independent sublinear estimate for $Q_{h,d}^{(K)}$ would change this |

The direct source contact is the authenticated rational kernel and boundary
integral (κ). The statements above survive exact algebra and written proof
checks (φ), with explicit class restrictions on countermodels (σ). Enthusiasm
for the target supplies no additional evidence (ρ). The available probes
include exact signed beta arithmetic and source-preserving complex-character
transport; the missing probe is an all-horizon arithmetic cancellation bound
on those rational-phase sums. No probabilistic or quantum interpretation of
their Fourier phases is used.

An independent inline Fraction oracle, using direct four-fraction forcing
and 40-term geometric tail enclosures rather than importing the source
module, checked (12) at $n=0,1,2,7,31$, $K=0,\ldots,7$: **40 exact
finite checks passed**. Separate symbolic reduction produced (6),(7) and
the displayed endpoint coefficients. These finite receipts corroborate the
implementation; the quantified proofs above establish the theorems. The
parent integration supplies durable executable probes and their run receipts.

The smallest change of verdict sought here is a genuinely source-derived
sublinear estimate for one nonzero-frequency signed rational-phase family
in (18), with its quantifiers stated on an unbounded horizon. The all-order
tail corrections make the transport error explicit and harmless; they do
not prove that estimate or replace it with an equivalent normality claim.
