# Causal volume at negative analytic orders

Research continuation of draft #637, exact parent
`55bcde3d0c5ceb47d50cb499bd39f4a97c96bfc5`.

## Preregistered question

Starting with positive-time, Gamma-normalized causal volumes, construct a
lawful extension to negative analytic orders and determine exactly which
source information controls the resulting values at negative integers.
Test whether the original BBP Gamma endpoint implies the negative-even
zeros of the Riemann zeta function.

Initial status: **UNVERIFIED**. Candidate language: holomorphic families of
causal distributions, convolution, signed finite differences, normalized
Mellin transforms, endpoint Taylor jets, and reflection parity.

## Scope and quantifiers

- Distinguish causal time `t >= 0`, complex order `s`, arithmetic index `n`,
  and the original selected phase. A negative order is not negative time.
- Keep the original four BBP poles, radix 16, and zero seed unchanged.
- Positive-side data may be combined with signed algebraic coefficients.
  Any loss of positivity, topology change, or regularity assumption must
  be stated.
- A universal analytic continuation theorem requires a specified function
  or distribution class and its complete positive-side germ; finitely
  many observations do not silently become such a germ.
- Density or compactness alone is not a path-connectivity or analyticity
  hypothesis. The proposed geometric inference is tested separately.

## Weakest useful result and dependency cut

Prove a source-faithful rule that computes negative-order readouts from
positive-side boundary derivatives and says when they vanish. This closes
the positive volume -> analytic order -> endpoint-jet edge without
assuming BBP digit cancellation, the Riemann functional equation, or RH.

Novelty tax: the general distribution and Mellin machinery is classical.
The contribution sought is an explicit SUCC source map, exact reusable
implementation, calibrated obstruction, and precise interpretation of
the Gamma depth shifts. Academic priority is not asserted.

## Discriminating probes before implementation

1. Recover the Gamma convolution/Beta law and `Phi_0 = delta`.
2. At negative integers recover `Phi_-m = D^m delta`; a missing sign or
   missing boundary term must fail an exact polynomial test.
3. Build these derivatives from atoms supported only at nonnegative
   times, with a proved error bound on smooth test functions.
4. Recover zeta's negative-even zeros from the positive Bose kernel's
   endpoint reflection parity, and break them with a positive analytic
   perturbation that preserves the leading singular term.
5. Apply the same endpoint rule to the *original* BBP kernel and full
   radix-weighted source family. If any negative even value is nonzero,
   the proposed implication from Gamma shape alone is refuted.
6. Distinguish uniqueness from stability, and signed distributions from
   positive measures. Check finite-observation and compact-space controls.

Finite exact computation audits formulas and finds counterexamples; the
infinite continuation, support, and all-order claims require proofs.
Next lamp if the source-to-zeta link remains Dark: a declared,
source-preserving parity or reflection intertwiner with verified maps
and quantitative control on the actual chronological phase.
