# Prime Genesis: claim supplement and execution boundary

Companion: [`research/2026-10-17/PRIME_JET_GENESIS_AFFINE_RIGIDITY.md`](../research/2026-10-17/PRIME_JET_GENESIS_AFFINE_RIGIDITY.md).

**Objective:** Reconstruct *arithmetic laws* rather than simply enumerate an abstract multiplicative carrier. A free prime-word monoid and its log spectrum always have a rank-successor, but its rank need not preserve multiplication. Authenticated general SUCC/Weil sources have **not** supplied the global rank-dilation law.

| Claim | Exact scope | Status |
|---|---|---|
| PJG-01 | `μ=exp_*(J/t)` and positive-gap-local finite Euler/jet identity | CLASSICAL / PAPER PROVED |
| PJG-02 | `log_*μ=J/t`, exact primitive recovery, collision multiplicity | CLASSICAL / PAPER PROVED + EXACT FINITE TESTED |
| PJG-03 | Uniform dilation count iff affine braid for collision-free ranked support | PAPER PROVED / condition on *all* source states |
| PJG-04 | Global braid makes rank multiplicative; increasing multiplicative spectrum is n^c | PAPER PROVED / conditional |
| PJG-05 | One independently normalized Archimedean unit cell fixes c=1 | PAPER PROVED / conditional |
| PJG-06 | Finite source/oracle/countermodel/56 systematic triple replay | TESTED EXACT FINITE (local focus only) |
| PJG-07 | Any free positive jet source must be the natural integers | REFUTED: q3=3/2 collision-free |
| PJG-08 | Single unit calibration forces the natural numbers | REFUTED: q3=9/2 collision-free and calibrated |
| PJG-09 | Global affine law alone fixes physical scale | REFUTED: q_p=p^c |
| PJG-10 | FUCC word cost of SUCC-one is uniformly bounded | REFUTED: successive 2^k−1→2^k |
| PJG-11 | Globally integral, positive rational diagonal equals positive integers | CLASSICAL; presupposes Q and all genuine local valuation rings |
| PJG-12 | Full causal/Tate source laws **derive** UDC without assuming N | UNVERIFIED — *next decisive proof gate* |
| PJG-13 | Positive finite Mellin source / arithmetic measure proves signed Weil positivity | REFUTED AS AN INFERENCE; RH OPEN |

Tests/finite receipt are in `tests/test_prime_jet_genesis.py`, `scripts/prime_jet_genesis_probe.py --verify`, and `research/2026-10-17/PRIME_JET_GENESIS_RECEIPT.json`.

Original Tate/Weil/Suzuki code, source passports, and provenance archives are unchanged. **No zero locations as input; RH PROVED: NO.**

## Profinite-index-derived route (additive second checkpoint)

See [`research/2026-10-17/PROFINITE_INDEX_SOURCE_GENESIS.md`](../research/2026-10-17/PROFINITE_INDEX_SOURCE_GENESIS.md).

| ID | Claim | Status |
|---|---|---|
| PIG-01 | In full procyclic `Zhat`, open subgroups are precisely `nZhat`, of index n | CLASSICAL / PAPER PROVED under full inverse-limit source |
| PIG-02 | Maximal proper open subgroups correspond to finite simple cyclic quotients and primes | CLASSICAL / PAPER PROVED |
| PIG-03 | Reciprocal Haar index determines q_p=p and log p; CRT gives products, resulting SUCC affine braid | CLASSICAL / PAPER PROVED, **conditional on full profinite and source-map hypotheses** |
| PIG-04 | Actual subgroup enumeration and controls for C64/C30/C210 | TESTED EXACT FINITE (10 focused tests) |
| PIG-05 | A finite cyclic or pro-p observer alone gives all natural-number arithmetic | REFUTED: omitted-prime/finite-depth controls |
| PIG-06 | Physical/source observer can complete every cyclic quotient and certify universal cofinality | UNVERIFIED |
| PIG-07 | Profinite subgroup counts establish signed Weil positivity/RH | NO; RH OPEN |

This is a stronger **sufficient** source law than bare prime jets; it is not claimed as an independent foundational derivation of natural numbers, since the full universal cyclic quotient structure already imports significant integer arithmetic.
