# BBP reciprocal source circle and reflected two-path Haar seam

**Date:** 2026-11-20. **Research status:** draft paper proofs plus exact/synthetic checks. **Parent:** SUCC draft #677 (`b0ca06d6346863e03b00565067c6526ed4295225`). Additive research only; no authenticated source or seed changes, no merge/release.

## Central result

The ORIGINAL signed BBP Mellin mask

`Q(t)=4-2t^3-t^4-t^5=(1-t)H(t)` with `H(t)=4+4t+4t²+2t³+t⁴`

has a **source-specific, exact reciprocal root circle**:

`H(t)=(t²+2)(t²+2t+2)`, `t⁴ H(2/t)=4H(t)`, `H(t) | (t⁸−16)`.

Its roots lie on `|t|=sqrt(2)` with eighth-root phases `2,3,5,6 (mod 8)`. The character `t⁴/4` is exactly +1 on `t=±i sqrt(2)` and −1 on `t=−1±i`. In `A=Q[t]/(H)` this character squares to one and yields orthogonal idempotents `e±=(1±t⁴/4)/2`, exactly splitting the source algebra into two quadratic factors. The same split is available as a calibrated **two-path Haar sum/difference** on complementary left-semicircle arcs, with port probabilities `(1±cos 4θ)/2` and perfect factor discrimination at the four roots.

Two further source-specific exact deductions:

* The optional analytic **inverse-mask filter** `1/H(z)` has an eight-step self-similar signed impulse: `a_(n+8)=a_n/16`, with motif `(1/4,-1/4,0,1/8,-1/16,0,0,0)`. Its normalized carrier response `sqrt(2)^n a_n` is 8-periodic, whereas the raw impulse contracts. This is a declared auxiliary filter, **not** the BBP digit orbit.
* `Q(r z)` has analytic winding 0 for `r<1`, 1 for `1<r<sqrt(2)`, 5 for `r>sqrt(2)`, with boundary zeros at critical radii. Hence the associated Hardy Toeplitz Fredholm index moves `0→−1→−5`. The second jump of −4 is source-mask-specific and splits into two quadratic blocks. It is not an extra proved physical energy barrier.

The **existing** Fibonacci evaluation `M=[[0,1],[1,-1]]` adds a useful, explicitly auxiliary arithmetic fingerprint: `det(M²+2I)=11` and `det(M²+2M+2I)=5`. Thus the two Haar ports sort quadratic factors whose evaluated matrix determinants are the familiar 11- and 5-adic channels. The evaluator `M` is not an authenticated dynamical factor of the Archimedean π orbit.

## Start here

* [THEOREMS.md](THEOREMS.md) — exact derivations, quantifiers, reflection and topology contracts.
* [source_reflection_haar.py](source_reflection_haar.py) — exact `fractions.Fraction` auxiliary impulse and calibrated two-path synthetic code.
* [test_source_reflection_haar.py](test_source_reflection_haar.py) — focused regression/hostile cases.
* [independent_sympy_audit.py](independent_sympy_audit.py) — independently constructed symbolic and high-precision control.
* [CLAIM_LEDGER.md](CLAIM_LEDGER.md), [NEXT.md](NEXT.md), [VALIDATION.md](VALIDATION.md), [PROVENANCE.md](PROVENANCE.md).

### Source/physics firewall

These are **zeros of the Mellin numerator's complementary polynomial H**, NOT the original rational-function poles `8n−7`, etc., and NOT directly measured real hexadecimal digit states. A reciprocal root symmetry does **not** supply a dynamical attracting fixed point. A coherent two-path interferometer requires a defined emitter, reference, receiver and scattering boundary; complementary geodesic lengths are not automatically reflected optical path lengths. No equivalence between this root-filter Fourier spectrum and the real π Weyl sums has been proved.

In particular, original forcing with changed seed `s=−π/16` shares the entire source filter and perfectly passes these algebraic checks while its completed real phase locks at zero. Its seed fails the **original U0=0 source contract**; this defeats only source/seed-blind inferences. The matched-first-jet mutant destroys the precise circle reciprocity but retains the DC root and leading forcing jet. Neither R0, base-16 π normality, RH, nor a physical condensate/superfluid interpretation is claimed.
