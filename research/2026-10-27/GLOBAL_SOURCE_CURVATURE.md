# Source curvature forces signed loss in prescribed moving bands

**PAPER-PROVED; exact finite replay; finite real core checked separately in
Lean.** These are estimates for the original full BBP phases, with every pole,
integer lift and carry retained. They hold for **every initial seed** under the
same forcing. Consequently they cannot, by themselves, distinguish the original
zero selector or establish fixed-frequency cancellation. Academic priority is
unverified. The additions are the unit-center refinement, explicit moving-band
estimates and full same-forcing transfer obstruction; the earlier quantitative
forcing argument is credited below.

## 1. The source and the results

Throughout, $e(x)=\exp(2\pi ix)$ and

$$
r(k)=\frac4{8k-7}-\frac2{8k-4}-\frac1{8k-3}-\frac1{8k-2},\qquad
X_{n+1}=16X_n+r(n+1).
$$

The authentic source has $X_0=0$ and is denoted $U$. All theorems in this
document also hold for real $X_0$. The distinction is explicit, not inferred
from a source label. Put $W_{m,h}(X)=\sum_{n=m+1}^{2m}e(hX_n)$.

For every integer $m\ge128$ and integer $h$ with $m^2\le|h|\le2m^2$,

$$
\boxed{|W_{m,h}(X)|\le m-\frac{\lfloor m/4\rfloor}{18496}.}
\tag{GC-1}
$$

For every integer $m\ge16$ and integer $h$ with
$m^3\le|h|\le\lfloor16m^3/15\rfloor$,

$$
\boxed{|W_{m,h}(X)|\le
m-\frac{\max(0,m-33)}{289}.}
\tag{GC-2}
$$

These are effective, uniform, nontrivial relative losses in prescribed bands.
Neither is an $o(m)$ bound. Both concern moving frequencies: for a fixed
nonzero $h$, their hypotheses eventually fail. They do not improve the order
of the separate zero-selected logarithmic theorem.

**Exact novelty credit.** The factor-289 norm comparison and an authentic
forcing-variance gap are already proved in PRK-02 of
[PRIME_CLOCK_RESONANCE_REPORT.md](../2026-10-25/PRIME_CLOCK_RESONANCE_REPORT.md),
commit `eca4462ee4d62642b15c4af672136aa5bcacd00b`, with native
`prime_clock_resonance.forced_coherence_gap`. Its explicit prime-window
floor already gives a relative loss at a quadratic moving frequency.
Those facts are inherited, not new. Here (GC-4) refines that comparison by
minimizing forcing distance over **unit** centers rather than arbitrary
complex centers; the new applications are the stated all-integer bands,
the cubic first-derivative estimate, and the full same-forcing obstruction.

There is also a stronger obstruction to any unsupported high-to-low transfer.
For the **same entire forcing**, set $V_n=-T_n$, where
$T_n=\sum_{j\ge1}16^{-j}r(n+j)$, so $V_0=-\pi/16$.
For every cubic-band pair $(m,h)$ above,

$$
\boxed{|W_{m,h}(V)|\le\min(m,512),}
\tag{GC-3}
$$

yet $N^{-1}\sum_{n=1}^Ne(hV_n)\to1$ for every fixed integer $h$.
Thus even **uniform decay throughout this entire moving band of the full
selected phases**, together with the exact forcing, does not imply the desired
fixed-frequency decay. The original zero selector is the failed assumption.

## 2. A paid comparison from forcing phases to orbit coherence

Consider any $L\ge2$ complex numbers $z_0,\ldots,z_{L-1}$ of modulus one.
Set $w_i=z_{i+1}\overline z_i^{16}$, $0\le i<L-1$, and

$$
D_z=L-\left|\sum_i z_i\right|,\qquad
D_w=(L-1)-\left|\sum_i w_i\right|.
$$

Then

$$
\boxed{D_w\le289D_z.}\tag{GC-4}
$$

Choose a unit $a$ in the direction of $\sum z_i$, or any unit $a$ when the sum
vanishes. The exact identity $\sum|z_i-a|^2=2D_z$ holds. Telescoping the
sixteenth power gives $|z_i^{16}-a^{16}|\le16|z_i-a|$. Hence

$$
|w_i-a^{-15}|=|z_{i+1}-a^{-15}z_i^{16}|
\le |z_{i+1}-a|+16|z_i-a|.
$$

For nonnegative $u_i=|z_i-a|$, weighted Cauchy gives

$$
\begin{aligned}
\sum_{i=0}^{L-2}(u_{i+1}+16u_i)^2
&\le\sum_{i=0}^{L-2}(17u_{i+1}^2+272u_i^2)\\
&=289\sum_{i=0}^{L-1}u_i^2-17u_0^2-272u_{L-1}^2.
\end{aligned}
$$

The left squared distances dominate $2D_w$, the minimum over **all** unit
centers for the $w_i$. This proves (GC-4), with both finite boundary costs paid.
To compare precisely with inherited PRK-02, put
$\rho=|\sum w_i|/(L-1)$. Its unconstrained variance is
$D_w(1+\rho)$, so the earlier argument gives
$D_z\ge D_w(1+\rho)/578$. The unit-center comparison improves that
right side by $2/(1+\rho)$, a factor between one and two. The common
factor-289 norm calculation itself is unchanged.
The constant 289 is sharp for this generic real norm comparison: constant
$u_i=1$ gives $(L-1)289/L\to289$. This is not a sharpness claim for the
complex recurrence or the BBP theorem.

For $z_i=e(hX_{m+1+i})$ the recurrence yields exactly
$w_i=e(hr(m+2+i))$. No stochastic surrogate, selected embedding average, or
frequency truncation has entered. The real finite norm statement is the scope
of the corresponding Lean declarations. The complex bridge above is a paper
proof, not claimed kernel-checked.

## 3. Source inequalities and monotonicity

The inherited IMW-04/05 identities prove, for every integer $n\ge1$,

$$
0<\frac{15}{64}-n^2r(n+1)<\frac7{5n},\qquad
0<\frac{15}{32}-n^3[r(n+1)-r(n+2)]<\frac3n.
\tag{GC-5}
$$

These follow by clearing the positive four-pole denominators; see
[the original polynomial certificates](../2026-10-25/SUCC_INTERNAL_MATRIX_WALK.md).
The new tests independently regroup the poles and check fresh finite indices;
finite checks are not substituted for that all-index proof.

The integral

$$
r(n+1)=\int_0^1t^{8n}(4-2t^3-t^4-t^5)\,dt
$$

has strictly positive density on $(0,1)$, since
$4-2t^3-t^4-t^5=(1-t)(4+4t+4t^2+2t^3+t^4)$.
Every forward difference with alternating sign therefore has an extra factor
$(1-t^8)^b>0$. In particular $r(n+1)$ and
$r(n+1)-r(n+2)$ are positive and strictly decreasing. This proves the exact
monotonicity needed below without relying on a fitted phase graph.

## 4. Quadratic band: separated source pairs

Take $h>0$; negative modes are conjugates. Among the $m-1$ forcing indices
$n=m+1,\ldots,2m-1$, pair the first $k=\lfloor m/4\rfloor$ indices with
the last $k$ indices, beginning at $\lceil7m/4\rceil$. For each pair $(a,b)$,
the source bounds imply

$$
\begin{aligned}
m^2[r(a+1)-r(b+1)]
&>\frac3{20}-\frac{112}{125m}-\frac{15}{196}\\
&=\frac{18}{245}-\frac{112}{125m}>\frac1{16}
\qquad(m\ge128).
\end{aligned}
$$

For clarity, the early lower bound follows by writing
$m^2r(a+1)>(m/a)^2[15/64-7/(5a)]$ and bounding its two positive
factors below by $16/25$ and $15/64-7/(5m)$, respectively.
For $h\le2m^2$ the same difference multiplied by $h$ is less than
$2(15/64)=15/32<1/2$. Thus the circular separation of the paired forcing
phases is at least $1/16$. The chord bound $|e(x)-e(y)|\ge4\|x-y\|$
gives distance at least $1/4$. For unit $u,v$,

$$
|u+v|=\sqrt{4-|u-v|^2}\le2-|u-v|^2/4\le2-1/64.
$$

Triangle inequality on these disjoint pairs and the unpaired observations
yields $D_w\ge k/64$. Apply (GC-4) to obtain (GC-1).
The classification into pairs was prescribed from indices, not selected after
observing which source phases happened to cancel.

## 5. Cubic band: a finite first-derivative estimate

We first prove the elementary exponential-sum bound used here. If real phases
$f_0,\ldots,f_{J-1}$ have monotone consecutive differences
$d_i=f_{i+1}-f_i$ in $[\delta,1/2]$ or in $[-1/2,-\delta]$, where
$0<\delta\le1/2$, then

$$
\left|\sum_{i=0}^{J-1}e(f_i)\right|\le1/\delta.\tag{GC-6}
$$

The case $J=1$ is immediate. Otherwise put
$a_i=(e(d_i)-1)^{-1}=-1/2-(i/2)\cot(\pi d_i)$.
Its real part is constant and its imaginary part is monotone. Thus its total
variation is at most $|a_0|+|a_{J-2}|$.
Summation by parts in $e(f_i)=a_i[e(f_{i+1})-e(f_i)]$ gives endpoint
coefficients $-a_0$ and $a_{J-2}+1$. The latter has modulus $|a_{J-2}|$.
Since the chord bound gives $|a_i|\le1/(4\delta)$, the two endpoints and
total variation together are at most $1/\delta$. This proves (GC-6);
no incomplete-sum or monotonicity error is omitted.

For the forcing phases, $d_n=-h[r(n+1)-r(n+2)]$ for
$m+1\le n\le2m-2$. In the cubic band (GC-5) and $m\ge16$ imply

$$
\frac1{32}<\frac{15/32-3/m}{8}
\le h[r(n+1)-r(n+2)]<\frac12.
$$

The displayed first strict inequality holds already at $m=16$:
$(15/32-3/16)/8=9/256>1/32$.
The increments are monotone by the positive integral. Formula (GC-6) with
$\delta=1/32$ bounds the $m-1$ forcing phases by 32.
Therefore $D_w\ge\max(0,m-33)$, and (GC-4) proves (GC-2).

## 6. Full same-forcing countermodel to an unpaid high-to-low transfer

The inherited Green identity gives $V_n=-T_n$ with the original forcing,
$V_0=-\pi/16$, and $0<T_n<1/(64n^2)$. Hence $V_n\to0$ and every fixed
Fourier average tends to one. The new assertion is that its **full**, rather
than prime-projected, cubic-band sums satisfy (GC-3).

Write $d(n)=r(n+1)-r(n+2)$. Absolute convergence and positivity give

$$
T_n-T_{n+1}=\sum_{j\ge1}16^{-j}d(n+j-1).
$$

The sum is positive and strictly decreasing. Its first term and (GC-5) give
the lower bound, while monotonicity and the geometric sum give the upper bound:

$$
\frac{15/32-3/n}{16n^3}
<T_n-T_{n+1}<\frac1{32n^3}.
$$

For a cubic-band $h>0$ and $m+1\le n\le2m-1$ this yields

$$
\frac1{512}<\frac9{4096}
<h(T_n-T_{n+1})<\frac1{30}<\frac12.
$$

The middle strict lower comparison uses $n>m$ and $m\ge16$; the weaker
$9/4096$ is sufficient. These are the monotone increments of the actual
phases $hV_n$. Apply (GC-6) with $\delta=1/512$ to obtain (GC-3).
All infinite sums here converge absolutely by positivity and the geometric
weight, and termwise differences are justified by that same domination.

In the quadratic band the same countermodel instead stays highly coherent:
$0<hT_n<1/32$, so, using $\pi<22/7$,

$$
\operatorname{Re}\frac{W_{m,h}(V)}m
\ge1-\frac{2(22/7)^2}{32^2}=\frac{6151}{6272}.
$$

This does not conflict with the small positive loss (GC-1). It shows that
different moving bands really can exhibit different signed behavior on the
same source, without enforcing any fixed-frequency cancellation.

## 7. Why the forcing comparison cannot close fixed modes

For fixed $h$, the forcing defect on any initial interval is bounded above by
the sum of $1-\operatorname{Re}e(hr(n+1))$. From (GC-5) and $\pi<22/7$,

$$
1-\operatorname{Re}e(hr(n+1))
\le\min\left(2,\frac{9h^2}{8n^4}\right).
$$

Splitting at $L=\lceil\sqrt{|h|}\rceil$ and bounding the tail by an integral
gives a uniform upper bound $(19/8)\sqrt{|h|}+2$. On a late block with
$n\ge m+1$ the bound is at most $3h^2/(8m^3)$.
Thus the lower bound $D_z\ge D_w/289$ alone cannot even produce growing
fixed-$h$ loss; its right side tends to zero on late blocks. This is a proved
limitation of this instrument, not a claim that the actual orbit has small loss.

The next missing comparison must use the zero selector and some additional
cross-time arithmetic information. The original boundary supplies the endpoint
$\pi$ in the separate [quiet-transition theorem](GLOBAL_BRANCH_COERCIVITY.md),
but that theorem currently extracts only logarithmically many constant losses.

## 8. Authority and hostile controls

`global_source_curvature.py` imports the immutable source; the certificate
checks every increment on a finite window with exact rationals. The interval
holdouts use the existing Machin/Taylor enclosure, independently of the generic
energy proof. A changed rational seed keeps all interior source recurrences but
is rejected by the **zero-source passport**; it remains within the deliberately
larger all-seed mathematical theorem. Changed poles and out-of-band frequencies
are rejected. Zero forcing does not satisfy the source separation hypotheses.

The Lean core covers the finite real norm/endpoint inequality and scalar
division implications. It does not check complex telescoping, the integral,
source asymptotics, first-derivative estimate, Green limits, or normality.
Neither a positive Gram nor a commuting source diagram is counted as a second
independent proof of signed cancellation. **π normality remains OPEN.**
