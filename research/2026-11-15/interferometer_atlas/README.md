# Interferometer Atlas — a finite inventory of SUCC π/RH detector families

Start with [THEOREMS.md](THEOREMS.md) for precise proofs and falsifiers, [INSTRUMENT_LEDGER.json](INSTRUMENT_LEDGER.json) for the 30 individually typed families, and [VALIDATION.md](VALIDATION.md) for actual executed checks and limits. Source: draft SUCC #642 at the pinned four-pole/zero-seed original head, no source mutation.

**Two original-to-this-round mathematical detector designs:**

1. **Oily all-frequency:** sample harmonic `h>=1` from original two-stage Oily critical grade conditioned nonzero, and independently sample two authentic zero-seeded BBP shell positions. Signed phase contrast has expectation `C_B=sum_h q_h |W_B(h)|^2`. `C_B->0 iff π is normal in base 16`. Exact full kernel `(4/(2-z)^2-1)/3`; source-specific all-frequency rational-vs-completed error `<=7/(12 B^2)`; truncation tail `(H+3)/(3·2^H)`.
2. **Haar all-depth:** sample future-digit depth geometrically; compare two authentic zero-source shell words by a next-child signed character. Its expectation `H_B=sum_k2^(-k-1)H_{B,k}`, `H_{B,k}=(16sum_children p^2-sum_parents p^2)/15`. `H_B->0 iff π is normal in base 16`; finite-depth error `<=2^-K`.

These are **equivalent open obligations, not proofs of decay**. Oily grade → chosen Fourier harmonic is an explicit new probe choice, not an authenticated dynamic equality of two physical sources. All π detector readouts refer to the original source; any randomness is in the observer's declared selection, not in π. RH has a separate signed source and requires real Gamma/pole/prime-power terms on its actual test domain.

`observational_succ/interferometer_atlas.py` and `tests/test_interferometer_atlas.py` use only standard-library exact `Fraction` data. `independent_oracle.py` independently audits exact grid kernels, certified BBP digits and finite Haar comparisons. Results, hashes and commands are in `VALIDATION.md` and `receipts/`.

**No merge, release, main modification, original BBP edits, historical claim rewrites, new Lean proof, pi normality or RH result.**
