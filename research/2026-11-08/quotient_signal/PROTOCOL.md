# Quotient signal / Euler constant: fixed experiment protocol

Baseline: `a974db527c19708006b9f6d7f0ca01d08d1e0524` on the existing
draft #544 research branch. Main freshly observed at
`43a607818907120d4cdab73d240f5b4d7700b63f`; no rebase or source changes.

User hypothesis: learning the local phase removes nuisance information and
isolates the complementary signed signal; an Euler–Mascheroni correction
may characterize the small residual. These are distinct claims. The second
has no specified normalization yet, so no arbitrary fitted constant will be
called a test of the entire conjecture.

Original forcing, all unwrapped states and carries, and literal U0=0 remain
authenticated. At J=[A,2A), take the C=2 selected prime from the preceding
round, a=e(h[U]_p), b=e(h(U-[U]_p)), z=ab. P_d averages over the actual
local digit cells floor(16^d {x+theta}), x=[U]_p, including any later birth.
All finite results use these actual fibers, not a periodic replacement.

Before source execution, fix development A=137,271; holdouts A=547,1093,2203;
h=1,3; d=0,1,2,3,4; cell origins theta=0,1/32. Holdouts are new epochs but
overlap earlier time ranges: they are not independent source datasets.

Compare the literal original source with (i) the exact synthetic complement
b=conjugate(a), z=1, and (ii) the existing exact rational same-forcing shadow
with K=32, eta=2^-20 and matched primes {3,5,7,11,p}. Each shadow seed depends
on its horizon and is explicitly not zero. No seed-ensemble inference.

Retain signed W, mean(Pa Pb), the within-cell residual
E[(a-Pa)(b-Pb)], coarse and total bilinear covariance, V_a, V_b,
||aPb-Pz||², and ||z-aPb||². The predictions to check are the exact mean
split, Cauchy residual bound |R|²<=V_a V_b, demodulation gap<=V_a,
and decreasing V_b under refinement. No monotonic signed covariance claim.
At 16^d>=p the local phase is cell measurable: the residual is exactly zero
regardless of the complementary signal. This is an algebraic prediction,
not a floating-point equality assertion. Global coupled gauge transport
a->e(theta)a,b->e(-theta)b will be checked independently of cell shifts.

80-bit outward integer rectangles reuse the audited preceding engine.
Exact source modular-power checks use an independent formula. Fresh
high-precision evaluations may corroborate containment but are not proofs.
No exponent, gamma coefficient, or source cancellation is fitted here.

Separate analytic bearing: derive a gamma-containing finite part for the
actual Green tail if possible, check all constants independently, and state
the missing map to signed covariance. Continuum adversarial calibration
fixes b=e(t)conjugate(a), uniform x and equal cells: derive the residual
before comparing any coefficient with gamma.

Stop when the exact quotient theorem, a source-tail identity and controls
are audited, or a precise failed premise is exposed. Normality and RH stay
OPEN unless an all-epoch original-source signed estimate is actually proved.
