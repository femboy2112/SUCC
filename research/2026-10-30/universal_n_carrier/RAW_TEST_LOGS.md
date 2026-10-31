# Raw validation excerpts — Operation Universal N, 2026-10-30

All finite checks ran locally on isolated Python 3.13 with SymPy/mpmath installed. Exact finite source/mutant rational operations and independently derived analytical formulas; no digit-normality proof.

## Main symbolic/finite probe
Command: python /mnt/data/succ_universal_bridge/bridge_probe.py

    test_bbpgamma_digamma_source_integral ... ok
    test_finite_n_zeta_spine_exact ... ok
    test_finite_pascal_cannot_choose_hypothesis ... ok
    test_first_jet_matched_positive_mutant_different_prime_clock ... ok
    test_gamma_large_rate_source ... ok
    test_gamma_pascal_exact ... ok
    test_gamma_quotient_finite_product ... ok
    test_golden_locus_from_gamma_pascal_observer ... ok
    test_kummer_and_all_places ... ok
    test_original_2adic_prime_balance ... ok
    test_pascal_fibonacci ... ok
    test_pisot_is_not_automatic ... ok
    test_regulator_must_be_declared ... ok
    test_seed_twist_invisible_to_potential_value ... ok
    test_source_rational_identity_and_log_derivative ... ok
    test_weighted_multiplicative_carrier_recovers_selected_BBP ... ok
    test_zeta_functional_equation_negative_one ... ok

    Ran 17 tests in 7.038s
    OK

## General measure-valued Pascal naturality
Command: python /mnt/data/succ_universal_bridge/natural_triangle_probe.py

    test_complete_diagonal_extrusion_word_not_aggregated ... ok
    test_count_out_quotient_does_not_make_all_words_equal ... ok
    test_exact_source_agnostic_pascal_update ... ok
    test_order_sensitive_extra_law_breaks_grade_sufficiency ... ok
    test_pgf_sum_and_partition ... ok
    test_source_mutation_invisible_to_unweighted_pascal_counts ... ok

    Ran 6 tests in 0.070s
    OK

## Compact pure-stdlib counterpart
Command: python /mnt/data/succ_universal_bridge/universal_n_probe.py

    test_all_prime_pascal_kummer_product ... ok
    test_finite_dirichlet_cross_sections ... ok
    test_finite_gamma_product_exact_numerical_holdout ... ok
    test_gamma_potential_power_and_golden_fixed_point ... ok
    test_original_source_four_pole_fingerprint ... ok
    test_original_v2_slope_and_all_places ... ok
    test_pascal_gamma_and_fibonacci_counting ... ok
    test_pisot_not_universal_for_colored_recursions ... ok
    test_same_rank_positive_mutant_has_different_prime_place ... ok
    test_seed_twist_has_same_potential_values_and_prime_signature ... ok
    test_source_shift_is_not_seed_specific ... ok
    test_universal_measure_word_extrusion ... ok
    test_weighted_rational_carrier_generates_original_zero_seed ... ok

    Ran 13 tests in 0.387s
    OK

The committed 13-test counterpart was separately authored; same-case local pass does not by itself establish byte-identical GitHub execution. The remote Git blob is preserved in the PR. An independent clone can rerun it.

## Independent high precision oracle
Command: python /mnt/data/succ_universal_bridge/independent_oracle.py

    ORACLE: exact log-derivative, original R(a), Q derivatives 15/-59/243 verified
    ORACLE: independent Laplace integral versus four rational poles five holdouts PASS
    ORACLE: exact rational P_N vs independent gamma ratio, all-primes balance and v2=-5N PASS
    N 100 normalized gamma ratio / C0 1.0024207825886480930751384 relative error 0.00242078258865
    N 1000 normalized gamma ratio / C0 1.0002421767670664182537353 relative error 0.000242176767066
    N 10000 normalized gamma ratio / C0 1.0000242186428620352440822 relative error 2.4218642862e-5
    ORACLE: C0 = 0.001714158314683720171042099538894356197989386481973209
    ORACLE: sum original forcing = 3.386047619597191721936418831438412860226918352182048
    ORACLE: original Gamma-Green constant = 0.01629699773382656556491836321059399840198326352046283
    ORACLE: Hurwitz zeta derivative at zero reproduces BBP Gamma-product constant
    ORACLE: zeta(-1) exactly -0.0833333333333333333333333333333 ; prime partial zeta2 relerr 2.70604439148e-5
    ORACLE: Gamma-Poisson mixture = exact Pascal binomial coefficients for ranks 2,3,4
    ORACLE: positive rank-two mutant has distinct exact p=2 slope -10N vs original -5N
    INDEPENDENT ORACLE PASS

## Initial failed probes and repairs
- Initial 10-test source version failed symbolic binomial series because SymPy preserved the |z|<1 domain branch; repaired with fixed coefficient proof.
- Symbolic prime logs required simplification (2 log2 versus log4).
- SymPy Boolean root types could not be summed as Python integers; repaired numeric predicate.
- Initial nonexchangeable counterexample accidentally gave equal path weights. Replaced with (1,0) mass 1/8 and (0,1) mass 1/4.
- Initial Hurwitz zeta numeric derivative missed ~1e-10 at rational shifts, and higher precision contour differentiation timed out. Repaired numerical oracle uses a 1e-8 numerical tolerance together with the official exact Lerch identity.
- A compact initial test compared a harmonic sum to itself; strengthened to the exact independent identity sum_(j<=N)H_j=(N+1)H_N-N before the final posted probe.

## Boundary
Full SUCC root provenance/10k+ unit suite, observer-foundations, ordinal probes, hosted exact-head CI, Lean, and outside peer review were NOT RUN. No selected signed all-horizon Weyl/occupancy saving, π normality, or RH is claimed.
