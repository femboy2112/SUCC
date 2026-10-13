#!/usr/bin/env python3
"""Fetch immutable mathlib4.14 sources and only the native topology import cache.

All build/download outputs stay in the supplied external directory. Existing
checkouts are verified, never reset. Compilation is sequential and guarded by
B09's resident-memory/system-headroom watchdog.
"""
from __future__ import annotations
import argparse, importlib.util, json, os, subprocess
from pathlib import Path

PIN='4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84'

def run(args, cwd=None):
    return subprocess.run(args,cwd=cwd,check=True,text=True,capture_output=True,timeout=180).stdout.strip()

def checkout(path, url, commit):
    if not (path/'.git').exists():
        if path.exists() and any(path.iterdir()):
            raise RuntimeError(f'Refusing to overwrite nonempty directory: {path}')
        path.mkdir(parents=True,exist_ok=True)
        run(['git','init','-q',str(path)])
        run(['git','remote','add','origin',url],path)
        run(['git','fetch','--depth','1','origin',commit],path)
        run(['git','checkout','--detach','FETCH_HEAD'],path)
    if run(['git','rev-parse','HEAD'],path)!=commit:
        raise RuntimeError(f'Unexpected existing commit: {path}')
    run(['git','diff','--exit-code'],path)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lean',type=Path,required=True)
    parser.add_argument('--mathlib-dir',type=Path,required=True)
    parser.add_argument('--receipt',type=Path,required=True)
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    lean=args.lean.absolute(); mathlib=args.mathlib_dir.resolve()
    if 'version 4.14.0,' not in run([str(lean),'--version']):
        raise RuntimeError('Expected pinned Lean4.14.0')
    checkout(mathlib,'https://github.com/leanprover-community/mathlib4.git',PIN)
    manifest=json.loads((mathlib/'lake-manifest.json').read_text())
    for package in manifest['packages']:
        checkout(mathlib/manifest['packagesDir']/package['name'],package['url'],package['rev'])
    module=root/'research/2026-10-13/SWARM_ATLAS/experiments/B09_topology_gate.py'
    spec=importlib.util.spec_from_file_location('swm_bounded_gate',module)
    gate=importlib.util.module_from_spec(spec); spec.loader.exec_module(gate)
    scratch=mathlib/'.swm-bootstrap'; scratch.mkdir(exist_ok=True)
    env=os.environ.copy(); env['LEAN_PATH']=str(mathlib)
    commands=[]
    for name in ['IO','Hashing','Requests']:
        command=[str(lean),'-j1','-M2048','-o',f'Cache/{name}.olean',f'Cache/{name}.lean']
        result=gate.bounded_compile(command,mathlib,env,scratch); commands.append(result)
        if result['exit_code']!=0:break
    else:
        wrapper=mathlib/'SWMCache.lean'
        wrapper.write_bytes((root/'research/2026-10-13/SWARM_ATLAS/receipts/cache-bootstrap-wrapper.lean').read_bytes())
        command=[str(lean),'-j1','-M2048','--run',str(wrapper)]
        # A cold serial cache download can take longer than a proof compilation.
        # The same memory guards apply; use a separate subprocess timeout budget.
        result=gate.bounded_compile(command,mathlib,env,scratch,timeout_seconds=600)
        result['timeout_seconds']=600
        commands.append(result)
    receipt={'mathlib_commit':PIN,'dependency_commits':{p['name']:p['rev'] for p in manifest['packages']},'checks':commands,'result':'PASS' if all(x['exit_code']==0 for x in commands) else 'FAIL'}
    args.receipt.parent.mkdir(parents=True,exist_ok=True)
    args.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
    print(receipt['result'],args.receipt)
    if receipt['result']!='PASS':
        print(commands[-1]['stdout']);print(commands[-1]['stderr']);raise SystemExit(1)

if __name__=='__main__':main()
