# BBP causal memory: contracting binary windows and retained ternary boundary

## Scope and provenance

**PROVED, source-specific corollary of inherited arithmetic.** Throughout,

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad n\in\mathbb Z_{\ge1}.
\]

The state is the unreduced mathematical rational value; using a reduced
fraction to compute its valuations does not change the source. For a rational
\(z\), let \(d_3(z)=3^{\max(0,-v_3(z))}\), with \(d_3(0)=1\).

The principal inherited result is [T1, the selected ternary
height theorem](../../2026-11-04/gamma_prybar/front7/TERNARY_DEPTH.md), present at
commit `6318eed7952c13d6869a2950f17e7df47363380d` and in this operation's base
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`. It already determines the genuine
state height for every \(n\ge11\), using a modulus-27 certificate. Its T2 and
T3 already prevent promotion of this local control to real normality. Section
1 gives a shorter, modulus-9 organization of the same height information,
including the finite initial range. This is an **alternative proof and
compression of an inherited result**, not a new normality estimate or a
claim of mathematical priority. Section 2 records the moving-window consequence
that matters for a causal observer.

The binary time-to-state isometry, ternary cleared-numerator isometry, and
failure of an infinite backward ternary source sum are separately proved in
[First-Primal Recursion](../../2026-10-27/BBP_PRIMAL_RECURSION_2ADIC_3ADIC.md).
The variable held fixed matters: contraction below concerns **differences
between states under the same future forcing**, whereas the binary isometry
concerns the map from **time** to authentic state.

## 1. A compact certificate for the inherited ternary height

For each integer \(j\ge1\), put \(q=9^j\) and define the integer endpoints

\[
a=\frac{q+7}{8},\quad b=\frac{q+1}{2},\quad
c=\frac{5q+3}{8},\quad d=\frac{3q+1}{4},\quad
e=\frac{9q+7}{8}.
\]

Then \(a(9q)=e(q)\), so these intervals partition all \(n\ge2\).
The complete certificate is:

| Time range | Exact local observation | \(d_3(U_n)\) |
| --- | --- | ---: |
| \(a\le n<b\) | \(qU_n\equiv1\pmod3\) | \(q\) |
| \(b\le n<c\) | \(qU_n\equiv2\pmod3\) | \(q\) |
| \(c\le n<d\) | \(qU_n\equiv6\pmod9\) | \(q/3\) |
| \(d\le n<e\) | \(3qU_n\equiv1\pmod3\) | \(3q\) |

At \(n=1\), \(U_1=47/15\), so \(d_3(U_1)=3\) and
\(3U_1\equiv1\pmod3\). All congruences are in the localization
\(\mathbb Z_{(3)}\), after the displayed scaling has made the value integral.

### Proof of the first, second and fourth rows

Expand the genuine finite source history:

\[
U_n=\sum_{t=1}^n16^{n-t}
\sum_{(f,s)\in\{(7,4),(4,-2),(3,-1),(2,-1)\}}
\frac{s}{8t-f}.
\]

Since \(q\equiv1\pmod8\), the first three raw denominators divisible by
\(q\) that occur before \(d\) are \(q,4q,5q\). Their arrival times are
\(a,b,c\), and their contributions to \(qU_n\) modulo 3 are respectively
\(4,-2/4,-1/5\), each equal to 1. There is no raw denominator divisible by
\(3q\) before \(d\). All denominators of smaller ternary depth disappear
after multiplication by \(q\) and reduction modulo 3. Also \(16\equiv1\pmod3\).
This proves the first two rows and the cancellation modulo 3 in the third.

The first denominator of depth \(2j+1\) is \(6q\), at time \(d\), with
source coefficient \(-1\). Its contribution to \(3qU_n\) is \(-1/2\equiv1\)
modulo 3. It is the only such denominator before time \(e\), when \(9q\)
enters. This proves the fourth row.

### Resolving the cancellation row modulo 9

For \(c\le n<d\), consider \(h=q16^{-n}U_n\) modulo 9. Only raw denominators
divisible by \(q/3\) can contribute. Write such a denominator as \(m(q/3)\).
All contributing denominators in this range have entered by \(c\), and the
possible \(m\) are exactly \(2,3,4,7,10,11,12,15\). Indeed \(q/3\equiv3\pmod8\),
the four admitted residues of a raw denominator are \(1,4,5,6\), and the next
admitted multiple \(18(q/3)\) arrives at \(d\).

The entry time is \(t=(m(q/3)+f)/8\), so \(t\equiv2f\pmod3\). Since
\(16^3\equiv1\pmod9\), the following table computes every contribution without
depending on \(j\):

| \(m\) | Pole offset \(f\) | Source coefficient \(s\) | \(16^{-t}3s/m\pmod9\) |
| ---: | ---: | ---: | ---: |
| 2 | 2 | -1 | 3 |
| 3 | 7 | 4 | 1 |
| 4 | 4 | -2 | 3 |
| 7 | 3 | -1 | 6 |
| 10 | 2 | -1 | 6 |
| 11 | 7 | 4 | 6 |
| 12 | 4 | -2 | 1 |
| 15 | 3 | -1 | 7 |

Their sum is \(33\equiv6\pmod9\). Multiplication back by \(16^n\) preserves
6 modulo 9. Hence \(qU_n\equiv6\pmod9\), proving the third row. This proof
works already for \(q=9\). No limiting interchange or numerical approximation
is used. QED.

Two useful consequences, now including every \(n\ge1\), are

\[
\boxed{d_3(U_n)\ge3,\qquad \frac49n<d_3(U_n)\le8n.}
\]

For the lower bound the smallest ratio occurs in the third interval, where
\(n\le d-1=(3q-3)/4\) and \(d_3(U_n)=q/3\). The other rows satisfy the same
bound directly. The upper bound follows because no source denominator exceeds
\(8n\), and taking a rational sum cannot introduce a larger ternary denominator
than the maximum present among its summands.

The first occurrence of depth \(k\ge1\) is therefore

\[
n_k=\begin{cases}
(3^k+7)/8,&k\text{ even},\\
(3^k+1)/4,&k\text{ odd},
\end{cases}
\quad v_3(U_{n_k})=-k,\quad3^kU_{n_k}\equiv1\pmod3.
\]

**Development correction retained:** the preliminary odd-\(k\) expression
\((3^k+3)/8\) was wrong: for \(k=3\) it is not an integer. The correct first
raw denominator is \(2\cdot3^k=8n_k-2\), not \(3^k=8n_k-3\).

## 2. The exact moving-window asymmetry

Let \(n,L\) be integers with \(0\le L\le n\), set \(t=n-L\), and define
the **zero-initialized trailing window** of the authentic source by

\[
V_{n,L}=\sum_{s=t+1}^n16^{n-s}r(s).
\]

This is a finite probe of the original trajectory; the source and its global
zero seed have not been changed. The probe simply drops the state incoming at
time \(t\). Finite recurrence unwinding gives

\[
\boxed{E_{n,L}:=U_n-V_{n,L}=16^LU_t.}
\]

### CM-1. Binary forgetting and ternary retention

**For every \(n\ge0\) and \(0\le L\le n\):**

\[
|E_{n,L}|_2\le2^{-4L}.
\]

If \(t=0\), the error is exactly zero at every place. If \(t\ge1\), then

\[
\boxed{|E_{n,L}|_3=d_3(U_t)\ge3,\qquad
\frac49t<|E_{n,L}|_3\le8t.}
\]

**Proof.** The exact canceled source expression is

\[
r(s)=\frac{120s^2-89s+16}{(2s-1)(4s-1)(8s-7)(8s-3)}.
\]

Every denominator factor is odd, so \(r(s),U_t\in\mathbb Z_2\). Thus
\(|16^LU_t|_2\le2^{-4L}\). At the ternary place 16 is a unit, hence
\(|16^LU_t|_3=|U_t|_3=d_3(U_t)\) for \(t\ge1\); Section 1 supplies the
stated bounds. QED.

Thus a trailing window of length \(\lceil m/4\rceil\) is uniformly enough to
recover the binary state modulo \(2^m\). A trailing window omitting even one
initial step cannot recover the actual ternary state modulo \(\mathbb Z_3\)
when it substitutes zero for the incoming boundary state. This is an all-time
source-specific statement, not an inference from a positive-density sample.

### CM-2. Growing late windows do not repair the ternary reset

For any integer sequences \(n\to\infty\), \(0\le L_n\le n\), and
\(t_n=n-L_n\):

- If \(L_n\to\infty\), then \(|E_{n,L_n}|_2\to0\).
- If \(t_n\to\infty\), then \(|E_{n,L_n}|_3\to\infty\).
- If \(t_n\ge\varepsilon n\) for fixed \(\varepsilon>0\), then
  \(|E_{n,L_n}|_3/|U_n|_3>\varepsilon/18\).

The final assertion uses \(d_3(U_{t_n})>(4/9)t_n\) and
\(d_3(U_n)\le8n\). A sublinear recent window therefore cannot become a
relatively accurate ternary reconstruction either.

### What the observer must retain

Keeping the boundary value \(U_t\), or its appropriate ternary residue at the
requested precision, repairs the probe exactly:

\[
U_n=16^LU_t+V_{n,L}.
\]

This does **not** require storing every old event. A sufficient state can
compress the history. A source model may also recompute a past boundary; that
is a present computation about the past, not a reversed causal trajectory.
The mathematical conclusion is that the same rule for dropping a boundary
has different errors at different places. It supplies no physical arrow of
time, thermodynamic irreversibility, or noncomputability claim.

## 3. Why this is not yet an arithmetic-to-real cancellation theorem

1. Inherited T2 preserves exact reduced denominators and all nonternary
   principal parts, and changes only the least singular
   \(O(\log\log n)\) ternary positions, while an altered zero-seeded forcing
   concentrates the real orbit. Thus even near-complete ternary height data
   can miss the load-bearing real signed phase.
2. Inherited T3 proves a genuine ternary occupancy bound
   \(O(\sqrt A+D)\) in a dyadic time shell. The same dossier explains how
   most pairwise local denominators can survive a real-concentrating
   alteration. Local occupancy cannot be relabeled real-circle occupancy.
3. The old [3-adic Memory Theorem](../../2026-10-27-ravel-prime-ladder/THREE_ADIC_MEMORY_THEOREM.md)
   correctly motivates logarithmic *ternary depth*, but its displayed claim
   about the logarithm of the **full** denominator does not follow from a
   bound on \(v_3\). Its assertion that transcendence or aperiodicity gives
   positive digit entropy is false. The repository already records the
   decisive [Kempner firewall, FK-1](../../2026-10-27-furstenberg-kempner/KEMPNER_FURSTENBERG_FIREWALL.md),
   including a transcendental sparse-digit counterexample with zero orbit
   entropy and empirical limit \(\delta_0\). This operation preserves that
   repair rather than treating the archived false bridge as a live theorem.

An elementary additional receipt for the last point is
\(\alpha=\sum_{j\ge1}16^{-j!}\): Liouville approximation proves transcendence;
the unbounded gaps between nonzero digits prevent eventual periodicity; and
for each fixed block length, nonzero-digit blocks have density zero. Its
empirical orbit measures tend to \(\delta_0\). Its word complexity is at most
\(3m+1\) for words of length \(m\): choose the first factorial gap larger
than \(m\); its left endpoint is at most \(2m\), and all later words contain
at most one nonzero digit. Thus its topological entropy is also zero.

**Next missing edge:** a bound involving the authentic ordered real phases
and their retained arithmetic boundary, which rejects both changed-forcing
controls and source-matched boundary mistakes. The present theorems prove
local causal-memory asymmetry. R0, base-16 normality of pi, Collatz, and RH
remain open.

## 4. Exact cycles of a rational source snapshot

### CM-3. Authentic snapshots exclude short exact autonomous cycles

For \(n\ge1\), write \(U_n=A_n/B_n\) in lowest terms with \(B_n>0\), and
let \(u_n=\{U_n\}\). Let \(\ell_n\) be the least positive period of the
**autonomous** circle map \(x\mapsto\{16x\}\) starting at \(u_n\). Then

\[
\boxed{
\ell_n=\operatorname{ord}_{B_n}(16),\qquad
3^{h_n-1}\mid\ell_n,\qquad
\ell_n\ge\frac{d_3(U_n)}3>\frac{4n}{27},
}\qquad h_n=v_3(B_n)\ge1.
\]

**Proof.** The source states have odd reduced denominators, so 16 is
invertible modulo \(B_n\). Since \(\gcd(A_n,B_n)=1\),

\[
\{16^kU_n\}=\{U_n\}
\iff B_n\mid16^k-1.
\]

For every integer \(k\ge1\), binomial expansion and successive cubing give
the classical lifting identity

\[
v_3(16^k-1)=1+v_3(k).
\]

Consequently \(\operatorname{ord}_{3^h}(16)=3^{h-1}\) for every \(h\ge1\).
As \(3^{h_n}\mid B_n\), this local order divides \(\ell_n\). The final
inequality follows from Section 1. QED.

The first exact checks are:

| \(n\) | \(B_n\) | \(\ell_n\) | Forced divisor \(3^{h_n-1}\) |
| ---: | ---: | ---: | ---: |
| 1 | 15 | 1 | 1 |
| 2 | 4095 | 3 | 3 |
| 3 | 765765 | 30 | 3 |
| 4 | 111035925 | 210 | 3 |
| 5 | 78058255275 | 630 | 3 |
| 6 | 24536311574775 | 6930 | 1 |
| 7 | 81926744348173725 | 90090 | 9 |

**Novelty and scope.** The order formula is classical; the source height is
inherited T1; inherited T3 already uses the same local order in a ternary
occupancy argument. CM-3 records their immediate source-specific consequence
as an explicit snapshot nonresonance lemma. The autonomous orbit of \(u_n\)
is not the genuine forced future \((u_{n+k})_{k\ge0}\). Nor is it the
irrational completed snapshot \(\{U_n+T_n\}\). None of these different
trajectories is silently substituted for another.

### Period grids and the cyclic source filter

The points fixed by the \(k\)-fold autonomous map form exactly

\[
\operatorname{Fix}(\times16^k)
=\left\{\frac{a}{16^k-1}\bmod1:
a\in\mathbb Z\right\}.
\]

Thus the integer \(16^k-1\) that occurs in the cyclic source-filter closure
is also the denominator of the complete period-dividing-\(k\) grid. This is
an exact algebraic identification of the grid, not a statement about the
frequency with which authentic snapshots approach it. CM-3 implies that
\(u_n\) does not belong to that grid when \(k<4n/27\).

More precisely, [CSF-08](CYCLIC_SOURCE_FILTERS.md) gives
\(\operatorname{coker}H(S_{8k})\cong
(\mathbb Z/(16^k-1)\mathbb Z)^4\). Applying the coordinate map
\(a\mapsto a/(16^k-1)\pmod1\) identifies this group with four copies of
\(\operatorname{Fix}(\times16^k)\). This is an identification of the declared
filter's obstruction group with a periodic-point group. It does not assert
that the authentic source phase is a filter obstruction coordinate.

### Long periods do not exclude close short-cycle shadows

There is a simple hostile control retaining **the full denominator and the
entire autonomous period** at every time. Define

\[
z_0=0,\qquad z_n=\frac1{B_n}\quad(n\ge1).
\]

Then \(z_n\) has the same reduced denominator \(B_n\), the same ternary
height, and the same autonomous period \(\ell_n\) as \(u_n\), yet

\[
0<z_n\le\frac1{d_3(U_n)}<\frac9{4n}\longrightarrow0.
\]

In particular, for every integer \(B\ge1\),

\[
\frac1B\sum_{n=B}^{2B-1}\bigl(1-\cos(2\pi z_n)\bigr)
\le\frac{81\pi^2}{8B^2}\longrightarrow0.
\]

This is a single rational, zero-seeded **altered-forcing** sequence, with
\(\widetilde r(n)=z_n-16z_{n-1}\). It does not satisfy the original four-pole
law. It decisively refutes an inference from even exact source denominator
and autonomous-period data alone to real anti-locking.

More generally, a fixed ternary factor permits exponentially close shadows:
for \(h\ge1\) and \(M\ge1\),

\[
y=\frac1{3^h(16^M+1)}
\]

has ternary height \(3^h\), autonomous period divisible by \(3^{h-1}\), and
distance less than \(16^{-M}/3^h\) from the fixed point 0. The cofactor
\(16^M+1\) is odd and prime to 3. These auxiliary rational examples do not
claim to be authentic BBP snapshots; they identify exactly what a period or
valuation argument leaves uncontrolled.
