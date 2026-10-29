"""Generate an exact rational receipt from executed local source/observer code."""
from __future__ import annotations

import json
import hashlib
from pathlib import Path
from fractions import Fraction as F

from hopf_source_exact import (
    SOURCE_ID, ORIGINAL_TAPS, CHIRAL_EVEN_TAPS, CHIRAL_ODD_TAPS, T,
    ONE,I,J,K,H, Sphere4, SOURCE_ORIGIN,
    hopf, hopf_left, hopf_right_to_left_odd, hopf_left_to_right_odd,
    hopf_two_step_base, t_step,t_iter, t_odd_quaternion_factor, t2_quaternion_factor,
    j_chirality, consecutive_hopf, original_forcing, pole_quaternion,
    source_labelled_mixed_hopf,source_labelled_decode_poles,source_sphere_chart,
    coherent_changed_seed_tail_bound,as_serializable
)

loc=Path(__file__).resolve().parent

before=hopf(ONE,I)
original_gauge=hopf(J,K)
one_right=hopf(t_step(ONE),t_step(I))
other_right=hopf(t_step(J),t_step(K))
after_left=hopf_left(t_step(ONE),t_step(I))
other_left=hopf_left(t_step(J),t_step(K))
assert before==original_gauge
assert one_right!=other_right
assert after_left==other_left==hopf_right_to_left_odd(before)
assert t2_quaternion_factor(ONE)==t_iter(ONE,2)
assert t_odd_quaternion_factor(ONE)==t_step(ONE)

selected8=[as_serializable(consecutive_hopf(n)) for n in range(8)]
assert len(set(tuple([*x['R'],x['B']]) for x in selected8))==5

mixed={}
for n in (1,2,3,8,12,16):
    q=pole_quaternion(n)
    p=source_labelled_mixed_hopf(n)
    recovered=source_labelled_decode_poles(n,p)
    assert recovered==q
    mixed[str(n)]={"signed_poles":[str(x) for x in q],
                   "signed_forcing":str(original_forcing(n)),
                   "Hopf":as_serializable(p),
                   "decode_exact":True}

poles={str(n):{"n":n,"pole_components":[str(x) for x in pole_quaternion(n)],
                "r(n)":str(original_forcing(n)),
                "anchored_Hopf":as_serializable(source_sphere_chart(pole_quaternion(n)))}
       for n in (1,2,3,4,8)}

selected_latitudes={str(n):str(source_sphere_chart(t_iter(SOURCE_ORIGIN,n)).B)
                    for n in (0,1,2,3,4,5,6,7,8)}

receipt={
  "record":"SUCC quaternionic Hopf source transport — exact local receipt",
  "date":"2026-10-27",
  "write_scope":"LOCAL_ONLY; no GitHub write; no merge, PR or CI",
  "source_provenance":{
    "SUCC_main_sha":"6dd80730c3575d91f746546a25da5aedbd2e2737",
    "source_PR":333,
    "source_PR_head":"a0e4bfd9c218dfdc83ed9d5684ce8d8e4624cde5",
    "source_code":"observational_succ/rank_two_chiral_towers.py",
    "source_identifier":SOURCE_ID,
    "Main_XII_draft_PR":342,
    "observed_Main_XII_draft_head":"ce7df73431e85a4eb2a290445da8e09d4f924b3e",
  },
  "source_fidelity":{
    "matrix_T": [[str(x) for x in row] for row in T],
    "first_8_signed_taps":[str(x) for x in ORIGINAL_TAPS],
    "even_8_taps":[str(x) for x in CHIRAL_EVEN_TAPS],
    "odd_8_taps":[str(x) for x in CHIRAL_ODD_TAPS],
    "four_exact_pole_samples":poles,
    "original_real_seed":"U_0=0; U_n=16 U_(n-1)+r(n)",
  },
  "source_Hopf_transport":{
    "one_step_anti_quaternion":"T(x)=(i+k)*conj(x)*(1-i-j-k)/4",
    "two_step_Hamilton":"T^2(x)=(1-k)*x*(1+i)/4",
    "odd_right_Hopf_one_chart_no_go":{
        "equivalent_inputs":["(1,i)","(j,k)"],
        "same_original_Hopf":as_serializable(before),
        "different_one_step_right_Hopf":[as_serializable(one_right),as_serializable(other_right)],
        "equal_after_step_left_Hopf":as_serializable(after_left),
        "source_gauge_counterexample_verified":True,
    },
    "two_chart_odd_transport":{"R_to_L":"R -> r^-1 conjugate(R) r",
                                "L_to_R":"R -> L conjugate(R) L^-1",
                                "latitude_B":"preserved"},
    "even_step_Hopf_rotation":"(r0,ri,rj,rk,B)->(r0,rj,-ri,rk,B)",
    "even_rotation_order":4,
    "selected_consecutive_8_Hopf_observations":selected8,
    "selected_consecutive_unique_count":5,
    "selected_consecutive_fixed_latitude":"1/3",
    "J_mirror_latitude":"0",
    "anchored_source_selected_latitudes":selected_latitudes,
    "mixed_pole_chiral_declared_pairing":mixed,
    "note":"Mixed clock pairing is a declared source-labelled observer candidate, not forced by BBP."
  },
  "source_seed_counterexample":{
    "alternative_seed":"-pi/16; not the original zero seed",
    "derived_tail":"U_n(alt)=-sum_{k>=1}16^-k r(n+k)",
    "real_tail_bound_n_8":str(coherent_changed_seed_tail_bound(8)),
    "verdict":"phase tends to 1, hence not normal; source-only Hopf candidate cannot distinguish seeds"
  },
  "claim_status":{
    "exact_source_specific_algebra":"DISCLOSED within source and quaternion conventions",
    "finite_source_execution":"OBSERVED 34 focused Fraction unit tests",
    "independent_symbolic_rederivation":"OBSERVED SymPy oracle PASS",
    "naive_odd_right_Hopf_self_map":"REFUTED",
    "source_full_S4_equidistribution":"UNVERIFIED",
    "zero_seed_signed_Weyl_saving":"UNVERIFIED",
    "SUCC_native_CI_Lean":"NOT_RUN"
  },
  "local_source_digests":{
    name: hashlib.sha256((loc/name).read_bytes()).hexdigest()
    for name in ('hopf_source_exact.py','test_hopf_source.py','oracle_sympy.py')
  }
}
(loc/'SOURCE_RECEIPT.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print('PASS exact SOURCE_RECEIPT generated;',len(selected8),'selected points and',len(mixed),'source-mixed samples')
