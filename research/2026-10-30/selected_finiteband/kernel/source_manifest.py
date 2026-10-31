"""Hash this front and pinned read-only mathematical inputs; no truth claim."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[3]
OUT=HERE/'SOURCE_MANIFEST.json'
EXCLUDE={'SOURCE_MANIFEST.json','manifest_audit.json'}


def digest(data): return hashlib.sha256(data).hexdigest()


def inventory():
    artifacts={p.name:{'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())}
               for p in sorted(HERE.iterdir()) if p.is_file() and p.name not in EXCLUDE}
    sources=[]
    parent='fa598e3a5a1111c3445200f1ddf48dcdea6bdc09'
    for p in sorted((REPO/'research/2026-10-30/codex_finite_band_crt').iterdir()):
        if p.is_file():
            rel=str(p.relative_to(REPO))
            frozen=subprocess.check_output(['git','show',f'{parent}:{rel}'],cwd=REPO)
            assert frozen==p.read_bytes()
            sources.append({'commit':parent,'path':rel,'sha256':digest(frozen)})
    for commit,path in [
        ('5a54cd1a4200f3b0e673f6c3feecff76bf6b6dc6','research/2026-10-30/deepseek_cylinder_fanout/MOVING_SCALE_THEOREM.md'),
        ('3857e70472cac7c572528cc6d4198246e57d36df','research/2026-10-30/carrier_realization_quotient/CARRIER_REALIZATION_QUOTIENT.md'),
        (parent,'research/2026-10-30/selected_boundary_slip/THEOREMS.md'),
        (parent,'AGENTS.md'),(parent,'docs/METHOD.md')]:
        data=subprocess.check_output(['git','show',f'{commit}:{path}'],cwd=REPO)
        sources.append({'commit':commit,'path':path,'sha256':digest(data)})
    local_reviews=[]
    for path in ('research/2026-10-30/selected_finiteband/certified_band.py',
                 'research/2026-10-30/selected_finiteband/cylinders/CYLINDERS_AND_STONEHAM.md'):
        local_reviews.append({'path':path,'sha256':digest((REPO/path).read_bytes())})
    return {'artifacts':artifacts,'read_only_git_inputs':sources,'local_review_inputs':local_reviews}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    current=inventory()
    if args.write:
        OUT.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'authority':'byte/provenance integrity only; paper proofs and finite tests separately scoped',
          'external_inputs':['https://dlmf.nist.gov/5.9.E7','https://dlmf.nist.gov/5.4.E6'],
          **current},indent=2)+'\n')
    recorded=json.loads(OUT.read_text())
    for key in current: assert current[key]==recorded[key],key
    print(json.dumps({'status':'PASS','artifacts':len(current['artifacts']),
                      'git_inputs':len(current['read_only_git_inputs']),
                      'local_review_inputs':len(current['local_review_inputs']),
                      'manifest_sha256':digest(OUT.read_bytes())},indent=2))


if __name__=='__main__':main()
