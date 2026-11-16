"""Reproduce the explanatory SVG from exact ratchet and window data.

Matplotlib is optional visualization tooling, not a dependency of the exact
implementation. Floating coordinates draw the picture; they certify nothing.
"""
from __future__ import annotations

from fractions import Fraction as Q
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2]))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from borwein_ratchet import RatchetState, window_mass


def main() -> None:
    purple, teal, gold, ink = "#7443b8", "#087f8c", "#c58a26", "#252b38"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "text.color": ink, "axes.labelcolor": ink,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "svg.hashsalt": "succ-borwein-ratchet-v1"})
    fig = plt.figure(figsize=(14.8, 9.1), facecolor="#fcfbff")
    grid = fig.add_gridspec(2, 2, width_ratios=(1.25, 1), hspace=.43, wspace=.15,
                           left=.07, right=.98, bottom=.11, top=.85)
    fig.suptitle("Two Borwein banks, one arithmetic carrier", x=.07, y=.96,
                 ha="left", fontsize=23, fontweight="bold")
    fig.text(.07, .906, "A growing support clock releases the pawl. A fixed window reads the degree.",
             fontsize=13, color="#616577")

    state, radii, events = RatchetState(), [], []
    for j in range(1, 501):
        update = state.advance(Q(1, 2*j+1))
        radii.append(float(update.after.radius))
        for tooth in update.releases:
            cert = update.certificate(tooth)
            events.append((j, tooth, float(update.after.radius), cert.approximate_log10_deficit()))
        state = update.after

    clock = fig.add_subplot(grid[0, 0], facecolor="#fcfbff")
    clock.plot(range(1, 501), radii, color=purple, lw=2.5)
    for tooth in (1, 2, 3):
        clock.axhline(tooth, color="#c8c6d4", lw=1, ls=(0, (4, 4)))
    for j, tooth, radius, logloss in events:
        clock.scatter(j, radius, s=55, color=purple, zorder=4)
        # Release labels sit below each threshold, away from the rising curve.
        label = f"tooth {tooth}: stage {j}\nloss ≈ 10$^{{{logloss:.1f}}}$"
        clock.annotate(label, (j, radius), xytext=(12, -51) if tooth < 3 else (-100, -82),
                       textcoords="offset points", fontsize=10, color=purple,
                       arrowprops={"arrowstyle": "-", "color": "#aaa0ba", "lw": .8})
    clock.set_xscale("log")
    clock.set_xlim(1, 650); clock.set_ylim(0, 3.6)
    clock.set_yticks((0, 1, 2, 3))
    clock.set_xlabel("Width inputs m (logarithmic scale)")
    clock.set_ylabel("Support radius Aₘ")
    clock.set_title("1   Release only when Aₘ > k", loc="left", fontweight="bold", pad=13)
    clock.text(.01, .97, "aⱼ = 1 / (2j + 1)", transform=clock.transAxes, va="top", color="#616577")

    gate = fig.add_subplot(grid[1, 0], facecolor="#fcfbff")
    charges = [Q(j, 80) for j in range(-20, 241)]
    masses = [window_mass((Q(1, 3), Q(1, 5)), shift=c) for c in charges]
    gate.plot([float(c) for c in charges], [float(x) for x in masses], color=teal, lw=2.5)
    for c, value, label, color in ((0, 1, "prime: 1", purple),
                                  (1, .5, "semiprime: ½", teal),
                                  (2, 0, "Ω ≥ 3: 0", "#657082")):
        gate.scatter(c, value, s=65, color=color, zorder=4)
        gate.annotate(label, (c, value), xytext=(12, 8), textcoords="offset points",
                      fontsize=10, color=color)
    gate.set_xlim(-.25, 3); gate.set_ylim(-.08, 1.25)
    gate.set_xticks((0, 1, 2, 3)); gate.set_yticks((0, .5, 1))
    gate.set_xlabel("Arithmetic charge c = Ω(n) − 1, for n ≥ 2")
    gate.set_ylabel("Normalized window mass B(c)")
    gate.set_title("2   Freeze the readout bank: (⅓, ⅕)", loc="left", fontweight="bold", pad=13)
    gate.text(.97, .94, "Tʳ = P₁ + 2⁻ʳP₂", ha="right", va="top",
              transform=gate.transAxes, color=teal, fontsize=12)

    cylinder = fig.add_subplot(grid[:, 1], projection="3d", facecolor="#fcfbff")
    theta, height = np.meshgrid(np.linspace(0, 2*np.pi, 45), np.linspace(0, 4, 9))
    cylinder.plot_surface(np.cos(theta), np.sin(theta), height, color=purple,
                          alpha=.035, linewidth=0, shade=False)
    for z in range(5):
        ring = np.linspace(0, 2*np.pi, 120)
        cylinder.plot(np.cos(ring), np.sin(ring), [z]*len(ring), color="#c8c6d4", lw=.7)
    t = np.linspace(0, 4, 600)
    cylinder.plot(np.cos(2*np.pi*t), np.sin(2*np.pi*t), t,
                  color="#9d8ab7", lw=1.3, alpha=.75)
    for n in range(1, 34):
        t0 = (n-1)/8
        x, y = np.cos(2*np.pi*t0), np.sin(2*np.pi*t0)
        prime = n >= 2 and all(n % d for d in range(2, int(n**.5)+1))
        color = gold if n == 1 else purple if prime else "#98a0ac"
        cylinder.scatter(x, y, t0, s=42 if prime else 24, c=color, depthshade=False)
        if (prime and n != 31) or n in (1, 9, 17, 25, 33):
            cylinder.text(1.12*x, 1.12*y, t0, str(n), color=color, fontsize=9)
    cylinder.set_xlim(-1.25, 1.25); cylinder.set_ylim(-1.25, 1.25); cylinder.set_zlim(0, 4.2)
    cylinder.set_xticks([]); cylinder.set_yticks([]); cylinder.set_zticks(range(5))
    cylinder.set_zlabel("Retained turns + angular fraction", labelpad=12)
    cylinder.set_box_aspect((1, 1, 2.1)); cylinder.view_init(elev=14, azim=-53)
    cylinder.set_title("3   Keep the winding\nsource n = 1 + 8h + r", fontsize=13,
                       fontweight="bold", pad=10)
    cylinder.xaxis.pane.fill = cylinder.yaxis.pane.fill = cylinder.zaxis.pane.fill = False
    cylinder.grid(False)
    fig.text(.66, .086, "● prime source", color=purple, fontsize=10)
    fig.text(.79, .086, "● composite intermediate", color="#657082", fontsize=10)
    fig.text(.07, .038,
             "Exact rational release decisions and integer-charge values. Curves illustrate the formulas; the helix shows successor order, not elapsed clock time.",
             fontsize=10, color="#616577")
    destination = HERE / "figures/borwein_ratchet.svg"
    destination.parent.mkdir(exist_ok=True)
    fig.savefig(destination, format="svg", metadata={"Date": None}, facecolor=fig.get_facecolor())
    destination.write_text("\n".join(line.rstrip() for line in destination.read_text().splitlines()) + "\n")
    # This raster is a temporary visual-QA rendering, not a second deliverable.
    preview = HERE.parents[3] / "borwein_ratchet_preview.png"
    fig.savefig(preview, dpi=140, facecolor=fig.get_facecolor())
    print(destination)
    print(preview)


if __name__ == "__main__":
    main()
