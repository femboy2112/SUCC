"""Reproducible exact finite/infinite-toy proof-access receipt; zero-free inputs."""
from __future__ import annotations

import json
from fractions import Fraction as Q
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.cofinal_schur_telescope import (  # noqa: E402
    DiagonalToy, FiniteCarrier, ConditionalSourceEnvelope, diag, matrix,
    trans, mul, search_toy, genuine_source_obligations,
)


def render(value):
    if isinstance(value,Q):return str(value)
    if isinstance(value,tuple):return [render(x) for x in value]
    if isinstance(value,dict):return {k:render(v) for k,v in sorted(value.items())}
    return value


def main():
    v=diag((Q(1,2),Q(1,3)))
    r=tuple(tuple(-q for q in row) for row in v)
    y=((-1,-1),(-1,1))
    b=tuple(tuple(-q for q in row) for row in mul(trans(v),matrix(y)))
    source=FiniteCarrier(((2,1),(1,2)),b,mul(v,v),v,y,r,Q(1))
    no_trial=source.trial(((0,0),(0,0)))
    exact_trial=source.trial(((2,2),(3,-3)))
    toy_delayed=DiagonalToy('delayed',delay=25)
    toy_singular=DiagonalToy('singular')
    toy_unbounded=DiagonalToy('unbounded')
    packet=ConditionalSourceEnvelope(
        '0cc8510b71d178fc79e8d410a86d8b6014cf9178',Q(1,2),
        ('prime2_half_density','real_gamma','pole_plus','pole_minus','contact'),
        (Q(1,3),Q(1,5),Q(1,7),Q(1,9)),
        diag((Q(1,20),Q(1,10),Q(1,15),Q(1,25))),
        Q(1,1000),Q(1,100),Q(20699,1000000),genuine_source_obligations())
    receipt={
        'status':'EXACT_FINITE_MODELS_AND_CONDITIONAL_SOURCE_GATE',
        'finite_cross_coupling':{'actual_short':source.actual_short(),
            'zero_trial_lower':no_trial.lower,'exact_residual_gram':exact_trial.residual_gram,
            'finite_source_authenticated_as_original_Weil':False},
        'hidden_mode':{'early':toy_delayed.stage(24),
            'first_visible':search_toy(toy_delayed,sign=True,max_stage=25),
            'premature_stop':search_toy(toy_delayed,sign=True,max_stage=24)},
        'divergent_response':{'stage10':toy_unbounded.stage(10),
            'stage20':toy_unbounded.stage(20),
            'accuracy_1_over_10':search_toy(toy_unbounded,accuracy=Q(1,10),max_stage=20)},
        'singular':{'stage10':toy_singular.stage(10),
            'strict_sign_budget':search_toy(toy_singular,sign=True,max_stage=10),
            'accuracy_1_over_1000':search_toy(toy_singular,accuracy=Q(1,1000),max_stage=10)},
        'source_packet_untrusted':packet.bracket(),
        'cofinal_actual_source_oracle_integrated':False,
        'whole_high_coercivity_independently_Lean_proved':False,
        'full_Weil_sign_decided':False,
        'RH_proved':False,
    }
    print(json.dumps(render(receipt),indent=2,sort_keys=True))


if __name__=='__main__':main()
