"""Replay exact CAMBRIAN C category/topology/interface witness receipt."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.cambrian_c_geometry import geometry_demo

if __name__ == "__main__":
    print(json.dumps(geometry_demo(), indent=2, sort_keys=True))
