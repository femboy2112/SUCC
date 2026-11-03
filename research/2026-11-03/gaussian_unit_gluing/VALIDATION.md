# Validation, source limits, and reproducibility

**Actual staged execution (2026-11-03).** The local container has the conversation's source URL and a standalone Gaussian-unit research staging directory, but not a complete SUCC git checkout. Attempted `git ls-remote https://github.com/femboy2112/SUCC.git HEAD` returned `Could not resolve host: github.com` with exit status 128. This is an ACCESS failure, not a mathematical failure. The GitHub connector has read/write access for a reviewable additive draft PR.

- Original source, provenance and existing quadratic-atom construction were directly read from the live connected repository: main `observational_succ/bbp_quadratic_atoms.py`, `research/2026-10-26/BBP_TWO_QUADRATIC_ATOMS.md`, main `AGENTS.md`, `docs/METHOD.md`, and existing Yoneda/observability architecture.
- Exact pure-Fraction algebra oracle independently constructs the quotient `Q[u]/m`, its trace through multiplication matrices, unique readout w, Frobenius Gram, central involution, idempotents, Gaussian complex structure, Q(sqrt2)-extended order-eight generator, all 8 impulse coefficients and both spectral channels.
- Second **implementation-distinct**, but **not blind reviewer independent**, SymPy oracle checks the rational factorization, partial transfer fractions, source polynomial identity, 4x4 Hankel determinant 4, projector algebra, trace handle, original indexed rational forcing resultant/discriminant and local n=0 residues, channel integrals and positive epsilon mutation integrated shift.
- Original zero-seeded rational recurrence reconstructed from original four poles and source Mellin moments. Exact source channel gluing `U_H+U_G=U` on explicitly executed finite windows; no pi digits required.
- `18/18` isolated staged `python -m unittest discover ...` tests PASS; Python `compileall` PASS, zero skips; `generate_receipt.py --verify` PASS after generating the receipt.
- Fresh (same-reasoner, **not blinded**) preregistered four holdouts `n=307,509,769,1021`: all source addition, odd denominator, and v2-sector pole depth comparisons PASS. Raw integer numerator/denominator and SHA256 of tested modules retained in EXACT_RECEIPT.json. These finite checks do not establish the universal paper theorem by themselves.

**NOT RUN/CLAIMED:** full native SUCC >11k test suite, provenance/observer/ordinal native probes, source-aware hidden build CI at exact child head, Lean proof kernel compilation, external mathematical referee or all-horizon selected real Weyl bound. Existing parent CI results are NOT child test receipts. Check hosted PR actions separately after creating PR; report queued/running states literally.

## Local reproduction

```
python -m unittest discover -s tests -p 'test_gaussian_unit_gluing*.py' -v
python -m compileall -q research/2026-11-03/gaussian_unit_gluing
python research/2026-11-03/gaussian_unit_gluing/symbolic_oracle.py
python research/2026-11-03/gaussian_unit_gluing/generate_receipt.py --verify
```

On a complete checkout, perform AGENTS.md required `verify_provenance`, native test suite, `observer_foundations_probe`, and `ordinal_succ_report_probe` with the environment correctly set, and inspect exact-head GitHub Actions. No main or production modifications authorized.

**Claim firewall:** exact linear-algebraic/categorical source reconstruction and 2-adic gluing DESCRIBE original forcing; no selected real phase cancellation or base-16 normality has been proved.
