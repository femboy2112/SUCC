# What complete lag observations determine

Date: 2026-11-13. Parent: unmerged PR #608, commit
`7f11088bf5e3d216ca0f6ae57da1544e17c46d1c`.

Status: elementary paper proofs and classical normality consequences. No
worldwide novelty, new source-selected cancellation, R0 proof, or normality
proof is claimed. The new contribution to this dossier is a precise separation
of three statements that the phrase “nonresonant lag cancellation” can obscure.

## 1. Objects and inherited source transport

Let `T(u)=16u mod 1` on the circle, `e(t)=exp(2 pi i t)`, and let `lambda`
be normalized Haar probability. For a probability measure `mu`, use
`mu_hat(k)=integral e(ku) dmu(u)`. For an integer `q != 0`, `q_*mu` is its
pushforward under multiplication by q. Signs in this Fourier convention do
not affect any vanishing assertion.

For the authenticated BBP source, retain exactly `U_0=0` and

```
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
U_n=16 U_(n-1)+r(n),
Y_n=U_n+T_n=16^n x,  x=pi/16.
```

Here `T_n` is the positive decreasing BBP completion tail, not the circle map
T. Define the **full shell** lag record

```
L_B(ell,h) = (1/B) sum_(n=B)^(2B-1) e(h(Y_(n+ell)-Y_n)),
L_B^U(ell,h) = (1/B) sum_(n=B)^(2B-1) e(h(U_(n+ell)-U_n)).
```

The record includes states through `2B-1+ell`; it is not the zero-padded
truncated autocorrelation used in the main Fejer instrument. Exactly,

```
L_B(ell,h) = W_B(h(16^ell-1)).                                  (1)
```

The signed correction is

```
e(h(Y_(n+ell)-Y_n))
 = e(h(U_(n+ell)-U_n)) e(-h(T_n-T_(n+ell))).
```

The parent dossier proves `0<T_n<1/(64 n^2)` for every `n>=1`.
Thus, for every integer `B>=1`, `ell>=1`, and h,

```
|L_B(ell,h)-L_B^U(ell,h)| < pi |h|/(32 B^2),                    (2)
```

when h is nonzero; equality zero holds for h=0. This bound is uniform in
ell. Proof: the positive difference `T_n-T_(n+ell)` is at most `T_n`,
and the character is `2 pi |h|`-Lipschitz. This is the same lawful two-time
transport as SG-S2, with the parent's simpler shell tail bound. It does not
replace the correction by `(16^ell-1)T_n`, and it does not change the seed.

Provenance: `research/2026-10-24/PI_SOURCE_GENESIS_SIGNED.md`, SG-S2;
`research/2026-11-12/leah_gamma_twist/INVERSE_R0.md`, equation (2).

## 2. A finite covering does not hide a non-Haar invariant lift of Haar

**Theorem JTLC-01.** For every `T`-invariant Borel probability `mu` and every
nonzero integer q,

```
q_*mu = lambda  ==>  mu = lambda.                              (3)
```

This is a classical normality-factor phenomenon, not a new arithmetic theorem.
Two proofs expose different load-bearing facts.

### Proof A: domination and the Fourier tail

Put `d=|q|`. For a nonnegative continuous f, define

```
F(y)=sum_(qz=y) f(z).
```

This is continuous, `f(z)<=F(qz)`, and `integral F dlambda=d integral f dlambda`.
Consequently

```
integral f dmu <= integral F d(q_*mu)
               = d integral f dlambda.
```

Hence `mu<=d lambda`, so mu has an L1 density. The Fourier coefficients of
an L1 density tend to zero: approximate that density in L1 by a trigonometric
polynomial and bound the coefficient of the approximation error by its L1
norm. Invariance gives `mu_hat(k)=mu_hat(16^j k)` for all j. For k nonzero,
the right-hand frequencies tend to infinity, so `mu_hat(k)=0`. Uniqueness of
Fourier coefficients for finite measures gives `mu=lambda`. QED.

### Proof B: an explicit sparse-clock orthogonality argument

Write `d=2^a d_odd`, with d_odd odd. Choose an integer c with `4c>=a`.
Choose r>=1 such that `16^r=1 mod d_odd` (take r=1 if d_odd=1). For any
fixed nonzero integer h and K>=1, set

```
f_j(u)=e(h 16^(c+rj) u),  0<=j<K.
```

Every f_j has mu-mean `mu_hat(h)` by T-invariance. When i!=j, the nonzero
difference of their frequencies is divisible by q. Its mu-Fourier coefficient
is therefore zero because `q_*mu=lambda`. Thus

```
|mu_hat(h)|^2
 <= integral |(1/K) sum_(j<K) f_j|^2 dmu
 = 1/K.
```

Let K tend to infinity. Every nonzero coefficient vanishes, and mu is Haar.
This proof does not import a quantitative rate for the actual orbit. QED.

The T-invariance hypothesis cannot be omitted. For example, the measure with
density `q 1_[0,1/q)` for q>=2 pushes to Haar under multiplication by q, but
is not Haar itself.

## 3. All Fourier modes of one fixed lag already detect normality

**Theorem JTLC-02.** Fix any real alpha and any integer ell>=1. The following
are equivalent:

1. alpha is normal in base 16.
2. For every nonzero integer h,
   `lim_(N->infinity) (1/N) sum_(n=0)^(N-1)
    e(h(16^(n+ell)-16^n)alpha)=0`.
3. The analogous full-shell averages over `[B,2B)` tend to zero for every
   fixed nonzero h as integer B tends to infinity.

**Proof.** Put q=`16^ell-1`. The lag averages are exactly the Fourier averages
of the orbit of q alpha. For completeness, let

```
nu_N=(1/N) sum_(n=0)^(N-1) delta_(T^n alpha).
```

Every weak subsequential limit mu of nu_N is T-invariant, since

```
|integral f d(T_*nu_N-nu_N)| <= 2 ||f||_infinity/N.
```

If the lag means vanish at every nonzero h, Fourier approximation implies
`q_*nu_N -> lambda`. Each subsequential limit therefore satisfies (3), and
is Haar. Compactness of circle probabilities now gives `nu_N -> lambda`.
The converse follows because multiplication by q preserves Haar. This is the
usual equivalence between normality of alpha and of its nonzero integer
multiple, proved here directly for the required factor.

The identical endpoint argument applies to full-shell empirical measures.
If all shell limits are Haar, prefix averages are Haar by dyadic decomposition;
conversely prefix convergence gives shell convergence by subtracting the two
prefixes ending at B and 2B. QED.

For the actual BBP source, (2) transfers this exact equivalence to the rational
two-time records `L_B^U(ell,h)` for any fixed ell. This is an equivalence, not
a source-specific estimate. No non-Haar invariant “15-root remainder” survives
if **all h** at lag 1 actually vanish.

### What all lags retain, and what they cannot authenticate

For a finite nonempty lag set L, the pointwise joint map

```
u |-> (e((16^ell-1)u))_(ell in L)
```

has kernel `{j/d mod 1:0<=j<d}`, where

```
d=gcd_(ell in L)(16^ell-1)=16^(gcd L)-1.                       (4)
```

The gcd identity follows from the Euclidean algorithm on the exponents;
Bezout's identity then identifies the joint character kernel. In particular,
all positive lags together retain exactly `15u mod 1`. Their pointwise
ambiguity is the 15 shifts j/15. Each higher-lag character is already a power
of the lag-1 character because `(16^ell-1)/15` is an integer.

This recovers the archived PSG-11 seed-authentication counterexample. It does
not obstruct Theorem JTLC-02: translation by j/15 preserves any Haar limit.
It **does** obstruct determination of R0 from lag records alone. The completed
fixed points 0 and 1/15 have identical lag records, while their shell
anti-locking values are respectively 0 and `1-cos(2 pi/15)>0`. These are
changed-source-pointing controls; neither is claimed to be the authentic pi
orbit. An initial anchor remains necessary for an R0 detector.

If instead “nonresonant modes” means all k **outside** 15Z, their vanishing
does not imply Haar. The uniform measure on the fifteen fixed points j/15
has precisely that Fourier vanishing and is not Haar. More generally such
vanishing means invariance under translation by 1/15; it leaves an entire
quotient law unresolved, not merely a choice of one fixed point. This is a
different assertion from vanishing on all nonzero frequencies **inside**
15Z, which by Theorem JTLC-01 does force Haar for a T-invariant measure.

## 4. A first-mode lag oracle can look perfect on a singular nonnormal law

**Theorem JTLC-03 (explicit hostile law).** There exists a singular
T-invariant probability mu such that

```
integral e(16^ell u-u) dmu(u)=0   for every ell>=1,
mu_hat(1)=0,
Re mu_hat(2)>9/10.                                             (5)
```

In fact every lag correlation at every odd h vanishes.

**Construction and proof.** Take independent fair bits xi_j and let

```
X=sum_(j>=1) 8 xi_j /16^j;  mu=law(X).
```

The radix digits are restricted to {0,8}; the support is covered, at depth m,
by 2^m intervals of length at most `16^-m`. Their total length tends to zero,
so mu is singular. Multiplication by 16 deletes the first digit, hence mu is
T-invariant. Let X' be the copy made from the remaining bits, independent
of xi_1. Then

```
X=xi_1/2 + X'/16,   0<=X'<=8/15.
```

For any odd integer k, averaging the first fair bit gives `mu_hat(k)=0`.
Every `h(16^ell-1)` is odd when h is odd, proving the lag assertion.

At frequency 2, the first digit contributes an integer and

```
mu_hat(2)=E e(X'/8).
```

All its phases lie in `[0,2 pi/15]`, so

```
Re mu_hat(2) >= cos(2 pi/15)
             >= 1-(2 pi/15)^2/2
             > 10057/11025 > 9/10,
```

using pi<22/7. Thus the first-mode time-lag field has exact vanishing at every
positive lag, but a second mode remains strongly coherent. QED.

The corresponding deterministic orbit control may be obtained by choosing a
sequence of digits generic for the fair Bernoulli law on {0,8}. This is an
auxiliary nonnormal carrier, not a claim about the original zero-seeded BBP
orbit or an authentication of a changed seed in its rational-state contract.

This example is stronger than merely observing that one Weyl mode is
insufficient: it gives **every fixed lag correlation** at that mode, and at
every odd mode, while retaining a strongly nonzero even mode. It is fully
consistent with van der Corput, whose conclusion here is cancellation of the
first mode, not normality.

## 5. Consequence for the joint-field offensive

The complete single-lag Fourier law can be a sufficient observation family
for the normality target even though it does not authenticate the point.
The actual arithmetic estimate for that law is still missing. Adding more
lags does not supply independent degrees of freedom: (4) makes their algebraic
dependence explicit. Integer linear combinations of the multipliers only
produce new **joint products of characters**; separate marginal cancellation
does not license multiplying expectations.

For finite estimates, reuse the dossier's sharp zero-padded Fejer identity
and its explicit source correction. No weaker full-window endpoint bound is
introduced here. Existing `mixed_lag_coercivity.py` already tracks products
of multipliers and obtains logarithmic absolute losses, with no positive
normalized source saving. Existing IAD-02 already proves schedule-freeness
for the signed Fejer response. The distinction settled by this note is
which lag data determine the target and which exact hostile law survives
an incomplete mode family.

Next falsifying probes: verify all normalization and Fourier-support claims
against finite {0,8} prefix laws; reject a proposed all-mode conclusion that
accepts the law in (5); reject any claim that the fifteenfold point ambiguity
produces a non-Haar invariant lift of Haar. All finite probes remain checks
of the displayed proofs, not replacements for their infinite quantifiers.
