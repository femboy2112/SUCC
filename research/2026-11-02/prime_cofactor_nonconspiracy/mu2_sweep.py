"""Sweep mu_2(h) over p=1 mod4 primes < 3000, h in {1,3,5}, two methods, dps=2000."""
from __future__ import annotations
import json, time, statistics
from mu2_engine import compute_mu2, primes_range, ord_p

DPS = 2000
PS = [p for p in primes_range(7, 3000) if p % 4 == 1]
HS = [1, 3, 5]

rows = []
t0 = time.time()
for i, p in enumerate(PS):
    L = ord_p(16, p)
    for h in HS:
        r = compute_mu2(p, h, DPS)
        # verify two methods agree
        assert abs(r["mu2_half_A"] - r["mu2_half_B"]) < 1e-12
        assert abs(r["mu2_full_A"] - r["mu2_full_B"]) < 1e-12
        rows.append({
            "p": p, "mod8": p % 8, "L": L, "h": h,
            "mu2_half": r["mu2_half_A"],
            "mu2_full": r["mu2_full_A"],
        })
    if (i + 1) % 20 == 0:
        print(f"  {i+1}/{len(PS)} primes done, elapsed {time.time()-t0:.0f}s", flush=True)

print(f"DONE {len(rows)} rows in {time.time()-t0:.0f}s", flush=True)
with open("mu2_sweep.json", "w") as f:
    json.dump({"dps": DPS, "primes": PS, "rows": rows}, f, indent=1)
print("saved mu2_sweep.json", flush=True)
