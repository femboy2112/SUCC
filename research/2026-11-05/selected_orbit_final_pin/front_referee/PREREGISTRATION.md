# Independent referee preregistration

Parent: PR #518, `749931f0f357c60ef4e21879d96b0306999f428f`.
Branch: `research/final-pin-referee-2026-11-05`.

This worker began without reading either arithmetic or Clausen worker's new
proofs. It read #518's proof dossier and repository AGENTS/METHOD. It then
proposed the entropy argument to the coordinator; the coordinator reported an
independent derivation of the same argument. These are two reasoning passes
with shared model and inherited source, not independent scholarly certification.

## Proposed claims, before new finite tests

1. For a radix-16 invariant circle probability measure, every non-Haar measure
has exponentially growing hexadecimal collision pressure. More precisely, with
`D_k = k log(16) - H_k`, expect
`log(P_m) >= floor(m/k) D_k`. Falsifier: an invariant non-Haar measure with
subexponential pressure or a failure of finite-block entropy subadditivity.
2. A fixed-depth empirical pressure envelope with zero lower exponential rate
should force Haar for the authenticated BBP orbit. Boundary atoms and the order
of the limits must be paid explicitly. This is a conditional reduction, not a
new BBP count estimate and not a logically weaker conclusion on invariant limits.
3. A positive absolutely continuous component, full support, atomlessness, or
an arbitrarily small fixed positive pressure exponent should NOT force Haar.
Controls: Haar/Dirac mixture and weakly biased full-support Bernoulli digits.
4. The literal rational seed `1/5` rotates every original character by exactly
`e(h/5)`; no character-magnitude test can distinguish it from seed zero.
5. #518's boundary-handled pressure-to-Haar argument should survive a direct
independent audit. Survival without a further independent certification does not
promote any unproved original-source inequality.

## Fresh finite calibration

All tests below are implementation/theorem calibration, not asymptotic evidence.
Use base 16 and rational Bernoulli bias `epsilon=1/128`, probabilities
`p_0=9/128`, `p_1=7/128`, and `p_j=1/16` for j=2,...,15. Check exact
`P_m=(513/512)^m` through m=47, plus direct product enumeration only at m<=3.
Use Haar/atom mixtures with weights 1/7 and 2/11 through depths 1,2,5,13,29.
Use original unwrapped Fraction recurrence through n=73 for the exact `1/5`
shift law and independent forcing identity; no finite π normality claim.
Use sparse exact-collision configurations formed from full grids, half-circle
grids, and the biased digit measure as mandatory countermodels.

No decimal numerical sign is promoted to a theorem. Proofs use exact algebra,
finite entropy inequalities, measure limits, and an elementary log inequality.

Before executing the tests, add a stationary Markov control with uniform digit
marginal and transition `P(i,j)=(2/3)/16+(1/3)1_{i=j}`. Prediction:
`P_m=(8/3)^(m-1)`. This falsifies one-digit uniformity as a selection mechanism.
Also prove (without numerical fit) that the Bernoulli measure obeys a Frostman
bound with exponent `s=log(128/9)/log(16)>2/3`; Borel-Cantelli should then supply
nearby same-forcing non-Haar completions of irrationality exponent below 3.
