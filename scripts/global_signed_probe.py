#!/usr/bin/env python3
"""Deterministic exact replay for the Global Signed research round.

Hashes bind source/code; all infinite estimates retain paper authority. The
receipt verifies explicit finite calculations, not a numerical onset for pi.
"""
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
import argparse
import hashlib
import json
from math import comb
from pathlib import Path

from observational_succ.global_branch_coercivity import (
    BLOCK_LOSS, approximation_coefficient_bound, authentic_forcing_parameters,
    conditional_logarithmic_budget, local_cosine_coefficient, whole_block_parameters,
)
from observational_succ.global_prime_resonance import (
    authentic_prime_source_passport, prime_resonance_budget, verify_prime_source_passport,
)
from observational_succ.global_source_curvature import (
    changed_green_control, cubic_source_certificate, quadratic_source_certificate,
    source_window,
)
from observational_succ.pi_succ_character_intervals import fourier_squared_interval
from observational_succ.succ_internal_matrix_walk import authentic_r

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT/'research/2026-10-27/global_signed_validation/exact_receipt.json'
SOURCES = (
    'observational_succ/succ_internal_matrix_walk.py',
    'observational_succ/integer_bbp_carrier.py',
    'observational_succ/bbp_twisted_pair.py',
    'observational_succ/bbp_diophantine_coherence.py',
    'observational_succ/pi_succ_character_intervals.py',
    'observational_succ/global_branch_coercivity.py',
    'observational_succ/global_prime_resonance.py',
    'observational_succ/global_source_curvature.py',
    'tests/test_global_branch_coercivity.py',
    'tests/test_global_prime_resonance.py',
    'tests/test_global_source_curvature.py',
    'scripts/global_signed_probe.py',
)


def serialize(value):
    if isinstance(value, Q):
        return str(value)
    if is_dataclass(value):
        return serialize(asdict(value))
    if isinstance(value, dict):
        return {str(k): serialize(v) for k,v in value.items()}
    if isinstance(value, (tuple,list)):
        return [serialize(x) for x in value]
    return value


def outward_upper(value, denominator=10**12):
    return Q((value*denominator).__ceil__(), denominator)


def valuation(value, p):
    if not value:
        raise ValueError('zero has infinite valuation')
    top, bottom, result = abs(value.numerator), value.denominator, 0
    while top % p == 0:
        result += 1
        top //= p
    while bottom % p == 0:
        result -= 1
        bottom //= p
    return result


def prime_jet_holdouts():
    # Generic finite polynomial surrogate, expressly not authentic forcing.
    coefficients, B = (Q(1,3), Q(2,5), Q(-1,7)), 3
    def surrogate(n):
        return sum((c*(Q(16,8*n+2*i-7)-Q(1,8*n+2*i+1))
                    for i,c in enumerate(coefficients)), Q())
    records = []
    for p in (37,101):
        for a in (1,2,4):
            k = next(k for k in (1,3) if k*p**a % 4 == 3)
            n = (k*p**a+1)//4
            for b in range(B+1):
                difference = sum((Q((-1)**(b-j)*comb(b,j)) *
                                  (authentic_r(n+j)-surrogate(n+j))
                                  for j in range(b+1)), Q())
                scaled = p**a*difference
                residue = scaled.numerator*pow(scaled.denominator,-1,p) % p
                expected = (-1)**(b+1)*pow(2*k,-1,p) % p
                if valuation(difference,p) != -a or residue != expected:
                    raise ArithmeticError('prime-jet discriminator failed')
                records.append({'p':p,'a':a,'b':b,'n':n,'valuation':-a,
                                'scaled_residue':residue,'authentic_forcing':False})
    return records


def green_control_holdout(m=521, h=None, depth=8):
    """Finite rational tail enclosure for the full irrational changed-seed orbit."""
    h = m**3 if h is None else h
    centers, errors = [], []
    for n in range(m+1,2*m+1):
        partial = sum((Q(1,16**j)*authentic_r(n+j)
                       for j in range(1,depth+1)), Q())
        rest = authentic_r(n+depth+1)/Q(15*16**depth)
        centers.append(-partial-rest/2)
        errors.append(rest/2)
    _, square_upper = fourier_squared_interval(tuple(centers),h)
    # If center rectangle proves |mean|<=1/2, add the paid tail Lipschitz error.
    if square_upper >= Q(1,4):
        raise ArithmeticError('chosen independent Green holdout did not separate')
    error = Q(44,7)*abs(h)*sum(errors,Q())/m
    bound = Q(1,2)+error
    if m*bound >= 512:
        raise ArithmeticError('finite Green holdout failed the cubic estimate')
    return {'m':m,'h':h,'depth':depth,'same_four_poles':True,
            'zero_selector':False,'normalized_modulus_upper':outward_upper(bound),
            'tail_phase_error_upper':outward_upper(error)}


def certificate():
    moving = []
    for m,h,kind in ((64,64**3,'cubic'),(129,-(16*129**3//15),'cubic'),
                      (128,128**2,'quadratic'),(257,2*257**2,'quadratic')):
        row = (cubic_source_certificate(m,h) if kind == 'cubic'
               else quadratic_source_certificate(m,h))
        _, square = fourier_squared_interval(source_window(m),h)
        if square > (row['selected_sum_upper']/m)**2:
            raise ArithmeticError('independent signed interval exceeded theorem')
        row.update({'kind':kind,'authentic_zero_selector':True,
                    'finite_squared_modulus_upper':outward_upper(square)})
        moving.append(row)
    primes = [prime_resonance_budget(p) for p in
              (257,65537,16777289,4294967377)]
    passports = []
    for p in (257,577,1153):
        passport = authentic_prime_source_passport(p)
        if not verify_prime_source_passport(passport):
            raise ArithmeticError('source passport replay failed')
        passports.append({'prime':p,'last_source_index':passport.points[-1].source_index,
                          'initial_state':passport.initial_state,
                          'source_id':passport.source_id,'exact_replay':True})
    return serialize({
        'schema':'SUCC-global-signed-v1',
        'parent_pr':316,'parent_sha':'239df54f5f56fdaba3bf4edfc282cdcabecea3c2',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCES},
        'fixed_mode_core':{
            'block_loss':BLOCK_LOSS,
            'quiet_margin':whole_block_parameters(20000,Q(15,4096)).nonconstant_loss_lower-BLOCK_LOSS,
            'local_cosine_coefficient':local_cosine_coefficient(),
            'approximation_coefficient_at_smallest_auxiliary_index':approximation_coefficient_bound(1),
            'source_parameters':[authentic_forcing_parameters(m,h) for m,h in
                                 ((4096,1),(4103,-17),(5003,5003**2//64))],
            'sample_COMBINATORIAL_budget_NOT_certified_onset':conditional_logarithmic_budget(8**12,1,4),
            'numerical_onset_certified':False},
        'moving_band_source':moving,'prime_resonance':primes,'source_passports':passports,
        'same_forcing_green_control':changed_green_control(1024,1024**3),
        'finite_green_tail_holdout':green_control_holdout(),
        'prime_jet_mutant_discriminators':prime_jet_holdouts(),
        'status':{'stronger_logarithmic_constant_paper_proved':True,
                  'normality_proved':False,'fixed_frequency_decay_proved':False,
                  'new_asymptotic_order_proved':False,
                  'finite_receipt_is_infinite_proof':False}})


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    actions=parser.add_mutually_exclusive_group(required=True)
    actions.add_argument('--write',action='store_true')
    actions.add_argument('--verify',action='store_true')
    parser.add_argument('--receipt',type=Path,default=DEFAULT)
    args=parser.parse_args()
    content=json.dumps(certificate(),indent=2,sort_keys=True)+'\n'
    if args.write:
        args.receipt.parent.mkdir(parents=True,exist_ok=True)
        args.receipt.write_text(content)
        print(f'wrote {args.receipt}')
    else:
        if args.receipt.read_text()!=content:
            raise SystemExit('receipt mismatch: source, theorem scope, or finite result changed')
        print(f'verified byte-for-byte {args.receipt}')


if __name__=='__main__':
    main()
