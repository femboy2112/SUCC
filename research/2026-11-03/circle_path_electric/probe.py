"""Regenerate / verify exact original BBP path/electric source receipts."""
from __future__ import annotations
import sys
import json
import hashlib
from pathlib import Path
import circle_path_electric as m
from fractions import Fraction as Q

HERE=Path(__file__).resolve().parent
RECEIPT=HERE/'FINITE_RECEIPT.json'


def phase_digest(phases):
    s='\n'.join(f'{x.numerator}/{x.denominator}' for x in phases)
    return hashlib.sha256(s.encode()).hexdigest()


def build_receipt():
    oracle1=dict(m.phase_stream(769))
    oracle2=dict(m.modular_phase_stream(769))
    assert oracle1==oracle2
    windows=[]
    for A in (96,192,384):
        x=m.empirical_source_epoch(A)
        energies=[m.collision_energy(x,k) for k in range(4)]
        increments=[m.branching_dissipation(x,k) for k in range(3)]
        assert sum(increments,Q(0))==energies[-1]-1
        assert all(increments[k]==m.explicit_branch_dissipation(x,k) for k in range(3))
        windows.append({'A':A,'exact_energy':list(map(str,energies)),
                        'exact_branch_imbalance':list(map(str,increments)),
                        'original_phase_sha256':phase_digest(x),
                        'exact_telescoping':True})
    arrows=[]
    for n in (97,193,385,769):
        z=m.original_inverse_receipt(n)
        assert z['same'] and z['selected_digit']==z['floor_digit'] and z['candidate_integral_count']==1
        arrows.append({'n':n,'selected_inverse_branch':z['selected_digit'],
                       'odd_candidates':z['candidate_integral_count'],
                       'current_sha256':phase_digest((z['current'],)),
                       'previous_sha256':phase_digest((z['previous'],))})
    projectors=all(m.selector_weights(j)==tuple(int(t==j) for t in range(16)) for j in range(16))
    dft=all(m.cyclotomic16_character_sum(j)==((16,)+(0,)*7 if j%16==0 else (0,)*8) for j in range(-32,33))
    return {'provenance':'original zero-seeded 4-signed-pole BBP rational source',
            'projector_cyclotomic_exact':projectors,'group_ring_orthogonality_exact':dft,
            'two_independent_arithmetic_oracles_agree_n0_to_769':True,
            'predeclared_source_windows':windows,
            'predeclared_source_arrow_indices':arrows,
            'noncontinuous_odd_inverse_witness':'y_k=1/(16k-1)->0, x_k=k/(16k-1)->1/16',
            'periodic_hostile':'x=1/5 fixed by x->16x',
            'resistance_real':'1/15',
            'geometric_2_adic_sum':'-1/15',
            'pi_normality_proved':False,
            'selected_branch_current_saving_proved':False}


def main():
    x=build_receipt()
    if '--write' in sys.argv:
        RECEIPT.write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
        print('WROTE',RECEIPT)
    elif '--verify' in sys.argv:
        old=json.loads(RECEIPT.read_text())
        if old!=x:
            raise SystemExit('RECEIPT MISMATCH')
        print('PASS exact source, independent integer oracle, DFT projector, electricity and original heldouts')
    else:
        print(json.dumps(x,indent=2,sort_keys=True))

if __name__=='__main__':main()
