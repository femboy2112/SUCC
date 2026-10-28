"""Deterministic proof-frontier receipt for the authentic BBP coherent bin tree.

Usage: python scripts/bbp_binwindow_conjugacy_probe.py --write|--verify|--mutate-check
No real pi digits, no normality claim, exact Fraction source only.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
from observational_succ import bbp_binwindow_conjugacy as b

ARTIFACT = ROOT/'research/2026-10-27/BBP_BINWINDOW_RECEIPT.json'


def _hash(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def _format(q):
    return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'


def build():
    boundaries=[]
    for k in list(range(1,17))+[24,32,48]:
        r=b.zero_boundary_certificate(k)
        boundaries.append({'k':k,'modulus':str(r['modulus']),
                           'residue':r['modulus_residue']})
    clocks=[]
    for k in (1,2,3):
        v=b.odometer_certificate(k)
        clocks.append({'k':k,'modulus':v.modulus,
                       'residues':v.unique_residues,'one_cycle':v.one_cycle,
                       'zero_seed':v.time_zero_value})
    ghosts=[]
    for k in (2,3,4,8):
        for n in (0,1):
            if n<k:
                r=b.negative_time_ghost_completion(n,k)
                ghosts.append({'k':k,'n':n,'nonzero_rational':r['nonzero_rational_witness'],
                               'residue':r['ghost_residue_mod_16k']})
    sample=[b.window_agrees_with_zero_seed(n,depth)
            for n,depth in ((0,1),(0,4),(1,2),(2,4),(3,8),(8,7),(33,5))]
    return {
        'source':'Coherent Main original signed four-pole rational forcing',
        'parent_research_pr':320,
        'source_hashes':{
            'module':_hash('observational_succ/bbp_binwindow_conjugacy.py'),
            'tests':_hash('tests/test_bbp_binwindow_conjugacy.py'),
        },
        'boundary':boundaries,
        'boundary_complete_paper_proof':'2-adic Gaussian logarithmic primitive; roots of unity have log zero',
        'first_hex_bin_permutation':[b.first_hex_bin(n) for n in range(16)],
        'odometer_clocks':clocks,
        'early_negative_source_zeroes':ghosts,
        'early_exact_original_vs_extended':[{'n':x['time'],'k':x['hex_depth'],
          'actual':x['direct_original'],'window':x['infinite_past_window']} for x in sample],
        'real_vs_adic_example':{
            'first_source_real_fraction':_format(b.genuine_vs_2adic_Fourier_firewall()['original_real_fraction']),
            'first_2adic_turn':_format(b.genuine_vs_2adic_Fourier_firewall()['hexadic_turn']),
        },
        'status':{'exact_finite_receipt':True,
                  'p_adic_zero_paper_proved':True,
                  'all_time_source_odometer_paper_proved':True,
                  'new_real_circle_weyl_saving_proved':False,
                  'pi_base16_normality_proved':False,
                  'rh_proved':False,
                  'new_lean_kernel_declarations':False},
    }


def main():
    parser=argparse.ArgumentParser()
    choice=parser.add_mutually_exclusive_group(required=True)
    choice.add_argument('--write',action='store_true')
    choice.add_argument('--verify',action='store_true')
    choice.add_argument('--mutate-check',action='store_true')
    args=parser.parse_args()
    truth=build()
    text=json.dumps(truth,indent=2,sort_keys=True)+'\n'
    if args.write:
        ARTIFACT.parent.mkdir(parents=True,exist_ok=True)
        ARTIFACT.write_text(text,encoding='utf-8')
        print('WROTE EXACT BBP BIN-WINDOW RECEIPT:',str(ARTIFACT))
        return
    if not ARTIFACT.is_file():raise SystemExit('expected receipt missing')
    original=ARTIFACT.read_text(encoding='utf-8')
    if args.verify:
        if original != text:raise SystemExit('FAILED: receipt does not match independent recomputation')
        print('VERIFIED EXACT BBP BIN-WINDOW RECEIPT')
        return
    bad=json.loads(original)
    bad['status']['pi_base16_normality_proved']=True
    bad_text=json.dumps(bad,indent=2,sort_keys=True)+'\n'
    if bad_text==text:raise SystemExit('FAILED: false normality mutation escaped')
    if original!=text:raise SystemExit('FAILED: original receipt must verify before mutation')
    print('REJECTED FALSE NORMALITY CLAIM MUTATION; ORIGINAL RECEIPT PRESERVED')


if __name__=='__main__':main()
