#!/usr/bin/env python3
"""Replay CERTIFIED exact rational Suzuki prime-source enclosures, not full Weil.

No zeta zero input. Logarithms and inverse square-roots are enclosed via
exact Fraction/isinteger-square-root arithmetic. mpmath is not used in
the proof-bearing module; optional tests compare independent mpmath
approximations as an AFTER-THE-FACT calibration only.

python scripts/prime_source_certificates_probe.py --output /tmp/prime-source.json
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as Q
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from observational_succ.source_prime_certificates import (
    CertifiedPrimeSource,rational_log_integer,rational_inverse_sqrt,
    finite_prime_horizon,prime_delta_at_fake_six,
)
from observational_succ.gamma_interferometer import GammaInterferometer
from observational_succ.observer_reflection import rational_gram_certificate


def _interval(i):
    return {"lower":str(i.lower),"upper":str(i.upper),
            "strictly_negative":bool(i.upper<0),
            "strictly_positive":bool(i.lower>0),
            "rational_width":str(i.upper-i.lower)}


def run(*,terms=30,places=25):
    if type(terms) is not int or not 8<=terms<=100:
        raise ValueError("Integer log terms in 8..100 required")
    if type(places) is not int or not 10<=places<=35:
        raise ValueError("Integer sqrt places in 10..35 required")
    horizon=27
    genuine=CertifiedPrimeSource.genuine(
        horizon,log_terms=terms,sqrt_places=places)
    source={n:1 for n in range(1,horizon+1)}
    source[6]=2
    fake=CertifiedPrimeSource(
        GammaInterferometer.from_prefix(source,horizon),
        log_terms=terms,sqrt_places=places)
    t=Q(9,5)
    true_wave=genuine.prime_psi(t)
    fake_wave=fake.prime_psi(t)
    anomaly=fake_wave-true_wave
    strict=prime_delta_at_fake_six(t=t,log_terms=terms,
                                   sqrt_places=places,horizon=horizon)
    if not strict.upper<0 or not anomaly.upper<0:
        raise ArithmeticError("Fake source must have certified negative delta")
    if not anomaly.intersects(strict):
        raise ArithmeticError("Separate rational source intervals do not overlap")

    sample=genuine.prime_screw(Q(1),Q(9,5))
    # This certificate is ONLY about a component; it is not RH evidence.
    gram=rational_gram_certificate(
        (Q(1),Q(9,5)),(Q(1),Q(1)),
        genuine.oracle,provenance="prime component ONLY, Gamma not supplied")

    return {
        "status":"CERTIFIED_FINITE_SOURCE_PRIME_TRANSPORT",
        "no_zeta_zero_input":True,
        "exact_rational_enclosures":True,
        "arithmetical_wavefront_t":"9/5",
        "horizon":horizon,
        "required_horizon":finite_prime_horizon((Q(9,5),)),
        "source_true":genuine.provenance(),
        "source_fake":fake.provenance(),
        "log6_enclosure":_interval(rational_log_integer(6,terms=terms)),
        "inverse_sqrt6_enclosure":_interval(
            rational_inverse_sqrt(6,places=places)),
        "prime_true_at_t":_interval(true_wave),
        "prime_fake_at_t":_interval(fake_wave),
        "prime_fake_minus_true":_interval(anomaly),
        "certified_strict_fake6_anomaly":_interval(strict),
        "prime_only_K_1_1p8":_interval(sample),
        "prime_only_gram":{
            "status":gram.result,
            "oracle_provenance":gram.oracle_provenance,
            "enclosure":_interval(gram.enclosure),
            "RH_counterexample_proved":False,
        },
        "Gamma_pole_interval_completed":False,
        "full_Weil_PSD_proved":False,
        "RH_proved":False,
        "next_gate":"certified Gamma+poles oracle followed by exact completed-source Gram",
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--terms",type=int,default=30)
    p.add_argument("--places",type=int,default=25)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    result=run(terms=a.terms,places=a.places)
    blob=json.dumps(result,sort_keys=True,indent=2)+"\n"
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(blob,encoding="utf-8")
    else:
        print(blob,end="")


if __name__=="__main__":
    main()
