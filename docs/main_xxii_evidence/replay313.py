import subprocess,os,sys,json,time,pathlib
E=pathlib.Path('/home/leah/succ-main-xxii-evidence');R=pathlib.Path('/home/leah/SUCC-main-xxii');py=sys.executable
commands=[]
for folder in ['research/2026-11-08/chronology_carry','research/2026-11-08/chronology_carry/model','research/2026-11-08/chronology_carry/theory','research/2026-11-08/chronology_carry/crucible']:
 commands.append([py,'-m','unittest','discover','-s',folder,'-p','test_*.py','-v'])
commands += [[py,'research/2026-11-08/chronology_carry/manifest.py'],['/home/leah/.elan/toolchains/leanprover--lean4---v4.14.0/bin/lean','research/2026-11-08/chronology_carry/CarryPoisson.lean'],[py,'research/2026-11-08/four_pole_nine/independent_sympy_oracle.py','--out',str(E/'four-pole-replay313.json')]]
for c in commands:
 print('COMMAND',c,flush=True);r=subprocess.run(c,cwd=R);print('EXIT',r.returncode,flush=True)
 if r.returncode:sys.exit(r.returncode)
