"""Field-relative observational_succ research engine (bounded, exact, no RH claims)."""
from .core import (ActualizationError, AffineChart, BasisLift, BudgetExceeded,
                   DomainError, Execution, Frame, IncompleteObservation,
                   Operation, Scalar, ZERO, ONE, I, execute)
from .arithmetic import (Limits, ShadowIndex, clock_contract, conditional_mean,
                         conductor_growth, connected_audit, factorization,
                         mixed_probe, source_at, structure_birth)
from .engine import Engine, LossyHistoryError, run_arithmetic
from .yoneda import (Arrow, DivisibilityCategory, PathCategory, ValuationCategory,
                     FiniteFunctor, CompanionBridge, valuation_bridge,
                     forget_path_bridge, restricted_yoneda, validate_yoneda,
                     co_yoneda_companion, verify_companion_actions)
from .resource_probe import (ValuationWord, ProbeBudget, compare_observers,
                             execute_probe, lcm_word, budget_demo)
from .phenomenology import Phenomenology
from .local_global import compare_local_global, prefix_demo
from .circle_transport import (FiniteClock, FiniteDualRefinement, CyclicOneObjectCategory,
                               conductor_birth_2_to_6, verify_refinement_tower)

from .infinite_realization import (LCMIndRealization, RationalEnclosure,
                                   e_enclosure, pi_enclosure, zeta_euler_enclosure,
                                   escaping_defect_form, escaping_defect_limit,
                                   pinned_negative_form)

from .gamma_succ_path import (
    FactorialSuccPath, MomentChannel, PrimeMomentPath, PathDomainError,
    gamma_periodic_gauge, gamma_periodic_log_curvature,
)

from .succ_shadow_window import (
    ShadowWindowCertificate, WindingHistory, WindowError,
    WindowResourceExhausted, sine_gauge_witness, seam_gauge_witness,
    periodic_quarter_probe, same_cell_quadratic_gauge_curvature,
    observed_window, unseen_within_prefix, certified_window_penalty_lower_bound,
    quadratic_weight_gluing_defect,
)

from .lambert_succ import (
    LambertPathError, FactorialInverseCertificate,
    principal_bulk_inverse, bulk_branches, invert_factorial_mass,
    gamma_bulk_defect, gamma_defect_succ,
    rooted_tree_coefficients, rooted_tree_succ_ratio,
    tree_functional_residual, rooted_tree_count, leaf_only_extension_count,
    tree_series_vs_lambert,
)

from .dirichlet_lambert import (
    ArithmeticWError, DirichletLambertSnapshot, convolve, identity,
    star_lambert_w, star_log_unit, star_exp,
)

from .hasse_theta_seam import (
    SeamError, SUCCDifferenceSource, eta_prime_trivial,
    eta_jet_trivial, gamma_pole_prime_bridge,
    gamma_subtracted_prime_current, prime_current_tail_enclosure,
    theta_xi_partial, theta_xi_tail_bound,
    raw_completed_finite_mutation, finite_mutation_parity_error,
    symmetric_offline_quartet_counterexample,
    riemann_siegel_leading, hardy_z_calibration,
    prime_source_moment_energy, prime_current_finite_differences,
)

from .balanced_theta_li import (
    BalancedWindowError, theta_finite, theta_defect,
    theta_defect_tail_envelope, matched_theta_cutoff,
    one_prime_fake_defect, wrong_half_density_limit,
    finite_gamma_window, finite_gamma_succ_defect,
    truncated_xi, finite_li_coefficients, li_all_degree_bound,
    finite_double_zero, li_coevolving_diagonal,
)

from .observer_logic import (
    LogicBoundaryError, Term as LogicTerm, Formula as LogicFormula,
    Var as LogicVar, Num as LogicNumeral, Pred as LogicPredicate,
    godel_code, decode_godel, diagonal_syntax,
    Theory as LogicTheory, ProofStep, FiniteProof,
    check_finite_proof, encode_proof, verifies_proof_code,
)
from .observer_reflection import (
    ReflectionBoundaryError, IncreasingTheoryChain,
    external_consistency_step, UnnamedElementOmegaCountermodel,
    RationalInterval, GramCertificate, rational_gram_certificate,
    exact_quartic_screw, exact_quadratic_screw, bounded_gram_search,
)

from .source_prime_certificates import (
    SourceCertificateError, rational_log_ratio,
    rational_log_integer, rational_inverse_sqrt,
    finite_prime_horizon, CertifiedPrimeSource, prime_delta_at_fake_six,
)

__version__ = "0.3.0"
