# Finite discrimination of the authenticated BBP forcing with unequal precision

Paper proofs and exact finite checks. This audit joins Astra [#619](https://github.com/femboy2112/SUCC/pull/619) at `f9efa624da06a28e1a8ac99a56499acd11197928` and the Second Forge [#620](https://github.com/femboy2112/SUCC/pull/620) at `5b7470c677135600c39f817064695308b86756f9`. Both drew on the founding questions in [#618](https://github.com/femboy2112/SUCC/pull/618). Only the Astra branch descends from that Git commit. The sources share the classical Hankel-rank mechanism. Their common output supports identifying the relevant model class and the first revealing index. The work below answers part of the Second Forge's request for a precision–horizon tradeoff, including one observation beyond the first revealing window. No claim of external priority is made.

## D4.0. What survives cross-examination

| Input | Verified claim and derivation | Boundary |
|---|---|---|
| [Second Forge FH-3/4/5](../principia_observatoris_second_forge/agents/OPUS_III_HORIZON_HUNTER.md) | Two declared scalar recurrence orders at most $n,m$ give agreement forever from $n+m$ exact terms. The difference satisfies the product recurrence. Without an order bound, every finite prefix can be extended by a distinct eventual-zero recurrence. | Eventual correctness of a learner does not supply a finite stopping certificate. |
| [FH-6(c–e)](../principia_observatoris_second_forge/FINITE_HORIZONS.md) | For $m_k=1/(k+1)$, the Cauchy determinant gives the exact residual $(d!)^4/[(2d)!(2d+1)!]$ if a rival exactly matches the preceding $2d$ terms. This produces the stated obstruction for noisy readouts. | Another rival may distribute its errors among the earlier readouts. The exact all-rival noise threshold is a different quantity. |
| [Astra PA-02/03](../../../docs/principia_observatoris/06_succ_applications.md) | A $d$-state rival has Hankel rank at most $d$. A positive source Gram matrix forces failure within $2d+1$ values. Fitting a monic recurrence to $2d$ exact values leaves the Schur complement $\delta=\det H_d/\det H_{d-1}$ at the next. The kernel-vector norm bound gives a positive certified tolerance. | Stationarity and a declared dimension bound are essential. |
| PA-04/05/06 | A finite Haar Fourier bank misses the uniform law on an odd periodic grid with modulus greater than every tested frequency (use the grid for the designated times-16 map). For the positive BBP measure, the inherited density sandwich, monic least squares and the beta norm price $\delta$. Centering at $1-u$ gives the fixed-$d$ inverse-Gram limit used below. | The Fourier example concerns invariant laws. The forcing estimate concerns a finite translated window. Neither determines the selected orbit statistic. |
| [Astra PA-07](../../2026-11-13/principia_observatoris/sharp_rival_radius.md) | The strict checkerboard inverse turns a componentwise singularity radius into an attained, unique stationary rival. For equal tolerances the radius is the Christoffel function at $-1$. Exterior-node quadrature gives an interior positive realization. | The proof addresses the first $2d+1$-point window with a uniform envelope. The extensions below use its actual hypotheses. |

The setting remains the original recurrence $U_0=0$, $U_n=16U_{n-1}+r(n)$, where
$$
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2).
$$
For every integer $N\ge1$ set $m_k=r(N+k)$ and $H=(m_{i+j})_{0\le i,j\le d}$, $d\ge1$. The authentic positive moment measure $\nu_N$ on $(0,1)$ is the image of $t^{8N-8}(4-2t^3-t^4-t^5)\,dt$ under $u=t^8$. The polynomial in parentheses equals $2(1-t^3)+(1-t^4)+(1-t^5)>0$. Hence $m_k=\int u^k\,d\nu_N$ and every finite Gram block is positive definite. The finite-window theorems D4.1–3 work for any finite positive measure supported on $[0,1]$ with positive density throughout $(0,1)$. The numerical constants and late-onset limit use the four actual poles. A rival is any complex scalar sequence $s_k=C_0 A^k b$ with a fixed matrix of dimension at most $d$.

## D4.1. Exact radius for any positive readout envelope

Fix any real $c_0,\ldots,c_{2d}>0$. Put $C_{ij}=c_{i+j}$, $S_{ii}=(-1)^i$ (diagonal), $B=SH^{-1}S$ and let $\rho$ denote spectral radius. Then
$$
e(c):=\min_{s}\max_{0\le k\le2d}\frac{|m_k-s_k|}{c_k}
=\rho(BC)^{-1}.
$$
Every minimizing complex rival has the same prefix $s_k=m_k-e(c)(-1)^k c_k$ and the same infinite scalar continuation. The continuation has a positive $d$-atom realization with distinct nodes strictly in $(0,1)$. No log-convexity, moment representation, or positive semidefiniteness of the envelope matrix $C$ is required.

**Positive inverse after changing signs.** Real monic orthogonal polynomials of degree $j$ for $\nu_N$ have $j$ distinct roots in $(0,1)$. Otherwise multiplying by one factor for each interior sign-changing root gives a lower-degree test polynomial whose product has constant sign and nonzero integral, contradicting orthogonality. Their coefficient rows thus alternate strictly in sign through degree $j$. Orthogonalizing $H$ with these rows expresses its inverse as a sum of coefficient outer products divided by the positive squared norms. At entry $(i,j)$ all nonzero terms have sign $(-1)^{i+j}$, including the top-degree term. This proves $B_{ij}>0$.

**Necessary radius and equality.** The rival's Hankel block has rank at most $d$ by its observability-times-reachability factorization. If $x$ is a nonzero null vector, set $z=Sx$, $D=S(H-H_s)S$ and $\epsilon=\max_k|m_k-s_k|/c_k$. Then $z=BDz$ and $|z|\le\epsilon BC|z|$ componentwise. The strictly positive matrix $BC$ has a simple positive Perron eigenvalue $\lambda=\rho(BC)$ and strictly positive left and right eigenvectors (Perron–Frobenius). Multiplication by its positive left eigenvector gives $\epsilon\lambda\ge1$. At equality, equality holds componentwise and $|z|$ is a positive right eigenvector. Strict positivity of $B,C$ forces $|D_{ij}|=\epsilon C_{ij}$ everywhere. The triangle equality forces every $D_{ij}z_j$ to have the phase of each $z_k$, independently of $k$. Consequently all $z_j$ have the same phase and $D=\epsilon C$.

**Existence and real nodes.** Put $t=1/\lambda$ and $H'=H-tSCS$. The prospective block $H-aSCS$ stays positive definite for $0\le a<t$: any earlier singularity would give the preceding vector inequality even for a freely perturbed matrix. At $a=t$ its kernel corresponds via $S$ to the Perron eigenspace of $BC$. Thus $H'$ is positive semidefinite of rank $d$, with kernel vector alternating strictly in sign. Its leading $d$-square block $G'$ is positive definite, since an extended zero last coordinate cannot lie in this kernel. Normalize the kernel polynomial $q$ to be monic, and write $L'(u^k)=m_k-t(-1)^kc_k$ for $0\le k\le2d$. We have $L'(qh)=0$ for $\deg h\le d$.

On the polynomials of degree below $d$ with inner product from $G'$, multiplication by $u$ modulo $q$ is self-adjoint. For two such polynomials $f,g$, reducing $uf$ or $ug$ modulo $q$ contributes a multiple of $q$ orthogonal to the other factor. Its vector $1$ is cyclic since $1,u,\ldots,u^{d-1}$ are independent. The spectral theorem now yields $d$ distinct real eigenvalues $x_j$ and positive weights $a_j$ (the squared projection lengths of $1$), and the minimal polynomial is $q$. For $\deg f\le2d$ divide $f$ by $q$, obtaining $f=qh+r$ with $\deg h\le d$, $\deg r<d$. Thus $L'(f)=L'(r)=\sum_j a_j f(x_j)$. Strict alternation of the coefficients of $q$ gives $q(x)\ne0$ for $x\le0$. All $x_j>0$.

**Upper support bound.** Suppose one root is $R\ge1$. Form
$$
f(u)=u(R-u)\prod_{x_j\ne R}(u-x_j)^2.
$$
It vanishes at all atoms and is positive almost everywhere on $(0,1)$. It has degree $2d$, vanishing constant term, and coefficients of strict sign $(-1)^{k-1}$ in degrees $1\le k\le2d$. Indeed $f(-v)=-v(R+v)\prod_{x_j\ne R}(v+x_j)^2$ has strictly negative nonconstant coefficients. The alternating error formula therefore makes $\int f\,d\nu_N-L'(f)=t\sum_k f_k(-1)^kc_k<0$, whereas $L'(f)=0$ and $\int f\,d\nu_N>0$. The contradiction places every node in $(0,1)$. The atom sum attains $t$ with a stable diagonal realization. Any rival with its same prefix has dimension exactly $d$ by $G'>0$. The first $2d$ values uniquely solve its characteristic recurrence since the coefficient matrix is $G'$. This also forces the entire scalar continuation. ∎

For rational source and rational $c$, $t$ is real algebraic. A rational minimum can fail already at $N=d=1$, $c=(1,1,2)$. The smaller root of
$$
t^2-\frac{1005869}{153153}t+\frac{362310761}{3135807675}=0
$$
is the radius. The discriminant is $25023302679797/765765^2$ with numerator strictly between $5002329^2$ and $5002330^2$. Consequently the unique attaining prefix has irrational entries. Rational stationary rivals approach it by approximating its recurrence coefficients and starting values, since each of finitely many readouts depends continuously on them.

**Classical boundary.** The matrix lower bound is a special instance of the classical componentwise regularity radius. The proof above adds a Hankel-compatible extremizer, its unique stationary continuation and its source-interval support for arbitrary Hankel error envelopes to this comparison. [Rohn, §2.3, equations (23)–(24)](https://www.cs.cas.cz/~rohn/publist/92.pdf).

Kammler’s continuous-interval approximation theorem establishes positive, alternating real exponential approximants for completely monotone functions. Rump studies componentwise perturbations preserving matrix structures including Hankel structure. Here the samples are a finite integer grid, the rival may have a complex non-diagonalizable realization, and the envelope can vary independently at every sample. These neighboring results do not by themselves supply the realization and support argument above. [Kammler, 1976](https://doi.org/10.1137/0713062) · [Rump, 2003](https://www.tuhh.de/ti3/paper/rump/Ru03g.pdf)

## D4.2. Source-specific asymptotics, geometric tolerances and bit budgets

Fix $d$ and $c$ independently of $N$. Put $a_d=(15/64)d!(d+1)!$ and $b_i=\binom di$. PA-06 gives $N^{-2d-2}B\to bb^T/a_d$: its proof centers the source moments at $v=1-u$, uses $N^{j+2}\int v^j d\nu_N\to (15/64)(j+1)!$, and takes determinant ratios of the finite centered Gram. Continuity of the spectral radius and the single positive eigenvalue of $bb^TC$ give
$$
N^{2d+2}e(c)\longrightarrow
\frac{a_d}{b^TCb}
=\frac{(15/64)d!(d+1)!}{\sum_{k=0}^{2d}\binom{2d}{k}c_k}.
$$
The last identity is Vandermonde's binomial convolution. It identifies the individual contribution of every readout tolerance to the leading late-onset resolution cost.

If $c_k=r^k$, $r>0$, write $v_i=(-r)^i$. Then the exact radius simplifies to $t=1/(v^TH^{-1}v)$ and $t/\delta\to(1+r)^{-2d}$. It is rational for rational $r$ and rational source moments. The monic null polynomial $q$ is orthogonal for $(u+r)\nu_N$: insert $h=(u+r)p$, $\deg p<d$, into $L'(qh)=0$; the subtracted functional $t f(-r)$ vanishes on $qh$. This yields the external evaluation at $-r$ and recovers PA-07 at $r=1$.

Suppose the authentic and rival hypotheses each admit independent deterministic errors in all coordinates, with respective (possibly different) radii $a_k,h_k\ge0$ and strictly positive sums $g_k=a_k+h_k$. Their possible records are disjoint **exactly if**
$$
H-S(g_{i+j})S \text{ is positive definite},
\quad\text{equivalently}\quad \rho\bigl(B(g_{i+j})\bigr)<1.
$$
Indeed two coordinate balls overlap exactly when their centers differ by at most the sum of their radii. Products of independently available errors intersect precisely when all individual balls do. The theorem realizes the boundary rival and monotonic enlargement preserves overlap. To see the positive definiteness test, the symmetric pencil is congruent to $I-a H^{-1/2}S(g_{i+j})SH^{-1/2}$ after scaling by $a$. Its largest eigenvalue before multiplication by $a$ equals the Perron root of $B(g_{i+j})$ by similarity. At $a=1$ the condition follows. Correlated noise need not fill this product of balls.

For equal per-hypothesis radii $2^{-b_k}$, choose integer bit counts $b_k\ge0$ and use $g_k=2^{1-b_k}$. The test becomes a finite exact check of positive leading principal minors of a rational matrix. The smallest total bit cost is obtained by testing nonnegative integer compositions in increasing total sum; a feasible common bit count exists as $g\to0$. For the authentic onset $N=1$ at dimension $d=1$, the exact probe obtains a minimum of 13 total bits. One optimal allocation is $(0,5,8)$, while a common bit count requires 6 bits at each of the three times (18 total). Here a “bit” is one unit of the declared absolute-error cost. A literal fixed-range encoder also needs a range, codebook and boundary rule. Other quantizers, shared errors, relative accuracy and unbounded sample length require their own model.

## D4.3. One more readout separates the previous optimizer

For a geometric envelope $r^k$ as above, let $s^*$ be the unique optimizer on $0,\ldots,2d$ and $q$ its monic recurrence polynomial. Then exactly
$$
m_{2d+1}-s^*_{2d+1}=-t r^{2d+1}+J,
\qquad J=\int_0^1(u+r)q(u)^2\,d\nu_N(u)>0.
$$
To verify this, the quadrature with nodes $-r,x_1,\ldots,x_d$ and weights $t,a_1,\ldots,a_d$ is exact through degree $2d$. Subtract the monic polynomial $(u+r)q(u)^2$ from $u^{2d+1}$. The remainder has degree at most $2d$, and the subtracted polynomial vanishes at every quadrature node. This gives the identity. By the same centered Gram determinant proof as PA-06 applied to $(u+r)\nu_N$, its degree-$d$ monic minimum $J$ satisfies $N^{2d+2}J\to (1+r)a_d$. Indeed $u+r=(1+r)-(1-u)$ and the extra centered moment is smaller by one power of $N$. Hence
$$
\frac{m_{2d+1}-s^*_{2d+1}}{t}
\longrightarrow (1+r)^{2d+1}-r^{2d+1}.
$$
In particular, whenever $(1+r)^{2d+1}>2r^{2d+1}$, the old optimum violates the enlarged-window tolerance $tr^{2d+1}$ for all sufficiently large $N$. This includes $r=1$ with limiting ratio $2\cdot4^d-1$.

The infimal weighted error on the longer window is then **strictly greater** than $t$. Otherwise a minimizing sequence of rivals has bounded prefixes on the longer window, hence a convergent subsequence. Its first block is singular by closedness of the determinant condition. The equality proof of D4.1 already forces the limiting first prefix for any singular block. Its leading $d$-square block is invertible, and so are those of the subsequence eventually. Their monic recurrence coefficients, solved from the first $2d$ moments by this block, converge to those of $s^*$. Their next values must converge to $s^*_{2d+1}$, contradicting the longer-window tolerance. This proves strict gain on a further observation without evaluating the new full minimax radius. ∎

## D4.4. Cost per additional state at fixed source onset

Fix $N\ge1$ and $r>0$ while $d\to\infty$, and denote by $e_d(r)$ the radius on $2d+1$ samples with $c_k=r^k$. Then
$$
\lim_{d\to\infty} e_d(r)^{1/d}
=(\sqrt r+\sqrt{1+r})^{-4}.
$$
This gives the leading exponential rate in the other asymptotic direction. It also holds for Lebesgue measure on $(0,1)$, the harmonic source of FH-6. In particular, unit-envelope minimax precision requires $4\log_2(1+\sqrt2)d+o(d)$ bits **per readout** (about $5.0862d$), for both sources. Allowing error under both hypotheses changes the bit threshold by at most a constant. FH-6's approximately $4d$ bits count the exact-prefix mimic's last compulsory error and give only a necessary bound when all readouts can vary.

**Proof.** By the rank-one formula and Cauchy–Schwarz in the $H$ inner product,
$$
e_d(r)=\min_{\deg p\le d,\ p(-r)=1}\int_0^1 |p(u)|^2\,d\nu_N(u).
$$
Indeed the minimum is attained by the coefficient vector $H^{-1}v/(v^TH^{-1}v)$. Denote $R=1+2r$ and $L=R+\sqrt{R^2-1}=(\sqrt r+\sqrt{1+r})^2$. Let $T_d$ be the Chebyshev polynomial with $T_d(\cos\theta)=\cos(d\theta)$. From the cosine recurrence, $T_d(R)=(L^d+L^{-d})/2$. The normalized trial polynomial $T_d(2u-1)/T_d(-R)$ gives $e_d(r)\le\nu_N((0,1))/T_d(R)^2$. This bounds its $d$th-root limsup by $L^{-2}$.

For the reverse bound fix $h\in(0,1/2)$. The authentic density has a strictly positive minimum $M_h$ on $[h,1-h]$, and so does the harmonic density. For $f(x)=p((1+(1-2h)x)/2)$, write $U=\max_{[-1,1]}|f|$ and $R_h=R/(1-2h)$. The real Chebyshev exterior inequality gives $1=|f(-R_h)|\le T_d(R_h)U$. To see it for complex $f$ with $f(-R_h)=1$, use its real part. If this inequality failed then $T_d(x)-T_d(-R_h)\operatorname{Re}f(x)$ would alternate strictly at the $d+1$ Chebyshev extrema and vanish at $-R_h$, an impossible $d+1$ distinct zeros for degree $\le d$.

Here is a polynomial-cost conversion of the supremum bound to an integral. Expand $f(x)=\sum_{j=0}^d a_j T_j(x)$. Cosine orthogonality gives $|a_j|\le2U$. Also $|T_j'(x)|\le j^2$ on $[-1,1]$, by $|\sin(j\theta)|\le j|\sin\theta|$ and continuity at the endpoints. Hence $\|f'\|_\infty\le2d^3 U$ for $d\ge1$. From a point where $|f|=U$ an interval of length $1/(4d^3)$ fits to one side inside $[-1,1]$, and $|f|\ge U/2$ on it. Changing variables gives
$$
\int |p|^2\,d\nu_N\ge
\frac{M_h(1-2h)}{32d^3 T_d(R_h)^2}.
$$
Taking $d$th roots, then $h\downarrow0$, gives the liminf $\ge L^{-2}$. The same reasoning works for any finite measure supported on $[0,1]$ whose density is bounded below on every such interior interval. This proves the stated rate. ∎

For a direct comparison on the authentic source, the exact-prefix minimizer's last residual satisfies $\lim_{d\to\infty}\delta_{N,d}^{1/d}=1/16$ at fixed $N$. Indeed PA-05 bounds $\delta_{N,d}$ between two constant multiples of its beta norm $h_d(\alpha)$, $\alpha=N-7/8$. The closed product in PA-05 gives
$$
\frac{h_{d+1}(\alpha)}{h_d(\alpha)}=
\frac{(d+1)(d+2)(d+\alpha)(d+\alpha+1)}
{(2d+\alpha+3)(2d+\alpha+2)^2(2d+\alpha+1)}
\longrightarrow 1/16.
$$
Taking logarithmic Cesàro means proves the same $d$th-root rate. Thus choosing the wider rival family of all noisy fits changes the authentic exponent from $4$ to $4\log_2(1+\sqrt2)$ bits per dimension at unit envelope. This comparison is between the final-point error after preceding exact observations and the error distributed across the entire window.

## D4.5. Frontier and falsification

The harmonic source in FH-6 is the uniform measure on $(0,1)$, so D4.1 gives its exact noise threshold as a specialization. For $d=1$ and unit envelope it is $1/28$, smaller than its exact-prefix residual $1/12$. This reconciles the two forges' precision claims and supplies a discriminator for a mistaken identification of these radii.

The arithmetic readout is the original forcing. The [Main XXV frontier](../../../docs/PI_NORMALITY_FRONTIER.md) names $\limsup_B\operatorname{Re} W_B(1)<1$ as its weakest open signed rung R0. [#610](https://github.com/femboy2112/SUCC/pull/610) gives a logarithmic loss whose normalized saving tends to zero. [#612](https://github.com/femboy2112/SUCC/pull/612) at `2128708b14d45493a2a8e48d967b098299b2556d` compares lag pinbeds and transports norms, while the original-zero all-shell estimate remains open. The coherent changed seed $-\pi/16$ shares *every* $m_k$ with the zero-seeded recurrence. Thus every new precision test above gives identical answers for the two seeds, even though their completed orbits differ. The new source estimate prices forcing-model discrimination. A new instrument that can force R0 must use information sensitive to the selected seed.

**Verification.** D4.1–4 are paper proofs with finite rational controls in [the exact probe](weighted_forcing_probe.py) and [its receipt](receipts/weighted_forcing.json). The receipt includes a nongeometric envelope, an indefinite envelope matrix, a rationality counterexample, a held-out readout and an exhaustive small bit-allocation problem. The next unresolved precision problem is the exact optimum on longer and irregularly sampled windows with prescribed weights.

[Joint onset and dimension](JOINT_PRECISION.md) proves D4.6–7. For every onset and dimension a positive finite Jacobi sum brackets the true radius within absolute source constants. A separate joint limit gives the exact logarithmic rate for finite limiting onset/dimension ratio and fixed geometric envelope.
