"""Source-blob-pinned receipt for Jacobi boundary spectrum and hidden round trips.

PYTHONPATH=. python scripts/spectral_boundary_rigidity_probe.py
The universal inverse spectral theorem is paper mathematics, not a test result.
"""
from __future__ import annotations
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from observational_succ.spectral_boundary_rigidity import (
    chain_response, response_at, round_trip_new_depth, chain_moments,
    interpolate_response, recover_positive_chain,
    finite_response_identity, approximate_hidden_mode_pair,
)
from observational_succ.boundary_realization_selection import (
    FiniteNetwork, boundary_response,
)


def blob(path):
    b=path.read_bytes()
    return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()


def main():
    root=Path(__file__).resolve().parents[1]
    source=(F(2),F(3),F(5))
    resp=chain_response(source)
    freqs=tuple(F(i) for i in range(1,8))
    samples=tuple((s,response_at(resp,s)) for s in freqs)
    interpolated=interpolate_response(samples,3)
    assert interpolated==resp
    assert recover_positive_chain(interpolated)==source
    assert finite_response_identity(resp,interpolated,freqs,3)
    network=FiniteNetwork(4,(0,3),((0,1,F(2)),(1,2,F(3)),(2,3,F(5))),
                         ((1,F(1)),(2,F(1))))
    for s in freqs+(F(0),):
        assert response_at(resp,s)==boundary_response(network,s)[0][0]
    delays={}
    for g,new in (((F(1),F(1)),F(3)),
                  ((F(2),F(3),F(5)),F(7)),
                  ((F(2),F(3),F(5),F(7)),F(11))):
        r=round_trip_new_depth(g,new)
        delays[str(r["depth"])]={
            "first_different_moment":r["first_distinguishing_moment"],
            "exact_moment_jump":str(r["difference"]),
            "all_earlier_moments_equal":r["moments_before"][:2*r["depth"]]==
                                        r["moments_after"][:2*r["depth"]],
        }
    short,long=approximate_hidden_mode_pair(F(1,1000))
    small_gap=abs(response_at(long,1)-response_at(short,1))
    assert F()<small_gap<F(1,1000000)
    report={
        "research":"SUCC_SPECTRAL_BOUNDARY_SOURCE_RIGIDITY_2026_10_22",
        "scope":"positive finite RC paths, fixed unit internal capacitances, exact Laplace DtN",
        "mathematical_prior":"finite Jacobi/Weyl m-function inverse spectral theory; minimal transfer realizations",
        "academic_novelty_claimed":False,
        "physical_observations_performed":False,
        "alpha_derived_from_SUCC":False,
        "global_gravitational_geometry_identified":False,
        "RH_proved":False,
        "signed_Weil_positivity_proved":False,
        "finite_chain_example_conductances":[str(x) for x in source],
        "finite_chain_example_boundary_numerator":[str(x) for x in resp[0]],
        "finite_chain_example_boundary_denominator":[str(x) for x in resp[1]],
        "finite_chain_example_static_response":str(response_at(resp,0)),
        "exact_frequency_samples_for_max_order_3":[[str(s),str(y)] for s,y in samples],
        "complete_response_recovered_from_seven_samples":True,
        "source_conductances_reconstructed":[str(x) for x in recover_positive_chain(interpolated)],
        "spectral_new_layer_first_return_moments":delays,
        "weak_extra_mode_frequency_1_exact_gap":str(small_gap),
        "weak_extra_mode_gap_below_one_millionth":True,
        "dark_mode_counterexample_preserved_in_tests":True,
        "2d_plus_1_identity_theorem_scope":"proper rational responses of degree at most d, exact distinct nonpole samples",
        "source_module_git_blob":blob(root/'observational_succ/spectral_boundary_rigidity.py'),
        "test_module_git_blob":blob(root/'tests/test_spectral_boundary_rigidity.py'),
    }
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__=="__main__":main()
