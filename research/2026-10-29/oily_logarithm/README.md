# SUCC — Operation Oily Logarithm

**Research only, 2026-10-29.** Original four-pole BBP forcing and `U_0=0` unchanged. The name is a proposed mathematical instrument, not a new physical law or a proof of π normality.

## Summary

| Feature | Exact result | Scope |
|---|---|---|
| Authentic source logarithm | Continuous zero-normalized Lévy exponent `log[R(a(1-it))/R(a)]`, Gamma(2) limit and first `59` source jet | Source-positive; seed-blind |
| Intrinsic base-16 log inversion | Original root shifts `alpha*beta=16`; `D(a)=log[16(a+3)(a+5)/((3a+16)(5a+16))]` and odd bounded hyperbolic form | Continuous `a>0`, not a discrete native-clock time reversal |
| Oily Gamma/harmonic/golden | Original Mellin log at rank two gives `1-gamma`; declared Oily Laplace probe gives `lambda²`; contrast `lambda-gamma` | Classical ingredients, source-specific `59` correction |
| Two observer geometric mean | Opposing source tilts and symmetric seed shifts satisfy `Psi_+ Psi_- = H Psi_0²` | All central seeds; exact common/relative split |
| Signed branch logarithm | Integer BBP carry is the branch discrepancy and cannot be recovered after ordinary integer-mode exponentiation | Exact all integer times and real seeds |
| q=3 disagreement triangle | Symmetric seed perturbations produce ternary branch variable, mapped by q=3 to two **equilateral-triangle sides**, with exact inverse to `{U_n(c)}` | Seed-sensitive but invertible representation; no new cancellation |
| Analytic signed log | `log E exp(eta M)` analytic uniformly for `|eta|<log 2`; derivatives retain actual selected phase and source covariance | Does not imply a signed all-N estimate |
| Log-smearing countercontrol | Euler gamma and ±90° finite parts arise **for every seed/source** | Universal no-go against source-free inference |

## Proof and reproduction

- [Complete mathematical report](RESEARCH.md) — definitions, 8 locally proved/verified constructions and precise limitations
- [Claims ledger](CLAIMS.md) — paper/classical/instrument/open statuses
- [Hostile controls](NEGATIVE_CONTROLS.md) — changed source/seed, branch erasure, q=2 failure
- [Validation](VALIDATION.md) — exact commands, scopes, errors corrected and nonclaims
- [Next proof obligation](NEXT.md) — original-zero-seed signed common-mode carry inequality
- [Exact production research module](oily_logarithm.py), [13 focused tests](test_oily_logarithm.py), [independent symbolic oracle](independent_oracle.py), [numerical oracle](numerical_oracle.py)

**Local check:** `python test_oily_logarithm.py -v && python independent_oracle.py && python numerical_oracle.py`. All of these were run in the standalone package. The complete native SUCC suite, hosted CI, Lean, math-memory rebuild and independent academic review have **not** been run on this new research head. Keep DRAFT; no main merge or theorem promotion authorized.
