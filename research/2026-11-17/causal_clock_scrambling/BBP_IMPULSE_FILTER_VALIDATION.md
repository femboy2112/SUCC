# BBP Signed-Impulse/Mellin Completion — exact validation receipt

**Date:** 2026-11-17. Companion to [the impulse-filter manuscript](BBP_IMPULSE_MELLIN_FILTER.md). The project uses the **literal original signed four poles and zero initial seed**. No claim of π normality, an all-shell R0 energy bound, original academic priority or a physical information scrambler.

## Exact local standard-library tests and byte equality

The assistant executed the following local source in Python:

~~~sh
python -m unittest -v /mnt/data/test_bbp_impulse_filter.py
~~~

**Result: 9 tests PASSED, 0 errors, 0 failures.** The exact executed file was aligned to the published branch file and reexecuted. Its local Git blob SHA-1 equals the GitHub branch blob SHA:

~~~text
a901d64dac16d5aa297d1c9234439763e4699287
~~~

It is published at [tests/test_bbp_impulse_filter.py](../../../tests/test_bbp_impulse_filter.py). Tests check the full 6-tap impulse convolution (4,0,0,-2,-1,-1), zero zeroth moment and first moment -15, three positive rational lag-differences for 100 original source clocks, five positive Beta channels, two positive quadratic memory factors, exact cancellation of four of eight completion poles, a rational derivative identity for the elementary BBP primitive, exact spectral lower/upper factor inequalities on rational cosines, and the constant-mode null of cyclic signal observers.

## Independent symbolic source derivation

A separate SymPy script—not importing the repository test module—verified that ALL expressions below simplify to **zero as rational or Laurent-polynomial identities**:

- \(Q(t)-(1-t)H(t)\)
- \(16-t^8-H(t)(2-t^2)(t^2-2t+2)\)
- \(r(n)-[6/(a(a+3))+4/(a(a+4))+5/(a(a+5))]\), \(a=8n-7\)
- \(r(n)-\sum_{j=0}^4h_j/[(a+j)(a+j+1)]\)
- \(Q(t)/(16-t^8)-(1-t)/[(2-t^2)(t^2-2t+2)]\)
- \(|H(z)|^2-(1+8c^2)[8(c+3/4)^2+1/2]\) algebraically on \(|z|=1\), with \(c=(z+z^{-1})/2\)
- The derivative of the proposed logarithm/arctangent primitive minus the reduced rational integrand.

The primitive's endpoint values were **exactly** \(-\pi/16\) and 0; SymPy integrated the reduced source kernel on [0,1] to \(\pi/16\). The source coefficient identities, denominator factorization and reduction are proved independently of these finite symbolic outputs by straightforward polynomial multiplication and integration.

## Numerical integral cross-check

A separate 50-decimal-digit mpmath quadrature directly evaluated
\[
\int_0^1\frac{1-t}{(2-t^2)(t^2-2t+2)}\,dt,
\]
and obtained the same 50-digit value as \(\pi/16\), with printed difference 0 at working precision. This is an ordinary numerical diagnostic, **not** an interval-certified proof. The exact antiderivative and convergent series/integral interchange are the paper proof.

## Spectral boundary and resolution limit

All four nontrivial zeros of the positive polynomial \(H\) lie on \(|z|=\sqrt2\); the only unit-circle zero of \(Q=(1-z)H\) is at \(z=1\). For a separately declared length-N cyclic probe the nonconstant-mode least gain obeys
\[
\sqrt2\sin(\pi/N)\le\sigma_N\le30\sin(\pi/N),
\]
and is \(\Theta(N^{-1})\). The full spectral theorem is proved by diagonalizing the cyclic shift; finite evaluations at N=8,16,32,64,128,256 were consistent with these bounds. This **does not** transport the auxiliary Mellin lag shift into the actual BBP chronological radix orbit.

## Source passport and hostile boundary

The user's observation about the Kempner source is correct: its *numerical seed* can be zero, but its **forcing law encodes the sparse powers-of-two pattern**, so it is not the original four-pole source. Conversely, exact source nullity and source-mask DC cancellation can coexist with non-normal completed endpoints for different forcing laws. The previously committed [matched non-telescoping locked source](BBP_TWO_FORMULA_LOCKED_COUNTERMODEL.md) defeats any attempt to infer R0 from positivity, first moment, and similar analytic features alone.

**OPEN:** derive a *source-history authenticated* comparison between Mellin/impulse-index cancellation and the literal zero-selected integer-winding distribution of \(U_{2B}\) that proves a positive fraction of backward positions separated from zero on **every late shell**. R0 and all-mode π normality remain open. The full root AGENTS gates, Lean, independent mathematical refereeing and hosted CI completion were **not** executed/claimed for this exact addition; older full-suite receipts apply only to their own recorded commits.
