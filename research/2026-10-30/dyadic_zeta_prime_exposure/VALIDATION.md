# Validation and reproduction — scoped exact run

**2026-10-30.** The uploaded probe is stdlib-only Python and performs exact Fraction/integer arithmetic. It uses two distinct finite algorithms for continued negative-integer values: the Stirling recurrence plus dyadic eta identity, and the Bernoulli binomial recurrence. These algorithms were written and checked in the same session; they are **not** blind witnesses.

Command:

~~~sh
python research/2026-10-30/dyadic_zeta_prime_exposure/dyadic_zeta_prime_probe.py
~~~

Observed local output:

~~~text
test_cycle_dyadic_basel_bridge ... ok
test_exact_special_values ... ok
test_exposure_is_not_survival ... ok
test_finite_circle_green_traces ... ok
test_finite_dyadic_cauchy_in_reals ... ok
test_geometric_series_boundary_scope ... ok
test_independent_bernoulli_triangle ... ok
test_integer_stirling_numerator_dyadic_eta ... ok
test_not_p_adically_cauchy ... ok
test_odd_denominator_divides_power_of_two_minus_one ... ok
test_prime_first_appearance ... ok
----------------------------------------------------------------------
Ran 11 tests in 0.024s
OK
~~~

**Exact coverage:** m=1..50; odd primes through 43; valuation checks at p=2,3,5,7; pseudoinverse and its square computed by independent rational Gaussian elimination for N=3..10; two explicit prime cancellation counterexamples (17,31); finite geometric/dyadic identities.

**GitHub artifact verification:** the uploaded dyadic_zeta_prime_probe.py Git blob SHA was re-fetched and exactly matched the pre-upload local Git blob SHA: 20418fe17dc48e2cb00cae486fd3d4d7d17b6b3b. This verifies file identity, not remote execution.

**Additional independent denominator-survival probe:** denominator_survival_probe.py was run locally; 3/3 unittest methods PASS (0.031s). It checks the full p^(1+v_p(m)) denominator product and the p-adic Stirling-numerator cancellation law for every even m=2..100, and the first-prime appearances through 101. Its uploaded Git blob SHA was re-fetched and matched the pre-upload local Git SHA: 8581f6df80fcabdff5999ebefa3bbbf6475c6578. Combined focused total: **14/14 test methods across two files**. These do not constitute a full-SUCC-suite result.

**Not run or claimed here:** the full native SUCC ~10k tests, provenance verification, both main foundation probes, hosted CI, a Lean proof, or a blind independent referee. The finite tests calibrate the implementation; all-order mathematics depends on the explicit derivations and cited classical input. No run of pi-digit signed Weyl cancellation or RH is claimed.
