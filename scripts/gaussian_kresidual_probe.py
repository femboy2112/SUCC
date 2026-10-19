"""Original signed source clamped K-residual vs Gaussian half-density.

Exact Fraction calculations; --source fails closed unless original Suzuki
archived SHA and actual signed low/high source are installed.
"""
import argparse
import json
from fractions import Fraction as F
from observational_succ.clamped_k_residual_bridge import (
 CLAMPED,checked_trial,gamma_action_tail,
 authentic_clamped_signed_source,conditional_schur_residual_envelope,
)
from observational_succ.gaussian_prime_two_density import (
 first_two_step_source,inert_prime_negative_control,
 authenticated_two_prime_source,local_prime_half_density_square,
)

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--source",action="store_true")
 p.add_argument("--verify",action="store_true")
 args=p.parse_args()
 trials={k:checked_trial(k) for k in CLAMPED}
 original=authentic_clamped_signed_source(J=8) if args.source else None
 gauss=authenticated_two_prime_source() if args.source else None
 residual=conditional_schur_residual_envelope(
      F(63,500),(F(1),F(1)),(F(2),F(2)),F(1,10),
      gamma_action_tail(8))
 if args.verify:
  assert local_prime_half_density_square(2)==F(1,2)
  assert local_prime_half_density_square(3)==F(1,3)
  assert all(v["source_Q4_constraints"] and
             v["zero_value_AND_zero_derivative_traces"] for v in trials.values())
  assert not residual["full_source_action_residual_certified_by_this_function"]
  assert not first_two_step_source()["Weil_half_density_uniquely_derived_from_Gaussian_2"]
  if args.source:
   assert original["source_git_blob"]=="0cc8510b71d178fc79e8d410a86d8b6014cf9178"
   assert gauss["source_sha"]==original["source_git_blob"]
   assert all(not z["complete_continuum_action_residual_norm_observed"]
              for z in original["parity_clamped_high_packets"].values())
 print(json.dumps({
    "program":"ORIGINAL_TWO_SUCC_GAUSSIAN_K_RELATIVE_CLAMPED_2026_10_18",
    "gaussian_two":first_two_step_source(),
    "gaussian_inert_prime_negative_control":inert_prime_negative_control(),
    "high_clamped_trials":trials,
    "source_clamped_signed_packets":original,
    "source_2_halfdensity":gauss,
    "conditional_not_source_residual_schur":residual,
    "RH_proved":False,
    "verification":"PASS" if args.verify else "UNVERIFIED"
 },sort_keys=True))

if __name__=="__main__":
 main()
