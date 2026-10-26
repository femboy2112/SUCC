# Zero-initial BBP cannot retain maximal coherence on every geometric block

**Status: PAPER-PROVED, with a CLASSICAL published irrationality-measure input;
EXACT FINITE certificates and hostile controls.** The theorem has an unspecified
uniform threshold. No numerical value for a global irrationality constant is
certified here. No infinite analytic theorem in this dossier is Lean-checked.
Scholarly novelty is unverified. **Base-16 normality of π remains OPEN.**

There is one integer $J_0$ such that, for every $N\ge1$ and every nonzero
integer $h$, the original zero-initial BBP trajectory satisfies

$$
\boxed{
\left|\sum_{n=1}^{N}e(hU_n)\right|
\le N-\frac1{1250}
\max\!\left(0,\lfloor\log_8 N\rfloor-
\max\!\left(J_0,\lceil\log_{64}|h|\rceil\right)\right).
}
\tag{DC-1}
$$

In particular the absolute loss from $N$ grows at least logarithmically for
each fixed $h$. This is a new source-selected inequality in this repository,
not a cancellation theorem: its normalized upper bound still tends to one.
The proof uses the exact zero anchor, the full four-pole source, a widened
finite inverse theorem, and a classical Diophantine bound. It does not infer
selection from a small measure of exceptional arcs.

## Provenance and the independent arithmetic input

The finite inverse theorem is inherited from
[PR #297, section 6](https://github.com/femboy2112/SUCC/blob/eca4462ee4d62642b15c4af672136aa5bcacd00b/research/2026-10-25/BBP_RESONANCE_OBSTRUCTIONS.md),
at source SHA `eca4462ee4d62642b15c4af672136aa5bcacd00b`. We reproduce its
proof to audit the constants and implement the rational certificate
independently. Its forcing-only near-coherent controls and original
three-to-one block are inherited. The new step is to widen to $(m,8m]$,
retain the Green correction exactly, and use a Diophantine obstruction
uniformly for $1\le |h|\le m^2$.

Zeilberger and Zudilin prove $\mu(\pi)\le7.103205334137\ldots<15/2$ in
[the corrected 2020 paper](https://arxiv.org/abs/1912.06345v2), published in
[Moscow Journal of Combinatorics and Number Theory](https://doi.org/10.2140/moscow.2020.9.407).
Only the strict inequality $\mu(\pi)<15/2$ is used. No claimed exponent-two
result is an input.

Consequently there is a rational constant $0<C\le1$ such that

$$
\left|\pi-\frac pq\right|\ge Cq^{-15/2}
\quad\text{for all }p\in\mathbb Z,\ q\in\mathbb Z_{\ge1}.
\tag{DC-2}
$$

Indeed the definition of irrationality exponent gives the bound with
constant one for all sufficiently large reduced denominators. For the
remaining finitely many denominators, irrationality gives a positive
minimum after restricting to numerators within distance one of π; the
other numerators already satisfy the bound. Choose a smaller positive
rational $C$. Reducing $p/q$ only decreases its denominator, so (DC-2)
holds also for unreduced fractions. We do not calculate $C$ or its finite
exceptional-denominator threshold.

## 1. Source passport and elementary Green bounds

Throughout the positive theorem, the source is exactly

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

Define the positive Green tail

$$
T_n=\sum_{k\ge1}16^{-k}r(n+k).
$$

The classical BBP identity, with precisely these indices and signs, gives

$$
U_n+T_n=16^{n-1}\pi.\tag{DC-3}
$$

For completeness the bounds needed below follow directly from the source.
Put

$$
g(t)=4-2t^3-t^4-t^5=(1-t)H(t),\qquad
H(t)=4+4t+4t^2+2t^3+t^4.
$$

For $0<t<1$, $0<H(t)<15$ and $16-t^8>15$. Therefore $r(n)$ is positive
and strictly decreasing, and for $n\ge1$,

$$
\begin{aligned}
r(n+1)&=\int_0^1t^{8n}g(t)\,dt
 <\frac{15}{(8n+1)(8n+2)}<\frac{15}{64n^2},\\
T_n&=\int_0^1t^{8n}\frac{g(t)}{16-t^8}\,dt
 <\frac1{(8n+1)(8n+2)}<\frac1{64n^2}.
\end{aligned}\tag{DC-4}
$$

The integral for $T_n$ follows by summing its nonnegative geometric
integrand; monotone convergence justifies that exchange. The rational
finite inverse implementation does not call π, π digits, or a complex
floating-point oracle.

## 2. Audited finite inverse theorem

Let $T\ge1$, $D=T+1$, $h\ne0$ be an integer, and

$$
X_{t+1}=16X_t+r_{t+1}\quad(0\le t<T),\qquad
S_T=\sum_{j=1}^{T}16^{-j}r_j.
$$

These are arbitrary real forcing values in this lemma. Suppose $a>0$ and

$$
34a+|h|(\max_jr_j-\min_jr_j)<1.\tag{DC-5}
$$

If

$$
D-\left|\sum_{t=0}^{T}e(hX_t)\right|\le8a^2,\tag{DC-6}
$$

then for some integer $p$,

$$
\left|X_0+S_T-\frac p{15|h|}\right|
\le\frac{32a+|h||r_T|}{15|h|16^T}.\tag{DC-7}
$$

Equivalently, the initial phase lies in the $15|h|$ corresponding arcs
modulo one. No implication from membership to coherence is asserted.

**Proof.** Write $M=D^{-1}\sum_t e(hX_t)$ and
$\varepsilon=1-|M|$. Since $a<1/34$, (DC-6) makes $M\ne0$. Choose a real
$\theta$ with $e(\theta)=M/|M|$. The exact identity

$$
\sum_t|e(hX_t)-e(\theta)|^2=2D\varepsilon\le16a^2
$$

and $|e(x)-1|\ge4\|x\|$ show that each phase has a lift
$y_t=\theta+q_t$, $|q_t|\le a$, with $y_t-hX_t\in\mathbb Z$.
The quantities

$$
d_t=q_{t+1}-16q_t-hr_{t+1}
$$

are all congruent to $15\theta$ modulo one. They lie in a real interval
of length at most the left side of (DC-5), hence have a common value $b$.
Set $k=b-15\theta\in\mathbb Z$, $f=-k/15$. Then

$$
y_{t+1}-f=16(y_t-f)+hr_{t+1},\qquad
y_0-f+hS_T=16^{-T}(y_T-f).
$$

The last transition gives

$$
y_T-f=\frac{16(q_T-q_{T-1})-hr_T}{15},\qquad
|y_T-f|\le\frac{32a+|h||r_T|}{15}.
$$

Since $y_0-hX_0$ is an integer, dividing the backward identity by $h$
places $X_0+S_T$ within the stated radius of a rational with denominator
$15|h|$. This proves (DC-7). QED.

For rational inputs the exact distance to the center grid is

$$
\frac{\|15|h|(X_0+S_T)\|}{15|h|}.
$$

Strictly exceeding the rational radius proves that the absolute loss is
strictly greater than $8a^2$. This comparison is ordinary rational
arithmetic, not an identification of formal group-algebra equality with
evaluated cyclotomic equality.

## 3. Widened blocks exclude extreme coherence uniformly in a growing band

**Theorem DC-3A.** There is an integer $m_0\ge64$ such that for every
$m\ge m_0$ and every integer $h$ with $1\le|h|\le m^2$,

$$
\boxed{
\left|\sum_{n=m+1}^{8m}e(hU_n)\right|<7m-\frac1{1250}.
}\tag{DC-8}
$$

**Proof.** Apply the inverse theorem with

$$
a=\frac1{100},\quad D=7m,\quad T=7m-1,\quad
X_t=U_{m+1+t},\quad r_j=r(m+1+j).
$$

The source monotonicity and (DC-4) certify (DC-5) uniformly:

$$
34a+|h|(r(m+2)-r(8m))
<\frac{34}{100}+\frac{15m^2}{64(m+1)^2}
<\frac{919}{1600}<1.\tag{DC-9}
$$

Suppose, to get a contradiction, that the absolute loss of the block is
at most $8a^2=1/1250$. Formula (DC-7) holds. The long source-dependent
center must not be discarded or assigned denominator $16^m$. Instead
use the **exact** finite identity

$$
U_{m+1}+S_T=16^{-T}U_{8m}
=16^m\pi-16^{-T}T_{8m}.\tag{DC-10}
$$

Combining (DC-7) and (DC-10), there is a rational with the actual
denominator $q=15|h|16^m$ such that

$$
\begin{aligned}
\left|\pi-\frac pq\right|
&\le16^{-(8m-1)}
  \left(\frac{32a}{15|h|}+\frac{r(8m)}{15}+T_{8m}\right)\\
&<16^{-8m}\,16\left(\frac{32}{1500}
 +\frac1{64(8m-1)^2}+\frac1{64(8m)^2}\right)\\
&\le\frac{1648007}{4704000}\,16^{-8m}
<16^{-8m}.
\end{aligned}\tag{DC-11}
$$

This small denominator arises after exact Green cancellation; it is not
the conductor of the rational partial source sum alone.

By (DC-2), (DC-11) is impossible if

$$
C^2 16^m>(15|h|)^{15}.\tag{DC-12}
$$

It suffices that $C^2 16^m>(15m^2)^{15}$. Such an $m_0$ exists and works
for every $m\ge m_0$: the exponential dominates the polynomial, and for
$m\ge64$ the consecutive ratio of $16^m/m^{30}$ exceeds one, since

$$
16\left(\frac m{m+1}\right)^{30}
\ge16\left(1-\frac{30}{m+1}\right)>1.
$$

Thus one threshold works for all the stated frequencies, proving
(DC-8). QED.

All displayed constants are explicit. The existence theorem is
unconditional given the cited classical theorem. Its threshold is
**unspecified, not numerically certified** in this work. A numerical
candidate $m_0$ can be checked by the last rational comparison once a
valid global $C$ has independently been supplied. Setting $C=1$ in a
test checks only arithmetic and does not certify (DC-2) with $C=1$.

The proof also explains the failure of the old block width for this
particular deduction. On $(m,4m]$ the same cancellation gives an error
of order $16^{-4m}$ against a denominator of order $16^m$; the established
exponent $15/2$ does not exclude it. Width eight supplies the necessary
strict exponential gap. The extra factor $|h|\le m^2$ is only polynomial.

## 4. Disjoint blocks, every N, and a prescribed frequency width

Set $J_0=\lceil\log_8 m_0\rceil$. The complete geometric blocks in
$\{1,\ldots,N\}$ are

$$
(8^j,8^{j+1}]\cap\mathbb Z,
\qquad 0\le j<\lfloor\log_8N\rfloor.
$$

They are disjoint. A block is eligible for (DC-8) whenever
$j\ge J_0$ and $64^j\ge|h|$. The remaining observations, including
$n=1$ and the incomplete last block, have total modulus at most their
number. Applying the triangle inequality to this exact partition proves
(DC-1), including $N=1$ and the case of no eligible blocks.
In particular, for fixed $h$,

$$
\left|\sum_{n=1}^{N}e(hU_n)\right|
\le N-\frac{\log_8N}{1250}+O_h(1).
\tag{DC-13}
$$

For a prescribed width $H\ge2$, put

$$
K(N,H)=\max\!\left(0,\lfloor\log_8N\rfloor-
\max\!\left(J_0,\lceil\log_{64}(H-1)\rceil\right)\right).
$$

All modes $1\le|h|<H$ obey the same bound $N-K(N,H)/1250$.
The authentic Fourier identity therefore yields

$$
\boxed{
\frac{D_{N,H}}H
\le(H-1)\left(1-\frac{K(N,H)}{1250N}\right)^2.
}\tag{DC-14}
$$

Indeed $2H^{-1}\sum_{h=1}^{H-1}(H-h)=H-1$. This is a genuine
source-selected deficit from the maximal spectral reinforcement $H-1$.
It does **not** approach zero on an increasing width.

One deterministic schedule is

$$
H_N=1+\lfloor\sqrt N\rfloor.
$$

Here $H_N\to\infty$ and $H_N=o(N)$. Since
$\log_{64}(H_N-1)\le\tfrac14\log_8N$, for all $N\ge1$,

$$
K(N,H_N)\ge\frac34\log_8N-J_0-2.
\tag{DC-15}
$$

For example, use $\lfloor x\rfloor\ge x-1$,
$\lceil y\rceil\le y+1$ and
$\max(J_0,\lceil y\rceil)\le J_0+y+1$ for $y\ge0$.
Thus the **absolute** Fourier loss is logarithmic uniformly over this
prescribed growing window. Dividing by $N$ makes this improvement vanish;
(DC-14) remains of order $H_N$. No assertion of equidistribution follows.

For the exact signed innovation sum, (DC-14) and the inherited telescoping
identity give only

$$
\frac{2}{N^2H}\sum_{m=1}^{N-1}m(q_{m,H}-H)
\le (H-1)\left[\left(1-\frac{K(N,H)}{1250N}\right)^2-\frac1N\right].
$$

No individual innovation sign was assumed. This upper bound is still
much too large for the desired $o(1)$ estimate.

## 5. Hostile controls and the exact assumption they violate

### A. Same authentic forcing, rational changed initial, arbitrarily coherent blocks

For each $m$ independently choose

$$
c_m=-16^{-8m}U_{8m}\ne0,\qquad
X_n=U_n+16^n c_m.
$$

Every forcing step retains all four original signed poles, and $X_{8m}=0$.
For $m+1\le n\le8m$ the exact backward expansion is

$$
X_n=-\sum_{k=n+1}^{8m}16^{n-k}r(k),\qquad
|X_n|<\frac1{64n^2}.
$$

Using $1-\cos(2\pi x)\le(968/49)x^2$ gives the certified strict upper bound

$$
0\le7m-\left|\sum_{n=m+1}^{8m}e(hX_n)\right|
<\frac{121mh^2}{3584(m+1)^4}.\tag{DC-16}
$$

For fixed $h$ this tends to zero. These controls lie exactly at the
inverse grid center: $X_{m+1}+S_T=0$. They fail the **zero initial state**,
not the forcing. The Green selector becomes
$X_n+T_n=16^n(\pi/16+c_m)$, so replacing it by π in (DC-10) would be false.
The quantifiers are $\forall m\ \exists c_m$; one common rational initial
state is not claimed. The tests independently replay the entire rational
trajectory and reject precisely this initialization mismatch.

The same finite orbit after time one can be generated from zero by changing
only $r(1)$ to $r(1)+16c_m$. That control fails the original four-pole law
at index one; preserving its later forcing does not repair the passport.

### B. Fixed nonzero initial with the same forcing

Take the real initial state $X_0=-\pi/16$, so $X_n=-T_n$. For each fixed $h$,

$$
0\le N-\left|\sum_{n=1}^{N}e(hX_n)\right|
\le\frac{968h^2}{49}\sum_{n\ge1}T_n^2<\infty.
$$

This directly refutes a uniform extension of (DC-13) to arbitrary initial
states. This particular infinite control has an irrational initial state;
it is not falsely assigned rational finite conductors. A rational periodic
Green seed works similarly at a denominator-multiple frequency. With
zero forcing and zero initial state, the orbit is identically zero; the
π selector (DC-3) and Diophantine input are absent. The generic finite
inverse oracle correctly reports these fixed phases inside the arcs.

### C. Even excellent irrationality type cannot finish normality

Let $\xi=\sum_{k\ge0}16^{-2^k}$. It is transcendental with irrationality
exponent two, a classical result recorded for every integer base in
[Hone and Varona, section 4, equation (4.2)](https://doi.org/10.1007/s00605-018-1244-1).
Its base-16 nonzero digits occupy only the powers of two, so it is not normal.

The elementary phase estimate is especially relevant here. Set
$s_n=\{16^n\xi\}=\sum_{2^k>n}16^{n-2^k}$. Summing nonnegative terms gives

$$
\sum_{n=1}^{N}s_n
\le\frac{1+\lfloor\log_2(N+1)\rfloor}{15}+\frac1{225}.
$$

For each digit position at most $N+1$ the inner geometric sum contributes
at most $1/15$. For later positions, bound their distinct positive gaps
by all positive integers and sum the second geometric series. Thus
$\sum_{n\le N}e(h16^n\xi)=N+O_h(\log N)$, even though its irrationality
type is excellent. With unchanged authentic BBP forcing and initial
$X_0=\xi-\pi/16$, the orbit is $X_n=16^n\xi-T_n$. Since
$\sum T_n<\infty$, the same estimate persists and its Fourier mean tends
to one. It violates the original initialization. This control shows that
a logarithmic absolute loss is compatible with maximal limiting Fourier
bias even in a class of finite-irrationality-type selectors.

Positive-source prefix/jet mutants, prime-marginal averages, lower-order
Walsh data, and gauge-erased shift spectra do not satisfy an identified
π selector merely by retaining those observations. No such replacement
is used at (DC-10). Existing controls against those replacements therefore
remain intact.

## 6. Exact implementation, authority, and remaining gate

Artifacts:

- [Finite rational instruments](../../observational_succ/bbp_diophantine_coherence.py).
- [Independent focused tests](../../tests/test_bbp_diophantine_coherence.py).

The tests cover literal source replay, signed frequencies, all finite
grid centers and arc boundaries, independent holdout cases at $m=23,37$,
changed-initial controls, a source impulse, zero forcing, independent
squared Diophantine comparisons, integer logarithm boundaries, disjoint
block enumeration, and the Fourier weight sum. There are no numerical
Fourier-spectrum tests masquerading as proof authority.

`conditional_budget` computes the formula for a supplied $J_0$ and always
reports `threshold_numerically_certified=False`. The theorem proves the
existence of one valid $J_0$; finite successful arc exclusions do not
identify it. The finite certificates impose a declared arithmetic budget
$m\le128$; this code budget is not a restriction on the paper theorem.

| Claim | Authority | Boundary |
| --- | --- | --- |
| $\mu(\pi)<15/2$ | CLASSICAL published theorem | Imported; not re-proved or kernel-checked here. |
| Finite inverse arc theorem | Inherited PAPER-PROVED; independently replayed EXACT FINITE | Arc membership is necessary, not sufficient, for extreme coherence. |
| Uniform widened-block loss (DC-8) | PAPER-PROVED from the authentic source and classical input | One unspecified threshold, common to $1\le|h|\le m^2$. |
| All-$N$ logarithmic absolute loss (DC-1) | PAPER-PROVED | No $o(N)$ signed cancellation. |
| Prescribed-width matrix upper bound (DC-14) | PAPER-PROVED | It remains of order $H$, not $o(1)$. |
| Concrete arc rejection, backward identities, controls | EXACT FINITE | Finite holds do not certify the universal threshold. |
| A user-supplied numerical threshold in the budget function | CONDITIONAL | Requires an independently valid global constant or threshold. |
| Extension to arbitrary initial states | REFUTED | Controls A and B retain the forcing but change the selector. |
| Finite irrationality exponent implies normality | REFUTED | Control C has exponent two and maximal limiting Fourier bias. |
| Sublinear selected Fourier sums and spectral purity | OPEN | Not obtained by this extreme-coherence exclusion. |

The formerly open all-growing-block exclusion is now discharged for the
constant absolute-loss regime on $(m,8m]$. The remaining gate is to control
**moderate** selected coherence or the accumulation of partial pair
correlations. The inverse premise (DC-6) covers only a block whose deficit
is at most $1/1250$. A block of normalized magnitude $1/2$, or even
$1-1/\log m$, lies outside that premise. The present Diophantine comparison
does not supply an inverse structure or a count for those blocks.
Any strengthening must enter that regime without dropping the zero anchor
or treating a source-selected phase as a random point in the circle.

Reproduce the focused finite checks with:

```bash
python -m unittest tests.test_bbp_diophantine_coherence -v
```

The focused run completed with **16 tests passing**. Full repository checks,
commit identifiers, hosted CI, and any separately formalized finite core
belong to the enclosing research receipt; none is inferred from this run.
