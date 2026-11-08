"""Scoped tests, source gates, Lean skeleton and deterministic replay checks."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
START='19d98078b60e47092c9b9d050a70b6b7eabb7cd2'


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--replay',action='store_true')
    args=ap.parse_args()
    out=args.output.resolve();out.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ,PYTHONPATH=str(ROOT),OPENBLAS_NUM_THREADS='1',
             OMP_NUM_THREADS='1',LEAN_NUM_THREADS='1')
    commands=[];comparisons=[]
    def run(name,cmd):
        log=out/(name+'.log');start=time.monotonic()
        with log.open('w') as handle:
            result=subprocess.run(cmd,cwd=ROOT,env=env,stdout=handle,stderr=subprocess.STDOUT)
        text=log.read_text()
        tests=re.search(r'Ran (\d+) tests?',text)
        commands.append({'name':name,'command':cmd,'exit_code':result.returncode,
                         'seconds':time.monotonic()-start,
                         'tests':int(tests.group(1)) if tests else None,
                         'log_sha256':sha256(log.read_bytes()).hexdigest()})
        print(name,result.returncode,flush=True)
        if result.returncode:raise RuntimeError(name+' failed')
    try:
        for folder,name in ((HERE,'root'),(HERE/'model','model'),
                            (HERE/'theory','theory'),(HERE/'crucible','crucible')):
            run(name+'_tests',[sys.executable,'-m','unittest','discover',
                              '-s',str(folder),'-p','test_*.py','-v'])
        for gate in ('verify_provenance','observer_foundations_probe','ordinal_succ_report_probe'):
            run(gate,[sys.executable,'scripts/'+gate+'.py'])
        run('lean_kernel',['lean',str(HERE/'CarryPoisson.lean')])
        lean=(out/'lean_kernel.log').read_text()
        assert 'sorryAx' not in lean and lean.count('depends on axioms:')==4
        if args.replay:
            for name,script,retained,extra in (
                ('signed','signed_probe.py','SIGNED_HOLDOUT.json',
                 ['--table',str(HERE/'model/FROZEN_TABLE.json')]),
                ('retro','retro_probe.py','RETRO_EXPLORATORY.json',[])):
                output=out/(name+'_replay.json')
                run(name+'_replay',[sys.executable,str(HERE/script),
                    '--source',str(HERE/'model/HOLDOUT_55003.json.gz'),
                    '--output',str(output),*extra])
                actual=json.loads(output.read_text());expected=json.loads((HERE/retained).read_text())
                comparisons.append({'name':name,'equal':actual==expected})
                assert actual==expected
        native=['tests','scripts','observational_succ','formal','provenance','docs','AGENTS.md']
        changed=subprocess.check_output(['git','diff','--name-only',START,'--',*native],cwd=ROOT,text=True)
        assert not changed,changed
        for path in HERE.rglob('*.json'):json.loads(path.read_text())
        bad=[]
        for path in HERE.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
                if '://' in target or target.startswith('#'):continue
                dest=target.split('#')[0]
                if dest and not (path.parent/dest).exists():bad.append((str(path.relative_to(HERE)),dest))
        assert not bad,bad
        run('whitespace',['git','diff','--check'])
    finally:
        (out/'SUMMARY.json').write_text(json.dumps({'starting_head':START,
            'commands':commands,'replays':comparisons,
            'focused_tests':sum(row['tests'] or 0 for row in commands),
            'native_suite':'Separate actual run; see native_suite.log and VALIDATION.md.',
            'pi_normality':'OPEN','RH':'OPEN'},indent=2,sort_keys=True)+'\n')


if __name__=='__main__':main()
