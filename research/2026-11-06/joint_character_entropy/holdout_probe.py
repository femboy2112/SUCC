"""Round-II calibration and source/observer probe. Signed epochs were explored before prereg; see immutable ADDENDUM."""
from __future__ import annotations
import hashlib
import json
import math
from fractions import Fraction
from joint_entropy import (certified_source_digits,original_states,certified_completed_digit,
                           pole_clock,mealy_run,decode_reversible_observer,block_entropy)
from independent_oracle import machin_pi16_interval,digit_certificates,independent_combined_source
from signed_certificate import (certified_weyl,source_completed_samples,short_receipt)

PREREG_SHA256="efcefe2c71f3d9898b7dd6f6b45f3cc7ed287cbef651bae66793fd43ae10cc32"


def run() -> dict:
    prereg=hashlib.sha256(open('PREREGISTRATION.md','rb').read()).hexdigest()
    assert prereg==PREREG_SHA256,"preregistered conditions changed"
    for n in range(1,201):
        from joint_entropy import four_pole
        assert independent_combined_source(n)==four_pole(n)
    independent_digits=digit_certificates(machin_pi16_interval(150,38),128)
    digits,depths=certified_source_digits(1536)
    assert digits[:128]==independent_digits

    metrics=[]
    for N in (384,768,1536):
        d=digits[:N]
        clock=tuple(pole_clock(n,7) for n in range(N))
        c,_=mealy_run(d,clock)
        assert decode_reversible_observer(c,clock)==d
        row={"N":N,"selected_max_source_tail_depth":max(depths[:N]),
             "input_d1":round(math.log(16)-block_entropy(d,1),12),
             "output_d1":round(math.log(16)-block_entropy(c,1),12),
             "input_d2":round(2*math.log(16)-block_entropy(d,2),12),
             "output_d2":round(2*math.log(16)-block_entropy(c,2),12)}
        row["output_improves_d1_finite"]=(row["output_d1"]<row["input_d1"])
        metrics.append(row)

    finite_signed=[]
    for A in (223,457):
        samples=source_completed_samples(A,depth=12)
        for h in (1,2):
            v=certified_weyl(samples,h)
            assert v['upper'] < Fraction(1)
            finite_signed.append({"epoch_start_A":A,**short_receipt(v)})

    rootgrid=[]
    zero_phase=tuple((Fraction(j,16),Fraction(j,16)) for j in range(16))
    for h in (1,2):
        v=certified_weyl(zero_phase,h)
        assert v['upper']<Fraction(1,1000000)
        rootgrid.append(short_receipt(v))

    periodic_ghost=[]
    periodic=tuple((Fraction(1,5),Fraction(1,5)) for _ in range(223))
    for h in (1,2):
        v=certified_weyl(periodic,h)
        assert v['lower']>Fraction(99,100)
        periodic_ghost.append(short_receipt(v))

    # One-pole first-step source mutant; original tail after n>=1 unchanged.
    from joint_entropy import original_states
    states=original_states(128)
    changed=[]
    for n in range(1,128):
        mutated_x=(states[n]+Fraction(16**(n-1),37))%1
        mutant_d,_=certified_completed_digit(mutated_x,n)
        changed.append(mutant_d)
    first_mutant_mismatch=next((n for n in range(1,128) if changed[n-1]!=digits[n]),None)
    assert first_mutant_mismatch is not None

    return {"source":"four original signed poles, literal U0=0", "normality":"OPEN",
            "preregistration_sha256":prereg,"original_pole_checks":200,
            "independent_machin_bbp_matching_digits":128,
            "source_clock_period":7,"observer_internal_states":16,
            "certified_1536_digits":len(digits),"first_32_hex":"".join(format(d,'x') for d in digits[:32]),
            "digit_entropy_metrics_in_nats":metrics,
            "selected_epoch_rigorous_signed_weyl_bounds":finite_signed,
            "positive_uniform_grid_controls":rootgrid,
            "negative_same_source_periodic_completion_beta_1_5":periodic_ghost,
            "mutated_first_source_step":{"delta":"1/37", "first_certified_digit_mismatch_at_n":first_mutant_mismatch},
            "signed_epoch_provenance":"pre-seen calibration, not blind holdout",
            "no_infinite_time_inference":True}


if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
