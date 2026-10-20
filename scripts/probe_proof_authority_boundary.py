import importlib.util
import json
from pathlib import Path
import subprocess
import sys

root = Path.cwd()
path = Path('/tmp/succ_authority_209.py')
path.write_bytes(subprocess.check_output(['git', 'show', '3e1ef648896821321423e6642f1de4a458a0c791:observational_succ/proof_authority.py']))
spec = importlib.util.spec_from_file_location('authority209', path)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
receipt = json.loads((root / 'formal/mathlib_bridge/axiom_audit.json').read_text())
theorem = module.FormalTheorem('polynomial_fermat',receipt['toolchain'],receipt['manifest_rev'],('propext','Classical.choice','Quot.sound'))
rh = module.Claim('unrelated-RH','The Riemann hypothesis is true.','C',scope='global')
wrong = module.Claim('wrong-matrix','The matrix [[-1]] is PSD.','B')
cert = module.LocalCertificate('psd_matrix',{'matrix': [[1]]})
print(json.dumps({'target':'3e1ef648896821321423e6642f1de4a458a0c791',
 'real_polynomial_receipt_for_RH':rh.discharge(theorem,receipt=receipt).status,
 'positive_matrix_certificate_for_negative_matrix':wrong.discharge(cert).status,
 'note':'Loaded exact historical authority.py with current exact arithmetic backend; historical full suite separately owned by referee.'},indent=2))
