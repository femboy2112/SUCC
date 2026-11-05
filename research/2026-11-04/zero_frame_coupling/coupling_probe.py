"""Unwrapped BBP coupling and certified complete-factorial observations.

Stdlib only. All trig reductions precede numerical approximation and all
reported sums have rational error bounds. Infinite claims require proofs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import gzip
import hashlib
import json
from math import comb, isqrt, lcm
from pathlib import Path

from certified_phase import (CHAR_ERROR, OUTPUT, character_grid,
                             critical_schedule, forcing, tail_interval)

BASE = "bc2d7b01b6b0a37cb79994e180758e98681aa68e"
P = tuple(map(F, (4, 0, 0, -2, -1, -1, 0, 0)))
RAD = (F(2), F(-2), F(-1), F(-2), F(-1, 2), F(-1, 2), F(1, 4), F(0))
ANG = tuple(a-b for a, b in zip(P, RAD))


def injection(n, taps):
    return sum((c/F(8*(n-1)+j) for j, c in enumerate(taps, 1)), F(0))


def collapsed(n):
    """Independent integer polynomials, checked symbolically in focused tests."""
    o = F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    poly = 30720*n**6-93952*n**5+111840*n**4-65764*n**3+19857*n*n-2848*n+144
    r = F(-2*poly, (2*n-1)*(4*n-3)*(4*n-1)*(8*n-7)*(8*n-5)*(8*n-3)*(8*n-1))
    return o, o-r, r


def floorq(x):
    return x.numerator//x.denominator


def qhex(x):
    """Canonical exact lift encoding without Python's decimal digit limit."""
    return f"{x.numerator:x}/{x.denominator:x}"


def states(N):
    """Keep ALL unwrapped values, validate an independent integer-LCM lift."""
    streams = [[F(0)] for _ in range(3)]
    L = 1
    V = [0, 0, 0]
    history = hashlib.sha256()
    carry_hash = hashlib.sha256()
    carry_rows = []
    for n in range(1, N+1):
        rs = (forcing(n), injection(n, ANG), injection(n, RAD))
        independent = collapsed(n)
        assert rs == independent
        nextL = lcm(L, *(x.denominator for x in independent))
        V = [16*v*(nextL//L)+q.numerator*(nextL//q.denominator)
             for v, q in zip(V, independent)]
        L = nextL
        carries = []
        for lane, r, v in zip(streams, rs, V):
            x = 16*lane[-1]+r
            assert x == F(v, L)
            c = floorq(16*(lane[-1] % 1)+r)
            assert x % 1 == 16*(lane[-1] % 1)+r-c
            carries.append(c)
            lane.append(x)
        assert streams[0][-1] == streams[1][-1]+streams[2][-1]
        assert streams[2][-1] > 0
        row = [qhex(lane[-1]) for lane in streams]
        history.update((str(n)+":"+"|".join(row)+"\n").encode())
        carry_hash.update((str(n)+":"+str(carries)+"\n").encode())
        carry_rows.append(carries)
    return streams, {"N": N, "zero_initial_values": ["0", "0", "0"],
                     "state_transcript_sha256": history.hexdigest(),
                     "carry_transcript_sha256": carry_hash.hexdigest(),
                     "literal_carries": carry_rows,
                     "integer_LCM_bits": L.bit_length(),
                     "reconciled_unwrapped_states": 3*N}


def radial_coefficients(order):
    """Independent from #506's moments: solve z(x)-16z(x-1)=r_rad(x)."""
    zs = [F(0)]
    for k in range(1, order+1):
        r = sum((c*F((8-j)**(k-1), 8**k) for j, c in enumerate(RAD, 1)), F(0))
        zs.append(-(r+16*sum((comb(k-1, d-1)*zs[d] for d in range(1, k)), F(0)))/15)
    return zs


def jet_weights(m):
    z = radial_coefficients(m+1)
    matrix = []
    for k in range(2, m+2):
        row = [sum((z[d]*(-1)**(k-d)*comb(k-1, d-1)*ell**(k-d)
                    for d in range(1, k)), F(0)) for ell in range(1, m+1)]
        c = sum((a*F((8-j)**(k-1), 8**k) for j, a in enumerate(P, 1)), F(0))
        matrix.append(row+[-c])
    for j in range(m):
        pivot = next(i for i in range(j, m) if matrix[i][j])
        matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
        q = matrix[j][j]
        matrix[j] = [x/q for x in matrix[j]]
        for i in range(m):
            if i != j:
                q = matrix[i][j]
                matrix[i] = [a-q*b for a, b in zip(matrix[i], matrix[j])]
    return tuple(row[-1] for row in matrix)


@lru_cache(maxsize=32768)
def phase_point(phase, radius=F(0)):
    return character_grid(phase, radius)


def weighted_point(point, w):
    return tuple(floorq(F(c)*w) for c in point)


def summary(points, error, A):
    """All consecutive prefix chords, including singletons and interior chords."""
    pref = [(0, 0)]
    for x, y in points:
        u, v = pref[-1]
        pref.append((u+x, v+y))
    best, witness = -1, None
    for b in range(1, len(pref)):
        for a in range(b):
            d = (pref[b][0]-pref[a][0])**2+(pref[b][1]-pref[a][1])**2
            if d > best:
                best, witness = d, [a, b]
    root = isqrt(best)
    radius = error*F(len(points), A)
    return {"signed_mean_grid": [str(F(c, A*OUTPUT)) for c in pref[-1]],
            "complex_error": str(radius),
            "M_interval": [str(max(F(0), F(root, A*OUTPUT)-radius)),
                           str(F(root+1, A*OUTPUT)+radius)],
            "witness_offsets": witness,
            "chords": len(points)*(len(points)+1)//2}


def factorial_contrasts(rows):
    """Unnormalized mixed differences over each subset of four binary factors."""
    out = []
    for mask in range(1, 16):
        vals = [F(0), F(0)]
        err = F(0)
        for sub in range(16):
            if sub & ~mask:
                continue
            sign = (-1)**((mask.bit_count()-sub.bit_count()))
            row = rows[sub]
            for j in (0, 1):
                vals[j] += sign*F(row["signed_mean_grid"][j])
            err += F(row["complex_error"])
        out.append({"mask": mask, "signed_grid": list(map(str, vals)),
                    "complex_error": str(err), "meaning": "finite nonadditivity only"})
    return out


def run_case(A, H, label, state_data, raw):
    (U, Y, Z), _ = state_data
    rows = []
    weight_error = 3*CHAR_ERROR+F(2, OUTPUT)
    for mask in range(16):
        sign = -1 if mask & 1 else 1
        seed = F(1, 5) if mask & 2 else F(0)
        lag = 1 if mask & 4 else 0
        reciprocal = bool(mask & 8)
        pts = []
        phase_hash = hashlib.sha256()
        for n in range(A, 2*A):
            # Seed is assigned to the angular channel before orientation reversal.
            phase = H*(sign*(Y[n]+16**n*seed)+Z[n+lag])
            phase_hash.update((qhex(phase)+"\n").encode())
            assert (H*sign*16**n*seed-H*sign*seed) % 1 == 0
            w = F(8*A**3, 3*n**3) if reciprocal else F(1)
            pts.append(weighted_point(phase_point(phase % 1), w))
        item = summary(pts, weight_error, A)
        item.update({"mask": mask, "angular_orientation": sign, "seed": str(seed),
                     "lag": lag, "measure": "reciprocal" if reciprocal else "uniform",
                     "unwrapped_phase_sha256": phase_hash.hexdigest()})
        rows.append(item)
        raw.append({"case": label, "mask": mask, "points": pts})
    controls = []
    for kind in ("radial", "coherent_same_forcing", "coherent_lag1", "anti_companion"):
        pts = []
        for n in range(A, 2*A):
            radius = F(0)
            if kind == "radial":
                phase = H*Z[n]
            elif kind == "anti_companion":
                phase = F(0)
            else:
                lo, hi = tail_interval(n)
                phase = -H*(lo+hi)/2
                radius = abs(H)*(hi-lo)/2
                if kind == "coherent_lag1":
                    phase += H*(Z[n+1]-Z[n])
            pts.append(phase_point(phase % 1, radius))
        controls.append({"kind": kind, **summary(pts, CHAR_ERROR, A)})
        raw.append({"case": label, "control": kind, "points": pts})
    # Seed 1/5 MUST preserve every maximal magnitude, even for reversed angular.
    for mask in range(16):
        rows[mask]["seed_transport_phase"] = str((-H*rows[mask]["angular_orientation"]*F(rows[mask]["seed"])) % 1)
        rows[mask]["source_aligned_signed_mean_grid"] = rows[mask & ~2]["signed_mean_grid"]
        rows[mask]["source_aligned_seed_defect"] = "0 (exact phase identity)"
        if not mask & 2:
            a, b = rows[mask]["M_interval"], rows[mask | 2]["M_interval"]
            assert max(F(a[0]), F(b[0])) <= min(F(a[1]), F(b[1]))
    return {"A": A, "signed_H": H, "Lambda": str(F(abs(H), A*A)),
            "schedule_label": label, "factor_cells": rows,
            "complete_mixed_differences": factorial_contrasts(rows), "controls": controls}


def run():
    data = states(1025)
    raw, cases = [], []
    for A, h, name in ((128, 1, "development_actual_h1"),
                       (256, 7, "fresh_actual_h7"),
                       (512, -3, "fresh_actual_hminus3")):
        depth, H = critical_schedule(A, h)
        row = run_case(A, H if h > 0 else -H, name, data, raw)
        row.update({"h": h, "depth": depth})
        cases.append(row)
    for A, H, name in ((128, 128*128**2, "diagnostic_reciprocal_tuned"),
                       (256, 7, "diagnostic_fixed_character")):
        cases.append(run_case(A, H, name, data, raw))
    base = Path(__file__).parent
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in (base/"coupling_probe.py", base/"certified_phase.py")}
    raw_bytes = json.dumps(raw, sort_keys=True, separators=(",", ":")).encode()
    receipt = {"source_base": BASE, "instrument_hashes": hashes,
               "authority": "exact finite rational enclosures; no asymptotic inference",
               "state_audit": data[1], "cases": cases,
               "raw_grid_sha256": hashlib.sha256(raw_bytes).hexdigest(),
               "total_chords": sum(r["chords"] for c in cases
                                   for r in c["factor_cells"]+c["controls"])}
    return receipt, raw_bytes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    receipt, raw = run()
    if args.write:
        args.write.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
        args.write.with_name("RAW_GRID.json.gz").write_bytes(gzip.compress(raw, mtime=0))
    if args.verify:
        assert receipt == json.loads(args.verify.read_text())
        assert raw == gzip.decompress(args.verify.with_name("RAW_GRID.json.gz").read_bytes())
    print(json.dumps({"status": "PASS", "cases": len(receipt["cases"]),
                      "factorial_cells": 16*len(receipt["cases"]),
                      "chords": receipt["total_chords"],
                      "state_sha256": receipt["state_audit"]["state_transcript_sha256"]}))


if __name__ == "__main__":
    main()
