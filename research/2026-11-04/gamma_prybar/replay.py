"""Reproduce all core exact and interval receipts without importing donor code."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CASES = {
    "principal": [
        ("reset_probe.py", "RESET_RECEIPT.json"),
        ("packing_probe.py", "PACKING_RECEIPT.json"),
    ],
    "front1": [
        ("cofactor_probe.py", "RECEIPT.json"),
        ("silent_primes.py", "SILENT_RECEIPT.json"),
        ("fiber_mean.py", "MEAN_RECEIPT.json"),
        ("cross_frame.py", "CROSS_FRAME_RECEIPT.json"),
    ],
    "front2": [
        ("checkpoint_probe.py", "CHECKPOINT_RECEIPT.json"),
        ("gap_height_probe.py", "GAP_HEIGHT_RECEIPT.json"),
        ("checkpoint_height_control.py", "HEIGHT_CONTROL_RECEIPT.json"),
    ],
    "front3": [
        ("valve_probe.py", "VALVE_RECEIPT.json"),
        ("reset_probe.py", "RESET_RECEIPT.json"),
        ("reset_probe.py --causal", "CAUSAL_RESET_RECEIPT.json"),
    ],
    "front4": [("fourier_probe.py", "FOURIER_RECEIPT.json")],
    "front5": [
        ("prybar_radial.py", "RADIAL_RECEIPT.json"),
        ("prybar_loss_probe.py", "GAP_RECEIPT.json"),
    ],
    "front7": [
        ("hostile_probe.py", "HOSTILE_RECEIPT.json"),
        ("ablation_probe.py", "ABLATION_RECEIPT.json"),
        ("dyadic_target_probe.py", "DYADIC_TARGET_RECEIPT.json"),
        ("ternary_depth_probe.py", "TERNARY_RECEIPT.json"),
    ],
}


def replay(case):
    section, command, expected = case
    workdir = ROOT / section
    result = subprocess.run([sys.executable, *command.split()], cwd=workdir,
                            check=True, capture_output=True, text=True)
    if json.loads(result.stdout) != json.loads((workdir / expected).read_text()):
        raise ValueError(f"Receipt differs: {section}/{expected}")
    return f"PASS {section}/{expected}"


if __name__ == "__main__":
    cases = [(section, command, expected) for section, rows in CASES.items()
             for command, expected in rows]
    with ThreadPoolExecutor(max_workers=3) as pool:
        for message in pool.map(replay, cases):
            print(message, flush=True)
    print(f"{len(cases)} receipts matched")
