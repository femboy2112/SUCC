import os,sys,subprocess,time,json,hashlib
from pathlib import Path
E=Path('/home/leah/succ-main-xxii-evidence'); R=Path('/home/leah/SUCC-main-xxii')
name=sys.argv[1]; cmd=sys.argv[2:]; start=time.time()
env={**os.environ,'PYTHONPATH':str(R),'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1'}
sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
with (E/(name+'.log')).open('wb') as f:
 p=subprocess.run(cmd,cwd=R,env=env,stdout=f,stderr=subprocess.STDOUT)
endsha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
r={'name':name,'command':cmd,'cwd':str(R),'start_commit':sha,'end_commit':endsha,'exit_code':p.returncode,'seconds':time.time()-start,'env':{k:env[k] for k in ['PYTHONPATH','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']},'log_sha256':hashlib.sha256((E/(name+'.log')).read_bytes()).hexdigest()}
(E/(name+'.json')).write_text(json.dumps(r,indent=2));print(json.dumps(r));sys.exit(p.returncode)
