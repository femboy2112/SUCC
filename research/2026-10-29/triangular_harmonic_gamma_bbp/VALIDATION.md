# Triangular harmonic–Gamma–BBP source: local execution and receipt

**Date:** 2026-10-29. **Parent:** SUCC draft PR #367 at `b6a3815ceb505de0b1f570eae3ff5be75cdbe99c` (source files read, not changed). **Execution:** local standalone Python; no main edits, no Lean kernel, no full SUCC test suite, no hosted CI.

Command run:

```sh
python /mnt/data/succ_triangle_rank/triangle_rank_probe.py
```

**Observed result:** 14/14 Python `unittest` methods passed (1.873 seconds) with exact rational `Fraction` arithmetic for source identities and algebraic controls; `mpmath` high-precision integrations are *labelled numerical observations* and do not establish infinite universal claims. Tests include original four-pole rational function vs factorization, exact four-pole source forcing and Green intervals, normalized source and convolution composition, mean squeeze, original-jet mutant, golden/base-16 norm noncollision, affine seed shift, phase-loop gauge identity, rank-two Frullani log agreement, rank 2/3/4 finite error bounds, first-order holdouts, strict rank monotonicity, and Oily fixed-point identity.

Source SHA-256 and raw local receipt SHA-256:

- `TRIANGULAR_HARMONIC_GAMMA_BBP.md`: `667c1768cbbea52b497566c84046ee35952c7cd7c769f0517ccefb01d5e571c0`
- `triangle_rank_probe.py`: `cbd23f6fcaf22b28bda170c6ba51c94e21267738ccde2481670ae35e862b9960`
- `probe_output.txt`: `ee22b45b2832acf9ac1dcdf027d1d0f87bf9a6e2e23fcc48947480418fa3602f`

Git blob identities of the two authored files for verification after publication:

- Dossier `0271e48b0f46cfb7354ad9f1de34371844d1ff82`
- Probe `79ef4fb218264f4a343e26d25e88930f456f0a58`

**Critical status:** mathematical proofs in the dossier are paper-level and have not been independently refereed or Lean-checked. The code does not demonstrate a source-derived physical field update or prove signed `o(N)` Weyl cancellation. The gamma rank first-order coefficient is checked numerically at several values, not inferred solely from those tests. Original source, seed, and historical proofs remain frozen.

## Raw test output

```
test_all_rank_one_sided_bound_numerical ... ok
test_clocks_algebraically_incommensurate ... ok
test_convolution_rank_semigroup ... ok
test_field_recursive_update ... ok
test_first_correction_numerical_holdout ... ok
test_four_poles_and_quadratic_factorization ... ok
test_initial_forcing_and_green_tail ... ok
test_rank_boundary_numeric_exact_fixedpoint ... ok
test_rank_log2_frullani_numerical_holdout ... ok
test_rank_monotonicity_numerical ... ok
test_seed_affine_anchor_and_zero_seed_control ... ok
test_source_gauge_cycles_exact_exponents ... ok
test_source_mean_and_bounds ... ok
test_source_mutant_same_local_jets ... ok

Ran 14 tests in 1.873s

OK
```

The abbreviated raw output here omits module/class prefix. The full local `probe_output.txt` is also available beside the exact generated artifacts in the analysis container. Verify exact-head execution of the GitHub-published files before elevating any execution status.
