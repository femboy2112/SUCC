# MOG — Multiplicative orientation Gram, log-prime filtration and cross-prime obstruction

**Parent:** SUCC PR #169 research/connes-oriented-local-trace-2026-10-18; parent exact Connes local proof ledger docs/CLAIM_SUPPLEMENT_CONNES_ORIENTED_SCALING.md. **Paper:** research/2026-10-18/MULTIPLICATIVE_ORIENTATION_GRAM.md. **Code:** observational_succ/multiplicative_orientation_gram.py and tests/test_multiplicative_orientation_gram.py. All underlying integer Gram/negative-type theorems are classical or elementary; new-to-project synthesis, not new priority.

| Claim | Status / exact boundary |
| --- | --- |
| MOG-01 | **PROVED CLASSICAL:** K_D(m,n)=gcd(m,n)/sqrt(mn) and K_A(m,n)=min(m,n)/sqrt(mn) have explicit normalized divisor-totient and interval-indicator Gram factorizations, hence PSD on *every finite label set*; complex coefficients valid. |
| MOG-02 | **PROVED:** both are simultaneous multiplication-invariant and coincide along every divisibility chain; K(1,p^k)=p^-k/2; cross-oracle matches COT-06 local Connes half-density squared. |
| MOG-02a | **PROVED:** arithmetic and interval feature vectors each densely span the same ℓ²(N), inducing two isometric representations T_a F_n=F_an. Their distinguished vacuum e1 agrees but the (2,3) orbit Gram differs, so no vacuum-preserving unitary intertwiner exists. |
| MOG-03 | **PROVED:** K_A-K_D has nonzero offdiagonal and zero diagonal at (2,3), hence is indefinite; convex interpolation yields continuum of PSD chain-agreeing completions, so jet observations don't uniquely determine all cross-prime correlations. |
| MOG-04 | **PROVED:** G(m,n)=log gcd(m,n) is PSD from p^k divisibility indicators weighted log p; log K_D=G-(log m+log n)/2 is conditionally PSD on zero-sum vectors, equivalently d_D is of negative type. This is NOT original completed Weil positivity. |
| MOG-05 | **PROVED LOCAL MAGNITUDE:** primitive FUCC increment d_D(p^k,p^(k+1))=log p and K_D(1,p^k)=p^-k/2 reproduce Λ(p^k)/sqrt(p^k) magnitude after single-prime projection; n=6 is NOT prime jet; global Weil signs/contact/Gamma not obtained. |
| MOG-06 | **PROVED TOPOLOGICAL OBSTRUCTION:** along log((n+1)/n)->0 the divisor PSD kernel tends to 0, while Arch interval kernel tends to 1. Consequently bare divisor kernel has no continuous extension to R in ordinary log topology; this does not obstruct an adelic topology. |
| MOG-07 | **UNVERIFIED:** identify original all-place Weil form, with canonical contact and domain, with one of these Gram forms or a source-derived compression/transport; prove global Connes trace or RH. |

**Hostile and positive controls:** exact totient divisors through n=300; signed coefficient exact Gram squares; real interval oracle; simultaneous multiplication; comparable/incomparable pairs; genuine 2,3,5,7,11 prime jets; composite6 non-prime stratum; log-filtration zero-sum guard; successor n→n+1; contact and Fourier/Weil signs remain unresolved. The algebraic proof of the theorems is in the paper; finite tests cannot prove universality.

**Reproduce:** python -m unittest discover -s tests -p 'test_multiplicative_orientation_gram.py' -v; combined focused Connes workflow on the exact GitHub head. **RH PROVED: NO.**
