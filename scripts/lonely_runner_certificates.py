#!/usr/bin/env python3
"""Recreate published controls and verify every generated certificate independently."""
from fractions import Fraction as F
from hashlib import sha256
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.lonely_runner_search import (
    bcs_five_configuration, cover_certificate, poliakova_configuration,
)
from observational_succ.lonely_runner_verify import exact_maxmin, verify_cover


def controls():
    yield "bcs-five", bcs_five_configuration(), {
        "reference": "Blanco, Criado, Santos arXiv:2603.24784v4, Fig. 1 / Proposition 5.11",
        "url": "https://arxiv.org/html/2603.24784v4", "status": "published control",
    }
    shifts = [F(x) for x in (
        "0", "15799/40560", "61501/162240", "12299/27040", "16219/32448",
        "6673/13520", "1645417/1784640", "2702/27885", "12291/13520",
        "2617/8112", "248957/324480", "10811/13520", "99791/137280")]
    yield "bcs-thirteen", (list(range(1, 14)), shifts, F(1, 16)), {
        "reference": "BCS author companion repository, output/consecutive.out; numerical data only",
        "url": "https://github.com/criado/shifted_lonely_runner_conjecture_counterexample/blob/fd0dbc5f2c7450ae8d7b784e855019507d5a8efd/output/consecutive.out",
        "source_file_sha256": "d835e86ad1b559d415a801e6a06872f3a41c14464ad859414452770281dfa675",
        "status": "published control; no author implementation copied",
    }
    yield "poliakova-n95", poliakova_configuration(96), {
        "reference": "Poliakova arXiv:2609.23952v1, Theorem 7; N=96, scale b=1",
        "url": "https://arxiv.org/html/2609.23952v1", "status": "published control",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    results = []
    for name, (v, s, d), provenance in controls():
        certificate = cover_certificate(v, s, d, source=provenance)
        verdict = verify_cover(certificate)
        data = (json.dumps(certificate, sort_keys=True, separators=(",", ":")) + "\n").encode()
        path = args.output / f"{name}.json"
        path.write_bytes(data)
        result = {"name": name, "file": path.name, "file_sha256": sha256(data).hexdigest(),
                  "file_bytes": len(data), "verdict": verdict}
        if len(v) <= 13:
            result["independent_maximum"] = exact_maxmin(v, certificate["shifts"])
            assert result["independent_maximum"]["gamma"] == certificate["delta"]
        results.append(result)
        print(name, "ACCEPTED", len(certificate["intervals"]), "intervals", flush=True)
    (args.output / "verification.json").write_text(json.dumps(results, indent=2) + "\n")


if __name__ == "__main__":
    main()
