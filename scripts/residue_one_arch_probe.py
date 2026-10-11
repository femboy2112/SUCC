#!/usr/bin/env python3
"""Typed exact receipt for residue-one Euler factors and finite/Arch limits.

All computed values are rational. The compact-group theorem, the existence
of weight-two p-adic zeta analytic branches and Tate's global Gamma factor
are externally sourced mathematics, not numerically proved here.
"""
import json
from observational_succ.residue_one_arch import demo


def main():
    x=demo()
    assert x["status"]=="PRIME_RESIDUE_ONE_ADELIC_LOCAL_GLOBAL_OBSTRUCTION"
    assert x["euler_geometric_series_converges_p_adically"] is True
    assert x["all_euler_factors_are_residue_one_units"] is True
    assert x["finite_local_euler_norms_all_one"] is True
    assert x["same_residue_has_nonunique_local_units"] is True
    assert x["factorial_one_limit_each_p_adic"]=="1"
    assert x["factorial_one_limit_real"]=="+infinity"
    assert x["factorial_one_not_always_prime"] is True
    assert x["diagonal_minus_one_twelfth_product_formula"]["finite_abs_product"]=="12"
    assert x["diagonal_minus_one_twelfth_product_formula"]["norm"]=="1"
    assert x["nondiagonal_idelic_example"][0]["norm_one"] is True
    assert x["nondiagonal_idelic_example"][2]["idele_norm"]=="1/12"
    assert x["nondiagonal_idelic_example"][2]["norm_one"] is False
    assert x["positive_real_scale_determined_by_residue_one_alone"] is False
    assert x["compact_to_positive_real_continuous_group_hom_trivial"] is True
    assert x["topological_group_theorem_tested_by_finite_sampling"] is False
    assert x["weight_two_Kubota_Leopoldt_branch_interpolation"][1]["weight_residue"]==2
    assert all(i["global_special_value"]=="-1/12"
               for i in x["weight_two_Kubota_Leopoldt_branch_interpolation"])
    assert x["interpolation_theorem_imported"] is True
    assert x["p_adic_zeta_function_constructed"] is False
    assert x["Tate_arch_completion_constructed"] is False
    assert x["RH_claimed"] is False
    print(json.dumps(x,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
