# ORBIT CLOCK GENESIS — claim supplement / source-relative certificates

Companion: [`research/2026-10-17/ORBIT_CLOCK_GENESIS_MINIMAL_SOURCE.md`](../research/2026-10-17/ORBIT_CLOCK_GENESIS_MINIMAL_SOURCE.md). **New bare prefix `OCG`**, unrelated to `SM.MIN` and `SM.SUZ` and never a license to invent claims absent from this table. Mathematical paper proofs are separately classified from tested finite instances. **RH PROVED: NO**.

| ID | Mathematical claim | Status / source boundary |
|---|---|---|
| OCG-01 | Rooted unary source on actual orbit admits C_m iff every repeated-state relation respects mod m; all m iff orbit injective | CLASSICAL / PAPER PROVED; discrete set-level factor, not physical test |
| OCG-02 | Every finite prefix of free ray has later-return periodic shadow; internal C_m does not imply actual external-source quotient | PAPER PROVED + exact finite tests; no finite no-return proof |
| OCG-03 | Fresh-state root-edge splice constructs C_(m+1) from C_m; not a quotient refinement for m>=2 | PAPER PROVED + exact finite machine; source access additional |
| OCG-04 | Rooted common clock of all periods <=N has least size L_N, and cofinal lcm tower completes to Zhat | CLASSICAL / PAPER PROVED; all periods are input constructions, not measured environment property |
| OCG-05 | Capacity jump L_N/L_(N-1) equals p exactly for N=p^k and 1 otherwise, so its symbolic log is Lambda(N) | CLASSICAL Chebyshev / PAPER PROVED + exact finite checks |
| OCG-06 | Divisor-clock join-irreducibles are exactly prime powers; incidence Möbius transform of log periods independently recovers Lambda | CLASSICAL / PAPER PROVED + separate finite implementation; shared mathematical source |
| OCG-07 | Any faithful deterministic simultaneous recurrent readout for periods <=N needs >=L_N states, L_N>=2^(N-1)/N | PAPER PROVED elementary exact state/bit bound; not physical thermodynamic work |
| OCG-08 | On compact root-orbit closure, a continuous C_m factor exists iff modular residue-subsequence closures are pairwise disjoint | PAPER PROVED; continuity required, cannot infer from finite samples |
| OCG-09 | If all continuous factors exist, their map to Zhat is surjective; it is an isomorphism iff finite factors jointly separate source points | PAPER PROVED; hidden-fiber no-go |
| OCG-10 | Infinite injective orbit by itself forces continuous clock factors | REFUTED by compact contraction x -> (1+x)/2 |
| OCG-11 | Autonomous instrument clock upgrades original finite source period or creates original-source prime evidence | REFUTED by C4 external source x C5 instrument |
| OCG-12 | Finite compatible clock evidence certifies a completed universal clock source or signed Weil positivity/RH | REFUTED inference / RH OPEN; physical source validity UNVERIFIED |

**Execution:** `python -m unittest discover -s tests -p 'test_orbit_clock_genesis.py' -v`, the companion incidence and topological test files, and `python scripts/orbit_clock_genesis_probe.py --verify`. Claim namespace registry `OCG` is additive; historical IDs and source archives remain unmodified.
