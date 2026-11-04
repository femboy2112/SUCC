"""Predeclared finite exact original-source checks (not asymptotic proof)."""
from __future__ import annotations
import json
import hashlib
from fractions import Fraction as Q
from pathlib import Path
from math import prod
from odd_gamma_front import (fraction_states,prime_passports,window_prime_clock,
  exact_prime_mass_profile,geometric_gamma_tail_interval,
  gamma_corrected_tail_interval,real_source,source)

ROOT=Path(__file__).resolve().parent

def sha_int(n:int)->str:
    return hashlib.sha256(n.to_bytes(max(1,(n.bit_length()+7)//8),'big')).hexdigest()

def run():
    finite={}
    checked_total=0
    for A in (96,192,384,768):
        passports=prime_passports(A)
        plus=passports['split']; minus=passports['inert']
        ps=tuple(sorted(p for p,b in plus+minus))
        mass=prod(ps)
        profile=exact_prime_mass_profile(A)
        if A<=192:
            states=list(fraction_states(passports['stop']-1))
            for typ,lst in [('split',plus),('inert',minus)]:
                for p,b in lst:
                    for n in range(A,passports['stop']):
                        q=p*states[n][3]
                        assert q.denominator%p != 0
                        observed=q.numerator*pow(q.denominator,-1,p)%p
                        expected=window_prime_clock(p,b,n,typ)
                        assert observed==expected
                        checked_total+=1
        finite[str(A)]={
            'window':[A,passports['stop']],'count_split':len(plus),
            'count_inert':len(minus),'log_prime_mass_approx':profile['log_mass_approx'],
            'log_radix_threshold_approx':profile['threshold_log_approx'],
            'certified_mass_greater_than_16_power':profile['exact_mass_dominates_full_window'],
            'minimum_nonalias_count':profile['minimum_nonaliases_across_lags'],
            'max_alias_count':profile['maximum_alias_count'],
            'worst_average_kernel_denominator_bits':profile['worst_average_kernel_denominator_bits'],
            'prime_product_sha256':sha_int(mass),
            'all_prime_clocks_tested_against_fraction':A<=192
        }
    gamma={}
    for n in (17,49,113,257):
        hl,hu=geometric_gamma_tail_interval(n,100)
        rl,ru=gamma_corrected_tail_interval(n,100)
        assert Q(0)<rl<ru<Q(1,64*n*n)
        # Interval endpoints are exact Fractions; quote them without pi digits.
        gamma[str(n)]={'minus_T_H_enclosure':[str(hl),str(hu)],
                       'residual_enclosure':[str(rl),str(ru)]}
    return {
        'original_source':'4 signed BBP terms, U0=0',
        'parent_sha':'057a68c4b4e01439e76c2050c28309a4858b9dc2',
        'preregistration_sha':'2235c5e00dcdfcbb96d5a9eee7709cd25f67848c',
        'status':'EXACT FINITE OBSERVATIONS ONLY, no pi-normality or all-horizon bound',
        'tested_prime_residue_instances':checked_total,
        'epochs':finite,'gamma':gamma,
        'false_long_window':{'p':47,'birth_n':12,'second_injection_n':18,
                              'inert_two_pole_window_is_false':True}
    }

if __name__=='__main__':
    dest=ROOT/'FINITE_RECEIPT.json'
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    got=run()
    if args.verify:
        assert json.loads(dest.read_text())==got
        print('Original-source exact prime/Gamma receipt replay: PASS')
    else:
        dest.write_text(json.dumps(got,indent=2,sort_keys=True)+'\n')
        print('Generated exact original-source receipt; verified instances:',got['tested_prime_residue_instances'])
