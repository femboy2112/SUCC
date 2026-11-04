# Finite real Fourier holdout declarations and failed-attempt log

**Batch 1 (pre-result):** Take first 3 primes p>4000 with p=5 modulo 8, namely 4013, 4021, 4093, with h=1,3,5,7. Before phase evaluation fix the strict target \(|W_p(h)|/|I_p|<1/8\), with L1 rational upper certification (stronger than just the modulus). All 12 subsequently PASS. Later noticing that all 12 also satisfy <1/16 is POST HOC, not a prespecified threshold.

**Batch 2 (pre-result):** Written in the local record BEFORE evaluation: "take the first three primes above 10000 congruent to 5 mod 8, namely 10037, 10061, 10069. Check harmonics h=1,3,5,7 using the same exact Fraction + Machin + dyadic + Taylor interval oracle. Target normalized L1 bound <1/16 for all 12 cases. Record all outcomes even if failures. Same author/reasoner, not independent validation." All 12 PASS.

**Failure preserved:** a combined >10000 evaluation was interrupted by the container execution timeout after outputting p=10037. The three p=10037,10061,10069 cases were each rerun individually and all passed. Their exact rounded-up rational upper bounds, not only floating diagnostics, are retained in FINITE_WINDOWS.json.

**Not blind:** all selection/preregistration, implementation and review were done within the same model session. This is not an independent group or true holdout from the general theorem. Finite success has no implication for all p or all h.

**Negative controls:** exact changed-source zero-seed coherent orbit; same-original-source altered irrational seed -pi/16; both have rigorous normalized window modulus >1-2pi|h|/(p+4)^2 for every relevant p. These exclude any scheme that infers cancellation solely from prime births, large denominator, zero seed plus all-order source expansion, or source-only observables.
