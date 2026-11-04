"""Replay recorded finite results in their own directories. Run with python replay.py."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CASES = (
    ("reflection/reflected_prefix.py", "REFLECTION_RECEIPT.json"),
    ("reflection/referee_probe.py", "REFEREE_RECEIPT.json"),
    ("reflection/marked_transport.py", "MARKED_TRANSPORT_RECEIPT.json"),
    ("primal/prime_layers_probe.py", "PRIME_LAYERS_RECEIPT.json"),
    ("energy/energy_probe.py", "FINITE.json"),
    ("boundary/probe.py", "RECEIPT.json"),
    ("weyl/probe_weyl.py", "WEYL_RECEIPT.json"),
    ("weyl/probe_separation.py", "SEPARATION_RECEIPT.json"),
    ("weyl/probe_independence.py", "INDEPENDENCE_RECEIPT.json"),
    ("beta/europa_probe.py", "receipt.json"),
    ("beta/gamma_boundary_probe.py", "gamma_receipt.json"),
)


def replay(script, receipt_name):
    path = ROOT / script
    run = subprocess.run([sys.executable, path.name], cwd=path.parent,
                         check=True, stdout=subprocess.PIPE, text=True)
    expected = json.loads(path.with_name(receipt_name).read_text())
    if json.loads(run.stdout) != expected:
        raise ValueError(f"Receipt mismatch for {script}")
    print(f"PASS {script}", flush=True)


if __name__ == "__main__":
    for script, receipt_name in CASES:
        replay(script, receipt_name)
