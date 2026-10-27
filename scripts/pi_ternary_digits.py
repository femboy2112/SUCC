"""CLI for certified π base-3 digit windows using independent exact oracles."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from observational_succ.pi_ternary_handle import SOURCES, digit_range, source_pole_distribution


def main(argv=None):
    p=argparse.ArgumentParser(description="Rigorously certify fractional base-3 digits of pi")
    p.add_argument('--start',type=int,default=1,help='one-indexed fractional digit')
    p.add_argument('--count',type=int,default=72)
    p.add_argument('--source',choices=('all',)+SOURCES,default='all')
    p.add_argument('--certificate',help='write exact rational interval witnesses as JSON')
    p.add_argument('--pole-depth',type=int,help='print prime-3 pole-depth histogram at level L (<=15)')
    args=p.parse_args(argv)
    sources=SOURCES if args.source=='all' else (args.source,)
    digits,certs=digit_range(args.start,args.count,sources=sources)
    print('pi base-3 fractional positions',args.start,'through',args.start+args.count-1)
    print('digits:',digits)
    print('full certified prefix: 10.'+certs[0].prefix)
    print('sources / exact terms:',', '.join(c.source+'='+str(c.terms) for c in certs))
    print('certificate status: all independent source floors equal')
    if args.pole_depth:
        print('3-adic sixth-slot depths mod 3^L:',source_pole_distribution(args.pole_depth))
    if args.certificate:
        path=Path(args.certificate)
        path.parent.mkdir(parents=True,exist_ok=True)
        body={'policy':'source-exact certified ternary digits; NOT BBP-style random access or pi normality',
              'start':args.start,'count':args.count,'digits':digits,
              'witnesses':[c.as_dict() for c in certs]}
        path.write_text(json.dumps(body,sort_keys=True,indent=2)+'\n',encoding='utf-8')
        print('exact witness JSON:',path)
    return 0

if __name__=='__main__': raise SystemExit(main())
