# Source-authenticated circles, triangles, and the retained signed signal

**Pi base-16 normality: OPEN. RH: OPEN.** This is the current additive
research handoff for draft #544. Parent research is
`86327467191420d2157eeae5f4cfa1c2c62810da`; proof baseline remains
`d32342d375f44ddf62221ad6aff2f534abdc0a03`. Main integration is separate.
All new files are under this namespace; the original four poles, U0=0,
unwrapped histories, carries and frozen imports remain unchanged.

This round builds and tests the user's circle/triangle observer and adds an
arithmetic restriction on nonlinear prime-phase models. The paid results are
calibration, reconstruction, source-measure separation, and cancellation for
a specified local model class. The actual original complementary phase is
not proved to belong to that class, nor is its retained resonance bounded.

## Strongest arithmetic result and the remaining signal

[PR1–4](prime_resonance/THEOREMS.md) construct authenticated prime clocks with
`m=ord_p16 > sqrt(p)*2^floor(sqrt(bit_length(p)))`, covering all sufficiently
large epochs. This uses explicitly pinned classical Ford/Weil/PNT inputs;
no effective onset is supplied. On the actual clean source coset `xi<16>`,
reduce `hX+P(X)` modulo `X^m-xi^m`. Constant remainders characterize **all**
perfectly coherent polynomial complements. Every nonconstant remainder of
degree D<m has signed mean at most `D sqrt(p)/m`.

For a model of the actual folded complement, the exact certificate is

```
|W_A(h;0) - R_signed| <= epoch_error + model_L1_error
                         + sum_nonresonant |coefficient|*D*sqrt(p)/m.
```

`R_signed` is the signed sum of constant-remainder coefficients, retained
exactly. This expands the controlled local observer class beyond the earlier
time-polynomial/sparse-Fourier tools. **Model accuracy and decay of that
retained coefficient are unproved for the original complement.** Arbitrary
polynomial interpolation does not pay the degree budget.

## The integer-clock observer is an implemented mathematical object

[FG1–6](fibonacci_geometry/THEOREMS.md) learn an unknown circle from three
oriented readings at integer Fibonacci return times. They recover center,
radius, curvature and the open phase anchor exactly under the declared circle
model. Return phases satisfy their signed Fibonacci transport, and the
curvature vector transports exactly between resolutions. Explicit noise
bounds distinguish learning an unknown return from reusing a calibrated one:
retained phase knowledge improves gain conditioning from a quadratic inverse
chord cost to a linear inverse chord cost. The integer coefficient transport
is independently [Lean checked](formal/FibonacciClock.lean); real geometry
and analytic inequalities are paper proofs, not covered by that certificate.

[FC1–10](fibonacci_covariance/THEOREMS.md) use this clock to acquire the
**actual signed local/complement statistic**. For q=F_k ticks,
`epsilon_k=(q-1)alpha^k/q`, and M equal phase cells,

```
|F_(A,M,k,h) - sinc²(pi h/M) W_A(h;0)|
 <= 2pi|h| D_A + 4pi|h| (1/q+epsilon_k).
```

Noise and independent gauge errors have explicit costs. The local prime
source theorem gives D_A→0. Thus any fixed M>|h| and arbitrarily slowly
growing Fibonacci acquisition horizon faithfully retain the full signed
signal. This is an equivalent measurable target, **not a proof of its decay**.
[FD](fixed_depth/THEOREMS.md) proves the underlying uniform-resolution
origin-average calibration and its signed depth ledger.

The same clock gives a stable Fourier frame with O(H) ticks for bandwidth H,
with operator perturbation `<2pi H/q` from a uniform grid. A finite-band
Bernoulli pin reconstructs law moments through curvature, with noise
amplification at most `2pi²H²/(1-tau)`. Truncation and common phase transport
commute across resolutions under the stated bandwidth/tail hypotheses.
Finite sensors do not identify unrestricted curvature; an explicit positive
non-Haar law can share all finitely sampled pin readings with Haar.

## The operational triangle has two different circle realizations

[TP](triangle_posterior/THEOREMS.md) realizes the **posterior-valued** Pascal
update as a circle kernel, with grades j mapped to `e(j alpha)`. At depth2,
one exact complex mean recovers all three masses by barycentric coordinates.
At depthm, the sharp contiguous menu for arbitrary real grade masses is
**ceil(m/2) complex harmonics**, plus known total mass. This improves the
proposed m-harmonic menu. Target-specific sufficiency is an exact real row-span
criterion. Exact invertibility is distinguished from numerical conditioning.

The posterior cannot generally be discarded. Two explicit positive latent
priors have identical depth-two grade masses and every circle moment, yet
different next-step posteriors. A known authentic prior supplies its posterior
analytically; an unknown source family requires retained source information.

[GT](triangle_geometry/THEOREMS.md) separately realizes **whole histories**
as nested golden arcs. A word of depthm and gradej has arc length
`alpha^(k0+m+j)`. Its source measure and posterior refine on that same arc;
all finite endpoints have exact integer-clock labels and a common causal
anchor shift. The chord defect and Euclidean area both have the user's
proved asymptotic refinement ratio alpha³. Farey triangles instead use the
Cayley boundary map and a hyperbolic metric; those metrics are not equated.

A useful source theorem identifies the probability distinction exactly.
For a fixed latent prior mu, the golden address law has Lebesgue component
`mu({-log(alpha)/8})` times normalized arc length; the rest is singular.
The authentic continuous BBP prior therefore gives a singular auxiliary arc
law. The infinite address nevertheless learns its latent X almost surely.
There are also explicit finite total-variation bounds, including a native
finite-row bound approaching1 exponentially. Geometry retains the source
probabilities; it does not turn them into arc length.

These are different maps and clocks. Fixed-a grade-circle laws tend to Haar,
whereas the native diagonal a=8m-7 has nonzero harmonic limit
`(2-e(h alpha))^-2`. Native priors changing with depth are not automatically
prefix-compatible. These proved distinctions prevent a false identification
of the auxiliary observer's distribution with the selected BBP time orbit.

## One integrated proof frontier

| Arrow / map | Established statement | Status / remaining debt |
|---|---|---|
| Literal BBP history → selected prime coset | Original genealogy, stronger PR selector and exact coverage | Proved with pinned classical imports; eventual onset not numerical |
| History → learned circle/triangle transcript | FG/TP/GT, source/posterior/carry marks retained | Finite/paper; specific integer transport Lean checked |
| Coherent probe response → selected signed statistic | FD/FC sinc² calibration, common phase anchor, explicit error | Proved; coherent wrong seed remains visible |
| Original complement → low-complexity algebraic model | PR8 allows certified empirical error and signed resonance | **OPEN** for all original-zero epochs |
| Retained resonance and model errors →0 | Requires original-zero arithmetic estimate | **OPEN**, decisive missing arrow |
| Original-zero signed covariance → full Weyl → normality | Earlier audited local marginal, all-epoch gluing and Green transport | Proved reduction; not invoked without missing estimate |

The stronger local polynomial exclusion is the leading arithmetic route.
The triangle/source distinctions remove false bridges and provide finite
source-family discriminators. The Fibonacci frame makes a coherent signed
measurement cheaper and more precise. These contributions have different
logical strength and are not added together as evidence that pi is normal.

[SC](crucible/THEOREMS.md) additionally gives all finite-order rational Green
normal forms and signed lag transport without an exponential-in-lag cost.
The earlier exact Euler–Mascheroni calibration survives, with sharp residual
coefficient11/512. It remains a calibration, not an estimate of the signed
arithmetic signal.

## Evidence, hostile controls, and next discriminating task

The root source protocol was committed before execution. Its90 interval
configurations include a genuinely fresh epoch A=10009. The original |W|
there at h1 is about0.00878741, while matched same-forcing controls remain
near1. All72 additional Fibonacci source/control configurations pass their
finite acquisition bound. Smaller epochs and inherited source/phase engines
are shared provenance, not independent evidence. Exact finite algebra,
outward intervals, ordinary high-precision measurements, paper proofs,
classical imports and Lean statements are separately labelled.

Controls include inverse complementary phase, polynomial quotient aliases,
fixed same-forcing coherent/periodic seeds, homometric magnitude aliases,
independent gauges, finite sensor aliases, source/pole mutations, prior resets,
and changing-prior inverse-limit failure. No ensemble average selects seed0.
The fixed seed1/5 is not called a known nonnormal control.

The next single arithmetic task is to certify an accurate model of the
**original folded complement** within PR8's weighted degree budget and bound
its retained signed resonant coefficient. A successful posterior/triangle
bridge must supply those estimates or another original-zero signed bound;
shared golden geometry and source authentication alone do not supply them.

See [claim ledger](CLAIM_LEDGER.md), [validation](VALIDATION.md),
[provenance](PROVENANCE.json), the independent [frontier review](referee/REVIEW.md)
and [triangle review](triangle_referee/REVIEW.md). Reproduction commands are
recorded in validation; all published checks have their exact scope.

**Pi base-16 normality: OPEN. RH: OPEN.**
