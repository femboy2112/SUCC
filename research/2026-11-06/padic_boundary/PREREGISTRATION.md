# BBP real/2-adic dual-boundary experiment — preregistration

2026-11-06. Branch `research/bbp-2adic-boundary-conservation-2026-11-06`; parent PR #526 at `d2960bacf939fbdfa76c81648b031e182e97d1a6`.

## Provenance/chronology

The preliminary 2-adic series `V(0)=sum_{j>=0}16^j r(-j)` had **already been inspected** at binary precisions 4 through 1024 before this registration. Its zero residues at those precisions are CALIBRATION, not fresh blind holdouts. An algebraic/logarithmic proof candidate was also discovered before this registration. No status promotion will rest on the finite zero observations.

## Frozen source and intended proof

`r(z)=(120z^2-89z+16)/((2z-1)(4z-1)(8z-7)(8z-3))`, literal `U0=0` on the original real recurrence. No edits to preserved sources, original contracts, production, or formal Lean.

Test the candidate identity `V(0)=0` with a proof from the formal power series `F(x)=sum_{j>=0}16^j[-4x^(8j+7)/(8j+7)+2x^(8j+4)/(8j+4)+x^(8j+3)/(8j+3)+x^(8j+2)/(8j+2)]`, whose derivative has denominator `1-16x^8`. Show its logarithmic primitive vanishes at x=1 in `Q_2(i)` because the endpoint logarithms have fourth-root-of-unity arguments. Verify the rational derivative and source compactification with an independent symbolic oracle.

## New held-out exact modular probes fixed *before* inspecting outputs

- Binary precisions `k=2048` and `k=4096`: compute `sum_{j=0}^{ceil(k/4)} 16^j r(-j) mod 2^k` using odd-denominator modular inverses; expected 0. Distinguish this from a proof.
- Mutate first original pole weight `4 -> 5` at all integer indices: compute the new past boundary modulo 2 and modulo 256; expected nonzero modulo 2.
- Test finite memory and source periodicity modulo `2^k` at `k=11,12`, compare `U_n(0)` and original `V(n)` with a modular recurrence at n=0,1,2,17,257; assert exact period `2^k` when enough n are checked. No claim of the minimal period.
- Coboundary mutant `H(z)=z/(2z-1)^4`, `r_H(z)=r(z)+H(z)-16H(z-1)`: assert H(0)=0, past boundary V_H(0)=0 at k=2048, exact source/carry identity `U_n^H=U_n+H(n)` for n<=20, and exact real finite-tail telescoping; **expect this source mutant to share both boundaries**, falsifying source-identification from dual matching alone.
- Real/2-adic seed contrast with rational shift s=1/5: verify `16^n/5` converges to 0 2-adically while its real fractional part remains `1/5` for all tested n; this refutes 2-adic convergence -> real-circle convergence.

## Verdict policy

The 2-adic equality, if proved algebraically, is a new SUCC-local source identity, **not** a proof of pi base-16 normality or a claim of external priority. If the analytic proof fails, retain exact finite checks as OBSERVED-FINITE and label equality UNVERIFIED. If the coboundary mutant survives, record both-boundary source uniqueness as REFUTED with its explicit witness. No main merge, release or publication.
