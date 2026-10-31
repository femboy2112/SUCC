# Raw test execution receipts — Basel × line-circle observer

## Primary stdlib 16/16

Command: python /mnt/data/succ_basel_circle_20261030/basel_cycle_probe.py

    test_all_edge_native_trace_exact_and_bound ... ok
    test_distributed_original_versus_mutant_first_jet ... ok
    test_exact_resistance_first_jet_and_cycle_response ... ok
    test_exact_source_excess_and_harmonic_tail ... ok
    test_green_and_finite_basel ... ok
    test_grid_to_continuum_bernoulli_defect ... ok
    test_physically_scaled_weak_seam_limit ... ok
    test_pi_twist_determinant_and_source_product ... ok
    test_resistance_line_circle_closure_defect ... ok
    test_single_source_bond_rank_one_identity ... ok
    test_source_resistance_renormalization_tail_bound ... ok
    test_source_sign_does_not_select_seed ... ok
    test_tiny_source_weight_is_positive_and_below_one ... ok
    test_twisted_determinant_does_not_see_edge_order ... ok
    test_unweighted_and_single_bond_pseudodeterminant ... ok
    test_weak_seam_open_path_trace ... ok

    Ran 16 tests in 0.243s
    OK

## Independent symbolic / high-precision oracle

Command: python /mnt/data/succ_basel_circle_20261030/basel_cycle_independent_oracle.py

    ORACLE: authentic source factorization and first-jet matched mutant PASS
    ORACLE: original source single-edge limit 59/1440, mutant 1/32 PASS
    ORACLE: arbitrary-weight twisted determinant N=3..7 PASS
    ORACLE: exact all-edge resistance harmonic/digamma partial fractions PASS
    ORACLE: Gamma product C_w = 0.200550308149309758095152543431427471990243
    ORACLE: digamma resistance renormalization C_res = 3.96605502759545301329845542169650637575632
    ORACLE: Basel-Gamma/Oily and twisted determinant exact formulas PASS
    ORACLE: rigorous rational interval proves Oily !=59/1440; Oily in [ 0.04081790768118264 , 0.04081840718168714 ]
    Independent oracle PASS

## Additional source/analytic calculations

Symbolic original source:
    R(a)=(15a²+121a+240)/[a(a+3)(a+4)(a+5)]
    w(a)=a(15a²+121a+240)/[15(a+3)(a+4)(a+5)]
    single-edge native Δ_N=59/1440 + 6031/(172800N) - 641341/(20736000N²) + O(N^-3)
    mutant Δ_N=1/32 + 7/(256N)-39/(2048N²)+O(N^-3)

Original ALL-edge finite trace numeric calibration:
    N=10: ΔTr=3.38361491208, first two asymptotic terms=4.24846613749
    N=100: ΔTr=50.0584377745, prediction=51.9188641864
    N=1000: ΔTr=610.587001899, prediction=613.530669980
    N=10000: ΔTr=7074.54935498, prediction=7078.72698096
    N=100000: ΔTr=80215.8609334, prediction=80221.4726212

The asymptotic error bound is an algebraic theorem, not derived from the displayed finite numeric data.

## Disclosed initial failure and corrected probe

The first independent SymPy oracle failed while trying to construct Rational(59,120*n) with symbolic n. It was repaired to Rational(59,120)/n. All independent checks then passed. Primary test was tightened to remove a vacuous source-weight self-equality and to avoid selecting the source mutant according to an ambiguous computed weights-list equality. The final 16/16 includes a new edge-order counterexample.

**Not run:** complete root provenance/10k+ suite/observer/ordinal probes, exact new-head hosted CI, Lean, blind peer review. Source-only finite response does not establish actual π digit normality or RH.
