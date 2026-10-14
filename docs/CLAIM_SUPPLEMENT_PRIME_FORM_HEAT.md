# Source-typed prime-form heat claim ledger (2026-10-14)

**Branch lineage** PR #65 → PR #67 → `research/prime-form-heat-mellin-2026-10-14`, parent `a29170d4`. Full derivations and numerical/proof boundaries are in [`research/2026-10-14/PRIME_FORM_HEAT_MELLIN_SOURCE.md`](../research/2026-10-14/PRIME_FORM_HEAT_MELLIN_SOURCE.md).

| ID | Scope / verdict | Claim and smallest load-bearing condition | Negative control / next check |
|---|---|---|---|
| PH-01 | CLASSICAL / PROVED MATHEMATICALLY | Complete radix-p `pq+b` partition, Cuntz digit isometries on `ℓ²(Z)`, all finite mixed radix words | Composite p=6 passes; physical source unauthenticated |
| PH-02 | CLASSICAL / PROVED MATHEMATICALLY | Signed affine composition defect `(p−1)c−(q−1)b` | Opposite path permutations diverge; no scalar-Pascal collapse |
| PH-03 | CLASSICAL / PROVED MATHEMATICALLY | IID fair Pascal paths converge to Gaussian heat on polynomial core; exact fourth moment gap and rigorous Fourier error bound in stated regime | Same marginals / correlated latent sign destroys limit |
| PH-04 | CLASSICAL / PROVED MATHEMATICALLY | Poisson/finite Fourier rotation of Gaussian residue heat, with full character phase and normalization | Dropping phase breaks nonzero residue matching; composite p is not prime evidence |
| PH-05 | CLASSICAL / PROVED MATHEMATICALLY | Real local Mellin `Γ_R(s)=π^(−s/2)Γ(s/2)` for Gaussian + Haar choice, Re(s)>0 | Wrong scale or spectral power changes Gamma |
| PH-06 | CLASSICAL / PROVED MATHEMATICALLY | Θ modular transformation gives meromorphic completed Λ and symmetric entire ξ, without zero-location inputs | Requires full lattice, Poisson and analytic split; does not give RH |
| PH-07 | CLASSICAL / PROVED MATHEMATICALLY | `Λ`-weighted residue 0 of genuine p radix isolates `(log p)/(p^s−1)`; general m=p^a truncated vs non-prime-power zero | m=4 vs m=6 sharp arithmetic source mutation |
| PH-08 | CLASSICAL / PROVED MATHEMATICALLY | Genuine prime jet heat Mellin is `Γ_R(s)(−ζ'/ζ)(s)` for Re(s)>1 | No zero oracle; *not* identified as Weil form or its positive completion |
| PH-09 | CLASSICAL / PROVED MATHEMATICALLY | Rigorous finite N Dirichlet tail majorant from monotone log/n^σ, σ>1,N≥3 | Large finite interpolation does not prove half-plane continuation |
| PH-10 | CLASSICAL / PROVED MATHEMATICALLY | Depth p^k multiplicities yield `ζ_p(s−1)`; normalized weighted functional yields `ζ_p(s)` | Ordinary Hilbert trace ≠ introduced weighted trace; still prime blind |
| PH-11 | OBSERVED / COMPUTATIONAL | Numerical quadrature, complex theta reflection, residue duality, exact rational path/test controls, frozen receipt | Exact manuscript proof not replaced by computation; run exact-head remote CI |
| PH-13 | CLASSICAL / PROVED MATHEMATICALLY | One global Gaussian Mellin `Γ_R(s)` applied to the joint P-smooth carrier yields Γ_R times product of finite prime geometric factors | Wrong independent-Gamma-per-prime product gives Γ_R^r; exact rational independent word oracle |
| PH-14 | CLASSICAL / PROVED MATHEMATICALLY | For real σ>1, ζ(σ)-finite-prime Euler cutoff nonnegative and bounded P^(1-σ)/(σ−1), extend to complex modulus via Re(s) | Direct mpmath ζ vs rational finite Euler, all term tails not guessed |
| PH-15 | CLASSICAL / PROVED MATHEMATICALLY | Every fixed P finite-prime Euler converges Re(s)>0, but P→all primes diverges for real 0<s<=1 by harmonic-prefix domination | Rules out naive interchange of infinite prime limit and analytic continuation |
| PH-12 | UNVERIFIED | Empirical source-law calibration, general stochastic/quantum operator descent, coherent Weil/Suzuki domain identification, positivity, RH | Source-authenticated experiments and independent distributional analytic theorem needed |

**Sources/limits:** Prime-power primality is certified in an abstract integer model, NOT physically measured. No fabricated instrument or unperformed zero observation; all source/prior labels remain declared mathematical metadata. No new independent academic priority asserted. Parent tests/receipt copied only to the isolated validation overlay and not republished as part of this PR. Open RH obstruction is unchanged.
