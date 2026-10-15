# Claim supplement — completed prime/heat/Gamma → Weil/Suzuki identification

**Branch:** `research/real-place-weil-identification-2026-10-14` stacked on prime-form heat commit `53934b3a5a980bb0f6e1001241822da5b6d928e5`. No changes to `main`. Mathematical domain is standard Gaussian and genuine zeta/von Mangoldt source. **RH PROVED: no**. Completed Weil equality relies on the classical external Weil explicit formula in Masatoshi Suzuki (2025) Eq. (3.3). This is **not** a new global sign theorem or source authentication.

| ID | Status | Scope and result | Failure/next probe |
|---|---|---|---|
| CW-01 | CLASSICAL/DERIVED | Gaussian heat Mellin = Gamma_R times authentic prime Dirichlet logarithmic derivative for Re(s)>1 | Reject fake-6 and wrong Gaussian powers |
| CW-02 | CLASSICAL/DERIVED | Fourier uniqueness on one complete Re(s)=σ>1 vertical line identifies positive weighted prime atomic source | Finite samples insufficient; specify source map |
| CW-03 | PROVED LOCAL | Explicit prime-tail majorant N^(1−σ)[logN/(σ−1)+(σ−1)^−2] at N>=3,σ>1 | Diverges as σ↓1; no critical-strip limit |
| CW-04 | CLASSICAL/DERIVED | Complete ξ'/ξ is **additive** pole + Gamma log derivative − normalized prime heat | Gamma product is wrong type |
| CW-05 | EXTERNAL THEOREM | Source-exact signed Weil distribution on Cc∞ with half-density, Gamma contact, pole and true primes | Weil (1952), Suzuki (2025) Eq (3.3), not independent proof |
| CW-06 | CLASSICAL/DERIVED | Real Gamma arch subtraction gives a well-defined compact C² distribution; H1 signed extension | No positivity inferred |
| CW-07 | PROVED LOCAL/CLASSICAL | Digamma Fourier symbol gives precisely −(γ+log4π)h(0) and renormalized continuous term | Wrong contact misses 2log2 |
| CW-08 | CLASSICAL/DERIVED | Conductor q gives log(q) contact and odd parity gives correct separate arch kernel | Not full Dirichlet L completion or root-number source |
| CW-09 | PROVED LOCAL | Signed finite Gamma ladder absolute remainder ≤C[1/(2a_J)+1/a_J²] on Cc² | Coefficient/source mutations retained |
| CW-10 | PROVED LOCAL | Corrected A_J−h(0)/(4J+1) has explicit O(J^-2) C² bound | Incorrect counterterm orientation fails |
| CW-11 | PROVED LOCAL | Uniform signed Weil H1_0(-a,a) form-norm remainder ≤ε_J∥v∥H1∥w∥H1, ε_J=O(J^-2) | No PSD factorization; all-vector lower sign still RH-hard |
| CW-12 | CLASSICAL/DERIVED | Exponential-Cauchy test family a>1/2 gives W(e^-a|x|)=2ξ'/ξ(a+1/2), zero-independent evaluation | One family not entire compact test space |
| CW-13 | PROVED LOCAL | Source-first Ψ(R)=W[(R−|x|)_+]/2 even, Ψ''=W in distributions | Preserve x=0 contact/atoms, not pointwise proof there |
| CW-14 | PROVED LOCAL/CLASSICAL | Prime finite + pole/Gamma signed Ψ formula from CW-05 | External Weil identity source dependency |
| CW-15 | PROVED LOCAL | Elementary Gamma rung I_j(R), |Ψ−Ψ_J|≤(1+R/2)[1/(2a_J)+1/a_J²] | No global operator limit |
| CW-16 | PROVED LOCAL | Away from atoms Ψ'' regular density matches gamma finite ladder; all source atoms remain distributional | Atoms must not be erased |
| CW-17 | PROVED LOCAL | Fake-6 positive connected impulse changes Ψ by −δ log6/√6 (R−log6)_+ | Breaks Euler multiplicativity |
| CW-18 | PROVED LOCAL | Positive Dirichlet coefficients yet Ψ_fake(2)<17−δ/30; at δ=1000 K_fake(2,2)<0 | Altered completion lacks functional equation and order-one growth |
| CW-19 | PROVED LOCAL/CLASSICAL | Compact source-derived differentiated K is a signed Hilbert–Schmidt/compact operator; no strictly positive H1 coercivity gap | Near-positive all-test lower bound remains open |
| CW-20 | UNVERIFIED | Genuine complete Weil form Qζ is nonnegative on all compact tests / Suzuki global limit | Equivalent to RH; no finite simulation establishes it |

**Evidence separation:** Exact Fraction bounds and algebraic analytic proofs are statements on infinite test classes. High-precision mpmath integration is a calibrated numerical oracle, not certified interval arithmetic. Real physical-source calibration, independent scholarship, general Dirichlet L root-number transport, formal Lean kernel verification and a positive factorization are not supplied.
