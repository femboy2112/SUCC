"""Reproduce source hashes, rigorous finite energies and hostile controls."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ import chiral_target_descent as d

FILES=(
    'observational_succ/rank_two_chiral_towers.py',
    'observational_succ/chiral_target_descent.py',
    'tests/test_chiral_target_descent.py',
    'scripts/chiral_target_descent_probe.py',
)


def decimal_out(q: Q, upper: bool=False, places: int=12) -> str:
    scale=10**places
    k=(q*scale).__ceil__() if upper else (q*scale).__floor__()
    sign='-' if k<0 else ''
    k=abs(k)
    return sign+str(k//scale)+'.'+str(k%scale).zfill(places)


def view(v: d.Bounds) -> list[str]:
    return [decimal_out(v.low),decimal_out(v.high,True)]


def build() -> dict:
    pairs=d.phase_history(256)
    xs=[sum(pair)%1 for pair in pairs]
    rows=[]
    for n in (16,32,64,128,256):
        true=d.poisson_energy(xs[:n],18)
        false=d.poisson_energy(d.rational_control(n),18)
        rows.append({'N':n,'modes':18,'authentic_full_energy':view(true.full),
                     'nonnormal_source_control':view(false.full),
                     'spectral_tail':str(true.spectral_tail),
                     'rounding':'outward decimal, exact rational internally'})
    e=d.poisson_energy(xs[:2],18).full
    j=d.innovation(xs[:2],xs[2])
    assert j.low-e.high/2>Q(3,5)
    return {
      'schema':'SUCC_CHIRAL_TARGET_DESCENT_V1',
      'source_parent':'a0e4bfd9c218dfdc83ed9d5684ce8d8e4624cde5',
      'source_hashes':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in FILES},
      'pi_normality_proved':False,
      'stronger_selected_weyl_order_proved':False,
      'finite_experiments_only':True,
      'gauge':'a_n=1/[4(8n+1)]; corrected plus=Uplus+a_n, minus=Uminus-a_n',
      'neutral_filter':{'plus':[17,-17,1],'minus':[1],
         'D_at_1':d.classify_filter((17,-17,1),(1,)).endpoint_residue,
         'log2_coefficient':d.classify_filter((17,-17,1),(1,)).log2_coefficient},
      'q17_full_grid_energy_exact':str(Q(2,2**17-1)),
      'false_per_step_contraction':{'N':2,'energy':view(e),'innovation':view(j),
         'certified_violation_lower':decimal_out(j.low-e.high/2)},
      'rows':rows,
    }


def verify(record: dict, actual: dict | None=None) -> None:
    if record.get('pi_normality_proved') is not False:
        raise ValueError('unsupported normality promotion')
    if record.get('stronger_selected_weyl_order_proved') is not False:
        raise ValueError('unsupported signed-Weyl improvement')
    if record != (actual if actual is not None else build()):
        raise ValueError('receipt differs from source-authenticated exact replay')


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    g=p.add_mutually_exclusive_group()
    g.add_argument('--write',type=Path)
    g.add_argument('--verify',type=Path)
    args=p.parse_args()
    actual=build()
    if args.verify:
        verify(json.loads(args.verify.read_text()),actual)
        print('EXACT CHIRAL TARGET RECEIPT VERIFIED')
    elif args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True)
        args.write.write_text(json.dumps(actual,indent=2,sort_keys=True)+'\n')
        print('EXACT CHIRAL TARGET RECEIPT WRITTEN:',args.write)
    else:
        print(json.dumps(actual,indent=2,sort_keys=True))
    for name in ('pi_normality_proved','stronger_selected_weyl_order_proved'):
        mutation=dict(actual);mutation[name]=True
        try:verify(mutation,actual)
        except ValueError:pass
        else:raise AssertionError('false proof flag accepted')
    mutation=dict(actual);mutation['source_parent']='foreign-source'
    try:verify(mutation,actual)
    except ValueError:pass
    else:raise AssertionError('wrong source accepted')
    print('THREE FALSE-AUTHORITY/SOURCE MUTATIONS REJECTED; PI NORMALITY OPEN')
    return 0

if __name__=='__main__':raise SystemExit(main())
