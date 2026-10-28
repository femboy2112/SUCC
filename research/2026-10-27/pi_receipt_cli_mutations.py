"""Recompute and reject three corrupted receipts from an unrelated cwd."""
from pathlib import Path
import copy,json,subprocess,sys,tempfile
root=Path(__file__).resolve().parents[2]
source=root/'scripts/pi_signed_cancellation_probe.py'
receipt=json.loads((root/'research/2026-10-27/PI_SIGNED_CANCELLATION_RECEIPT.json').read_text())
mutations=[]
v=copy.deepcopy(receipt);v['pi_normality_proved']=True;mutations.append(('false_normality',v))
v=copy.deepcopy(receipt);v['energies'][0]['authentic_interval']=['0','0'];mutations.append(('zero_width_false_energy',v))
v=copy.deepcopy(receipt);v['source_hashes'][source.name]='0'*64;mutations.append(('source_hash',v))
with tempfile.TemporaryDirectory() as tmp:
 for name,v in mutations:
  p=Path(tmp)/(name+'.json');p.write_text(json.dumps(v,sort_keys=True,indent=2)+'\n')
  run=subprocess.run([sys.executable,str(source),'--verify',str(p)],cwd=tmp,capture_output=True,text=True)
  if run.returncode==0 or 'RECEIPT REJECTED' not in run.stderr:raise RuntimeError((name,run.returncode,run.stdout,run.stderr))
  print(json.dumps({'mutation':name,'exit_code':run.returncode,'stderr':run.stderr.strip()}))
print('All three fresh CLI mutations rejected; no universal proof inferred.')
