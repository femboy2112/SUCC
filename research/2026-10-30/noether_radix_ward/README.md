# Operation Noether × Radix-Ward — SUCC research handoff

**Date 2026-10-30. DRAFT RESEARCH ONLY.** Exact proposed parent: [SUCC #402](https://github.com/femboy2112/SUCC/pull/402) head `384fe179250a172c2e667c387fdb55bf9589e7a0`, stacked on [#397](https://github.com/femboy2112/SUCC/pull/397), rooted in merged Main XVI. Source and U_0=0 remain immutable. π base-16 normality and RH remain OPEN.

## Start here

1. `NOETHER_RADIX_WARD.md`: full derivation, proofs, arithmetic control and explicit failures.
2. `CLAIMS.md`: theorem domains, scope, statuses and falsifiers.
3. `noether_probe.py`: exact Fraction/Gaussian rational 18 tests: constrained BBP action, seed/carry first integrals, source-specific observer backreaction, local U(1) continuity and work, 3D wave gauge tests, zero-charge non-cancellation control.
4. `radix_ward_probe.py`: exact integer/Fraction 10 tests: 16-radix signed-moment selection, first 17-factor resonance, first 34th balanced moment, shrinking seed cylinder and source/fake controls.
5. `noether_independent_oracle.py`, `radix_ward_independent_oracle.py`: separately implemented SymPy/mpmath checks of source mass 59², coupled-energy variation and first 17-factor/34th-moment identities.
6. `VALIDATION.md`: raw logs, file hashes and tests not run.
7. `NEXT.md`: actual source-selected Weyl/Noether proof obligations.

## Key exact results

- A constrained discrete action for the original BBP forcing has a bulk affine seed-shift symmetry and cotangent Noether charge `16^n p_n`; the fixed authentic U_0=0 boundary *does not allow* nonzero shifts.
- A separate exact first integral reconstructs the circle seed only when literal integer carries are retained. Ordinary differences of one scalar arithmetic phase are pure-gauge with zero loop holonomy.
- A declared Hermitian 3D discrete wave action has a global U(1) symmetry and exact local charge-current continuity. Its charge persists even while time-varying source-dependent edges do work; a complete observer+field action closes the energy account under its declared equations.
- Haar seed integrals of all moments are seed-blind. Balanced moments through order 32 contain NO source phase information. At **17-factor unbalanced** order, the first radix resonance is exactly `∫W_N^16 conjugate(W_N)ds = Σ_(n<N) e(−h r_(n+1)) = N−1+O_h(1)`. At **34th balanced** order, the first pairwise source differences `e(h(r_q−r_p))` appear, with explicit multinomial weights.
- Global Haar moments do not control the marked seed; an **exponentially shrinking** interval of width 16^−N is required for an O_h(1) transfer of the unnormalized Weyl sum. The local result is another equivalent representation, not a signed saving.

**Verdict:** Noether and finite cyclic Ward identities rigorously account for source, boundary and wave charges; they do not yet force phase mixing or π normality. The most promising missing instrument is a *source-derived* noncommuting, zero-seed-sensitive signed history current with gauge-consistent time/space links and a new non-circular long-horizon bound.
