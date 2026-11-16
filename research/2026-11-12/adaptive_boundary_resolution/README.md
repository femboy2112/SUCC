# Adaptive boundary resolution

**Research continuation, 2026-11-12.** This round makes the cost of
boundary reconstruction explicit: which information is supplied, how
many measurements a prescribed instrument needs, how accurately they
must be known, and which arithmetic statement remains after successful
reconstruction. It continues the
[holographic boundary-filter dossier](../holographic_boundary_filters/README.md)
on [draft PR #605](https://github.com/femboy2112/SUCC/pull/605).

The first round was published as commit
`f4151c4ae877ee43c4b7d130174b6bec1dbab9d6`. Its tree is identical to the
previously tested local commit `5d9917031855f806fd5c1f9d8b4543ad3ca24bbf`.
This continuation is additive. Goldbach, BBP R0, pi normality and RH
remain open.

## 1. What this round earns

| Result | What is established | What it does not supply |
|---|---|---|
| Integer information barrier | Nearly matching lower/upper channel costs for a fixed geometric observation ladder, over arbitrary finite integer grade supports. | A lower bound for arbitrary nodes, an arithmetic-source counterexample, or a fast decoder. |
| Movable damping | One appropriately chosen response, with an authentic uncertainty interval, can recover the integer zero count. | A response oracle, a free precision budget, or a pointwise arithmetic lower bound. |
| Fixed complex-bank obstruction | All fixed finite phase-twisted exponential minorants on the punctured closed unit disk eventually have negative cumulative Goldbach response. | An obstruction to growing banks, continuum profiles, source-informed support filters or other observables. |
| Adaptive arithmetic | A truly per-midpoint resolution schedule has the positive classical aggregate, and a verified classical quantitative theorem gives density-one positivity. | Control of every midpoint or an improved exceptional-set theorem. |
| Phase aperture | Exact continuum projection, finite alias accounting, and a clear distinction between angular completeness and finite sampling. | An all-scale theorem merely from successful finite reconstruction. |

The main change of perspective is practical. A filter can be a complete
decoder for a target while the task of acquiring or estimating its
authenticated response remains as hard as the original arithmetic
problem. The notes identify that boundary instead of assuming it away.

## 2. The common source and target

Start with a nonnegative grade histogram and its damped response,

\[
F(s)=\sum_{h\ge0}c_hs^h,\qquad M=\sum_hc_h.
\]

For the genuine arithmetic source at midpoint `n>=2`,

\[
h_n(a)=\Omega(n+a)+\Omega(n-a)-2,
\qquad 0\le a\le n-2,
\]

and `c_h` counts offsets at grade `h`. Both endpoints are at least two,
so grade zero means both endpoints are prime. Consequently `c_0=G(n)`,
the unordered prime-pair count of `2n`, including a prime diagonal, and
`M=n-1`. The joint midpoint coupling is part of the source. Separate
marginal information is not substituted for it.

Even complete recovery of this histogram recovers a graded occupancy
distribution, not every original offset or every possible internal
dynamical state. The prior ordered-realization theorem addresses a
different interface: joint ordered operator responses in the accessible
cyclic sector. The two results are complementary and have different
equivalence classes.

## 3. A nearly sharp cost for the fixed observation ladder

Fix an integer base `b>=2` and supply the exact packet

\[
M,F(b^{-1}),\ldots,F(b^{-d}).
\]

Let `M_min(b,d)` be the least mass for which two nonnegative integer
histograms have the same packet but different zero counts. Over **all
finite supports**, for `d>=1`,

\[
\boxed{
b^{d(d+1)/2}+1
\le M_{\min}(b,d)
\le\prod_{r=1}^d(b^r+1)
<\frac{153}{64}b^{d(d+1)/2}.
}
\]

The proof is an integer kernel calculation. A difference polynomial
with the same observations has roots `1,b^-1,...,b^-d`, so it is an
integer multiple of `(1-z) product(1-b^r z)`. The leading coefficient
must contain `b^[d(d+1)/2]`. The positive root and equal coefficient
masses force at least one additional unit. Splitting the annihilator
into its positive and negative coefficient parts supplies explicit
indistinguishable sources for the upper bound.

Thus the optimal required prefix length is

\[
N_b(M)=\sqrt{2\log_bM}+O_b(1).
\]

Explicit finite lower and upper channel bounds differ by at most one;
the prior stable even-degree rule is within two channels of optimum.
The upper construction is deliberately not claimed to be exact. At
`b=2,d=2`, multiplying its polynomial by `1+z` improves the twin mass
from 15 to 14. The exact minimum is not settled here.

See [INTEGER_INFORMATION.md](INTEGER_INFORMATION.md) and the
[separate audit](INTEGER_APERTURE_AUDIT.md). Exact product witnesses are
saved in [INTEGER_RESULTS.json](INTEGER_RESULTS.json).

## 4. Changing the instrument changes the channel count

If the damping node may depend on the known mass bound, then

\[
0\le F(s)-c_0\le Ms.
\]

One exact sample with `Ms<1` therefore gives `c_0=floor F(s)`. More
usefully, an authentic interval `[l,u]` gives

\[
\max(0,\lceil l-Ms\rceil)\le c_0\le\min(M,\lfloor u\rfloor).
\]

If `u-l+Ms<1`, this interval contains exactly one integer. Choosing
`s=1/(4M)` allows raw interval width up to `1/2`; normalized by the
known bound `M`, that is width `1/(2M)`.

This both supplies a simple constructive alternative and prevents an
overclaim about the fixed-ladder lower bound. The cost moved into the
range of permitted damping nodes, response acquisition, and normalized
precision. The integer noise twins independently show that a one-count
distinction has a precision cost of order `1/M`. Normalization cannot
erase the cost, and an unknown normalization mass cannot recover an
absolute count at all.

For Goldbach, the one-channel criterion reduces exactly to

\[
F_n\!\left(\frac1{4(n-1)}\right)>\frac14
\quad\Longleftrightarrow\quad G(n)>0.
\]

That equivalence is useful for locating the missing estimate. It is not
a proof of its left-hand side. [ADAPTIVE_APERTURE.md](ADAPTIVE_APERTURE.md)
states the exact access and uncertainty contracts.

## 5. What fixed twisting can and cannot accomplish

Take a finite, conjugation-paired bank

\[
q(h)=\sum_j b_jz_j^h,\qquad
0<|z_j|\le1,\qquad q(0)=1,\quad q(h)\le0\ (h\ge1).
\]

Keep the whole bank fixed while the arithmetic cutoff grows. If
`R=max |z_j|`, the all-grade sign condition forces the positive real
node `R` to be present with a negative coefficient. More sharply,

\[
b_R\le-\frac{\sum_{|z_j|=R}|b_j|^2}
{\sum_{|z_j|=R}|b_j|}<0.
\]

The argument uses finite-frequency averages and a square bound, so it
covers irrational phases and roots of unity without assuming a period.
The classical complex Selberg--Delange mean then gives sufficient
cancellation for every other node. The arithmetic conclusion is

\[
\sum_{n\le X}\sum_jb_jF_n(z_j)
\sim b_RK_RX^2(\log X)^{2R-2}<0,
\qquad K_R>0.
\]

Every sufficiently large fixed-ratio shell contains a negative
certificate response. This is stronger than a source-blind countermodel:
the proof uses the genuine Omega source. It still says nothing about
negativity at every individual midpoint.

Two different finite traps are preserved. A purported minorant can pass
an arbitrarily long grade prefix and fail later. A **genuine** minorant
can equal the actual count at every midpoint through any chosen finite
cutoff and still have an eventually negative aggregate if frozen there.
Thus neither kind of finite success can replace the all-grade and
all-scale proof obligations.

[COMPLEX_BANKS.md](COMPLEX_BANKS.md) gives the proof, endpoint treatment,
primary import audit, and exact controls. The separate
[complex/pointwise audit](COMPLEX_POINTWISE_AUDIT.md) checks the complex
mean, triangular endpoint, unconjugated diagonal and strict exponent gap.

## 6. A constructive angular route, with aliasing paid

A complete angular profile at radius `R` has an exact projection:

\[
c_0=\frac1{2\pi}\int_0^{2\pi}F(Re^{i\theta})\,d\theta.
\]

The corresponding finite `L`-phase average retains every grade divisible
by `L`. At `0<R<1`, its positive alias tail is bounded by
`R^L(M-c_0)`. Removing the declared worst tail produces a sound lower
certificate; leaving it unpaid can report a false zero count. A fixed
corrected finite bank remains subject to the negative-aggregate theorem.

This separates three access models: a complete continuum response,
finite phase sampling with a tail budget, and finite sampling with an
authenticated support ceiling. Increasing the phase order or changing
the support information can make reconstruction exact. No such change
establishes the sign of the authentic response at every arithmetic target.
See [PHASE_APERTURE.md](PHASE_APERTURE.md).

## 7. The remaining arithmetic quantifier

For the earlier even-degree filter, let
`epsilon_n=t^[d_n(d_n+1)/2]`. The exact uniform positivity and clamped
recovery threshold for the mass-only integer class is

\[
\epsilon_n(n-2)<1.
\]

Under it, `B_(d_n,t)(n)>0` is equivalent to Goldbach at that midpoint.
An equality-budget histogram makes the strict inequality necessary for
that entire class. Failure of the budget does not mean failure on a
particular authentic packet.

A weaker schedule, `epsilon_n=o(log^-2 n)`, already gives

\[
\sum_{n\le X}B_{d_n,t}(n)\sim X^2/\log^2X.
\]

This is a genuinely individual sequence of degrees; earlier targets
retain their degree when the cutoff changes. A verified classical
mean-square estimate for genuine prime-pair counts further transfers
to at most `O_A(X/log^A X)` nonpositive certificates for every fixed
`A>0`. A sufficient degree scale is `sqrt(log log n)`, compared with
`sqrt(log n)` for the worst-case complete integer count regime.

The density-one result imports quantitative count size from classical
additive prime theory. It is not a new exceptional-set estimate.
An infinite set as thin as the powers of two is compatible with every
displayed density bound. The note supplies a source-blind histogram
family with the correct leading aggregate, density-one positivity,
and infinitely many failed targets. [POINTWISE_GAP.md](POINTWISE_GAP.md)
states exactly where arithmetic remains open.

## 8. Frozen arithmetic integration and reproduction

Four midpoints were fixed before their new responses were inspected.
The entries below show rounded values only for readability; the saved
packets use exact fractions.

| Midpoint `n` | Direct unordered count `G(n)` | Degree 2 lower response | Degree 4 lower response | Degree 6 lower response | One moving-node interval |
|---:|---:|---:|---:|---:|---|
| 67 | 6 | 2.790405 | 5.978044 | 5.999998 | Exactly 6 |
| 263 | 15 | 1.920968 | 14.903231 | 14.999978 | Exactly 15 |
| 521 | 22 | -3.278224 | 21.808654 | 21.999950 | Exactly 22 |
| 1033 | 34 | -16.790155 | 33.613557 | 33.999886 | Exactly 34 |

Ten of the twelve damped packets are positive. Eight recover the exact
count from their particular observed intervals; seven satisfy the
stronger uniform mass-only completeness budget. All four one-channel
packets recover the count with their declared uncertainty intervals.
These observations test implementation and conventions, not asymptotics.
All four selected midpoints are prime, so their diagonal pairs already
guarantee a positive target. Their role is to check exact count recovery
and filter failures on a known-positive source, not to test difficult
existence cases. The shorter arithmetic controls in the unit suite also
include composite midpoints.

Reproduce the frozen exact reports and their code hashes:

```sh
python -W error research/2026-11-12/adaptive_boundary_resolution/run_checks.py
```

The dossier contributes 42 native unit tests. The separate deterministic
probe checks integer twins, rational phase-prefix impostors, 726
one-channel histogram/noise cases, and the arithmetic packets above.
The validation note records the complete required repository run and
the later phase addendum's separate controls without conflating them.

## Reading and next action

- [CLAIM_LEDGER.md](CLAIM_LEDGER.md): statuses, exact domains and falsifiers.
- [SOURCE_MAP.md](SOURCE_MAP.md): pinned repository and primary-source dependencies.
- [VALIDATION.md](VALIDATION.md): observed runs, receipts and the repaired normalization ambiguity.
- [NEXT.md](NEXT.md): the next discriminating research task and what would change the verdict.

The next productive step is a source-specific discriminator with a proved
arithmetic estimate that survives the exceptional targets. Another exact
representation of the count, an unqualified fixed phase bank, or a longer
successful finite prefix does not discharge that obligation.
