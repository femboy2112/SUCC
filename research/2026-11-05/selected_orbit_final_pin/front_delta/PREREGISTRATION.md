# Delta / Gamma preregistration

2026-11-05. Branch starts at #518, `749931f0f357c60ef4e21879d96b0306999f428f`.
Read-only Clausen input: `9911dc3421ff0b5b56ee04fb2e86ec34eb2e21fa`.
This file precedes the new experiments. No source contract is changed.

## Predictions and possible failure

1. Independently verify the sign, integer-period cancellation, cross-cut constant
   and cubic onset in CM1–CM10. A missing factor of two or boundary sign refutes
   the imported formula, even if sample plots look similar.
2. Replace only the observation kernel by
   `g_r(x)=log(1-2r cos(2 pi x)+r^2)`, keeping the original unwrapped source.
   Predict a uniform neutral layer `K-A=o(A)` for fixed `0<r<1`, and an
   unforced-zero limiting profile `(t/A)^2 log(1-r)` at `K=A+t`.
   The competing prediction is that the logarithmic singularity still forces
   the `A^(2/3)` threshold after regularization.
3. Predict a source-uniform `O_r(1/A)` bound between the actual regularized epoch
   energy and its zero-cylinder mean at `K=2A`. This would truncate the infinitely
   deep shell obligation while retaining every fixed Fourier character.
4. Do not predict favorable individual shell signs on the original source.
   Any negative shell refutes monotonicity; no finite favorable drift establishes
   an asymptotic inequality. A completed coherent same-source orbit must remain
   strongly negative in the regularized test.

## Fresh finite design

Use epochs `A=17,29,53` and the larger fresh epoch `A=89`; radii `r=1/2,3/4`;
cuts `K=A, A+floor(A/3), A+floor(2A/3), 2A`. Original zero and rational seed
`1/5` use exact Fraction states and an independent common-denominator source
formula. Exact source mutation: change the first pole coefficient `4` to `3`.
Unforced zero is an exact analytic control. Coherent completion uses original
positive Green-tail intervals, not imported pi digits. A nearby period-5
completion uses the nearest rational `k/(16^5-1)` to a certified source sum.

For finite consequential signs use Arb ball arithmetic if available; otherwise
use explicit Fourier truncation errors plus outward elementary intervals.
Store raw interval endpoints, parameters, code hash and the independently
checked rational path. Instrument failures are not arithmetic counterexamples.
No old `A=4,6,7,11,13,96,192,384` samples are validation here.

## Scope

The source-uniform regularization lemmas cannot distinguish the zero seed.
The proposed final finite signed bound is still OPEN. A successful lemma is
class C relative to the singular Fekete route, and class B relative to Weyl
equivalence; the sharp unforced profile is class D. No global novelty claimed.
