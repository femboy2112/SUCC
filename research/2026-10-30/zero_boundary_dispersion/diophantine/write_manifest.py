"""Record input and artifact hashes. Run only after intentional edits."""
from pathlib import Path
import hashlib,json,subprocess
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[3]

def entry(p,relative):
    b=p.read_bytes()
    return {'path':str(p.relative_to(relative)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

inputs=[ROOT/'AGENTS.md']
inputs+=sorted((ROOT/'research/2026-10-30/selected_boundary_slip').glob('*'))
inputs += [ROOT/'research/2026-10-30/gamma_twist/signed/SHARP_SEED_ENERGY.md',
           ROOT/'research/2026-10-30/gamma_twist/CURRENT_OBSTRUCTION.md',
           ROOT/'research/2026-10-30/gamma_twist/run_receipt.py']
artifacts=[p for p in sorted(BASE.rglob('*')) if p.is_file() and
           '__pycache__' not in p.parts and p.name!='SOURCE_MANIFEST.json']
data={'parent_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
      'scope':'Diophantine branch artifacts; no source changes',
      'source_inputs':[entry(p,ROOT) for p in inputs if p.is_file()],
      'artifacts':[entry(p,BASE) for p in artifacts],
      'external_primary_inputs':[
          {'url':'https://arxiv.org/abs/1912.06345','authority':'Published Zeilberger-Zudilin 2020; pi mu<15/2'},
          {'url':'https://cs.uwaterloo.ca/~shallit/Papers/scf.pdf','authority':'Shallit 1979 Theorems1,8,9; bounded partial quotients for beta_2'}],
      'proof_authority':'Paper proofs plus narrowly scoped Lean finite integer kernel; no external referee.'}
(BASE/'SOURCE_MANIFEST.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'input_files':len(data['source_inputs']),'artifact_files':len(data['artifacts'])}))
