"""Replayable exact original BBP shift-averaged-current receipt.

Usage: python probe.py --write    (development; archive exact receipt)
       python probe.py --verify   (literal byte comparison with frozen receipt)
No pi digits, no floating fits, no external web, no random samples.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('selected_current_probe_module',ROOT/'selected_current.py')
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def _q(x):
    z=F(x)
    return f'{z.numerator}/{z.denominator}'


def _digest_phase_cloud(p):
    raw='\n'.join(_q(x) for x in p).encode('ascii')
    return hashlib.sha256(raw).hexdigest()


def build():
    out={
      'contract':'authentic_four_signed_BBP_U0_0_source_selected_real_phase',
      'preregistration_sha':'d07f6d1487eb032de36935e66e7a81357aa71ebc',
      'source':'r=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U0=0',
      'status':'finite exact observed; no asymptotic normality proof',
      'pi_digits_as_input':False,
      'windows':[],
      'independent_origin_integral':[],
      'negative_controls':[]
    }
    for A in (40,80,160):
        p=c.source_epoch(A)
        assert p==c.independent_modular_epoch(A)
        rows=[]
        for m in (8,16,32):
            z=c.canonical_vs_translated_bound(p,m)
            b=c.forced_boundary_mean(A,m)
            cap=c.forced_boundary_cap(A,m)
            assert b<=cap
            rows.append({'mesh':m,'E_unshifted':_q(z['canonical_energy']),
                         'J_half_mesh':_q(z['translation_averaged_half_mesh']),
                         'J_mesh':_q(c.translated_energy(p,m)),
                         'E_upper_4J':_q(z['certified_upper']),
                         'Gamma_completed_comparison_cap':_q(c.gamma_tail_energy_transport_bound(A,m)),
                         'mean_forced_boundary_crossings':_q(b),
                         'forced_crossing_cap':_q(cap)})
        out['windows'].append({'A':A,'phase_sha256':_digest_phase_cloud(p),
                               'denominators_odd':all(z.denominator%2==1 for z in p),
                               'independent_modular_source_match':True,
                               'meshes':rows})
    for A in (12,24):
        p=c.source_epoch(A)
        for m in (4,8,16):
            lhs=c.translated_energy(p,m)
            rhs=c.independent_origin_integral(p,m)
            assert lhs==rhs
            out['independent_origin_integral'].append({'A':A,'mesh':m,
                    'exact_J':_q(lhs),'piecewise_origin_integration_matches':True})
    for mesh in (4,16,256):
        q=c.periodic_fixed_point_control(mesh)
        out['negative_controls'].append({'mesh':mesh,'point':'1/5',
            'E':_q(q['canonical_energy']),'J':_q(q['translated_energy']),
            'nonnormal_counterexample_remains_coherent':True})
    return out


def encoded(o):
    return (json.dumps(o,indent=2,sort_keys=True,ensure_ascii=True)+'\n').encode('utf-8')


def main():
    ap=argparse.ArgumentParser()
    x=ap.add_mutually_exclusive_group(required=True)
    x.add_argument('--write',action='store_true')
    x.add_argument('--verify',action='store_true')
    args=ap.parse_args()
    dest=ROOT/'FINITE_RECEIPT.json'
    data=encoded(build())
    if args.write:
        dest.write_bytes(data)
        print('wrote exact source receipts',dest,'bytes',len(data))
    else:
        if dest.read_bytes()!=data:
            raise AssertionError('exact original source receipt drift; inspect before changing')
        print('PASS: selected source exact finite receipt replay, bytes',len(data))

if __name__=='__main__':main()
