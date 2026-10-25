#!/usr/bin/env python3
"""Exact rational 0/1 gamma charts, true BBP moment dominance, finite mutant."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q

from observational_succ.zero_one_gamma_bridge import (
 logarithmic_successor_unit,gamma_defect_interval,
 gamma_field_certificate,gamma_r_finite_bracket,
 bbp_gamma_cell_certificate,bbp_gamma_quadratic,shared_resolvent_certificate,
 finite_jet_moment_mutant,bbp_polynomial,
)


def serial(v):
    if isinstance(v,Q):return str(v)
    if isinstance(v,(tuple,list)):return [serial(x) for x in v]
    if isinstance(v,dict):return {key:serial(x) for key,x in v.items()}
    if hasattr(v,'__dataclass_fields__'):
        return {key:serial(getattr(v,key)) for key in v.__dataclass_fields__}
    return v


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--verify',action='store_true')
    args=p.parse_args()
    unit=logarithmic_successor_unit(Q(1),30)
    defect=gamma_defect_interval(Q(1),35)
    gamma1=gamma_field_certificate(Q(1),80,30)
    gamma2=gamma_field_certificate(Q(2),80,30)
    gamma_r2=gamma_r_finite_bracket(2,Q(1),80)
    selected=tuple(bbp_gamma_cell_certificate(n,25) for n in (1,2,4,8,32,128))
    vector=bbp_gamma_quadratic((Q(1),Q(-1),Q(1)),65)
    compared=shared_resolvent_certificate(8,32)
    mut=finite_jet_moment_mutant(3,3)
    if args.verify:
        assert unit['additive_successor']==1 and unit['normalized_log_unit']==1
        assert unit['log_increment'].upper<1
        assert defect.lower>0
        assert gamma1.total.lower>gamma2.total.upper
        assert gamma_r2.lower>0
        assert all(4<t.lower_ratio and t.upper_ratio<30 for t in selected)
        assert all(selected[i].upper_ratio<selected[i+1].lower_ratio for i in range(len(selected)-1))
        assert 4*vector['gamma_form'].upper<vector['bbp_form']<30*vector['gamma_form'].lower
        assert compared.pi_outer.lower<compared.pi_outer.upper
        assert all(mut.moment_shift(i)==0 for i in range(3))
        assert mut.moment_shift(3)>0 and mut.resolvent_shift_bracket.lower>0
        assert mut.kernel_at(Q(1))==0 and mut.kernel_at(Q(1,2))>0
        assert bbp_polynomial(Q(1))==0
    out={
      'study':'gamma-zero-one-BBP-coherent-carrier',
      'verification':'passed' if args.verify else 'not_requested',
      'source':'true four-pole BBP, underlying SUCC main source implementation',
      'unit_chart_x1':unit,
      'delta_x1':defect,
      'gamma_x1':gamma1.total,
      'gamma_x2':gamma2.total,
      'gamma_r2_x1':gamma_r2,
      'bbp_gamma_n_ratio_witnesses':selected,
      'hankel_quadratic':vector,
      'shared_resolvent':compared,
      'positive_finite_moment_counterfeit':mut,
      'analytical_hankel_all_dimensions':'paper theorem; not inferred from finite tests',
      'finite_data_select_pi':False,
      'source_specific_signed_carry_bound_proved':False,
      'pi_normality_proved':False,
      'RH_proved':False,
    }
    print(json.dumps(serial(out),sort_keys=True,indent=2))


if __name__=='__main__':main()
