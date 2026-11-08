#!/usr/bin/env python3
"""Render explanatory scientific figures from the exact pin-bed models.

Curve rasterization uses floating point only for display. Proofs and exact
checks are in THEOREMS.md, the Fraction module, and the recorded oracles.
"""
from fractions import Fraction as Q
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from observational_succ.fourier_yoneda_pinbed import CircleLaw, affine_push, pin_surface


def curve(law, t):
    result = np.zeros_like(t)
    for x, p in law.atoms:
        u = (t-float(x)) % 1
        result += float(p)*(u*u-u+1/6)
    return result


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.titleweight": "bold", "svg.fonttype": "none",
                         "svg.hashsalt": "succ-fourier-yoneda-pinbed-v1"})
    fig, axes = plt.subplots(3, 1, figsize=(9.6, 10.8), constrained_layout=True)
    t = np.linspace(0, 1, 1601)
    plum, teal, orange = "#6e3aa7", "#087f8c", "#c26a17"
    law = CircleLaw(((Q(1, 5), Q(2, 3)), (Q(3, 5), Q(1, 3))))
    pins = [Q(j, 32) for j in range(33)]

    ax = axes[0]
    ax.plot(t, curve(law, t)+1/12, color=plum, linewidth=2.4, label="Continuous pin surface")
    heights = [float(pin_surface(law, x)+Q(1, 12)) for x in pins]
    ax.vlines([float(x) for x in pins], 0, heights, color=plum, linewidth=1, alpha=.5)
    ax.scatter([float(x) for x in pins], heights, color=plum, s=12, zorder=3)
    ax.axhline(1/12, color="#555555", linestyle="--", linewidth=1.2, label="Haar reference")
    ax.set_title("A  A probability law leaves a continuous imprint", loc="left", pad=13)
    ax.set_ylabel("Raw pin height")
    ax.set_ylim(0, .20)
    ax.legend(frameon=False, loc="upper right", fontsize=10)
    ax.text(.02, .92, "Two source atoms: 1/5 and 3/5\nWeights: 2/3 and 1/3", transform=ax.transAxes,
            va="top", fontsize=10, bbox={"facecolor":"white", "edgecolor":"none", "alpha":.85})

    ax = axes[1]
    pushed = affine_push(law, 2, Q(1, 10))
    ax.plot(t, curve(law, t), color=plum, linewidth=2, label="Before the carrier step")
    ax.plot(t, curve(pushed, t), color=teal, linewidth=2.4, label="After x → 2x + 1/10")
    ax.axhline(0, color="#888888", linewidth=.8)
    ax.set_title("B  An explicit operator transports the whole imprint", loc="left", pad=13)
    ax.set_ylabel("Centered pin height")
    ax.legend(frameon=False, loc="upper right", fontsize=10)
    ax.text(.02, .08, "The surface update equals the carrier update exactly.\nIdentity and composition are preserved.",
            transform=ax.transAxes, va="bottom", fontsize=10,
            bbox={"facecolor":"white", "edgecolor":"none", "alpha":.88})

    ax = axes[2]
    q = 3
    alias = CircleLaw(tuple((Q(j, q)+Q(k, 3*q), p/q) for j in range(q)
                           for k, p in ((0,Q(1,4)), (1,Q(3,8)), (2,Q(3,8)))))
    assert affine_push(alias, 16) == alias
    sampled = [Q(j, q) for j in range(q+1)]
    assert all(pin_surface(alias, x) == 0 for x in sampled)
    ax.plot(t, curve(alias, t), color=orange, linewidth=2.4, label="An atomic, ×16-invariant law")
    ax.axhline(0, color="#333333", linestyle="--", linewidth=1.3, label="Haar's complete surface")
    ax.scatter([float(x) for x in sampled], [0]*len(sampled), s=65, color=teal, zorder=4,
               label="Chosen pins agree exactly")
    ax.set_title("C  A finite bed can certify a relative match", loc="left", pad=13)
    ax.set_ylabel("Centered pin height")
    ax.set_xlabel("Probe position on the circle")
    ax.legend(frameon=True, facecolor="white", edgecolor="none", framealpha=.94,
              loc="upper right", fontsize=9.5)
    ax.text(.02, .08, "These sampled pins match Haar at every future ×16 step.\nThe complete surface distinguishes the two laws.",
            transform=ax.transAxes, va="bottom", fontsize=10,
            bbox={"facecolor":"white", "edgecolor":"none", "alpha":.9})

    for ax in axes:
        ax.set_xlim(0, 1)
        ax.set_xticks([0, .25, .5, .75, 1])
        ax.grid(axis="y", color="#e5e5e5", linewidth=.6)
        ax.set_axisbelow(True)
    fig.suptitle("THE FOURIER–YONEDA PIN BED", fontsize=18, fontweight="bold")
    dest = Path(__file__).resolve().parent
    fig.savefig(dest/"PINBED.png", dpi=160, facecolor="white")
    fig.savefig(dest/"PINBED.svg", facecolor="white", metadata={"Date": None})
    svg = dest/"PINBED.svg"
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines())+"\n")


if __name__ == "__main__":
    main()
