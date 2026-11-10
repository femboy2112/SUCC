# Signed clock-orbit quotient: a better budget and its exact circular trap

[QCO1](THEOREMS.md) improves the finite PR8 arithmetic budget by grouping
polynomial phases under the actual prime-clock symmetry `Q(X)->Q(16X)`.
Within each orbit it charges the magnitude of the **signed coefficient sum**,
instead of summing magnitudes first. The discarded part is an explicit
source-frame twisted coboundary, so its contribution to the full clock
average is exactly zero.

This is a useful instrument improvement, with a sharp boundary. [QCO4](THEOREMS.md)
proves that a canonical zero-extension Fourier fit has every such orbit
coefficient proportional to the unknown Weyl average W. Its apparent
compression is a rank-one projection: it cannot prove cancellation that
was not already bounded. [QCO5](THEOREMS.md) proves the same obstruction for
**every complex-linear equivariant coefficient selector**, with a quantitative
commutator bound when equivariance fails. This includes a complete
mixed-quadratic linear analysis frame with correctly transported labels.
Nonlinear or source-anchored chronology selectors remain outside that theorem;
their coefficient estimates must still be obtained independently of the target W.

On reused authentic-source data, the finite improvement is substantial:

| A | h | Canonical atomwise nonresonant cost, lower bound | New canonical total quotient bound, upper bound |
|---:|---:|---:|---:|
|1103|1|1.774385|0.077915|
|1103|3|1.752073|0.139383|
|2203|1|1.786783|0.081023|
|2203|3|1.758276|0.054138|

The new total includes the retained resonant coefficient. These are
**particular canonical representations**, not optimized approximation costs.
They reuse prior development windows and are not fresh holdouts. The smaller
numbers supply no new asymptotic evidence because QCO4 identifies their
exact dependence on W. [Raw outward receipt](SOURCE_QUOTIENT.json) includes
input hashes and each orbit coefficient; [protocol](PROTOCOL.md) fixed the
four configurations before this front's replay.

The [proof dossier](THEOREMS.md) connects the result to archived CZR finite
cycle/cohomology work, categorical phase transport, the current arithmetic
budget, and classical Livsic/Gottschalk–Hedlund theory. It proves the sharp
finite inverse factor `1/(2 sin(pi/m))`, warning that exact solvability does
not supply a bounded primitive.

Independent checks use rational cyclotomic counts rather than the FFT:
153 orbit-mean identities,90 twisted coboundaries,720 rank-one identities,
50 rational cyclic primitives,30 coherent controls, and732 rejected
missing-twist/wrong-shift mutations. Another408 rational-matrix checks
verify QCO5, with11 chronology-asymmetric controls. Six unit tests pass. The FFT replay
evaluates26,324 coefficients and all32 nonzero slope-orbit sums; direct
interval predictions lie inside all corresponding certified FFT balls.

The separate [hostile review](ENERGY_REVIEW.md) accepts root RE1–4 within
their stated scope. A different Hierholzer implementation checks nine
finite de Bruijn constructions; the infinite normality conclusion rests
on the paper stage-count argument, not these finite cases.

No new Lean theorem or full-native-suite run is claimed by this front.
**Original-zero signed covariance decay: OPEN. Pi normality: OPEN. RH: OPEN.**
