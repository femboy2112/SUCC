# Chronology-sensitive carry prediction: preregistered round

Starting research head: `19d98078b60e47092c9b9d050a70b6b7eabb7cd2`.
Fetched main: `43a607818907120d4cdab73d240f5b4d7700b63f`.
Original proof baseline: `d32342d375f44ddf62221ad6aff2f534abdc0a03`.
New files stay in this directory; frozen sources and prior receipts are read-only.

## Candidate and honest loss

Can a predictor derived from chronological carries supply a useful original-zero
signed certificate, without fitting the target Weyl sum? This is a pathway/probe
gap, not a presumed near-complete proof. Earlier covariance_forge round three
already tested in-window carry partitions. This experiment adds frozen training,
a later source clock, and signed orbit accounting; it is not the first carry test.

Preserve exactly the four-pole forcing and literal U0=0. At time n define the
literal carry kappa_n=floor(U_n)-16 floor(U_(n-1)). No kappa_(n+1), current
fractional phase, local prime coordinate or holdout target may enter a prediction.
Those quantities may be evaluated later to score the frozen predictor. Source
replay can of course compute U_n exactly; that computational availability does
not turn a target-reading model into an independent arithmetic estimate.

For each h=1,3 train two fixed categorical tables predicting e(h U_n), using
features kappa_n and (kappa_(n-1),kappa_n). Training times are the UNION of old
clean intervals [1103,2204] and [2189,4376], each time used once: [1103,4376].
These windows overlap in 16 times. No other training targets or model selection.
Cell values are the empirical complex mean, frozen as Gaussian dyadics with
denominator 2^24, with a declared deterministic inward disk rounding rule.
Unseen cells predict zero. Preserve any carry outside 0..15 as its actual
integer category. Compare both tables with the zero predictor; do not choose
only the best after testing. Publish the exact table/code hashes before holdout.

Holdout selector A=55003 was fixed before source phases were evaluated. The
source-blind PR1 selector gives p=220009, m=27501, q=2, clean interval
[55003,110004]. Check these predicates in code and verify the interval begins
after the previous branch source endpoint44000. It is fresh relative to the
declared earlier branch experiments, not a random independent source sample.
No stopping or replacement based on phase results. If computation fails, retain
the failed attempt and fix the instrument, without changing the mathematical
menu. One core for heavy arithmetic, no compiler-heavy parallelism.

For frozen table g, use V_r=conj(a_r)*q^-1 sum_j g(feature_(n0+r+jm)).
Score rho=mean_r|B_r-V_r| and M=mean_r a_r V_r. The direct valid certificate is
|W|<=rho+|M|. M is a carry-occupancy statistic and its smallness still requires
an arithmetic theorem; it is not automatically a nonresonant phase bound.
Also report the canonical QCO1 resonance and signed orbit budget for V, either
through certified Gauss periods or a proved conservative Parseval upper bound.
This canonical expansion reads M, not W; its residual rho must remain charged.
No phase-blind energy or fitted small W can replace that residual.

Declare outcomes before measurement: a total certificate <=1/4 is a promising
finite saving; a certified lower bound above1/4 refutes that threshold for this
model; overlapping bounds are inconclusive. Compare to zero without relabeling
any finite success as asymptotic decay. Retain the raw signed residual as a
diagnostic only: evaluating its small mean is not proving its decay.

Controls: coherent inverse complement B=conj(a), homogeneous periodic completed
orbits (explicitly separate from literal-zero source), unseen carry words,
forbidden-next-carry leakage, independent gauge rotation without transport,
and direct versus grouped accounting. Do not use seed1/5 as a known nonnormal
counterexample. Record source signatures, carry/unwrapped hashes, original
principal parts and independent modular source checkpoints.

## Independent fronts and proof gates

Model front owns training and outward source/model receipts. Theory front
studies finite-state Poisson/innovation certificates and source carry transport.
Hostile front audits information leakage, seed cylinders and all-epoch quantifiers.
Root explores finite-alphabet folded-law obstructions, reconciles claims and
runs repository gates. Agents share model family/repository; distinct methods
and implementations do not constitute independent external refereeing.

Complete paper proofs, exact or interval tests, finite observations, Lean checks
and global claims remain separate. Any new explorations after this fixed test
will receive their own scope, not be called preregistered holdout predictions.
The all-epoch, every fixed h!=0 original-zero signed estimate remains unpaid.
Pi base-16 normality: OPEN. RH: OPEN.
