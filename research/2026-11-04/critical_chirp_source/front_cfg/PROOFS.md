# Normal completions can fail the critical ratchet, even divergently

**Authority: paper proofs; same-model independent derivation, not Lean or an
external referee.** The original zero seed remains unresolved. These are precise
obstructions to a *seed-uniform* depth-selection or analytic-boundary promotion.

Write `e(x)=exp(2 pi i x)`, `alpha=pi/16`, and retain all four original poles.
The unchanged recurrence with a real seed s has

\[
 U_n(s)=16^n y-T_n,\qquad y=s+\alpha,\qquad
 0<\frac1{64n^2}-T_n<\frac1{64n^3}.
\]

The last bound is CC-01 of the pinned parent; it is the only nontrivial tail
input below. For each fixed nonzero integer h use exactly the mission's
`j_A(h), H_A(h), Lambda_A(h)`, hence
`log(A)/16 < Lambda_A(h) <= log(A)` eventually. All epochs below are dyadic.
The maximum in M includes every contiguous subinterval of `[A,2A)`.

## CFG-1. A normal same-forcing completion saturates every fixed-h ratchet

There is one fixed real seed s, with base-16 normal completion y, such that

\[
 \forall h\in\mathbb Z\setminus\{0\},\qquad
 \liminf_{A\to\infty,\ A\text{ dyadic}}
 \Lambda_A(h)M_A^{(s)}(H_A(h))\ \ge\ \frac{256}{\pi}.
\]

Nevertheless every fixed-character full-prefix Weyl mean for this same orbit
tends to zero. The quantifiers use one seed, all fixed h, and all sufficiently
late dyadic epochs for each h. They do not use epoch-dependent seeds.

**Construction and preservation of normality.** Start with any base-16 normal
number z, for example the base-16 Champernowne number. For every sufficiently
large dyadic A put

\[
 m_A=\lfloor A/\sqrt{\log A}\rfloor,\qquad
 p_A=\lceil 10\log_{16}A\rceil.
\]

Replace digits in positions `2A-m_A+1` through `2A+p_A` by zero, and set the
first hexadecimal digit to 1, leaving the other digits of z unchanged. Thus
`y<1/8<pi/16`, so the resulting seed is certainly nonzero. Positions are counted from 1 after the radix
point. These intervals are disjoint eventually. Their union has density zero:
for any epsilon>0, all sufficiently late lengths are at most epsilon A, and
the dyadic sum through a horizon N is at most a constant times epsilon N,
plus a fixed initial contribution. Letting epsilon decrease proves the claim.
For a fixed word of length k, at most k times the number of edited digits up
to N+k can change its count in the first N starting positions. Dividing by N
proves the edited number y is normal. This is a proof for all prefixes,
including prefixes lying inside an edited interval.

For `2A-m_A <= n < 2A`, its next at least p_A digits are zero; hence
`0 <= {16^n y} <= 16^(-p_A) <= A^(-10)`. Consequently

\[
 |e(H_AU_n(s))-e(-H_AT_n)|\le 2\pi H_A A^{-10}.
\]

**Independent local derivation of the constant.** Set Lambda=H/A^2 and
`K=floor(128 A/Lambda)`. For the mission schedule, K<m_A eventually. On the
terminal interval `n=2A-k`, `1<=k<=K`, put `t_k=Lambda k/A`. Uniformly for
`0<=t<=128` and Lambda sufficiently large,

\[
 H T_{2A-k}=\frac{\Lambda}{256}+\frac{t_k}{256}
              +O(\Lambda^{-1}+\Lambda/A).
\]

Indeed CC-01 costs at most Lambda/(64 A), and Taylor expansion of
`Lambda/[64(2-t/Lambda)^2]` gives the first two displayed terms with a uniform
`O(1/Lambda)` remainder on the fixed t interval. Multiplication by Lambda/A
turns the terminal sum into a Riemann sum with mesh Lambda/A. Therefore

\[
 e(\Lambda/256)\frac\Lambda A
       \sum_{k=1}^{K}e(-H T_{2A-k})
 \longrightarrow \int_0^{128}e(-t/256)\,dt
 =-\frac{256i}{\pi}.
\]

The digit error after the same normalization is
`O(H A^(-10))`, since `Lambda K/A <=128`, and vanishes. Taking moduli gives
CFG-1. This uses the half-turn's rescaled profile and a fixed-interval Riemann
sum; it does not assume CC-02's global maximality or its second integration by
parts. It only needs `Lambda -> infinity`, `Lambda/A -> 0` for the local tail
calculation, both true at the scheduled depth.

Finally normality of y gives every fixed-h completed Weyl mean zero. Since
`sum_n T_n < infinity`, the difference between original-forcing and completed
prefix sums is bounded by `2 pi |h| sum_n T_n`, so their normalized limits
agree. Negative characters are covered by conjugation.

## CFG-2. A normal same-forcing completion has a divergent critical ratchet

There is a second fixed real seed s with normal completion y such that

\[
 \boxed{\liminf_{A\to\infty,\ A\text{ dyadic}}
   \frac{R_A^{(s)}(1)}{\sqrt{\log A}}
   \ge\frac{\cos(\pi/15)}{16}>0.}
\]

In particular `R_A^(s)(1) -> infinity`, despite every fixed-character Weyl
mean and every fixed-character Abel mean tending to zero. The same divergence
holds for every fixed `h=+/-16^k`, k a nonnegative integer, because the selected
positive H and Lambda then equal those for h=1 at all sufficiently late A.

**Rational digit prescription.** Retain m_A above and now put
`p_A=ceil(3 log_16 A)`, `j=j_A(1)`, `H=16^j`, `Lambda=H/A^2`.
For integers `2A-m_A <= n <= 2A+p_A-1` define

\[
 q_n=\frac H{64n^2},\quad k_n=\lfloor15q_n+\tfrac12\rfloor,
 \quad d_n=k_n\pmod {15}\in\{0,\ldots,14\}.
\]

Set digit number `n+j+1` of y equal to d_n, outside these disjoint eventual
patches retaining the digits of a normal z except for setting its first digit
to 1. Again `y<1/8<pi/16` ensures a genuinely changed seed. The prescription uses rational
arithmetic and the schedule only; no pi digits are used. The patch length is
`m_A+p_A`, and the O(log A) shift j does not affect the preceding density-zero
argument. Thus this y is normal. It determines one fixed seed `s=y-alpha`.

Call an n in `I_A=[2A-m_A,2A)` good if
`d_n=d_(n+1)=...=d_(n+p_A-1)`. At a good n the first p_A digits of
`{16^(n+j)y}` all equal d_n, so comparison with the infinite constant digit
expansion gives

\[
 \left|\{16^{n+j}y\}-\frac{d_n}{15}\right|\le16^{-p_A}.
\]

This is an exact radix fact and pays for future-digit dependence. Rounding and
CC-01 then give, in circle distance,

\[
 \|\{16^{n+j}y\}-H T_n\|
 \le \eta_A:=\frac1{30}+16^{-p_A}+\frac\Lambda{64A}.
\]

Since `H=16^j`, this is precisely the phase of `e(HU_n(s))`. Its real part is
at least `cos(2 pi eta_A)`, tending to `cos(pi/15)`. There is no freely chosen
phase rotation in this comparison.

**All switches are paid.** The integers k_n decrease with n. The number of
changes of d_n across the extended patch is at most

\[
 V_A\le15(q_{2A-m_A}-q_{2A+p_A-1})+1
 \le\frac{15\Lambda(m_A+p_A)}{32A}+1,
\]

because `|d(H/(64x^2))/dx|=H/(32x^3) <= Lambda/(32A)` on the patch.
Each digit change spoils at most p_A starting positions, so the number B_A of
bad n in I_A obeys `B_A <= p_A V_A`. This is
`O((log A)^(3/2))=o(m_A)`. The added right padding prevents an uncounted final
boundary. Bad terms cost at most one each in the real part. Consequently

\[
 \Re\sum_{n\in I_A}e(HU_n(s))
 \ge(m_A-B_A)\cos(2\pi\eta_A)-B_A
 =(\cos(\pi/15)-o(1))\frac A{\sqrt{\log A}}.
\]

This is a single contiguous subinterval, so it lower-bounds A M_A. Multiply
by Lambda and use `Lambda > log(A)/16` to finish. Full-prefix fixed-h Weyl
decay follows from normality exactly as in CFG-1. Abel vanishing follows by
the elementary Abelian implication from Cesaro convergence; no Tauberian
converse is needed in this proof.

## Consequences for fronts C and F; exact first invalid inferences

The F1 Gram bound is valid for every real seed, hence for both constructed
normal completions. In CFG-2 a single selected squared maximal coefficient is
of order at least `1/log A`; this fits comfortably within F1's bounded total
budget. Thus adding full-prefix fixed-h Weyl decay to F1 still does not force
the requested moving-depth rate. The invalid step is uniformizing a
fixed-character limit over `h=H_A` while also multiplying by Lambda_A.

The exact same-forcing Ward equations, forcing Mellin/Gamma data, and
absolutely summable fixed-h Green-tail correction also hold. All fixed-h Abel
boundary limits are even zero for these controls, yet the critical ratchet
fails. Therefore an argument whose entire new input is fixed-h Abel boundary
vanishing, or its equivalent qualitative normality, cannot establish this
stronger moving estimate uniformly over real seeds. A source-selected
quantitative rate can still do so; no impossibility for seed zero is claimed.

The initial-zero term must be handled honestly: for a changed seed the Ward
series begins at `e(hs)`, not 1. After Abel normalization this contributes
`(1-rho)e(hs)` and tends to zero. The countermodels satisfy the correct
changed-seed equation; they do not satisfy the literal zero-seed contract.

The proposed original zero-seed saving remains **OPEN**, as do the mission's
original coarse energy gate and pi normality. These obstructions do not refute
Hypothesis A, whose zero boundary is an essential hypothesis.

## Source map and prior-art check

- Parent CC-01: `c9dfcdf057c4870f113e898464e4821c2ff5fedf`,
  `research/2026-11-04/critical_chirp/PROOFS.md`.
- Parent F1/F4 and existing density-zero counterexample to the *coarse energy*
  converse: `af5c7ba30ea57d725bd334310798357d50f12fce`,
  `research/2026-11-04/gamma_prybar/front4/FOURIER.md` and `PROOFS.md`.
  CFG-1/2 apply this classical edit method to the newly calibrated critical
  **signed maximal** ratchet; CFG-2 adds the rational digit tracking rule.
- Analytic Exile #496, pinned `a0a2619578a88182c73420901c99994699eb2024`,
  [AE-07 through AE-10](https://github.com/femboy2112/SUCC/blob/a0a2619578a88182c73420901c99994699eb2024/research/2026-11-04/analytic_exile/PROOFS.md),
  read through the connected GitHub source. No sibling source was imported.
- Bailey--Crandall, [On the Random Character of Fundamental Constant
  Expansions](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf), Hypothesis A
  and Theorem 1.1: their normality implication is conditional and starts at zero.
- Lagarias, [On the Normality of Arithmetical
  Constants](https://arxiv.org/pdf/math/0101055), Theorems 3.1, 3.3 and 4.1:
  orbit shadowing is general; the rational-function dichotomy is conditional.
  Our changed-seed examples do not challenge that dichotomy.
- Bailey--Crandall, [Random Generators and Normal
  Numbers](https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf), Theorems 4.6
  and 4.8: their cancellation uses modular orbit bounds with explicit length
  and growth conditions. F1 supplies different data; no transfer is automatic.

No priority claim is made for density-zero normality preservation, repeated
digit fixed points, Weyl/Abel implications, or classical normal numbers.

## Remaining source-specific lamp

Prove a bound excluding, for the **original** centered numerator/carry history,
the sustained alignment `||{16^(n+j_A)y}-H_A T_n|| <= 1/30+o(1)` on blocks
of length `A/sqrt(log A)`. CFG-2 makes this a concrete falsifying target for
candidate cofactor or carry inequalities. Excluding this one pattern alone is
not yet enough to prove the maximal ratchet; all signed patterns remain due.
