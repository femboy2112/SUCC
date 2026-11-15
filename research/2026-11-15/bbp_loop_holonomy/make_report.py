"""Generate self-contained rational finite BBP return-loop certificates."""
from __future__ import annotations
import json
import hashlib
from fractions import Fraction
from math import sin,pi

from loop_probe import (
    source_states, lifted_source_states, modular_source_states,
    circle_pulse_certificate, clock_jet, predicted_jet,
    source_crt_passport, forcing,
)


def as_fraction(v: Fraction) -> str:
    return str(v.numerator) + '/' + str(v.denominator)


def pulse(k:int, n:int) -> dict:
    q=16**k
    reduced=source_states(n+q)
    lift=lifted_source_states(n+q)
    modular=modular_source_states(n+q,16*q)
    cert=circle_pulse_certificate(reduced,q,n,18)
    source_jet=clock_jet(modular,k,n)
    assert source_jet==predicted_jet(n)
    assert cert.passed and cert.distance_lower>Fraction(1,17)
    passports=[]
    for m in (n,n+q):
        p=source_crt_passport(m,lift[m])
        passports.append({
            'n':m,
            'odd_denominator_bits':p['odd_denominator'].bit_length(),
            'odd_prime_factors':len(p['local_characters']),
            'crt_integer_winding':p['crt_reconstruction_integer'],
            'source_integer_winding_decimal_digits':len(str(abs(p['integer_winding']))),
            'crt_exact_reconstruction':True,
            'source_full_rational_sha256':hashlib.sha256(str(lift[m]).encode()).hexdigest(),
        })
    d=cert.distance_lower
    return {
        'k':k, 'q':q, 'n':n,
        'carrier_mod_q_returns':(modular[n+q]-modular[n])%q ==0,
        'jet_mod16':source_jet,
        'jet_is_nonzero_unit':bool(source_jet%2),
        'source_sign_sector':'omega^3' if source_jet==3 else '-omega^3',
        'circle_distance_lower_exact':as_fraction(d),
        'circle_distance_lower_decimal_annotation':format(float(d),'.12f'),
        'original_green_difference_interval_width_exact':as_fraction(cert.interval_width),
        'phase_chord_energy_lower_decimal_annotation':format(4*sin(pi*float(d))**2,'.12f'),
        'beats_universal_1_over_17':bool(d>Fraction(1,17)),
        'odd_crt_passports':passports,
    }


def make():
    source_fingerprint='\n'.join(str(forcing(n)) for n in range(1,33))
    mutated=modular_source_states(18,256,leading=3)
    original=modular_source_states(18,256)
    return {
      'scope':'Finite source-certified BBP return-loop/2-adic jet; no infinite real normality assertion',
      'original_zero_seed':True,
      'original_source_sha256_of_r1_through_r32':hashlib.sha256(source_fingerprint.encode()).hexdigest(),
      'phase_floor_symbolic':'4*sin(pi/17)^2',
      'phase_floor_decimal_annotation':format(4*sin(pi/17)**2,'.14f'),
      'tested_source_loops':[pulse(1,2),pulse(2,3)],
      'mutation_control':{
          'pole_changed':'4/(8n-7) to 3/(8n-7)',
          'original_return_after_16_mod16':original[16]%16,
          'mutated_return_after_16_mod16':mutated[16]%16,
          'mutant_does_not_preserve_original_loop':mutated[16]%16!=original[16]%16,
      },
      'normality_status':'OPEN',
      'source_scope':'Authenticated four-pole rational BBP forcing, not a digit fixture',
    }

if __name__=='__main__':
    print(json.dumps(make(),indent=2,sort_keys=True))
