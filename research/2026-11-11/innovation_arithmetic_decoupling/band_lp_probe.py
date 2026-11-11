#!/usr/bin/env python3
"""Finite LP evidence for OBSTRUCTIONS O-7 (correlation positivity on a lag band).

Question: if a positive measure of mass 1 on the circle (the spectral measure of
a correlation sequence) has vanishing Fourier coefficients at every integer lag
d in [a, b], how large can its atom at frequency 0 (the squared mean) be?

The LP restricts the non-atomic part to a symmetric grid, so its optimum is a
LOWER bound for the true supremum: each reported value certifies (to LP
floating tolerance, re-checked below) the existence of a positive measure with
that atom and zero band coefficients.  This is floating-point evidence about
positive-definite sequences in general.  It is NOT a statement about pi and
not a rigorous certificate.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

BANDS = ((30, 30), (20, 22), (40, 44), (10, 15), (20, 30), (40, 60), (80, 120), (20, 39), (40, 79))
GRID = 6000


def best_atom(a: int, b: int, grid: int = GRID) -> dict:
    theta = np.arange(1, grid + 1) / (2 * grid)
    lags = np.arange(a, b + 1)
    A = np.zeros((len(lags) + 1, grid + 1))
    rhs = np.zeros(len(lags) + 1)
    A[: len(lags), 0] = 1.0
    A[: len(lags), 1:] = np.cos(2 * np.pi * np.outer(lags, theta))
    A[-1, :] = 1.0
    rhs[-1] = 1.0
    cost = np.zeros(grid + 1)
    cost[0] = -1.0
    res = linprog(cost, A_eq=A, b_eq=rhs, bounds=[(0, None)] * (grid + 1), method="highs")
    if res.status != 0:
        raise RuntimeError(f"LP failed for band {(a, b)}: {res.message}")
    sol = np.clip(res.x, 0.0, None)
    residual = float(np.max(np.abs(A @ sol - rhs)))
    return {"a": a, "b": b, "ratio": round(b / a, 4), "atom": round(float(sol[0]), 9),
            "support_points": int(np.count_nonzero(sol[1:] > 1e-12)),
            "max_constraint_residual": float(f"{residual:.3e}")}


def main() -> None:
    rows = [best_atom(a, b) for a, b in BANDS]
    out = {"claim": "O-7 finite LP evidence; floating point; lower bounds on the supremum",
           "grid": GRID, "two_point_kernel_bound": 0.5, "rows": rows,
           "reference_values": {"1/sqrt(5)": round(5 ** -0.5, 9), "(sqrt(3)-1)/2": round((3 ** 0.5 - 1) / 2, 9)}}
    path = Path(__file__).with_name("RESULTS_band_lp.json")
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
