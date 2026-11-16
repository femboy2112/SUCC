# The failed-carry endpoint set has exact dimension 7/8

**Status: proved, for the fixed authentic BBP tail and arbitrary completed
endpoints.** This is a second-pass theorem. It does not decide whether the
specific endpoint \(\pi/16\) belongs to the set.

## 1. The set and the source attachment

Keep the literal four-pole source

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad T_n=\sum_{j\ge1}16^{-j}r(n+j).
\]

The inherited bounds are
\(0<T_n<1/(64n^2)\). For \(\beta\in[0,1)\), put

\[
C_n^\beta=\lfloor16^n\beta-T_n\rfloor,\qquad
d_B(\beta)=\frac1B\sum_{B\le n<2B}
  \mathbf1_{\{C_n^\beta\bmod4\in\{1,2\}\}}.
\]

This is exactly the original recurrence with seed
\(s=\beta-\alpha\), where \(\alpha=\pi/16\). Only
\(\beta=\alpha\) has the required zero seed.

Define

\[
E=\{\beta\in[0,1):\liminf_{B\to\infty}d_B(\beta)=0\}.
\tag{E1}
\]

Here and throughout, \(B\) ranges over **all positive integers**.
The mask-transfer theorem T3 in [TRANSLATOR_NOTES.md](TRANSLATOR_NOTES.md)
gives, uniformly over \(\beta\),

\[
|d_B(\beta)-\widetilde d_B(\beta)|\le\varepsilon_B\longrightarrow0,
\]

where \(\widetilde d_B\) counts the completed hexadecimal digits with
residues one or two. Therefore E is precisely the set defined by
\(\liminf_B\widetilde d_B=0\). The floor and fixed source tail do not
change this set.

## 2. The theorem

\[
\boxed{\dim_{\mathrm H}E=\frac78.}
\tag{E2}
\]

The dimension refers to the usual Euclidean metric on the interval.
The endpoint conventions use the terminating base-sixteen expansion
where two expansions are possible; the countable ambiguity does not
change the dimension.

### Upper bound

Let

\[
G=\{0,3,4,7,8,11,12,15\}
\]

be the eight unselected symbols. A word of length B with exactly k
selected symbols has \(\binom Bk8^B\) possibilities: choose its selected
positions, then one of eight symbols at every position.

Fix \(0<\eta<1/2\). Standard binomial counting, or the elementary
exponential-moment bound, gives

\[
\sum_{k\le\eta B}\binom Bk
\le \exp(BH_2(\eta)),
\quad H_2(\eta)=-\eta\log\eta-(1-\eta)\log(1-\eta).
\tag{E3}
\]

One direct proof weights each summand by
\(\eta^k(1-\eta)^{B-k}\). For \(k\le\eta B\), this weight is at least
\(\exp[-BH_2(\eta)]\), and the sum of all binomial probabilities is one.

Before the shell \([B,2B)\), its \(B-1\) preceding digits are unrestricted.
Consequently the condition \(\widetilde d_B\le\eta\) can be covered by at most

\[
16^{B-1}8^B e^{BH_2(\eta)}
\tag{E4}
\]

cylinders of depth \(2B-1\), each with diameter \(16^{-(2B-1)}\).
Every element of E satisfies this condition for infinitely many B.
The sum of the s-powers of the cylinder diameters converges if

\[
2s\log16>\log16+\log8+H_2(\eta).
\]

It follows that

\[
\dim_{\mathrm H}E
\le\frac{\log16+\log8+H_2(\eta)}{2\log16}.
\]

Let \(\eta\downarrow0\) to obtain \(\dim_{\mathrm H}E\le7/8\).

### Matching lower bound

Choose explicit integers \(B_k=2^{2^k}\), \(k\ge1\). Their shells are
disjoint, \(2B_k<B_{k+1}\), and

\[
\frac{\sum_{j<k}B_j}{B_k}\longrightarrow0.
\]

Construct a compact digit set by restricting digits to G on each interval
\([B_k,2B_k)\), while allowing all sixteen symbols elsewhere.
Every such endpoint has \(\widetilde d_{B_k}=0\), hence belongs to E after
the tail transfer. Countable expansion ambiguities can be removed.

Let \(F(n)\) count restricted positions among the first n digits.
Within a restricted interval its density increases; in the following
free interval it decreases. Its successive maxima occur at
\(n=2B_k-1\), where

\[
\frac{F(2B_k-1)}{2B_k-1}
=\frac{B_k+\sum_{j<k}B_j}{2B_k-1}\longrightarrow\frac12.
\]

Thus \(\limsup_nF(n)/n=1/2\).

Give each allowed digit equal probability, independently at every
position. A nonempty depth-n cylinder has probability exactly

\[
16^{-(n-F(n))}8^{-F(n)}
=2^{-4n+F(n)}.
\tag{E5}
\]

For every \(s<7/8\), this is at most \(16^{-sn}\) for all sufficiently
large n. If
\(16^{-(n+1)}<|I|\le16^{-n}\), an interval I meets at most two
depth-n cylinder interiors, apart from measure-zero endpoints. Therefore

\[
\mu(I)\le2\,16^{-sn}\le2\,16^s|I|^s.
\]

The elementary mass-distribution argument now gives dimension at least s:
any sufficiently fine cover has
\(\sum |I|^s\ge1/(2\,16^s)\). Let \(s\uparrow7/8\).
Together with the upper bound, this proves (E2).

The proof uses \(s<7/8\). It does not claim a uniform Frostman constant
at the critical exponent: the earlier forced blocks contribute an
unbounded, sublinear factor in (E5).

## 3. What was gained, and what was not

The failed-gate set is now exactly calibrated, not just measure zero or
bounded by an unspecified exceptional class. Its dimension is \(7/8\).
The signed three-count failure set is much larger in the entropy bound:
the translator's pressure argument only bounds its dimension by
approximately \(0.99742447485\). This difference records the additional
clock-orientation cost of that particular sufficient certificate.

The remaining source problem is

\[
\boxed{\alpha=\pi/16\notin E.}
\tag{E6}
\]

Equation (E6) is **equivalent to the selected positive lower shell
density**, since the densities are nonnegative. The dimension theorem is
a genuine quantitative statement about its complementing class, but it
does not establish this arithmetic exclusion.

Neither transcendence nor a finite irrationality exponent supplies such
an exclusion. A particularly strong inherited control is

\[
\beta_{\rm TM}=3\sum_{k\ge1}t_k16^{-k},
\quad t_0=0,\quad t_{2k}=t_k,\quad t_{2k+1}=1-t_k.
\]

The Thue--Morse sequence has no three consecutive zeros. Thus
\(3/4096\le\{16^n\beta_{\rm TM}\}\le1/5\), and no tail borrow occurs
for \(n\ge5\). Its digits remain zero or three, so
\(d_B(\beta_{\rm TM})=0\) for every \(B\ge5\). It also has restricted
power-sixteen approximation exponent zero. Bugeaud's theorem gives
ordinary irrationality exponent exactly two, preserved by rational
scaling. This control was already in
[WINDING_PACKETS.md](../carry_quadrature_assault/WINDING_PACKETS.md);
its application to E is the new comparison here.

The control survives every finite prefix. For any length-N hexadecimal
prefix represented by \(0\le A<16^N\), put
\[
\beta_A=\frac{A+\beta_{\rm TM}}{16^N}.
\]
It lies in that prefix cylinder, still has ordinary irrationality exponent
two by rational affine invariance, and still has restricted exponent zero.
After its prefix its digits are the same zero/three Thue--Morse tail;
the fixed BBP tail cannot cause a borrow once \(n\ge\max(N+1,5)\).
Thus \(\beta_A\in E\). In particular,
\[
E\cap\{\beta:\mu(\beta)=2,\ v_{16}(\beta)=0\}
\quad\hbox{is dense in }[0,1).
\]
This is a family of infinite controls with arbitrarily prescribed finite
real data. One must not assume that a particular \(\beta_A\) differs from
\(\pi/16\): excluding that equality would itself require a digit argument.
To guarantee a nonzero alternative seed in the same cylinder, use the two
tails \(\beta_{\rm TM}/16\) and \((3+\beta_{\rm TM})/16\) after A.
Both retain the stated properties, differ from each other, and therefore
at least one differs from \(\pi/16\). Finite disjoint enclosures can select
such an alternative without deciding equality for the other one.
These controls are not asserted to retain rational source states.
The rational deep-dyadic controls in the adversary note are a different
family; their finite typing and this family's infinite Diophantine
properties must not be silently combined.

Primary reference: Yann Bugeaud, *On the rational approximation to the
Thue--Morse--Mahler numbers*, Annales de l'Institut Fourier 61 (2011),
2065--2076, [journal record](https://www.numdam.org/item/AIF_2011__61_5_2065_0/).
The source-selection boundary is unchanged: this endpoint uses a changed
real seed, not the canonical zero seed.

## 4. Independent audit and novelty boundary

The adversary reviewed the upper cylinder count, all-integer-shell
quantifier, lower product construction, and critical-exponent caveat in
[EXCEPTIONAL_SET_AUDIT.md](EXCEPTIONAL_SET_AUDIT.md). The two derivations
use the same elementary digit-counting framework and are not an external
referee or formal kernel proof.

The theorem is established here by its complete proof. No claim of
external scholarly priority is made. Its arithmetic consequence for
\(\pi/16\), and hence the current carry-density gate, remains open.
