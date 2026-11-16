"""Render the exact local p=3 interference example; plots are illustrations.

The theorem and exact rational receipts carry the proof. Matplotlib is only
used for drawing the already computed values. Optional PNG is a preview.
"""
from pathlib import Path
import argparse

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from prime_waves import local_pair_factor, survivor_wave


def render(preview=None):
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "svg.hashsalt": "succ-prime-wave-2026-11-12",
                         "svg.fonttype": "none", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(12.4, 7.2), sharex=True,
                             gridspec_kw={"height_ratios": [1.1, 1]},
                             layout="constrained")
    purple, teal, ink = "#7446B8", "#157F87", "#252B3C"
    positions = list(range(12))
    for column, target in enumerate((30, 32)):
        first = [float(survivor_wave(3, n)) for n in positions]
        second = [float(survivor_wave(3, target - n)) for n in positions]
        product = [x * y for x, y in zip(first, second)]
        average = local_pair_factor(3, target)
        top, bottom = axes[0, column], axes[1, column]
        top.plot(positions, first, "o-", color=purple, linewidth=1.7,
                 markersize=7, markerfacecolor="white", label=r"$w_3(n)$")
        top.plot(positions, second, "x--", color=teal, linewidth=1.2,
                 markersize=7, label=r"$w_3(N-n)$")
        explanation = ("One forbidden residue: 0" if target == 30
                       else "Two forbidden residues: 0 and 2")
        top.set_title(f"Target N = {target}   |   {explanation}",
                      loc="left", fontsize=12, color=ink, pad=14)
        top.set_ylim(-0.18, 2.02)
        top.set_yticks((0, 1, 1.5), ("0", "1", "3/2"))
        top.legend(loc="upper center", ncols=2, frameon=False, fontsize=10)
        bottom.vlines(positions, 0, product, color=purple, linewidth=3, alpha=.5)
        bottom.scatter(positions, product, color=purple, s=45, zorder=3)
        bottom.axhline(float(average), color=teal, linewidth=1.7, linestyle="--",
                       label=f"Complete-period mean = {average}")
        bottom.set_ylim(-.15, 2.65)
        bottom.set_yticks((0, .75, 1.5, 2.25), ("0", "3/4", "3/2", "9/4"))
        bottom.legend(loc="upper center", frameon=False, fontsize=10)
        bottom.set_xlabel("Integer position n on the common carrier")
        for ax in (top, bottom):
            ax.set_xlim(-.45, 11.45)
            ax.xaxis.set_major_locator(MultipleLocator(1))
            ax.grid(axis="y", color="#E6E8EE", linewidth=.8)
            ax.set_axisbelow(True)
            ax.tick_params(length=0, pad=6)
    axes[0, 0].set_ylabel("Normalized survivor wave")
    axes[1, 0].set_ylabel("Reflected wave product")
    fig.suptitle("One prime's interference detects the target's arithmetic",
                 fontsize=18, fontweight="bold", color=ink)
    fig.supxlabel("Exact integer samples for p = 3; connecting segments guide the eye.\n"
                  "These full-period correlations are local factors, not prime-pair counts.",
                  fontsize=10, color="#535A6D")
    destination = Path(__file__).resolve().parent / "figures/prime_wave_interference.svg"
    destination.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destination, metadata={"Date": None,
                                       "Description": "Exact local prime-wave correlation illustration, p=3."})
    # Matplotlib pads SVG path lines; normalize source whitespace for Git.
    destination.write_text("\n".join(line.rstrip() for line in
                                    destination.read_text().splitlines()) + "\n")
    if preview:
        fig.savefig(preview, dpi=150)
    plt.close(fig)
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview", help="Optional local PNG preview path")
    args = parser.parse_args()
    print(render(args.preview))
