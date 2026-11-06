"""Reproducible original-source exact finite receipt; never a pi normality proof."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as Q

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('analytic_exile_receipt_source',HERE/'analytic_exile.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def make_receipt():
    out={'source':'original four signed BBP poles, zero seed','source_normality_proved':False,
         'observer_notes':'All exact rational diagnostics, neither pi digits nor a blind independent referee',
         'tested_original_epochs':{},'Ward_conditionals':{},'rational_normal_prefix_control':{},'gamma2_abel_exact':{},'analytic_boundary_ghosts':{}}
    for A in (40,96,160):
        x=m.original_phases(2*A)
        y=m.modular_original_phases(2*A)
        assert x==y
        txt='|'.join(f'{a.numerator}/{a.denominator}' for a in x[A:2*A])
        out['tested_original_epochs'][str(A)]={
            'n':A,'phase_sha256':hashlib.sha256(txt.encode()).hexdigest(),
            'odd_denominators':all(z.denominator&1 for z in x),
            'independent_modular_exact_match':True,
            'max_source_positive_denominator_bits':max(m.authentic_r(j).denominator.bit_length() for j in range(A,2*A)),
            'gamma_epoch_upper_h5':str(m.completion_epoch_coeff_upper(A,5)),
            'phase_shadow_bound_h5':str(m.finite_prefix_shadow_error(A,5))}
        out['Ward_conditionals'][str(A)]={str(h):{str(j):str(m.ward_ladder_bound(A,h,j)) for j in range(4)}
                                     for h in (1,3,5)}
    for M in (4,17,40):
        u=m.champernowne16_prefix(M)
        out['rational_normal_prefix_control'][str(M)]={
            'denominator_bits':u.denominator.bit_length(),
            'terminating_tail_after_M':(16**M*u)%1==0,
            'eventually_non_normal':True,
            'limit_normality_imported_classical_theorem':True}
    for r in (Q(1,2),Q(7,8),Q(31,32)):
        key=f'{r.numerator}/{r.denominator}'
        out['gamma2_abel_exact'][key]={
            'mass_sum_last_17':str(m.nb2_partial_mass(r,17)),
            'omitted_mass_last_17':str(m.nb2_tail_mass(r,17)),
            'mass_adds_to_one':m.nb2_partial_mass(r,17)+m.nb2_tail_mass(r,17)==1,
            'scaled_mean':str(m.gamma2_scaled_mean(r)),
            'exact_abel_cesaro':str(m.abel_cesaro_finite_identity((Q(1),Q(-1),Q(1)),r)['abel_mean']),
            'source_gamma_abel_error_upper_h3':str(m.gamma_tail_abel_boundary_upper(3,r)),
            'analytic_ward_source_error_upper_h3':str(m.analytic_ward_source_error_bound(3,r)),
        }
    for M in (1,3,8,32):
        z=Q(127,128)
        out['analytic_boundary_ghosts'][str(M)]={
            'first_M_coefficients_zero':True,
            'normalized_test_at_z_127_128':str(m.boundary_ghost(M,z)['normalized_boundary_expression']),
            'at_fixed_M_boundary_residue':1,
            'unit_phase_pair_boundary_difference':-2,
        }
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    out=HERE/'FINITE_RECEIPT.json'
    raw=json.dumps(make_receipt(),indent=2,sort_keys=True)+'\n'
    if args.verify:
        assert out.read_text()==raw,'exact finite receipt does not match replay'
        print('EXACT_SOURCE_RECEIPT_REPLAY: PASS')
    else:
        out.write_text(raw)
        print('WROTE',out)
