"""Source-typed SUCC×FUCC Tate–Mellin exact receipt and numeric holdouts.

Do NOT treat mpmath holdouts as interval calculations or RH-sign evidence.
Run from repository root after installation or with PYTHONPATH=.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from fractions import Fraction as F

from observational_succ.tate_mellin_prime_transport import (
    completed_mellin_band_certificate,prime_euler_certificate,
    finite_hyperbolic_succ_fucc_certificate,euler_vs_succ_carrier_certificate,
    finite_prime_jet_cumulants,compact_weil_prime_jet_source,
    prime_escape_certificate,finite_hyperbolic_prime_coupling,
    mutant_source_discriminator,archimedean_parity_and_pole_firewall,
    finite_mellin_gram_transport_certificate,
    finite_completed_characteristic,completed_characteristic_oracle,
    natural_succ_characteristic,finite_euler_characteristic,
)


def exact_receipt():
    n=0
    c=completed_mellin_band_certificate(n,F(1,120),-840,840,F(2),97,5,500)
    prime=prime_euler_certificate(97,5,2)
    natural=finite_hyperbolic_succ_fucc_certificate(200,2)
    bridge=euler_vs_succ_carrier_certificate(200,2,97,5)
    cumulants=finite_prime_jet_cumulants(7,2,4)
    compact=compact_weil_prime_jet_source(36)
    escape=prime_escape_certificate(97,5)
    coupling=finite_hyperbolic_prime_coupling(6,2,2,3)
    mutant=mutant_source_discriminator(3,2)
    parity=archimedean_parity_and_pole_firewall(0)
    gram=finite_mellin_gram_transport_certificate(
            (F(0),F(1,2),F(1),F(2)),c['completed_dirac_error_upper'],F(2))
    return {
        'schema':'SUCC_TATE_MELLIN_PRIME_FUCC_V1',
        'status':'CERTIFIED_POSITIVE_SOURCE_RE_GT_ONE_NOT_SIGNED_WEIL',
        'parent':{'factorial':'draft PR145','dirac':'draft PR141','band':'draft PR142'},
        'positive_completed_source':{
            'shape_a':1,'sigma':2,'gamma':'pi^(-s/2)Gamma(s/2)',
            'Euler':'actual independent prime geometric valuations',
            'characteristic':'Gamma_R(sigma+2it)zeta(sigma+2it)/(Gamma_R(sigma)zeta(sigma))',
        },
        'finite_gamma_and_euler':{
            'mesh':'1/120','left':-840,'right':840,'event_count':1681,
            'Beta_rate_cutoff':500,'prime_cutoff':97,'prime_exponent_cutoff':5,
            'prime_count':prime['prime_count'],
            'Dirac_uniform_error':str(c['dirac_gamma_error']),
            'Beta_uniform_error':str(c['beta_gamma_error']),
            'Euler_uniform_error':str(c['euler_prime_error']),
            'Dirac_Beta_comparison_upper':str(c['dirac_vs_beta_uniform_error_upper']),
            'completed_Dirac_uniform_upper':str(c['completed_dirac_error_upper']),
            'completed_Beta_uniform_upper':str(c['completed_beta_error_upper']),
            'bounds_exact_Fraction':True,
            'finite_weight_numerical_readouts_directed_rounding':False,
        },
        'finite_SUCC_FUCC_hyperbolic':{
            'H':200,'number_of_natural_states':natural['natural_address_count'],
            'number_of_valuation_vectors':natural['unique_valuation_vector_count'],
            'exact_finite_Dirichlet_partition':str(natural['SUCC_Dirichlet_partition_exact']),
            'rectangular_box_not_hyperbolic_cutoff':True,
            'rational_natural_vs_Euler_upper':str(bridge['uniform_zeta_source_discrepancy_upper']),
        },
        'prime_jets':{
            'authentic_prime_labels':list(prime['prime_labels']),
            'p2_first_log_coefficient':str(cumulants['rows'][0]['coefficient_of_log_prime']),
            'p2_log_variance_coefficient':str(cumulants['rows'][0]['coefficient_of_log_prime_squared_in_variance']),
            'compact_horizon':36,'compact_prime_power_impulse_count':compact['count'],
            'genuine_log_2_at_4':next(x['half_density_weight'] for x in compact['prime_power_impulses'] if x['n']==4),
            'fake_composite_6_excluded':True,
        },
        'finite_world_boundary':{
            'sigma_range':'0<sigma<=1',
            'P':97,'threshold':5,
            'rational_untruncated_mass_escape_upper':str(escape['all_sigma_in_open_0_to_1_untruncated_mass_upper']),
            'rational_finite_geometric_mass_escape_upper':str(escape['all_sigma_in_open_0_to_1_finite_geometric_mass_upper']),
            'sigma2_H6_covariance_p2_p3':str(coupling['finite_SUCC_coupling_covariance']),
            'full_sigma_gt1_prime_covariance':0,
            'no_probability_weak_limit_on_finite_log_addresses':True,
        },
        'adversarial_source_firewalls':{
            'fake_six_first_wrong_n':mutant['fake_six_first_difference'],
            'fake_six_coefficient_at_6':str(mutant['fake_six_mutant_coefficient_at_6']),
            'wrong_alpha2_first_wrong_n':mutant['changed_two_first_difference'],
            'wrong_alpha2_coefficient_at_2':str(mutant['changed_two_mutant_coefficient_at_2']),
            'both_mutants_preserve_probability_positivity':True,
            'correct_even_pi_second_moment':str(parity['even_pi_scaled_second_moment']),
            'wrong_odd_pi_second_moment':str(parity['odd_pi_scaled_second_moment']),
            'wrong_2pi_second_moment':str(parity['wrong_2pi_scaled_second_moment']),
            'standalone_xi_pole_scalar_modulus_squared':10,
            'finite_positive_gram_dimension':gram['dimension'],
            'finite_positive_gram_operator_error_upper':str(gram['operator_error_upper']),
            'signed_Weil_sign_identified':False,'RH_proved':False,
        },
    }


def numerical_holdout():
    """Two source constructions against an independent Gamma/zeta evaluation."""
    import mpmath as mp
    with mp.workdps(75):
        c=completed_mellin_band_certificate(0,F(1,120),-840,840,F(2),97,5,500)
        to_mp=lambda q: mp.mpf(q.numerator)/q.denominator
        errors=[]
        for t in (mp.mpf('0.375'),mp.mpf('1.25'),mp.mpf('1.875')):
            target=completed_characteristic_oracle(0,t,dps=75)
            beta=finite_completed_characteristic(0,t,chart='beta',cutoff=500,
                         prime_cutoff=97,max_exponent=5,dps=75)
            dirac=finite_completed_characteristic(0,t,chart='dirac',
                         mesh=F(1,120),left=-840,right=840,
                         prime_cutoff=97,max_exponent=5,dps=75)
            if not (abs(beta-target)<to_mp(c['completed_beta_error_upper']) and
                    abs(dirac-target)<to_mp(c['completed_dirac_error_upper']) and
                    abs(beta-dirac)<to_mp(c['dirac_vs_beta_uniform_error_upper'])):
                raise ArithmeticError('fresh Gamma Euler numerical holdout failed certificate')
            errors.append({'t':mp.nstr(t,8),'beta_error':mp.nstr(abs(beta-target),18),
                           'dirac_error':mp.nstr(abs(dirac-target),18)})
        # Independent direct Mellin integral at a point, no Gamma oracle used.
        t=mp.mpf('0.625')
        s=mp.mpc(2,2*t)
        integrand=lambda x: mp.exp(-mp.pi*x*x)*mp.power(x,s-1)
        direct=2*mp.quad(integrand,[0,1,mp.inf])
        gamma_formula=mp.power(mp.pi,-s/2)*mp.gamma(s/2)
        delta=abs(direct-gamma_formula)
        if delta>mp.mpf('1e-50'):
            raise ArithmeticError('Tate Gaussian direct integral did not match Gamma_R')
        bnd=euler_vs_succ_carrier_certificate(200,2,97,5)
        t=mp.mpf('0.875')
        nat=natural_succ_characteristic(200,2,t,dps=75)
        fucc=finite_euler_characteristic(97,5,2,t,dps=75)
        if abs(nat-fucc) >= to_mp(bnd['uniform_zeta_source_discrepancy_upper']):
            raise ArithmeticError('natural/FUCC finite horizon triangle failed')
        return {'source_holdouts':errors,
                'real_Gaussian_integral_difference':mp.nstr(delta,18),
                'finite_natural_vs_prime_product_difference':mp.nstr(abs(nat-fucc),18),
                'numerical_interval_certificate':False}


def main(args):
    snapshot=exact_receipt()
    receipt=Path(__file__).resolve().parents[1]/'research/2026-10-16/TATE_MELLIN_PRIME_TRANSPORT_RECEIPT.json'
    if args==['--verify']:
        expected=json.loads(receipt.read_text(encoding='utf-8'))
        if snapshot!=expected:
            raise SystemExit('TMF exact source receipt does not match original arithmetic')
        diag=numerical_holdout()
        print('TMF exact rational source receipt VERIFIED')
        print('TMF independent numerical Gamma, Euler, and SUCC/FUCC holdouts PASSED')
        print(json.dumps(diag,sort_keys=True))
        return 0
    if not args:
        print(json.dumps(snapshot,indent=2,sort_keys=True))
        return 0
    raise SystemExit('usage: python scripts/tate_mellin_prime_transport_probe.py [--verify]')

if __name__=='__main__':
    raise SystemExit(main(sys.argv[1:]))
