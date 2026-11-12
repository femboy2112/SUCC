# Claim ledger — Signed Sieve Carrier (SFC)

Date 2026-11-12. `PROVED LOCAL` refers to paper-level elementary derivation in THEOREMS.md, calibrated with two implementations; **not** a Lean/Coq kernel proof or external blind review. `OBSERVED` refers to exact finite integer computation, never universal certification. `CLASSICAL IMPORT` refers to well-established results in the literature.

| ID | Statement and scope | Verdict | Decisive boundary / hostile receipt |
| --- | --- | --- | --- |
| SFC-01 | Exact `q*s = p*p - c*c = 2p*q-q*q` for the genuine prime-inclusive rough majorant | PROVED LOCAL | Missing restoration of small primes violates `q>=p` |
| SFC-02 | `K_z=P⊗P-C_z⊗C_z` is an increasing quadratic-form lower operator; sieve increments positive | PROVED LOCAL | `K_z` is indefinite, so positivity is not automatic |
| SFC-03 | `K_z -> P⊗P` strongly but `||K_z-P⊗P||=1` for each finite z | PROVED LOCAL | Finite horizon != uniform infinite operator norm |
| SFC-04 | At `z=floor(N^(1/3))`, rough composites within indices <=N are semiprimes; signed source is `-lambda q` | PROVED LOCAL | Requires finite index cap; false on unrestricted H |
| SFC-05 | Exact one-sided majority `2(p*q)>q*q` is sufficient for Goldbach; exact Fourier and Haar signed expansions | PROVED LOCAL | Uniform sign estimate not supplied by mere basis change |
| SFC-06 | Fixed sieve cutoff fails on all sufficiently large multiples of its primorial | PROVED LOCAL + CLASSICAL prime density | CRT arithmetic lower bound vs `pi(N)=o(N)` |
| SFC-07 | At cutoff `z=X^(1/3)`, global signed mass `~(1-(log2)^2)X^2/log^2 X` | PROVED LOCAL + CLASSICAL PNT | Toy P={2,5}, C={3}: positive total mass with negative N=6 coefficient |
| SFC-08 | Cube-root criterion holds for every even N<=500000 | OBSERVED EXACT FINITE | Integer NTT all 249999 cases; separate direct 4095 cases; not asymptotic |
| SFC-09 | Fourth-root cutoff suffices uniformly through 500000 | REFUTED FINITE | Eight exact counterexamples, including N=82862 with L=-2 |
| SFC-10 | Source-blind marginal positivity or finite commutator energy forces Goldbach | REFUTED in model | Prime subset 1 mod 4 has no multiples-of-4 pair, yet retains local machinery |
| SFC-11 | `L_floor_cuberoot(N)(N)>0` for every sufficiently large even N | **UNVERIFIED / OPEN** | Would imply Goldbach; no uniform source-specific signed estimate |
| SFC-12 | Positive global signed energy yields positivity for every even N | REFUTED FINITE | Same toy and fixed-cutoff negative examples |
| SFC-13 | Any one-object/categorical semantics necessarily has less description length than any object-oriented implementation | REFUTED as universal claim | Object-based encoder can share identical generator and reuse same factorization rule; model-specific redundancy alone proved in earlier dossier |

## Boundaries and dependencies

- The source is the actual rational primes, not a random-prime surrogate, π digits, RH spectral input, or a modified prime alphabet.
- Operator `Delta_+` acts on finite-support vectors; do not silently promote unbounded operators to bounded endomorphisms.
- The signed operator K_z has negative eigenvalues; it is a lower operator, not a positive Gram.
- The Liouville identification only holds on a size-`N` source truncation if z is at least the exact cube-root cutoff.
- The finite-scanned cube-root criterion is **stronger than Goldbach**. Its failure at any future input would not refute Goldbach.
- Prior CRT–Haar certificates and classical Buchstab/sieve parity formulations contain related mathematics. No blanket priority claim is made.

## Next verdict-changing test

Produce a *uniform* estimate, from the **genuine** prime source and a controlled sieve at z≈N^(1/3), showing `2(p*q_z)(N)-(q_z*q_z)(N)>0` for all large even N, with a proven error margin and a worked example of the full major/minor-arc or Type-I/Type-II budget. The estimate must fail or explicitly reject p'={primes=1 mod4}, and must retain Chen prime+semiprime mixed-sector information without treating it as prime+prime. No finite computation is a substitute.
