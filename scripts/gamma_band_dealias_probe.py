"""Band-uniform real-place de-aliasing: exact receipt plus independent probes.

Usage: python scripts/gamma_band_dealias_probe.py [--verify]
Full repository CI is not invoked. Finite numerical checks are NOT proof
certificates; every theorem bound is an exact Fraction in the source module.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.gamma_band_dealias import (  # noqa: E402
    gamma_r_band_certificate, gamma_r_jet_certificate,
    compact_mellin_band_bound, sampled_gamma_r, uniform_phase_filter,
)


def exact_receipt():
    single=gamma_r_band_certificate(F(1,2),F(1,2),F(3,2),8,
        left_steps=175,right_steps=8,taylor_order=80)
    combined=gamma_r_band_certificate(F(1,2),F(1,2),F(3,2),8,
        interleaves=2,left_steps=350,right_steps=16,taylor_order=80)
    jet=gamma_r_jet_certificate(F(1,4),F(1,2),F(3,2),8,
        collar=F(1,4),jet_order=2,left_steps=500,right_steps=18,
        taylor_order=100)
    bump=compact_mellin_band_bound(F(1,4),8,7,derivative_order=2)
    assert combined['total_upper'] < F(1,10**7)
    assert combined['alias_error_upper'] < single['alias_error_upper']
    assert combined['total_upper'] < single['total_upper']
    assert combined['source_event_count'] > single['source_event_count']
    assert all(uniform_phase_filter(5,k)==int(k%5==0) for k in range(-20,21))
    return {
        'schema':'SUCC_GAMMA_BAND_DEALIAS_v1',
        'status':'CLASSICAL_ANALYTIC_THEOREM_EXACT_RATIONAL_SOURCE_BOUND',
        'source':'GAUSSIAN_TATE_REAL_PLACE_PI_NORMALIZED_S_HALF',
        'h':'1/2', 'subclocks':2, 'effective_mesh':'1/4',
        'band':{'sigma_min':'1/2','sigma_max':'3/2','imag_radius':'8'},
        'first_alias_before':'8*pi', 'first_alias_after':'16*pi',
        'event_count_before':single['source_event_count'],
        'event_count_after':combined['source_event_count'],
        'alias_upper_before':str(single['alias_error_upper']),
        'alias_upper_after':str(combined['alias_error_upper']),
        'total_rational_upper_after':str(combined['total_upper']),
        'rigorously_total_error_lt_1e_minus_7':True,
        'Cauchy_second_jet_upper':str(jet['jet_error_upper']),
        'compact_Mellin_W2_alias_upper_conditional_norm_7':str(bump['bound']),
        'q5_character_filter': [uniform_phase_filter(5,k) for k in range(11)],
        'alias_horizon_proved_sharp_in_absolute_norm':True,
        'full_Tate_adeles_constructed':False,
        'prime_Euler_source_constructed':False,
        'Weil_sign_proved':False,
        'RH_proved':False,
    }


def numerical_diagnostics():
    import mpmath as mp
    with mp.workdps(70):
        z=mp.mpc('.5','6')
        a=sampled_gamma_r(z,F(1,2),left_steps=175,right_steps=8,dps=70)
        b=sampled_gamma_r(z,F(1,2),interleaves=2,
                          left_steps=350,right_steps=16,dps=70)
        c=gamma_r_band_certificate(F(1,2),F(1,2),F(3,2),8,
                           interleaves=2,left_steps=350,right_steps=16,
                           taylor_order=80)
        B=mp.mpf(c['total_upper'].numerator)/c['total_upper'].denominator
        assert b['observed_absolute_error'] < B
        assert b['coherent_chart_disagreement'] < mp.mpf('1e-60')
        assert b['observed_absolute_error'] < a['observed_absolute_error']
        old_alias=mp.mpc(1,8*mp.pi)
        bad=sampled_gamma_r(old_alias,F(1,2),left_steps=400,right_steps=20,dps=70)
        good=sampled_gamma_r(old_alias,F(1,2),interleaves=2,
                             left_steps=800,right_steps=40,dps=70)
        assert abs(bad['refined'])>mp.mpf('.99')
        assert abs(good['refined'])<mp.mpf('1e-6')
        return {
            'single_observed_error':mp.nstr(a['observed_absolute_error'],10),
            'interleaved_observed_error':mp.nstr(b['observed_absolute_error'],10),
            'interleaved_rational_bound_decimal_readout':mp.nstr(B,10),
            'old_alias_magnitude_unshifted':mp.nstr(abs(bad['refined']),10),
            'old_alias_magnitude_after_interleaving':mp.nstr(abs(good['refined']),10),
            'comparison_note':'NUMERIC DIAGNOSTICS, NOT THE PROOF',
        }


if __name__=='__main__':
    args=sys.argv[1:]
    if args not in ([],['--verify']):
        raise SystemExit('usage: python scripts/gamma_band_dealias_probe.py [--verify]')
    receipt=exact_receipt()
    if args==['--verify']:
        path=Path(__file__).resolve().parents[1]/'research/2026-10-16/GAMMA_BAND_DEALIAS_RECEIPT.json'
        if json.loads(path.read_text(encoding='utf-8'))!=receipt:
            raise SystemExit('Gamma band de-alias source receipt diverged')
    diagnostics=numerical_diagnostics()
    if args==['--verify']:
        print('GAMMA_BAND_DEALIAS exact rational and independent numerical controls: OK')
    else:
        print(json.dumps({'receipt':receipt,'diagnostics':diagnostics},indent=2,sort_keys=True))