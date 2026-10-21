# Effective primitive abc means: reviewed paper claims

These identifiers record complete paper proofs in the
[draft manuscript](../research/2026-10-20/ABC_EFFECTIVE_MEAN.md).
They are not formal proof authority. All sums count ordered positive primitive
triples a+b=c≤X, with H=abc/rad(abc) and S_t(X)=ΣH^t.
Academic novelty is UNVERIFIED; external refereeing remains required.

| Claim | Statement and quantifiers | Status | Boundary |
|---|---|---|---|
| ABC-EFF-01 | Every real X≥2 and pairwise-coprime positive d,e,f: primitive divisor-count discrepancy from X²/(2ζ(2)def)∏_(p∣def)p/(p+1) is at most (3/2)X H_M+X²/(2M), M=floor(X/2) | PROVED LOCAL, uniform lattice slicing and full Möbius proof | Absolute error; no arbitrary moving-modulus relative asymptotic |
| ABC-EFF-02 | Every 0≤t<s<2/3, α>t, 2α−t>1, X≥2 and Y≥1: product-cutoff error is at most E(t,α)[3H_M/(2X)+1/(2M)]Y^α+2K_sY^(-(s−t)/2) | PROVED LOCAL, positive divisor expansion and stronger moment | Explicit convergent products E and K are defined in the manuscript |
| ABC-EFF-03 | Every fixed 0≤t<2/3 and 0<δ<(2−3t)/5: there is an explicit finite C_(t,δ) with ∣S_t(X)/X²−C_t∣≤C_(t,δ)X^(-δ) for all real X≥2 | PROVED LOCAL, optimized cutoff | Endpoint exponent is not asserted; no optimality claim |
| ABC-EFF-04 | Deleting Möbius terms sharing primes with def gives the wrong primitive count: X=4,(d,e,f)=(2,1,1), wrong 2 versus actual 1 | REFUTED proposed truncation, exact counterexample | Full Möbius inversion must reduce each divisor by its gcd with the summation variable |
| ABC-EFF-05 | liminf S_1(X)/(X²logX)≥1/(4ζ(2)log2); for every t>1 and X≥8, S_t(X)≥8^(-t−1)X^(t+1) | PROVED LOCAL, positive single-prime divisor strata and explicit dyadic family | Quadratic bounds fail for t≥1; the interval [2/3,1) remains OPEN |

The [post-main receipt](../research/2026-10-20/ABC_EFFECTIVE_POSTMAIN_RECEIPT.json)
records 11 focused tests and 1,729 exact cases on the actual Main VII base.
Separate same-model proof reconstruction and independently coded arithmetic
holdouts are supporting evidence, not an external referee or Lean verification
of the full analytic theorem.
