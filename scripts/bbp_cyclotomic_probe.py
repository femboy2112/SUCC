"""Deterministic exact-data receipt; run from repository root (PYTHONPATH=.)."""
from __future__ import annotations

import json

from observational_succ.bbp_source_memory import forcing
from observational_succ.bbp_cyclotomic_birth import (
    birth_index, first_phase_residue, next_pole_gap,
    multiplicative_order_16, full_cycle_count, galois_mean_squared,
    construct_coprime_clock_counterfeit, counterfeit_upper,
    exceptional_prime_count_bound, source_window_split,
    within_block_complement_variation,
)


def fraction_pair(x):
    return [str(x.numerator), str(x.denominator)]


def main():
    records=[]
    for p in (3,5,7,11,13,17,29,41,73,97,113,137,193):
        row={"p":p,"birth":birth_index(p),"gap":next_pole_gap(p),
             "phase_mod_p":first_phase_residue(p),
             "multiplicative_order":multiplicative_order_16(p),
             "forcing_first":fraction_pair(forcing(birth_index(p)))}
        if p%8==1:
            row.update(cycles=full_cycle_count(p),
                       galois_mean_square=fraction_pair(galois_mean_squared(p)),
                       p_free_length=len(source_window_split(p)),
                       within_block_variation=fraction_pair(within_block_complement_variation(p)))
        records.append(row)
    phase,Q=construct_coprime_clock_counterfeit(17,6,2)
    report={"research":"CBCW source-typed prime birth and lag",
            "complete_normality_proof":False,
            "source_contract":"BBP index forcing + y0=0; no fake pi digits",
            "exception_bound_X_1000":exceptional_prime_count_bound(1000),
            "prime_cases":records,
            "hostile_coprime_phase_17":fraction_pair(phase),
            "hostile_coprime_denominator_17":str(Q),
            "hostile_global_sum_error_upper_17":fraction_pair(counterfeit_upper(6,Q)),
            "external_BKG_power_saving_computationally_verified":False}
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__=="__main__":main()
