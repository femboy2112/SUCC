# RENORM transport — ×16 Fourier renormalization of the original BBP source

**Draft research. π base-16 normality: OPEN. RH: OPEN (separate program).**

A new quantitative transport lemma on the selected-current front, plus the matching barrier.
It is **general** (holds for any `U_n=16U_{n-1}+f(n)` with small `f`; the BBP source only enters
the bound's constant — it is **not** a source discriminator, verified against scaled mutants).
It does **not** prove the open estimate; it maps the obstruction precisely.

- **RENORM-1** (proved): `c_A(h) = c_A(16h) + ε_A(h)` with the rigorous, tight budget
  `|ε_A(h)| ≤ 2/A + 15π|h|/(4A(8A−15))`, where `c_A(h)=A⁻¹Σ_{n=A}^{2A-1} e(hU_n)`. The error
  comes from one boundary pair (`≤2/A`) and the forcing `Σr(n)`, bounded via the merged SC-6
  numerator inequality `r(n)<15/((8n-7)(8n-6))`.
- **RENORM-2** (barrier): `h↦16h` is injective on frequencies, so iterating RENORM-1 transports
  the SC-8 low band bijectively onto a high band near `A^{3/2}` with `o(1)` budget. The recursion
  is information-preserving; it cannot, alone, drive `Σ_{|h|≤q_A²}|c_A(h)|²` to `o(K_A)`. The
  missing input is genuine high-frequency equidistribution — the OPEN problem.

## Run

```sh
python research/2026-11-03/renorm_transport/renorm_transport.py              # print receipt to stdout
python research/2026-11-03/renorm_transport/renorm_transport.py --write research/2026-11-03/renorm_transport/FINITE_RECEIPT.json
python research/2026-11-03/renorm_transport/renorm_transport.py --verify research/2026-11-03/renorm_transport/FINITE_RECEIPT.json
python -m unittest tests.test_renorm_transport -v
```

Receipt headline: **0 rigorous-bound violations**, worst residual/bound = 0.9809 (tight,
non-vacuous), two blind sources (zero-seed vs odd-conductor) agree to 0, `c_A(0)=1` to precision.

## Firewall

The exponential sums are a calibrated instrument, not a proof certificate. The identity and
bound are exact/rigorous; the barrier is a method obstruction, not a size theorem. No Galois
average, no inverse-branch averaging, no Haar assumption, no π digits. **Nothing here promotes
π normality, which stays OPEN.** See `PROOFS.md`, `SOURCE_MAP.md`, `VALIDATION.md`, `NEXT.md`.
