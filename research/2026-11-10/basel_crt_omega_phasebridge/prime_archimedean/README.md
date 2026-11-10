# Operation PRIME–ARCHIMEDEAN × Basel–Ω × Weil wavepacket

**10 November 2026 · research-only continuation of SUCC draft PR #585** (itself stacked on #584). Original four-pole source, literal `U_0=0`, provenance, historical dossiers, main, Lean, CI and release state are unchanged.

**Status.** The formulas in [WEIL_PACKET_PROOFS.md](WEIL_PACKET_PROOFS.md) are derived from the classical completed Guinand–Weil explicit formula. The Möbius factorization, log-derivative defect and the exact original-source `b_h(6)` sign certificate in [DIRICHLET_PRIME_DEFECT.md](DIRICHLET_PRIME_DEFECT.md) are paper-level deductions with standalone finite rational tests. **RH, π base-16 normality, original-zero odd-eight decay, and analytic continuation of the BBP-twisted Dirichlet series remain OPEN.** Neither a spectral sampling identity nor Weil positivity alone gives signed cancellation.

## Research results

1. **Prime visibility threshold.** A sufficiently narrow logarithmic wavepacket supported on one half-open index epoch `[A,2A)` has *zero direct nonarchimedean prime-power term* in the completed Weil formula. This is a rigorous support mismatch, not an unverified heuristic. Seeing both `×2` and `×3` in a complete commuting diamond `{m,2m,3m,6m}` requires index spread at least 6, rather than one dyadic octave.
2. **Source-sensitive completed Weil identity.** Encode original-zero phases `a_h(n)=exp(2πih·16^(n-1)π)` as amplitudes `b_h(n)=a_h(n)/n`. Under RH, Weil's spectral side becomes `Σ_γ |φ̂(γ)|² |Σ_(n∈I)a_h(n)n^(-1+iγ)|²`; without RH retain the original zero sum with correct holomorphic Mellin evaluation. On the prime side, for sufficiently narrow bumps, the exact term is a signed sum over *only* prime-power dilation edges `n=q m`, weighted by `Λ(q)/√q`. Polar/Γ terms are retained exactly via Bombieri's formula, not discarded.
3. **First 2×3 diamond and composite firewall.** For `I={m,2m,3m,6m}` only primitive `q=2,3` contribute: the direct `q=6` edge does not, because `Λ(6)=0`. The oriented four-cycle product of vertex phase ratios is exactly 1 for all seeds (pure gauge); the *oriented edges* and the Möbius mixed difference are nevertheless seed-sensitive.
4. **Exact, genuine-BBP phase discriminator.** A 12-term rational prefix of the immutable four-pole source, with its strict rational remainder, certifies two **positive** and two **negative** prime-edge cosines on `{1,2,3,6}` at `h=1`. It also proves `Im[(μ*a_h)(6)]<1−√3<0`. The coherent wrong seed has each edge cosine +1 and `(μ*a)(6)=0`. No π digit or zeta-zero oracle enters the certificate.
5. **Exact prime-jet transport differential equation.** For `Re s>1`, the BBP-twisted Dirichlet series `D_h(s)` obeys `D_h=ζG_h` with `G_h=Σ(μ*a_h)(n)n^(-s)` and `G_h'(s)=−E_h(s)/ζ(s)`, where `E_h(n)=Σ_{p^k|n}(log p)[a_h(n)−a_h(n/p^k)]`. The missing continuation/cancellation is isolated in an explicit non-Euler, source-selected defect, not furnished by RH.

## Why this matters, and what it does not solve

The selected **signed Basel tail** on finite `I` is a plain-log-carrier vacuum overlap:

`Σ_(n∈I) a_h(n)/n² = ||φ||_2^(-2) ⟨g_h,g_0⟩`, for disjoint translated bumps and the convention `⟨g_h,g_0⟩=∫g_h conjugate(g_0)`.

The completed Weil Gram is a **different quadratic form**. RH supplies its nonnegativity, but not the required asymptotic decay of this overlap. When the source is replaced by the coherent wrong seed, `g_h=g_0` and there is no cancellation even though every unphased Basel/Weil structure persists.

**Proof debt:** construct a source-preserving estimate that transfers the completed prime-power plus Γ/pole spectral information to *off-diagonal vacuum overlap suppression*, controlling the full old-prime CRT/winding/real-tail complement for the literal zero seed. A generic positive Gram comparison fails on the coherent seed.

## Reproduction

```sh
cd research/2026-11-10/basel_crt_omega_phasebridge/prime_archimedean
python -W error -m unittest -v test_prime_weil_probe.py
```

The test suite uses only stdlib exact `Fraction` arithmetic, independent of the large SUCC test environment. There is no imported π-digit table, zero list, quantum hardware simulation, unverified floating proof certificate, or long full-suite run. See [VALIDATION.md](VALIDATION.md) and [CLAIM_LEDGER.md](CLAIM_LEDGER.md).

**External source:** Enrico Bombieri, *The Riemann Hypothesis* (Clay Mathematics Institute), §5 explicit formula, https://www.math.ucdavis.edu/~tracy/courses/math205A/riemann.pdf ; Bombieri (2000), *Remarks on Weil's quadratic functional in the theory of prime numbers, I*, https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0 . Classical Dirichlet convolution/Möbius inversion: NIST DLMF §27.5 https://dlmf.nist.gov/27.5 . Repo sources: `docs/PI_NORMALITY_FRONTIER.md`, `research/2026-11-10/omega_bbp_operational_completion/intrinsic_carrier/PROOFS.md`, #585 `SIGNED_BASEL_TAUBERIAN.md` and `RH_SPECTRAL_INTERFEROMETRY.md`.
