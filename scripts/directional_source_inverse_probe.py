"""Exact verifier and bounded authentic directional-inverse source replay."""
import argparse
from fractions import Fraction as F
import gzip
from hashlib import sha256
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ import directional_source_inverse as S

RECEIPT=ROOT/'research/2026-10-19/DIRECTIONAL_INVERSE_RECEIPT.json'


def json_ready(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:json_ready(v)for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [json_ready(v)for v in x]
    return x


def verify_raw_archive(data):
    record=data.get('raw_archive')
    if not isinstance(record,dict):
        raise ValueError('sealed receipt requires raw archive provenance')
    archive=(ROOT/record['path']).resolve()
    if not archive.is_relative_to(ROOT.resolve()) or not archive.is_file():
        raise ValueError('raw archive missing or outside repository')
    if sha256(archive.read_bytes()).hexdigest()!=record['sha256']:
        raise ValueError('raw archive SHA256 mismatch')
    return True


def verify_compact(data,require_archive=True):
    if data['source_blob']!=S.SOURCE_BLOB or data['RH_proved']:
        raise ValueError('wrong source or unlicensed RH claim')
    if require_archive or 'raw_archive' in data:verify_raw_archive(data)
    output={}
    for name,b in data['blocks'].items():
        a={k:tuple(tuple(tuple(F(v)for v in z)for z in row)for row in x)
           for k,x in b['retained_data_enclosures'].items()}
        checks=[]
        for witness in b['independent_all_response_obstructions']:
            check=S.finite_family_obstruction_from_intervals(**a,kappa=F(b['kappa']),
                c=tuple(F(x)for x in witness['direction']))
            if F(witness['family_upper_bound'])!=check['family_upper_bound']:
                raise ValueError('tampered exact response-family witness')
            if bool(witness['strict_obstruction'])!=check['strict_obstruction']:
                raise ValueError('tampered obstruction truth flag')
            checks.append(check['strict_obstruction'])
        output[name]=any(checks)
    return output


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',action='store_true')
    p.add_argument('--source-holdouts',action='store_true')
    p.add_argument('--reconstruct-pr178',action='store_true')
    p.add_argument('--run-source',action='store_true',help='One costly J24 original-source continuum replay')
    p.add_argument('--output',type=Path)
    p.add_argument('--raw-gzip',type=Path)
    opts=p.parse_args()
    result={}
    if opts.run_source:
        if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(50000)
        raw=S.directional_original_trial()
        result=S.compact_source_receipt(raw)
        if opts.raw_gzip:
            with gzip.open(opts.raw_gzip,'wt')as f:json.dump(json_ready(raw),f,sort_keys=True)
        if opts.output:opts.output.write_text(json.dumps(json_ready(result),indent=2,sort_keys=True)+'\n')
    elif opts.verify:
        result=json.loads(RECEIPT.read_text())
    if opts.verify:result={'independent_compact_verification':verify_compact(result,require_archive=not opts.run_source)}
    if opts.source_holdouts:
        holdout=S.fresh_source_direction_holdout()
        result['fresh_source_holdouts']=[{
            'J':x['J'],'levels':x['levels'],'source_intersection':x['enclosures_intersect'],
            'contact_mutant_disjoint':x['wrong_contact_mutant_disjoint']}
            for x in holdout['fresh_unfitted_direction_checks']]
    if opts.reconstruct_pr178:result['PR178_fixed_data_obstruction']=S.pr178_fixed_obstruction()
    result['RH_proved']=False
    print(json.dumps(json_ready(result),sort_keys=True))


if __name__=='__main__':main()
