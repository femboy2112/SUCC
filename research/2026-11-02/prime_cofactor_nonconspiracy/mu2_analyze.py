"""Analyze mu2_sweep.json: averages, scaling vs L, mod-8 split, claim ledger inputs."""
from __future__ import annotations
import json, statistics
from collections import defaultdict

with open("mu2_sweep.json") as f:
    data = json.load(f)

rows = data["rows"]

# group by h
by_h = defaultdict(list)
for r in rows:
    by_h[r["h"]].append(r)

print("=" * 70)
print("MU2 EMPIRICAL SUMMARY (dps=%d)" % data["dps"])
print("=" * 70)

for h in [1, 3, 5]:
    rs = by_h[h]
    half = [r["mu2_half"] for r in rs]
    full = [r["mu2_full"] for r in rs]
    n = len(rs)
    print(f"\n--- h = {h}  (n = {n} primes) ---")
    print(f"  mu2_half  mean = {statistics.mean(half):.6f}   median = {statistics.median(half):.6f}   stdev = {statistics.pstdev(half):.6f}")
    print(f"  mu2_full  mean = {statistics.mean(full):.6f}   median = {statistics.median(full):.6f}   stdev = {statistics.pstdev(full):.6f}")
    # random-phase reference: sin^2(pi h delta/2) mean = 1/2 for uniform delta; sin^2(pi h delta) mean = 1/2 too
    print(f"  (random-phase reference = 0.500000 for both)")

    # mod-8 split
    for mod8 in [1, 5]:
        sub = [r for r in rs if r["mod8"] == mod8]
        mh = statistics.mean(r["mu2_half"] for r in sub)
        mf = statistics.mean(r["mu2_full"] for r in sub)
        print(f"    p={mod8} mod 8 (n={len(sub)}): mu2_half mean = {mh:.6f}, mu2_full mean = {mf:.6f}")

    # scaling vs L: bucket by L
    print("  scaling vs L (mu2_half):")
    buckets = [(0, 50), (50, 100), (100, 200), (200, 400), (400, 1000)]
    for lo, hi in buckets:
        sub = [r for r in rs if lo <= r["L"] < hi]
        if sub:
            mh = statistics.mean(r["mu2_half"] for r in sub)
            mf = statistics.mean(r["mu2_full"] for r in sub)
            print(f"    L in [{lo},{hi}): n={len(sub):3d}  mu2_half={mh:.6f}  mu2_full={mf:.6f}  mean_L={statistics.mean(r['L'] for r in sub):.0f}")

    # count how many below 0.4 / above 0.6
    below04 = sum(1 for x in half if x < 0.4)
    above06 = sum(1 for x in half if x > 0.6)
    print(f"  mu2_half < 0.4 : {below04}/{n}   > 0.6 : {above06}/{n}")

# correlation mu2_half vs L and vs p
import math
for h in [1,3,5]:
    rs = by_h[h]
    xs = [r["L"] for r in rs]
    ys = [r["mu2_half"] for r in rs]
    mx, my = statistics.mean(xs), statistics.mean(ys)
    cov = sum((x-mx)*(y-my) for x,y in zip(xs,ys))
    vx = sum((x-mx)**2 for x in xs); vy = sum((y-my)**2 for y in ys)
    corr = cov/math.sqrt(vx*vy)
    print(f"\n  Pearson corr(mu2_half, L) for h={h}: {corr:.4f}")
    xs2 = [r["p"] for r in rs]
    mx2 = statistics.mean(xs2)
    cov2 = sum((x-mx2)*(y-my) for x,y in zip(xs2,ys))
    vx2 = sum((x-mx2)**2 for x in xs2)
    print(f"  Pearson corr(mu2_half, p) for h={h}: {cov2/math.sqrt(vx2*vy):.4f}")
