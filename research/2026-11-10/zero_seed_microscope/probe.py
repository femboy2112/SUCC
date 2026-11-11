"""Finite source-first seed-microscope replay; all signed sums are diagnostics.

Run from SUCC repository root. The strict all-N sign proof is in
MICROSCOPE_THEOREMS.md and certify_first_weyl8_detail(), not inferred from
this finite sample.
"""
from __future__ import annotations

from dataclasses import asdict
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json
import sys

THIS = Path(__file__).resolve().parent
spec = spec_from_file_location("succ_seed_microscope", THIS / "seed_microscope.py")
m = module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def main() -> None:
    all_n = []
    for n in (2, 4, 8, 16, 24):
        r = m.microscope_receipt(n, 8)
        direct = r.signed_zero_child_details[0]
        lower = float(F(16,225) / (m.machin_pi_bounds(9)[1] * n*n))
        assert direct > lower
        all_n.append({
            "N":n, "frequency":8, "first_detail_float":direct,
            "theorem_lower_float":lower,
            "source_midpoint_analytic_error_upper":str(r.truncated_phase_budget),
            "uniform_seed_energy":r.annealed_energy[0],
            "selected_zero_weyl_power_float":r.selected_weyl_power,
            "last_cell_energy_float":r.annealed_energy[-1],
            "coherent_zero_control_first_detail_float":m.zero_child_detail(F(0),n,0,8),
            "signed_details_have_both_signs":
                min(r.signed_zero_child_details)<0<max(r.signed_zero_child_details),
        })
    print(json.dumps({
        "truth_state":"PROVED_PAPER all-N first h=8 seed Haar sign; OBSERVED finite floating probes; PI NORMALITY OPEN",
        "parent_pr":591,
        "branch":"research/zero-seed-radix-microscope-2026-11-10",
        "sign_certificate": {k:str(v) for k,v in asdict(m.certify_first_weyl8_detail()).items()},
        "N_experiments":all_n,
        "warning":"Float complex evaluations are not rigorous sine/cosine enclosures. Analytic source-phase interval is separate.",
    },indent=2))


if __name__ == '__main__':
    main()
