"""Independent deterministic finite SUCC/FUCC IMS and authentic-source cutoff probe."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from observational_succ.source_covariant_ims import (
    FiniteToySource, finite_ims, first_prime_window_frequency_packet,
    authenticated_first_prime_window_packet, prime_power_parent,
    gamma_prefix_multiplier, affine_succ_fucc_square,
)


def toy():
    n=5
    jump=tuple(tuple(F(0) if i==j else F(1,1+abs(i-j)) for j in range(n)) for i in range(n))
    source=FiniteToySource(jump,((1,F(1,2)),(2,F(1,3))),F(7,9),
                           tuple(F(i+1) for i in range(n)),
                           tuple(F((-1)**i) for i in range(n)))
    pieces=((F(3,5),F(4,5)),(F(4,5),F(3,5)),(F(1),F(0)),
            (F(0),F(1)),(F(-3,5),F(4,5)))
    charts=tuple(tuple(p[i] for p in pieces) for i in (0,1))
    return source,(F(2),F(-1),F(3),F(0),F(4)),charts


def emit(with_source=False):
    src,f,charts=toy()
    v=finite_ims(src,f,charts)
    ans={"kind":"SUCC_FUCC_SOURCE_COVARIANT_IMS_V1",
         "finite_signed_IMS":{k: str(value) if isinstance(value,F) else value for k,value in v.items()},
         "finite_band":first_prime_window_frequency_packet(),
         "Gamma_prefix_at_9":{k:str(value) if isinstance(value,F) else value
                              for k,value in gamma_prefix_multiplier(F(9)).items()},
         "affine_square":affine_succ_fucc_square(8,3),
         "fake_independent_6_rejected": prime_power_parent(6) is None,
         "analytic_source_equality_claimed_by_discrete_toy":False,
         "RH_proved":False}
    if with_source:
        ans['pinned_original_first_window_source']=authenticated_first_prime_window_packet()
    return ans


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',action='store_true')
    ap.add_argument('--verify',action='store_true')
    args=ap.parse_args()
    ans=emit(args.source)
    if args.verify:
        assert ans['finite_signed_IMS']['actual']==ans['finite_signed_IMS']['reconstructed']
        assert ans['fake_independent_6_rejected']
        assert ans['finite_band']['band_radius']==2**24
        if args.source:
            assert ans['pinned_original_first_window_source']['source_gate_verified']
    print(json.dumps(ans,sort_keys=True,indent=2,default=str))

if __name__=='__main__': main()
