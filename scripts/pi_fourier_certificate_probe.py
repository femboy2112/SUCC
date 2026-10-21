#!/usr/bin/env python3
"""Small finite Fourier certificates; no normality or limit assertion."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.pi_fourier_certificate import (
    pi_orbit_fourier_enclosure, rational_orbit_fourier_enclosure,
)


def down(value, grid=10**18):
    return Q((value*grid)//1,grid)


def up(value, grid=10**18):
    return -down(-value,grid)


def pack(result):
    return {
        'source':result.source,'base':result.base,'frequency':result.frequency,
        'depth':result.depth,'polygon_steps':result.polygon.steps,
        'precision_bits':result.polygon.precision_bits,'taylor_order':result.taylor_order,
        'source_midpoint':str(result.source_midpoint),
        'actual_polygon_width':str(result.polygon.upper-result.polygon.lower),
        'real':[str(down(result.real[0])),str(up(result.real[1]))],
        'imag':[str(down(result.imag[0])),str(up(result.imag[1]))],
        'squared_modulus':[str(down(result.squared_modulus[0])),str(up(result.squared_modulus[1]))],
        'source_transport_error_upper':str(up(result.source_transport_error,10**30)),
        'angle_error_upper':str(up(result.angle_rounding_error,10**30)),
        'cosine_taylor_error_upper':str(up(result.cosine_taylor_error,10**30)),
        'sine_taylor_error_upper':str(up(result.sine_taylor_error,10**30)),
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    pi_cases=[pi_orbit_fourier_enclosure(2,1,n) for n in (8,16,32)]
    decisive=pi_cases[-1]
    assert Q(1,25)<decisive.squared_modulus[0]<=decisive.squared_modulus[1]<Q(1,20)
    rational_cases=[rational_orbit_fourier_enclosure(x,2,1,32)
                    for x in (Q(0),Q(1,3),Q(1,4))]
    coarse=pi_orbit_fourier_enclosure(2,1,32,polygon_steps=2,precision_bits=16)
    assert coarse.squared_modulus==(Q(0),Q(1))
    paths=['observational_succ/pi_fourier_certificate.py',
           'observational_succ/pi_polygon_normality.py',
           'tests/test_pi_fourier_certificate.py',
           'scripts/pi_fourier_certificate_probe.py']
    receipt={
        'title':'Finite polygon-source Fourier enclosure', 'date':'2026-10-21',
        'pi_cases':list(map(pack,pi_cases)),
        'rational_nonnormal_controls':list(map(pack,rational_cases)),
        'underresolved_control':pack(coarse),
        'certified_finite_statement':'1/25 < |(1/32) sum_(j=0)^31 exp(2*pi*i*2^j*pi)|^2 < 1/20',
        'pi_normality_proved':False,'asymptotic_cancellation_proved':False,
        'formal_kernel_verified':False,
        'independent_holdout':'tests use Machin source and nested dyadic roots, without the Fourier Taylor implementation',
        'sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(receipt['certified_finite_statement'])


if __name__=='__main__':
    main()
