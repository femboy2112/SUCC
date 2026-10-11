#!/usr/bin/env python3
"""Exact SUCC clock / Mahler interpolation / Kummer congruence receipt.

Classical imported mathematical ingredients: Euler's theorem, Mahler's
continuous-function representation, and Kummer's all-weights congruences.
The finite code does not construct Kubota-Leopoldt measures or RH.
"""
import json

from observational_succ.clock_mahler_interpolation import clock_mahler_demo


def main():
    x=clock_mahler_demo()
    assert x["status"]=="SUCC_CLOCK_MAHLER_KUMMER_COMPATIBILITY"
    assert x["p_five_clock_mod_25_period"]==20
    assert x["p_five_SUCC_jet_gap_at_level_one"]==20
    assert x["unit_clock_period_equals_prime_jet_gap"] is True
    assert x["mahler_coefficient_formula"]=="Delta^r f_p(0)=(-p)^r"
    assert x["mahler_interpolated_minus_one"]=="1/(1-p)"
    assert x["mahler_p_five_local"]["continued_local_euler_factor"]=="-1/4"
    assert x["mahler_p_five_local"]["error_valuation"]==4
    assert x["kummer_p_five_weights"]["weights"]==[2,22] or x["kummer_p_five_weights"]["weights"]==(2,22)
    assert x["kummer_p_five_weights"]["corrected_zeta_residues"] in ([17,17],(17,17))
    assert x["kummer_p_five_weights"]["raw_zeta_residues"] in ([2,17],(2,17))
    assert x["wrong_unremoved_Euler_factor_breaks_clock_congruence"] is True
    assert x["torsion_clock_mod_three_requires_branch"]["continuous_integer_power_sequence_over_Zp"] is False
    assert x["parity_clock_mod_two_is_continuous"]["continuous_integer_power_sequence_over_Zp"] is True
    assert x["clock_algebra_generates_a_p_adic_zeta_measure_without_extra_proofs"] is False
    assert x["classical_Mahler_and_Kummer_theorems_imported"] is True
    assert x["nontrivial_zeta_zeros_used"] is False
    assert x["RH_claimed"] is False
    print(json.dumps(x,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
