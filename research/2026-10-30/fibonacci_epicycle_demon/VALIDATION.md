# Validation receipt — Operation Fibonacci Clock × Epicycle-Demon Observer
Date: 2026-10-30. Baseline Main XVI SHA: e18ba565ca540adb7edf3292f5593929e76d91c5.
Branch: research/fibonacci-epicycle-demon-normality-2026-10-30.
All files are additive under research/2026-10-30/fibonacci_epicycle_demon/.

## Executed locally (standalone stdlib Python)

Command:

    python epicycle_probe.py

Raw output:

    test_fibonacci_harmonic_offset (__main__.FibonacciClock.test_fibonacci_harmonic_offset) ... ok
    test_fibonacci_matrix (__main__.FibonacciClock.test_fibonacci_matrix) ... ok
    test_four_pole_rational_source (__main__.FibonacciClock.test_four_pole_rational_source) ... ok
    test_integral_lorentz_conjugacy (__main__.FibonacciClock.test_integral_lorentz_conjugacy) ... ok
    test_jeffreys_convergence_and_first_jet (__main__.FibonacciClock.test_jeffreys_convergence_and_first_jet) ... ok
    test_computable_sequence_has_arbitrarily_long_zero_runs (__main__.NormalObserver.test_computable_sequence_has_arbitrarily_long_zero_runs) ... ok
    test_debruijn_all_short_circular_blocks_uniform (__main__.NormalObserver.test_debruijn_all_short_circular_blocks_uniform) ... ok
    test_no_universal_finite_prefix_horizon (__main__.NormalObserver.test_no_universal_finite_prefix_horizon) ... ok
    test_wrong_iid_likelihood_exact_rate (__main__.NormalObserver.test_wrong_iid_likelihood_exact_rate) ... ok
    test_wrong_one_step_markov_likelihood (__main__.NormalObserver.test_wrong_one_step_markov_likelihood) ... ok

    ----------------------------------------------------------------------
    Ran 10 tests in 0.020s

    OK

The locally executed standalone source had Git blob SHA-1 fdbd938c770f568f3e3afbff317a489e90360437; the GitHub fetch of this new branch's epicycle_probe.py independently returned the **same exact SHA-1 and 6648-byte length**.

## What actually was checked

- Fraction-exact R(a) source, exact rational E_a[X] and monotonicity over integer a in 1..149; positivity of original four-pole carrier in these cases only (global positivity comes from analytic derivation).
- Fibonacci matrix powers and both isometry/anti-isometry laws over 625 exact integer vectors.
- Finite original-versus-fake Jeffreys divergence and first coefficient approach using Decimal with 65-digit internal precision.
- Finite Fibonacci harmonic offset diagnostic.
- Exact cyclic de Bruijn finite word counts for base 2, order 6 and base 4, order 4; such periodic controls are NOT normal sequences.
- Wrong iid/one-step Markov likelihood on those finite circular controls; biased prefix model and binary Champernowne zero-run examples.

**No finite calculation proves the infinite claims.** Their quantifiers and arguments are in RESEARCH.md. Local exact test and known literature are not independent mathematical referees.

## Not run, not claimed

Full SUCC provenance checker; full 9k+ unittest suite; observer foundations probe; ordinal probe; Lean; exact-head hosted GitHub CI; independent original-source audit; peer review; global selected signed π Weyl estimate. No change to archives, root provenance, source code, claim namespaces, or main.

**Next discriminating task:** A new original-four-pole, zero-seed-sensitive source-to-selected arithmetic occupancy or signed Weyl inequality, rejecting s*=-π/16 and higher-jet-matched fake while surviving all 16 carry modes and growing temporal windows.
