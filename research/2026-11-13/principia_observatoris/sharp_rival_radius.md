# Exact uniform separation from a stationary rival

Fix integers $N\ge1$ and $d\ge1$. Write $m_k=r(N+k)$ for the authentic
four-pole BBP forcing in [Book VI, PA-01](../../../docs/principia_observatoris/06_succ_applications.md).
Its moment measure $\nu_N$ has positive density throughout $(0,1)$, satisfies
$m_k=\int u^k d\nu_N(u)$, and gives rational moments. The recurrence for the
original BBP orbit retains its prescribed zero seed. The theorem here concerns
a finite window of the forcing, a specified component of that recurrence.

A rival is any scalar sequence $s_k=CA^k b$ with one constant complex matrix
of dimension at most $d$, for all $k\ge0$. Let $H=(m_{i+j})_{i,j=0}^d$,
$v_i=(-1)^i$ for $0\le i\le d$, and $S=\operatorname{diag}(v)$.

**PA-07 (exact uniform radius, attainment and uniqueness).** The distance in
maximum absolute readout error to the whole rival class is
$$
 \min_s\max_{0\le k\le 2d}|m_k-s_k|
 = t_{N,d}:=\frac1{v^T H^{-1}v}>0.
$$
The unique optimal prefix is $s_k=m_k-t_{N,d}(-1)^k$ for $0\le k\le2d$.
It has a unique scalar continuation in this rival class. That continuation
has both a rational companion realization and a positive real representation
$s_k=\sum_{j=1}^d a_j u_j^k$, with $a_j>0$ and distinct $0<u_j<1$.
Coordinate realizations of the continuation can differ by a change of basis.
The radius is rational. This gives the sharp version of PA-03's all-rival
margin and answers a different question from PA-02's compelled last error
under $2d$ preceding *exact* values.

## 1. Strict checkerboard sign of the inverse

Let $P_j$ be the real monic polynomial of degree $j$ orthogonal to lower
degrees in $L^2(\nu_N)$. These exist by Gram–Schmidt because every finite
moment Gram matrix is positive definite. For $j\ge1$, $P_j$ has $j$ distinct
roots in $(0,1)$. Indeed, multiply $P_j$ by the product of the factors
$u-x$ for its distinct sign-changing roots $x$ in $(0,1)$. The resulting
polynomial has one constant sign there except at finitely many zeros. Its
integral is nonzero. If fewer than $j$ such roots existed this would violate
orthogonality. Degree $j$ now forces all these roots to be simple.

Write $P_j(u)=\sum_i c_{ji}u^i$ and $h_j=\int P_j^2\,d\nu_N>0$.
For $0\le i\le j$, the coefficient $c_{ji}$ has strict sign $(-1)^{j-i}$,
since its magnitude is an elementary symmetric polynomial of positive roots
(with leading coefficient one). For $j=0$ the coefficient is one. With $L$
the lower triangular matrix of these coefficients, orthogonality gives
$LHL^T=\operatorname{diag}(h_0,\ldots,h_d)$. Thus
$$
 (H^{-1})_{ij}=\sum_{k\ge\max(i,j)} c_{ki}c_{kj}/h_k.
$$
Every summand has sign $(-1)^{i+j}$. The matrix $B=SH^{-1}S$ consequently
has strictly positive entries. In particular
$\mathbf1^TB\mathbf1=v^T H^{-1}v$.

## 2. Lower bound and uniqueness, including complex rivals

The rival Hankel block $\widetilde H=(s_{i+j})_{0\le i,j\le d}$ has rank
at most $d$, by factoring it into rows $CA^i$ and columns $A^j b$.
Set $E=H-\widetilde H$, $D=SES$, and $e=\max_{i,j}|E_{ij}|$. Take
$x\ne0$ in $\ker\widetilde H$ and normalize $z=Sx$ by $\|z\|_1=1$.
From $Hx=Ex$ we obtain $z=BDz$. Therefore, for every $i$,
$$
 |z_i|\le\sum_{k,j} B_{ik}|D_{kj}||z_j|
       \le e\sum_k B_{ik}.
$$
Summing over $i$ gives $1\le e\mathbf1^TB\mathbf1$, or $e\ge t_{N,d}$.
This argument even permits independent complex errors in every matrix entry.

If $e=t_{N,d}$, equality holds in every row because the sum of the upper
bounds is exactly one. Every row sum of $B$ is positive, so each $|z_i|>0$.
Equality in the second inequality forces $|D_{kj}|=t_{N,d}$ for every
$k,j$. Equality in the complex triangle inequality in the first forces all
$D_{kj}z_j$ to have the same phase as $z_i$. This list of nonzero terms is
the same in every row, since $B_{ik}>0$. All $z_i$ thus share that phase,
and every $D_{kj}=t_{N,d}$. This yields the unique optimizing matrix error
$E=t_{N,d}vv^T$. Its entries depend only on $i+j$ and correspond to the
claimed alternating prefix. Attainability still requires a stationary rival.

## 3. The first singular block is realized by a positive stationary system

Abbreviate $t=t_{N,d}$. Set $H'=H-tvv^T$. This is a rank-$d$ positive
semidefinite Hankel matrix because
$$
 H'=H^{1/2}(I-ww^T)H^{1/2},\qquad
 w=H^{-1/2}v/(v^TH^{-1}v)^{1/2}.
$$
Its kernel is spanned by $H^{-1}v=SB\mathbf1$, whose last entry is nonzero.
Consequently its leading $d$-square matrix $G'$ is positive definite.
Otherwise a nonzero vector supported in its first $d$ coordinates would
have zero quadratic form and would lie in the kernel of $H'$.

Define the truncated functional on polynomials of degree at most $2d$ by
$L'(f)=\int f(u)d\nu_N(u)-tf(-1)$. Then $H'$ is its moment block.
Normalize the kernel vector to have last entry one and call its coefficient
polynomial $q$, monic of degree $d$. Its coefficients are rational since
$H,v$ are rational. The kernel equations are precisely
$L'(q h)=0$ for every polynomial $h$ of degree at most $d$.

For any $p$ of degree below $d$, choose $h=(1+u)p$. This annihilates the
exterior evaluation term and gives
$$
 \int q(u)p(u)(1+u)\,d\nu_N(u)=0.
$$
The measure $(1+u)d\nu_N$ has positive density throughout $(0,1)$.
The sign-change proof in §1 therefore gives $d$ distinct simple roots
$u_1,\ldots,u_d$ of $q$ in $(0,1)$.

Let $\ell_j$ be the Lagrange cardinal polynomials of degree below $d$ at
these roots and put $a_j=L'(\ell_j)$. Divide any polynomial $f$ of degree
at most $2d$ by $q$, obtaining $f=qh+r$, with $\deg h\le d$ and $\deg r<d$
(the zero polynomial is permitted). Evaluation on the roots and interpolation
give $r=\sum_j f(u_j)\ell_j$. Thus $L'(f)=\sum_j a_j f(u_j)$.
Taking $f=\ell_j^2$ shows $a_j=L'(\ell_j^2)>0$ by positive definiteness
of $G'$. For $f(u)=u^k$ this proves
$$
 m_k=t(-1)^k+\sum_{j=1}^d a_j u_j^k,\qquad 0\le k\le2d.
$$
The interior-node sum defines a dimension-$d$ stationary rival with absolute
error exactly $t$ at every tested index. The formula samples an exterior
node at $-1$ in the quadrature identity. The rival's own nodes are all
interior and stable.

The monic polynomial $q$ annihilates the entire interior-node sum under
forward shift. Hence its rational coefficients and the first $d$ rational
values of $s$ give a rational order-$d$ companion realization. Conversely,
any rival with the same optimal prefix has dimension at least $d$ by $G'$.
Its dimension-$d$ characteristic polynomial provides a monic recurrence by
Cayley–Hamilton. The first $2d$ values determine the coefficients of that
monic recurrence uniquely, since their coefficient matrix is $G'$. They
must give $q$. Its first $d$ values then determine the whole continuation.
This proves the theorem. ∎

## 4. Consequences for observation

**Adversarial readout budget.** Suppose the source is promised to provide
either the authentic prefix or a rival prefix, and in either case each
readout may suffer arbitrary error of modulus at most $\eta$. The two sets
of possible records are disjoint exactly when $2\eta<t_{N,d}$. Below that
threshold the triangle inequality separates the hypotheses. At or above the
threshold the midpoint of the authentic prefix and the optimal
rival prefix is compatible with both. This is an exact worst-case error
threshold for the stated consecutive-readout experiment.

**Fixed-$d$ cost.** Write $\delta_{N,d}=1/(H^{-1})_{dd}$ for PA-02's
prefix-interpolation residual. Book VI, PA-06, proves the fixed-$d$ endpoint
limit of $N^{-2d-2}H^{-1}$ as $\ell\ell^T/[c d!(d+1)!]$, where
$c=15/64$ and $\ell_j=(-1)^j\binom dj$. Here $\ell_d^2=1$ and
$v^T\ell=2^d$. Taking the ratio gives
$$
 \frac{t_{N,d}}{\delta_{N,d}}
 =\frac{(H^{-1})_{dd}}{v^TH^{-1}v}\longrightarrow 4^{-d},\qquad
 N^{2d+2}t_{N,d}\longrightarrow\frac{15}{64}\frac{d!(d+1)!}{4^d}.
$$
The quantifiers require fixed $d$. The exact formula remains available for
each finite $N,d$. It controls precision for identifying finite-order rivals
to the forcing. Estimating the zero-seeded orbit's signed Fourier cancellation
requires another theorem.

**Executed rational control.** For $N=d=1$, direct substitution of the four
fractions for $r(1),r(2),r(3)$ gives $t=362310761/10769637060$.
The attaining model has weight $33382552027/10769637060$ and node
$131441/2498507$. Exact rational evaluation verifies its three errors are
$(t,-t,t)$ and the node is strictly between zero and one. For this check one
can compute $t=(m_0m_2-m_1^2)/(m_0+2m_1+m_2)$, the weight $m_0-t$, and the
node $(m_1+t)/(m_0-t)$. The exact-prefix residual is larger,
$362310761/9825530715$. This finite witness checks normalization and signs.

## Provenance and verification boundary

**PROVED PAPER.** The uniform radius combines established matrix and moment
mechanisms with the authenticated forcing and an explicit optimizing
stationary continuation. The expression $t$ is the classical Christoffel
function at $-1$ with polynomial degrees at most $d$. Indeed Cauchy–Schwarz
in the $H$ inner product gives $\min_{p(-1)=1}\int|p|^2d\nu_N=t$, with
coefficient vector $tH^{-1}v$. The rank perturbation belongs to the classical
componentwise regularity-radius problem. The positive quadrature rule is
Gauss-type quadrature with one prescribed exterior node. The argument above
proves that the unique extremal perturbation in the larger matrix class has
Hankel form and a stable stationary realization for this source. Scholarly
priority for this combination has not been established.

- [Last and Simon, Appendix A, Theorem A.2](https://web.ma.utexas.edu/mp_arc/c/06/06-174.pdf) gives the Christoffel variational principle.
- [Rohn, §2.3](https://www.cs.cas.cz/~rohn/publist/92.pdf) treats componentwise distances to matrix singularity.
- [Bultheel, Cruz-Barroso and Van Barel, *On Gauss-type quadrature formulas with prescribed nodes anywhere on the real line*](https://citeseerx.ist.psu.edu/document?doi=e3345c65cfe4545c93ee0a63ed59e6193bb6f26d&repid=rep1&type=pdf) describes orthogonal polynomials for modified measures with a prescribed node outside the interval. The positive weights and the finite-degree identity used here were proved directly in §3.
