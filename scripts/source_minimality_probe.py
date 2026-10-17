#!/usr/bin/env python3
"""Exact finite-source and analytic-identity calibration. stdlib only.

Mathematical universal claims are paper proofs, not inferred from tests.
"""
import argparse
import json
import sys
from pathlib import Path
from fractions import Fraction as F
from math import lcm
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from observational_succ.source_minimality import (
    ClockTheory, finite_clock_closure, missing_power_infinite_shadow,
    matching_finite_shadow, rooted_diagonal_orbit, unique_pointed_clock_map,
    authenticate_prime_word, divisors)
from observational_succ.carry_clock_lift import CarryClock,carry_vs_uncoupled
from observational_succ.renewal_rigidity import (
    MUTANT_A,MUTANT_B,mutant_atoms,calibration_atoms,
    renewal_residual,first_unit_cell,affine_counterexample,density_residue_certificate)

RECEIPT=Path(__file__).resolve().parent.parent/'research/2026-10-17/SOURCE_MINIMALITY_RECEIPT.json'


def exact_receipt():
    full=ClockTheory('full')
    square=ClockTheory('squarefree')
    pro2=ClockTheory('pro_p',2)
    finite_family=(2,3,4,5,6,8,12,15,30,84)
    shadow=missing_power_infinite_shadow(finite_family)
    finite=matching_finite_shadow(finite_family)
    assert finite['finite_signature']==finite['full_signature']
    assert full.finite_signature(finite_family)==ClockTheory('one_prime_cap',(2,shadow['capped_depth'])).finite_signature(finite_family)
    assert full.permits(shadow['first_missing_power'])
    assert not ClockTheory('one_prime_cap',(2,shadow['capped_depth'])).permits(shadow['first_missing_power'])
    assert all(square.prime_exposure(p) and not square.permits(p*p) for p in (2,3,5,7,11))
    assert pro2.permits(2**12) and not pro2.permits(3)
    assert rooted_diagonal_orbit(4,6)['diagonal_period']==12
    assert len(rooted_diagonal_orbit(4,6)['orbit'])==12
    assert not authenticate_prime_word(ClockTheory('finite_lcm',30),((2,2),))['source_authenticated']
    assert authenticate_prime_word(full,((2,2),))['source_authenticated']
    carry = CarryClock(4,2).certificate()
    corrupt_carry=CarryClock(4,2,2).certificate()
    assert carry['rooted_period']==8 and corrupt_carry['rooted_period']==4
    assert carry_vs_uncoupled(4,2)['uncoupled_period']==4
    carry_validation=0
    for m in range(1,13):
        for p in range(2,12):
            for c in range(0,12):
                clock=CarryClock(m,p,c)
                assert len(clock.orbit())==clock.period()
                carry_validation+=1
    triples=0
    for m in range(1,51):
        for n in divisors(m):
            for k in divisors(n):
                fnm=unique_pointed_clock_map(m,n)
                fnk=unique_pointed_clock_map(n,k)
                fmk=unique_pointed_clock_map(m,k)
                assert fmk==tuple(fnk[fnm[i]] for i in range(m))
                triples+=1
    families=0
    for a in range(1,14):
        for b in range(1,14):
            for c in range(1,6):
                stage=finite_clock_closure((a,b,c))
                assert stage['lcm']==lcm(a,b,c)
                D=stage['closed_periods']
                assert all(d in D for d in (a,b,c))
                assert all(lcm(x,y) in D for x in D for y in D)
                assert all(d in D for n in D for d in divisors(n))
                families+=1
    specimen=mutant_atoms(240)
    assert all(v==1 for v in specimen.values())
    assert first_unit_cell(specimen)==1
    count_residual=renewal_residual(specimen,240)
    assert count_residual['3']=='-1' and count_residual['35/11']=='1'
    assert not renewal_residual(calibration_atoms(240),240)
    braid=affine_counterexample(specimen)
    assert braid and braid['defect']
    res=density_residue_certificate()
    assert res['zeta_factor_at_one']=='1'
    for H in (40,80,160,240,400):
        # Observations, NOT proofs of density or prime asymptotics.
        observed=mutant_atoms(H)
        assert set(observed.values())=={1}
    return {
        'status':'exact finite and symbolic identities only; no global observation theorem from tests',
        'RH_proved':False,
        'finite_clock':{
            'observed_moduli':list(finite_family),
            'closure_lcm':finite['stage'],
            'infinite_countermodel':shadow,
            'actual_clock_probe_triples':triples,
            'independent_divisor_lcm_closed_families':families,
            'C4_times_C6_rooted_diagonal_size':12,
            'C4_times_C6_cartesian_size':24,
            'squarefree_every_prime_no_prime_square':True,
            'pro2_infinite_depth_no_odd_primes':True,
            'finite_C30_virtual_four_not_authenticated':True,
            'C4_by_C2_carry_period':carry['rooted_period'],
            'C4_by_C2_bad_carry_period':corrupt_carry['rooted_period'],
            'verified_carry_models':carry_validation,
        },
        'analytic_camouflage':{
            'replaced_generator_3':str(MUTANT_A),
            'replaced_generator_5':str(MUTANT_B),
            'rational_mutant_atom_count_240':len(specimen),
            'first_unit_cell':str(first_unit_cell(specimen)),
            'first_reconstructed_atoms':[str(x) for x in list(specimen)[:10]],
            'affine_counterexample':braid,
            'renewal_residual_at_3':count_residual['3'],
            'renewal_residual_at_35_over_11':count_residual['35/11'],
            'residue_identity':res,
            'finite_horizons':{str(H):len(mutant_atoms(H)) for H in (40,80,160,240,400)},
            'critical_strip_zero_locations_loaded':False,
        },
        'next_proof_gate':'derive prime-totality plus unbounded prime-power lift, or exact renewal, from independent source-indexed causal laws',
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    parser.add_argument('--print',action='store_true',dest='print_it')
    args=parser.parse_args()
    receipt=json.loads(json.dumps(exact_receipt()))  # canonical JSON: tuple->list
    if args.verify:
        if not RECEIPT.exists():
            raise SystemExit('Missing pinned deterministic receipt')
        actual=json.loads(RECEIPT.read_text())
        if actual!=receipt:
            raise SystemExit('Receipt mismatch: regression or source change')
        print('SOURCE_MINIMALITY_SOURCE_EXACT_VERIFIED')
    if args.print_it or not args.verify:
        print(json.dumps(receipt,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
