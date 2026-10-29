# Oily → Pólya → origin-locked prime observers (28 October 2026)

**Status:** research-only, exact paper derivations + locally executed tests. Source parent: SUCC draft PR #347 (`8345ce2854663b1c40924db5d4efe020bcad521c`), descended from #346/#344 and Main XIII. Original zero-seeded four-pole BBP forcing unchanged. No academic priority, physical hbar, RH, π-normality, or optimal physical observer claim.

## Read these in order

1. [Full source-typed dossier](OILY_ZETA_CAUSAL_GROWTH_AND_SOURCE_DEFECT.md): WCG-01..10, proofs, controls, provenance, exact signed-source coupling and a new exact BBP Dirichlet finite part.
2. [`observational_succ/oily_prime_growth_compiler.py`](../../observational_succ/oily_prime_growth_compiler.py): exact full-x Oily online birth/stopping kernel, critical Pólya law, zeta local stopping comparison, certified prime cutoff.
3. [`observational_succ/origin_fiber_arithmetic_observer.py`](../../observational_succ/origin_fiber_arithmetic_observer.py): exact source-indexed divisor-jump and SU2 finite structure, composition defect and source-phase commutator diagnostic.
4. [Independent symbolic oracle](../../scripts/oily_prime_growth_independent_oracle.py) and [original BBP finite-part oracle](../../scripts/bbp_dirichlet_finite_part_oracle.py), each replayable, with JSON receipts.
5. Exact [compiler tests](../../tests/test_oily_prime_growth_compiler.py), [arithmetic observer tests](../../tests/test_origin_fiber_arithmetic_observer.py) and [original-BBP bridge tests](../../tests/test_original_bbp_carry_origin_bridge.py).
6. [Codex Ultra autonomous handoff](../../handoffs/CODEX_ULTRA_ORIGIN_LOCKED_GROWTH_2026-10-28.md): maximum-effort independent reproof, rigorous next theorems and adversarial controls; intentionally asks for proof execution rather than another roadmap.

## Results in one paragraph

The authentic Oily conditional packet law has a unique causal nearest-neighbor split compiler under its explicit stage/stop assumptions. At the critical endpoint its transitions are a one/one Pólya urn and its stopping law produces precisely `(j+1)/2^(j+2)`. The same Pólya split compiler with *constant geometric stopping* realizes every prime-local source-preserving zeta mode; Oily is its size-biased stopping transform. Applying the Pólya stochastic kernel to coherent amplitudes instead loses norm, demonstrating the probability/quantum distinction. Prime-factor fibers have Schwinger SU2 representations, while first-factor additive successor compresses to divisor jumps rather than genuine SUCC and fails to preserve compositions by an exact 5/24 counterexample. This leads to a bona fide zero-seeded BBP cross-time commutator, but not yet a Weyl bound. Separately the authentic four-pole Dirichlet response has an exact pole at s=-1 and an exact finite part involving γ, π, log 2 and log(1+√2). All source-only/changed-seed/positive-energy gates remain open as stated.

## Local validation scope

Run `PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'` in a checkout with the new files, and `python scripts/oily_prime_growth_independent_oracle.py` and `python scripts/bbp_dirichlet_finite_part_oracle.py` (SymPy/mpmath required only for symbolic oracles). Full CI and Lean must be inspected separately; local tests/receipts do not stand in for hosted validation. Claim IDs WCG-01..10 are scoped **research-local** until reconciliation with the repository claim namespace registry; do not silently assign registered global FQIDs.
