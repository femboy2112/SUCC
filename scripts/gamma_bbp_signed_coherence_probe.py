#!/usr/bin/env python3
"""Exact source-signed gamma and BBP Green-tail carrier certificates."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as Q
from observational_succ.gamma_bbp_signed_coherence import (
    moment_anchor,signed_moment_crossing,centered_resolvent_certificate,
    finite_twisted_coboundary,summable_tail_budget,weyl_orbit_transport,
    gamma_eight_channel_certificate,synthetic_atomic_order_countermodel,
    signed_green_memory_lower,finite_green_source,
)


def outward_decimal_interval(interval, digits=16):
    """Compact machine-checkable RATIONAL outer bracket, never float rounding."""
    scale=10**digits
    lower=interval.lower.numerator*scale//interval.lower.denominator
    upper=-((-interval.upper.numerator*scale)//interval.upper.denominator)
    assert Q(lower,scale)<=interval.lower<=interval.upper<=Q(upper,scale)
    return {"lower":str(Q(lower,scale)),"upper":str(Q(upper,scale)),
            "decimal_places":digits,"rational_outward":True}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--verify',action='store_true',help='enforce exact rational finite gates')
    args=p.parse_args()
    anchor=moment_anchor(0,terms=32)
    crossing=signed_moment_crossing(0,1,terms=33)
    centered=centered_resolvent_certificate(0,depth=12,terms=36)
    mass=summable_tail_budget(prefix_count=32,depth=12)
    weyl=weyl_orbit_transport(1,1000,prefix_count=32,depth=12)
    eight=gamma_eight_channel_certificate(20,terms=30)
    mutant=synthetic_atomic_order_countermodel()
    bridge=finite_twisted_coboundary(10,12)
    generic=finite_green_source(16,(Q(1),Q(-1,2),Q(2),Q(0)))
    memory_excess_lower=signed_green_memory_lower(terms=36)
    if args.verify:
        assert Q(4)<anchor.normalizer.lower<anchor.normalizer.upper<Q(30)
        assert crossing.determinant.lower>0
        assert centered.signed_resolvent.lower>0
        assert centered.pi_anchor_at_zero
        assert mass.mass.upper<=Q(17,648)
        assert weyl.normalized_error == weyl.uniform_absolute_sum_error/1000
        assert bridge[0]-bridge[1]==bridge[2]
        assert generic.source_orbit[1]+generic.green_potentials[1]==16*generic.green_potentials[0]
        assert Q(1,2)<eight.lower<eight.upper<Q(2,3)
        assert mutant.strict_cross_moment_order and not mutant.authentic
        assert memory_excess_lower>0
    record={
        'program':'SUCC_Gamma_BBP_signed_cocycle',
        'status':'locally_verified' if args.verify else 'not_requested',
        'original_source':'Coherent Main X BBP 4,-2,-1,-1 U0=0',
        'anchor_k0_lower':outward_decimal_interval(anchor.normalizer)['lower'],
        'anchor_k0_upper':outward_decimal_interval(anchor.normalizer)['upper'],
        'signed_cross_k0_j1_lower':outward_decimal_interval(crossing.determinant)['lower'],
        'signed_pi_gamma_resolvent_lower':outward_decimal_interval(centered.signed_resolvent)['lower'],
        'signed_pi_gamma_resolvent_upper':outward_decimal_interval(centered.signed_resolvent)['upper'],
        'signed_memory_excess_lower':outward_decimal_interval(type(centered.signed_resolvent)(memory_excess_lower,memory_excess_lower))['lower'],
        'gamma_eight_channel_lower':outward_decimal_interval(eight)['lower'],
        'gamma_eight_channel_upper':outward_decimal_interval(eight)['upper'],
        'global_T_mass_lower':outward_decimal_interval(mass.mass)['lower'],
        'global_T_mass_upper':outward_decimal_interval(mass.mass)['upper'],
        'original_rational_orbit_N1000_weyl_gap_cap':outward_decimal_interval(type(mass.mass)(weyl.uniform_absolute_sum_error,weyl.uniform_absolute_sum_error))['upper'],
        'normalized_weyl_gap_cap_N1000':outward_decimal_interval(type(mass.mass)(weyl.normalized_error,weyl.normalized_error))['upper'],
        'generic_radix_green_l1_bound':str(generic.l1_operator_bound),
        'synthetic_rational_counterfeit':str(mutant.rational_resolvent),
        'actual_pi_orbit_signed_cancellation_proved':False,
        'pi_normality_proved':False,
        'RH_proved':False,
    }
    print(json.dumps(record,indent=2,sort_keys=True))

if __name__=='__main__':main()
