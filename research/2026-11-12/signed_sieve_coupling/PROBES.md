# Analytical assault plan — from signed carrier to a uniform positive coupling

**Goal:** Prove or refute the *stronger* source-specific signed conjecture `L_floor_cuberoot(N)(N)>0` for sufficiently large even N; success plus a finite small-N check would prove Goldbach. It is allowed for this signed conjecture to fail while Goldbach holds. All experiments below are **research probes**, not planned proof outcomes.

## Target and quantitative sufficient criterion

For `z=floor(N^(1/3))`, define

```
A_z(N)=sum_{p prime, 2<=p<=N-2} q_z(N-p)            [prime + rough]
B_z(N)=sum_{a=2}^{N-2}q_z(a)q_z(N-a)              [rough + rough]
L_z(N)=2 A_z(N)-B_z(N).
```

The necessary theorem **for this strategy** is `A_z(N)>B_z(N)/2`. A quantitative route would prove, for some `epsilon>0,N_0` and every even `N>=N_0`,

`2 A_z(N)-B_z(N) >= epsilon*N/(log N)^2`.

This is *not* implied by Chen's prime-plus-semiprime theorem, by positive CRT local densities, by `K_z<=P⊗P`, or by the globally positive signed mean of SFC-07.

## Route A — prime in the two-sided rough corridor

Let `J_{N,z}={a in [2,N-2]: q_z(a)q_z(N-a)=1}`. Then `B_z=|J|` and `A_z=|J intersect Primes|`. Prove a **uniform prime majority** inside this specific doubly-sifted set. The simplest error-contract version is:

- a rigorous sieve count `B_z(N)=B_main(N)+E_B(N)`;
- a prime-in-sifted-complement count `A_z(N)=A_main(N)+E_A(N)`;
- independent source-derived bounds `2A_main-B_main>eta N/log²N` and `2|E_A|+|E_B|<eta N/log²N`.

This would genuinely pay the proof debt. Mere heuristic singular series or an estimated average over N is inadequate. CRT modulus `prod_{p<=z}p` is astronomical when z=N^(1/3), making naive full-residue equidistribution invalid; try combinatorial Buchstab identities, explicit sieve weights, Type-II dispersion, and source-specific parity-sensitive terms. Retain small primes at the boundary.

## Route B — signed Liouville oscillation, preserving the true source

At cube-root cutoff, `s_z=-lambda q_z` on the sum fiber, giving

`L_z(N)= -sum_{a+b=N}q_z(a)lambda(a)q_z(b)`.

The only missing sign is the arithmetic correlation, not the category, not the phase projector. The local CRT factors can model the major arc; the minor arc needs **signed**, source-correlated control sufficient at the single N coefficient. See Tao (2012) on the binary circle-method obstruction and Bhowmik–Grimmelt (2026) on major arcs / exceptional sets.

**Do not** substitute raw Liouville sign-pattern results on *unrestricted* integers: parity -1 includes numbers with 3,5,... prime factors. The cube-root rough restriction is load-bearing and is not a free consequence of Liouville cancellation.

## Route C — monotone sieve-scale flux (Scott-compatible)

For `z<z'`, let `e=c_z-c_{z'}` denote the composites killed by the next prime(s). Then

`L_{z'}(N)-L_z(N) = 2(c_{z'}*e)(N)+(e*e)(N)>=0`.

This is an exact nonnegative flux as the observer refines its arithmetic source. Investigate whether an independently estimated cumulative flux can cross zero by a **sub-square-root** sieve cutoff. But the identity alone is not a proof: the flux terms encode composite-pair correlations, and proving their sum crosses zero is itself the hard estimate. No fixed cutoff can work for all large N (SFC-06).

The observed minimal certifying cutoff `z_*(N)` does not exceed floor(N^(1/3)) for even N<=500000. A stronger exponent such as 1/4 is already **refuted finite** at eight targets, so avoid overfitting small data.

## Route D — signed Haar and transport of actual errors

For each N construct `a_k=q_z(k), b_k=s_z(N-k)`, dyadically padded. Parseval gives exact `L_z=AB/M+sum signed detail bands`. A partial coefficient cut must carry a rigorous bound on the remaining signed details, not replace them by positive energy. In particular the finest positive band at N=2048 is offset by negative medium bands. Compare original source, Chen-style source, and matched counterfeit before promising all-scale positivity.

## Calibration / hostile models

- **Positive control:** genuine primes and exact source masks with N=20,100,2048,8192,100000; both R and signed L computed independently.
- **Negative control:** substitute `p'={primes p:p=1 mod 4}` (a *changed source*) at even N multiple 4; no Goldbach-style witnesses remain, so any source-blind certificate claiming positivity is invalid.
- **Null control:** fixed z with N a large multiple of primorial `M_z`; the strong signed lower condition must eventually fail.
- **Resolution mutation:** use z=floor(N^(1/4)); the eight known failure inputs must remain negative/unresolved, with N=82862 giving L=-2.
- **Boundary mutation:** incorrectly remove the small prime ell itself when sieving its multiples; reject because q no longer majorizes the genuine prime source.
- **Scott mutation:** an unresolved primality label cannot be promoted to prime just because the lower defect interval contains zero.
- **Large-N holdout:** a source-independent analytic bound must apply to new unexamined even N above the existing exact range and to adversarial arithmetic progressions, not just random samples or fitted constants.

## Go/no-go acceptance criteria

**GO** for a theorem claim only after a proof establishes explicit domains, source provenance, signed term bounds, and nonnegative error payment for every relevant N, and independent review rules out the changed-prime controls. **NO-GO** for proof promotion if an estimate uses `R(N)` or precomputed Goldbach witnesses in its premises, if local PNT is silently applied to primorial-size moduli, or if a pointwise theorem is inferred from an average/global Hilbert norm. A failed stronger conjecture must be recorded as a counterexample to SCG, not as failure of Goldbach.
