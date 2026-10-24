# Pascal finite differences of the fixed BBP source

**Date:** 2026-10-24.
**Parent:** [draft #270](https://github.com/femboy2112/SUCC/pull/270) at
`3acd547ff122368d5694efdab029b3156a292d8a`.
**Research contract:** [Pascal / prime geometry](PI_PASCAL_HOLE_CONTRACT.md).
**Authority:** explicit elementary proofs, inherited authenticated source
identity, and exact finite controls. There is no new Lean authority.

The candidate identity is true in full stated generality. For every
$k\ge1$ and every $t\in\mathbb Z_2$,

$$
\boxed{
v_2(\Delta^k r(t))
=v_2(\Delta^k F(t))
=k-1+v_2(k!)
=2k-s_2(k)-1.
}
$$

Here $s_2(k)$ is the binary digit sum, $r$ is the **fixed original BBP
forcing**, and $F$ is the authenticated interpolation of its unwrapped
zero-initial source. This yields exact Mahler coefficient values, a sharp
uniform approximation theorem, and the minimum polynomial degree required
at every finite 2-adic precision. Odd-prime factors obey a different rule:
individual pole counts are exact, but cancellation between poles prevents
the dyadic minimum-term argument from transferring unchanged.

These are actual source identities and approximation results. They do not
bound real-close-pair retention or prove pi normality. The real-phase attack
below identifies the remaining cancellation problem explicitly.

## 1. Fixed source, Pascal operators and provenance

Let $S$ act on functions by $(Sf)(t)=f(t+1)$ and let $\Delta=S-I$.
Then

$$
\Delta^k f(t)
=\sum_{j=0}^k(-1)^{k-j}\binom{k}{j}f(t+j).
$$

The unsigned Pascal row has total weight $2^k$:

$$
\sum_{j=0}^k\binom{k}{j}=2^k.
$$

Consequently $2^k$ is also the sum of the absolute weights in the signed
difference row. The signed difference and the unsigned averaging operator
are different maps. Neither row identity makes the actual source choices
independent.

The forcing and unwrapped source are

$$
\begin{aligned}
r(t)&=\frac4{8t-7}-\frac2{8t-4}
-\frac1{8t-3}-\frac1{8t-2},\\
U_0&=0,\qquad U_n=16U_{n-1}+r(n).
\end{aligned}
$$

The inherited [dyadic source report](PI_DYADIC_SOURCE_ISOMETRY.md) proves

$$
F(t)=\sum_{j=0}^{\infty}16^j r(t-j),
\qquad F(0)=0,
\qquad F(n)=U_n\quad(n\ge0).
$$

It also proves that $r$ and $F$ are bijective isometries of $\mathbb Z_2$.
The new results retain that exact forcing and authenticated initialization.

The implementation is
[pi_pascal_source.py](../../observational_succ/pi_pascal_source.py).
Its [test module](../../tests/test_pi_pascal_source.py) uses the independent
original four-pole formula, literal signed Pascal rows, and independently
formed rational $U_n$ values as controls.

## 2. The reciprocal finite-difference identity

### Lemma PMS-1 — PROVED

Whenever all denominator factors are defined,

$$
\Delta^k\frac1{at+b}
=\frac{(-1)^k a^k k!}
{\prod_{j=0}^{k}(a(t+j)+b)}.
$$

This holds as a rational-function identity for every integer $k\ge0$.

**Proof.** The case $k=0$ is the original reciprocal. If the formula holds
at $k$, subtract its values at $t+1$ and $t$. Their common denominator is
the product over $j=0,\ldots,k+1$; the numerator gains

$$
(at+b)-(a(t+k+1)+b)=-a(k+1).
$$

Thus the numerator becomes $(-1)^{k+1}a^{k+1}(k+1)!$, proving the induction.
$\square$

For dyadic analysis it is useful to keep the four terms in the form

$$
r(t)=\frac4{8t-7}-\frac1{8t-3}
-\frac1{2(2t-1)}-\frac1{2(4t-1)}.
$$

The two half coefficients cancel appropriately in the original function;
they need not individually be 2-integral at order zero. Every denominator
factor inside the reciprocal products is a 2-adic unit when
$t\in\mathbb Z_2$.

## 3. Exact source-specific valuation at every order

For brevity write

$$
P_{a,b;k}(t)=\prod_{j=0}^k(a(t+j)+b),
\qquad \nu(k)=k-1+v_2(k!)\quad(k\ge1).
$$

### Theorem PMS-2: forcing differences — PROVED

For every $k\ge1$ and $t\in\mathbb Z_2$,

$$
v_2(\Delta^k r(t))=\nu(k).
$$

More precisely,

$$
\begin{aligned}
\frac{\Delta^k r(t)}{(-1)^{k+1}2^{k-1}k!}
={}&\frac1{P_{2,-1;k}(t)}
+\frac{2^k}{P_{4,-1;k}(t)}\\
&+\frac{2^{2k+1}}{P_{8,-3;k}(t)}
-\frac{2^{2k+3}}{P_{8,-7;k}(t)}.
\end{aligned}
$$

**Proof.** Apply PMS-1 to each of the four fixed poles and factor out the
displayed common term. Every $P_{a,b;k}(t)$ is a unit. The first summand in
the remaining bracket is odd, and all three others are even because
$k\ge1$. The bracket is therefore a unit. This proves the exact valuation,
not just a lower bound. $\square$

The mechanism is a uniquely least divisible contribution: the slope-$2$
pole has valuation $k-1+v_2(k!)$. The other three valuations exceed it by
$k$, $2k+1$, and $2k+3$. No cancellation can erase that unique minimum.

### Theorem PMS-3: authenticated source differences — PROVED

For every $k\ge1$ and $t\in\mathbb Z_2$,

$$
v_2(\Delta^k F(t))=\nu(k),
$$

and the first forcing-to-source correction has the exact valuation

$$
v_2\bigl(\Delta^k F(t)-\Delta^k r(t)\bigr)=\nu(k)+4.
$$

**Proof.** The defining series for $F$ converges uniformly, so the finite
linear operator $\Delta^k$ passes through it:

$$
\Delta^kF(t)=\sum_{j=0}^{\infty}16^j\Delta^k r(t-j).
$$

By PMS-2 the valuations of these terms are exactly $\nu(k)+4j$.
The term $j=0$ is the unique minimum, proving the first claim. Removing
that term leaves the unique minimum at $j=1$, proving the correction
formula. Equivalently, the difference equals $16\Delta^kF(t-1)$.
$\square$

For every integer $n\ge0$, this gives the authentic finite rational identity

$$
v_2\left(
\sum_{j=0}^k(-1)^{k-j}\binom{k}{j}U_{n+j}
\right)=\nu(k).
$$

The quantifier $k\ge1$ matters. At order zero, $F(0)=0$ while
$r(0)=16/21$; neither is described by the displayed positive-order formula.

## 4. Pascal geometry inside the valuation

Counting multiples of powers of two in a factorial gives

$$
v_2(k!)=\sum_{j\ge1}\left\lfloor\frac{k}{2^j}\right\rfloor
=k-s_2(k).
$$

Hence

$$
\nu(k)=2k-s_2(k)-1,
\qquad
\nu(k+1)-\nu(k)=1+v_2(k+1)>0.
$$

The sharp jumps therefore occur at the binary carry positions. For example:

| $k$ | 1 | 2 | 3 | 4 | 7 | 8 | 16 | 17 | 31 | 32 | 40 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $\nu(k)$ | 0 | 2 | 3 | 6 | 10 | 14 | 30 | 31 | 56 | 62 | 77 |

The standard Pascal congruence has an operator form. If
$k=\sum_j k_jp^j$ is the base-$p$ expansion, then in $\mathbb F_p[S]$,

$$
(S-I)^k
=\prod_j(S^{p^j}-I)^{k_j}.
$$

This follows from the binomial theorem in characteristic $p$ and
$(S-I)^{p^j}=S^{p^j}-I$. Comparing coefficients gives Lucas's digit-product
rule. At $p=2$, a Pascal row contains exactly $2^{s_2(k)}$ odd entries.
Thus the same binary digit sum governs both the nonzero pattern of the
row modulo $2$ and the exact valuation of its signed action on this source.

For general primes, the factorial identity gives

$$
v_p\binom nk
=\frac{s_p(k)+s_p(n-k)-s_p(n)}{p-1},
$$

which counts base-$p$ carries. These classical identities identify the
arithmetic of the observation operator. The source-specific theorem is
PMS-2: what that operator does to the fixed four-pole BBP function.

## 5. Exact Mahler coefficient values

Set

$$
a_k=\Delta^kr(0),\qquad b_k=\Delta^kF(0).
$$

Both sequences consist of rational numbers. The forcing coefficients are
given directly by PMS-1. The source coefficients have a useful exact
recurrence:

$$
\boxed{b_0=0,\qquad b_{k+1}=15b_k+\Delta^k r(1).}
$$

**Proof.** Rewrite the authenticated source equation as
$\Delta F(t)=15F(t)+r(t+1)$. Apply $\Delta^k$ and evaluate at zero.
$\square$

Some initial exact values are:

| Order | $a_k$ for the forcing | $b_k$ for the source |
|---:|---:|---:|
| 0 | $16/21$ | $0$ |
| 1 | $83/35$ | $47/15$ |
| 2 | $-22012/4095$ | $180164/4095$ |
| 3 | $705528/85085$ | $39045656/58905$ |

For $k\ge1$, both columns have valuation exactly $\nu(k)$, but their real
values behave very differently. Smallness in the 2-adic norm is not smallness
in the real norm.

### Theorem PMS-4: uniform Mahler expansions — PROVED

For every $t\in\mathbb Z_2$,

$$
r(t)=\sum_{k=0}^{\infty}a_k\binom tk,
\qquad
F(t)=\sum_{k=0}^{\infty}b_k\binom tk,
$$

with uniform convergence.

**Proof.** Each polynomial $\binom tk$ maps $\mathbb Z_2$ to
$\mathbb Z_2$: it is integer-valued on the nonnegative integers, and the
claim extends by polynomial continuity and their density in $\mathbb Z_2$.
The exact coefficient valuations tend to infinity, so each displayed series
converges uniformly. At every nonnegative integer $n$ the sums truncate at
$k=n$ and agree with the finite Newton inversion identity. The continuous
functions therefore agree everywhere by density. $\square$

This proof only needs the proved coefficient decay for the present source.
The general Mahler expansion theorem is classical; references are listed
below.

## 6. Sharp approximation and minimum degree as a function

Let $f$ denote either $r$ or $F$, let $c_k$ be its corresponding coefficient,
and put

$$
P_D(t)=\sum_{k=0}^{D}c_k\binom tk.
$$

### Theorem PMS-5: exact minimax approximation error — PROVED

For every $D\ge0$,

$$
\boxed{
\|f-P_D\|_\infty
=2^{-\nu(D+1)}
=\inf_{\deg P\le D}\|f-P\|_\infty,
}
$$

where the norm is the uniform 2-adic norm on $\mathbb Z_2$, and the
infimum may be taken over all polynomials in $\mathbb Q_2[t]$ of degree
at most $D$.

**Proof.** Since $\nu(k)$ increases strictly, the omitted coefficients have
norm at most $2^{-\nu(D+1)}$. The binomial polynomials have norm at most one,
so the upper bound follows. At $t=D+1$, the tail is exactly $c_{D+1}$:
all terms of higher order vanish, and $\binom{D+1}{D+1}=1$. Thus the upper
bound is attained.

For any polynomial $P$ of degree at most $D$, one has
$\Delta^{D+1}P=0$. The finite signed difference operator has uniform
2-adic operator norm at most one, because its coefficients are integers.
Therefore

$$
2^{-\nu(D+1)}
=|\Delta^{D+1}(f-P)(0)|_2
\le\|f-P\|_\infty.
$$

This proves optimality against every competing polynomial, not just a
different truncation in the same basis. $\square$

### Corollary PMS-6: exact degree at precision $B$ — PROVED

For any integer $B\ge1$, define

$$
D_B=\max\{k\ge1:2k-s_2(k)-1<B\}.
$$

Then $D_B$ is the **minimum degree of an integer-valued polynomial function**
on $\mathbb Z_2$ agreeing with $r$, or with $F$, modulo $2^B$ everywhere.

**Proof.** The polynomial $P_{D_B}$ is integer-valued and its omitted
coefficients are all divisible by $2^B$, so it gives the required function.
If a polynomial of degree below $D_B$ agreed pointwise modulo $2^B$, applying
$\Delta^{D_B}$ at zero would force $\Delta^{D_B}f(0)$ to be divisible by
$2^B$. Its valuation is $\nu(D_B)<B$, a contradiction. This is a
function-level obstruction and does not assume uniqueness of a chosen
polynomial representation modulo $2^B$. $\square$

Useful explicit bounds are

$$
\left\lceil\frac B2\right\rceil
\le D_B
\le\left\lfloor\frac{B+\lfloor\log_2B\rfloor+1}{2}\right\rfloor.
$$

For the lower bound, set $k=\lceil B/2\rceil$ and use $s_2(k)\ge1$.
For the upper bound, $\nu(k)\ge k-1$ first gives $k\le B$; then
$\nu(k)<B$ gives $2k\le B+s_2(k)\le B+\lfloor\log_2B\rfloor+1$.
Thus $D_B=B/2+O(\log B)$.

| Precision $B$ in bits | 8 | 16 | 32 | 64 | 128 | 256 |
|---:|---:|---:|---:|---:|---:|---:|
| Minimum degree $D_B$ | 5 | 9 | 17 | 33 | 65 | 129 |

These are polynomial-approximation degrees, not real collision-retention
fractions. The occurrence of approximately one-half in this degree count
does not discharge the earlier half-retention premise.

### Implementation and complexity boundary

`newton_mod` evaluates the exact minimal-degree polynomial at an integer
index modulo $2^B$. Reduction of the index modulo $2^B$ is justified by the
inherited isometry, and a binomial recurrence avoids re-expanding the
polynomial into monomials.

The present implementation precomputes $O(B)$ rational coefficients using
$O(B^2)$ rational product operations. A subsequent evaluation uses $O(B)$
terms, with exact modular reductions and inverses. These are arithmetic
operation counts. The integer and rational sizes grow with precision;
binomial integers for a $B$-bit representative can themselves require
$O(B^2)$ bits. No unit-cost bit-complexity claim is made.

This supplies a sharp finite polynomial representation and an independently
structured evaluator. It is not asserted to run faster than the inherited
backwards-source modular sum, which already avoids constructing the enormous
real unwrapped rational state.

## 7. Odd-prime factors: exact counts and a failed shortcut

The dyadic proof uses a unique least divisible pole. Odd primes generally
see ties among the pole contributions.

### Theorem PMS-7: per-pole odd-prime denominator count — PROVED

Let $n\in\mathbb Z$, $k\ge0$, $a=2^h$ with $h\ge1$, $b$ be odd,
and $p$ be an odd prime. Set

$$
C_e=\#\{0\le j\le k:p^e\mid a(n+j)+b\}.
$$

Then

$$
v_p\left(\Delta^k\frac1{at+b}\bigg|_{t=n}\right)
=\sum_{e\ge1}\left(
\left\lfloor\frac{k}{p^e}\right\rfloor-C_e
\right),
$$

and each $C_e-\lfloor k/p^e\rfloor$ is either zero or one. In particular,
the per-pole valuation is nonpositive.

**Proof.** Apply PMS-1. Since $a$ is prime to $p$, its power contributes
no valuation. The factorial contributes the displayed floor counts, and
the denominator contributes $C_e$ at precision $p^e$. The map
$j\mapsto a(n+j)+b$ visits one fixed zero residue class modulo $p^e$.
Among $k+1$ consecutive indices that class is visited either
$\lfloor k/p^e\rfloor$ or one more times. $\square$

The coefficients $4,-1,-1/2,-1/2$ are units at every odd prime, so the same
per-pole calculation applies to all four weighted terms. Equivalently, the
odd part of $k!$ divides each odd arithmetic-progression denominator product.
After cancellation, each individual weighted pole term has numerator equal
up to sign to a power of two. Their **sum** can acquire new odd numerator
factors.

At $(n,k,p)=(0,1,3)$, the four pole valuations are

$$
(0,-1,0,-1),
$$

but the exact sum is

$$
\Delta r(0)=\frac{83}{35},\qquad v_3(\Delta r(0))=0.
$$

Thus taking the minimum of the four valuations would give the wrong answer.
The two least divisible terms cancel at the odd place. This is an exact
receipt against transferring the dyadic minimum-term rule to all primes.

The odd-place statements above concern rational values at **integer** starts.
A general $t\in\mathbb Z_2$ is not automatically an element of every
other local field with a canonical compatible value. No such identification
is assumed.

## 8. What the exact values do and do not buy on the real side

The recurrence for the actual coefficients
$b_{k+1}=15b_k+\Delta^kr(1)$ retains information that the valuation profile
alone discards. For example, changing a slope-$8$ pole changes these values
while preserving the unique slope-$2$ valuation minimum at every positive
order. The focused tests retain this mutation as a failure of
profile-only source authentication.

We also tried using the signed Pascal rows directly on the real source.
The inherited exact tail representation is

$$
U_n=16^n A-T_n,
\qquad A=\pi/16,
\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j),
$$

where $T_n>0$ is decreasing and $T_n=O(n^{-2})$ for large $n$.
Since $\Delta^k16^n=15^k16^n$, one obtains the exact identity

$$
\Delta^kU_n
=15^kU_n+15^kT_n-\Delta^kT_n.
$$

The signed Pascal row gives the safe real bound
$|\Delta^kT_n|\le2^kT_n$. Thus, for fixed $k$,

$$
|\Delta^kU_n-15^kU_n|
\le(15^k+2^k)T_n=O_k(n^{-2}).
$$

Writing $e(x)=\exp(2\pi i x)$, the corresponding phase comparison is

$$
|e(h\Delta^kU_n)-e(15^khU_n)|
\le2\pi|h|(15^k+2^k)T_n.
$$

Consequently, fixed-order Pascal phase differencing transports the unknown
Fourier cancellation at frequency $h$ to cancellation at frequency $15^kh$,
with a controlled small source error. It does not itself make that latter
mean small. Allowing $k$ to grow incurs the explicitly growing factor
$15^k+2^k$ and cannot be treated as a uniform fixed-order estimate.

The real moment/Euler-transform lane studies the coefficient values further.
This report does not duplicate that implementation or treat its identities
as a central-carry retention theorem. No nontrivial real selected-source
half bound or positive collision exponent was obtained in this constructor
lane.

### Theorem PMS-8: the dyadic polynomial can contain negligible real magnitude — PROVED

For the authentic source, let $P_D(n)=\sum_{k\le D}b_k\binom nk$, where
$n\ge1$ and $0\le D\le n$. Then

$$
\boxed{
\frac{|P_D(n)|}{U_n}
\le\frac{16}{15}(D+1)\frac{(17n)^D}{16^n}.
}
$$

Here both absolute value and ratio are real. In particular, for a precision
budget $B=O(\log n)$, the degree-optimal polynomial $P_{D_B}$ captures the
entire source residue modulo $2^B$ while its share of the real unwrapped
magnitude is at most

$$
\exp\bigl(-n\log16+O((\log n)^2)\bigr).
$$

**Proof.** Positivity and decrease of the fixed forcing give

$$
r(1)16^{n-1}\le U_n
\le r(1)\sum_{j=0}^{n-1}16^j
<\frac{r(1)}{15}16^n.
$$

The signed Pascal formula for $b_k=\Delta^kU_0$ therefore gives

$$
|b_k|\le\frac{r(1)}{15}
\sum_{j=0}^k\binom kj16^j
=\frac{r(1)}{15}17^k.
$$

For $k\le D\le n$, use $\binom nk\le n^k$ and $17n\ge1$ to obtain
$|P_D(n)|\le(r(1)/15)(D+1)(17n)^D$. Dividing by the lower bound for $U_n$
proves the result. Corollary PMS-6 gives $D_B=O(\log n)$ under the stated
precision budget, yielding the exponential form. $\square$

An exact finite control at $n=128$, $B=16$, has degree $D_B=9$. The bound
above is already less than $2^{-400}$, even though the polynomial has
exactly the correct source residue modulo $2^{16}$.

This is a source-specific comparison of two norms. It explains why the new
finite polynomial representation cannot simply replace the real source in
a circle-phase estimate. Almost all real magnitude can lie in the omitted
tail, and the fractional part of that tail remains consequential. The
theorem does not assert that large magnitude prevents cancellation; it
identifies an uncontrolled term that cannot be discarded on the strength
of a 2-adic error bound.

## 9. Verification and earned scope

The new focused suite contains **21 tests**, all passing in the recorded
focused execution. It includes:

- The preregistered calibration grid: integer starts $0$ through $16$,
  difference orders $1$ through $16$.
- Fresh orders $17$ through $40$ at starts $19,31,64,127$, with exact
  signed-row and closed-product agreement.
- Additional rational 2-adic starts $1/3,-7/5,1009/17$.
- Independently formed authentic rational $U_n$ through index $167$,
  checking the source valuation and the exact first-correction valuation.
- Exact source Mahler coefficients against direct Pascal differences;
  finite polynomial evaluation against the separate modular source evaluator
  through precision $129$, including negative and large integer indices.
- Minimum-degree witnesses, sharp uniform-error witnesses, Pascal parity
  controls, odd-prime Lucas controls, and explicit odd-prime pole cancellation.
- Exact cross-norm controls, including the $n=128$, 16-bit source polynomial
  whose real magnitude share is bounded above by $2^{-400}$.
- Rejected source and domain mutations, including the distinction between
  preserving the valuation profile and preserving the actual source values.

The universal statements are supported by the proofs above. The computations
verify their implementations in the stated finite domains; they do not
constitute an infinite lift or a pi-normality certificate.

## 10. Claim ledger and next dependency

| Claim | Status | Boundary |
|---|---|---|
| Exact four-pole reciprocal-difference values | PROVED | Rational identity away from poles |
| $v_2(\Delta^kr(t))=\nu(k)$ | PROVED | Every $k\ge1$, every $t\in\mathbb Z_2$ |
| Same valuation for $F$, and correction valuation $\nu(k)+4$ | PROVED | Uses the inherited authenticated $F$ |
| Exact rational Mahler coefficients and recurrence | PROVED | Fixed source values retained |
| Sharp minimax polynomial error and minimum degree | PROVED | Uniform 2-adic function approximation |
| Odd-prime per-pole count formula | PROVED | Rational values at integer starts |
| Odd-prime minimum-of-poles shortcut | REFUTED | Explicit $(0,1,3)$ counterexample |
| Exact dyadic polynomial can contain exponentially little real magnitude | PROVED | The fixed authentic unwrapped source; no phase cancellation conclusion |
| Focused executable controls | VERIFIED_FINITE | Exactly the ranges listed above |
| Real central-carry saving or tripling transport | OPEN | Requires additional selected-source joint information |
| Pi normality | OPEN | No closing real estimate obtained |

The first open dependency remains an estimate on the actual real-conditioned
carry law or the same selected empirical measures under tripling. The new
coefficient values give a fully specified source representation against
which such an estimate can be tested. The valuation profile, Pascal row
mass and finite polynomial compression are insufficient substitutes.

**Novelty tax.** Newton differences, Mahler expansions, Lucas congruences and
factorial carry counts are classical. The contributions established here
are their exact specialization to the fixed authenticated BBP source,
including its valuation profile, sharp approximation scale and executable
source-faithful coefficient evaluator. Scholarly priority is unverified.
No theorem is labeled a normality proof merely because it changes the
coordinates of the surviving obstruction.

## 11. Mathematical references

1. K. Mahler, [An Interpolation Series for Continuous Functions of a p-adic
   Variable](https://doi.org/10.1515/crll.1958.199.23), Journal fuer die reine
   und angewandte Mathematik 199 (1958), 23–34. Classical expansion context.
2. Keith Conrad, [Mahler expansions](https://kconrad.math.uconn.edu/blurbs/gradnumthy/mahlerexpansions.pdf),
   especially the coefficient formula and uniform binomial-polynomial
   estimates in Sections 1–2. The present source-specific expansion and
   minimax proofs are supplied above rather than inferred from a citation.
3. [The inherited authenticated dyadic-source theorem](PI_DYADIC_SOURCE_ISOMETRY.md),
   for the analytic zero, exact source selector and original modular
   evaluator. This report does not reclassify a finite test as its proof.
