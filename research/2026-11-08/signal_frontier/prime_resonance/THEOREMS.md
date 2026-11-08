# Algebraic resonance exclusion on stronger authenticated prime clocks

**PROVED PAPER, with explicit classical imports. Pi normality: OPEN. RH: OPEN.**
This front proves a new original-source local-character estimate relative to
this repository's inspected frontier. Its complement certificate remains
conditional. The underlying finite-field estimates are classical; worldwide
novelty, external refereeing and Lean certification are not claimed.

Throughout `e(t)=exp(2pi i t)`. Preserve exactly

```
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
U0=0,  Un=16 U_(n-1)+r(n).
```

For an odd prime, `[U]_p` means the canonical rational principal part, not
reduction of a real floating approximation. All integer carries and unwrapped
states remain unchanged. Source authentication is inherited from PE1–9 and
checked against literal source histories separately.

## PR1. A computable super-square-root order selector with epoch coverage

Write `b(p)=floor(log_2 p)+1`, `k(p)=floor(sqrt(b(p)))`,
`Lambda(p)=2^k(p)`, `m(p)=ord_p(16)`. Define p_A as the largest prime <=4A with

```
p=1 mod8,       m(p)^2 > p * 4^k(p).                 (PR1)
```

This uses only integer predicates, no observed pi phases. It is defined for
every sufficiently large integer A. Let

`eta_F = 1-(1+log log 2)/log 2`, approximately0.0860713.

For every fixed `0<B<eta_F/2`, eventually

```
0 <= 4A-p_A <= 4A/(log(4A))^B.                       (PR2)
```

No effective threshold A0 or explicit implied constants are asserted.
This selector is an additional option, not a replacement for the earlier C2
selector, whose proved logarithmic epoch-gap exponent is better.

**Classical input.** Ford's shifted-prime divisor estimate, in the convenient
form of Agrawal–Pollack Proposition4.3: for sufficiently large x,y with
`y<=sqrt(x)` and `2y<=z<=y^2`, writing `z=y^(1+u)`, the number of primes p<=x
such that p-1 has a divisor in `(y,z]` is
`O(pi(x) u^eta_F [log(2/u)]^(-3/2))`.
We use only its upper bound, and the already declared quantitative fixed-
modulus PNT/AP for modulus8. Ford's Theorems1(v),6 establish this input.
This is unconditional; the theorem's use of geometry over finite fields later
is not an assumption of the classical Riemann hypothesis.

**Proof.** Put X=4A and restrict attention to p in `[X/2,X]`. Set
`Y=sqrt(X)/(log X)^2`. Those p with m(p)<=Y divide
`V=product_(1<=j<=floor(Y))(16^j-1)`. Distinct primes in this interval divide
V, and `log V < (log16)Y(Y+1)/2`. Since each such p has logp>=log(X/2), their
number is `O(X/(log X)^5)`.

Every other rejected p has a divisor m(p) of p-1 in `(y,z]`, where

```
y=Y,    z=sqrt(X)*exp((log2)*sqrt(log_2 X+1)).
```

The upper bound follows directly from PR1's rejection and b(p)<=log_2 X+1.
For sufficiently large X, all Ford hypotheses hold: y grows, y<=sqrt(X),
2y<=z, and z<=y^2. Moreover

```
u=log(z/y)/log y
 =[(log2)sqrt(log_2 X+1)+2log log X]
   /[(log X)/2-2log log X]
 =O((log X)^(-1/2)).
```

The Ford estimate and pi(X)=O(X/logX) bound these rejected primes by
`O(X/(log X)^(1+eta_F/2))`; dropping the extra negative loglog factor only
weakens the estimate. The small-order count is negligible beside this.

Take w=X/(logX)^B. Quantitative PNT/AP gives
`#{p=1mod8: X-w<=p<=X} ~ w/(4logX)`. If B<eta_F/2, this exceeds the total
rejected-prime bound in `[X/2,X]` for all sufficiently large X. Thus at least
one eligible p lies there, and the largest gives PR2. QED.

For `L=(p_A-1)/4`, `I={L+1,...,2L}`, and `J={A,...,2A-1}`, PE1–9 give
m|L and the exact clean clock

```
x_r = p[U_(L+1+r)]_p = xi *16^r modp,
xi=4*16^(L+1-(p+7)/8) modp,      0<=r<L.             (PR3)
```

The exact weight distance `eps_A=sum_n|1_J(n)/A-1_I(n)/L|` obeys
`eps_A<=4(A-L)/A`, hence is `O((log A)^(-B))`. The interval ends immediately
before the second p-pole; no periodic continuation of the full source is used.
Since `m>sqrt(p)Lambda(p)`, this selector eventually satisfies all older good-
order predicates. All uses of an actual finite prime still check PR1 directly.

## PR2. Quotient algebra identifies every polynomial phase resonance

Fix any split prime p and its clean clock. Let G=<16> in F_p^*, |G|=m, and
let xi!=0. Put `c=xi^m`. The coset xi G consists exactly of the roots of
`X^m-c`. These roots are distinct since p does not divide m.

For a polynomial P in F_p[X] and h in Z, compute the unique remainder

```
R(X) = hX+P(X) mod (X^m-c),      deg R<m.             (PR4)
```

The coherent mean on a complete local cycle is exactly

`S(P;h)=m^-1 sum_(x in xiG) e(R(x)/p)`.

It has modulus1 **if and only if R is constant**. In that case
`S(P;h)=e(R(0)/p)` exactly. Thus every polynomial phase that perfectly locks
to the local h-character lies in the precisely declared class

```
P(X) = -hX + c0 + (X^m-c) Q(X),                     (PR5)
```

with c0 in F_p and Q in F_p[X].

**Proof.** Evaluation on the coset annihilates X^m-c. The average of unit
complex numbers has modulus1 exactly when all terms coincide (equality in
triangle inequality). For residues in F_p, e(v/p) is injective, so this means
R is constant on all m points. Then R-c0 has m distinct roots and degree<m,
forcing the zero polynomial. Polynomial division proves PR5. QED.

The condition is about the actual observation support. Formal nonlinearity
alone is insufficient: P=-hX+c0+(X^m-c) already gives exact resonance. The
linear inverse P=-hX is the simplest member, not the whole syntactic class.

## PR3. All nonresonant algebraic phases have an explicit cancellation bound

If R in PR4 is nonconstant of degree D (so 1<=D<m), then

```
|S(P;h)| <= min(1, ((Dq-1)sqrt(p)+1)/(p-1))
         <= min(1, D sqrt(p)/m),     q=(p-1)/m.       (PR6)
```

**Imported finite-field input.** Weil's additive polynomial bound says
`|sum_(t in F_p)e(F(t)/p)| <= (deg F-1)sqrt(p)` when `1<=deg F<p`.
The reference is Kowalski's notes, Theorem3.2, printed page31; its assumptions
are checked explicitly here.

**Proof.** The map t->t^q from F_p^* onto G has q preimages at each point.
Consequently

```
q*m*S(P;h) = sum_(t in F_p)e(R(xi*t^q)/p)-e(R(0)/p).
```

The polynomial F(t)=R(xi*t^q) has degree Dq; its leading coefficient is
nonzero. Since D<m, `1<=Dq<p`. The imported bound applies, and removing t=0
costs exactly at most1, proving the first inequality. Since
`(Dq-1)sqrt(p)+1 <= Dq sqrt(p)`, the second follows. QED.

For PR1's selector, the last bound is strictly less than D/Lambda(p).
Thus for every degree budget D_A=o(Lambda(p_A)), uniformly over all
source-dependent P_A whose reduced polynomial hX+P_A is nonconstant of
degree at most D_A,

```
|mean_(n in I_A) e((h*x_n+P_A(x_n))/p_A)| ->0.         (PR7)
```

For sufficiently large A, p_A^2>16A, so every source denominator through
2A-1 has p_A-valuation at most1. Thus x_n=p_A[U_n]_pA is an integer even
on J_A outside I_A. The same observable there, built from the **actual**
principal parts, has bound eps_A+D_A/Lambda(p_A). Outside I_A no clean-clock
formula is asserted. At a finite epoch without p_A^2>16A, use only the
complete-interval statement or explicitly define a unit-modulus extension;
do not apply finite-field polynomials to nonintegral p_A[U_n]_pA. Each fixed degree is allowed, as are degrees up to any
`2^(theta*k(p_A))` with fixed0<theta<1. Coefficients are unrestricted residues
and may be chosen after reading authenticated history. Only the maximum
reduced degree and the exact resonance test enter the bound.

This is an unconditional original-local-source signed estimate for nonlinear
functions of the learned prime residue. Earlier CFS7 controlled polynomials
in **time**; PR7 controls finite-field polynomials in the **spatial local
residue**. These model classes and their costs are different. The new bound
does not say the authentic complementary phase belongs to either class.

## PR4. The surviving algebraic signal is an explicit resonant coefficient

On the complete interval I_A, fold the authentic complement over repeated
clock periods as in CFS4:

```
a_r=e(h*x_r/p),
B_r=mean_j e(h*(U_(L+1+r+jm)-[U_(L+1+r+jm)]_p)),
W_I=mean_r a_r B_r.
```

Suppose a proposed finite model is
`V_r=sum_l alpha_l e(P_l(x_r)/p)`. Define its actual empirical error
`rho=mean_r |B_r-V_r|`; no probabilistic training independence is assumed.
Reduce each hX+P_l as in PR4. For constant remainders c_l retain the **signed**
coherent coefficient

```
Rsig = sum_(l: remainder constant) alpha_l e(c_l/p).
```

For nonconstant remainders let D_l be their reduced degrees and define

`Ealg=sum_(l: nonconstant) |alpha_l| min(1,D_l sqrt(p)/m)`.

Then, for every finite original epoch and every such specified model,

```
|W_A(h;0)-Rsig| <= eps_A+rho+Ealg.                    (PR8)
```

**Proof.** Folding is exact since a is periodic. Replace B by V at costrho
using |a|=1, expand the finite model, retain the constant-remainder terms
exactly, and apply PR6 to each other term. Finally transfer W_I to W_J using
the exact weight distanceeps_A. QED.

In particular, if the original source admits such models for every large A
with rho_A->0, Rsig_A->0, and
`sum_nonconstant |alpha_l|D_l=o(Lambda(p_A))`, then every fixed-h Weyl mean
decays. The existing all-epoch Green-tail/Weyl implication gives pi normality
if this holds for every fixed h!=0. **These original-complement hypotheses
are OPEN.** They are sufficient model conditions, not a known weaker
criterion equivalent to normality.

The same inequality is an inverse diagnostic:
`|Rsig| >= |W_A|-eps_A-rho-Ealg`. A large full mean forces a large retained
resonance within any accurate model having a small certified nonresonant
budget. Learning is allowed to increase this resonance; discarding it would
throw away the actual signal. Signed cancellation between resonant atoms is
allowed and is not replaced by their sum of absolute coefficients.

## PR5. Hostile controls and logical contribution

- P=-hX gives a*e(P/p)=1 on every source clock, regardless of how small the
  local marginal is. PR8 keeps Rsig=1 and cannot falsely certify decay.
- Adding any multiple of X^m-xi^m changes syntax but no measured value;
  quotient reduction is mandatory. No nominal degree or nonlinear label can
  replace it.
- If h is divisible by p, a is trivial. PR2–6 still apply to hX+P after field
  reduction, but a separate local-marginal claim must exclude this case.
- A nonconstant reduced degree near m can have PR6>=1. This is an honest
  unresolved range, not an omitted error. Every function on the m-point
  coset has a polynomial interpolation of degree<m, so mere representability
  is vacuous; the weighted degree budget is load-bearing.
- Changing xi independently of the source, or using the periodic extension
  beyond the next p-pole, fails authentication. The oracle tests both.
- The coherent same-forcing wrong seed s*=-pi/16 has Weyl means tending1 and
  obeys the same Green-tail forcing law. Its irrational states do not have
  canonical rational principal parts: it is a real forcing control, not a
  claim of matching authenticated rational genealogy. No theorem here
  excludes it merely from that forcing or from gamma calibration. PR8's source-specific model
  premise must discriminate the original zero boundary.

PR1 pays a stronger local-order/coverage theorem. PR2–3 exclude a larger,
precisely delimited family of nonresonant local observation mechanisms. PR4
provides a checkable signed coefficient target. **No new bound on the actual
original complementary covariance is proved by this front.**

## Sources and dependency pins

- PE1–9: `research/2026-11-07/learning_yoneda/arithmetic/PRIME_EPOCH_THEOREM.md`;
  CFS4: `research/2026-11-08/covariance_forge/spectral/THEOREMS.md`; both at
  parent86327467191420d2157eeae5f4cfa1c2c62810da.
- [Ford, Theorems1(v),6](https://annals.math.princeton.edu/wp-content/uploads/annals-v168-n2-p01.pdf),
  Annals168(2008),367–433, and [Agrawal–Pollack, Proposition4.3, page7](https://www.pollack-math.net/nearprimitive.pdf).
  These are one imported theorem family, not two independent proofs.
- [Kowalski, Theorem3.2, printed page31](https://people.math.ethz.ch/~kowalski/exponential-sums-elementary.pdf),
  version14 September2021, states and later develops the classical Weil bound.
- Quantitative fixed-modulus PNT/AP is the same classical input already pinned
  in `signed_covariance_round2/EXPLICIT_CLOCKS.md`; its source contract is unchanged.

The failed original Murty URL now redirects to an author homepage; no claim
is based on its faulty search extraction. The direct Ford import supplies the
needed theorem and an explicit logarithmic coverage exponent. Full imported
proofs have not been Lean-formalized here; finite tests verify the new algebra,
selector and source transport, not those infinite classical inputs.
