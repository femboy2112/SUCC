# SUCC Operation LAPLACE CRITICAL × Phase-True Adelic Boundary

**Status 2026-11-08: PI BASE-16 NORMALITY OPEN; selected zero-seed signed Abel boundary OPEN; RH OPEN.** Research branch stacked on PR #558 at `46b96e61ea8a309546b399da328c9bfcc077ada2`. Original 4 signed poles, zero seed and archived provenance untouched.

## Why this front

The user's hypothesis: signed prime-phase cancellation may be more accessible in the Laplace/analytic domain, where all-scale source gluing and Euler-Mascheroni corrections are explicit. Prior SUCC #496 already owns the **bounded Abel/Cesaro equivalence** and Gamma(2) observation, so we do not present that as new. PRs #556/#558 own all-scale source defects and exact additive-adelic phase reconstruction; #555 owns the critical A² source-coboundary separation.

## Results

1. **Exact positive Stieltjes source:** `R(z)=z integral_0^1 (4−2u³−u⁴−u⁵)/(1−zu⁸)du`, with genuine `15/64*(1−z)log(1/(1−z))` near-boundary branch.
2. **Euler–Mascheroni seam, proved with explicit tail:** sharp `sum n r(n)` and Abel `R'(z)` finite-part constants differ by exactly `(15/64)*gamma`. This is source-normalization, not signed Fourier decay.
3. **Critical source-frequency obstruction:** the genuine Ward source correction vanishes in normalized Abel form only for `|h| t²->0`, not uniformly at `|h|~t^-2`. An actual source-only critical response has a nonzero explicit integral limit with square-root Gamma(1/2) cusp. It is *seed blind* and shared by matched-leading source mutants.
4. **Exact signed prime/complement Laplace spectrum:** product across all finite prime characters becomes a finite cyclic Fourier inner product (not the product of the marginal Laplace transforms). A sufficient low-frequency/high-frequency separation bound is proved; its high-complement-energy hypothesis remains unverified and looks unfavorable on already inspected epochs. Target signed high-mode overlap instead.
5. **Hard negative controls:** coherent wrong seed has Abel residue 1 for fixed h despite the same source law, and the critical source-only response is shared with a distinct four-pole source. Neither scale covariance nor positive Laplace weighting gives free normality.

## Evidence and use

- [THEOREMS.md](THEOREMS.md): exact derivations, conditional gates and countermodels.
- [PREREGISTRATION.md](PREREGISTRATION.md): first commit, before the new 9 critical-source numerical probes.
- [FINITE_RECEIPT.json](FINITE_RECEIPT.json): MP60 and independent double-precision finite critical source diagnostics, exact rational four-pole replay and an explicit omitted-tail budget. No asymptotic inference from finite data.
- [VALIDATION.md](VALIDATION.md): exact tests, independent replay and GitHub CI scope.
- [NEXT.md](NEXT.md): source-selected Laplace cross-prime resonance research assignment and hostile controls.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md): claim provenance/authority.
- `observational_succ/laplace_critical_source.py` and `tests/test_laplace_critical_source.py`: additive new library code and root-discoverable regression tests. Code imports canonical `duck_bbp.forcing` and the inherited `adelic_additive_gluing.local_additive_fraction`, not a new four-pole implementation.

**Next real proof:** for every fixed integer `h!=0`, force the actual zero-seeded signed overlap `sum_k ahat_(A,p,h)(k) bhat_(A,p,h,tau)(−k)->0` for the balanced eligible p_A, or prove #554's forcing-corrected signed covariance upper bound. This must fail for coherent wrong-seed controls; otherwise it is only an observer transform.
