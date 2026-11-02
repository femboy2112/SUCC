"""Analysis of dft_scaling_raw.json: scaling of max_{ell!=0}|D_hat| and energy vs L."""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
raw = json.load(open(HERE / "dft_scaling_raw.json"))

# Group by (L) across h, take max; also per-h
from collections import defaultdict
by_L = defaultdict(list)
for r in raw:
    by_L[r["L"]].append(r)

# For each L, aggregate: max over h of max_ell_neq0, and median
rows = []
for L, recs in sorted(by_L.items()):
    maxs = [r["max_ell_neq0"] for r in recs]
    energy = [r["total_energy"] for r in recs]
    rows.append((L, max(maxs), min(maxs), sum(maxs)/len(maxs),
                 sum(energy)/len(energy), len(recs)))

print("=== max_{ell!=0}|D_hat| vs L (aggregated over h) ===")
print(f"{'L':>5} {'maxMax':>12} {'minMax':>12} {'meanMax':>12} {'meanEnergy':>14}")
for L, mx, mn, avg, e, n in rows:
    print(f"{L:>5} {mx:>12.6e} {mn:>12.6e} {avg:>12.6e} {e:>14.6f}")

# Fit power law: maxMax ~ C * L^{-alpha}  via log-log regression
import statistics
def fit_powerlaw(rows):
    # use meanMax vs L
    pts = [(L, avg) for L, _, _, avg, *_ in rows if L > 0]
    xs = [math.log(L) for L, _ in pts]
    ys = [math.log(max(avg, 1e-300)) for _, avg in pts]
    n = len(xs)
    sx = sum(xs); sy = sum(ys)
    sxx = sum(x*x for x in xs); sxy = sum(x*y for x, y in zip(xs, ys))
    slope = (n*sxy - sx*sy)/(n*sxx - sx*sx)
    intercept = (sy - slope*sx)/n
    return slope, intercept, xs, ys

slope, intercept, xs, ys = fit_powerlaw(rows)
print(f"\n=== power-law fit: meanMax ~ C * L^slope ===")
print(f"alpha (meanMax) = {slope:.4f}  (log-log slope, so meanMax ~ L^{slope:.4f})")
print(f"C = exp({intercept:.4f}) = {math.exp(intercept):.4f}")

# R^2
import math
def r2(xs, ys, slope, intercept):
    ym = sum(ys)/len(ys)
    ss_tot = sum((y-ym)**2 for y in ys)
    ss_res = sum((y - (slope*x+intercept))**2 for x, y in zip(xs, ys))
    return 1 - ss_res/ss_tot
print(f"R^2 = {r2(xs, ys, slope, intercept):.4f}")

# Fit per-h alpha
print("\n=== per-h alpha (max_ell_neq0 vs L) ===")
for h in [1, 3, 5]:
    subh = [(r["L"], r["max_ell_neq0"]) for r in raw if r["h"] == h]
    subh.sort()
    xsh = [math.log(ll) for ll, _ in subh]
    ysh = [math.log(max(vv, 1e-300)) for _, vv in subh]
    nh = len(xsh)
    sxh = sum(xsh); syh = sum(ysh)
    sxxh = sum(xx*xx for xx in xsh); sxyh = sum(xx*yy for xx, yy in zip(xsh, ysh))
    denom = nh*sxxh - sxh*sxh
    a = (nh*sxyh - sxh*syh)/denom
    b = (syh - a*sxh)/nh
    rrh = r2(xsh, ysh, a, b)
    print(f"  h={h}: alpha={a:.4f}, R^2={rrh:.4f}, n={nh}")

# Energy: Parseval gives sum|D_hat|^2 = (1/L) sum|D|^2. Check.
print("\n=== energy relation: sum_ell |D_hat|^2 vs (1/L) sum_r |D(r)|^2 ===")
# recompute |D(r)|^2 = 4 sin^2(pi h delta) -> need delta; instead check against reported energy scaling
sub = sorted(set(r["L"] for r in raw))
for L in sub[:5] + sub[-5:]:
    recs = [r for r in raw if r["L"] == L]
    e = sum(r["total_energy"] for r in recs)/len(recs)
    print(f"  L={L}: meanEnergy={e:.6f}")

# Correlation of maxMax with L
Ls = [L for L,*_ in rows]
mm = [mx for L, mx, *_ in rows]
import statistics
corr = statistics.correlation([math.log(L) for L in Ls], [math.log(m) for m in mm])
print(f"\ncorr(log L, log maxMax) = {corr:.4f}")
