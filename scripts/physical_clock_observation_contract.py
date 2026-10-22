"""Evaluate a USER-PROVIDED physical clock transcript against preregistered source laws.

No physical sensors are connected. This script does NOT authenticate that the
JSON was measured rather than fabricated, does NOT infer an infinite p-adic
source, and does NOT identify physical spacetime with its model.

Usage: PYTHONPATH=. python scripts/physical_clock_observation_contract.py --input reading.json
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from observational_succ.observation_pinned_geometry import (
    oriented_cycle_probe, ObservationContractError
)


def analyze(record):
    if not isinstance(record,dict):
        raise ObservationContractError('record must be a JSON object')
    required=('source_id','instrument_id','candidate_primes','phase_labels')
    if any(name not in record for name in required):
        raise ObservationContractError('source and initial observation fields required')
    selection=oriented_cycle_probe(
        record['phase_labels'],record['candidate_primes'],
        record['source_id'],record['instrument_id'])
    p=selection['selected_p']
    report={'selected_prime':p,'initial_clock_calibration':'MATCH_CONDITIONAL_ON_SOURCE_FIDELITY',
            'source_id':selection['source_id'],'instrument_id':selection['instrument_id'],
            'second_level_result':'NOT_SUPPLIED',
            'source_hypotheses_global_verified':False,
            'physical_measurement_authentication_by_script':False,
            'spacetime_geometry_identified':False}
    second=record.get('second_level')
    if second is None:
        return report
    if not isinstance(second,dict):
        raise ObservationContractError('second-level holdout must be an object')
    fields=('phase_labels','coarse_phase_for_fine_sequence','multiplier_p_outputs')
    if any(field not in second for field in fields):
        raise ObservationContractError('complete independent second-level fields required')
    fine=tuple(second['phase_labels'])
    coarse=tuple(second['coarse_phase_for_fine_sequence'])
    mult=tuple(second['multiplier_p_outputs'])
    N=p*p
    if len(fine)<N+1 or len(set(fine[:N]))!=N or fine[N]!=fine[0]:
        report['second_level_result']='REJECT_INCOMPLETE_OR_ALIASED_FINE_CLOCK'
        return report
    if any(fine[i]!=fine[i%N] for i in range(len(fine))):
        report['second_level_result']='REJECT_NONPERIODIC_FINE_CLOCK'
        return report
    expected_coarse=tuple(record['phase_labels'][n%p] for n in range(N))
    if coarse!=expected_coarse:
        report['second_level_result']='REJECT_INCOMPATIBLE_RING_QUOTIENT_MAP'
        return report
    if len(mult)!=N or any(mult[i]!=fine[(p*i)%N] for i in range(N)):
        report['second_level_result']='REJECT_FUCC_MULTIPLICATION_HOLDOUT'
        return report
    report['second_level_result']='SECOND_LEVEL_HELD_OUT_PREDICTIONS_MATCH'
    report['predicted_root_degree_if_rank_two_lift_assumed']=p+1
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',required=True,type=Path,help='independent source transcript JSON; not populated automatically')
    args=parser.parse_args()
    record=json.loads(args.input.read_text(encoding='utf-8'))
    print(json.dumps(analyze(record),indent=2,sort_keys=True))


if __name__=='__main__':main()
