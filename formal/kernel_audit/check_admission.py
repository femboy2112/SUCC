"""Compare a fresh kernel observation with coordinator-admitted formal evidence."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from observational_succ._formal_catalogue import APPROVED_RECORD_DIGESTS
from observational_succ.proof_authority import FormalTheorem

fresh = json.loads(Path(sys.argv[1]).read_text())
if not APPROVED_RECORD_DIGESTS:
    print("FORMAL_ADMISSION_PENDING: live kernel build passed; no Level C authority admitted yet")
    sys.exit(0)
admitted = ROOT / "formal/kernel_audit/admitted/kernel-attestation.json"
if not admitted.is_file():
    raise RuntimeError("approved catalogue requires the exact archived build record")
record = json.loads(admitted.read_text())
for field in ("environment_sha256", "theorem_exports", "dependency_revisions", "source_hashes"):
    if fresh[field] != record[field]:
        raise RuntimeError(f"fresh kernel observation differs from admitted {field}")
for name in record["theorem_exports"]:
    FormalTheorem.from_receipt(name, record)
    print(f"ADMITTED_EXACT_PROPOSITION {name}")
