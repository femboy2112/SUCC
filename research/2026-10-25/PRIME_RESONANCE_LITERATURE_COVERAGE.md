# Prime-window coverage, imported estimates, and the cost of almost perfect resonance

Date: 2026-10-25. Baseline: `461942c0bf616518e668d236d1c6b1596665a7dd`.
Scope: independent arithmetic audit for Operation FUCC THE RESONANCE.
No assertion of authentic BBP cancellation, pi normality, or RH is made.

## 1. Literature authority and inherited results

The precise imported BGK statement is Kowalski's Theorem 1.1: for every
fixed gamma>0 there are C_gamma,nu_gamma>0 such that every prime p,
subgroup H of F_p^* with |H|>=p^gamma, and a not divisible by p satisfy
`|sum_(x in H) e(ax/p)| <= C_gamma |H| p^(-nu_gamma)`.
The constants depend only on gamma. This does not estimate arbitrary
correlated weights. No numerical exponent is assigned here.

Primary author exposition: [Kowalski, Exponential sums over small subgroups,
revisited, Theorem 1.1](https://people.math.ethz.ch/~kowalski/small-subgroups.pdf).
The original [BGK paper, JLMS 73 (2006), 380--398,
DOI 10.1112/S0024610706022721](https://doi.org/10.1112/S0024610706022721)
was checked through its publisher metadata/abstract; the accessible
full theorem/proof text used for the hypothesis audit was Kowalski's.

[Bailey--Crandall, Random Generators and Normal Numbers](https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf),
Theorem 2.2(5),(8), gives the normality/orbit and Weyl bridges. Its
Hypothesis 3.1 (Hypothesis A) is explicitly a conjectural alternative
between equidistribution and a finite attractor for the stated rational
forcing class. Their proved normality classes do not prove pi normality.
The paper's Theorem 3.2 supplies a vanishing-forcing orbit transfer; the
present project already has a sharper source-specific Green transfer.
It is not necessary to assume Hypothesis A in the reduction below.

[Kedlaya, Notes on analytic number theory, Theorem 4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html)
is the fixed-modulus PNT input: for fixed q and a coprime to q,
`pi(X;q,a) ~ X/(phi(q) log X)`. The modulus is fixed before X grows.
No uniform growing-modulus version is imported.

The following are **inherited**, not discoveries of this round:

- `BBP_CYCLOTOMIC_BIRTH_AND_LAG.md`, CBCW-04/05: small-order exceptional
  count and scale-four window equivalence.
- `BBP_PRIME_CLOCK_SPECTRAL_PROJECTION.md`, PSC-01/02/03/07: synchronized
  cosets, bounded short-period weights, conditional projection, coverage.
- `BBP_MINIMAL_PATH_GAUGE_AND_MISSING_PRIME.md`, MP-04: averaging the
  complement across repeated full prime periods and its exact cyclic DFT.
- `CYCLOTOMIC_SELECTED_INTERFERENCE.md`, CSI-01/02: all temporal twists
  controlled through the local autocorrelation identity, and a Wiener-norm
  conditional bound. Section 6 already quantifies the spectral complexity
  forced by coherent changed-initial-state controls.
- `CYCLOTOMIC_SELECTED_LEAN.md`, item 6: the finite twisted-clock identity
  and square bound have their own recorded Lean authority. This audit did
  not rerun that historical checker and does not promote its authority.

For example, writing S_chi=sum_(x in H) chi(x)e(ax/p), elementary expansion
gives `|S_chi|^2=sum_(z in H) chi(z) sum_(y in H)e(a(z-1)y/p)`.
BGK controls z!=1, so
`|S_chi|^2/|H|^2 <= 1/|H|+(1-1/|H|)C_gamma p^(-nu_gamma)`.
This tempting extension is already CSI-01; it must not be counted again.
Parseval still permits a broad anti-phase spectrum and total coherence.

## 2. Coverage proof with all quantifiers exposed

**Status: independently rederived inherited reduction; external PNT-AP.**

Fix an integer d>=1 and let G_d consist of primes p=1 mod 8d with
L_p=ord_p(16)>p^(1/3). Excluding the finitely many primes dividing a
fixed nonzero Fourier frequency h does not change the conclusions.

If p<=X has L_p<=p^(1/3), then p divides
`P_M=product_(k=1)^M (16^k-1)`, M=floor(X^(1/3)). Since
`log_2 P_M < 2M(M+1)`, there are at most 2M(M+1) distinct such primes.
For any fixed 0<epsilon<1, PNT-AP gives

```
# {p=1 mod 8d : (1-epsilon)X < p <= X}
    ~ epsilon X/(phi(8d) log X).
```

The exceptional O(X^(2/3)) count is smaller than this main term.
Consequently every sufficiently large fixed relative interval contains
a member of G_d. If g_d(X) is the largest such prime <=X, then
`(X-g_d(X))/X -> 0`. This last statement follows directly by applying
the preceding result for each epsilon; no effective rate is claimed.

Let |a_n|<=M_0, F(N)=sum_(1<=n<=N)a_n. For all large N choose
`p=g_d(2N+1)=8m+1`, so m<=N/4 and m=N/4+o(N). Then

```
|F(N)-F(floor(N/4))-[F(4m)-F(m)]|
 <= M_0 (N-4m + floor(N/4)-m)
 = o(N).
```

Thus `F(4m)-F(m)=o(m)` on G_d implies
`F(N)=F(floor(N/4))+o(N)`. Setting
`A=limsup |F(N)|/N`, boundedness gives `0<=A<=M_0`; taking limsups
gives A<=A/4 and hence A=0. The converse follows by subtraction.
For the authentic a_n=e(hU_n), the established Green transfer and Weyl
criterion give base-16 normality exactly when this premise holds for
every fixed nonzero h. The premise remains unproved.

The same elementary exceptional-product proof works for any fixed order
threshold p^theta with 0<theta<1/2, replacing O(X^(2/3)) by O(X^(2theta)).
This is a parameter extension of an inherited argument, not a new source
cancellation theorem. At theta=1/2 the crude count no longer pays the PNT
main term; that failure is a limitation of this estimate, not a theorem
that orders cannot be larger.

If d=d_p grows, the inequality `L_p/gcd(L_p,d_p)>=L_p/d_p` still holds
pointwise. However PNT in each fixed progression is not a uniform theorem
about a chosen growing progression. The analysis needs a separate
coverage proof for the actual selected family. A valid fixed d, including
d=1, avoids this additional obligation.

## 3. Sparse favorable windows are insufficient; averaged estimates suffice

**Status: proved bounded-sequence counterexample and reduction.**

Choose a sequence of good primes p_j=1 mod16 so large that their
`m_j=(p_j-1)/8` satisfy m_(j+1)>=16m_j. Such a sequence exists by Section
2. Each m_j is even. Put a_n=alternating +1,-1 on the disjoint windows
`m_j<n<=4m_j`, and put a_n=1 elsewhere. Every chosen window has sum zero.
But before the next window, at least the indices
`4m_j<n<=m_(j+1)` contribute +1, and all earlier complete windows have
zero sum. Hence `F(m_(j+1))/m_(j+1)>=3/4`. An arbitrary infinite
favorable good-prime subsequence is therefore not enough, even for
unit-modulus sequences. This is not an authentic BBP counterexample.

There is a useful alternate sufficient contract. Write
`b_p=|[F(4m)-F(m)]/(3m)|`, p=8m+1 in G_d, and assume

```
(1/#G_d(X)) sum_(p in G_d, p<=X) b_p^2 -> 0.
```

For any fixed eta>0, Markov's inequality makes the number of primes with
b_p>eta be o(X/log X). For any fixed epsilon>0, each relative interval
((1-epsilon)X,X] contains asymptotically a positive multiple of X/log X
eligible primes, so eventually some prime there has b_p<=eta. Taking
eta and epsilon arbitrarily small (or a diagonal sequence), the previous
scale-four proof applies. Conversely, F(N)=o(N) implies this mean-square
condition by boundedness and the usual finite-prefix/tail split.
This is an equivalent averaged proof contract, **not a saving already
proved for the BBP source**.

Prime averaging does not automatically create an independent Galois
variable. For any finite family P of p=8m+1, exact rearrangement gives

```
sum_(p in P) |W_p(h)|^2
 = sum_(n,r) e(h(U_n-U_r)) K_P(n,r),
K_P(n,r) = # {p=8m+1 in P : ceil(max(n,r)/4)<=m<min(n,r)}.
```

After the p-primary and p-free factors recombine, e(hU_n) is independent
of which eligible window contains n. A large-sieve or trace-function
argument must establish the relevant structural hypotheses; it cannot
invent independent coefficients by splitting this same source twice.

## 4. Authentic forcing excludes almost perfect coherence quantitatively

**Status: paper theorem, independently derived; new finite obstruction in
this round. It does not assert decay of the authentic signed mean.**

Let D=3m>=2, n_0=m+1, and let any real circle trajectory obey the exact
BBP forcing on the window, with any initial state. Fix an integer h!=0. Define

```
z_t=e(h X_(n_0+t)),                 0<=t<D,
f_t=e(h r(n_0+t+1)),              0<=t<D-1,
A=(1/D)sum_t z_t,
V_f=(1/(D-1))sum_t |f_t-mean(f)|^2.
```

Then `z_(t+1)=z_t^16 f_t` and

```
1-|A| >= (D-1)V_f/(578D)
       >= 8/[289D(D-1)]
          sum_(0<=i<j<D-1) dist(h(r(n_0+i+1)-r(n_0+j+1)), Z)^2.    (1)
```

**Proof.** Choose c=A/|A| if A!=0, otherwise any unit c. Since z and c
are unit complex numbers, telescoping the sixteenth powers gives

```
|f_t-c^(-15)| <= |z_(t+1)-c|+16|z_t-c|.
```

The real inequality `(a+16b)^2<=17a^2+272b^2` therefore implies
`sum_t |f_t-c^(-15)|^2 <=289 sum_t|z_t-c|^2
=578D(1-|A|)`. Variance minimizes the sum of squares over all complex
centers, giving the first inequality in (1). For M=D-1,
`V_f=M^(-2)sum_(i<j)|f_i-f_j|^2`. The circle chord bound
`|e(x)-e(y)|>=4 dist(x-y,Z)` gives the second inequality. No independence,
prime-order, source positivity, or floating-point approximation was used
in this finite algebra; the exact forcing supplies the right side.

Using the independently proved source inequalities in
`SUCC_INTERNAL_MATRIX_WALK.md`,

```
0 < 15/64 - n^2 r(n+1) < 7/(5n),
```

one gets an explicit consequence. If m>=11 and m^2>=|h|, choose the m
early forcing indices m+2,...,2m+1 and the m late indices 3m+1,...,4m.
Monotonicity and the displayed inequality give every early-minus-late
gap at least

```
r(2m+1)-r(3m+1)
 >= 25/(768m^2)-7/(40m^3)
 >= 1/(64m^2).
```

All forcing differences are smaller than `r(m+2)<15/(64m^2)`, so
the condition m^2>=|h| ensures no wrap in their distances to Z. There
are m^2 early/late pairs. Inserting them into (1) gives

```
1-|A| >= h^2/(1331712 m^4).                                  (2)
```

This theorem applies in particular to the authentic zero-initial BBP
window, including the selected product u_t v_t. It refutes exact unit
coherence there. Its lower bound vanishes with m and therefore does not
rule out a fixed nonzero limiting correlation, or even |A| tending to 1.

## 5. Sharp scale of the forcing obstruction and its boundary

**Status: paper asymptotics; no numerical extrapolation.**

Write a=15/64 and average over the M=3m-1 forcing indices
n=m+2,...,4m. The exact source estimate implies uniformly there
`r(n)=a n^(-2)+O(n^(-3))`. Riemann sums give

```
m^2 mean(r) -> a/4,
m^4 mean(r^2) -> 7a^2/64,
m^4 Var(r) -> 3a^2/64 = 675/262144.
```

For fixed h, the Taylor expansion of the pairwise chord square is
`|e(hx)-e(hy)|^2=(2pi h)^2(x-y)^2+O_h((x-y)^4)` uniformly when x,y
are O(m^(-2)). The variance pair identity therefore proves

```
m^4 V_f -> 675 pi^2 h^2/65536,
liminf m^4(1-|A|) >= 675 pi^2 h^2/(65536*578).                 (3)
```

The liminf claim holds for any sequence of window initial states, since
(1) is uniform in those states. Equation (3) concerns a lower bound on
coherence deficit; it is not an asymptotic formula for authentic |A|.

The exponent four cannot be improved uniformly over all initial states
with this exact forcing. Let alpha=sum_(n>=1)16^(-n)r(n)=pi/16 and
`T_n=sum_(j>=1)16^(-j)r(n+j)`. Choosing X_0=-alpha makes
`X_n=-T_n` exactly. The geometric tail and source asymptotic give
`T_n=1/(64n^2)+O(n^(-3))`. For the window n=m+1,...,4m,
the same variance calculation, now using
`1-|mean(z)|=(1-|mean(z)|^2)/(1+|mean(z)|)`, proves

```
m^4 [1-|mean_(m<n<=4m)e(-h T_n)|]
    -> 3 pi^2 h^2/131072.                                    (4)
```

For each window, rational initial states with denominator a power of 3
can approximate -alpha with error `o(16^(-4m)m^(-4))`. Their forced
trajectories differ by `16^n` times this initial error, so their window
means differ by o(m^(-4)); they reproduce (4). Their denominators stay
odd, and their p-primary component agrees with the authentic one for
every p!=3. They obey the same forcing but **not the required initial
state X_0=0**. These are window-dependent counterfeit controls, not an
authentic-source counterexample and not one fixed rational orbit claimed
to have the limiting behavior (4).

Thus a proof of authentic cancellation must use the selected initial
state together with its full history. Forcing nonconstancy supplies a
real finite exclusion, whose best possible uniform order is m^(-4);
it cannot by itself supply an o(1) upper bound for |A|.

## Claim and next-probe ledger

| Claim | Authority | Boundary |
|---|---|---|
| BGK and fixed-modulus PNT hypotheses | Externally checked | No fabricated constants or growing-modulus uniformity |
| Complete-period DFT and twisted BGK/Wiener bound | Inherited MP-04/CSI-01/02 | Do not count as new |
| Scale-four and fixed-d coverage | Reproved inherited reduction | Source cancellation premise remains open |
| Sparse good-prime subsequence suffices | Refuted by unit-sequence construction | Not a BBP counterexample |
| Prime mean-square condition suffices | Proved reduction | Equivalent target, not proved estimate |
| Exact-forcing coherence gap (1)--(3) | Proved on paper | Excludes only near-unit coherence at quantified scale |
| Uniform m^(-4) scale cannot improve | Proved changed-initial-state construction | Authentic zero initial state excluded from counterfeit |
| Authentic signed prime windows vanish | UNVERIFIED | Need selected-state signed decorrelation, not another weight-blind bound |

Next falsification: compare a proposed authentic cancellation estimate
against the exact-forcing rational initial-state controls in Section 5.
If it cannot distinguish initial zero from those controls, its uniform
claim must pay at least their measured coherence. Finite authentic
samples can falsify constants or monotonicity, but cannot prove the
required all-prime asymptotic.
