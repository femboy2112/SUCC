# Academic Main VII: independent reconstruction of the primitive abc moment

Date: 2026-10-20. Reviewed input: PR #208,
`1c6f2adfe3ebbd1dc6613e9adb4e95bdef2f3e29`; review checkout:
`176d7f0fff8e9c7fae290e545376bac4cefe05ac`. This document concerns that
mathematical input, not an assertion that this checkout passed repository-wide
validation. It changes no previous claim identifier or archived source.

**Verdict: SURVIVES, PROVED LOCAL**, in the repository's paper-proof sense.
CLOUD-ABC-01 and CLOUD-ABC-05 have the domains stated below. Their argument
is reconstructed here; finite tests are not its universal authority.
Independent agent review is a separate same-model proof audit, not external
refereeing, a formal proof, or evidence of academic originality.

## 1. Objects and exact claims

For a positive integer $n$, let $\operatorname{rad}(n)$ be the product of
its distinct prime divisors and $r(n)=n/\operatorname{rad}(n)$, with
$\operatorname{rad}(1)=r(1)=1$. For real $X\ge2$, sum over **ordered**
positive integer triples $a+b=c\le X$, $\gcd(a,b)=1$, and put

\[
 H=r(abc),\qquad S_t(X)=\sum H^t.
\]

For every real $0\le t<2/3$, the reconstructed conclusions are

\[
 S_t(X)\le K_tX^2\quad\hbox{for every real }X\ge2,
 \qquad \lim_{X\to\infty}\frac{S_t(X)}{X^2}=C_t,
\]

where the following finite constants depend on $t$ alone:

\[
\begin{split}
A_p(t)&=\frac{p^t-1}{p^2(1-p^{t-1})},\quad
E_3(t)=\prod_p(1+3A_p(t)),\\
\eta_t&=(2/3-t)/2,\quad
B_\eta=\prod_p\left(1+\frac{2}{p(p^\eta-1)}\right),\\
K_t&=2E_3(t)+\frac{2B_{\eta_t}}{2/3-t},\\
C_t&=\frac1{2\zeta(2)}\prod_p\left(1+\frac{3p}{p+1}A_p(t)\right).
\end{split}
\]

The product for $C_t$ converges even for $t<1$; that wider convergence
does not extend the proved mean-value domain. Integer abc, RH, Goldbach,
the endpoint $t=2/3$, and academic priority remain unproved here.

## 2. The load-bearing determinant and packing invariant

Fix pairwise-coprime positive integers $d,e,f$, and write $D=def$.
Let $N_X(d,e,f)$ count the above primitive triples with $d\mid a$,
$e\mid b$, $f\mid c$. A primitive triple has
$\gcd(a,c)=\gcd(b,c)=1$. Consequently $a/c$ is reduced, and equality of
two such slopes forces equality of both numerator and denominator. For
example, from $ac'=a'c$, Euclid's lemma gives $c\mid c'$ and
$c'\mid c$; positivity gives $c=c'$, then $a=a'$ and $b=b'$.

For distinct triples the determinant

\[
 \Delta=ac'-a'c=ab'-a'b
\]

is nonzero. The first expression is divisible by $d$ and $f$; the
second is divisible by $e$. Pairwise coprimality implies $D\mid\Delta$,
so $|\Delta|\ge D$. Hence distinct slopes in $(0,1)$ have distance at
least $D/(cc')\ge D/X^2$. Sorting their finite set yields
$(N_X-1)D/X^2<1$ when it is nonempty. Thus uniformly in all moduli,

\[
 N_X(d,e,f)\le1+X^2/D.
\]

This is a finite packing argument, not a fixed-modulus asymptotic. Its
consequence $N_X\le2X^2/D$ is licensed only when $D\le X^2$.
When $D>X^2$, the original separation proves $N_X\le1$, not zero.

## 3. Positive powerful-divisor expansion

The multiplicative function $f_t(n)=r(n)^t$ satisfies $f_t=1*g_t$
under **Dirichlet** convolution, because prime-power telescoping gives

\[
 g_t(1)=1,\quad g_t(p)=0,\quad
 g_t(p^k)=p^{t(k-1)}-p^{t(k-2)}\quad(k\ge2).
\]

For $t\ge0$ these coefficients are nonnegative. Every nonzero
coefficient other than at 1 is supported on powerful integers. At $t=0$,
all coefficients except $g_0(1)$ vanish. On a primitive triple the three
slots are pairwise coprime; a prime can occupy at most one divisor slot.
For $t<1$, summing the prime-power geometric series gives

\[
 \sum_{k\ge2}g_t(p^k)p^{-k}=A_p(t),\qquad
 \sum_{(d,e)=(e,f)=(f,d)=1}\frac{g_t(d)g_t(e)g_t(f)}{def}=E_3(t).
\]

First expand finite prime/exponent supports, then use monotone convergence.
The bound $A_p(t)\le p^{t-2}/(1-2^{t-1})$ proves convergence for $t<1$.
No additive convolution is substituted for Dirichlet convolution here.

## 4. Low weights absorb the singleton lawfully

If a divisor term contributes, $D=def$ is powerful and divides $abc$.
Prime by prime, $D\le r(D)^2$ and $r(D)\mid r(abc)=H$, so $D\le H^2$.
On the low-weight subset $H\le X$, this gives $D\le X^2$. Expand the
weight, interchange finite nonnegative sums, then enlarge each count by
removing the low-weight restriction. Section 2 applies on precisely its
valid domain:

\[
 \sum_{H\le X}H^t\le
 \sum_{D\le X^2}g_t(d)g_t(e)g_t(f)\frac{2X^2}{D}
 \le2E_3(t)X^2.
\]

All sums over divisor triples in this document impose pairwise
coprimality unless otherwise indicated. This step permits moving divisors
up to $D=X^2$ because its bound is uniform, not because CRT is exact.

## 5. A different argument handles the high weights

For any real $\eta>0$, unique factorization and monotone convergence give

\[
 \sum_{\gcd(m,n)=1}\frac{(mn)^{-\eta}}
 {\operatorname{rad}(m)\operatorname{rad}(n)}=B_\eta<\infty.
\]

The two possible occupied slots give the stated local factor. Its excess
is at most $2p^{-1-\eta}/(1-2^{-\eta})$. For real $R>0,X\ge1$, each
pair with $m,n\le X$ and radical product at most $R$ contributes at
least 1 to $RX^{2\eta}$ times this sum. Its cardinality is therefore at
most $B_\eta RX^{2\eta}$.

Let $T_X(y)=\#\{H>y\}$. Such a triple has
$\operatorname{rad}(abc)=abc/H<X^3/y$. Among its three pairwise radical
products, at least one is at most $(X^3/y)^{2/3}$: their product is
$\operatorname{rad}(abc)^2$. Each selected ordered pair determines at
most one triple. All coordinates are at most $X$, so the union bound
over the three coordinate pairs proves, uniformly in $y>0,X\ge2$,

\[
 T_X(y)\le3B_\eta X^{2+2\eta}y^{-2/3}.
\]

For $0<t<2/3$, the finite layer-cake identity is

\[
 \sum_{H>X}H^t=X^tT_X(X)+t\int_X^\infty y^{t-1}T_X(y)\,dy.
\]

Inserting the majorant and integrating the convergent power gives

\[
 \sum_{H>X}H^t\le
 \frac{2B_\eta}{2/3-t}X^{2+2\eta+t-2/3}.
\]

At $\eta=\eta_t$ the exponent is exactly 2. At $t=0$, use the
cardinality $T_X(X)$ directly; no $0\cdot\infty$ expression is used.
Together with Section 4 this proves CLOUD-ABC-01. Fully elementary bounds
are $E_3(t)\le\exp(3/((1-t)(1-2^{t-1})))$ and
$B_\eta\le\exp(2/(\eta(1-2^{-\eta})))$, by integral comparison of
convergent integer power sums. They are finite but numerically very loose.

## 6. Actual global primitivity in the fixed-divisor density

Fix $d,e,f$, then fix a finite prime cutoff $P$ containing every prime
divisor of $D$. Impose the divisor conditions and exclude common prime
divisors through $P$. At an occupied $p^k\Vert D$, its local density is
$p^{-k}(1-p^{-1})$: the other summand must be a unit. If the occupied slot
is $c$, the determinant-one change $(a,b)\mapsto(a,a+b)$ gives the same
calculation. At unoccupied primes the density is $1-p^{-2}$.

CRT multiplies these **finite** densities. For this fixed modulus, count
each residue class in the triangle by cells; the boundary contributes
$O_P(X+1)$. Its normalized count tends to half its residue density.
The count that survives finite primitivity but fails actual primitivity is
at most the sum of counts with $p\mid a,b$, $p>P$. Scaling by $p$
shows each is at most $X^2/(2p^2)$. Therefore the normalized excess is at
most $\frac12\sum_{p>P}p^{-2}\le1/(2\lfloor P\rfloor)$.

First let $X\to\infty$ for fixed $P,d,e,f$, then let $P\to\infty$.
The absolutely convergent product yields

\[
 \lim_{X\to\infty}\frac{N_X(d,e,f)}{X^2}
 =\frac1{2\zeta(2)D}\prod_{p\mid D}\frac p{p+1}.
\]

The factor $p/(p+1)$ is $(1-1/p)/(1-1/p^2)$. There is no simultaneous
growing-modulus limit in this proof. The new arithmetic research will give
a separate uniform quantitative proof, not retroactively attribute one to
this argument.

## 7. Full mean: the order of limits is controlled

Fix real $t<s<2/3$ with $t\ge0$, and an integer $L\ge1$. Truncate
each divisor sum at $d\le L$, obtaining $S_{t,L}(X)$. On $H\le\sqrt L$
all supported divisors are at most $H^2\le L$, so truncation loses
nothing. Otherwise its loss is at most $H^t\le L^{-(s-t)/2}H^s$. Thus
simultaneously for every real $X\ge2$,

\[
 0\le(S_t(X)-S_{t,L}(X))/X^2\le K_sL^{-(s-t)/2}.
\]

For fixed $L$, Section 6 may be applied to each of finitely many terms.
It gives the limit

\[
 C_{t,L}=\frac1{2\zeta(2)}\sum_{d,e,f\le L}
 \frac{g_t(d)g_t(e)g_t(f)}{D}\prod_{p\mid D}\frac p{p+1}.
\]

The nonnegative series is dominated by $E_3(t)$; its Euler factors give
$C_t$. Applying the uniform truncation bound to $L'>L$, taking their
fixed finite limits, then letting $L'\to\infty$, gives
$0\le C_t-C_{t,L}\le K_sL^{-(s-t)/2}$. Consequently

\[
 \left|S_t(X)/X^2-C_t\right|\le
 \left|S_{t,L}(X)/X^2-C_{t,L}\right|+2K_sL^{-(s-t)/2}.
\]

Choose $L$ first, then $X$. This proves CLOUD-ABC-05 without assuming
the desired convergence as an input. At $t=0$, the correct calibration is
$S_0(X)=\sum_{2\le c\le X}\varphi(c)$, not a sum including $c=1$.
The omission changes no limit.

## 8. Adversarial boundary and source comparison

* Removing primitivity admits $(n,n,2n)$, with $r(2n^3)\ge n^2$, and
  produces growth at least a constant times $X^{1+2t}$. The quadratic
  bound is false on that larger domain for $t>1/2$.
* Removing the singleton term is false on powerful support:
  $(a,b,c)=(441,400,841)$, $D=abc$, has $N_{841}=1$ but
  $2\cdot841^2/D<1$.
* The pairwise-coprime moduli $(8,9,17)$ at $X=34$ count two
  nonprimitive triples, exceeding $1+34^2/(8\cdot9\cdot17)=35/18$.
  Distinct multiples of one slope defeat primitive injectivity.
* At $t=2/3$, this majorant has a logarithmically divergent integral and
  the chosen $\eta=0$ has no convergent product. This refutes an endpoint
  extension **by these estimates**, not the endpoint theorem itself.
* The convergence of the Euler product for $t<1$ is insufficient without
  uniform integrability. No mean or bound on $[2/3,1)$ is asserted.

The primary source Bernert--Browning--Lichtman--Teräväinen,
[arXiv:2410.12234v2](https://arxiv.org/abs/2410.12234v2), revised 9 May 2026,
concerns radical-sublevel exceptional counts, with Fourier and geometric
arguments. None of its analytic estimates is imported by this proof. The
fact that the domains overlap does not identify its exceptional count
with this weighted moment. Its exponent-layer regrouping is also not
needed here. The machinery above uses classical unique factorization,
Farey separation, Rankin's trick, CRT, and uniform integrability.
The moment result is a **new-to-project synthesis**; academic novelty is
**UNVERIFIED** pending substantial literature comparison and external review.

## 9. Review boundaries and integration recommendation

This reconstruction checks all claimed quantifiers, constants, limiting
orders and the prime-slot normalization. It finds no mathematical blocker
to integrating CLOUD-ABC-01/05 with their existing paper-proof status.
It does not certify any executable proof-authority interface. The original
finite census is supporting evidence only. A separate reviewer has been
asked to check the new uniform counting argument and the existing theorem;
its own receipt must state actual completed checks. The formal-mathematics
lane owns any Lean determinant/injectivity proof and its actual build logs.

The next decisive probe is an explicit, uniform bound for the finite
divisor truncation term above. That is a quantitative **pathway gap** in
the old result, not an access gap or a demonstrated theorem boundary.
Endpoint progress additionally needs a stronger additive high-weight
estimate or a different treatment of high-determinant singleton strata.
