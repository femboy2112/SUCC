# The authentic BBP source as a dyadic isometry

**Date:** 2026-10-24. **Status:** source-specific paper proofs and exact finite
instruments; the real-source collision bound and pi normality remain **OPEN**.

**Starting frontier:** draft [PR #268](https://github.com/femboy2112/SUCC/pull/268),
head `06f6b03eed2521c6bd5c02db618cb421ac6b5a51`, above coherent
`main@e648df3e4fca73ab6b942232b5ca4b310e9cac08`. Its
[inverse-branch discussion](https://github.com/femboy2112/SUCC/blob/06f6b03eed2521c6bd5c02db618cb421ac6b5a51/research/2026-10-24/PI_TWISTED_OBSERVER_AGREEMENT.md#111-an-exact-inverse-branch-step-toward-a-first-arithmetic-saving)
proves a local inclusion and a conditional refinement theorem. Neither its
one-half nor its one-sixteenth real-circle retention premise is established.

**Authority:** elementary algebra, convergent 2-adic analytic power series,
and exact rational controls. There is no new Lean authority, external referee
certificate, or claim of academic priority. The mathematical source is the
classical [Bailey--Borwein--Plouffe formula](https://www.davidhbailey.com/dhbpapers/digits.pdf).
This report derives the additional statements below from that specified source.

**Implementation:** [bbp_two_adic.py](../../observational_succ/bbp_two_adic.py).
**Independent rational controls:** [test_bbp_two_adic.py](../../tests/test_bbp_two_adic.py).

## 1. Result and exact boundary

The authentic **unwrapped** BBP source admits a bijective isometric
interpolation over the 2-adic integers. Its time-residue collision counts
are therefore explicit, and four successive binary refinements satisfy

$$
P_{k+4}(W)\le\frac1{16}P_k(W)+\frac{15}{16}|W|.
$$

This is an unconditional one-sixteenth theorem for a specified statistic of
the actual zero-initial-state source. It is not the real-circle count
required by PR #268. The source's real fractional states are obtained by
subtracting its actual integer carry history; that coupling remains essential.

The same construction gives coherent multiplication by every odd prime on
the dyadic source coordinates. An exact authentic-source counterexample
shows that this transport does not automatically transport real-circle states.
Consequently neither a coherent base-3 dyadic action nor the finite list of
primes below 16 supplies the missing real estimate by itself.

## 2. Definitions: source, lift, and carries

For integer n at least 1, write the classical forcing as

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}
      -\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}
{(2n-1)(4n-1)(8n-7)(8n-3)}.
$$

The authenticated unwrapped source and its real fractional state are

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad y_n=\{U_n\}.
$$

Thus the real source also obeys

$$
y_0=0,\qquad y_n=\{16y_{n-1}+r(n)\}.
$$

Keep both integer carry quantities:

$$
c_n=16y_{n-1}+r(n)-y_n,\qquad C_n=\lfloor U_n\rfloor.
$$

They satisfy

$$
C_0=0,\qquad C_n=16C_{n-1}+c_n,\qquad U_n=C_n+y_n.
$$

The literal local carry c_n must not be silently treated as a digit already
reduced modulo 16. A positive forcing can allow a local carry of 16 in this
recurrence class. The implementation retains integer carries exactly; its
synthetic `[16,1]` control tests this distinction without asserting that this
particular carry word occurs in the authentic source.

All U_n and y_n have odd reduced denominators. They can therefore be embedded
in the 2-adic integers as well as in the real numbers. Congruences below refer
to that 2-adic embedding; real fractional parts refer to the real embedding.

## 3. The rational forcing is an isometric permutation

Let

$$
N(t)=120t^2-89t+16,\qquad
D(t)=(2t-1)(4t-1)(8t-7)(8t-3).
$$

Every factor of D(t) is odd on the 2-adic integers. Hence the same rational
formula r(t)=N(t)/D(t) is defined on all of that space, including zero and
negative integer arguments. Its positive real integral interpretation is
only needed at the original positive source indices.

### Theorem DSI-1: forcing isometry

For all x,y in the 2-adic integers,

$$
v_2(r(x)-r(y))=v_2(x-y).
$$

At x=y both sides have the usual value infinity. In particular, r is a
bijective isometry and induces a permutation modulo every power of two.

**Proof.** For x distinct from y,

$$
\frac{N(x)-N(y)}{x-y}=120(x+y)-89
$$

is odd. Every nonconstant coefficient of D is even: each of its four factors
has even slope and odd constant coefficient. Therefore

$$
\frac{D(x)-D(y)}{x-y}\in2\mathbb Z_2.
$$

Now

$$
\frac{r(x)-r(y)}{x-y}
=\frac{[120(x+y)-89]D(y)
-N(y)[D(x)-D(y)]/(x-y)}{D(x)D(y)}
$$

is a 2-adic unit. This proves the valuation equality.

For surjectivity, the isometry gives well-defined injective maps on each
finite quotient modulo 2^k. Each is a permutation because domain and codomain
have the same finite size. Their inverses are compatible under reduction.
Passing to compatible residue sequences constructs an inverse on the entire
2-adic integer space. This explicitly supplies surjectivity; it is not
inferred from the word isometry alone. QED.

## 4. A canonical analytic particular solution

Define

$$
F(t)=\sum_{j=0}^{\infty}16^j r(t-j),\qquad t\in\mathbb Z_2.
$$

Each summand belongs to 2^(4j) times the 2-adic integers, uniformly in t.
The series therefore converges uniformly and obeys

$$
F(t)=16F(t-1)+r(t).
$$

### Theorem DSI-2: particular-solution isometry

The function F is a bijective isometry. For every k at least 1,

$$
F(t)\bmod2^k
=\sum_{0\le j<\lceil k/4\rceil}16^j r(t-j)\bmod2^k.
$$

**Proof.** Divide F(x)-F(y) by x-y. The j=0 term is a unit by DSI-1.
Every later term is divisible by 16, because each shifted forcing difference
has the same valuation as x-y. Their sum is therefore a unit. The finite
permutation and inverse-limit argument from DSI-1 again proves bijectivity.
Terms with 4j at least k vanish modulo 2^k, giving the exact evaluator. QED.

This evaluator is logarithmic in the requested modulus size at the level of
the number of forcing terms. It avoids forming the large rational numerator
and denominator of U_n. Bit lifting supplies its exact inverse modulo 2^k.

## 5. The authenticated zero: F(0)=0

### Theorem DSI-3: reversed-source zero identity

The following 2-adically convergent series is exactly zero:

$$
F(0)=\sum_{j=0}^{\infty}16^j r(-j)=0.
$$

This theorem is not an assertion that the real number pi equals zero in a
different field. The object is the displayed rational series, with a distinct
index direction and a declared convergence domain.

### Analytic convention and domain

In this proof an integral denotes evaluation of a **single convergent analytic
power-series antiderivative**, normalized to vanish at zero. It is not a Haar
integral, a Volkenborn integral, or an unspecified notion of integration over
a disconnected space.

All power series used below converge on a disc of radius strictly greater
than 1. Fix any real radius R with

$$
1<R<\sqrt2
$$

in the normalization |2|_2=1/2. Every composition and derivative identity
below holds as one analytic power series on that disc. In characteristic
zero, a single power series with derivative zero has all nonconstant
coefficients zero. We do not use the false general inference that every
locally constant p-adic function is globally constant.

### Proof, first step: generating integral

The original four-pole formula at negative indices is

$$
r(-j)=-\frac4{8j+7}+\frac2{8j+4}
       +\frac1{8j+3}+\frac1{8j+2}.
$$

Termwise analytic integration gives

$$
F(0)=\int_0^1
\frac{-4t^6+2t^3+t^2+t}{1-16t^8}\,dt
=\int_0^1
\frac{t(1-t)}{(1-2t^2)(1-2t+2t^2)}\,dt.
$$

The second equality is a rational polynomial identity. The geometric series
in the first integrand converges whenever |t|_2 is less than sqrt(2).
Dividing its coefficients by their positive integer indices leaves that
radius unchanged, so the antiderivative and its value at 1 converge.

### Proof, second step: a Mobius involution

Set

$$
q(t)=1-2t+2t^2,\qquad
I(t)=\int_0^t\frac{ds}{q(s)},\qquad
M(t)=\frac{1-t}{1-2t}.
$$

The series for 1/q and its antiderivative converge on the chosen disc.
For |t|_2 at most R, the denominator 1-2t is a unit and |M(t)|_2 is at most R.
Thus I(M(t)) is a valid single analytic composition there. Direct algebra gives

$$
M'(t)=\frac1{(1-2t)^2},\qquad
q(M(t))=\frac{q(t)}{(1-2t)^2}.
$$

Consequently the derivative of I(M(t))-I(t) is zero as an analytic power
series on this disc. It is constant. Evaluating at t=0 gives the constant
I(1), since M(0)=1. Evaluating at t=1 gives -I(1), since M(1)=0. Hence

$$
2I(1)=0,\qquad I(1)=0.
$$

The same interval argument would not be valid over the reals: M has a real
pole at 1/2. In the present metric |1/2|_2=2, so that pole lies outside the
disc on which the analytic argument was made.

### Proof, third step: evaluate the primitive

The rational decomposition

$$
\frac{t(1-t)}{(1-2t^2)q(t)}
=\frac{t}{2(1-2t^2)}+\frac{t}{2q(t)}
$$

has analytic primitive

$$
-\frac18\log(1-2t^2)+\frac18\log q(t)+\frac14 I(t).
$$

Both logarithm series converge on the chosen disc. At t=1, q(1)=1 and
I(1)=0. Also log(-1)=0 for this 2-adic logarithm: the convergent formal
identity log((1+z)^2)=2 log(1+z), evaluated at z=-2, gives
0=2 log(-1). Thus the primitive vanishes at both zero and one. QED.

The finite modular zero checks are corroborating controls. The analytic
argument above, not the number of tested bits, establishes the infinite identity.

## 6. Exact authentic interpolation and all-depth denominators

### Corollary DSI-4: zero-initial-state source interpolation

For every integer n at least zero,

$$
F(n)=U_n\quad\hbox{in }\mathbb Q_2.
$$

Therefore, for all distinct nonnegative integer indices s,t,

$$
v_2(U_s-U_t)=v_2(s-t),
$$

and in particular

$$
v_2(U_n)=v_2(n)\qquad(n\ge1).
$$

**Proof.** F and U have the same recurrence and, by DSI-3, the same initial
zero. Induction gives equality. Apply the isometry theorem. QED.

The recurrence may also be extended algebraically backward from U_0=0 to
every integer index. The same statement then holds for that rational backward
extension. It is not an assertion of additional authentic negative-time BBP
observations; the application here uses nonnegative indices.

### Corollary DSI-5: every truncation depth

Let

$$
P_N=\sum_{n=1}^{N}16^{1-n}r(n),\qquad N\ge1.
$$

Since U_N=16^(N-1) P_N,

$$
v_2(P_N)=v_2(N)-4(N-1).
$$

The exact power of two in the reduced denominator of P_N is therefore

$$
e_N=4(N-1)-v_2(N),
$$

including e_1=0. The exact preperiod of its real rational circle orbit under
multiplication by 16 is

$$
\left\lceil\frac{e_N}{4}\right\rceil
=N-1-\left\lfloor\frac{v_2(N)}4\right\rfloor.
$$

**Proof of the preperiod assertion.** A reduced rational denominator
2^e times an odd number loses precisely four factors of two per multiplication
by 16, until none remain. Before that time a periodic return would require
2^e to divide 16^j(16^l-1); the latter factor is odd, so 4j must be at least e.
After that time multiplication by 16 is invertible modulo the remaining odd
denominator and the orbit is periodic. QED.

This strengthens the inherited
[odd-depth preperiod theorem](PI_SOURCE_GENESIS_SIGNED.md#sg-s4-exact-dyadic-preperiod-of-odd-bbp-truncations)
to every N. At N=16,64,256 the preperiods are respectively 14,62,253.
It preserves the prior warning: a long eventual odd-conductor period does
not estimate the source's long initial transient.

## 7. Exact dyadic collision counts and four coherent halves

For a consecutive interval W of N nonnegative integer indices, define

$$
P_k(W)=\#\{(s,t)\in W^2:U_s\equiv U_t\pmod{2^k}\},\qquad k\ge0.
$$

Ordered pairs and the diagonal are included. Precision zero means one class.

### Theorem DSI-6: explicit pair counts

Write M=2^k and N=qM+r, with 0 at most r less than M. Then

$$
P_k(W)=r(q+1)^2+(M-r)q^2
=\frac{N^2}{M}+r\left(1-\frac rM\right).
$$

The answer does not depend on the interval's starting index.

**Proof.** The source isometry identifies the source congruence exactly with
s=t modulo M. A consecutive integer interval has q or q+1 members in each
residue class, with exactly r larger classes. Sum the squared class counts.
QED.

### Theorem DSI-7: arbitrary binary refinement

For every integer a at least 1,

$$
P_{k+a}(W)\le2^{-a}P_k(W)+(1-2^{-a})N.
$$

In particular,

$$
P_{k+1}(W)\le\frac12P_k(W)+\frac12N,
\qquad
P_{k+4}(W)\le\frac1{16}P_k(W)+\frac{15}{16}N.
$$

**Proof.** Each parent residue class is a consecutive arithmetic progression.
Its m members split into 2^a child classes as evenly as possible. Every child
has size at most ceil(m/2^a), so the sum of squared child sizes is at most

$$
m\left\lceil\frac m{2^a}\right\rceil
\le\frac{m^2}{2^a}+(1-2^{-a})m.
$$

Sum over the parents. QED.

The linear term is necessary, for example for a one-element window whose
diagonal collision persists at every precision. The bound concerns the
authentic source, without an ensemble average or an assumed independent-bit
model. The finite quotient isometry supplies the conditional refinements.

## 8. The real carry coupling and the exact novelty boundary

The proven dyadic count P_k is distinct from the inherited real-circle count

$$
Q_W(\tau)=\#\{(s,t)\in W^2:\|y_s-y_t\|_{\mathbb T}\le\tau\}.
$$

The exact relation between the two states is

$$
F(n)-y_n=C_n,
\qquad
C_n=\sum_{j=0}^{n-1}16^j c_{n-j}.
$$

At fixed dyadic precision only the last ceil(k/4) literal carries contribute
to C_n modulo 2^k. This is finite memory in the 2-adic coordinate; it is not
a proof that those carries are statistically independent of F(n) or of the
real state. The full integer C_n retains all preceding carries.

For the inherited prime windows, N is comparable to p and the prescribed
M=16^d is comparable to p^(2/5). DSI-6 gives

$$
P_{4d}(W)\asymp\frac{N^2}{M}.
$$

Consequently a proposed comparison

$$
Q_W(1/M)\le p^{o(1)}P_{4d}(W)
$$

is, up to fixed constants, exactly the existing sufficient target

$$
K_p(1)=\frac{M Q_W(1/M)}{N^2}=p^{o(1)}.
$$

**Novelty tax:** naming this comparison transport does not make it a weaker
independently established arithmetic estimate. The new proven inputs are the
source isometry, its authenticated analytic zero, the all-depth denominator
formula, the coherent residue actions, and the exact dyadic pair counts. A
successful use for pi normality still needs new control of the real carry
coupling or another genuine source-specific real estimate.

## 9. Coherent odd-prime actions, with a declared transport defect

### Theorem DSI-8: odd-unit source actions

For every odd integer q, define on the 2-adic integers

$$
\sigma_q=F^{-1}\circ(q\,\cdot)\circ F.
$$

Then sigma_q is a bijective isometry fixing zero, and

$$
F(\sigma_q(t))=qF(t),\qquad
\sigma_q\circ\sigma_r=\sigma_{qr}
$$

for odd q,r. Its finite quotient permutations are compatible under reduction.

**Proof.** Multiplication by an odd integer is a bijective isometry of the
2-adic integers. Conjugate it by F. The composition identity follows by
cancelling F and its inverse. QED.

This construction covers 3 and every other odd prime. It does not assert that
a 2-adic time is an ordinary nonnegative integer time, that finite residue
representatives remain in a chosen chronological window, or that a perfect
2-adic relation has small real-circle error.

For integer representatives n and s satisfying s=sigma_q(n) modulo 2^k, the
exact defect is

$$
E_{q,k}(n)=U_s-qU_n\in2^k\mathbb Z_2.
$$

Its real-circle class is y_s-qy_n modulo one. Real transport requires
information about that class, not merely the displayed 2-adic congruence.

### Small odd multipliers do not give ordinary source times

There is a stronger domain statement for the primes below 16. For every
positive integer n and every odd integer q with 1<q<16,

$$
\sigma_q(n)\notin\mathbb Z_{\ge0}.
$$

Indeed, r(n)>0 at every positive source index, U_1>0, and
U_(n+1)=16U_n+r(n+1)>16U_n. Thus the increasing real rational sequence has

$$
U_n<qU_n<U_{n+1}.
$$

No nonnegative integer index m can satisfy U_m=qU_n. If sigma_q(n) were
such an index, its defining 2-adic identity would assert equality of these
two rational numbers. The rational embedding into the 2-adics is injective,
so that would also be a real rational equality, a contradiction. This is a
domain obstruction for the exact sigma transport, not a no-go for other
approximate couplings of the real empirical laws.

### Authentic-source refutation of automatic real transport

The exact finite evaluator gives

$$
\sigma_3(10)=14\pmod{32}.
$$

Thus U_14-3U_10 is zero modulo 32. Nevertheless, exact rational arithmetic gives

$$
\|U_{14}-3U_{10}\|_{\mathbb T}
=\frac{768205462011658030046123174167}
{1551998839414697967442350160575}
>\frac{49}{100}.
$$

This witness uses the authentic initial zero and forcing. It refutes an
automatic real-circle interpretation of this dyadic tripling action. It does
not refute a later asymptotic estimate with additional hypotheses.

## 10. Finite-prime control and the ternary chart boundary

Let

$$
L_k=(2\cdot3\cdot5\cdot7\cdot11\cdot13)^k,
\qquad x_k=\frac{L_k}{2L_k+1}.
$$

For every prime p below 16, v_p(x_k)=k. The denominator is a unit at every
one of those primes. Thus x_k tends to zero simultaneously in all six local
metrics, while its real value tends to 1/2. This is an exact obstruction to
a generic finite-prime-to-real norm bound without further arithmetic input,
such as suitable height control.

This generic family is not claimed to be an authenticated BBP trajectory.
The preceding U_14-3U_10 witness supplies a separate actual-source finite
control. Neither is an asymptotic refutation of pi normality.

The forcing formula also cannot simply be copied as a global map from the
3-adic integers to themselves: r(1)=47/15 is not 3-integral. Odd-prime source
analysis needs the correct domains and pole stratification. Multiplication
by 16 contracts at the 2-adic place and is a unit action at every odd prime;
the size ordering 2<3<5 is not itself a contraction hierarchy.

### A finite prime list does not contain the full real phase

This is a separate question from observing the bounded centered carry.
For a reduced rational u=A/D, let its canonical p-primary component be
a_p/p^e when p^e is the exact p-power in D, where
a_p=A(D/p^e)^(-1) modulo p^e and 0<=a_p<p^e. Then

$$
u=\sum_{p\mid D}\frac{a_p}{p^{v_p(D)}}\pmod1.
$$

Indeed, subtracting these components leaves a rational integral at every
prime, hence an integer. This is the elementary primary-fraction form of
the additive adelic product formula, already underlying the inherited
prime-clock construction. It is not a new cross-place identification.

For authentic U_n the standard 2-adic component is zero, since its
denominator is odd. Nontrivial characters of U_n modulo 2^k instead apply
the standard character to U_n/2^k; that changes the conductor and does not
discard the complementary odd-prime factors.

An exact authentic example occurs already at n=3:

$$
U_3=\frac{615863723}{765765},\qquad
y_3=\frac{188663}{765765}.
$$

The sum of its primary components at ALL primes below 16, reduced modulo
one, is 499/45045. The omitted component is exactly

$$
y_3-\frac{499}{45045}=\frac4{17}.
$$

At this index 17 first enters the original denominator through 4/(8n-7).
The independent analytic oracle verifies the original-source value and the
primary decomposition. This is information lost by that particular finite
projection; the complete forcing and initial zero still determine U_3.
A carry readout such as kappa modulo 9 is a different observation, applying
a character to kappa/9 rather than a standard local character to the integer
kappa. Its exact branch-identification theorem is unaffected.

## 11. Verification, claim states, and next discriminator

The focused suite runs with

```sh
python -m unittest tests.test_bbp_two_adic -v
```

It contains 15 tests and passed when this dossier was prepared. The tests use
the independent original four-pole formula, exact rational unwrapped source,
finite quotient permutations, compatible inverse lifting, all-depth rational
denominators, literal carries, exact residue pair tables, and the countermodels
above. Source-sign, source-doubling, omitted-carry, and omitted-diagonal controls
reject specifically false versions. Modular zero checks extend through 256
bits; inverse checks include 129-bit precision. These are finite corroboration,
not the proof of the analytic identity.

The integration-wide validation record belongs to the enclosing research
round; this focused receipt does not claim that unrelated repository gates
or hosted workflows have passed.

| Statement | Earned state | Boundary |
|---|---|---|
| r and F are bijective 2-adic isometries | PROVED | Declared source and local field |
| F(0)=0 and F(n)=U_n | PROVED | Single analytic power-series proof; no Lean authority |
| All-depth dyadic denominator and preperiod | PROVED | Rational truncations, not real cancellation |
| Exact P_k and one-sixteenth refinement | PROVED | 2-adic source congruence counts |
| Coherent odd-prime sigma actions | PROVED | 2-adic time residues |
| Automatic real-circle transport | REFUTED | Exact authentic finite witness |
| Generic real bound from all primes below 16 | REFUTED | Rational family without height control |
| First real-source half-retention bound | OPEN | Inherited arithmetic premise remains unpaid |
| Real-source subpower collision bound | OPEN | Required for the existing sufficient route |
| Pi normality or base-3 real invariance | OPEN | Not a consequence of this dossier |

The next useful discriminator must retain the actual source and quantify
either its real carry coupling, the real defect of a specified source-derived
time transport, or a different real correlation estimate. A restatement of
K_p(1)=p^(o(1)) as transport is an equivalent target, not a completed proof step.
