# Original BBP comoving-gauge source mass: an improved uniform Weyl transport constant

**Date:** 2026-11-05. **Research-only, independent derivation.**
**Base:** additive child of draft #508, pinned parent
`61cdf240d0c2e75afe934dde6c98ce71a783a832`.
This supplement sharpens *only* the existing `O_h(1)` comparison
of authentic BBP `U_n` and the base-16 pi orbit. It does **not**
establish the missing `o_h(N)` cancellation, normality, or RH.
Historical original bounds and their sources must not be rewritten.

## Definitions and exact source

For `j>=1`,

```text
P(j)=120j^2-89j+16,
D(j)=(2j-1)(4j-1)(8j-7)(8j-3),
r(j)=P(j)/D(j)
    =4/(8j-7)-2/(8j-4)-1/(8j-3)-1/(8j-2).
U_0=0; U_(n+1)=16 U_n+r(n+1);
pi/16 = sum_(j>=1) r(j)/16^j  (classical BBP identity).
e(t)=exp(2*pi*i*t).
Z_n=sum_(k>=1) 16^(-k)r(n+k) (n>=0).
```

All finite values are exact rationals. Since `P(j)>0,D(j)>0`
for `j>=1`, `Z_n>0`. The BBP identity gives the **exact**
original-orbit representation

```text
U_n = 16^(n-1) pi - Z_n (n>=1).
```

This is precisely the residual in the limiting source-comoving frame
`theta_infinity=-pi/16`, whose finite rational connection is
`theta_n=-U_n/16^n`; see [PROOFS.md](PROOFS.md).

## TG-1. Exact mass conservation by chronological reindexing [PROVED PAPER]

Let `R=sum_(j>=1) r(j)`, which converges absolutely since
`r(j)=O(j^-2)`. By Tonelli (all terms positive),

```text
sum_(n=1)^infinity Z_n
 = sum_(j=2)^infinity r(j) sum_(k=1)^(j-1) 16^(-k)
 = (1/15) sum_(j=2)^infinity r(j)(1-16^(-(j-1)))
 = (1/15)(R-r(1)-(pi-r(1)))
 = (R-pi)/15.
```

There is **no new limit exchange assumption**: all interchanged summands
are nonnegative and the resulting sums are finite by `r(j)=O(j^-2)`.
Consequently, for every integer `h` and `N>=1`, the elementary
chord bound `|e(t)-1|<=2*pi*|t|` gives

```text
abs(sum_(n=1)^N e(h U_n)
    -sum_(n=1)^N e(h 16^(n-1) pi))
  <= 2*pi*abs(h)*sum_(n=1)^N Z_n
  <= (2*pi*abs(h)/15)(R-pi).
```

This includes all source-selected zero-seeded `U_n` and is uniform
in `N`. It is just a constant-level transport, not `o(N)`.

## TG-2. Certified sharper rational constant without special functions [PROVED PAPER]

For `j>=2`, put `t=j-2>=0`. Direct integer polynomial expansion yields

```text
13 D(j) - 25 j^2 P(j)
= 3656 t^4 + 18161 t^3 + 30078 t^2 + 16694 t + 141 > 0.
```

Thus `0<r(j)<13/(25j^2)` for `j>=2`. As `n+k>=2`
whenever `n,k>=1`,

```text
0<Z_n < (13/25) * (sum_(k>=1)16^-k)/(n+1)^2
      = 13/(375(n+1)^2)  for n>=1.
```

Monotonicity of `x^-2` gives
`sum_(n=1)^infinity 1/(n+1)^2
<=1/4+int_2^infinity x^-2 dx=3/4`.
Therefore, with the classical rational bound `pi<22/7`,

```text
abs(sum_(n=1)^N e(h U_n)-sum_(n=1)^N e(h 16^(n-1)pi))
 < (2*pi*abs(h))*(13/375)*(3/4)
 = (13*pi/250)*abs(h)
 < (143/875)*abs(h)
 < (119/648)*abs(h).
```

The final strict comparison is exact integer arithmetic:
`143*648=92664<104125=119*875`.
The previous inherited repository transport constant is
`119/648 ~= 0.1836419753`; the new **certified rational**
constant is `143/875 ~= 0.1634285714`. No numerical pi oracle
or paper-only special-function evaluation is required for this
strict improvement.

The inequality `r(j)<13/(25j^2)` is specific to the *authentic*
four signed BBP poles. A source mutant cannot reuse it by name.

## TG-3. Exact closed-form mass and a still sharper analytic constant [PROVED PAPER, classical special-function step]

The unweighted BBP forcing sum has the elementary integral representation

```text
R = integral_0^1 (4-2x^3-x^4-x^5)/(1-x^8) dx
  = integral_0^1 (x^2+2)(x^2+2x+2)/
                   [(x+1)(x^2+1)(x^4+1)] dx.
```

This follows by geometric series and Tonelli on the individual positive
`r(j)`, or by first summing the finite source expression and using its
absolutely summable `O(j^-2)` remainder. The cancelled rational
integrand is continuous at `x=1`.

An independently checkable digamma representation is

```text
R = -psi(1/8)/2 + psi(1/2)/4 + psi(5/8)/8 + psi(3/4)/8,
```

since the signed coefficients sum to zero. Standard digamma identities
(or the partial fractions of the rational integrand) give

```text
R = pi*(4+5*sqrt(2))/16
    + (5/8)*log(2)
    + (5*sqrt(2)/8)*log(1+sqrt(2)).
```

One exact partial-fraction verification, with `q=sqrt(2)`, is

```text
(4-2x^3-x^4-x^5)/(1-x^8)
 = 3/[4(x+1)] + (x+3)/[4(x^2+1)]
   + [(-4+5q)x-3q+10]/[8(x^2+qx+1)]
   - [(4+5q)x-10-3q]/[8(x^2-qx+1)].
```

Differentiate the elementary logarithmic/arctangent primitives and
evaluate at `x=0,1` to verify the stated closed form.
Numerical values below are *checks*, not the primary certificate:

```text
R ~= 3.3860476195971917219364188314384
R-pi ~= 0.2444549660073984834737754481589
2*pi*(R-pi)/15 ~= 0.1023970567123180940512445096220
```

Hence the exact special-function bound is about
`0.102397057*abs(h)`, a further constant improvement over both the
historical `0.183642*abs(h)` and the new elementary
`0.163429*abs(h)` certificates. No assertion of best possible
constant: the chord inequality may be strict.

**Independent numerical triangulation performed for this investigation:**
(i) a high-precision digamma evaluation, (ii) high-precision quadrature of
the rational source integrand, (iii) a 1000-term signed-pole partial
sum with explicit `O(1/1000)` decay, and (iv) the closed
`pi/log/sqrt(2)` formula agree at their applicable accuracies.
A computer algebra antiderivative shortcut was rejected after its
derivative failed to reproduce the integrand; no such antiderivative
is used as authority.

## TG-4. Source/failure controls and limits

1. Exact finite rearrangement of `Z_n` and its source-index sum must
   agree over every rectangular finite cutoff. The test suite checks it.
2. Check the polynomial identity for multiple integers `j>=2`;
   the displayed polynomial expansion is the mathematical certificate.
3. The `+1` forcing mutant has the same circle phase links while
   changing its unwrapped source; do not promote circle equality to
   source authenticity. The `+1/7` mutant changes the phase link.
4. The limiting coherent wrong seed `-pi/16` yields `-Z_n->0`,
   not a normal orbit: a bounded transport error from the **zero**
   seed does not turn an arbitrary seed into a normal source.
5. An `O_h(1)` improvement—even to an arbitrarily small constant—is
   still insufficient to prove `sum e(hU_n)=o_h(N)`. The needed
   source-selected signed cancellation is still **OPEN**.

**Claim labels:** TG-1 and TG-2: **PROVED PAPER** by explicit algebra,
Tonelli and inequalities; TG-3: **PROVED PAPER** conditional only on
classical BBP and standard digamma/rational integration formulas,
with numerical cross-checks; no new Lean declarations or external
refereeing. Finite tests: **OBSERVED** only. Pi normality: **OPEN**.
