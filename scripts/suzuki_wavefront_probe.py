"""Source-pinned Suzuki wavefront probes; JSON receipt, honest proof-status flags."""
from __future__ import annotations

import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from fractions import Fraction as Q
from observational_succ.suzuki_prime_boundary import complete_receipt
from observational_succ.suzuki_arch_intervals import first_source_screw_interval
from observational_succ.suzuki_bath_factor import (
    bath_source_receipt, certified_prime_free_small_interval,
    high_frequency_bath_tail_lower,
)


def receipt():
    out=complete_receipt()
    out["arch_source_point_intervals"]=[
        first_source_screw_interval(t,terms=40)
        for t in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(4,5))
    ]
    out["gamma_ou_bath"]=bath_source_receipt()
    out["certified_whole_space_small_interval"]=certified_prime_free_small_interval(Q(1,12),64)
    out["differentiated_tail_high_frequency_lower"]=high_frequency_bath_tail_lower(8,1024)
    out["completed_source_known_at_point_samples"]=True
    out["completed_Ga_operator_spectral_interval_certified"]=False
    out["certified_full_lambda_a_positive"]=False
    out["Weil_form_identification_at_selected_source_points"]="Suzuki (1.3), not a global sign"
    return out


def main():
    import argparse
    from pathlib import Path
    p=argparse.ArgumentParser()
    p.add_argument("--output")
    opts=p.parse_args()
    payload=json.dumps(receipt(),sort_keys=True,indent=2)+"\n"
    if opts.output:Path(opts.output).write_text(payload,encoding="utf-8")
    else:print(payload,end="")


if __name__=="__main__":main()
