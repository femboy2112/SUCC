"""Original source, three independent real-Gamma depths (no zeros).

Do not interpret a negative conservative lower as a negative Weil witness.
This holds only clamped H2 source trials and authentic two-polar source.
"""
import json
import argparse
from fractions import Fraction as F
from observational_succ.original_continuum_residual import (
 source_residual_schur_trial,SOURCE_SHA,
)

def signed_decimal(v,places=10):
 x=F(v);a=10**places;n=x.numerator*a//x.denominator
 sign="-" if n<0 else ""
 z=str(abs(n)).zfill(places+1)
 return sign+z[:-places]+"."+z[-places:]

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verify",action="store_true")
 args=p.parse_args()
 cells=[]
 for j,M in ((4,56),(8,80),(12,100),(16,128)):
  r=source_residual_schur_trial(J=j,M=M,P=18,fit=True)
  if args.verify:
   assert r["frozen_source_git_blob"]==SOURCE_SHA
   assert all(z["source_continuum_residual_norm_certified"]
              for z in r["four_original_parity_Schur_blocks"].values())
  blocks={}
  for k,z in r["four_original_parity_Schur_blocks"].items():
   blocks[k]={
      "S_lower_diagonals":tuple(signed_decimal(z["genuine_source_2x2_Schur_Loewner_lower"][i][i])
                           for i in range(2)),
      "source_qJ_diagonal_lowers":tuple(signed_decimal(v)
                                    for v in z["source_qJ_original_diagonal_lower"]),
      "surrogate_projection_norm_sq_diagonals":tuple(signed_decimal(v)
                       for v in z["surrogate_projected_action_diagonal_squared"]),
      "source_finite_action_errors":tuple(signed_decimal(v)
                                       for v in z["finite_source_action_error_each"]),
      "Gamma_tail_action_errors":tuple(signed_decimal(v)
                                    for v in z["genuine_omitted_Gamma_action_error_each"]),
      "fitted_clamped_high_coefficients":z["fitted_high_coefficients"],
      "certified_positive_full_source_Schur_lower":z["source_Schur_lower_PSD_certified"]}
  cells.append({"source":SOURCE_SHA,"J":j,"M":M,"blocks":blocks,
                "all_S4_sign_certified":r["all_four_source_S4_sign_certified"]})
 print(json.dumps({"program":"ORIGINAL_CONTINUUM_CUTOFF_SWEEP",
   "cells":cells,"RH_proved":False,
   "validation":"PASS" if args.verify else "UNVERIFIED"},sort_keys=True))

if __name__=="__main__":
 main()
