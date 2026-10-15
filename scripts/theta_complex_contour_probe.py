"""Exact source-derived complex-contour proof receipt; no zero tables."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.theta_complex_contour import receipt
from observational_succ.theta_suzuki_shadow import (
    authentic_local_weil_rank_one,localized_mass_lower,shadow_impostor_inside_critical_strip,paired_original_Weil_window,paired_phase_kernel_interval)


def full_receipt():
    d=receipt()
    d['local_Weil']=authentic_local_weil_rank_one()
    d['normalized_small_source_local_spectral_mass']=localized_mass_lower()
    d['false_global_curve_control']=shadow_impostor_inside_critical_strip()
    d['true_completed_Weil_pair_operator_window']=paired_original_Weil_window()
    d['true_completed_Weil_pair_phase_at_1over2']=paired_phase_kernel_interval()
    return d


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    result=full_receipt()
    if args.verify:
        expected=json.loads(args.verify.read_text())
        if expected!=result:raise SystemExit('ORIGINAL_THETA_COMPLEX_CONTOUR_RECEIPT_MISMATCH')
        print('ORIGINAL_THETA_COMPLEX_CONTOUR_RECEIPT_VERIFIED')
    else:
        s=json.dumps(result,indent=2,sort_keys=True)+'\n'
        if args.output:args.output.write_text(s)
        else:print(s,end='')

if __name__=='__main__':main()
