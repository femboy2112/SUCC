# Full prime-two inverse certificates (R2S)

The [paper](../research/2026-10-18/ROUND2_SIGNED_PRIME_RESOLVENT.md) audits
the original Suzuki source on the primitive K-Hilbert carrier and proves a
whole-residual non-scalar inverse bound. Its [capsules](../research/2026-10-18/ROUND2_SIGNED_CAPSULES.json)
use the existing `source_proof_certificate.audit_capsules` authority schema.

| Claim | Domain and conclusion | Authority |
|---|---|---|
| R2S-SOURCE | Original first-prime signed source equals the closed primitive Fourier-Gamma/contact/prime/pole form on its declared domain. | PAPER_PROVED |
| R2S-HIGH | On each fixed primitive parity high space, the complete source dominates its parity-specific kappa plus exact prime mismatch. | PAPER_PROVED; independent exact implementation check |
| R2S-INVERSE | Complete residual errors are bounded in the non-scalar inverse norm after evaluating the entire nominal continuum Gram. | PAPER_PROVED |
| R2S-STRICT | Fixed J8/M80 and J24/M192 clamped trials give strictly positive definite gains in both original signed Schur lower blocks. | EXACT_FINITE_CHECK |
| R2S-SIGN | The true original first-window Schur form is positive semidefinite. | UNVERIFIED; both computed lower blocks remain negative definite |

All universal quantifiers, domains, source hashes, dependencies, hypotheses,
prior art, mutation controls and remaining experiments are retained in the
paper and capsules. Hash validation issues no mathematical authority. This
stream supplies no Lean proof and makes no novelty claim for the classical
Bessel, variational or Young mechanisms. **RH PROVED: NO.**

Replay capsule integrity with:

```sh
python scripts/full_prime_resolvent_probe.py --audit-capsules
```
