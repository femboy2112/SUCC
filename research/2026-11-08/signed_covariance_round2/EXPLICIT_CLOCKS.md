# Quantitative original-source clocks and explicit observer budgets

**PROVED PAPER with stated classical imports.** This changes the prime
observer selection, never the original four-pole forcing or literal U0=0.
The previous selector and all its receipts remain intact. The full original
signed covariance, pi normality and RH remain **OPEN**.

## EC1. A computable stronger selector pays an epoch-gluing rate

Fix an integer C>=1. For each prime p let b(p)=floor(log_2 p)+1 and
m(p)=ord_p(16). Define p_A^(C) as the largest prime p<=4A satisfying

`p=1 mod8, m(p)^3>p, m(p)^2 b(p)^(2C)>p`.

The selector need only be defined for sufficiently large A; finite software
returns an explicit absence if its set is empty. All predicates are integer
predicates. For every fixed real B with 0<B<2C, eventually

`0 <= 4A-p_A^(C) <= 4A/(log(4A))^B`.                    (EC1)

**Proof.** Put X=4A and w=X/(log X)^B. For p in [X-w,X], b(p) is bounded
below by a fixed positive multiple of log X. If the second order predicate
fails then m(p)<=K_C sqrt(X)/(log X)^C, for a constant K_C. If the first
order predicate fails, m(p)<=X^(1/3), which is smaller than that threshold
eventually. Let Y be an integer upper bound of this order. Every rejected
prime in the interval divides the integer

`V_Y=product_(j=1)^Y(16^j-1)`.

Distinct such primes divide V_Y, so their count times log(X-w) is at most
log V_Y, which is strictly less than (log16)Y(Y+1)/2. Thus the rejected
count is O_C(X/(log X)^(2C+1)).

The **quantitative fixed-modulus PNT/AP**, imported for modulus8, is
pi(x;8,1)=Li(x)/4+O(x exp(-c sqrt(log x))). Subtract its values at X and
X-w. The difference of Li values is asymptotic to w/log X, and the two
errors are negligible relative to it. Consequently the count of candidate
primes in the interval is asymptotic to X/[4(log X)^(B+1)]. Since B<2C,
this exceeds the rejected count for all sufficiently large X. One eligible
prime exists there; the largest eligible prime is at least that large. QED.

The exact PE source genealogy applies because p=1mod8 and the old good-order
predicate is retained. Set L=(p-1)/4 and I=[L+1,2L+1). Then m divides L,
the original local source is e(xi16^r/p) on I, and L<A. Write d=A-L>=1;
indeed p=1mod4 and p<=4A imply p<=4A-3. The overlap of I and J=[A,2A)
has size max(0,A-2d+1). Their exact normalized weight distance therefore gives

`eps_A=sum_n |1_J/A-1_I/L| <= 4d/A`.

Using d=(4A-p+1)/4, EC1 yields

`eps_A <= 4/(log(4A))^B+1/A` eventually.                 (EC2)

Finite certificates use the exact weight distance, not this asymptotic bound.
No numerical threshold A0 or explicit PNT error constant is asserted.
For C=2 we may choose B=3. There is no claim of a power saving in gluing.

## EC2. An explicit classical local bound replaces an unspecified exponent

Cochrane--Pinner, *Explicit bounds on monomial and binomial exponential
sums*, Theorem1.1, supplies, for any multiplicative subgroup G of F_p^*,
|G|=m, and c!=0 modp,

`|sum_(x in G)e(cx/p)| <= min(sqrt(p),
 lambda m^(3/8)p^(1/4), lambda m^(5/8)p^(1/8))`,
`lambda=2/3^(1/4)`.

Their paragraph immediately after Theorem1.2 explicitly states that each
bound is valid outside its indicated optimality range. The constants and
ranges have therefore not been inferred from an abstract or search snippet.
Their proof uses the additive-energy bound E(G)<=(16/3)m^(5/2) for
m<p^(2/3), together with the classical Gauss bound for larger subgroups.
This is a **classical imported theorem**, not a new SUCC exponential-sum proof.

For normalized S(c)=m^-1 sum_G e(cx/p), define the exact rational cap

`D8(p,m)=min(1,p^4/m^8,(256/9)p^2/m^5,(256/9)p/m^3)`.

Then uniformly in c!=0,

`|S(c)| <= delta_CP(p,m):=D8(p,m)^(1/8)`                 (EC3)

for every prime and every subgroup. The eighth power makes a finite bound
computable by rational arithmetic and integer root enclosure without rounding
the irrational constant lambda. It is not an asymptotic fit.

For the EC1 selector, m>sqrt(p)/b(p)^C. Substitution in the third bound gives

`delta_CP(p,m) <= lambda p^(-1/16)b(p)^(3C/8)`.          (EC4)

This is a uniform explicit local power exponent, with logarithmic cost.
The actual-source epoch estimate, for every h not divisible by p, is

`|A^-1 sum_(n=A)^(2A-1)e(h[U_n(0)]_p)| <= eps_A+delta_CP`.

For C=2, the right side is O((log A)^(-3)), with the finer local term
lambda p^(-1/16)b(p)^(3/4) and exact finite eps retained. This does not
bound e(hU_n); the complementary factor has not disappeared.

## EC3. Consequences for nonlinear history and sparse predictors

The cube and chronology theorems are stated for any valid uniform subgroup
bound delta, so EC3 can replace their unspecified BK bound on this selector.
No other change to their proofs is needed.

1. **Cyclic cubes.** For every integer j>=1, uniformly in nonzero xi,
   `||e(xi16^r/p)||_(U^j)^(2^j) <= (j-1)b(p)^C/sqrt(p)
                                  +lambda^2 p^(-1/8)b(p)^(3C/4)`.
   Thus every fixed c<1/8 gives an eventual bound exp(-c log p/2^j)
   when2^j=o(log p). The degeneracy lower bound still makes this depth
   threshold necessary for this norm.
2. **Larger sparse models with the same residual requirement.** CQ6 proves
   leakage on any s Fourier modes is at most
   `[s(1/m+delta_CP^2)]^(1/4)`.
   Therefore an original folded-complement residual tending to zero on
   `s=o(p^(1/8)/b(p)^(3C/4))` modes suffices for Weyl decay. The old
   maximum-bin argument with this same delta only permits
   `s=o(p^(1/16)/b(p)^(3C/8))` as a uniform sufficient budget.
   This is a strict relaxation of a conditional sparsity premise; the
   original residual estimate remains **OPEN**. No predictor is manufactured.
3. **Growing observed local histories.** CH4's digit-word total-variation
   bound tends to zero whenever
   `16^d b(p)^(3C/8+1)/p^(1/16) ->0`.
   In particular any fixed0<eta<1/16 permits
   `d=floor((1/16-eta)log_16 p)` eventually. This concerns the empirical
   digit histories of the original **p-local projection**, compared to
   the deterministic ×16 trajectory of a Haar initial circle point.
   It asserts neither product independence of exact circle histories nor
   normality of the full source. Complete histories still have modular
   resonances and the finite-support information horizon proved in CH5.

All three deductions are uniform over allowed source-dependent choices of
the finite observer. Shared source, classical imports and proof dependencies
are counted once, not as independent evidence.

## EC4. The remaining signed gate with explicitly bounded overhead

Use the exact-forcing covariance Gamma and R from hostile/H2 on the EC1
selector. Choose H_A=min(m_A,floor(sqrt(A))), for sufficiently large A.
Then H_A<=m_A, H_A=o(A), and H_A is bounded below by a constant multiple
of sqrt(A)/b(p_A)^C. Consequently H_A->infinity and

`|W_A(h;0)|^2 <= ((A+H_A-1)/A) * [1/H_A+R_(A,h)(H_A)
              +(1-1/H_A)(eps_A+delta_CP)
              +(H_A^2-1)/(3H_A A)]`.                  (EC5)

Every overhead term is now explicit at a finite epoch. Asymptotically their
sum is O((log A)^(-B)) for fixed B<2C. Therefore

`original-zero limsup R_(A,h)(H_A)<=0 for every fixed h!=0`
`=> full real Weyl decay => pi base16 normality`.

The first line is the unpaid signed estimate. By hostile/H3, this prescribed
aperture target is equivalent to normality, not a proved weaker conjecture.
The new contributions are the stronger source-local bounds, larger conditional
observer budget, and quantified costs of the reduction. They do not infer
that source authentication or local uniformity supplies the missing sign.

## Sources and scope

- [Cochrane--Pinner author manuscript, Theorem1.1 and the paragraph after1.2](https://www.math.ksu.edu/~cochrane/research/binsum7.pdf),
  published Q. J. Math.62 (2011),323--349, DOI10.1093/qmath/hap041.
  Root read the statement, its global-range clarification and proof reduction.
- [Rudnick, fixed-modulus PNT/AP, Section2, printed page2](https://www.math.tau.ac.il/~rudnick/courses/sieves2015/fixed%20progressions.pdf).
  The quantitative PNT is a declared standard import. Root and chronology
  independently verified the shrinking-interval subtraction and order count.
- Original PE1--9 at pinned1990b051 supply source genealogy, clean interval
  and exact principal parts. Root and chronology independently derived EC1--2.
- The2020 Di Benedetto et al. subgroup theorem was investigated but is not
  needed here; its small-group range must not be applied blindly above sqrt(p).

All new results are paper proofs with exact finite implementation checks.
No external refereeing, numerical A0, or Lean certification is claimed.
**Pi base16 normality: OPEN. RH: OPEN.**
