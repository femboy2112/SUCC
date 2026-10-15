"""Exact-rational deterministic SUCC source-Gaussian report; zero independent."""
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.source_gaussian_fock import receipt
if __name__ == "__main__":
    print(json.dumps(receipt(),sort_keys=True,indent=2))
