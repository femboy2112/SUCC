"""Exact rational Legendre-to-Suzuki source low interactions, NO zero inputs.

All pure rational coefficients are source-independent algebra templates;
only --source-stage requests actual completed signed Suzuki coefficients,
and it fails closed without the immutable PR85 original-source module.
"""
from pathlib import Path
import sys,json,argparse
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fractions import Fraction as F
from observational_succ.suzuki_moment_schur import PARENT_SOURCE_BLOB,PARENT_SHA, AMW_SIBLING_SHA,low_inverse_neumann
from observational_succ.suzuki_legendre_source import (
    source_ou_pair_affine,prime_hinge_integral_polynomial,poly_integral,
    poly_mul,poly_two_variable_cross,authentic_direct_low_matrix,
)

PAIRS=((1,1),(1,2),(1,3),(2,2),(2,4),(3,3))

def receipt():
    a=F(1,2); K=low_inverse_neumann(a,4)
    rows=[]
    for i,j in PAIRS:
        aa,bb=source_ou_pair_affine(i,j,a,F(1,2))
        cc,dd=source_ou_pair_affine(i,j,a,F(5,2))
        poly=prime_hinge_integral_polynomial(i,j,a)
        integral=poly_integral(poly_mul((0,1),poly_two_variable_cross(i,j,a)),0,1)
        assert integral==-2*low_inverse_neumann(a,max(i,j))[i-1][j-1]
        rows.append({'pair':[i,j], 'OU_alpha_half':[str(aa),str(bb)],
                     'OU_alpha_fivehalves':[str(cc),str(dd)],
                     'prime_hinge_poly':[str(x) for x in poly],
                     'source_contact_distance':str(integral)})
    return {'source':'SUZUKI_Q_ZETA_ORIGINAL_MEANZERO_LEGENDRE',
            'sibling_AMW_30moment_sha':AMW_SIBLING_SHA,
            'pinned_original_source_parent':PARENT_SHA,
            'pinned_source_blob':PARENT_SOURCE_BLOB,
            'halfwidth':'1/2', 'pairs':rows,
            'Gamma_rungs_have_PSD_omitted_tail':True,
            'full_source_sign_certified':False,'RH_proved':False,
            'original_unknown_zeros_used':False}


def source_run(rank=3,J=2):
    x=authentic_direct_low_matrix(rank=rank,J=J)
    mat=x['interval_matrix']
    return {'source':x['source'],'rank':rank,'J':J,'halfwidth':x['a'],
            'matrix_interval':[[[str(y.lo),str(y.hi)] for y in row] for row in mat],
            'original_signed_prime_pole_contact_Gamma':True,
            'omitted_authentic_Gamma_tail_PSD':True,
            'RH_proved':False, 'true_Ga_nonnegative_certified':False}


def main():
    p=argparse.ArgumentParser();p.add_argument('--verify',type=Path)
    p.add_argument('--source-stage',action='store_true');p.add_argument('--rank',type=int,default=3)
    p.add_argument('--J',type=int,default=2);args=p.parse_args()
    if args.source_stage:
        print(json.dumps(source_run(args.rank,args.J),sort_keys=True,indent=2));return
    x=receipt()
    if args.verify:
        y=json.loads(args.verify.read_text())
        if x!=y:raise SystemExit('SUZUKI_DIRECT_SOURCE_RECEIPT_MISMATCH')
        print('SUZUKI_DIRECT_SOURCE_RECEIPT_VERIFIED')
    else:print(json.dumps(x,indent=2,sort_keys=True))

if __name__=='__main__':main()
