# Gaussian Unit Gluing — recovered source object

Research-only additive 2026-11-03 work, stacked on PR #479. Original BBP forcing `r(n)` and `U0=0` remain immutable. No pi-normality proof or RH implication.

The **full** original scalar BBP transfer has a canonical reachable-observable rational minimal realization, described by the four-dimensional commutative semisimple **Frobenius algebra** `Q[s]/((s²−1/2)(s²−s+1/2)) ~= Q(sqrt2) x Q(i)`. A canonical half-clock involution `C=4s^4` and idempotents `(1±C)/2` restore its two spectral channels from scalar impulse samples `c_n,c_(n+4)`.

The uniquely source-selected trace weight is `w=−8s³+2s²+2s−1`; the BBP eight-tap numerator and four Mellin forcing terms follow by exact rational moment extraction. The two canonical channel integrals are `−2log2` and `π+2log2`; their O(1/n) forcing contributions cancel. Even more sharply, the separate channels each have a 2-adic pole `±1/(32t)` at source index zero and nonintegral rational values, while their full gluing is the integral, 2-adic-isometric original source. **Glue before p-adic quotienting.**

Only the complete transfer with readout fixes this object: an explicit higher-jet mutation preserves the same atoms/clock/c0/first endpoint jet but changes the integrated constant by `67 eps /480`. Exact Gaussian phases do not automatically prove selected real Weyl cancellation.

Files: [proofs](PROOFS.md), [source map](SOURCE_MAP.md), [next probe](NEXT.md), [validation](VALIDATION.md), [finite receipt](EXACT_RECEIPT.json), implementation `gaussian_unit_gluing.py`, independent symbolic oracle `symbolic_oracle.py`, and two root-style tests.
