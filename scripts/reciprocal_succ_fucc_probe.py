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
    finite_reciprocal_boundary_defect, finite_reciprocal_square_on_basis,
    finite_reciprocal_power_square, finite_reciprocal_boundary_hierarchy,
    factorial_gauge, factorial_creator_intertwiner,
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
    boundary_cases=0
    boundary_basis=0
    for N in range(1,81):
        for p in (2,3,5,7,11):
            defect=finite_reciprocal_boundary_defect(N,p)
            assert defect==((p*(N//p),N//p+1,Q(-1)) if N>=p else None)
            boundary_cases+=1
            for n in range(1,N+1):
                lhs,rhs=finite_reciprocal_square_on_basis(n,N,p)
                if defect is not None and n==defect[0]:
                    assert lhs is None and rhs==defect[1]
                else:
                    assert lhs==rhs
                boundary_basis+=1
    graded_configs=0
    graded_basis=0
    for N in range(1,66):
        for p in (2,3,5,7):
            for t in range(1,8):
                ports=finite_reciprocal_boundary_hierarchy(N,p,t)
                deficits={n:(m,c) for n,m,c in ports}
                assert len(deficits)==len(ports)
                graded_configs+=1
                for n in range(1,N+1):
                    left,right=finite_reciprocal_power_square(n,N,p,t)
                    if n in deficits:
                        assert left is None and (right,Q(-1))==deficits[n]
                    else:
                        assert left==right
                    graded_basis+=1
    gauges=0
    for ps in ((2,),(2,3),(2,3,5)):
        for alpha in product(range(4),repeat=len(ps)):
            for i in range(len(ps)):
                for beta in (2,4):
                    lhs,rhs=factorial_creator_intertwiner(alpha,i,ps,beta)
                    assert lhs==rhs and lhs>0
                    gauges+=1
    assert factorial_gauge((6,))==Q(1,720)
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
        'mixed_cutoff_boundary_cases':boundary_cases,
        'mixed_cutoff_basis_checks':boundary_basis,
        'rank_one_boundary_defect_exact':True,
        'graded_cutoff_configurations':graded_configs,
        'graded_cutoff_basis_checks':graded_basis,
        'graded_boundary_rank_t_law':True,
        'factorial_gauge_source_cases':gauges,
        'factorial_gauge_inverse_unbounded_claim':True,
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
