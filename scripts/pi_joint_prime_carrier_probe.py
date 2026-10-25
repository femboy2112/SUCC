"""Reproducible exact joint-carrier receipt; floating observations are labelled."""
from __future__ import annotations

import cmath
from collections import Counter
from fractions import Fraction as Q
import json
from math import pi
from pathlib import Path

from observational_succ.pi_joint_prime_carrier import (
    certified_hex_digit, conditional_squared_residual, correlated_six_phase_control,
    dyadic_integral, floor_hex_digit, forcing, forcing_odd, four_gate_interaction,
    hidden_prime_halfway, joint_primary, local_primary, primes_through,
    six_phase_control, source_prime_bound, states,
)


def phase(x: Q) -> complex:
    # Noncertifying complex diagnostic: exact rational x modulo 1 first.
    t=float(x%1)
    return cmath.exp(2j*pi*t)


def main():
    length=513
    xs=states(length)
    exact_checks=0
    source_components=[]
    for n,x in enumerate(xs):
        assert forcing(n)==forcing_odd(n) if n else x==0
        exact_checks+=1
        assert x.denominator%2==1
        exact_checks+=1
        comps=joint_primary(x,primes_through(source_prime_bound(n)))
        source_components.append(comps)
        assert sum((z for _,z in comps),Q())%1==x%1
        exact_checks+=1
        assert all(p!=2 for p,_ in comps)
        exact_checks+=1
        for h in (-7,-1,1,2,5,17):
            assert (sum((h*c for _,c in comps),Q()))%1 == (h*x)%1
            exact_checks+=1
    for n in range(1,length):
        for p in (2,3,5,7,11,13,17,31,127):
            assert local_primary(xs[n],p)==(
                16*local_primary(xs[n-1],p)+local_primary(forcing(n),p))%1
            exact_checks+=1
    for k in range(1,10):
        actual={dyadic_integral(xs[n],k) for n in range(2**k)}
        assert actual==set(range(2**k))
        exact_checks+=2**k
    print('verified full source factorization, local recurrences, dyadic residue permutations')

    synthetic=six_phase_control()
    losses={str(mask):str(conditional_squared_residual(synthetic,mask))
            for mask in ((),(2,),(3,),(2,3))}
    assert losses=={'()':'5/36','(2,)':'1/9','(3,)':'1/12','(2, 3)':'0'}
    assert four_gate_interaction(synthetic,2,3)==Q(1,18)
    exact_checks+=5

    correlated=correlated_six_phase_control()
    assert Counter(local_primary(x,2) for x in correlated)=={Q(0):3,Q(1,2):3}
    assert Counter(local_primary(x,3) for x in correlated)=={
        Q(0):2,Q(1,3):2,Q(2,3):2}
    exact_checks+=2

    out={'schema':1,'authority':'exact integer/Fraction controls except explicitly labelled complex diagnostics',
         'parent_source':'fixed four-pole rational BBP forcing, U0=0',
         'source_states_count':length,
         'synthetic_prime_synergy':{'residuals':losses,'factorial_gain':'1/18'},
         'prime_character_correlated_control':{
             'local_p2_character_mean':'0', 'local_p3_character_mean':'0',
             'global_character_mean':'(1-omega^2)/3, omega=exp(2*pi*i/3)',
             'global_mean_squared_modulus':'1/3'},
         'moving_prime_windows':{},
         'certified_hex_prefixes':{},
         'empirical_actual_rational_sample':{},
         'fixed_prime_missing_half_real':{},
         'comments':['All source window statistics are finite and not a pi-normality theorem.',
                     'Only genuine BBP finite gates with certified tail intervals are labelled certified.',
                     'A joint empirical conditional residual can vanish from unique state fingerprints.']}

    for n in (1,8,16,31,63,127,255,511):
        u=xs[n]
        comps=source_components[n]
        out['moving_prime_windows'][str(n)]={
            'prime_bound':source_prime_bound(n),'active_odd_primes':len(comps),
            'largest_active_prime':comps[-1][0] if comps else 0,
            'denominator_bits':u.denominator.bit_length(),
            'dyadic_residue_mod_256':dyadic_integral(u,8),
            'p2_torsion_is_zero':local_primary(u,2)==0,
        }

    for N in (16,64,256,512):
        digits=[certified_hex_digit(n,xs[n]) for n in range(1,N+1)]
        assert all(d is not None for d in digits)
        exact_checks+=N
        counts=[digits.count(d) for d in range(16)]
        out['certified_hex_prefixes'][str(N)]={
            'certified':len(digits),'ambiguous':0,'zero_gate_count':counts[0],
            'zero_gate_target_ratio':'1/16','digit_counts':counts,
        }

    a,b=1,256
    selected=xs[a:b+1]
    for mask in ((),(2,),(3,),(5,),(3,5),(3,5,7)):
        out['empirical_actual_rational_sample'][str(mask)]=str(
            conditional_squared_residual(selected,mask))
        exact_checks+=1
    seen={tuple(local_primary(x,p) for p in (3,5)) for x in xs[1:65]}
    unseen=sum(tuple(local_primary(x,p) for p in (3,5)) not in seen
               for x in xs[65:257])
    out['empirical_actual_rational_sample']['holdout_unseen_prime_signatures_65_through_256']=unseen
    assert unseen>150

    for q in (23,101,1009):
        x=hidden_prime_halfway(q)
        assert all(local_primary(x,p)==0 for p in primes_through(19))
        exact_checks+=1
        out['fixed_prime_missing_half_real'][str(q)]={'real_fraction':str(x),
            'distance_from_half':str(Q(1,2)-x), 'all_primes_2_to_19_see_zero':True}

    # Correlation sensitivity: hold every prime's marginal multiset fixed,
    # but cyclically permute the p=3 *time alignment*; violates true source.
    p3=[local_primary(x,3) for x in selected]
    shifted=[((x - p3[i] + p3[(i+1)%len(p3)])%1) for i,x in enumerate(selected)]
    mut_counts=[sum(floor_hex_digit(v)==d for v in shifted) for d in range(16)]
    true_counts=[sum(floor_hex_digit(v)==d for v in selected) for d in range(16)]
    assert Counter(p3)==Counter(p3[1:]+p3[:1])
    out['diagnostic_not_certified']={
       'prime_3_shift_keeps_exact_primary_marginal':True,
       'primary_source_gate_counts':true_counts,
       'shifted_prime_3_gate_counts':mut_counts,
       'changes_gate_histogram':true_counts!=mut_counts,
       'complex_weyl_h1_for_source_abs':round(abs(sum(phase(v) for v in selected)/len(selected)),8),
       'complex_weyl_h1_for_mutant_abs':round(abs(sum(phase(v) for v in shifted)/len(shifted)),8),
    }
    assert true_counts!=mut_counts
    out['exact_assertions']=exact_checks
    output=Path(__file__).resolve().parents[1]/'research'/'2026-10-24'/'PI_JOINT_PRIME_CARRIER_RECEIPT.json'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'exact_assertions':exact_checks,
                      'active_prime_counts':{n:out['moving_prime_windows'][n]['active_odd_primes']
                                             for n in ('31','127','255','511')},
                      'synergy':'1/18', 'certified_N512':True,
                      'mutant_changes_counts':true_counts!=mut_counts,
                      'output':str(output)},indent=2))

if __name__=='__main__':main()
