"""Reproducible Git-blob-pinned exact SUCC/FUCC reciprocity and Pascal receipt."""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

from observational_succ.reciprocal_succ_fucc import (
    reciprocal_braid, mixed_radix, finite_stationarity,
    weighted_affine_diamond, pascal_prime_rank, direct_prime_rank,
    gibbs_rank_nonprojective,
)


def _blob(path):
    data=path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()


def main():
    root=Path(__file__).resolve().parents[1]
    reciprocal=0
    for p in (2,3,5,7,11,17):
        for n in range(1,311):
            a,b=reciprocal_braid(n,p)
            assert a==b
            reciprocal+=1
    clocks=0
    for p,q in product((2,3,5,7),repeat=2):
        for n in range(1,161):
            (m,s,r),(mm,t,u)=mixed_radix(n,p,q)
            assert m==mm and p*s+r==q*t+u
            clocks+=1
    generators=0
    for N in (4,9,18,32):
        for beta in (2,3,4):
            report=finite_stationarity(N,(2,3,5),beta)
            assert not report['edge_fails']
            assert not any(report['row_sums']+report['pi_L'])
            generators+=1
    flat=0
    for beta in (2,3,4):
        for p in (2,3,5,7):
            for n in range(1,36):
                a,b,d=weighted_affine_diamond(n,p,beta)
                assert a==b==d
                flat+=1
    ranks=0
    for ps in ((2,),(2,3),(2,3,5)):
        for k in range(8):
            for beta in (2,4):
                assert pascal_prime_rank(ps,k,beta)==direct_prime_rank(ps,k,beta)
                ranks+=1
    direct,cotrans=gibbs_rank_nonprojective((2,3),2)
    assert direct!=cotrans and cotrans>direct
    receipt={
        'research':'SUCC_FUCC_RECIPROCAL_PASCAL_BRIDGE_2026_10_22',
        'status':'PAPER_PROOF_AND_EXACT_FINITE_CALIBRATION_NOT_LEAN_CERTIFIED',
        'source':'positive integers, genuine rational primes, zeta Gibbs beta>1',
        'reciprocal_braid_input_cases':reciprocal,
        'mixed_radix_input_cases':clocks,
        'exact_finite_generator_checks':generators,
        'flat_weighted_diamond_cases':flat,
        'divided_power_rank_source_cases':ranks,
        'projectivity_rank1_source_2_3_beta2':str(direct),
        'projectivity_rank2_cotransport_2_3_beta2':str(cotrans),
        'projectivity_false_equivalence_refuted':True,
        'unweighted_shift_p_clock_with_extra_phase_required':True,
        'state_dependent_mirror_anti_homomorphism':True,
        'physical_reverse_causality_claimed':False,
        'intrinsic_geometric_holography_claimed':False,
        'signed_Weil_positivity_proved':False,
        'RH_proved':False,
        'source_module_git_blob':_blob(root/'observational_succ/reciprocal_succ_fucc.py'),
        'tests_git_blob':_blob(root/'tests/test_reciprocal_succ_fucc.py'),
    }
    print(json.dumps(receipt,sort_keys=True,indent=2))


if __name__=='__main__':main()
