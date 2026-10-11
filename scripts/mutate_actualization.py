#!/usr/bin/env python3
"""Hostile code mutations: a PASS means every deliberate semantic bug is caught.

Runs isolated temporary copies, never edits the checkout. This is a bounded
mutation sample, not a claim of exhaustive verification or independent agents.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from hashlib import sha256
import argparse
import json
import os
import py_compile
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
MUTATIONS=[
 ('wrong_step','core.py','v + direction*e','v - direction*e','fields'),
 ('erase_context','engine.py','obs["context"], obs["probe"]','"erased", obs["probe"]','engine'),
 ('discard_pending','engine.py','new["phase"] = "observed"','new["phase"] = "ready"','engine'),
 ('forget_factor_weights','arithmetic.py','self.known[f]*self._products[r][k-1]','self._products[r][k-1]','shadow'),
 ('certify_partial','arithmetic.py','self._longest[target] <= self.limits.max_depth','True','shadow'),
 ('skip_semantic_replay','engine.py','if canonical(actual.data()) != canonical(supplied):','if False:','engine'),
 ('erase_conjugation','engine.py','return Scalar.from_data(obj).conjugate().data()','return Scalar.from_data(obj).data()','engine'),
 ('wrong_reverse_order','engine.py','original = self._records[self._active[-1]-1]','original = self._records[self._active[0]-1]','engine'),
 ('collapse_path_yoneda','yoneda.py','tuple(f.word for f in category.hom(p, target))','(len(category.hom(p, target)),)','category'),
 ('wrong_separation_boundary','resource_probe.py','if first <= budget.max_probe_label:','if first < budget.max_probe_label:','resource_probe'),
 ('lose_source_audit','phenomenology.py','"source_audit":shadow.get("source"),','"source_audit":None,','resource_probe'),
 ('erase_prime_factor_horizon','phenomenology.py','self.multipliers = tuple(sorted(n for n in known if 2 <= n <= self.max_shadow_target))','self.multipliers = (2,)','resource_probe'),
 ('future_shadow_source_leak','local_global.py','if n > horizon:\n            break','if n > horizon:\n            pass','local_global'),
 ('erase_coend_identifications','yoneda.py','union(ids[right],ids[left])','pass','category'),
 ('wrong_dual_clock_inclusion','circle_transport.py','(self.n//self.m)*FiniteClock(self.m).mod(j)','1*FiniteClock(self.m).mod(j)','circle_transport'),
]


def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--output',default=str(ROOT/'research/2026-10-09/field_relative_observational_succ/evidence/mutations'))
 args=p.parse_args();out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
 def run(case):
  name,file,old,new,lane=case
  with tempfile.TemporaryDirectory(prefix='succ-mutant-') as tmp:
   tmp=Path(tmp)
   shutil.copytree(ROOT/'observational_succ',tmp/'observational_succ',ignore=shutil.ignore_patterns('__pycache__'))
   shutil.copytree(ROOT/'tests/observational_succ',tmp/'tests')
   path=tmp/'observational_succ'/file
   code=path.read_text();count=code.count(old)
   if count!=1:raise RuntimeError(f'{name}: expected unique mutation site; got {count}')
   path.write_text(code.replace(old,new))
   py_compile.compile(str(path),doraise=True)
   cmd=[sys.executable,'-m','unittest','discover','-s','tests','-p',f'test_{lane}.py']
   proc=subprocess.run(cmd,cwd=tmp,capture_output=True,text=True,timeout=120,
                       env={**os.environ,'PYTHONPATH':str(tmp),'PYTHONHASHSEED':'0'})
   raw=proc.stdout+proc.stderr
   (out/(name+'.txt')).write_text(raw)
   return {'mutation':name,'module':file,'lane':lane,'detected':proc.returncode!=0 and 'FAILED' in raw,
           'exit_code':proc.returncode,'output_sha256':sha256(raw.encode()).hexdigest()}
 with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(run,MUTATIONS))
 report={'status':'PASS' if all(r['detected'] for r in rows) else 'FAIL',
         'mutations':rows,'tested':len(rows),'detected':sum(r['detected'] for r in rows),
         'scope':'eight specific semantic mutations; not exhaustive proof'}
 (out/'report.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(json.dumps(report,indent=2,sort_keys=True))
 return int(report['status']!='PASS')

if __name__=='__main__':raise SystemExit(main())
