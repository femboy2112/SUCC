"""Display-only scientific figure; exact claims are in proofs and receipts."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).resolve().parent
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15,
                         "svg.hashsalt": "succ-driven-pinbed-2026-11-07"})
    fig, axes = plt.subplots(3, 1, figsize=(10.5, 12), constrained_layout=True)
    fig.suptitle("DRIVE THE PIN BED", fontsize=24, fontweight="bold")
    x = np.linspace(0, 1, 1001)
    a = axes[0]
    # alpha=1/2, source density 1+0.6*cos(4*pi*x). Static profile is Haar's.
    delta_r1 = .3*(2j/np.pi*np.exp(4j*np.pi*x)
                    - 2j/(3*np.pi)*np.exp(-4j*np.pi*x))
    a.axhline(0, color="#343a40", linestyle="--", linewidth=2,
              label="Static profile difference: exactly zero")
    a.plot(x, delta_r1.real, color="#7b3fb3", linewidth=3,
           label="Driven in-phase response")
    a.plot(x, delta_r1.imag, color="#008b98", linewidth=3,
           label="Driven quadrature response")
    xx = np.arange(0, 1+1/24, 1/24)
    yy = .3*(2j/np.pi*np.exp(4j*np.pi*xx)-2j/(3*np.pi)*np.exp(-4j*np.pi*xx))
    a.vlines(xx, 0, yy.real, color="#7b3fb3", alpha=.3)
    a.scatter(xx, yy.real, color="#7b3fb3", s=15, zorder=4)
    a.set(title="A  The oscillator makes a hidden density mode visible",
          xlabel="Translated pin position", ylabel="Response minus Haar reference",
          xlim=(0, 1), ylim=(-.34, .34))
    a.text(.02, -.315, r"Source density: $1+0.6\cos(4\pi x)$   |   Aperture: $1/2$",
           fontsize=11, bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    a.legend(loc="upper right", fontsize=10, framealpha=.95)

    a = axes[1]
    h = np.arange(1, 33)
    static = np.where(h % 2, 4/np.pi**2, 0.)
    weights = np.where(h % 2, 4/(np.pi**2*h*h),
                       4*(h*h+1)/(np.pi**2*np.maximum((h*h-1)**2, 1)))
    weights[0] = 4/np.pi**2 + .5
    a.scatter(h, static, facecolors="none", edgecolors="#a1a7ad", s=45,
              label=r"Static aperture: $h^2 w_h$", zorder=3)
    a.plot(h, h*h*weights, color="#008b98", marker="o", markersize=4,
           linewidth=1.8, label=r"Driven pair: $h^2 w_h$", zorder=4)
    lower, upper = 4/np.pi**2, 4/np.pi**2+.5
    a.axhspan(lower, upper, color="#008b98", alpha=.08)
    a.axhline(lower, color="#008b98", linestyle=":", alpha=.7)
    a.axhline(upper, color="#008b98", linestyle=":", alpha=.7)
    a.set(title="B  Every Fourier mode has a controlled response",
          xlabel="Source frequency h", ylabel="Frequency-scaled sensitivity",
          xlim=(0, 33), ylim=(-.08, 1.05))
    a.legend(loc="upper right", fontsize=10, framealpha=.95)
    a.text(14, .68, r"Sharp band: $4/\pi^2\leq h^2 w_h\leq 4/\pi^2+1/2$",
           fontsize=11, bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})

    a = axes[2]
    pins = np.array([4, 8, 16, 32, 64])
    z = (np.pi/pins/np.sin(np.pi/pins))**2
    dc = 1/(6*pins*pins)
    a.plot(pins, z, "o-", color="#7b3fb3", linewidth=2.5,
           label="Coherent scan: signed mode estimate")
    a.axhline(1, color="#008b98", linestyle="--", linewidth=2,
              label="Actual locked source: first mode = 1")
    a.plot(pins, dc, "s-", color="#cb6a14", linewidth=2.5,
           label="Unreferenced scan average")
    a.set_xscale("log", base=2)
    a.set_xticks(pins, [str(p) for p in pins])
    a.set(title="C  Keep the oscillator reference: scanning alone can mislead",
          xlabel="Number of B2 pin samples M", ylabel="Readout on a fixed atom",
          ylim=(-.15, 1.36))
    a.legend(loc="center right", fontsize=10, framealpha=.95)
    a.text(4.2, -.12, "The raw average tends to zero even though the source never moves.",
           fontsize=11, bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    for a in axes:
        a.grid(alpha=.15)
        a.spines[["top", "right"]].set_visible(False)
    fig.savefig(out/"DRIVEN_PINBED.png", dpi=160)
    fig.savefig(out/"DRIVEN_PINBED.svg", metadata={"Date": None})
    svg = out/"DRIVEN_PINBED.svg"
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines())+"\n")


if __name__ == "__main__":
    main()
