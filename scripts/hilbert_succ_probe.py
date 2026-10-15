"""Deterministic finite Hilbert/measure-Zeno experiment; optional authentic Weil gate."""
from __future__ import annotations
import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.hilbert_succ import (
    hilbert_adjacency_receipt, hilbert_inner_product,
    hilbert_refinement, hilbert_square_midpoint_average,
    diagonal_zeno_mutant, monomial_strata, hilbert_dimension_obstruction,
    genuine_suzuki_hilbert_scan, source_scan_locality_check,
    original_weil_measure_strata, PINNED_WEIL_BLOB, PARENT_MAIN_SHA,
)


def serial(obj):
    if isinstance(obj,Q):return str(obj)
    if isinstance(obj,dict):return {k:serial(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):return [serial(v) for v in obj]
    if type(obj) is bool or type(obj) is int or obj is None or type(obj) is str:
        return obj
    raise TypeError(f"nonexact/malformed scientific receipt field {type(obj)}")


def receipt():
    path_summary=[]
    for level in range(1,6):
        path_summary.append(hilbert_adjacency_receipt(level))
    source_poly=[]
    for level in range(0,5):
        n=1<<level
        avg=hilbert_square_midpoint_average(level,lambda x,y:x*x+y*y)
        source_poly.append({'level':level,'signed_error':Q(2,3)-avg,
                            'exact_expected_error':Q(1,6*n*n)})
    parent=(Q(3,7),Q(-1,7),Q(5,11),Q(0))
    fine=hilbert_refinement(1,parent)
    return serial({
        'experiment':'HILBERT_SUCC_SOURCE_STRATA_2026_10_14',
        'integrated_parent_main':PARENT_MAIN_SHA,
        'original_suzuki_source_git_blob':PINNED_WEIL_BLOB,
        'mathematical_hilbert_paths':path_summary,
        'dyadic_quadrature':source_poly,
        'finite_L2_isometric_refinement':{'coarse':hilbert_inner_product(1,parent,parent),
                                        'fine':hilbert_inner_product(2,fine,fine)},
        'bulk_contact_graph_controls':monomial_strata(1,1,Q(1,2)),
        'noncommuting_resolution_limits':[diagonal_zeno_mutant(k) for k in range(1,6)],
        'ambient_dimension_obstructions':[hilbert_dimension_obstruction(d,Q(2,d))
                                          for d in (2,3,5,10)],
        'source_weil_full_operator_is_signed':True,
        'original_suzuki_parent_must_be_authenticated_by_remote_CI':True,
        'source_measure_channels_not_flattened_to_bulk':True,
        'new_original_completed_weil_PSD_proof':False,
        'RH_PROVED':False,
        'physical_infinite_traversal':False,
        'test_count_is_not_theorem':True,
    })


def source_probe():
    """Fails closed without ORIGINAL pinned source; use inside integrated checkout CI."""
    measure=original_weil_measure_strata(Q(1,2))
    stage=genuine_suzuki_hilbert_scan(Q(1,2),3,2)
    local=source_scan_locality_check(stage)
    if not local['all_consecutive_original_source_readouts_lipschitz_certified']:
        raise RuntimeError('source Hilbert locality certificate failed')
    if [j['n'] for j in measure['prime_shift_graphs']]!=[2]:
        raise RuntimeError('wrong source-prime wavefront')
    return serial({'original_source':stage.source,
                   'original_parent_sha':stage.source_blob,
                   'signed_kernel':stage.signed_kernel,
                   'global_operator_norm_error':stage.source_operator_norm_error,
                   'hilbert_measurement_count':len(stage.hilbert_matrix_cells),
                   'hilbert_locality_budget':local['declared_bound'],
                   'hilbert_max_source_jump':local['maximum_exact_difference'],
                   'primitive_place_list':[j['n'] for j in measure['prime_shift_graphs']],
                   'positive_bulk_and_negative_contact_both_retained':True,
                   'RH_PROVED':False})


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--verify',type=Path)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--source-probe',action='store_true')
    args=ap.parse_args()
    if args.source_probe:
        print(json.dumps(source_probe(),indent=2,sort_keys=True))
        return
    report=receipt()
    txt=json.dumps(report,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
    if args.verify:
        if json.loads(args.verify.read_text(encoding='utf-8'))!=report:
            raise SystemExit('HILBERT_SUCC_ORIGINAL_RECEIPT_MISMATCH')
        print('HILBERT_SUCC_EXACT_RECEIPT_REPLAY_VERIFIED')
    elif args.output:
        args.output.write_text(txt,encoding='utf-8')
    else:
        sys.stdout.write(txt)


if __name__=='__main__':main()
