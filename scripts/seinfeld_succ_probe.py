"""Deterministic exact replay for the Seinfeld SUCC research dossier.

Usage: python scripts/seinfeld_succ_probe.py --verify
       python scripts/seinfeld_succ_probe.py --output /tmp/seinfeld.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

from observational_succ import seinfeld_succ as S

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / 'research/2026-10-25/SEINFELD_SUCC_FINITE_RECEIPT.json'


def exact(x: Q) -> str:
    return f'{x.numerator}/{x.denominator}'


def build() -> dict:
    rank = [S.recurrence_rank_receipt(n) for n in (1,2,4,8,16)]
    nulls = []
    for n,p in ((1,2),(2,3),(3,5)):
        chain = S.affine_null_loop(n,p)
        values={e:Q(e[1]) if e[0]=='S' else Q() for e in chain}
        u=S.source_states(p*(n+1))
        nulls.append({'n':n,'prime':p,'nonzero_edges':len(chain),
                      'boundary':S.chain_boundary(chain),
                      'holonomy_nonexact':exact(S.chain_holonomy(chain,values)),
                      'holonomy_exact':exact(S.gradient_transport(chain,
                         {j:u[j] for j in range(1,len(u))}))})
    fibers=[]
    for k in (1,2,3):
        s=S.source_states(k)
        f=S.circle_backward_fiber(s[-1]%1,tuple(S.bbp_forcing(j) for j in range(1,k+1)))
        fibers.append({'depth':k,'circle_predecessors':len(f),
                       'odd_predecessors':sum(y.denominator%2 for y in f),
                       'source_zero_included':Q(0) in f})
    fake=[]
    for n in (1,2,3,8,16):
        fake.append({'n':n,'forcing':exact(S.counterfeit_forcing(n)),
                     'state':exact(S.counterfeit_closed_state(n)),
                     'phase':exact(S.counterfeit_phase(n)),
                     'strictly_inside_quarter_to_third':S.counterfeit_is_confined(n)})
    frob=[]
    for p in (2,3,5,7):
        a=S.bbp_frobenius_relation(1,p)
        frob.append({'p':p,'zero':exact(a['zero']),
                     'p_integral':a['p_integral'],'carry':exact(a['carry'])})
    source_hashes={}
    for name in ('observational_succ/seinfeld_succ.py','tests/test_seinfeld_succ.py'):
        source_hashes[name]=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    return {'schema':'seinfeld-succ-exact-v1','source_main':'1e3a453e869992961bc2d7f3bb6f2f1ddab38854',
            'status':'finite exact only; pi normality and RH OPEN',
            'rank':rank,'null_cycles':nulls,'inverse_fibers':fibers,
            'counterfeit':fake,'frobenius':frob,'source_hashes':source_hashes}


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--verify',action='store_true')
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    text=json.dumps(build(),indent=2,sort_keys=True)+'\n'
    if args.verify:
        if not RECEIPT.exists() or RECEIPT.read_text()!=text:
            raise SystemExit('SEINFELD_EXACT_RECEIPT_MISMATCH')
        print('SEINFELD_EXACT_RECEIPT_VERIFIED')
    elif args.output:
        args.output.write_text(text)
        print(args.output)
    else:
        print(text,end='')

if __name__=='__main__':
    main()
