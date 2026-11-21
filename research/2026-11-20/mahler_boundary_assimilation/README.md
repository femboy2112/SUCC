# Operation BORG–MAHLER — auxiliary dynamics **until the boundary**

**2026-11-20 · additive, stacked research dossier · π normality OPEN.**

> User-directed thesis: assimilate Mahler's two-completion and Fibonacci results into SUCC, treating Mahler as *an observer-selected dynamic chart*, not automatically the intrinsic BBP dynamics. Preserve source and continuation when a chart reaches a boundary.

**Base:** SUCC draft [#681](https://github.com/femboy2112/SUCC/pull/681), itself stacked on [#680](https://github.com/femboy2112/SUCC/pull/680) and [#679](https://github.com/femboy2112/SUCC/pull/679), ultimately Main XXVI. This directory adds no edit to `main`, the authentic four BBP poles, `U_0=0`, frozen provenance, CI, formal, production, or earlier dossiers. No merges, tags, releases or hidden background runs.

## Four distinct meanings of Mahler — do not collapse the types

1. **Mahler's 1968 Z-number / 3/2 problem.** An actual rational-multiplier trajectory `xi*(3/2)^n` whose fractional parts are constrained to `J=[0,1/2)`. Its integer and remainder charts agree only on a guarded domain. The existence of any positive infinite such orbit remains open.
2. **Mahler expansion (p-adic Newton basis).** `f(x)=sum_j Delta^j f(0) binom(x,j)` for continuous functions on `Z_p`, previously brought into SUCC in [#17](https://github.com/femboy2112/SUCC/pull/17) and used in dyadic BBP/Pascal work [#272](https://github.com/femboy2112/SUCC/pull/272). This is a representation theorem, not the W trajectory or an automatic real-phase mixing estimate.
3. **Mahler measure.** Jensen's logarithmic root potential of the authentic BBP numerator/filter. Source polynomial `Q(t)=(1-t)(t^2+2)(t^2+2t+2)` gives a radial family with *exact* slope/analytic-index changes `0 -> 1 -> 5` at `rho=1,sqrt(2)`. This is an **auxiliary radial observer flow**, not the BBP time successor.
4. **Mahler functional equations.** `k`-Mahler generating functions satisfy finite-order relations among `F(z),F(z^k),...`. The native D-finite, nonrational BBP *source-time* series is NOT a standard `k`-Mahler function (Bézivin theorem); this is a negative result about the direct representation, not a ban on Mahler-type auxiliary observers.

## The new exact chart object

Let `xi=g+r`, `g` integer and `0<=r<1` (real completion). The intrinsic multiplier is

`T(g,r) = ( floor(3*(g+r)/2), {3*(g+r)/2} )`.

The *conditional Mahler observer* uses `b=g mod2` and

`M(g,r) = ((3*g+b)/2, (3*r-b)/2)`.

For input `r in J=[0,1/2)`, `M` agrees with `T` **and has output in J** exactly on

```
D = {g even, 0 <= r < 1/3} U {g odd, 1/3 <= r < 1/2}.
```

At an even `r=1/3`, the next real remainder is exactly `1/2`: window exit but integer formula still matches. At odd `r<1/3`, the Mahler integer branch is wrong, and its predicted remainder becomes negative; the full real multiplier still has a well-defined continuation. At `r=1/2`, `J` itself is exited. The first failed guard `tau` is an **observer-chart stopping time**, not the universe stopping.

`survivor_interval(g0,N)` is an exact rational half-open interval (or empty) of starting remainders that permit `N` guarded steps. The interval is computed by intersecting rational pullbacks of those guards; *finite survival does not certify infinite Z-admissibility.*

## Source-completion interface and the first π boundary

On every all-guarded path, let `b_n=g_n mod 2` and `S_N=sum_{j=0}^{N-1} b_j (2/3)^j`. Then

- Real: `3*r_0 = S_N+3*(2/3)^N*r_N`, with remainder in `[0,(3/2)*(2/3)^N)`.
- 2-adic: `S_N+3*g_0 = 3*(2/3)^N*g_N`, hence congruent to zero modulo `2^N`.
- For an **infinite** guarded orbit, the same rational series converges to `3*r_0` in `R` and `-3*g_0` in `Q_2`. This is Mahler's classical double completion, not an equality of these different limits.
- The no-`11` necessary rule follows since `11` forces `S_infty >= 1+2/3 > 3/2`; the number of length-`N` binary *necessary-condition* words is `F_(N+2)`. The full admissibility restriction is stronger.

The SUCC original-four-pole, zero-seeded BBP finite certificate (imported from #681) gives `pi/16 = 0.3243F6A8885A..._16`. Grouping each nibble low-bit-first, its parity journal starts `1100`. Therefore the *literal π-selected journal is not the parity journal of a Mahler Z-number*, already at the first nibble. It **is** a lawful `2`-adic parity address for both W and shortcut Collatz: the source selects symbolic coordinates, not a positive real Z orbit or a positive integer Collatz orbit.

For the first 48 bits, the two separately constructed addresses are:

```
W (Mahler 3/2 integer chart): 0x0E8F0415EFC3 mod 2^48
C (shortcut Collatz chart):   0x138D4B466283 mod 2^48  [#681 cross-check]
```

They have the same bits only after **different** conjugacies, not from the same raw integer dynamics. Neither residue is a canonical `2`-adic value of π. Any infinite continuation depends on further authenticated digits.

## Why the analytic boundary is equally interesting

For `rho>0`, use `Q_rho(z)=Q(rho*z)` on `|z|=1` and define the **log Mahler potential** `m(rho) = (1/2pi) int log|Q_rho(e^(i theta))| d theta`.

```
m(rho) = log 4                  if 0<rho<=1,
       = log 4 + log rho        if 1<=rho<=sqrt(2),
       = 5 log rho              if rho>=sqrt(2).
```

The radial slope `d m /d log rho` is `0,1,5` off the two root circles, agreeing with the authentic root-count winding and negative Hardy-Toeplitz Fredholm index from [#678](https://github.com/femboy2112/SUCC/pull/678). **At both root circles the winding/Fredholm index is undefined**; do not fill a value by continuity. The *potential* itself stays continuous. This is literal **Mahler measure as piecewise radial dynamics until boundary** in an auxiliary operator family; it provides no automatic real-phase orbit dynamics, physical energy flux, source-to-digit transfer, or signed Weyl bound.

## Test/review entry points

- [`THEOREMS.md`](THEOREMS.md): formal domains, derivations, exact boundaries, classical credit, hostile controls.
- [`mahler_boundary.py`](mahler_boundary.py): stdlib exact guard detector, full multiplier, survivor interval, two 2-adic parity inverse charts, finite source bits, radial spectral chart.
- [`test_mahler_boundary.py`](test_mahler_boundary.py): focused exact regression suite.
- [`independent_audit.py`](independent_audit.py): same-agent alternate implementation with brute checks and explicitly nonrigorous spectral quadrature.
- [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md): disclosed / imported / refuted / unverified distinctions.
- [`NEXT.md`](NEXT.md): source-to-Mahler transport and boundary-pressure probes, accept/reject criteria for R0.
- [`VALIDATION.md`](VALIDATION.md): executed receipt, assumptions, unrun root gates.
- [`HANDOFF_GOD_CLAUDE.md`](HANDOFF_GOD_CLAUDE.md): coordination prompts for existing local research agents, no main merge.

## Provenance and authoritative sources

- Kurt Mahler, *An Unsolved Problem on the Powers of 3/2*, J. Austral. Math. Soc. **8** (1968), 313–321. Original PDF: <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6416420BFE33A5DDC3DAB6EA358C2B0B/S1446788700005371a.pdf/an-unsolved-problem-on-the-powers-of-32.pdf> ; DOI <https://doi.org/10.1017/S1446788700005371>. Especially pp. 314–316.
- Daniel Bernstein and Jeffrey Lagarias, *The 3x+1 Conjugacy Map* (1996), DOI <https://doi.org/10.4153/CJM-1996-060-x>. Different, classical shortcut-Collatz parity chart.
- Keith Conrad, *Mahler Expansions*, <https://kconrad.math.uconn.edu/blurbs/gradnumthy/mahlerexpansions.pdf>, distinct p-adic interpolation theorem.
- Jason Bell, Michael Coons and Eric Rowland, *The Rational-Transcendental Dichotomy of Mahler Functions*, J. Integer Sequences **16** (2013), <https://arxiv.org/abs/1210.2070>, reproves Bézivin's D-finite/Mahler rationality theorem.
- SUCC historical [#17](https://github.com/femboy2112/SUCC/pull/17), [#272](https://github.com/femboy2112/SUCC/pull/272), [#599](https://github.com/femboy2112/SUCC/pull/599); current source [#678](https://github.com/femboy2112/SUCC/pull/678), digit observer [#679](https://github.com/femboy2112/SUCC/pull/679), dual completions [#680](https://github.com/femboy2112/SUCC/pull/680), parity dual categories [#681](https://github.com/femboy2112/SUCC/pull/681).

**Open theorem:** prove a *new source-derived signed, uniform all-late-shell bound* on the **actual** zero-seeded `pi/16` orbit. Mahler's finite boundaries, Fibonacci necessary language, radial measure, and universal 2-adic conjugacies are not that bound. `R0`, full π normality, positive-integer Collatz termination, existence of Z-numbers and RH remain OPEN.
