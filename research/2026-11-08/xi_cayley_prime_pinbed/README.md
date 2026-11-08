# The critical circle as a learning observer: Euler source, prime roots, gamma and the global log obstruction

This exploratory SUCC research round implements the user's intuition about an infinite-degree root-of-unity polynomial whose critical vertical line is bent into a circle. The **honest** result is a source-constrained geometry and a sharp **counterexample** to the tempting infinite-product zero-confinement inference.

- [PROOFS.md](PROOFS.md): all CXP-01…CXP-08 proofs, exact Euler horodisks, source log, Jensen zero-count, Mertens gamma boundary, Li response and fake controls.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md): scopes, statuses, explicit blockers.
- [VALIDATION.md](VALIDATION.md): executed exact tests, numerical diagnostics, unrun integration gates.
- [NEXT.md](NEXT.md): concrete route to source-faithful Jensen/log transport.
- [`observational_succ/xi_cayley_prime_pinbed.py`](../../../observational_succ/xi_cayley_prime_pinbed.py): rational geometry and source-typed Euler/Jensen instruments; no actual zeta zeros used as inputs.
- [`tests/test_xi_cayley_prime_pinbed.py`](../../../tests/test_xi_cayley_prime_pinbed.py): original-source numerical controls, exact fabricated critical/offcritical models, winding and prime cutoff tests.
- [`handoffs/rh/2026-11-08-cayley-prime-horodisk-jensen.md`](../../../handoffs/rh/2026-11-08-cayley-prime-horodisk-jensen.md): review candidate for independent RH program, not direct RH repo modification.

**All ordinary Euler factors unchanged.** A half-density shifted factor is used only as an adversarial calibration. Classical Mertens shows the shifted infinite Euler product acquires a *zero inside the critical circle*, even though **each finite product has only critical-circle zeros**. Euler–Mascheroni enters as the exact renormalized cutoff. No RH proof is claimed. The new observation theorem is a reformulation: zero-free continuation of the actual original-source logarithm across the whole disk is RH-equivalent.
