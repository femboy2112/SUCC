# Borwein delta prime-clock research claims (BDW-01–06)

Main derivations: [Borwein–delta–SUCC dossier](../research/2026-10-19/BORWEIN_DELTA_PRIME_CLOCK.md).
Exact implementation: `observational_succ/borwein_prime_clock.py`.
Independent exact tests: `tests/test_borwein_prime_clock.py`.

**No academic priority claim. ABC OPEN. RH OPEN. Signed completed Weil/Suzuki S4 sign OPEN.**

| Claim | Defined scope | Status / evidence |
|---|---|---|
| BDW-01 | Independent real uniform increments: sinc product times sinc(x) integrates to π/2 times a box probability; first overflow δ has exact δ^m/(2^(m−1)m! ∏a_j) leakage when 0<δ≤2 min a_j | CLASSICAL / PAPER PROVED with exact inclusion-exclusion and simplex derivations |
| BDW-02 | Model widths a_q=1/q for odd true-prime q: plateau persists through q=23, first finite crossing at q=29 with normalized leak ≈1.82013483066771×10^(-12) | PROVED LOCAL exact rational finite result; not a p-dependent residue observation |
| BDW-03 | Genuine q-clock phase 1, phase −1 and nonzero Kronecker delta gates have exact root-of-unity projectors; soft Borwein mass may disagree | CLASSICAL finite Fourier / PROVED LOCAL; a prime p>q automatically passes nonzero gate |
| BDW-04 | Finite wheel sub-Markov operator chain of stochastic jump kernels, integer SUCC steps and exact modular gates has rational surviving-mass evaluation | PROVED LOCAL exact finite paths / independent enumerated oracle; discrete Dirichlet kernel ≠ continuum sinc |
| BDW-05 | Small-step uniform-jump products have Gaussian Brownian scaling **only with additional limit conditions**; fixed prime-width cumulant κ4<0 excludes exact Gaussian; Poisson symmetric SUCC semigroup has distinct factorial weights | CLASSICAL probability/semigroup + PROVED LOCAL finite coefficients; no prime randomness inferred |
| BDW-06 | Replacing modular phase sources by sinc widths or positive diffusion makes an ABC/RH/Weil theorem | REFUTED as inference by missing n-residue input, soft-score plateau, and signed-Weil firewall; proposed uniform arithmetic correlation estimate UNVERIFIED |

**Falsification / next instrument:** source-authenticated p-adic cancellation q^k|(a+b) using actual primitive triples, followed by a held-out growing-modulus CRT stress test and an independently derived integer-height bound. Any positive stochastic kernel must remain separate from the signed completed Weil form.
