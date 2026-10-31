# Moving conductors, exact character fields, and the selected coherence cylinder

**PROVED LOCAL means a paper derivation.** These proofs have exact finite cross-checks and same-model complementary review, not an external referee or a Lean proof. No scholarly priority is asserted. The authentic four poles and zero boundary are unchanged. **No new fixed-frequency selected SC-06 bound is proved here.**

Let `den(x)` be the positive reduced denominator of a rational, `e(x)=exp(2πix)`, and `P_p` the canonical p-primary projection on Q/Z. The inherited, source-authenticated CG01 theorem states

`log den(U_n)=6n+o(n)`.

Its external input is the prime number theorem in fixed arithmetic progressions; its source proof and exceptions remain those of [the parent dossier](../../arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md). In particular, p19 and p73 cancellations are not discarded. The fixed-polynomial version below was already CG03; it is not counted again as new.

## CT-01 — uniform conductor growth for every sublinear moving lag

Let `P_n(z)=sum_(j=0)^(d_n) b_(n,j) z^j` have integer coefficients. Assume

- `d_n=o(n)`;
- `log(max(1,sum_j |b_(n,j)|))=o(n)`;
- `M_n=P_n(16) != 0`.

Then, for the actual zero-seed source,

\[
\boxed{\log\operatorname{den}(P_n(E)U_n)=6n+o(n).}\tag{CT1}
\]

In particular, **uniformly along every sequence of positive lags `d_n=o(n)`**,

\[
\log\operatorname{den}(U_{n+d_n}-U_n)=6n+o(n).
\]

This extends the inherited fixed-lag theorem to all sublinear lags, including `d_n` much larger than `n/log n`. It is an arithmetic constraint, not a real separation or cancellation estimate.

**Short-interval LCM lemma.** For integers `m>=0,s>=1`,

\[
\operatorname{lcm}(m+1,\ldots,m+s)
\mid {m+s\choose s}\operatorname{lcm}(1,\ldots,s).       \tag{CT2}
\]

To prove this prime by prime, put `k=max_(m<t<=m+s) v_p(t)` and `a=floor(log_p s)`. At each power `p^j`, the interval contains at least `floor(s/p^j)` multiples, so every summand in the valuation of the binomial coefficient is nonnegative. If `k>a`, each level `a<j<=k` contributes one. Consequently its valuation is at least `max(0,k-a)`, while the small LCM supplies `a`. This proves divisibility. The elementary binomial estimate and `psi(s)=O(s)` give

\[
\log\operatorname{lcm}(m+1,\ldots,m+s)
\le s\log\frac{e(m+s)}s+O(s).                          \tag{CT3}
\]

**Exact denominator inequalities.** For one filter of degree d, iterate the actual recurrence:

\[
P(E)U_n=M U_n+R_n,\qquad
R_n=\sum_{t=1}^d\left(\sum_{j=t}^d b_j16^{j-t}\right)r(n+t).
\]

Let `D=den(U_n)`, `Q=lcm_(1<=t<=d) den(r(n+t))`, and `V=den(P(E)U_n)`. For d=0 use Q=1. Then

\[
V\mid DQ,\qquad D/\gcd(D,M)\mid VQ,
\qquad \frac D{|M|Q}\le V\le DQ.                     \tag{CT4}
\]

Indeed `den(MU_n)=D/gcd(D,M)` divides the product of the denominators of `P(E)U_n` and `R_n`, and `den(R_n)|Q`. All denominators used in Q divide the LCM of the consecutive integers `8n+1,...,8n+8d`. Apply CT3 with `m=8n,s=8d`:

\[
\log Q=O\!\left(d\log\frac{n+d}{d}+d\right)=o(n)
\]

when d=o(n). Also `log|M| <= log(sum|b_j|)+d log16=o(n)`. Taking logarithms in CT4 and applying inherited CG01 proves CT1. ∎

For a fixed nonzero integer h, multiplying by h costs at most `log|h|` in conductor. Deleting the primary components of any set `S_n` with `|S_n|=o(n/log n)` also costs o(n): every prime-power factor in the filtered denominator is at most `8(n+d_n)`, because the filter has integer coefficients and each original state denominator divides the source LCM through `n+d_n`. Thus the complementary root retains `exp(6n+o(n))` order after both operations.

This does not give a bound for its selected complex argument. Large order is compatible with a root arbitrarily close to one. A low-energy cylinder can contain high-order roots.

## CT-07 — the full finite-field character-value field needs growing extension degree

Fix an odd prime p and extension degree f>=1. Permit **all** ordinary additive and multiplicative characters over `F_(p^f)`, not merely the eighth-order family. All their values, finite sums, products, quotients, and Galois conjugates lie in

\[
K_{p,f}=\mathbb Q(\zeta_{p(p^f-1)}).
\]

This statement describes the complete available character-value field. It does **not** assert that the particular BBP weighted Gauss products generate that entire field.

Let v be rational with reduced odd denominator D, `(D,p)=1`. Then

\[
\boxed{e(v)\in K_{p,f}\iff D\mid p^f-1.}\tag{CT5}
\]

The same necessary condition holds after adjoining any roots of unity of 2-power order, or conventional Tate square-root normalizations contained in `Q(zeta_(4p(p^f-1)))`.

**Proof.** If D divides `p^f-1`, the field includes `zeta_D`. Conversely, since `e(v)` is a primitive D-th root, membership implies
`Q(zeta_lcm(D,p(p^f-1)))=Q(zeta_(p(p^f-1)))`.
An extra odd prime-power factor increases the cyclotomic degree: an added prime contributes its factor `ell-1>1`, and an added exponent contributes `ell>1`. Thus no extra odd factor can occur. Because `(D,p)=1`, D must divide `p^f-1`. Extra 2-primary roots do not change this odd-factor argument. ∎

For D>1 the **least** extension degree for membership in this complete field is therefore

\[
\boxed{f_{\min}=\operatorname{ord}_D(p).}\tag{CT6}
\]

This is an exact field-membership statement, not an algorithm identifying the cofiber with a naturally arising Gauss sum. Inserting the already-known selected numerator as a multiplicative-character exponent would merely encode the answer.

For the authentic p-complement `v_(n,p)=U_n-P_p(U_n)`, fixed h!=0, and `D=ord(e(hv_(n,p)))`, inherited CG01 and the bound `p`-primary denominator `<=8n` imply **uniformly in p**

\[
\log D=6n+o(n).
\]

Hence exact reconstruction in the declared family requires

\[
\boxed{f\ge\frac{\log(D+1)}{\log p}
      =\frac{6n+o(n)}{\log p}.}\tag{CT7}
\]

At native first births `n~p/8`, this is `f >= (3/4+o(1))p/log p`. Thus bounded extension degree cannot produce the full complementary character at sufficiently large native births, even when every multiplicative-character order over that extension is admitted. The same argument applies to the moving filtered cofibers of CT1.

Exact selected examples (h=1):

| p | n | D | minimum f |
|---|---:|---:|---:|
| 13 | 2 | 315 | 12 |
| 19 | 5 | 4108329225 | 2520 |
| 73 | 10 | 8153867029599816525 | 240240 |
| 1033 | 130 | full integer in receipt | 79485107315235635798288344798367669127511763134382323790061621715934060448000 |
| 1061 | 133 | full integer in receipt | the same exact integer as the preceding row |

The last equality is a finite exact observation, not a new law. The receipt factors D into prime powers, gives the order at each factor, and verifies minimality by removing every prime divisor of f.

**Scope.** This excludes an exact bounded-extension-degree architecture built from the stated finite-field character values and field operations. It does not exclude approximate transport, prime-power additive characters, arbitrary sheaves with externally supplied coefficient fields, separately adjoined Gross–Koblitz uniformizers, unrestricted roots, analytic limits, or inequalities. It proves no selected signed saving.

## CT-02/03/06 — the actual coherence cylinder and its boundary ambiguity

Fix a nonzero integer h. Write `x_j=h(U_(A+j+1)-U_(A+j)) mod1`. Its full, source-correct evolution is

\[
x_{j+1}=16x_j+f_j\pmod1,\qquad
f_j=h(r(A+j+2)-r(A+j+1)).
\]

The p-primary and complementary factors are both retained in this formula. Fix `0<delta<1/17` and suppose `17 delta+max|f_j|<1`. Put `g_0=0`, `g_(j+1)=16g_j+f_j`. Every centered phase of a length-L window lies in `[-delta,delta]` **if and only if** its initial centered phase lies in the exact rational, possibly empty, interval

\[
\boxed{\bigcap_{j=0}^{L-1}
 [16^{-j}(-\delta-g_j),\ 16^{-j}(\delta-g_j)].}\tag{CT8}
\]

Indeed if two consecutive centered phases lie in the small arc, their integer wrap has magnitude at most `17delta+|f_j|<1`, hence is zero. Induction gives `x_j=16^j x_0+g_j`; the converse follows by substitution. The intersection has length at most `2delta16^{-(L-1)}`, with length zero for an empty intersection. Since the initial seed enters the lag by the integer multiplier `15h16^A`, this is also an upper bound for the Lebesgue measure of the all-coherent seed set modulo one.

This exact cylinder is a representation and finite certificate, **not a new universal selected bound**. Exponentially small measure does not exclude the one selected point. Finite irrationality exponent supplies the inherited exclusion only on windows much longer than SC-06.

A sharp reason to retain the literal boundary is available without assigning p-adic values to an irrational seed. For any fixed finite A,L, form the rational Green prefix

`T_A^[R]=sum_(j=1)^R 16^-j r(A+j)`, `R=L+padding`.

Let `t` be the centered representative of `-U_A-T_A^[R]`, choose an integer m nearest `16^R t`, and set

\[
s=\frac m{16^{A+R}}.
\]

Then `|s|<=16^-A`. The positive tail remainder is bounded by
`16^-R r(A+R+1)/15`, so all lag distances on `[A,A+L)` are at most

\[
\frac{16}{(8A+1)^3}
+15\,16^{L-1}\,16^{-R}
  \left(\frac12+\frac{r(A+R+1)}{15}\right).             \tag{CT9}
\]

The numerator-rounding error contributes the first term inside parentheses; homogeneous transport multiplies it by `16^j`, and taking the lag contributes15. The inherited SB1 bounds the coherent real lag `D_n`. Choosing the padding large makes this smaller than delta whenever the source-tail threshold allows it.

For **every odd prime and every time**, this rational seed has exactly the same primary trajectory as the authentic seed:

`P_p(U_n(s))=P_p(U_n(0))`,

because the difference `16^n s` is dyadic. At every n>=A+R it is an integer, so the two trajectories are **exact circle aliases from then on**. No asymptotic normality failure is demanded of this rational translate.

The ambiguity has an exact converse: for rational seeds s,t, equality of all odd-primary data (at n=0 or any fixed n) holds iff `s-t` has power-of-two denominator. Hence all-time odd-primary data determine the *eventual* real-circle orbit among rational seeds, although they do not give a uniform finite-window onset. The finite shadow refutes a boundary-blind finite-window assertion, not eventual normality and not a theorem whose hypothesis is literally s=0.

At fresh p1033 and p1061, the exact authentic initial phase is outside CT8; the constructed tiny dyadic shadow is inside for respectively128 and264 lag steps. All full lag distances of the shadows are below1/20. This demonstrates a real joint correlation effect with identical odd-primary data: the complementary factor restores coherence. The selected zero boundary must be used quantitatively to exclude this alignment, not merely mentioned.

**The direct SC-06 attempt remains DARK.** To force a positive fraction, one must exclude the authentic zero-boundary coordinate from the union of source-determined cylinders allowing fewer than rho L slips, uniformly for eligible p. CT8 solves the zero-slip cylinder exactly and the raw probes locate the actual point, but no arithmetic inequality controls the larger union uniformly. Its thin measure, high conductor, and complete source reconstruction do not provide that exclusion.

## CT-05 — prime-power top digits do not give a complete primary character

Before the next Q=p^a-divisible source pole after its first birth, put
`P_p(U_n)=a_n/Q mod1`. Then

\[
a_{n+1}=16a_n+Q P_p(r(n+1))\pmod Q.
\]

Lower p-valuation source poles contribute multiples of p to the second term. Therefore `a_n mod p` propagates purely under16, but the complete p^a-primary character generally does not. This is the time-window version of the inherited precision-layer obstruction, not a new Hensel theorem.

At Q=121, b=16, the next Q pole is n=61, yet already n=17 breaks the pure full-primary orbit. Its mod11 top digit still follows16 exactly. The same controlled failure occurs for Q=343,169,361,5329 at n87,23,48,694 respectively. Omitting those lower layers in a prime-power character estimate is invalid even for the authentic zero seed.

## CT-08 — exact polynomial degree on the annihilating branch

For completeness, inherited CG03's `O(log n)` branch can be made exact. Fix a nonzero integer polynomial P with P(16)=0, and write `P(z)=(z-16)Q(z)`. Let s be the number of nonzero coefficients of Q. Then

\[
\boxed{\operatorname{den}(P(E)U_n)=\Theta_P(n^{4s}).}\tag{CT10}
\]

Indeed `P(E)U_n=Q(E)r(n+1)`. The reduced source is

`r(n)=(120n^2-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)]`.

Each nonzero shifted source contributes four simple poles. Their four fractional parts are distinct, and integer shifts cannot identify poles from different times. Thus a common-denominator polynomial D(n) of degree4s has no common root with the summed numerator N(n). Their nonzero integer resultant bounds `gcd(N(n),D(n))` by a fixed constant, while D(n) is comparable to n^(4s). This proves CT10. It is an exact arithmetic refinement, with no additional signed consequence. Four small quotient polynomials and20 evaluations were checked by symbolic resultants and direct rational states.

## Executed results and boundaries

- **13 focused tests passed**; no floating trigonometry is used in the slip certificates.
- **48 fresh joint primary/cofiber/full rows**, including24 SC-06-eligible rows, all have at least half their lag distances >=1/20. The smallest fraction is39/44 at p1069,h3. This is finite observation only.
- The independent oracle reconstructed all48 rows using a reduced rational source and integer numerator/denominator updates, not the four-pole Fraction implementation. It checked both shadows,12 inverse-branch cylinders, and27,786 short-interval prime-valuation comparisons.
- **41 filter certificates** and25 short-LCM cases obey the exact inequalities, including an explicitly typed annihilator.
- Five prime-power windows retain pure top mod-p transport and refute pure complete-primary transport.
- The seven-pole null source has zero slips in the declared127-lag control; authentic has119, wrong-ratio110, same-ratio114, and rank-matched-ratio115. Passing this lag test neither identifies BBP nor proves normality.
- Original p19 disappearance at n10..16 and p73,n274 cancellation are preserved exactly.

Raw outputs and command metadata are in `receipts/`. Separate implementations check finite algebra; the asymptotic claims rest on the displayed proofs and the inherited conductor theorem. The original source provenance, author attribution and historical theorem contracts are not changed.
