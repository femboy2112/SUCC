# Joint onset and dimension in the forcing discrimination threshold

**D4.6 (paper proof).** At the critical window of $2d+1$ readouts, let $e_{N,d}(r)$ be the minimax error for the geometric absolute-error envelope $r^k$, $r>0$, on the authenticated four-pole forcing $m_k=r_{\rm BBP}(N+k)$. This is the Christoffel minimum $\min_{\deg p\le d,\,p(-r)=1}\int |p|^2d\nu_N$. The variable $r$ in this note describes the instrument. The symbol $r_{\rm BBP}$ denotes the forcing in [D4.0](ARITHMETIC_FRONTIER.md). Classical Jacobi polynomials compute the comparison minimum below. This gives uniform finite bounds and a joint exponential rate when the onset and the rival dimension grow together.

For every pair of integers $N\ge1$, $d\ge1$ put $\alpha=N-7/8$ and
$$
\begin{aligned}
J_j&=\sum_{k=0}^j
 {j+\alpha-1\choose j-k}{j+1\choose k}
 (1+r)^{j-k}r^k,\\
A_j&=(2j+\alpha+1)(j+\alpha)/(j+1),\qquad
K_d=\sum_{j=0}^d A_j J_j^2 .
\end{aligned}
$$
Here the generalized binomial is the falling product divided by the integer lower factorial, with empty product one. Every term displayed is strictly positive. Then
$$
\frac{15}{64K_d}<e_{N,d}(r)<\frac{1}{2K_d}. \tag{1}
$$
For fixed $r>0$ a single $d$th-degree sum gives a two-sided estimate uniform in **both** $N$ and $d$:
$$
 A_d J_d^2\le K_d\le C_r A_d J_d^2,\quad
 C_r=64\sum_{h\ge0}(h+1)^3(1+r)^{-2h}<\infty. \tag{2}
$$
The constant in (2) is deliberately conservative. Formula (1) retains the full finite sum for greater resolution.

**Proof of (1).** The inherited source density satisfies strict pointwise bounds $15w/64<d\nu_N/du<w/2$ on $(0,1)$, where $w(u)=u^{\alpha-1}(1-u)$. Apply the lower comparison to the source minimizer and the upper comparison to the $w$ minimizer. Strictness follows since the polynomials equal one at $-r$ and have only finitely many roots. It remains to evaluate the minimum for $w$. [Source density and monic norm, PA-05](../../../docs/principia_observatoris/06_succ_applications.md).

For each $j$ take the Rodrigues polynomial
$$
Q_j(u)=\frac{(-1)^j}{j!w(u)}
 \frac{d^j}{du^j}\{u^{j+\alpha-1}(1-u)^{j+1}\}.
$$
Its Leibniz expansion is
$$
Q_j(u)=\sum_{k=0}^j{j+\alpha-1\choose j-k}{j+1\choose k}
                   (u-1)^{j-k}u^k .
$$
Thus $Q_j(-r)=(-1)^jJ_j$. The $j$ integrations by parts establish orthogonality to every smaller degree, since derivatives through order $j-1$ of the bracket vanish at both endpoints for $\alpha>0$. Its leading coefficient is $\prod_{i=1}^j(j+\alpha+i)/j!$ by expanding the numerator before differentiating and taking the highest power; equivalently this is the binomial convolution of the expansion coefficients. The squared monic norm from PA-05 is
$$
 \frac{j!(j+1)!}{(2j+\alpha+1)(j+\alpha)\prod_{i=1}^j(j+\alpha+i)^2}.
$$
Multiplication by the squared leading coefficient gives $\int Q_j^2w=1/A_j$, also for $j=0$ by direct integration. Expand a degree-at-most-$d$ polynomial in this orthogonal basis. Cauchy–Schwarz for the single constraint $p(-r)=1$ gives squared norm at least $1/K_d$, with equality at the coefficient vector proportional to $(A_jQ_j(-r))_{0\le j\le d}$. This proves (1).

**Proof of (2).** Compare each $k\le j$ term for $J_{j+1}$ with the same $k$ in $J_j$. The new first binomial contributes factor $(j+\alpha)/(j+1-k)$, the second contributes $(j+2)/(j+2-k)$, and the exterior power contributes $1+r$. Thus $J_{j+1}/J_j\ge(1+r)(j+\alpha)/(j+1)$. Write $d=j+h$. For $\alpha\ge1$, iteration gives $J_d/J_j\ge(1+r)^h$. For $1/8\le\alpha<1$ each factor $(j+i+\alpha)/(j+i+1)$ increases with $j$ and $\alpha$. The product of the $h$ such factors is at least $1/[8(h+1)]$: for $h\ge1$ take its first factor at least $1/8$ and the rest at least $\prod_{i=1}^{h-1}i/(i+1)=1/h$. For $h=0$ the empty product is one. Finally $A_j/A_d\le(d+1)/(j+1)\le h+1$. Summing $A_jJ_j^2/(A_dJ_d^2)$ over $h=0,\ldots,d$ yields (2).

**D4.7 (joint rate).** Fix $r>0$. Along any integer sequence $d\to\infty$ and $N/d\to\kappa$ with $0\le\kappa<\infty$,
$$
\lim \frac{\log e_{N,d}(r)}{d}=-2F(p_*),
$$
where $H(x)=-x\log x-(1-x)\log(1-x)$ with endpoint values zero and
$$
F(p)=(1+\kappa)H\!\left(\frac{1-p}{1+\kappa}\right)
       +H(p)+(1-p)\log(1+r)+p\log r .
$$
The unique maximizer $p_*\in(0,1)$ is the positive solution of
$$
 p_*^2+[2r+(1+r)\kappa]p_*-r=0.
$$
The bit slope per added dimension is $2F(p_*)/\log 2$ for this growing sequence of authenticated sources. For $\kappa=0$, $\exp F(p_*)=(\sqrt r+\sqrt{1+r})^2$, recovering D4.4 even when $N$ tends to infinity sublinearly in $d$.

**Proof.** To replace the generalized binomial in $J_d$ with an integer one, set $M=d+N-1$, so $d+\alpha-1=M-7/8$. For every $0\le l\le d$,
$$
\frac{1}{8(d+1)}{M\choose l}
\le {M-7/8\choose l}\le {M\choose l}.
$$
Its ratio to the integer binomial is the product of $1-7/(8a)$ over the $l$ distinct consecutive positive integers $M-l+1,\ldots,M$. For $l\ge1$ the smallest product occurs at $1,\ldots,l$ and is at least $(1/8)\prod_{a=2}^l(a-1)/a=1/(8l)$. The empty case is immediate. Also $1\le{d+1\choose k}/{d\choose k}\le d+1$. These replacements therefore introduce only $O(\log d)$ in the log of each summand, uniformly in $k$.

The integer estimate $\log{m\choose l}=m H(l/m)+O(\log(m+1))$ is uniform for $0\le l\le m$. One elementary proof takes the binomial law at success probability $l/m$. Its mode is $l$ by successive probability ratios, and its peak probability lies between $1/(m+1)$ and $1$. The endpoint laws are point masses. As $M/d\to1+\kappa$, uniform continuity of entropy on the closed interval now makes the log of the $k$th summand divided by $d$ equal to $F(k/d)+o(1)$ uniformly. A sum of $d+1$ positive terms lies between its largest term and $(d+1)$ times that term. Dense mesh and continuity therefore give $\log J_d/d\to\max_{[0,1]}F$. Since $\log A_d/d\to0$, (1)–(2) give the asserted exponent. Strict concavity and
$$
F'(p)=\log\!\left(\frac{r(1-p)^2}{(1+r)p(\kappa+p)}\right)
$$
give the stated quadratic and uniqueness. At $\kappa=0$, substituting $p_*=\sqrt r/(\sqrt r+\sqrt{1+r})$ yields the displayed value. ∎

For all $N,d$ formula (1) applies directly. The rate proof assumes fixed $r$ and a finite limiting ratio $N/d$ and gives logarithmic accuracy. It does not supply a uniform relative prefactor or a rate for $N/d\to\infty$. The [exact probe](joint_precision_probe.py) compares these positive sums with a different finite calculation using beta and four-pole Gram systems. [Receipt](receipts/joint_precision.json).
