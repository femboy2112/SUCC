# Conditional entropy and simultaneous authenticated BBP clocks

**Date:** 2026-10-24. **Authority:** paper proofs and exact finite arithmetic.
**Base:** `ea5f92bbc52468e55b597e52455f24bceedb47b3`.
**Scholarly novelty:** unverified; elementary finite entropy and torsion algebra
are classical. **Pi normality:** OPEN. No new Lean authority is asserted here.

This track investigates the proposed multiple-prime / conditional-entropy
attack. It proves an exact obstruction to one such proof architecture, including
its application to the actual BBP source. It does not prove a polynomial saving
for the selected collision count. Its main useful distinction is between
conditioning away a clock and obtaining independence from that clock.

## 1. The authenticated simultaneous-clock domain

Retain the entire source

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
y_0=0,\quad y_n=\{16y_{n-1}+r(n)\}.
$$

Let distinct primes $p_i=8u_i+1$ be given. Their first source-free windows are
the integer intervals $[u_i+1,4u_i]$. On their common interval $[A,B]$, put

$$
A=1+\max_i u_i,\quad B=4\min_i u_i,\quad
N=B-A+1=4\min_i u_i-\max_i u_i.
$$

All assertions below concerning a common sample require $N>0$. Its exact source
decomposition is

$$
y_n=\sum_i v_i(n)+w_n\pmod1,\qquad
v_i(n)=\frac{4\,16^{n-u_i-1}}{p_i}\pmod1,
\quad A\le n\le B,
$$

where the reduced denominator of $w_n$ is coprime to $P=\prod_i p_i$.

**Proof.** The first $p_i$-divisible source denominator is $p_i$ at $n=u_i+1$,
with coefficient 4. The next is $4p_i$ at $n=4u_i+1$. No earlier state has a
$p_i$-primary component. Between these events it is multiplied by 16 at every
step. Subtracting all distinct primary components simultaneously leaves a
rational whose denominator is coprime to their product. This is canonical
primary decomposition in $\mathbb Q/\mathbb Z$, not a claim of independence.

**First-window coverage restriction.** A distinct prime $q=8v+1$ cannot have
its first source-free window contain the full target window $[u+1,4u]$ of
$p=8u+1$. Such containment requires $v\le u$ and $4v\ge4u$, hence $v=u$ and
$q=p$. A multiple-prime method must therefore shrink/partition the target
window or retain additional source impulses beyond first birth. It cannot
attach several unchanged first-birth clock laws to the entire target window.
This restriction does not exclude later source-labelled prime-power methods.

## 2. Exact clock fibers, including incomplete periods

Let $L_i=\operatorname{ord}_{p_i}(16)$ and $K=\operatorname{lcm}_i L_i$.
For uniform random $J\in\{0,\ldots,N-1\}$, define the clock vector

$$
R(J)=(v_i(A+J))_i.
$$

Then $R(j)=R(k)$ if and only if $K\mid j-k$. Indeed, each nonzero primary
coefficient cancels in its own prime field, giving $16^{j-k}=1\pmod{p_i}$.
Consequently $R$ is merely a one-to-one relabelling of $J\bmod K$.

Write $N=qK+s$, $0\le s<K$. Exactly $s$ nonempty-or-possibly-singleton clock
fibers have size $q+1$, and the remaining $K-s$ have size $q$ (zero-size fibers
are omitted from probability calculations). Thus

$$
H(R)=\log N-
\frac{s(q+1)\log(q+1)+(K-s)q\log q}{N},             \tag{1}
$$

using $0\log0=0$. The exact number of ordered time pairs agreeing in every
clock is

$$
B_K(N)=s(q+1)^2+(K-s)q^2
      =\frac{N^2}{K}+s\left(1-\frac{s}{K}\right).   \tag{2}
$$

In particular, if $K\ge N$, every clock fiber is a singleton, $H(R)=\log N$,
and for **every** deterministic observed cell label $X(J)$,

$$
H(X\mid R)=0.                                    \tag{3}
$$

This applies to the actual BBP cell label at any resolution. Conditioning on
enough clocks can reveal the sample index completely; it supplies no remaining
conditional entropy. A theorem demanding positive conditional cell entropy
after such conditioning is false even for uniform unconditioned cell laws.
This is a finite conditional-entropy obstruction, not a normality obstruction.

Adding marginal clock entropies is also generally unlawful. On a complete
common period their sum is $\sum_i\log L_i$, whereas their joint entropy is
only $\log K$. The difference is the exact deterministic dependence cost.
For incomplete periods (1) supplies the correction; neither independence nor
complete-period sampling is assumed.

## 3. What Galois averaging does after the clocks are conditioned on

For residues $1\le a_i<p_i$ define the authentic relative conjugate sample

$$
z_j(\boldsymbol a)=\sum_i a_i v_i(A+j)+w_{A+j}\pmod1.
$$

The complementary denominator is coprime to $P$, so these are genuine
simultaneous relative cyclotomic conjugates. The selected sample is
$\boldsymbol a=\boldsymbol1$. Define $X_{\boldsymbol a}(j)=
\lfloor Mz_j(\boldsymbol a)\rfloor$ for an integer $M\ge1$.

On a fixed clock fiber $R=r$, changing conjugate translates all circle points
by the **same** shift $\theta_r=\sum_i(a_i-1)v_i(r)$. Therefore:

1. Every within-fiber circular close-pair count is exactly conjugate invariant,
   at every radius, with all threshold equalities and diagonal pairs retained.
2. For every nonempty fiber, its normalized $M$-cell collision energies before
   and after the conjugate change differ by at most a factor 2 in either
   direction.
3. The conditional Shannon entropies obey

$$
\left|H(X_{\boldsymbol a}\mid R)-H(X_{\boldsymbol1}\mid R)\right|
\le\log2.                                         \tag{4}
$$

**Proof.** The first claim is translation invariance of circular distance.
For the others, a translated half-open cell meets at most two cells of the
original equal partition, including the wrap at 1. Integer cell shifts merely
permute labels, and the remaining subcell shift has the factor-two transport
proof from SCE-04. Given one label and $r$, there are at most two possible
translated labels, and conversely; the conditional entropy chain rule gives
(4). No boundary avoidance assumption is used. The factor 2 is sharp already
for equal masses at $49/100$ and $51/100$, $M=2$, translated by $1/4$.

Thus conditioning to preserve the local clock removes precisely its useful
translation variation from within-fiber pairs. Averaging conjugates cannot
improve their exact close-pair statistic at all. Cross-fiber pairs remain the
unpaid part.

For the original first $p$-window, $N=\Delta=3u$ is divisible by $L$. Its
same-clock ordered pairs number exactly $\Delta^2/L$, so their contribution
to selected scaled close pairs is at most

$$
\frac ML <p^{-1/10}\log p                           \tag{5}
$$

on the good-prime family and the prescribed $M\le p^{2/5}$. This vanishing
part is an explicit consequence of SCE-05's already-counted equal-phase term,
not claimed as a newly solved part of the dominant collision count. For a
common incomplete window, its exact upper bound is $M B_K(N)/N^2$ from (2).
When $K\ge N$, only the $N$ diagonal pairs are included.

## 4. A quantified obstruction to the naive entropy-transfer proof

The finite entropy chain rule gives the sharpened comparison

$$
H(X_{\boldsymbol a})\le H(X_{\boldsymbol1})+
H(R\mid X_{\boldsymbol1})+\log2.                   \tag{6}
$$

But for every $M$-valued variable $X$,

$$
H(R\mid X)=H(R)-I(R;X)\ge H(R)-\log M.             \tag{7}
$$

On the complete first $p$-window, $H(R)=\log L$. For every good prime in the
handoff contract, with its fixed $c=2/5$ resolution, this forces

$$
H(R\mid X) >\frac1{10}\log p-\log\log p.           \tag{8}
$$

The assertion applies, in particular, to the **actual** selected BBP labels.
No additional theorem about those labels can make the loss in (6) be
$o(\log p)$, because (8) forbids it. This proves a precisely scoped no-go:
transferring near-maximal averaged cell entropy by paying the entire clock
conditional entropy in (6) cannot yield the $o(\log p)$ deficit needed by
SCE-02 at the predetermined scale. With an injective joint clock and a common
window $N\asymp p$, the unavoidable lower bound strengthens to
$\log N-\log M=(3/5)\log p+O(1)$.

This does **not** exclude a more precise entropy argument. In fact (4) gives
the exact useful decomposition

$$
H(X_{\boldsymbol a})-H(X_{\boldsymbol1})
=I(X_{\boldsymbol a};R)-I(X_{\boldsymbol1};R)+\epsilon,
\qquad |\epsilon|\le\log2.                         \tag{9}
$$

The relevant unresolved input is a bound on this **difference of mutual
informations**, not smallness of either conditional clock entropy by itself.
For instance, at a conjugate with near-maximal cell entropy, an upper bound
$I(X_{\boldsymbol a};R)-I(X_{\boldsymbol1};R)=o(\log p)$ would transfer it.
No such actual-source estimate is established here. Naming it is a conditional
dependency refinement, not an independent advance toward normality.

## 5. A finite authenticated certificate and its counterfeit control

Choose primes $(73,97)$, with $(u_1,u_2)=(9,12)$. The actual common interval
is $n=13,\ldots,36$, of length 24. Direct integer modular powers give
$(L_1,L_2)=(9,12)$ and $K=36$. Thus the clock vector is injective, proving
$H(X\mid R)=0$ for the actual source at every resolution. Exact rational
recurrence evaluation verifies the complementary denominator is coprime to
$73\cdot97$ at all 24 states.

At the explicitly **diagnostic** resolution $M=16$ (not the prescribed
asymptotic scale at these small primes), the actual nonzero cell counts are

```text
cell:   0  1  2  3  4  7  8  9 10 13 14
count:  4  2  1  4  3  2  2  2  2  1  1
```

There are 106 ordered close pairs at radius $1/16$, including the 24 diagonal
pairs. The individual clock fiber sizes are six 3s and three 2s for 73, and
twelve 2s for 97. All 24 joint fibers have size one. These exact counts are
finite calibration only.

The known aligned-complement adversary survives **any finite number** of
local clocks. For $Q=2MP+1$, round $-\sum_i v_i(n)$ upward to the $1/Q$ grid,
and call the resulting complement $\widetilde w_n$. Its denominator is
coprime to every $p_i$, while all selected phases lie in $[0,1/Q)$, so their
scaled close-pair count is exactly $M$. In the above example $Q=226593$ and
all $24^2=576$ ordered pairs are close. This counterfeit preserves the local
clocks and their joint injectivity, but **changes the full BBP complement**.
It cannot refute a claim restricted to $y_0=0$ and the full four-pole law.

The implementation is
[`pi_prime_clock_conditioning.py`](../../observational_succ/pi_prime_clock_conditioning.py).
Its [seven focused tests](../../tests/test_pi_prime_clock_conditioning.py) passed
locally. An independent exact oracle reconstructs each selected state by a
weighted source sum rather than the modular state loop, using the combined
rational forcing

$$
r(j)=\frac{120j^2-89j+16}{(2j-1)(4j-1)(8j-7)(8j-3)}.
$$

The oracle checks the discovery window and a preregistered noninjective
holdout: primes $(193,241)$, state indices $31,\ldots,96$, resolutions
$M=3,16,64$, and conjugates $(2,3),(192,240),(17,19)$. Its joint period is 24
and its 24 fibers comprise six pairs and eighteen triples. Direct rational
distance enumeration verifies within-fiber invariance. Exact conditional
support counts verify the two-label transport bound in both directions;
there is no floating logarithm decision. The clock-pair formula is checked by
direct double enumeration on all $1\le N<40$, $1\le K<45$. The two
implementations share Python/Fraction and the stated mathematics, so these
are separate finite calculation paths, not independent external proof
authorities. The paper conclusions do not depend on the sample counts.

## 6. Comparison with the signed route and primary literature

The sibling at `a777aa99f541df2a0e2a0b8d57fef3f0940e465c`, CSI-01--03,
controls every temporal character of the local prime clock and bounds the
actual mixed source term by an **unpaid** complementary Fourier mass. The
sibling at `4b52cb87a19c2f599e5386fc12a9758bab12cba8`, MP-05--08, controls
relative Galois moments but leaves selected amplification unpaid. Those Git
objects were read, not merged or granted new authority on this branch.

The present obstruction does not weaken either signed route. Fixed-mode
cancellation concerns each fixed integer frequency; prescribed-depth collision
control also constrains increasingly fine concentration. SCE-03's normal de
Bruijn-repeat control remains a reason that failure of the latter cannot be
called a proof of nonnormality. The entropy identity (9) preserves a signed
difference of information quantities, in the same practical sense that keeping
complex Fourier signs avoids an unnecessary absolute-value loss; it is not a
physical analogy or a new cancellation theorem.

Primary sources checked during this track:

- Bailey--Crandall, [*Random Generators and Normal Numbers*](https://www.davidhbailey.com/dhbpapers/bcnormal.pdf),
  author's 20 March 2003 version. The introduction distinguishes proven sparse
  series classes from its conjectural rational-forcing Hypothesis A. We do not
  import Hypothesis A as a theorem about BBP.
- Bailey--Misiurewicz, [*A Strong Hot Spot Theorem*](https://www.davidhbailey.com/dhbpapers/dhb-mm-hotspot.pdf),
  13 February 2006, Theorem 1.1. Its interval-visit criterion concerns actual
  long-run orbit frequencies, not a finite Galois ensemble or a conditional
  distribution obtained by exposing its time index.
- Bourke--Hitchcock--Vinodchandran,
  [*Entropy Rates and Finite-State Dimension*](https://www.eecs.uwyo.edu/~jhitchco/papers/erfsd.shtml),
  authors' publication page. Its block-entropy characterization does not turn
  source description length or primary clock counts into normality.

No imported deep estimate is needed for (1)--(9). The next useful test for this
track is an authenticated bound on the mutual-information difference in (9),
or directly on cross-clock close pairs. Neither marginal clock entropy nor
conditional entropy after complete time reconstruction supplies that bound.

## 7. Independent derivation review of the lag arithmetic track

A separate reading of LA-01--05 found no error in the centering sign, the
integer-carry formula, the strict beta constants, or the close-run converse.
In particular, the converse is justified by the inverse maps preserving the
entire closed arc, not by endpoint membership alone. The irrational tracker
excludes an infinite uninterrupted run, while its finite return frequency
remains unpaid. The directional escape theorem applies only to a run starting
with nonpositive centered lag; it must not be promoted to a universal run bound.

The target-scale gate can be made completely explicit. On an actual prime
window $n\ge u+1$, the positive kernel gives

$$
0<f_{n,l}<r(n+1)<\frac{15}{(p+8)(p+9)}<\frac{15}{M}.
$$

For canonical $M\ge256$ this implies both LA-03 hypotheses, since
$17/M+f_{n,l}<32/M\le1/8<1$. At $M=16$ the gate indeed fails because
$17/M>1$. The first possible canonical level $M=256$ requires
$p\ge16^5$; smaller-prime runs at that resolution are diagnostic, not the
prescribed asymptotic schedule.

An additional exact scratch check, separate from the production lag module,
used the combined rational forcing displayed above. It compared direct
centered affine iteration with interval membership at $n\in\{1,2,10\}$,
$l\in\{1,3,20\}$, $\tau\in\{1/32,1/256\}$, and
$k\in\{0,1,2,4\}$ whenever the stated gate held. The input set was the
$1/64$ grid in $[-1/2,1/2)$, both interval endpoints, the midpoint, and points
$2^{-25}$ beyond each endpoint. All **4,140** admissible comparisons passed.
The two strict beta bounds and one-step forcing-difference monotonicity also
passed all **2,020** cases $0\le n\le100$, $1\le l\le20$. These counts are
finite review observations, not substitutes for LA-02/03's paper proofs.

The entropy track itself received a separate hostile review of its source
windows, fiber counts, boundary carries, and the scope of (8); no defect was
found. These are shared-model research checks, not external scholarly review.
