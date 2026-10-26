"""Reproducible four-point geometric finite audit; numerical values are diagnostics.

--write creates the local JSON fixture after focused tests pass.
--verify compares the saved JSON fixture with newly recomputed output.
No pi normality or Gamma space fingerprint uniqueness claim.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.seinfeld_four_point import (
 LAMBDA_GOLD,legendre_j,weierstrass_j,cross_ratio,source_fourth_point,
 tetrahedral_face_syzygy,torsion_fiber_exponents,elliptic_four_torsion_pairing,
)
from observational_succ.four_point_kronecker import (
 workdps,golden_signature,cusp_remainder,epstein_poisson,
)
FIXTURE=ROOT/'research'/'2026-10-25'/'SEINFELD_FOURPOINT_RECEIPT.json'
SOURCES=('observational_succ/seinfeld_four_point.py',
         'observational_succ/four_point_kronecker.py',
         'tests/test_seinfeld_four_point.py')


def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def make_receipt():
    for n in (1,2,3,4,5,8,12):
        assert source_fourth_point(n)['j_invariant']>0
    with workdps(60):
        data=golden_signature(60,100)
        y=data['period_y']
        eps=mp.mpf('.0005')
        independent=2*(epstein_poisson(y,1+eps/2,12)-mp.pi/(eps/2))-(epstein_poisson(y,1+eps,12)-mp.pi/eps)
        cusp=cusp_remainder(4,100)
        numerical={
          'lambda_golden':mp.nstr(data['lambda'],32),
          'golden_period_y':mp.nstr(y,32),
          'golden_shape_log':mp.nstr(data['log_shape'],32),
          'golden_kronecker_finite_part':mp.nstr(data['kronecker_finite_part'],32),
          'shape_difference_from_square':mp.nstr(data['square_reference_difference'],32),
          'lambda_minus_gamma':mp.nstr(data['gamma_subtracted_from_lambda'],32),
          'epstein_poisson_richardson_error':mp.nstr(abs(independent-data['kronecker_finite_part']),16),
          'cusp_y4_error':mp.nstr(cusp['positive_difference'],16),
          'cusp_y4_proved_upper_formula_numeric':mp.nstr(cusp['explicit_upper'],16),
          'numeric_authority':'noncertifying mpmath consistency only'
        }
    source=[source_fourth_point(n) for n in range(1,6)]
    cycles=tetrahedral_face_syzygy()
    return {
      'schema':'SUCC-SEINFELD-FOURPOINT-1',
      'source':'Q:Coherent-Main-X-four-pole-BBP',
      'source_sha256':{name:sha(name) for name in SOURCES},
      'golden_j_exact':str(legendre_j(LAMBDA_GOLD)),
      'rational_weierstrass_j':str(weierstrass_j(-30,25)),
      'projective_cr_check':str(cross_ratio(None,0,1,source[0]['circle_phase'])),
      'source_first_states':[{'n':x['n'],'unwrapped':str(x['unwrapped_state']),
         'circle_phase':str(x['circle_phase']),'j':str(x['j_invariant'])} for x in source],
      'tetrahedron_face_boundaries_cancel':not bool(cycles['edge_boundary']),
      'cycle_ranks':[cycles['cycle_rank_triangle'],cycles['cycle_rank_tetrahedron']],
      'torsion_fibers':torsion_fiber_exponents(),
      'weil_pairing_10_01':elliptic_four_torsion_pairing((1,0),(0,1)),
      'numerical':numerical,
      'projective_geometry_selects_bbp':False,
      'signed_weyl_estimate_proved':False,
      'pi_normality_proved':False,
      'RH_proved':False,
      'authority':'paper proof for classical geometry; local exact checks; numeric diagnostics'
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--write',action='store_true')
    p.add_argument('--verify',action='store_true')
    args=p.parse_args()
    if args.write and args.verify: p.error('choose write OR verify')
    receipt=json.loads(json.dumps(make_receipt(),sort_keys=True))
    if args.write:
        FIXTURE.parent.mkdir(parents=True,exist_ok=True)
        FIXTURE.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
        print(f'Wrote {FIXTURE}')
    elif args.verify:
        expected=json.loads(FIXTURE.read_text())
        if expected!=receipt:
            raise SystemExit('FOURPOINT RECEIPT MISMATCH: source or output changed')
        print('EXACT SOURCE-HASHED RECEIPT REPLAY PASSED; numeric diagnostic fields remain uncertified')
    else:
        print(json.dumps(receipt,indent=2,sort_keys=True))

if __name__=='__main__':main()
