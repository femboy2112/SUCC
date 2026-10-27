"""Reproducible exact finite rank-two SUCC research certificate.

No gamma/pi approximation is an input or output. The negative authority flags
must be present; this is NOT a π-normality certificate.
"""
import argparse
import hashlib
import json
from pathlib import Path
from observational_succ import rank_two_chiral_towers as r


def receipt():
    e,o=r.first_shell_channels()
    assert r.source_8_shell_sums()==(r.Q(15,4),r.Q(-15,4),r.Q(-15))
    assert r.polynomial_denominator()==(1,-1,0,r.Q(1,2),r.Q(-1,4))
    assert r.transfer_numerator_from_first_terms()==(4,-4,0,0,0)
    assert r.shell_hankel_det()==4
    assert all(r.impulse(n)==r.impulse_from_towers(n) for n in range(64))
    assert all(r.source_moment(n)==r.authentic_four_poles(n) for n in range(1,129))
    assert all(sum(r.chiral_zero_seed_states(n))==r.original_zero_seed_prefix(n)
               for n in range(25))
    return {
        'schema':'SUCC_CHIRAL_RANK2_BBP_SOURCE_2026_10_27',
        'source':r.SOURCE,
        'carrier':'Q(i) x Q(i), rank2 over Q(i), Q-dimension4',
        'independent_multiplication':True,
        'Q_linear_coupled_successor':True,
        'half_clock':'T^4=-J/4',
        'full_clock':'T^8=I/16',
        'initial_source': '(2,0)',
        'rational_transfer':'4(1-t)/[(1-t+t^2/2)(1-t^2/2)]',
        'full_first_shell':[str(z) for z in r.TAPS],
        'even_first_shell':[str(z) for z in e],
        'odd_first_shell':[str(z) for z in o],
        'even_shell_mass':'15/4',
        'odd_shell_mass':'-15/4',
        'hankel4_det':'4',
        'source_authenticated_first_128':True,
        'selected_zero_seed_first_25':True,
        'real_signed_fourier_oN_proved':False,
        'pi_normality_proved':False,
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',action='store_true')
    p.add_argument('--write',type=Path)
    args=p.parse_args()
    cert=receipt()
    if args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True)
        args.write.write_text(json.dumps(cert,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    if args.verify:
        target=args.write or Path(__file__).resolve().parents[1]/'research/2026-10-27/RANK_TWO_CHIRAL_RECEIPT.json'
        old=json.loads(target.read_text(encoding='utf-8'))
        if old!=cert:
            raise SystemExit('RANK TWO RECEIPT REJECTED: source or result mutation')
        print('RANK TWO SOURCE AND RECEIPT VERIFIED')
    else:
        print(json.dumps(cert,sort_keys=True,indent=2))

if __name__=='__main__':main()
