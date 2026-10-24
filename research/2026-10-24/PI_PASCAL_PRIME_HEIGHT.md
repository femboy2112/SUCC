# Prime births, Pascal filters and the height of the authentic BBP source

**Date:** 2026-10-24.
**Parent:** [draft #270](https://github.com/femboy2112/SUCC/pull/270) at
`3acd547ff122368d5694efdab029b3156a292d8a`.
**Contract:** [Pascal / prime geometry](PI_PASCAL_HOLE_CONTRACT.md).
**Status:** elementary paper proofs below, with classical fixed-modulus
prime number theorem used only for the asymptotic height estimates.
No normality or real-close-pair saving is claimed.

The fixed forcing has prime factors which cannot disappear from a whole
initial interval after their first appearance. This excludes exact integer
locking for many translated Pascal filters. It also proves that the odd
denominators of the authentic source grow exponentially. The corresponding
real separation is exponentially small, so these facts do not supply the
polynomial-scale nonalignment needed for the open retention estimate.

## 1. Source, notation and inherited prime-birth input

Throughout,

$$
r(j)=\frac4{8j-7}-\frac1{8j-3}
-\frac1{2(2j-1)}-\frac1{2(4j-1)},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

Write $E U_n=U_{n+1}$, $\Delta=E-I$, and
$\mathbb Z_{(p)}=\{a/b\in\mathbb Q:p\nmid b\}$.
For $n\ge1$, let $D_n$ be the positive reduced denominator of $U_n$.
It is odd, as follows either from the inherited
[source isometry](PI_DYADIC_SOURCE_ISOMETRY.md) or the common-denominator
argument below. Put

$$
L_X=\mathrm{lcm}\{d\in\mathbb Z:1\le d\le X,\ d\text{ odd}\}.
$$

The $p\equiv1\pmod8$ prime-birth interval is **inherited**, specifically
[SCE-05, §6](PI_SOURCE_COLLISION_ENTROPY.md#6-sce-05--full-source-galois-collision-counting-proved-paper).
That report already retains the complete $p$-integral complement of the
actual source. The polynomial-filter corollary, the explicit
$p\equiv5\pmod8$ companion, and the combined height bookkeeping below are
the additions here. They do not constitute a new selected-embedding
collision theorem.

## 2. PH-1 — sole-birth intervals for two prime classes (PROVED)

Let $p$ be prime in one of the following classes, and define $a_p$, $B_p$
and $\gamma_p$ by the table.

| Prime class | First index $a_p$ | Last index $B_p$ before the second pole | First coefficient $\gamma_p/p$ |
|---|---:|---:|---:|
| $p\equiv1\pmod8$ | $(p+7)/8$ | $(p-1)/2$ | $4/p$ |
| $p\equiv5\pmod8$ | $(p+3)/8$ | $(p-1)/2$ | $-1/p$ |

For every integer $a_p\le n\le B_p$,

$$
U_n=\frac{\gamma_p16^{n-a_p}}p+W_{p,n},
\qquad W_{p,n}\in\mathbb Z_{(p)},
\qquad v_p(U_n)=-1.
\tag{PH-1}
$$

**Proof.** If $p\equiv1\pmod8$, the first positive multiples of $p$ in
the four odd denominator progressions $8j-7$, $8j-3$, $2j-1$, $4j-1$
are respectively $p$, $5p$, $p$, $3p$. Their indices are

$$
\frac{p+7}8,\quad\frac{5p+3}8,\quad
\frac{p+1}2,\quad\frac{3p+1}4.
$$

The first index is $a_p$, and the next is $(p+1)/2=B_p+1$.
If $p\equiv5\pmod8$, the first multiples in those progressions are
$5p$, $p$, $p$, $3p$, at indices

$$
\frac{5p+7}8,\quad\frac{p+3}8,\quad
\frac{p+1}2,\quad\frac{3p+1}4.
$$

Again the first index is $a_p$ and the second is $B_p+1$.
There is no second multiple in the progression containing the first pole
before that second index. Thus among $r(1),\ldots,r(n)$ there is precisely one pole at $p$,
of order one, with the coefficient displayed in the table. Expanding
$U_n=\sum_{j=1}^n16^{n-j}r(j)$ proves the decomposition. Since
$p\nmid16\gamma_p$, the displayed $p$-pole cannot cancel against
$W_{p,n}$. This includes $p=5$, where $a_p=1$ and $B_p=2$.
$\square$

## 3. PH-2 — integer polynomial and Pascal filters (PROVED)

Let $p,a_p,B_p,\gamma_p$ be as above. For every nonzero
$P\in\mathbb Z[X]$ of degree $d\ge0$ and every integer $n$ satisfying
$a_p\le n$ and $n+d\le B_p$,

$$
P(E)U_n
=\frac{\gamma_p16^{n-a_p}P(16)}p+W,
\qquad W\in\mathbb Z_{(p)}.
\tag{PH-2}
$$

Consequently,

$$
v_p(P(E)U_n)=
\begin{cases}
-1,&p\nmid P(16),\\
\text{at least }0,&p\mid P(16).
\end{cases}
$$

**Proof.** Apply PH-1 separately to each $U_{n+j}$ in the integer
linear combination $P(E)U_n$ and factor out
$\gamma_p16^{n-a_p}/p$. The remaining scalar is $P(16)$. The complement
stays in $\mathbb Z_{(p)}$. $\square$

In particular, for every integer $k\ge0$ with $n+k\le B_p$,

$$
p\nmid15^k
\quad\Longrightarrow\quad
v_p(\Delta^k U_n)=-1.
\tag{PH-3}
$$

For $k\ge1$ this requires $p\nmid15$; the $p=5$ case must be excluded.
For $k=0$ every prime in PH-1 is allowed. Also
$k\le B_p-n<p$, so $p\nmid k!$ and the same valuation holds for
$\Delta^k U_n/k!$. These are statements about **translated** Pascal
rows lying wholly inside the sole-birth interval. They exclude exact
integer values there; they do not count how often the values approach
integers in the real metric.

## 4. PH-3 — forcing coefficients and the source-origin cancellation guard

Define the two origin coefficients

$$
a_k=\Delta^k r(0),\qquad A_k=\Delta^k U_0.
$$

They are different objects. For $k\ge1$, suppose $p$ is prime and either

$$
\begin{aligned}
&p\equiv1\pmod8, &&2k+1\le p\le8k-7,\\
\text{or }\quad &p\equiv5\pmod8, &&2k+1\le p\le8k-3.
\end{aligned}
\tag{PH-4}
$$

Then

$$
v_p(a_k)=v_p(a_k/k!)=-1.
\tag{PH-5}
$$

**Proof.** The inequalities say $a_p\le k\le B_p$. Exactly one entry
of $r(0),\ldots,r(k)$ has a $p$-pole: the entry at $a_p$. Here
$r(0)=16/21$ is $p$-integral for the permitted prime classes. Its
coefficient in the signed Pascal row is
$(-1)^{k-a_p}\binom{k}{a_p}\gamma_p/p$.
Since $k<p$, both $\binom{k}{a_p}$ and $k!$ are $p$-units. Thus this
pole cannot cancel. $\square$

The first class has no eligible prime at $k=1$ or $k=2$; its first
nonempty example is $k=3,p=17$. The second class does include $p=5$
at $k=1,2$. The $p\nmid15$ condition from translated **source** rows
does not apply to this sole-entry **forcing** argument.

For $A_k$, several entries have inherited the first pole. For
$a_p\le k\le B_p$ its $p$-primary coefficient is instead

$$
\frac{\gamma_p}{p}
\sum_{j=a_p}^k(-1)^{k-j}\binom{k}{j}16^{j-a_p}.
\tag{PH-6}
$$

The incomplete binomial sum can vanish modulo $p$, even though $k<p$.
A concrete receipt is

$$
p=89,\quad a_p=12,\quad k=35,\qquad
\sum_{j=12}^{35}(-1)^{35-j}\binom{35}{j}16^{j-12}
\equiv0\pmod{89}.
$$

Exact rational evaluation gives $v_{89}(A_{35})=0$, whereas
$v_{89}(a_{35})=-1$. Division by $35!$ preserves both valuations.
This refutes the inference that every fresh prime divisor of $U_k$,
or of $a_k$, must divide the reduced denominator of $A_k$.
The exact coefficient implementation and independent original-forcing
controls are in [pi_pascal_source.py](../../observational_succ/pi_pascal_source.py)
and [its tests](../../tests/test_pi_pascal_source.py).

## 5. PH-4 — exact denominator divisibility and real separation (PROVED)

For every integer $n\ge1$,

$$
\boxed{
\left(\prod_{\substack{p\text{ prime},\ p\equiv1\ (8)\\
2n+1\le p\le8n-7}}p\right)
\left(\prod_{\substack{p\text{ prime},\ p\equiv5\ (8)\\
2n+1\le p\le8n-3}}p\right)
\ \mid\ D_n\ \mid\ L_{8n-3}.
}
\tag{PH-7}
$$

Empty products equal one. This is divisibility, not a claimed formula
for every prime exponent in $D_n$.

**Proof of the lower divisibility.** Each displayed prime satisfies
$a_p\le n\le B_p$, so PH-1 gives $v_p(U_n)=-1$. The two prime classes
are disjoint, hence their product divides $D_n$.

**Proof of the upper divisibility.** Put $L=L_{8n-3}$. For
$1\le j\le n$, the four positive odd numbers
$8j-7$, $8j-3$, $2j-1$, $4j-1$ divide $L$. The two quotients
$L/(2j-1)$ and $L/(4j-1)$ are odd integers, so their sum is even.
Therefore

$$
Lr(j)=\frac{4L}{8j-7}-\frac{L}{8j-3}
-\frac12\left(\frac{L}{2j-1}+\frac{L}{4j-1}\right)
\in\mathbb Z.
$$

The integer-weighted recurrence expansion gives $LU_n\in\mathbb Z$.
$\square$

More generally, every integer polynomial filter $P(E)U_n$ of degree
$d$, with $n\ge0$ and $n+d\ge1$, has denominator dividing
$L_{8(n+d)-3}$. Whenever PH-2 certifies that it is nonintegral,

$$
\boxed{
\|P(E)U_n\|_{\mathbb R/\mathbb Z}
\ge \frac1{L_{8(n+d)-3}}.
}
\tag{PH-8}
$$

Indeed $P(E)U_n$ is an integer divided by this common denominator,
and its difference from any integer is a nonzero integer divided by
the same denominator. This proves a real circular bound directly.

There is also a conditional dyadic refinement: for integers $N\ge1$ and
$0\le s,t\le N$, if the **chosen real residual**
$z=U_s-U_t-a\ne0$ with $a\in\mathbb Z$ satisfies
$v_2(z)\ge h$ for an integer $h\ge0$, then

$$
|z|\ge\frac{2^h}{L_{8N-3}}.
\tag{PH-9}
$$

The numerator over the odd common denominator is divisible by $2^h$.
For circular distance, $a$ must be a nearest integer. The inherited
congruence of $U_s-U_t$ alone does not supply the required congruence
of this residual: the nearest integer/carry must also be controlled.

## 6. PH-5 — exponential height and the BBP prefix boundary (PROVED)

The classical prime number theorem in the two fixed reduced residue
classes gives

$$
\sum_{\substack{p\le x\\p\equiv a\ (8)}}\log p
=\frac{x}{4}+o(x),\qquad a\in\{1,5\}.
$$

Each product in PH-7 therefore contributes $(3/2+o(1))n$ to its
logarithm. Also
$\log L_X=\psi(X)-\lfloor\log_2X\rfloor\log2=X+o(X)$.
Consequently

$$
\boxed{(3+o(1))n\le\log D_n\le(8+o(1))n.}
\tag{PH-10}
$$

Only fixed modulus $8$ is used; there is no uniformity claim in a
growing modulus. A primary exposition of the required PNT and PNT in
fixed arithmetic progressions is Tao,
[254A, Notes 2](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/),
equations (3), (6), Exercise 55 and Remark 56.

For completeness, these heights obstruct a specific naive approximation
strategy. The $n$-term BBP truncation of $\pi$ is
$P_n=16^{1-n}U_n$. The inherited identity $v_2(U_n)=v_2(n)$ gives its
exact reduced denominator

$$
q_n=D_n2^{4(n-1)-v_2(n)},\qquad n\ge1.
$$

From the [positive real kernel](PI_PASCAL_REAL_KERNEL.md),

$$
\pi-P_n=16^{1-n}T_n,\qquad
T_n=\int_0^1\frac{x^{8n}(1-x)
(4+4x+4x^2+2x^3+x^4)}{16-x^8}\,dx.
$$

On $0<x<1$, the ratio of the displayed polynomial to $16-x^8$
exceeds $1/4$. Thus

$$
T_n>\frac1{4(8n+1)(8n+2)},\qquad
q_n(\pi-P_n)
=\frac{D_nT_n}{2^{v_2(n)}}
>\frac{D_n}{4n(8n+1)(8n+2)}\longrightarrow\infty.
\tag{PH-11}
$$

This excludes the $q_n|\pi-P_n|\to0$ regime for these particular BBP
prefixes. It makes no claim about other rational approximants, Padé
constructions, or auxiliary linear forms.

## 7. Novelty tax, finite falsifiers and the remaining bridge

The actual gain is an exact arithmetic exclusion: on each sole-birth
window, an integer filter with $p\nmid P(16)$ cannot equal an integer.
The gain is source-specific, and it survives every finite order whose
support remains inside that window. The height theorem also excludes
bounded-denominator counterfeit behavior for the authentic $U_n$.

The real lower bound in PH-8 is only
$\exp(-(8+o(1))(n+d))$. At source indices comparable to $p$, this is
much smaller than the polynomial radii used in the collision/retention
contract. Even PH-9 with $h=O(\log p)$ remains exponentially small.
No frequency bound, cancellation estimate, conditional half bound, or
$1/16$ inverse-branch retention follows from these lemmas. The missing
step remains a bound on the number of authentic selected pairs whose
real residual is small and whose carry lies in the selected branch.

The [off-sample probe](../../scripts/pi_pascal_probe.py) checks the
two prime-birth families against rational values constructed from the
original four-pole forcing, verifies permitted translated Pascal rows,
and retains the $p=89,k=35$ cancellation receipt. The saved
[probe receipt](PI_PASCAL_RECEIPT.json) records its finite ranges.
Those checks are falsification opportunities, not the proof of the
all-index statements above. Further targeted falsifiers are the birth
endpoints, $p=5$ at orders zero and one, and attempts to transfer a
translated-row assertion to a row starting before the prime's birth.
