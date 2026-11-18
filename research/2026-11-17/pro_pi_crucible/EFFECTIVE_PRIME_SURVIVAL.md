# Effective survival of the original BBP prime inventory

## Status and novelty boundary

**PROVED LOCAL (paper proof), with finite exact checks.** This note retains precisely
`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, and
`U_n=16U_(n-1)+r(n)`. It improves the finite-prime survival statement in
`research/2026-10-30/arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md` (CG-01)
from a fixed-epsilon, unspecified-threshold statement to an explicit finite
certificate and a shrinking cutoff of order `n/log n`.

**Already established, not rediscovered:** `log den(U_n)=6n+o(n)`, the fixed
filter dichotomy, all-class Frobenius packet transport, and the existence of
actual prime cancellations (19 and 73). The rate-6 result was independently
recovered during this attack, then correctly retired as a novelty claim when
CG-01 was found. This note does not count that rediscovery as progress.

**Not established:** any terminal-wall lower bound, R0, swept Borwein
convergence, or pi normality. Prime survival controls reduced fractional
arithmetic; integer winding remains missing from this estimate. The proof
also survives any fixed rational seed at primes outside its denominator, so
it cannot by itself select the literal-zero signed orbit.

## 1. Exact objects and statement

For integer n>=1 define

```
L_n = lcm{2j-1,4j-1,8j-7,8j-3 : 1<=j<=n},
U_n = N_n/Q_n in lowest terms, Q_n>0.
```

Call an odd prime p **born by n** if p divides L_n. For p>7 its first birth
is at `(p+7)/8` in class 1 mod8, `(p+3)/8` in class 5 mod8, and `(p+1)/4`
in classes 3,7 mod8.

**EPS-01 (finite certificate).** Suppose p is prime,

```
p>7, p^2>8n, p | L_n, K=floor((8n-2)/p).
```

Then K>=1 and

```
p^2 >= 19*32^K  ==>  v_p(U_n)=-1.
```

This is a sufficient certificate, not an equivalence: many surviving primes
do not satisfy this coarse height inequality.

**EPS-02 (shrinking cutoff).** For every real A>20 log(2), there is an
effective integer n_A such that, for every n>=n_A and every born prime
p>=A n/log n, `v_p(U_n)=-1`. In particular if M_n is the largest born prime
that is missing from Q_n (zero if there is none),

```
limsup_(n->infinity) M_n log(n)/n <= 20 log(2).
```

**EPS-03 (effective denominator saturation).** `Q_n | L_n` and

```
0 <= log(L_n/Q_n) = O(n/log n).
```

More explicitly, for any real Y>=max(7,sqrt(8n)) satisfying

```
Y^2 >= 19*32^(8n/Y),
```

all born primes strictly larger than Y survive, and

```
0 <= log(L_n/Q_n)
   <= log(4)*Y + sqrt(8n)*log(8n).
```

The prime number theorem is not needed for EPS-01--03. Combining EPS-03
with the *inherited* prime inventory asymptotic `log L_n=6n+o(n)` recovers
CG-01; this recovery is not a new normality result.

## 2. Exact normalized local coefficient

Use the identical simplified four-pole presentation

```
r(j)=4/(8j-7) - 1/[2(2j-1)] - 1/(8j-3) - 1/[2(4j-1)].
```

Set `j0=(p+1)/2`, `chi=1` for p=1,7 mod8 and `chi=-1` for p=3,5 mod8.
The normalization `16^(n-j0)` is a nonzero element of F_p even if n-j0 is
negative. For each source lane `(a,b,c)` in

```
(8,7,4), (8,3,-1), (4,1,-1/2), (2,1,-1/2),
```

include each odd k>=1 for which `j=(kp+b)/a` is an integer in `[1,n]`.
Define the rational F=F_(n,p) by summing the corresponding entries:

| Lane | Rational contribution to F |
|---|---|
| (8,7,4) | `(4/k)*chi*2^((1-k)/2)` |
| (8,3,-1) | `(-1/k)*chi*2^((5-k)/2)` |
| (4,1,-1/2) | `-2^(2-k)/k` |
| (2,1,-1/2) | `-2^(1-2k)/k` |

All k<=K<p, because p^2>8n. Thus F is p-integral. Exactly

```
[p U_n]_p = 16^(n-j0) [F_(n,p)]_p.
```

**Derivation.** A p-divisible denominator `aj-b=kp` contributes
`(c/k)16^(n-j)` to `[pU_n]_p`; all other terms contribute zero. The
hypothesis p^2>8n ensures every denominator has at most one p factor.
Normalize by `16^(n-j0)`. For a=8,

```
4(j0-j) = ((4-k)(p-1) + 8-k-b)/2.
```

Euler's criterion `2^((p-1)/2)=chi` and odd k give the two displayed
powers. For a=4,

```
4(j0-j)=(2-k)(p-1)+(3-k),
```

and for a=2,

```
4(j0-j)=2(1-k)(p-1)+2(1-k).
```

Fermat's identity gives the remaining rows, including their original signs.
No artificial prime clock or random residue law has been inserted.

## 3. Nonzero rational sign for every admissible entry pattern

The source lanes are not independently switched in the proof. At any time
n each lane has its chronological initial segment, and first birth is
retained. The following bounds even allow arbitrary later subsets, so they
cover every authentic entry pattern.

For p=1 mod4 the possible lane contributions, indexed by l>=0, are

```
+4*16^(-l)/(8l+1),
-  16^(-l)/(8l+5),
-(1/2)*16^(-l)/(4l+3),
-(1/2)*16^(-l)/(2l+1).
```

Birth always includes the first positive term +4. Consequently

```
F >= 4 - (1/5+1/6+1/2) sum_(l>=0)16^(-l)
  = 692/225 > 0,
F < 4 sum_(l>=0)16^(-l) = 64/15.
```

The strict upper inequality follows because only finitely many terms are
present. The arithmetic congruences for classes 1 and 5 interchange the two
8j pole lanes but give exactly the same four numerical series.

For p=3 mod4 the possible lane contributions are

```
-2*16^(-l)/(4l+1),
-2*16^(-l)/(8l+3),
-(1/2)*16^(-l)/(2l+1),
+(1/2)*16^(-l)/(8l+7).
```

Birth includes the first negative term -2. Hence

```
F <= -2 +(1/14) sum_(l>=0)16^(-l) = -202/105 < 0,
F > -(2+2/3+1/2) sum_(l>=0)16^(-l) = -152/45.
```

Thus in every class F is nonzero and `|F|<64/15`. Nonzero over Q does
**not** automatically mean nonzero modulo p; the next height bound pays
that remaining arithmetic debt.

## 4. A self-contained coefficient-height bound

Let `Lambda_K=lcm(1,...,K)`.
Every k appearing above is at most K. The power-of-two denominator of each
8j-lane coefficient is at most `2^floor(K/2)`. For the 4j lane,
`kp<=4n-1` gives `2k<=K`, and its denominator exponent is at most `max(0,k-2)`.
For the 2j lane, `kp<=2n-1` gives `4k<=K`, and its denominator exponent is
at most `2k-1`. Thus, writing F=A/D in lowest terms with D>0,

```
D | 2^floor(K/2) Lambda_K.
```

### Elementary lemma: Lambda_K <= 4^K for every K>=1

Put t=ceil(K/2). The quotient `Lambda_K/Lambda_t` is squarefree: no prime
can acquire two new powers when the upper endpoint grows by a factor at
most two. For every prime dividing this quotient there is a prime power
q in `(t,K]`; the factorial valuation formula gives a contribution 1 from
q to `binom(K,floor(K/2))`. All its other valuation contributions are
nonnegative. Hence

```
Lambda_K/Lambda_t | binom(K,floor(K/2)).
```

Use strong induction. If K=2m, the binomial coefficient is at most 4^m,
so `Lambda_K<=4^m Lambda_m<=4^(2m)`. If K=2m+1 with m>=1, its two equal
middle binomial coefficients have total at most `2^(2m+1)`, so each is at
most 4^m; therefore `Lambda_K<=4^m Lambda_(m+1)<=4^(2m+1)`. K=1 is immediate.

It follows that

```
|A|^2 < (64/15)^2 * 2^K * (4^K)^2
      = (4096/225)*32^K
      < 19*32^K.
```

If `p^2>=19*32^K`, then `0<|A|<p`. Since p does not divide D, F cannot
vanish modulo p. The normalized principal-part identity proves EPS-01.
The inequalities are one-sided and finite: no limiting argument or
floating-point comparison occurs here.

## 5. The n/log n cutoff

Fix A>20 log2 and put `Y=A n/log n`. For large n, `Y>max(7,sqrt(8n))`.
For every p>=Y, `K<=8n/p<=8 log n/A`. Thus

```
log(19*32^K) <= log19 + (40 log2/A) log n,
2 log p >= 2 log n - 2 log log n + 2 log A.
```

The coefficient `40 log2/A` is strictly smaller than 2, so the second
line eventually exceeds the first. This verifies EPS-01 uniformly over
all p>=Y. This proves EPS-02. For rational A the threshold is effective. Put c=2-40 log(2)/A>0.
Choose log(n_A)>=max(2,2/c), then increase n_A until
`c log n_A-2 log log n_A+2 log A-log19>=0` and
`A n_A/log n_A>max(7,sqrt(8n_A))`. Both inequalities remain true
afterwards by monotonicity (differentiate in log n). Certified logarithm
bounds make the finite searches effective. For a real A, take an
intermediate rational value between 20 log2 and A. No ineffective
Diophantine theorem is used.

## 6. Saturation of the full native denominator

The four-pole collapsed identity

```
r(j)=(120j^2-89j+16)/[(2j-1)(4j-1)(8j-7)(8j-3)]
```

shows that r(j) has odd denominator. The four simple fractions show that
`den(2r(j))` divides the LCM of their four odd denominators. Since r(j)
is 2-integral, `den(r(j))=den(2r(j))`, so `den(r(j))|L_n`. Integer radix
weights therefore imply `Q_n|L_n`.

For any Y as in EPS-03, every born prime p>Y survives with exponent one.
Such primes cannot have higher powers in L_n, since Y>=sqrt(8n). Therefore
all factors of the integer `L_n/Q_n` are supported at p<=Y. The contribution
of their first powers is at most

```
sum_(p<=Y) log p <= log Lambda_floor(Y) <= Y log4.
```

All higher powers have p<=sqrt(8n). There are at most sqrt(8n) possible
such primes, and all powers of each contribute at most log(8n). Their total
contribution is at most `sqrt(8n)log(8n)`. This proves the explicit inequality
in EPS-03. Take `Y=A n/log n` for a fixed A>20log2. Since
`sqrt(n)log n=o(n/log n)`, the asserted O(n/log n) follows.

Small primes, primes with p^2<=8n, and their powers have therefore been
accounted for; they have not been declared noncancelling. No exclusion of
known exceptions is hidden in the statement.

## 7. Hostile receipts and conclusion

The exact script `prime_survival_probe.py` compares the literal four-pole
Fraction recurrence with the collapsed polynomial source and independently
computes the normalized finite-prime coefficient above. Before computation
it fixed n=17,33,65,129,257,513,1025. Results:

- 1,665 exact principal-part comparisons passed.
- 988 instances satisfied the sufficient cutoff and survived in Q_n.
- 1,662 sign-reversed nonzero residue mutations were rejected.
- p=19 at n=10,...,16 gives F=-19/6 and genuinely disappears.
- p=73 at n=274 gives F=357201535487/113700787200 and genuinely disappears.
- Neither hostile cancellation satisfies the sufficient height cutoff.
- The holdouts also retained cancellations at (n,p)=(129,37),(257,47),(513,113);
  none satisfies the cutoff. Their exact normalized coefficients are in the receipt.

This is finite implementation validation of the paper formulas, not the
source of the universal theorem. The original theorem/probe assumptions
remain intact; no failed prime has been deleted.

**Exact remaining obstruction:** every principal part of a rational U_n
is unchanged by adding an integer. Thus even complete prime support,
all local principal parts, the new mesoscopic survival bound, and exact
terminal fraction can coexist with arbitrarily different low integer
hexadecimal digits. The existing terminal-cofactor clone supplies that
counterexample. To reach R0, a new inequality must constrain the actual
zero-seeded integer quotient C_(2B) and its radix residue tower; no such
positive wall-density lower bound is derived here. This observation does
not fix the 2-adic residue modulo 16^B. The later M-02 classification adds
that datum and explicitly restricts the compatible words; it still does
not exclude their low-wall subset.

### Inspected source heads

- Main: `81be6b897ae980b801a3b9de9e22ef81e8360bfb`.
- #657: `7e406514ffdd1dac932cdfa6a0e1bf12b8059ebf`, particularly
  BBP_POLE_SHIFT_CRUCIBLE.md, BBP_TWO_FORMULA_LOCKED_COUNTERMODEL.md.
- #662: `fc723029eddd7d3f32dff12218cd9c6bfa916f84`, terminal_domain_walls/THEOREMS.md.
- #660: `6ece172c5f7faa22955129374cb93db005316c94`, prime_path_nerve/THEOREMS.md.
- Inherited CG-01--03, AT-01--07 and PF-01--08 as present at the pinned main.

No external priority claim, external referee claim, or Lean claim is made.

## 8. Closing FQR refinement: lane-restricted height, with normalization repaired

The closing source at 9ff8544c799b5e4c8eb1db33127438bc3f221045 introduces
a useful smaller denominator envelope for the normalized coefficient.
Credit for the lane restriction belongs to its FQR-05. Its printed
normalization is incorrect; the rational coefficient used above satisfies
F=16 C, term by term, where C is that paper's FQR-02 coefficient.

For K=floor((8n-2)/p) and r=p mod4 in {1,3}, put

\[
S(K,r)=\{1\le k\le K:k\equiv r\pmod4\}
\cup\{1\le k\le K/2:k\text{ odd}\},
\quad H(K,r)=2^{\lfloor K/2\rfloor}\operatorname{lcm}S(K,r).
\]

**Corrected finite certificate EPS-FQR.** Under EPS-01's other hypotheses,

\[
p^2\ge19H(K,r)^2\quad\Longrightarrow\quad v_p(U_n)=-1.
\]

**Proof.** In the two 8j lanes the odd multiplier k satisfies k=p mod4;
the two shorter lanes have k<=K/2. Thus den(F) divides H(K,r), retaining
the same power-of-two factor as the earlier proof. The chronological sign
argument already gives 0<|F|<64/15. For F=a/d reduced,

\[
0<a^2<(4096/225)H(K,r)^2<19H(K,r)^2\le p^2.
\]

Hence p does not divide a. Also d is prime to p because K<p when p^2>8n.
The authentic principal-part congruence then proves the assertion. QED.

For a fixed r, the first-power prime support of lcm S(K,r) comprises
all odd primes <=K/2 and the primes congruent to r mod4 up to K. The
fixed-modulus prime number theorem gives logarithmic weight 3K/4+o(K).
Additional powers cost O(sqrt K log K)=o(K). Therefore

\[
\log H(K,r)=(\tfrac12\log2+\tfrac34+o(1))K.
\]

The same height comparison now proves eventual survival for every born
p>=A n/log n whenever A>4 log2+6. For unbounded K, compare log p with
log H at the cutoff; bounded K is covered by its finite height bound.
The original explicit elementary EPS certificate remains valid. This
refinement improves its sufficient constant; it does not prove that the
new constant is optimal and is not a signed real-circle estimate.

The imported fixed-modulus theorem was checked in the author's primary
paper, Ivan Soprounov, Theorem 2.1 and its weighted formulation:
[A short proof of the Prime Number Theorem for arithmetic progressions](https://academic.csuohio.edu/soprunov-ivan/wp-content/uploads/sites/93/2023/02/primes.pdf).
The finite certificate itself uses no prime-distribution theorem.
The normalization counterexample and exact scope are retained in
audits/FQR_FRONTIER_ADDENDUM.md and evidence/fqr_minimal_arithmetic.json.
