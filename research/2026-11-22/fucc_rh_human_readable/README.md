# FUCC → Arithmetic multiplicity → Human-readable RH: first proof packet

**Research-only; source-typed; no RH-proof promotion.** Created 2026-11-22 on a stacked SUCC branch; original source, main branch, archived imports and formal/production implementations remain unchanged.

## What is completed

- Exact original-FUCC log-commutator representation of the very Riesz–Chebyshev statistic used by the verified Alpöge–Claude RH proof.
- Full elementary Mellin calculation showing why the corrected weighted sum sees zeta zeros and why the `(1+gamma)x` counterterm is required.
- A **constructive FUCC prime-square/Mahler resolvent** producing exactly the height-two formal logarithm used in the local model; its p-adic denominators and selected weighting are explicitly accounted for.
- A **self-contained** height-two formal-power-series p-adic derivative-valuation lemma reproducing the correct arithmetic-multiplicity *shape* (with original theta-integrality not assumed).
- Elementary global integer-minor capacity theorem and a decisive no-go: bare FUCC support growth does not imply p-adic divisibility of coefficients.
- A specific theorem-by-theorem contract for the **human-readable version of the hard inequality (M)**, with all missing inputs kept visible.

## Reading order

1. [LEARNERS_DICTIONARY.md](LEARNERS_DICTIONARY.md) — SUCC language ↔ formal mathematics, including limitations.
2. [HUMAN_READABLE_PROOF_SPINE.md](HUMAN_READABLE_PROOF_SPINE.md) — narrative derivation and the RH proof's conditional top-level architecture.
3. [FUCC_MAHLER_RESOLVENT.md](FUCC_MAHLER_RESOLVENT.md) — exact FUCC construction of the height-two logarithm; crucial source-weighting caveat.
4. [TECHNICAL_PROOFS.md](TECHNICAL_PROOFS.md) — detailed derivations of local model and FUCC/Riesz identity.
5. [MAIN_INEQUALITY_CONTRACT.md](MAIN_INEQUALITY_CONTRACT.md) — true arithmetic bottleneck (M), exact external status and next proof obligations.
6. [SOURCE_MAP.md](SOURCE_MAP.md) — public and SUCC/FuckingRH provenance.
7. [CLAIM_LEDGER.md](CLAIM_LEDGER.md), [NEXT.md](NEXT.md), [VALIDATION.md](VALIDATION.md).

## Reproduce focused computational checks

```bash
python -m unittest -v test_fucc_rh_bridge.py
python independent_audit.py
python -m compileall -q fucc_rh_bridge.py test_fucc_rh_bridge.py independent_audit.py
```

No proof in this directory establishes the full inequality (M); those ingredients are in the externally verified Lean proof but have not yet been translated into a complete conventional argument or derived independently by SUCC. **This is a first verified segment of an honest human-readable proof reconstruction, not a full proof.**
