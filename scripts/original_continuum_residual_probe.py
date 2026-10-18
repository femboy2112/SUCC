"""Full ORIGINAL Suzuki signed primitive residual and K-relative Schur receipt.

No zeta zero positions, no finite-grid PSD substitution, no imaginary
source. The rational polynomial surrogates are bounded by rigorous Taylor
and frozen original source parameter-error intervals.
"""
import argparse
import json
from pathlib import Path
from fractions import Fraction as F
from observational_succ.original_continuum_residual import (
    SOURCE_SHA, frozen_operator_matrix_holdout,
    source_residual_schur_trial, source_parameters,
)


def scalar12(s):
    v=F(s)
    factor=10**12
    return str((v.numerator*factor//v.denominator)/factor)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verify",action="store_true")
    p.add_argument("--source",action="store_true")
    p.add_argument("--output",default=None)
    opts=p.parse_args()
    if not opts.source:
        raise SystemExit("Refuse a source-independent 'original' Weil residual.")
    params=source_parameters()
    oracle=frozen_operator_matrix_holdout(J=2,M=44,P=18)
    trial=source_residual_schur_trial(J=8,M=80,P=18,fit=True)
    assert trial["frozen_source_git_blob"]==SOURCE_SHA
    assert oracle["original_source_sha"]==SOURCE_SHA
    assert trial["authentic_first_prime_wavefront"]==((2,2),)
    assert trial["one_real_Gamma_contact_two_completed_poles"]
    assert oracle["all_original_signed_channels_tested"]
    if opts.verify:
        assert all(z["source_continuum_residual_norm_certified"]
                   for z in trial["four_original_parity_Schur_blocks"].values())
        assert all(v["independent_enclosures_intersect"]
                   for v in oracle["independent_exp_matrix_vs_Taylor_continuum_action"].values())
    result={
      "program":"ORIGINAL_SUZUKI_COMPLETED_CONTINUUM_K_RELATIVE_RESIDUAL",
      "source_SHA":SOURCE_SHA,
      "true_half_density":"1/2","true_prime2_only_at_radius_half":True,
      "source_calibration":{"b":str(params["b"]),"w":str(params["w"]),
                            "contact":str(params["contact"]),
                            "source_error_budget":(str(params["db"]),str(params["dw"]),str(params["dc"]))},
      "independent_archived_source_agreement":oracle,
      "four_low_schur_lower":trial,
      "Riemann_hypothesis_proved":False,
      "verification":"PASS" if opts.verify else "UNVERIFIED"
    }
    if opts.output:
        Path(opts.output).write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    reduced={"source_SHA":SOURCE_SHA,
       "independent_source_holdout_count":
          len(oracle["independent_exp_matrix_vs_Taylor_continuum_action"]),
       "signed_S4_lower_certificate_verdict":
          "CERTIFIED_FIRST_WINDOW_ONLY" if trial["all_four_source_S4_sign_certified"] else "AMBIGUOUS",
       "parity_blocks":{
          k:{"high_coefficients":v["fitted_high_coefficients"],
             "Schur_lower_decimal":
                  [[scalar12(q) for q in row] for row in v["genuine_source_2x2_Schur_Loewner_lower"]],
             "source_lower_PSD":v["source_Schur_lower_PSD_certified"]}
          for k,v in trial["four_original_parity_Schur_blocks"].items()},
       "RH_proved":False}
    print(json.dumps(reduced,sort_keys=True))


if __name__=="__main__":
    main()
