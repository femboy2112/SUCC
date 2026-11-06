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
- **RENORM-2** (barrier, **corrected 2026-11-03**): iterate RENORM-1 at a **common depth**
  `j=⌊log₁₆(A^{3/2}/H)⌋` across the whole band `{1≤|h|≤H}`. Then `h↦16^j h` is injective, so the
  band maps to *distinct* high frequencies `≤A^{3/2}` with accumulated error
  `≤2j/A+π|h|(16^j−1)/(4A(8A−15))=o(1)` uniformly. Each modulus is preserved up to `o(1)`: mass is
  relocated up the ladder, not killed. The recursion is information-preserving; it cannot, alone,
  drive `Σ_{|h|≤q_A²}|c_A(h)|²` to `o(K_A)`. The missing input is genuine high-frequency
  equidistribution — the OPEN problem. *(The original draft used a per-`h` depth that reached only
  `A^{3/4}√|h|` and was non-injective; see `PROOFS.md` RT-03 and `test_D1/D2/D3`.)*
- **RT-00** (chain direction): `band=o(K_A) ⟹ J=o(K_A) ⟹ E=o(log m) ⟹ π normal`, and separately
  `π normal ⟺ S_N(h)=o(N)`. Only the last is a biconditional — the earlier "band ⇔ J" was an
  overclaim (equally-spaced cloud: `J=1`, unweighted band `=2q`).

## Run

```sh
python research/2026-11-03/renorm_transport/renorm_transport.py              # print receipt to stdout
python research/2026-11-03/renorm_transport/renorm_transport.py --write research/2026-11-03/renorm_transport/FINITE_RECEIPT.json
python research/2026-11-03/renorm_transport/renorm_transport.py --verify research/2026-11-03/renorm_transport/FINITE_RECEIPT.json
python -m unittest tests.test_renorm_transport -v
```

Receipt headline: **0 rigorous-bound violations** (RENORM-1 and the corrected accumulation RT-3a),
worst residual/bound = 0.9809 (RENORM-1) / 0.923 (RT-3a) — tight, non-vacuous; two blind sources
(zero-seed vs odd-conductor) agree to 0; `c_A(0)=1` to precision; the receipt's `defect_regression`
block records the D0–D3 witnesses. `unittest` → **13/13 OK** (8 original + 5 defect regressions).

## Firewall

The exponential sums are a calibrated instrument, not a proof certificate. The identity and
bound are exact/rigorous; the barrier is a method obstruction, not a size theorem. No Galois
average, no inverse-branch averaging, no Haar assumption, no π digits. **Nothing here promotes
π normality, which stays OPEN.** See `PROOFS.md`, `SOURCE_MAP.md`, `VALIDATION.md`, `NEXT.md`.
