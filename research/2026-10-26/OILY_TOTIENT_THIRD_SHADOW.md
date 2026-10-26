# Operation Oily–Macaroni Totient: Möbius-primitive grades, complex Mellin paths, and the third-order golden–Gamma shadow

**Research round:** October 26, 2026. **Starting point:** the authentic, source-typed PR #309 packet compiler at `8e9d8a4d7d42bb0931f899ac221f27fccf090b36`, stacked over PR #306. **Scope:** a new (to this program) synthesis of elementary Möbius inversion, two geometric-source loops, Gamma-limit Mellin moments, Fourier-enriched finite arithmetic quotients and selected-phase source transport. Classical elementary ingredients are not claimed to be new. **π base-16 normality and RH remain OPEN.** No imported source changes; no physical virtual-particle probability claim.

## 0. Steelman of the author's research intuition

The author constructs meaning by recognizing a *common operational phenomenon* behind superficially different carriers: discrete recursion/Fibonacci golden normalization, continuous logarithmic Gamma/Euler regularization, finite SUCC/FUCC quotient paths, projective signed mirrors, and real-circle BBP phases. The proposed “oily-macaroni totient” should count **which mathematical paths are primitive**, weight them by the actual positive source, remember the **complex phases** of those paths, and measure a **connected source-dependent log response**. It must preserve intermediate histories and the initial arithmetic selection, not use apparent numerical proximity as proof. A conjectural third-order link is valuable only if it is derived by an actual source map and survives well-chosen hostile controls.

The strongest testable reading is the following **graded** packet interface. Its packet grammar is that of PR #309: the two geometric loops correspond to the *specific* rational-positive expansion of the unchanged BBP Green kernel. Removing that grammar changes the fixed point and the Oily–Macaroni coefficient. The resulting probability law is an auxiliary arithmetic observation, **not a probabilistic realization of the deterministic π digit orbit**.

## 1. Source passport and the exact joint probability space

Let

$$
R(x)=\frac{4-2x^3-x^4-x^5}{16-x^8}
=\frac{1-x}{(2-x^2)(x^2-2x+2)},\quad 0\le x\le1.
$$

Put $u(x)=x-x^2/2$, $v(x)=x^2/2$. Then $0\le v\le u\le1/2$ and

$$R(x)=\frac{1-x}{4(1-u)(1-v)}.$$

Define the **actual PR #309 packet polynomial**, for each grade $j\ge0$,

$$p_j(x)=\frac{1-x}{4}\sum_{k=0}^{j}u(x)^kv(x)^{j-k}.$$

Every $p_j\ge0$, $\sum_{j\ge0}p_j=R$, and the finite compiler has the **sharp source-relative bound**

$$0\le R-\sum_{j<M}p_j\le\rho_M R,\quad\rho_M=(M+2)/2^{M+1}.$$

At an arithmetic source time $n\ge1$, set $a=8n$ and

$$T_n=\int_0^1x^aR(x)\,dx
=\sum_{m\ge1}16^{-m}r(n+m)>0.$$

**On ONE common carrier** $\{(x,j):0<x<1,\,j\ge0\}$, define the probability law

$$\boxed{\mathbb P_n(J=j, X\in dx)=\frac{x^a p_j(x)}{T_n}\,dx.}$$

The source-time marginal in $x$ is $x^aR(x)/T_n\,dx$. Given $X=x$, $J=K_1+K_2$ with **two independent geometric variables conditional on $x$** and parameters $u,v$. This independence is *within the defined packet source law*, not independence between actual arithmetic times or primes. At $x=1$, the limiting grade weights are

$$\boxed{w_j=\frac{j+1}{2^{j+2}},\quad\sum_j w_jz^j=G(z)=\frac1{(2-z)^2}.}$$

The total tail $\sum_{j\ge M}w_j=\rho_M$ equals, **exactly**, the same sharp compiler defect $\rho_M$.

### Exact source-graded finite Mellin integral

For $\operatorname{Re}s>-2$ and $|z|\le1$,

$$\boxed{
\mathcal K_n(z,s)=\mathbb E_n[z^JY_n^s]
=\frac{a^s}{4T_n}\int_0^1
\frac{x^a(1-x)^{s+1}}{(1-zu(x))(1-zv(x))}\,dx,
\quad Y_n=a(1-X).
}$$

This uses the *same* BBP kernel $R$ and sums both packet stages *before* analytic continuation. The integral is absolutely convergent in the displayed domain. At $z=1,s=0$, it equals 1. With $\operatorname{Re}s>-2$, all source/endpoint limits below are legitimate; the presentation does not assert continuation past that domain.

## 2. Oily totient, Möbius projector and Fourier characters

For each $q\ge1$ define the scalar weighted primitive totient and its complex Fourier form:

$$\boxed{\Phi_{\rm OM}(q)=\mathbb P(\gcd(J,q)=1),\qquad
C_q(z)=\mathbb E[\mathbf1_{\gcd(J,q)=1}z^J],\ |z|=1.}$$

Here $J$ follows the **limiting** weight $w_j$ and $\gcd(0,q)=q$. For a divisor $d$, put $t=(z/2)^d$. Exact geometric summation gives

$$\sum_{m\ge0}w_{dm}z^{dm}=
\frac{1+(d-1)t}{4(1-t)^2}.$$

Hence classical Möbius inversion gives the **exact rational-function theorem**

$$\boxed{ C_q(z)=\frac14\sum_{d\mid q}\mu(d)
\frac{1+(d-1)(z/2)^d}{[1-(z/2)^d]^2},\quad
\Phi_{\rm OM}(q)=C_q(1).}$$

Exact examples:

| $q$ | $\Phi_{\rm OM}(q)$ |
|---:|---:|
| 1 | $1$ |
| 2,4,16 | $4/9$ |
| 3 | $29/49$ |
| 6 | $416/1323$ |

In particular,

$$\Phi_{\rm OM}(6)-\Phi_{\rm OM}(2)\Phi_{\rm OM}(3)=68/1323>0.$$

The totient **is not multiplicative**: different coprimality conditions see the same concentrated grade $J$. This is a correlation of auxiliary packet grades; it does not certify any correlation of genuine BBP prime-clock values.

For every dyadic $q=2^k$ ($k\ge1$), the primitive grades are the **odd** grades. With $z=e^{2\pi ih/q}$,

$$\boxed{C_{2^k}(z)=\frac{4z}{(4-z^2)^2},\qquad
\frac4{25}\le|C_{2^k}(z)|\le\frac49.}$$

These characters **never vanish**. Indeed they remain close to $4/9$ as $k\to\infty$ with fixed $h$. Primitive-path positivity and finer dyadic resolution therefore DO NOT automatically create Fourier cancellation.

## 3. Source-conditioned primitive Fourier transform and an exact source identity

Conditioned on $X=x$, the grade PGF is

$$F_x(z)=\frac{(1-u)(1-v)}{(1-uz)(1-vz)}.$$

For dyadic primitive paths (all odd $J$), let

$$F_x^{\rm odd}(z)=\mathbb E_x[z^J\mathbf1_{J\text{ odd}}]
=\frac{(1-u)(1-v)z(u+v)}{(1-z^2u^2)(1-z^2v^2)}.$$

Since **$u+v=x$**, the complete source-weighted character simplifies to

$$\boxed{R(x)F_x^{\rm odd}(z)
=\frac{z x(1-x)}{4(1-z^2u(x)^2)(1-z^2v(x)^2)}.}$$

This is the exact two-atom source primitive character, with the boundary zero still present. The corresponding full complex source/grade/Mellin transform is

$$\boxed{\mathcal K_n^{\rm odd}(z,s)=
\frac{a^s z}{4T_n}\int_0^1
\frac{x^{a+1}(1-x)^{s+1}}{(1-z^2u(x)^2)(1-z^2v(x)^2)}\,dx.}$$

This formula gives all higher logarithmic jets by differentiating in $s$ at zero. It is **not** a Weyl sum over the zero-seeded integer BBP orbit.

## 4. Proved boundary expansion: third-order golden-centered log shadow

Let $g_{q,z}(j)=\mathbf1_{\gcd(j,q)=1}z^j$, with $|z|=1$. Then, as $x\uparrow1$,

$$\mathbb E_x[g_{q,z}(J)]
=C_q(z)+(1-x)H_q(z)+O((1-x)^2),$$

where the remainder may be bounded uniformly for $|z|=1$ and for dyadic $q$, and

$$\boxed{H_q(z)=2C_q(z)-zC_q'(z).}$$

Proof: $u'(1)=0$, $v'(1)=1$, $R(x)\sim1-x$, and direct differentiation of the exact conditional packet formula yields

$$\frac{d}{dx}\Pr_x(J=j)\Big|_{x=1}=(j-2)w_j.$$

The exponential grade tail makes the first two derivatives summable uniformly against $|g|\le1$. In particular, for the odd (dyadic primitive) projector,

$$\boxed{H_{2^k}(z)=\frac{4z(4-5z^2)}{(4-z^2)^3},\qquad H_{2^k}(1)=-4/27.}$$

Meanwhile $Y_n=a(1-X)$ converges in law, and in all fixed polynomial/logarithmic moments, to $Y\sim\operatorname{Gamma}(2,1)$ with density $ye^{-y}dy$. The proof uses $R(x)=(1-x)/D(x)$, $D(1)=1$, $1/4\le1/D(x)\le1$ and dominated convergence after $y=a(1-x)$; the integrable envelope bounds are uniform on the $y$-interval and the log singularity is integrable against $y$.

For any fixed $s$ with $\operatorname{Re}s>-2$ we get the **connected complex Mellin theorem**:

$$\boxed{
\lim_{n\to\infty}a\,\operatorname{Cov}_{\mathbb P_n}
(g_{q,z}(J),Y_n^s)
=H_q(z)\,s\,\Gamma(2+s),\qquad a=8n.
}$$

The covariance is algebraic $\mathbb E[AB]-\mathbb E[A]\mathbb E[B]$ for complex observables, **not** a Hermitian covariance with conjugation. Proof: conditional on $X$, the first variation is $(Y_n/a)H_q(z)$; constants disappear in connected covariance and $\operatorname{Cov}_{\Gamma(2)}(Y,Y^s)=\Gamma(3+s)-2\Gamma(2+s)=s\Gamma(2+s)$.

Differentiating at $s=0$ gives the **first connected logarithmic shadow**:

$$\boxed{\lim_{n\to\infty}a\,\operatorname{Cov}(g_{q,z}(J),\log Y_n)=H_q(z).}$$

For the genuine **third-order algebraic observable** consisting of one primitive grade factor and two copies of a *golden-centered* logarithmic boundary factor, set $q_*=(3-\sqrt5)/2=\varphi^{-2}$ and $\Omega=\varphi^{-1}-\gamma$. The packet PGF $G(z)=(2-z)^{-2}$ has fixed points $q_*$ and 1; rational iteration starting from 0 selects its smaller fixed point $q_*$. Because $\psi(2)=1-\gamma$ and $1-q_*=\varphi^{-1}$, the second derivative of $e^{-q_*s}s\Gamma(2+s)$ gives

$$\boxed{
\lim_{n\to\infty}a\,\operatorname{Cov}
\bigl(g_{q,z}(J),[\log Y_n-q_*]^2\bigr)
=2\,\Omega\,H_q(z).
}$$

**In particular, for the dyadic primitive scalar projector** $g=\mathbf1_{J\text{ odd}}$,

$$\boxed{\lim_{n\to\infty}8n\operatorname{Cov}\bigl(
\mathbf1_{J\text{ odd}},[\log Y_n-\varphi^{-2}]^2\bigr)
=-\frac8{27}(\varphi^{-1}-\gamma).}$$

This proves a nontrivial first-order *finite-time correlation defect* carrying the named constant within the **specified, retained grade law**. Neither $\gamma$ nor $\Omega$ was inserted into the finite source distribution.

### Fundamental gauge/centering counterexample (important)

For any real center $c$, the same proof gives the coefficient $2[1-\gamma-c]H_q(z)$. Choosing $c=1-\gamma$ makes that coefficient zero. **The exact mixed third-order joint cumulant with the logarithmic observable centered at its own mean has zero $a^{-1}$ coefficient**: the golden/Oily term arises from the *specified external center* $q_*$. This is a true graded-observable result, **NOT a gauge-invariant intrinsic constant of the ungraded BBP kernel**, and not an independent third cumulant theorem.

PR #309 already exhibits source-compatible packet regradings that change the fixed point without changing the completed ungraded kernel. This new theorem preserves that negative evidence. The fact that the covariance is "connected" with respect to the grade observable does **not** remove its dependence on the logarithmic reference.

## 5. A sharp finite quantitative transfer — and why it still cannot prove normality

For each time $n$ define the auxiliary character

$$W_{n,q}(z)=\mathbb E_n[g_{q,z}(J)].$$

For dyadic $q$ the limiting coefficient is $C_q(z)=4z/(4-z^2)^2$.

The total-variation **$\ell^1$** distance between the product of two geometric laws with parameters $u(x),v(x)$ and their limiting fair geometric laws is bounded by

$$4\bigl(|u-1/2|+|v-1/2|\bigr)=4(1-x).$$

Here we used the derivative $\ell^1$ estimate $\sum_j|\partial_p [(1-p)p^j]|\le2/(1-p)\le4$ for $0\le p\le1/2$ and the tensor-product triangle inequality. Also $R(x)=(1-x)w(x)$ with $w=1/D(x)$ increasing, so comparing the source measure with $\mathrm{Beta}(a+1,2)$ gives $\mathbb E_n(1-X)\le2/(a+3)$ (the weight $w$ favors larger $X$). Hence

$$\boxed{|W_{n,q}(z)-C_q(z)|\le\frac8{8n+3}\le\frac1n.}$$

Now let $U_0=0$, $U_{n+1}=16U_n+r(n+1)$ be the **actual** SUCC orbit and $Z_n(h)=e^{2\pi ihU_n}$. For every $N,h\in\mathbb Z$ and any dyadic modulus/frequency $q=2^k$, $z=e^{2\pi i\ell/q}$,

$$\boxed{
\left|\frac1N\sum_{n=1}^{N}Z_n(h)W_{n,q}(z)
-C_q(z)\frac1N\sum_{n=1}^{N}Z_n(h)\right|
\le\frac{H_N}{N}.
}$$

This is **source-faithful selected Fourier transport with a quantitative, uniform harmonic error**. Because $|C_q(z)|\ge4/25>0$, the weighted selected sum tends to zero if and only if the original selected Weyl sum tends to zero (at each fixed selected $h$). The equivalence is source-passive, **not a new cancellation estimate**.

Replace the infinite grade packet law by the first $M$ polynomial layers normalized by their exact rational mass. The original source-relative compiler bound says its discarded mass is at most $\rho_M$. The $\ell^1$ normalized-observation error is therefore at most $2\rho_M$. Thus the finite certified *representation* of the selected sum has error at most

$$\boxed{H_N/N+2(M+2)/2^{M+1}.}$$

One may choose $M_N=\lceil3\log_2(N+2)\rceil$ so this representation error is $O(\log N/N)$. This is much cheaper than approximating the **expanding arithmetic phase** itself, which needs a far deeper $M\asymp N$ schedule as proved in PR #309. **Do not confuse the two precision requirements.**

### Nonvanishing and changed-seed obstruction

The dyadic primitive limit $|C_q(z)|$ is bounded below by $4/25$; as $q=2^k\to\infty$ with fixed $\ell$, $C_q(z)\to4/9$. The packet-weight character does not itself become small at fine resolution. More decisively, keep the original forcing $r(n)$ and its entire positive packet law, but use the alternate initial state $V_0=-T_0=-\pi/16$. Then $V_n=-T_n\to0$, and the selected Fourier mean converges to 1. Every auxiliary packet/totient/third-shadow object is unchanged under this seed switch. Its selected decorated mean converges to $C_q(z)\ne0$. **No implication from packet primitive masses, scalar weighted totients, or centered Gamma moments alone to π normality can hold without the actual zero-seed/phase coupling.**

## 6. Exact finite certificates and numerical holdouts

For each fixed finite packet grade $j$, $p_j$ is a rational polynomial divisible by $(1-x)$. The moments

$$m_{n,j}^{(k)}=\int_0^1 x^{8n}p_j(x)[\log(1-x)]^k\,dx,\quad k=0,1,2$$

are **exact rationals**. For a monomial $c x^m(1-x)$ the three factors are

$$B=\frac1{(8n+m+1)(8n+m+2)},\quad
B(1-H_{8n+m+2}),$$

$$B\left[(1-H_{8n+m+2})^2+H_{8n+m+2}^{(2)}-1\right].$$

This is ordinary beta differentiation; the $\zeta(2)$ constants cancel at finite integer indices. The implementation uses exact Fraction coefficients, tests against independent high-precision quadrature, and returns the finite-depth covariance with golden center as

$$A_{n,M}+B_{n,M}\left[\log(8n)-q_*\right]$$

for **rational** $A_{n,M},B_{n,M}$; no numeric $\gamma$ or $\varphi$ is used in the finite arithmetic certificates. The finite compiler's defect for bounded observables is certified by $\rho_M$. Because $\log Y$ is unbounded, this same total-variation bound does NOT alone certify finite squared-log-moment errors; those need dedicated moment-tail estimates or analytic asymptotic proofs, as provided conceptually in §4.

The tested exact values $\Phi_{\rm OM}(2)=4/9$, $\Phi_{\rm OM}(3)=29/49$, $\Phi_{\rm OM}(6)=416/1323$ and nonmultiplicativity $68/1323$ match the direct grade series. For the unweighted dyadic parity projector the predicted coefficients are $-4/27$ in the first log covariance and $-(8/27)(\varphi^{-1}-\gamma)$ in the golden-centered quadratic log covariance. Independent direct source-density quadrature approaches these limits. The **finite** values are numerical probes, while the asymptotic identities follow from the analytic Gamma-limit proof.

## 7. Verdict, relevance to the π-normality proof, and next falsifier

**Earned mathematics:** the source-graded Möbius totient and complex rational-function filter; exact dyadic Fourier nonvanishing; full complex Mellin connected-shadow limit; source-graded **golden-centered third-order covariance** with the Oily–Macaroni coefficient; a uniform, source-faithful finite totient/Weyl **transport without saving**; exact finite rational polynomial/log moments; definitive changed-seed and gauge countermodels.

**Not earned:** a source-intrinsic golden constant independent of packet grading or centering; mathematical dynamics giving actual random probabilities to π; power-saving signed Weyl sums; mean-zero selected cross-time correlations; full normality or RH.

**Single real next gate:** build a source-authenticated cross-*time* joint law or operator whose primitive-graded/Mellin response is conditioned on the true **integer carry history and the zero-seed trajectory**, not only source time $n$, and prove a genuinely signed off-diagonal estimate that rejects (a) the exact-forcing changed seed, (b) rational matched-moment nonnormal source, (c) uniform-cell auxiliary-cancellation nonnormal source, (d) regraded packet laws with different $q_*$, and (e) nontrivial cross-digit Walsh modes. If this cannot be done, prove a typed no-go for this primitive-path grammar and seek an external analytic arithmetic estimate. **The equality of scalar normalization constants is not the theorem.**

### Bibliographic/precursor anchors

PR #309 `FOUR_POLE_ATOMIC_SUBSTRATE.md`, `OILY_MACARONI_SOURCE_BRIDGE.md`, and PR #306 signed-categorical base-change; classical Möbius inversion, the beta/gamma differentiation formulas (NIST DLMF §§5.2, 5.9, 5.12), Gamma(2) polygamma values, Weyl's criterion, and the BBP formula. New-to-repo composites are explicitly scoped; no scholarly priority asserted.
