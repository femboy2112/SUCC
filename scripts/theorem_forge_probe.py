#!/usr/bin/env python3
"""Replay the portable acquisition certificate and exact Forge II controls.

The acquisition certificate is checked without calling its synthesizer.
Infinite analytical theorems are proved in papers, not by this finite probe.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.information_repair import (
    Acquisition, AcquisitionCertificate, ProbeEdge, check_acquisition,
    advice_at_budget,
)
from observational_succ.finite_euler_rigidity import euler_ratio
from observational_succ.forge_operator_transport import finite_control_report


def checked_acquisition(path):
    data = json.loads(path.read_text())
    expected = {"target": "original class", "costs_observed": True,
                "refusal_oracle": False, "controller_memory_bounded": False,
                "source_restoration_certified": False}
    if data["contract"] != expected:
        raise ValueError("acquisition interface drift")
    raw = data["problem"]
    edges = tuple(ProbeEdge(e["start"], e["action"], e["target"],
                            e["receipt"], Q(*e["cost"])) for e in raw["edges"])
    problem = Acquisition(edges=edges, **{k: tuple(v) for k, v in raw.items() if k != "edges"})
    raw = data["certificate"]
    beliefs = lambda rows: tuple(tuple(tuple(pair) for pair in b) for b in rows)
    cert = AcquisitionCertificate(
        starts=beliefs(raw["starts"]), beliefs=beliefs(raw["beliefs"]),
        values=tuple(None if v is None else Q(*v) for v in raw["values"]),
        policy=tuple(raw["policy"]), ranks=tuple(raw["ranks"]))
    check_acquisition(problem, cert)
    points = [advice_at_budget(problem, cert, Q(c)) for c in (0, 1, 2)]
    frontier = [(p["advice_bits"], str(p["budget"])) for p in points]
    if frontier != [(2, "0"), (1, "1"), (0, "2")]:
        raise ValueError("exact advice frontier drift")
    return {"beliefs": len(cert.beliefs), "certificate_verified_without_synthesis": True,
            "advice_bits_and_cost": frontier}


def main():
    acquisition = checked_acquisition(ROOT / "research/2026-10-19/INFORMATION_REPAIR_CERTIFICATE.json")
    U, V = (3, 11), (Q(9, 2), Q(77, 17))
    positive, reflected = euler_ratio(U, V, 2), euler_ratio(U, V, -1)
    if (positive, reflected) != (Q(504, 517), Q(34, 21)):
        raise ValueError("finite Euler counterfeit drift")
    operator = finite_control_report()
    if operator["fresh_shell_formula_mass"] != operator["fresh_shell_counted_mass"]:
        raise ValueError("independent cylinder count disagrees")
    print(json.dumps({"status": "EXACT_FINITE_CERTIFICATES_VERIFIED",
                      "acquisition": acquisition,
                      "Euler_counterfeit": {"F2": str(positive), "Fminus1": str(reflected)},
                      "operator": operator, "infinite_theorems_checked_by_code": False,
                      "RH_proved": False}, indent=2))


if __name__ == "__main__":
    main()
