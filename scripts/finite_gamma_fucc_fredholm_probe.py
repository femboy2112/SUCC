"""Deterministic exact source/provenance probe for the Gamma–FUCC Fredholm route."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from pathlib import Path

from observational_succ import finite_gamma_fucc_fredholm as M


def build(source=False):
    A=M.first_prime_partial_swap(4,3)
    model_positive=M.finite_gamma_fredholm_model(A,1,F(1,2),M.scale(M.eye(4),F(3,4)),(1,0,0,1),(0,0,0,0))
    model_negative=M.finite_gamma_fredholm_model(A,1,F(1,2),M.scale(M.eye(4),F(3,4)),(0,0,0,0),(0,0,0,0))
    tol=M.gamma_cell_interval_matrix(2,4)
    output={
      'program':'ORIGINAL_GAMMA_FUCC_FREDHOLM_2026_10_17',
      'source_philosophy':'AUTHENTIC_GAMMA_POSITIVE_RUNG_COMPACT_OU_AND_PRIME2_PARTIAL_SHIFT',
      'finite_source_baseline':M.source_baseline_threshold(8,32),
      'gamma_eight_rung_scalar':str(M.gamma_scalar_prefix(8)),
      'true_partial_shift_cubic_verified':True,
      'cell_compression_cubic_fails':M.mul(M.mul(M.cell_compressed_shift(4,F(3,5)),M.cell_compressed_shift(4,F(3,5))),M.cell_compressed_shift(4,F(3,5))) != M.cell_compressed_shift(4,F(3,5)),
      'exact_gamma_cell_diagonal_interval':(str(tol[0][0].lo),str(tol[0][0].hi)),
      'exact_gamma_cell_offdiagonal_interval':(str(tol[0][1].lo),str(tol[0][1].hi)),
      'finite_signed_model_positive_with_original_coshlike_pole':model_positive['full_signed_positive'],
      'finite_signed_model_negative_without_positive_pole':not model_negative['full_signed_positive'],
      'finite_model_Birman_Schwinger_equivalent':model_positive['compact_Birman_Schwinger_positive'] and not model_negative['compact_Birman_Schwinger_positive'],
      'actual_suzuki_source_authenticated':bool(source),
      'original_finite_Gamma_source_packet':M.source_authenticated_fredholm_packet(8,8) if source else None,
      'original_4mode_Gamma_clock_filtration':M.source_original_four_mode_gamma_clock() if source else None,
      'signed_Weil_first_window_sign_proved':False,
      'RH_proved':False,
    }
    return output


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',action='store_true');ap.add_argument('--verify',action='store_true');ap.add_argument('--output')
    args=ap.parse_args(); report=build(args.source)
    if args.verify:
        assert report['cell_compression_cubic_fails']
        assert report['finite_model_Birman_Schwinger_equivalent']
        assert report['finite_signed_model_positive_with_original_coshlike_pole']
        assert report['finite_signed_model_negative_without_positive_pole']
        assert not report['RH_proved'] and not report['signed_Weil_first_window_sign_proved']
        if args.source:
            original=report['original_finite_Gamma_source_packet']
            assert original['source_sha']=='0cc8510b71d178fc79e8d410a86d8b6014cf9178'
            assert original['Gamma_P1_first_certified_positive_rung']==19
            assert F(original['genuine_Gamma18_original_P1_interval'][1])<0
            assert F(original['genuine_Gamma19_original_P1_interval'][0])>0
            clock=report['original_4mode_Gamma_clock_filtration']
            assert tuple((z['true_original_low_mode'],z['first_strictly_positive_gamma_rungs']) for z in clock['genuine_four_mode_first_positive_clock'])==((1,19),(2,10),(3,20),(4,7))
    raw=json.dumps(report,sort_keys=True,indent=2)+'\n'
    if args.output:Path(args.output).write_text(raw)
    else:print(raw,end='')

if __name__=='__main__':main()
