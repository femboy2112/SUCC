# Basel × 2/3 CRT × Ω–Haar × signed Weyl

**Research only — 2026-11-10.** Additive child of Main XXIII candidate #584 at `50481e49592af00d87c602f671a28f3503709de0`. No original BBP pole/seed/provenance/history, Lean, main or CI workflow edits.

## Mathematical deliverables

- [PROOFS.md](PROOFS.md): exact six-adic CRT cycle graph and Laplacian Green trace `(M²−1)/12`; commuting 2/3 refinements with `ζ(−1)` fixed point; Basel–Haar–Fourier–Γ identities; intrinsic `B₂/B₃` Gibbs trace with `L(2,χ₋₃)`; Archimedean height nonextension.
- [PHASE_OBSERVER.md](PHASE_OBSERVER.md): six translated signed Ω–Haar successor edges form an exact bulk partition of unity. Their phase-twisted directed trace reconstructs the original-seed Weyl mean for every integer epoch `A≥11`; the same trace with Basel Gibbs weights yields the weighted Weyl mean. An explicitly retained `n²` operator unweights it. This is an algebraic reconstruction, **not an asymptotic cancellation bound**.
- Hostile controls: fixed coherent wrong seed, finite rational wrong seed, missing shifted frame, lost integer winding/height, PPP-08 epoch-dependent rational shadow, positive Mellin mutants.

## Focused local validation

```sh
python -W error research/2026-11-10/basel_crt_omega_phasebridge/test_basel_omega.py
python -W error research/2026-11-10/basel_crt_omega_phasebridge/test_phase_weyl.py
```

Both files contain nine focused tests each (18 total), run locally with exact matrix/Fraction checks and a stated non-rigorous numerical smoke check. The full native ~13k suite, hosted CI, external review and Lean were not run for this research contribution. This branch must not be merged until its parent #584 is accepted and its independent gates pass.

**OPEN:** original zero-seed signed Weyl decay, base-16 normality of π, RH. Exact trace equivalence alone is not the missing decay estimate. Review alongside `docs/PI_NORMALITY_FRONTIER.md` and `AGENTS.md`.

## Signed Basel tail / Tauberian completion

New [SIGNED_BASEL_TAUBERIAN.md](SIGNED_BASEL_TAUBERIAN.md) proves for every bounded complex sequence the equivalence:

- ordinary dyadic epoch mean tends to zero;
- A times the signed reciprocal-square tail tends to zero;
- normalized signed reciprocal-square shell mean tends to zero.

An explicit inverse-Abel inequality bounds the epoch mean by 10 times the supremum of later weighted shell means. Applying this to the source-selected original-zero π orbit gives a precisely typed **normality-equivalent signed Ω–Basel trace criterion**, not a proof that its required o(1/A) cancellation holds. The fixed coherent bad seed has tail asymptotic 1/A and fails the gate.

Focused stdlib test: python -W error research/2026-11-10/basel_crt_omega_phasebridge/test_signed_basel_tauberian.py (8 tests run locally). No expensive full suite or hosted CI claimed.
