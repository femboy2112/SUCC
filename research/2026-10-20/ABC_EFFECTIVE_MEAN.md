# Primitive slope rigidity and effective weighted abc-triple means

**Draft manuscript and research dossier — 20 October 2026.**
Not submitted or published. Paper proofs below are PROVED LOCAL under
the repository's claim vocabulary. They are not fully formalized.
Academic novelty is UNVERIFIED; independent external refereeing is
still required. This review and the hostile review are separate
same-model agent analyses, not independent human referees.

## Abstract

We count ordered positive primitive solutions of $a+b=c\le X$, weighted
by $(abc/\operatorname{rad}(abc))^t$. A powerful-divisor expansion and
primitive slope separation give a quadratic moment bound for
$0\le t<2/3$. We prove a uniform absolute error of order $X\log X$ for
primitive triples satisfying three pairwise-coprime divisor conditions,
with an explicit constant independent of the divisors. A product cutoff
then gives an effective Euler-product mean. For each fixed
$0\le t<2/3$ and $0<\delta<(2-3t)/5$, the normalized mean differs from
its limit by at most $C_{t,\delta}X^{-\delta}$. All constants below are
explicit. The endpoint $t=2/3$ remains unresolved by this argument.

## 1. Statements, domains, and dependencies

Let $\operatorname{rad}(n)$ be the product of the distinct prime factors of
a positive integer $n$, and put $r(n)=n/\operatorname{rad}(n)$. Both
functions have value 1 at 1. All triple sums below are ordered and run over
positive integers $a+b=c\le X$ with $\gcd(a,b)=1$, where $X\ge2$ is real.
Write

$$
 H=r(abc),\qquad S_t(X)=\sum_{\substack{a+b=c\le X\\(a,b)=1}}H^t .
$$

For $0\le t<1$ define

$$
 A_p(t)=\frac{p^t-1}{p^2(1-p^{t-1})},\quad
 E_3(t)=\prod_p(1+3A_p(t)),\quad
 C_t=\frac1{2\zeta(2)}
       \prod_p\left(1+\frac{3p}{p+1}A_p(t)\right).
$$

For $\eta>0$ define $B_\eta=\prod_p(1+2/[p(p^\eta-1)])$.
For $0\le s<2/3$, put

$$
 K_s=2E_3(s)+\frac{2B_{(2/3-s)/2}}{2/3-s}.
$$

For $\alpha>t$ and $2\alpha-t>1$, set

$$
 E(t,\alpha)=
 \prod_p\left(1+
 \frac{3(p^t-1)p^{-2\alpha}}{1-p^{t-\alpha}}\right).
$$

Every product used in its declared domain converges; proofs are below.
The analytic dependencies are elementary integration and absolutely or
monotonically convergent series. No exceptional-set theorem, unproved
abc estimate, conjectural local independence, or zero-location data is used.

**Theorem 1 (ABC-EFF-01: uniform primitive divisor count).**
For every real $X\ge2$ and all pairwise-coprime positive integers $d,e,f$,
let $D=def$, $M=\lfloor X/2\rfloor$ and $H_M=\sum_{k=1}^M k^{-1}$.
Let $N_X(d,e,f)$ count the primitive triples with $d\mid a$,
$e\mid b$, $f\mid c$. Then

$$
 \left|N_X(d,e,f)-\frac{X^2}{2\zeta(2)D}
             \prod_{p\mid D}\frac p{p+1}\right|
 \le \frac32 XH_M+\frac{X^2}{2M}.                    \tag{1}
$$

The error is independent of $d,e,f$, even when they vary with $X$.
It is an **absolute** error, not a relative asymptotic for arbitrary
moving moduli or arbitrarily sparse congruence conditions.

**Theorem 2 (ABC-EFF-02: finite cutoff transfer).**
Fix real $0\le t<s<2/3$ and $\alpha>t$ with $2\alpha-t>1$.
For every real $X\ge2,Y\ge1$,

$$
 \left|\frac{S_t(X)}{X^2}-C_t\right|
 \le E(t,\alpha)\left(\frac{3H_{\lfloor X/2\rfloor}}{2X}
                 +\frac1{2\lfloor X/2\rfloor}\right)Y^\alpha
       +2K_sY^{-(s-t)/2}.                           \tag{2}
$$

**Theorem 3 (ABC-EFF-03: effective mean-value convergence).**
Fix $0\le t<2/3$ and $0<h<2/3-t$. Set

$$
 s=2/3-h,\quad \alpha=(1+t+h)/2,\quad
 r=\frac{2-3t-3h}{5},\quad
 Q_{t,h}=\frac72 E(t,\alpha)+2K_s.
$$

Then $r>0$ and, for every real $X\ge2$,

$$
 \boxed{\left|\frac{S_t(X)}{X^2}-C_t\right|
       \le Q_{t,h}\left(\frac{1+\log X}{X}\right)^r.} \tag{3}
$$

In particular for every $0<\delta<(2-3t)/5$ the explicit constant
specified in Section 6 satisfies

$$
 \left|S_t(X)/X^2-C_t\right|\le C_{t,\delta}X^{-\delta}
 \quad\hbox{for all real }X\ge2.                     \tag{4}
$$

These are new-to-project quantitative conclusions. No optimality of
exponent or constant is asserted. At $t=0$, summatory totient estimates
are substantially sharper.

## 2. A self-contained quadratic moment bound

Here is the elementary argument used as input to (2). The detailed
integration review is [ACADEMIC_VII_ABC_REVIEW.md](ACADEMIC_VII_ABC_REVIEW.md).
Its historical identifiers are CLOUD-ABC-01/02/04/05.

**Powerful expansion.** The multiplicative function defined by

$$
 g_t(1)=1,\quad g_t(p)=0,\quad
 g_t(p^k)=p^{t(k-1)}-p^{t(k-2)}\quad(k\ge2)
$$

satisfies $r(n)^t=\sum_{d\mid n}g_t(d)$ by prime-power telescoping.
For $t\ge0$ its terms are nonnegative and supported on powerful integers.
At $t=0$ only $g_0(1)$ is nonzero. A primitive triple is pairwise coprime,
so its three divisor slots are pairwise coprime: a prime may occupy at
most one slot. Summing the geometric series gives

$$
 \sum_{\substack{d,e,f\ge1\\(d,e)=(d,f)=(e,f)=1}}
 \frac{g_t(d)g_t(e)g_t(f)}{def}=E_3(t).
$$

Indeed $\sum_{k\ge2}g_t(p^k)/p^k=A_p(t)$ and
$A_p(t)\le p^{t-2}/(1-2^{t-1})$. Finite prime/exponent expansions and
monotone convergence justify the identity and convergence for $t<1$.

**Slope separation.** A primitive triple maps injectively to its reduced
fraction $a/c\in(0,1)$. For completeness, $ac'=a'c$ and the coprimality
conditions force $c\mid c'$ and $c'\mid c$; positivity gives equality of
denominators and then of all coordinates. Two distinct fractions have
nonzero determinant $ac'-a'c=ab'-a'b$, divisible by $d,f,e$, hence by
$D=def$. Their distance is at least $D/X^2$. Sorting the finite set proves
$N_X(d,e,f)\le1+X^2/D$, uniformly in all moduli. In particular
$N_X\le2X^2/D$ if $D\le X^2$.

**Low weights.** For a nonzero divisor term, $D$ is powerful and divides
$abc$. Prime by prime, $D\le r(D)^2\le H^2$. On $H\le X$, all contributing
terms satisfy $D\le X^2$. Positivity and the packing bound give
$\sum_{H\le X}H^t\le2E_3(t)X^2$.

**Radical tail.** Unique factorization gives, for $\eta>0$,

$$
 \sum_{(m,n)=1}
 \frac{(mn)^{-\eta}}{\operatorname{rad}(m)\operatorname{rad}(n)}
 =B_\eta .
$$

Its prime factor excess is at most $2p^{-1-\eta}/(1-2^{-\eta})$,
proving convergence. Hence the number of coprime pairs $m,n\le X$ with
radical product at most $R$ is at most $B_\eta RX^{2\eta}$: each counted
pair contributes at least 1 to $RX^{2\eta}$ times the preceding sum.
If $H>y$, then $\operatorname{rad}(abc)<X^3/y$, so one of its three
pairwise radical products is at most $(X^3/y)^{2/3}$. Each pair determines
at most one triple. Consequently

$$
 T_X(y):=\#\{H>y\}\le3B_\eta X^{2+2\eta}y^{-2/3}.
$$

For $0<t<2/3$, finite layer-cake integration gives

$$
 \sum_{H>X}H^t
 =X^tT_X(X)+t\int_X^\infty y^{t-1}T_X(y)\,dy
 \le\frac{2B_\eta}{2/3-t}X^{2+2\eta+t-2/3}.
$$

Choosing $\eta=(2/3-t)/2$ proves $S_t(X)\le K_tX^2$.
For $t=0$ the high contribution is $T_X(X)$ directly.
This proves the moment bound on the full real-cutoff domain.

## 3. Uniform raw lattice count by slicing

Let $M_X(d,e,f)$ impose the three divisor conditions without primitivity;
here $X\ge0$ is any real number. Write $a=du$ and $n=\lfloor X/d\rfloor$.
Since $(e,f)=1$, the condition $b=ev$ and $f\mid du+ev$ puts $v$ in one
residue class modulo $f$. Its positive row count differs from
$(X-du)/(ef)$ by at most 1, including empty rows. Thus

$$
 \left|M_X(d,e,f)-\frac1{ef}\sum_{u=1}^n(X-du)\right|
 \le n\le X/d.
$$

Put $X=d(n+\theta)$, $0\le\theta<1$. Exact algebra gives

$$
 \frac{X^2}{2d}-\sum_{u=1}^n(X-du)
 =\frac d2(n+\theta^2)\in[0,X/2].
$$

This formula includes $n=0$. Therefore, uniformly over all moduli,

$$
 \boxed{\left|M_X(d,e,f)-\frac{X^2}{2def}\right|
        \le\frac Xd+\frac{X}{2ef}\le\frac32X.}       \tag{5}
$$

This special three-divisor lattice avoids summing a general residue-set
boundary error over all permitted residue classes. It complements the
general CRT/Möbius machinery without a moving-modulus asymptotic.

## 4. Full Möbius inversion: proof of Theorem 1

For positive $a,b$ with $a+b\le X$, a common divisor is at most
$M=\lfloor X/2\rfloor$. The exact identity
$1_{\gcd(a,b)=1}=\sum_{k\mid a,\ k\mid b}\mu(k)$ yields

$$
 N_X(d,e,f)=\sum_{k\le M}\mu(k)
 M_{X/k}\left(\frac d{(d,k)},\frac e{(e,k)},\frac f{(f,k)}\right). \tag{6}
$$

The reduced moduli are pairwise coprime. Their product is $D/(D,k)$
because the original slots have disjoint prime support. Formula (5) gives

$$
 \left|N_X(d,e,f)-
 \frac{X^2}{2D}\sum_{k\le M}\frac{\mu(k)(D,k)}{k^2}\right|
 \le\frac32XH_M.                                     \tag{7}
$$

The infinite series is absolutely convergent for each $D$, since
$(D,k)\le D$. Its Euler factor is $1-p^{-1}$ when $p\mid D$ and
$1-p^{-2}$ otherwise. Therefore

$$
 \frac1D\sum_{k\ge1}\frac{\mu(k)(D,k)}{k^2}
 =\frac1{\zeta(2)D}\prod_{p\mid D}\frac p{p+1}.        \tag{8}
$$

After dividing by $D$, its tail is uniformly bounded:

$$
 \frac1D\left|\sum_{k>M}\frac{\mu(k)(D,k)}{k^2}\right|
 \le\sum_{k>M}k^{-2}\le\frac1M.                       \tag{9}
$$

Equations (7)--(9) prove (1). There is no hidden constant depending on
$D,X$, or a chosen prime cutoff. This independently supplies actual
global primitivity rather than primitivity at finitely many primes.

**Minimal hostile shortcut (ABC-EFF-04, REFUTED inference).**
Keeping only $(k,D)=1$ in (6), while keeping unmodified divisor
conditions, is false. At $X=4,(d,e,f)=(2,1,1)$, it returns 2
from $(a,b)=(2,1),(2,2)$; the actual primitive count is 1.
The omitted $k=2$ term is necessary. Separately imposing local unit
conditions at primes dividing $D$ gives a different, potentially valid
formula; this counterexample does not refute that procedure.

## 5. Product cutoff: proof of Theorem 2

Write $w_t(d,e,f)=g_t(d)g_t(e)g_t(f)$ on pairwise-coprime triples.
In every divisor sum in this section pairwise coprimality is imposed.
Define the finite **product** cutoff

$$
 S_{t,Y}(X)=\sum_{\substack{d,e,f\ge1\\def\le Y}}w_t(d,e,f)N_X(d,e,f),
$$

and define $C_{t,Y}$ by replacing $N_X/X^2$ with the density in (1).
This differs from an individual-slot cutoff $d,e,f\le L$.
If $H\le\sqrt Y$, every supported divisor product satisfies $D\le H^2\le Y$.
On the complementary set the lost weight is at most
$H^t\le Y^{-(s-t)/2}H^s$. Thus

$$
 0\le\frac{S_t(X)-S_{t,Y}(X)}{X^2}
       \le K_sY^{-(s-t)/2}                           \tag{10}
$$

uniformly for all $X\ge2,Y\ge1$.

The nonnegative coefficient series $\sum w_t(d,e,f)/D^\alpha$ has local
factor $1+3(p^t-1)p^{-2\alpha}/(1-p^{t-\alpha})$. It converges under
$\alpha>t$, $2\alpha-t>1$, since its excess is at most
$3p^{-(2\alpha-t)}/(1-2^{t-\alpha})$.
Its sum is $E(t,\alpha)$ by monotone convergence. Hence

$$
 \sum_{D\le Y}w_t(d,e,f)\le Y^\alpha E(t,\alpha).      \tag{11}
$$

Multiplying (1) by the nonnegative coefficients gives

$$
 \left|S_{t,Y}(X)/X^2-C_{t,Y}\right|
 \le\left(\frac{3H_M}{2X}+\frac1{2M}\right)
       Y^\alpha E(t,\alpha).                        \tag{12}
$$

For fixed $Y$, (1) proves convergence of this finite sum.
The constants $C_{t,Y}$ increase to $C_t$: their series at exponent 1
is dominated by $E_3(t)$, with precisely the prime factors defining $C_t$.
For fixed $Y'>Y$, apply (10) to $S_{t,Y'}-S_{t,Y}$ and let $X\to\infty$,
then $Y'\to\infty$. This proves

$$
 0\le C_t-C_{t,Y}\le K_sY^{-(s-t)/2}.                \tag{13}
$$

The limiting argument does not assume the full mean-value theorem;
only finite sums have been sent to the limit. The triangle inequality
in (10), (12), (13) proves (2), including its factor 2.

## 6. Optimize the cutoff: proof of Theorem 3

For $X\ge2$, $M=\lfloor X/2\rfloor\ge X/4$ and $H_M\le1+\log X$, so

$$
 \frac{3H_M}{2X}+\frac1{2M}
 \le\frac72\,\frac{1+\log X}{X}.                     \tag{14}
$$

Fix $h$ as in Theorem 3 and put $\beta=(s-t)/2$. Then
$\alpha>t$, $2\alpha-t-1=h>0$, and $\alpha+\beta=5/6$.
Since $X/(1+\log X)\ge1$ for $X\ge1$, the admissible choice

$$
 Y=\left(\frac X{1+\log X}\right)^{6/5}
$$

balances both powers in (2). Both become
$((1+\log X)/X)^{\beta/(\alpha+\beta)}$, with
$\beta/(\alpha+\beta)=(2-3t-3h)/5$. This proves (3).
Real $Y$ causes no ambiguity: $D\le Y$ has the usual integer meaning,
already permitted in Theorem 2.

For the pure power form let $\delta_*=(2-3t)/5$ and fix
$0<\delta<\delta_*$. Set $r=(\delta+\delta_*)/2$,
$h=5(\delta_*-r)/3$ and $\epsilon=r-\delta$.
All preceding strict inequalities hold. Maximizing
$(1+u)^r e^{-\epsilon u}$ for $u\ge0$ gives
$e^\epsilon(r/(e\epsilon))^r$, since $0<\epsilon<r$.
An explicit valid choice is therefore

$$
 C_{t,\delta}=Q_{t,h}\,e^\epsilon
                 \left(\frac r{e\epsilon}\right)^r.
$$

The supremum exponent $\delta_*$ is not attained by this proof:
$h=0$ destroys the coefficient estimate and forces the unproved
moment at $s=2/3$.

## 7. Explicit constants and reproducibility

Decreasing-power integral comparison and $1+u\le e^u$ give

$$
\begin{split}
 E_3(s)&\le\exp\left(\frac3{(1-s)(1-2^{s-1})}\right),\\
 B_\eta&\le\exp\left(\frac2{\eta(1-2^{-\eta})}\right),\\
 E(t,\alpha)&\le
 \exp\left(\frac3{(2\alpha-t-1)(1-2^{t-\alpha})}\right).
\end{split}
$$

The code encodes larger exact powers of two for rational parameters,
using integer-root brackets and $e^u<4^u$. These constants establish
effectiveness; they are not useful numerical error bars near $t=2/3$.

Implementation:
[abc_effective_mean.py](../../observational_succ/abc_effective_mean.py).
The raw count is a row/CRT formula; the primitive count uses (6).
No floating-point comparison enters the code. Strict type guards reject
booleans and floating-point cutoffs; the real-cutoff theorem is
implemented for integers and exact fractions. Frozen dataclasses record
arithmetic budgets, not proof authority.

Focused commands from the repository root:

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest discover -s tests -p test_abc_effective_mean.py -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/abc_effective_mean_probe.py
~~~

The eleven-test suite includes independent direct $(a,b)$ enumeration,
the earlier divisor-of-$c$ Möbius route, rational cutoffs, sparse and huge
moduli, the false coprime-$k$ shortcut, product-cutoff support, exact
exponent optimization and strict input guards. The probe receipt records
actual cases, file hashes, parameters, and checkout; it is not a formal
proof receipt. A separate referee's no-project-import implementation
adds methodological separation. Counts alone do not prove (1)--(4).

## 8. Literature and priority assessment

Farey separation, Möbius inversion, elementary lattice counting, positive
Euler products and Rankin bounds are classical. This combination is new
to the project; no academic priority is claimed.

Primary sources inspected on 2026-10-20:

1. Bernert--Browning--Lichtman--Teräväinen,
   [arXiv:2410.12234v2](https://arxiv.org/html/2410.12234v2), Proposition
   1.1, Theorem 1.2 and Proposition 4.1. Their radical-sublevel exceptional
   counts use Fourier analysis and geometry. The radical-pair exponent
   $2/3$ is already in Proposition 1.1. Theorem 1.2 treats
   $0<\lambda\le2$ with exponent $(23\lambda+3)/40+\varepsilon$;
   it is not invoked for our weighted sum. The abstract lists revision
   9 May 2026; retrieved HTML displays an internal August 2026 date.
   We identify the version without inferring a revision from that
   inconsistent metadata.
2. Daniel M. Kane, *On the number of ABC solutions with restricted radical
   sizes*, [arXiv:1104.2635v2](https://arxiv.org/pdf/1104.2635),
   Theorem 2 and Section 2; J. Number Theory 154 (2015), 32--43.
   For fixed $0<a,b,c\le1$, its restrictions
   $\operatorname{rad}(A)\le|A|^a$, and analogously for $B,C$,
   on relatively prime $A+B+C=0$ of height at most $N$, give
   $O(N^{a+b+c-1+\varepsilon}+N^{1+\varepsilon})$.
   Its lattice and conic arguments are material prior art. Applying
   an $X$-dependent parameter partition would require additional
   uniform-constant analysis; no such import is asserted.
3. R. de la Bretèche and T. D. Browning, *Sums of arithmetic functions over
   values of binary forms*,
   [arXiv:math/0604119v1](https://arxiv.org/pdf/math/0604119),
   definition of $\mathcal M(A,B)$ and Theorem 1.
   It assumes $h(p^\ell)\le A^\ell$ uniformly in $p$, and subpower growth.
   For $t>0$, $h(n)=r(n)^t$ fails both: $h(p^2)=p^t$ is unbounded in $p$,
   and $h(2^k)=2^{t(k-1)}$ is not $O_\varepsilon(2^{k\varepsilon})$
   for $\varepsilon<t$. That theorem does not directly certify this
   result; this exclusion does not rule out other prior art.

Novelty remains unverified until broader comparison of multiplicative
correlations and radical moments, and external review, is complete.

## 9. Boundaries and next decisive research

1. **Primitivity is essential.** Without it, $(n,n,2n)$ has
   $r(2n^3)\ge n^2$, giving moment growth at least $X^{1+2t}$.
   The quadratic bound fails for $t>1/2$ on the enlarged domain.
2. **Absolute error does not imply relative error.** The error in (1)
   divided by its leading term can grow with $D$. The powerful moduli
   $(441,400,841)$ at $X=841$ have one primitive solution while
   $2X^2/D<1$. This also forbids deleting the packing singleton.
3. **The $2/3$ boundary is a strategy obstruction.** The tail integrates
   as $y^{-1}$ at the endpoint, and $B_\eta$ has no meaning at $\eta=0$.
   Neither is a counterexample to an endpoint moment theorem.
4. **Endpoint verdict-changing theorem.** An integrable high-weight
   estimate on the actual additive primitive family, or a summable
   bound for occupied high-determinant singleton strata, is needed.
   Finite censuses cannot supply this uniform input.
5. **Next effectiveness improvement.** Replace (1) by a weighted
   discrepancy exploiting cancellations or average moduli. Equation (2)
   specifies the quantity whose improvement increases the rate.
   No such cancellation is assumed here.

## 10. Claim and verification ledger

| ID | Statement and quantified domain | Status | Boundary |
|---|---|---|---|
| ABC-EFF-01 | (1), all real $X\ge2$, pairwise-coprime positive $d,e,f$ | PROVED LOCAL, Sections 3--4 | absolute error; paper proof |
| ABC-EFF-02 | (2), all declared $t,s,\alpha,X,Y$ | PROVED LOCAL, Section 5 | positive cutoff; stronger moment |
| ABC-EFF-03 | (3)--(4), fixed $0\le t<2/3$, strict exponent range | PROVED LOCAL, Section 6 | not optimal; no endpoint claim |
| ABC-EFF-04 | deleting shared-prime Möbius terms from (6) | REFUTED, exact $(4;2,1,1)$ | no claim about a separate local-unit sieve |
| ABC-EFF-05 | $S_t(X)/X^2\to\infty$ for every fixed $t\ge1$ | PROVED LOCAL, Appendix A | does not decide $2/3\le t<1$ |

The formal lane may check determinant divisibility and slope injectivity.
That supports one lemma, not a Lean proof of this entire argument.
Exact tests are TESTED MODEL evidence for executable arithmetic; the
universal statements rest on the proofs above. RH, integer abc, binary
Goldbach and the authentic signed $S_4$ sign are unaffected.

## Appendix A. An actual upper boundary for the moment range

The failure of the proof at $t=2/3$ does not show that a quadratic bound
is false there. At $t=1$, however, such a bound really is false.
This appendix establishes a boundary for the theorem itself, not merely
for the sufficient method.

**Theorem ABC-EFF-05.** For every fixed real $t\ge1$,
$S_t(X)/X^2\to\infty$ as the real variable $X\to\infty$. More precisely,

$$
 \liminf_{X\to\infty}\frac{S_1(X)}{X^2\log X}
       \ge\frac1{4\zeta(2)\log2}.                    \tag{15}
$$

For every real $t>1$ and every real $X\ge8$, one also has the explicit
bound

$$
 S_t(X)\ge8^{-(t+1)}X^{t+1}.                         \tag{16}
$$

**Fixed-prime proof of divergence.** For any fixed integer $K\ge2$,
retain only the three single-slot divisor terms $2^k$, $2\le k\le K$,
in the nonnegative expansion at $t=1$. Their coefficient is
$g_1(2^k)=2^{k-2}$. The normalized density for each slot is

$$
 \frac1{2\zeta(2)2^k}\frac23.
$$

Thus each term contributes $1/(12\zeta(2))$ to the finite-cutoff limit.
All three slots give

$$
 \liminf_{X\to\infty}\frac{S_1(X)}{X^2}
        \ge\frac{K-1}{4\zeta(2)}.
$$

First take the limit for fixed $K$, then let $K\to\infty$.
This proves divergence without any moving-modulus step.
Since $H\ge1$, $H^t\ge H$ for $t\ge1$, proving the same divergence
for every such $t$.

**Quantitative strengthening.** Let
$B_X=\frac32XH_{\lfloor X/2\rfloor}+X^2/(2\lfloor X/2\rfloor)$.
The uniform estimate (1) applied to the same finite expansion gives,
for every $X\ge2$ and every integer $K\ge2$,

$$
 S_1(X)\ge\frac{K-1}{4\zeta(2)}X^2
            -3(2^{K-1}-1)B_X.                      \tag{17}
$$

No positivity of the right-hand side is needed for the validity of this
lower bound. Fix $0<\alpha<1$ and let
$K=\lfloor\alpha\log_2 X\rfloor$ once this is at least 2.
Since $B_X=O(X\log X)$ and $2^K\le X^\alpha$, the error in (17) is
$o(X^2\log X)$. Consequently the left-hand side of (15) is at least
$\alpha/(4\zeta(2)\log2)$. Letting the fixed parameter $\alpha\uparrow1$
proves (15). No unproved endpoint moment is an input.

**Explicit family for (16).** Set
$a=2^{\lfloor\log_2 X\rfloor-1}$; then $X/4<a\le X/2$.
Choose every positive odd integer $b\le X-a$ and set $c=a+b$.
There are at least $X/8$ such choices when $X\ge8$. All triples are
primitive because $a$ is a power of two, and
$r(abc)\ge r(a)=a/2>X/8$. Summing their weights proves (16).

The executable lower subexpansion is checked against direct exact
first-moment censuses; the dyadic family is checked separately.
These finite checks support the formulas, not their universal proofs.
The actual unresolved range of quadratic moments is therefore contained
in $[2/3,1)$; no assertion about which point in that interval is critical
is made.
