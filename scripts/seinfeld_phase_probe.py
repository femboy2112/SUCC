"""Deterministic exact Seinfeld-SUCC phase receipts, no float/π-digit inputs."""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ import seinfeld_phase as P


def exact_bbp_states(n: int) -> tuple[Q, ...]:
    """Independent direct sum of original four BBP reciprocal poles."""
    states = [Q()]
    for k in range(1,n+1):
        r=Q(4,8*k-7)-Q(2,8*k-4)-Q(1,8*k-3)-Q(1,8*k-2)
        states.append(16*states[-1]+r)
    return tuple(states)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def receipt() -> dict:
    source = ROOT / 'observational_succ/seinfeld_phase.py'
    test = ROOT / 'tests/test_seinfeld_phase.py'
    script = ROOT / 'scripts/seinfeld_phase_probe.py'
    s=exact_bbp_states(41)
    source_fn=lambda n:s[n]
    fake=P.counterfeit_unit_phase
    fake_rows=[]
    for p in (2,3,5):
        for n in (1,2,4,8):
            phi=P.counterfeit_mixed_phase_lift(n,p)
            limit=P.counterfeit_relative_phase_bound(n,p)
            assert abs(phi)<limit
            fake_rows.append({'p':p,'n':n,'phase':str(phi),'bound':str(limit)})
    original=[]
    for p in (2,3,5):
        for n in (1,2,3,4):
            phi=P.relative_affine_phase(n,p,source_fn)
            assert phi == P.source_mixed_phase_lift(n,p,s) % 1
            original.append({'p':p,'n':n,'phase_turn':str(phi)})
    f=lambda n:Q(n*n+3*n,29)
    coherent=P.flat_prime_potential(24,lambda p,n:(f(p*n)-f(n))%1)
    assert all(coherent[n]==(f(n)-f(1))%1 for n in range(1,25))
    try:
        P.flat_prime_potential(24,lambda p,n:Q(n,p))
    except P.PhaseSourceError:
        failed=True
    else:
        failed=False
    assert failed
    return {
        'schema':'SEINFELD_PHASE_EXACT_V1',
        'scope':'classical exact algebra and finite certificates; pi normality/RH OPEN',
        'source_pole_contract':'original four-pole BBP, zero-initial',
        'input_sha256':{'module':digest(source),'tests':digest(test),'probe':digest(script)},
        'unit_root_fibers':[{'k':k,'complex_root_count':len(P.root_turns(k)),
                             'F2_geometric_points':P.frobenius_thickening(k)['geometric_points_over_algebraic_closure'],
                             'F2_nilpotent_rank':P.frobenius_thickening(k)['rank']}
                            for k in range(1,7)],
        'first_order_jets':{str(m):list(P.jet_of_unit_relation(m,3)) for m in (1,2,3,4,8,16)},
        'primitive_prime_affine_twist':{str(p):str(P.primitive_clock_affine_holonomy(7,p))
                                        for p in (2,3,5,7,11)},
        'independent_2x3_prime_twist':str(P.naive_cross_prime_defect(1,2,3)),
        'flat_prime_potential_test':{'horizon':24,'last':str(coherent[24]),'all_prime_squares':True,
                                     'naive_prime_independence_rejected':failed},
        'authentic_selected_mixed_phases':original,
        'nonnormal_fake_mixed_phases':fake_rows,
        'full_gradient_holonomy':{'authentic_p2n3':str(P.full_gradient_affine_holonomy(3,2,source_fn)),
                                  'fake_p2n3':str(P.full_gradient_affine_holonomy(3,2,fake))},
        'unpaid_debt':'source-selected signed Fourier / real collision estimate and transport to normality'
    }


def main() -> None:
    cli=argparse.ArgumentParser()
    cli.add_argument('--verify',action='store_true')
    cli.add_argument('--output',type=Path)
    args=cli.parse_args()
    encoded=(json.dumps(receipt(),sort_keys=True,indent=2,ensure_ascii=False)+'\n').encode('utf-8')
    official=ROOT/'research/2026-10-25/SEINFELD_SUCC_PHASE_RECEIPT.json'
    if args.verify:
        if not official.is_file() or official.read_bytes()!=encoded:
            raise SystemExit('FAIL: exact Seinfeld phase receipt mismatch')
        print('PASS: Seinfeld phase exact receipt byte-identical')
    else:
        dest=args.output or official
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(encoded)
        print(f'Wrote {dest}, {len(encoded)} bytes')


if __name__=='__main__':
    main()
