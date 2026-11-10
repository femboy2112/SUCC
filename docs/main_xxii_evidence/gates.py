import subprocess,sys
for s in ['verify_provenance','observer_foundations_probe','ordinal_succ_report_probe','verify_math_memory_graph']:
 c=[sys.executable,'scripts/'+s+'.py'];print('COMMAND',c,flush=True);r=subprocess.run(c);print('EXIT',r.returncode,flush=True)
 if r.returncode:sys.exit(r.returncode)
c=[sys.executable,'scripts/build_math_memory.py','--check'];print('COMMAND',c,flush=True);r=subprocess.run(c);sys.exit(r.returncode)
