#!/usr/bin/env python
"""carry_transport_probe.py - Front B instrument driver (Daniel Bernoulli).

Stages (each writes data/<stage>.json; `all` merges into FINITE_RECEIPT.json):
  calibrate  Exp 1   known facts, hand case, pi-digit routes
  cb1        Exp 2   CB-1 exact check, oracle A (Fraction) vs oracle B (big-int), mutants, boundary
  cb1g       Exp 3   CB-1g gauge check with rigorous Green tail and pi (gauge-verification only)
  trueseed   Exp 4   exact J for s=0, s=1/5, coherent s*=-pi/16
  cb3        Exp 5   CB-3 countermodel sweep (calls countermodel_cb3)
  j2         Exp 6   second-order selected carry statistic
Usage:  python carry_transport_probe.py --stage calibrate|cb1|cb1g|trueseed|cb3|j2|all [--quick] [--procs N]
Never run under `python -I`.  mpmath precision is ALWAYS locally scoped (mp.workdps).
"""
import argparse
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import oracle_b as OB  # noqa: E402

DATA = os.path.join(HERE, "data")
EPOCHS = [64, 173, 347, 691, 1024, 4096]
SEEDS = [(0, 1), (1, 5), (1, 3), (3, 7), (5, 17)]


# ====================================================================== oracle A (Fractions)
def r_frac(spec, n):
    t = Fraction(0)
    for (num, den, off) in spec["poles"]:
        t += Fraction(num, den * (8 * n - off))
    t += Fraction(*spec["const"])
    t *= spec["sign"]
    if spec["alt"] and (n & 1):
        t = -t
    return t


def S_direct(spec, n, k, cache):
    key = (n, k)
    v = cache.get(key)
    if v is None:
        v = Fraction(0)
        for j in range(1, k + 1):
            v += 16 ** (k - j) * r_frac(spec, n + j)
        cache[key] = v
    return v


def run_oracle_A(spec, A, dcap, seed=(0, 1)):
    """Repo definitions with Fraction arithmetic.  Same record schema as IntOracle.run()."""
    p, q = seed
    nlast = 2 * A - 1 + dcap + 2
    x = Fraction(0)
    xs = {}
    for n in range(1, nlast + 1):
        x = (16 * x + r_frac(spec, n)) % 1
        if n >= A:
            xs[n] = (x + Fraction((p * pow(16, n, q)) % q, q)) % 1
    triples = [(m, d - m) for d in range(2, dcap + 1) for m in range(1, d)]
    rec = {t: dict(nadm=0, mm_b_adm=0, mm_d_adm=0, mm_b_inadm=0, mm_d_inadm=0, n_inadm=0, sum_b=0,
                   sum_delta=Fraction(0), min_margin=None, min_margin_n=None,
                   bits_def=bytearray(), bits_claim=bytearray()) for t in triples}
    cache = {}
    for n in range(A, 2 * A):
        xn = xs[n]
        theta = {}
        for d in range(2, dcap + 1):
            theta[d] = Fraction(16 ** d * xn.numerator, xn.denominator) % 1
        for (m, k) in triples:
            d = m + k
            Sk = S_direct(spec, n, k, cache)
            delta = (16 ** m * Sk) % 1
            b_def = 1 if theta[d] + delta >= 1 else 0
            Sd = S_direct(spec, n, d, cache)
            Sm = S_direct(spec, n + k, m, cache)
            b_cl = 1 if (Sm <= xs[n + d] < Sd) else 0
            dl_cl = Sd - Sm
            rr = rec[(m, k)]
            rr["bits_def"].append(b_def)
            rr["bits_claim"].append(b_cl)
            rr["sum_b"] += b_def
            rr["sum_delta"] += delta
            mmb = b_def != b_cl
            mmd = delta != dl_cl
            if Sd < 1:
                rr["nadm"] += 1
                mg = 1 - Sd
                if rr["min_margin"] is None or mg < rr["min_margin"]:
                    rr["min_margin"], rr["min_margin_n"] = mg, n
                rr["mm_b_adm"] += mmb
                rr["mm_d_adm"] += mmd
            else:
                rr["n_inadm"] += 1
                rr["mm_b_inadm"] += mmb
                rr["mm_d_inadm"] += mmd
        if len(cache) > 4000:
            cache.clear()
    out = {}
    for (m, k), rr in rec.items():
        out["%d,%d" % (m, k)] = dict(
            m=m, k=k, d=m + k, nadm=rr["nadm"], n_inadm=rr["n_inadm"],
            mm_b_adm=rr["mm_b_adm"], mm_d_adm=rr["mm_d_adm"], mm_b_inadm=rr["mm_b_inadm"],
            mm_d_inadm=rr["mm_d_inadm"], sum_b=rr["sum_b"], sum_delta=rr["sum_delta"],
            min_margin=rr["min_margin"], min_margin_n=rr["min_margin_n"],
            digest_b_def=OB.digest_bits(rr["bits_def"]), digest_b_claim=OB.digest_bits(rr["bits_claim"]))
    return out


# ====================================================================== helpers
def dcap_for(spec_name, A):
    if spec_name == "M2_const_1_1000" or spec_name == "M3_unforced":
        return 5
    return int(math.floor(math.log(64 * A * A, 16))) + 2


def spec_by_name(name):
    if name == "source":
        return OB.SOURCE
    return OB.mutant_specs()[name]


def cb1_task(args):
    """one (spec, seed, A) cell: run both oracles, cross-compare, summarise."""
    spec_name, seed, A, run_a = args
    t0 = time.time()
    spec = spec_by_name(spec_name)
    dcap = dcap_for(spec_name, A)
    ob = OB.IntOracle(spec, A, dcap, seed)
    rb = ob.run()
    tb = time.time() - t0
    ra = None
    ta = None
    if run_a:
        t1 = time.time()
        ra = run_oracle_A(spec, A, dcap, seed)
        ta = time.time() - t1
    rows = []
    cross_dis = 0
    for key, v in rb.items():
        row = dict(spec=spec_name, seed="%d/%d" % seed, A=A, m=v["m"], k=v["k"], d=v["d"],
                   nadm=v["nadm"], n_inadm=v["n_inadm"],
                   B_mm_b_adm=v["mm_b_adm"], B_mm_d_adm=v["mm_d_adm"],
                   B_mm_b_inadm=v["mm_b_inadm"], B_mm_d_inadm=v["mm_d_inadm"],
                   sum_b=v["sum_b"], sum_delta=str(Fraction(v["sum_delta_num"], v["sum_delta_den"]).limit_denominator(10 ** 30)) if False else None,
                   J_num_den=None, min_margin=None, min_margin_n=v["min_margin_n"],
                   mismatch_classes=v["mismatch_classes"], examples=v["examples"])
        sd = Fraction(v["sum_delta_num"], v["sum_delta_den"])
        row["sum_delta_float"] = float(sd)
        row["J"] = Fraction(v["sum_b"]) / A - sd / A
        row["J_float"] = float(row["J"])
        row["J_sign"] = (row["J"] > 0) - (row["J"] < 0)
        row["J_str"] = ("%+.18e" % float(row["J"]))
        if v["min_margin_frac"] is not None:
            mg = Fraction(*v["min_margin_frac"])
            row["min_margin"] = float(mg)
            row["min_margin_exact_B"] = "%d/%d" % (mg.numerator, mg.denominator) if mg.denominator < 10 ** 40 else "(big)"
        if ra is not None:
            a = ra[key]
            row.update(A_mm_b_adm=a["mm_b_adm"], A_mm_d_adm=a["mm_d_adm"],
                       A_mm_b_inadm=a["mm_b_inadm"], A_mm_d_inadm=a["mm_d_inadm"])
            dis = []
            if a["sum_b"] != v["sum_b"]:
                dis.append("sum_b")
            if a["sum_delta"] != sd:
                dis.append("sum_delta")
            if a["digest_b_def"] != v["digest_b_def"]:
                dis.append("digest_b_def")
            if a["digest_b_claim"] != v["digest_b_claim"]:
                dis.append("digest_b_claim")
            if a["nadm"] != v["nadm"]:
                dis.append("nadm")
            if v["min_margin_frac"] is not None and a["min_margin"] != Fraction(*v["min_margin_frac"]):
                dis.append("min_margin")
            if a["mm_b_inadm"] != v["mm_b_inadm"] or a["mm_d_inadm"] != v["mm_d_inadm"]:
                dis.append("inadm_counts")
            row["cross_disagreements"] = dis
            cross_dis += len(dis)
        del row["J"]
        del row["sum_delta"]
        del row["J_num_den"]
        rows.append(row)
    return dict(spec=spec_name, seed="%d/%d" % seed, A=A, dcap=dcap, D_bits=ob.D.bit_length(),
                time_B=tb, time_A=ta, ran_A=run_a, cross_disagreements=cross_dis, rows=rows)


def exactJ_table(spec_name, seed, A):
    """exact J as Fraction strings from oracle B only (used for Exp 4)."""
    spec = spec_by_name(spec_name)
    dcap = dcap_for(spec_name, A)
    ob = OB.IntOracle(spec, A, dcap, seed)
    rb = ob.run()
    out = []
    for key, v in rb.items():
        sd = Fraction(v["sum_delta_num"], v["sum_delta_den"])
        J = (Fraction(v["sum_b"]) - sd) / A
        out.append(dict(A=A, m=v["m"], k=v["k"], d=v["d"], admissible=(v["nadm"] == A),
                        sum_b=v["sum_b"], avg_delta=float(sd / A),
                        J=float(J), J_sign=(J > 0) - (J < 0), J_dec="%+.20e" % float(J),
                        J_exact_num_bits=J.numerator.bit_length(), J_den_bits=J.denominator.bit_length()))
    return out, ob


# ====================================================================== calibration
def stage_calibrate(quick=False):
    import mpmath as mp
    import numpy as np
    out = {"mpmath": mp.__version__, "numpy": np.__version__}
    # 1. r(1)
    out["r1_is_47_over_15"] = (r_frac(OB.SOURCE, 1) == Fraction(47, 15))
    out["r1_oracleB"] = [OB.R_int(OB.SOURCE, 60, 1), 60, OB.R_int(OB.SOURCE, 60, 1) * 15 == 47 * 60]
    # 2. positivity of r(n) n<=1e5 (exact) + analytic argument noted
    nmax_pos = 20000 if quick else 100000
    bad = 0
    for n in range(1, nmax_pos + 1):
        a, b, c, e = 8 * n - 7, 8 * n - 4, 8 * n - 3, 8 * n - 2
        # sign of r*a*b*c*e: integer arithmetic
        num = 4 * b * c * e - 2 * a * c * e - a * b * e - a * b * c
        bad += num <= 0
    out["r_positive_checked_to"] = nmax_pos
    out["r_nonpositive_count"] = bad
    # 3. U_n/16^n -> pi/16 and U_n + T_n = 16^(n-1) pi
    nmaxT = 9000
    LO, HI = OB.tail_intervals(nmaxT)
    U = Fraction(0)
    Us = {}
    for n in range(1, nmaxT + 1):
        U = 16 * U + r_frac(OB.SOURCE, n)
        if n in (1, 2, 5, 10, 20, 50, 100, 500, 1000, 2000, 4096, 8192):
            Us[n] = U
    rows = []
    for n, Un in Us.items():
        dps = int(1.21 * n) + 130 if not quick or n <= 1000 else None
        if dps is None:
            continue
        with mp.workdps(dps):
            ref = mp.pi * mp.mpf(16) ** (n - 1)
            Umpf = mp.mpf(Un.numerator) / mp.mpf(Un.denominator)
            Tmid = (mp.mpf(LO[n]) + mp.mpf(HI[n])) / 2 / mp.mpf(OB.SC)
            resid = ref - Umpf - Tmid
            width = (mp.mpf(HI[n]) - mp.mpf(LO[n])) / mp.mpf(OB.SC)
            rows.append(dict(n=n, dps=dps, resid=mp.nstr(resid, 5), tail_width=mp.nstr(width, 5),
                             within_bracket=bool(abs(resid) <= width), T_n=mp.nstr(Tmid, 15),
                             U_over_16n_minus_pi16=mp.nstr(Umpf / mp.mpf(16) ** n - mp.pi / 16, 8)))
    out["gauge_identity"] = rows
    # 4. 64 n^2 T_n -> 1
    nm = 1 << 18
    LO2, HI2 = OB.tail_intervals(nm)
    rows = []
    for n in [1, 2, 4, 8, 16, 32, 64, 128, 256, 1000, 4096, 16384, 65536, 131072, 262144]:
        v = Fraction(64 * n * n * LO2[n], OB.SC)
        rows.append(dict(n=n, val_64n2_T=float(v), n_times_dev=float((v - 1) * n)))
    out["64n2_Tn"] = rows
    # 5. 16T_n - T_{n+1} = r(n+1) inside rigorous bracket, all n<=nm-1
    viol = 0
    maxwidth = 0
    for n in range(0, nm):
        rl, rh = OB._r_bounds(n + 1)
        lo = 16 * LO2[n] - HI2[n + 1]
        hi = 16 * HI2[n] - LO2[n + 1]
        viol += not (lo <= rh and rl <= hi)   # brackets for r(n+1)*2^400 must overlap
        maxwidth = max(maxwidth, hi - lo)
    out["green_recurrence"] = dict(n_checked=nm, bracket_inconsistent=viol,
                                   max_bracket_width_in_2e400_units=int(maxwidth),
                                   max_bracket_width_log2=math.log2(maxwidth) - 400)
    # 6. series sum
    with mp.workdps(260):
        s = mp.mpf(0)
        for n in range(1, 200):
            s += mp.mpf(4) / (8 * n - 7) / 16 ** n - mp.mpf(2) / (8 * n - 4) / 16 ** n \
                 - mp.mpf(1) / (8 * n - 3) / 16 ** n - mp.mpf(1) / (8 * n - 2) / 16 ** n
        out["series_minus_pi_over_16"] = mp.nstr(s - mp.pi / 16, 5)
    # 7. pi hex routes
    M = 4000 if quick else 262544
    h = OB.pi_hex_digits(M)
    with mp.workdps(int(M * 1.21) + 60):
        Pm = int(mp.floor(mp.pi * mp.mpf(16) ** (M)))
    hm = format(Pm - (3 << (4 * M)), "x").zfill(M)
    mine = "".join("0123456789abcdef"[v] for v in h)
    out["pi_hex_chudnovsky_vs_mpmath_digits_compared"] = M
    out["pi_hex_chudnovsky_vs_mpmath_agree"] = (mine[:M - 2] == hm[:M - 2])
    out["pi_hex_first32"] = mine[:32]
    out["pi_hex_known_prefix_ok"] = mine.startswith("243f6a8885a308d313198a2e0370734")
    # BBP digit extraction (third route, float; 8 digits)
    def bbp_hex(pos, nd=8):
        def series(j, n):
            s = 0.0
            for k in range(n + 1):
                s = (s + pow(16, n - k, 8 * k + j) / (8 * k + j)) % 1.0
            k = n + 1
            while True:
                t = 16.0 ** (n - k) / (8 * k + j)
                if t < 1e-17:
                    break
                s += t
                k += 1
            return s
        n = pos - 1
        x = (4 * series(1, n) - 2 * series(4, n) - series(5, n) - series(6, n)) % 1.0
        r = ""
        for _ in range(nd):
            x *= 16
            r += "0123456789abcdef"[int(x)]
            x %= 1
        return r
    chk = []
    for pos in [1, 10, 100, 1000, 3990] + ([5000, 19990, 100000, 262000] if not quick else []):
        chk.append(dict(pos=pos, bbp=bbp_hex(pos), chud=mine[pos - 1:pos + 7],
                        agree=bbp_hex(pos)[:6] == mine[pos - 1:pos + 5]))
    out["bbp_digit_extraction"] = chk
    # 8. hand case A=2, m=k=1 (explicit Fractions, no class machinery)
    def hand(A=64, mk=((2, 2), (1, 3), (3, 1))):
        """plain loops, no oracle classes: window A..2A-1 of the repo definition."""
        r = lambda n: Fraction(4, 8 * n - 7) - Fraction(2, 8 * n - 4) - Fraction(1, 8 * n - 3) - Fraction(1, 8 * n - 2)
        U = [Fraction(0)]
        for n in range(1, 2 * A + 12):
            U.append(16 * U[-1] + r(n))
        S = lambda nn, kk: sum(16 ** (kk - j) * r(nn + j) for j in range(1, kk + 1))
        res = {}
        for (m, k) in mk:
            d = m + k
            sb = 0
            sdl = Fraction(0)
            mmatch = 0
            for n in range(A, 2 * A):
                x = U[n] % 1
                th = (16 ** d * x) % 1
                dl = (16 ** m * S(n, k)) % 1
                b = 1 if th + dl >= 1 else 0
                sb += b
                sdl += dl
                bc = 1 if S(n + k, m) <= (U[n + d] % 1) < S(n, d) else 0
                mmatch += (bc != b)
            res["%d,%d" % (m, k)] = dict(sum_b=sb, sum_delta=float(sdl), J=float((sb - sdl) / A), claim_mismatch=mmatch)
        return res
    out["hand_case_A64_plain_loops"] = hand()
    ob = OB.IntOracle(OB.SOURCE, 64, 5)
    rb = ob.run()
    ra = run_oracle_A(OB.SOURCE, 64, 5)
    out["hand_case_vs_oracles"] = {kk: dict(oracleB_sum_b=rb[kk]["sum_b"], oracleA_sum_b=ra[kk]["sum_b"],
                                            oracleB_J=float((Fraction(rb[kk]["sum_b"]) - Fraction(rb[kk]["sum_delta_num"], rb[kk]["sum_delta_den"])) / 64),
                                            oracleA_J=float((ra[kk]["sum_b"] - ra[kk]["sum_delta"]) / 64))
                                   for kk in ("2,2", "1,3", "3,1")}
    return out


# ====================================================================== stage cb1
def stage_cb1(procs, quick=False):
    t0 = time.time()
    epochs = [64, 173, 347] if quick else EPOCHS
    tasks = []
    # heavy first
    for A in sorted(epochs, reverse=True):
        for seed in SEEDS:
            run_a = (A <= 1024) or (seed in ((0, 1), (1, 5)))
            tasks.append(("source", seed, A, run_a))
    mut_epochs = [64, 173, 347] if quick else [64, 173, 347, 691, 1024]
    for name in OB.mutant_specs():
        for A in mut_epochs:
            tasks.append((name, (0, 1), A, True))
    tasks.sort(key=lambda t: -t[2])
    with Pool(procs) as pool:
        res = pool.map(cb1_task, tasks, chunksize=1)
    out = dict(tasks=res, wall=time.time() - t0)
    return out


# ====================================================================== summary helpers
def summarise_cb1(cb1):
    """compact per-(spec,seed,A) summary: dmax, mismatch totals in admissible and boundary"""
    rows = []
    for t in cb1["tasks"]:
        by_d = {}
        for r in t["rows"]:
            by_d.setdefault(r["d"], []).append(r)
        dmax = 1
        for d in sorted(by_d):
            if all(r["nadm"] == t["A"] for r in by_d[d]):
                dmax = d
            else:
                break
        adm = [r for r in t["rows"] if r["d"] <= dmax and r["d"] >= 2]
        bd = [r for r in t["rows"] if r["d"] == dmax + 1]
        far = [r for r in t["rows"] if r["d"] > dmax + 1]
        sB = sum(r["B_mm_b_adm"] + r["B_mm_d_adm"] for r in t["rows"])
        sA = sum(r.get("A_mm_b_adm", 0) + r.get("A_mm_d_adm", 0) for r in t["rows"]) if t["ran_A"] else None
        rows.append(dict(spec=t["spec"], seed=t["seed"], A=t["A"], dmax=dmax, n_admissible_triples=len(adm),
                         cases_admissible=sum(r["nadm"] for r in t["rows"]),
                         mismatches_oracleB_admissible=sB, mismatches_oracleA_admissible=sA,
                         cross_oracle_disagreements=t["cross_disagreements"],
                         boundary_d=dmax + 1,
                         boundary_cases=sum(r["n_inadm"] for r in bd),
                         boundary_b_mismatch=sum(r["B_mm_b_inadm"] for r in bd),
                         boundary_delta_mismatch=sum(r["B_mm_d_inadm"] for r in bd),
                         beyond_boundary_cases=sum(r["n_inadm"] for r in far),
                         beyond_boundary_b_mismatch=sum(r["B_mm_b_inadm"] for r in far),
                         time_B=t["time_B"], time_A=t["time_A"]))
    return rows


# ====================================================================== stage cb1g
def stage_cb1g(quick=False):
    import numpy as np
    out = {}
    epochs = [64, 173, 347] if quick else EPOCHS
    SC = OB.SC
    nlast_all = 2 * max(epochs) + 20
    LO, HI = OB.tail_intervals(nlast_all + 10)
    M = nlast_all + 200
    t0 = time.time()
    h = OB.pi_hex_digits(M)
    hs = "".join("0123456789abcdef"[v] for v in h)
    out["pi_digits_M"] = M
    out["pi_time"] = time.time() - t0
    import countermodel_cb3 as CM
    TT = CM.Tails(nlast_all + 40)
    Dpi = CM._pi_digits(nlast_all + 200, quick)
    Zpi = CM.zfloat(Dpi)
    res = []
    for A in epochs:
        t1 = time.time()
        dcap = dcap_for("source", A)
        ob = OB.IntOracle(OB.SOURCE, A, dcap, (0, 1))
        D = ob.D
        cnt = dict(cases=0, mism_b_pi=0, mism_b_x=0, ambiguous=0, delta_viol=0, wrap_cases=0,
                   wrap_with_mismatch=0, adm_cases=0, max_zdiff_units=0, min_margin_units=None)
        per_triple = {}

        def hook(n, m, k, b_def, Sd, Sm, dlD, Xnd, adm):
            d = m + k
            # thresholds, rigorous brackets (units of 2^-400)
            tl_lo = 16 ** m * LO[n + k]
            tl_hi = 16 ** m * HI[n + k]
            tu_lo = 16 ** d * LO[n]
            tu_hi = 16 ** d * HI[n]
            # z via pi digits: z_j = 0.h_j h_{j+1}... ; j = n+d ; 100 hex digits => 400 bits
            j = n + d
            z1 = int(hs[j - 1:j + 99], 16)             # floor(z_j 2^400), error < 1
            # z via x + T mod 1
            xf = (Xnd * SC) // D
            zlo = xf + LO[j]
            zhi = xf + 1 + HI[j]
            wrap_x = zlo >= SC           # x+T >= 1 -> subtract
            if wrap_x:
                zlo -= SC
                zhi -= SC
            elif zhi >= SC:
                cnt["ambiguous"] += 1
                return
            # decide membership with z1 (pi route)
            def decide(zl, zh):
                # returns 1/0 or None if ambiguous
                if zl >= tl_hi and zh < tu_lo:
                    return 1
                if zh < tl_lo or zl >= tu_hi:
                    return 0
                return None
            b1 = decide(z1, z1 + 1)
            b2 = decide(zlo, zhi)
            if b1 is None or b2 is None:
                cnt["ambiguous"] += 1
                return
            # margin
            mg = min(abs(z1 - tl_lo), abs(z1 - tu_lo), abs(z1 - tl_hi), abs(z1 - tu_hi))
            if cnt["min_margin_units"] is None or mg < cnt["min_margin_units"]:
                cnt["min_margin_units"] = mg
            cnt["max_zdiff_units"] = max(cnt["max_zdiff_units"], abs(z1 - (zlo + zhi) // 2))
            dl_ex = ((Sd - Sm) * SC) // D
            dl_g_lo = tu_lo - tl_hi
            dl_g_hi = tu_hi - tl_lo
            if not (dl_g_lo - 2 <= dl_ex <= dl_g_hi + 2):
                cnt["delta_viol"] += 1
            wrap = tu_lo >= SC
            if adm:
                cnt["adm_cases"] += 1
                cnt["cases"] += 1
                cnt["mism_b_pi"] += (b1 != b_def)
                cnt["mism_b_x"] += (b2 != b_def)
                if wrap:
                    cnt["wrap_cases"] += 1
                    cnt["wrap_with_mismatch"] += (b1 != b_def) or (b2 != b_def)
            else:
                pt = per_triple.setdefault(d, dict(cases=0, mism_b_pi=0, mism_b_x=0))
                pt["cases"] += 1
                pt["mism_b_pi"] += (b1 != b_def)
                pt["mism_b_x"] += (b2 != b_def)

        rb = ob.run(hook=hook)
        # instrument-vs-instrument: gauge b_vector (pi digits, float+exact fallback) vs oracle-B repo-definition bits
        agree = 0
        tot = 0
        for key, v in rb.items():
            if v["nadm"] != A:
                continue
            m, k = v["m"], v["k"]
            bv, mg, na, nu = CM.b_vector(Dpi, Zpi, TT, A, m, k)
            dg = OB.digest_bits(bytes(bv.astype("uint8")))
            tot += 1
            agree += (dg == v["digest_b_def"])
        dmax_gauge = TT.dmax(A)
        dmax_oracle = max([v["d"] for v in rb.values() if v["nadm"] == A] or [1])
        res.append(dict(A=A, dcap=dcap, **cnt, inadmissible_by_d=per_triple, b_vector_digest_agree=agree,
                        b_vector_triples=tot, dmax_gauge=dmax_gauge, dmax_oracle=dmax_oracle, time=time.time() - t1))
    for r in res:
        r["min_margin_abs"] = float(Fraction(r["min_margin_units"], OB.SC)) if r["min_margin_units"] is not None else None
        r["min_margin_units"] = None
    out["epochs"] = res
    return out


# ====================================================================== stage trueseed
def _trueseed_task(args):
    spec_name, seed, A = args
    tab, ob = exactJ_table(spec_name, seed, A)
    return dict(seed="%d/%d" % seed, A=A, table=tab)


def stage_trueseed(procs, quick=False):
    import mpmath as mp
    epochs = [64, 173, 347] if quick else EPOCHS
    tasks = [("source", (0, 1), A) for A in epochs] + [("source", (1, 5), A) for A in epochs]
    with Pool(procs) as pool:
        res = pool.map(_trueseed_task, sorted(tasks, key=lambda t: -t[2]), chunksize=1)
    out = dict(exact=res)
    # coherent seed: rigorous-T route (b==0, J=-avg delta) all epochs; repo-definition route in mp for small A
    LO, HI = OB.tail_intervals(2 * max(epochs) + 40)
    SC = OB.SC
    coh = []
    P = [0]
    for v in LO:
        P.append(P[-1] + v)

    def psum(a, b):  # sum LO[a..b]
        return P[b + 1] - P[a]
    for A in epochs:
        dmax = int(math.floor(math.log(64 * A * A, 16))) + 1
        for d in range(2, dmax + 1):
            for m in range(1, d):
                k = d - m
                # admissible?
                adm = all(16 ** d * HI[n] - LO[n + d] < SC for n in range(A, 2 * A))
                if not adm:
                    continue
                # b==0 : z=0 < 16^m T_{n+k} always since T>0
                bz = all(16 ** m * LO[n + k] > 0 for n in range(A, 2 * A))
                sd = (16 ** d * psum(A, 2 * A - 1) - 16 ** m * psum(A + k, 2 * A - 1 + k))
                J = Fraction(-sd, SC * A)
                coh.append(dict(A=A, m=m, k=k, d=d, b_all_zero=bool(bz), J=float(J), J_dec="%+.20e" % float(J)))
    out["coherent_gauge"] = coh
    # repo-definition route at high precision for coherent seed, small A
    rep = []
    for A in ([64, 173] if quick else [64, 173, 347, 691]):
        dcap = dcap_for("source", A)
        nlast = 2 * A - 1 + dcap + 2
        dps = int(1.21 * nlast) + 150
        U = Fraction(0)
        Us = {}
        for n in range(1, nlast + 1):
            U = 16 * U + r_frac(OB.SOURCE, n)
            if n >= A:
                Us[n] = U
        with mp.workdps(dps):
            pi = mp.pi
            tot = {}
            for n in range(A, 2 * A):
                x = mp.mpf(Us[n].numerator) / mp.mpf(Us[n].denominator) - mp.mpf(16) ** (n - 1) * pi
                x = x - mp.floor(x)
                for d in range(2, dcap + 1):
                    th = mp.mpf(16) ** d * x
                    th = th - mp.floor(th)
                    for m in range(1, d):
                        k = d - m
                        Sk = Fraction(0)
                        for j in range(1, k + 1):
                            Sk += 16 ** (k - j) * r_frac(OB.SOURCE, n + j)
                        dl = mp.mpf(16 ** m * Sk.numerator) / mp.mpf(Sk.denominator)
                        dl = dl - mp.floor(dl)
                        b = 1 if th + dl >= 1 else 0
                        t = tot.setdefault((m, k), [0, mp.mpf(0)])
                        t[0] += b
                        t[1] += dl
            for (m, k), (sb, sdl) in sorted(tot.items(), key=lambda kv: (kv[0][0] + kv[0][1], kv[0][0])):
                rep.append(dict(A=A, m=m, k=k, d=m + k, sum_b=sb, J=mp.nstr((sb - sdl) / A, 18)))
    out["coherent_repo_definition_mp"] = rep
    return out


# ====================================================================== stage third (cross-check vs reference module)
REF_DEFAULT = os.path.abspath(os.path.join(HERE, *[".."] * 5))  # repository root (relocated from scratch after the run)


def stage_third(ref=REF_DEFAULT, quick=False):
    """THIRD cross-check only: observational_succ.selected_orbit (carry_by_definition / carry_by_window,
    critical_depths).  Imported read-only (no bytecode written); our oracles never import it."""
    sys.dont_write_bytecode = True
    sys.path.insert(0, ref)
    try:
        from observational_succ import selected_orbit as SO
    except Exception as e:  # report the wall instead of failing silently
        return dict(UNVERIFIED="could not import selected_orbit: %r" % (e,))
    finally:
        sys.path.remove(ref)
    out = dict(module=SO.__file__, rows=[])
    for A in ([64, 173] if quick else [64, 173, 347, 691]):
        dcap = dcap_for("source", A)
        crit = SO.critical_depths(A)
        for seed in [(0, 1), (1, 5)]:
            ob = OB.IntOracle(OB.SOURCE, A, dcap, seed)
            rb = ob.run()
            dmax_ours = max(v["d"] for v in rb.values() if v["nadm"] == A)
            orb = SO.SelectedOrbit(Fraction(*seed))
            n_cmp = 0
            bad = 0
            for key, v in rb.items():
                if v["d"] > dmax_ours:
                    continue
                m, k = v["m"], v["k"]
                Jb = (Fraction(v["sum_b"]) - Fraction(v["sum_delta_num"], v["sum_delta_den"])) / A
                Jw = orb.innovation(A, m, k, by="window")
                Jd = orb.innovation(A, m, k, by="definition")
                n_cmp += 1
                bad += (Jb != Jw) + (Jb != Jd)
            out["rows"].append(dict(A=A, seed="%d/%d" % seed, our_dmax=dmax_ours,
                                    ref_critical_depths=crit, ref_max_depth=(max(crit) if crit else None),
                                    triples_compared=n_cmp, J_disagreements=bad,
                                    our_dmax_equals_ref=(max(crit) == dmax_ours if crit else None)))
    return out


# ====================================================================== stage edge (S_d just below 1)
def stage_edge(quick=False):
    """For each d, the smallest epoch A whose window is admissible at depth d (S_d(A) barely < 1).
    Both oracles (oracle A only for A<=2100) on the whole window; reports 1-S_d at the tightest n."""
    import countermodel_cb3 as CM
    T = CM.Tails(2 * 9000 + 100)
    rows = []
    for d in range(3, 9 if not quick else 6):
        lo, hi = 1, 9000
        while lo < hi:                      # smallest A with S_d(A) < 1  (S_d decreasing in n)
            mid = (lo + hi) // 2
            adm = 16 ** d * T.HI[mid] - T.LO[mid + d] < OB.SC
            if adm:
                hi = mid
            else:
                lo = mid + 1
        A = lo
        dcap = d + 1
        rb = OB.IntOracle(OB.SOURCE, A, dcap, (0, 1)).run()
        sel = [v for v in rb.values() if v["d"] == d]
        ra = run_oracle_A(OB.SOURCE, A, dcap, (0, 1)) if A <= 2100 else None
        below = [v for v in rb.values() if v["d"] == d + 1]
        row = dict(d=d, A_edge=A, A_minus_1_admissible=bool(16 ** d * T.HI[A - 1] - T.LO[A - 1 + d] < OB.SC),
                   tightest_one_minus_Sd=min(float(Fraction(*v["min_margin_frac"])) for v in sel),
                   cases=sum(v["nadm"] for v in sel), mismatches_B=sum(v["mm_b_adm"] + v["mm_d_adm"] for v in sel),
                   mismatches_A=(sum(ra[k]["mm_b_adm"] + ra[k]["mm_d_adm"] for k in ra if ra[k]["d"] == d) if ra else None),
                   next_depth_inadmissible_cases=sum(v["n_inadm"] for v in below),
                   next_depth_b_mismatch=sum(v["mm_b_inadm"] for v in below),
                   cross_ok=(None if ra is None else all(ra[k]["sum_b"] == rb[k]["sum_b"] and ra[k]["digest_b_def"] == rb[k]["digest_b_def"]
                                                         for k in rb if rb[k]["d"] <= d)))
        rows.append(row)
    return dict(rows=rows)


# ====================================================================== stage summary (pure post-processing of data/*.json)
def stage_summary():
    import numpy as np
    out = {}
    j2 = json.load(open(os.path.join(DATA, "j2.json")))
    cb3 = json.load(open(os.path.join(DATA, "cb3.json")))
    As = j2["As"]
    rows = []
    for A in As:
        for nm, e in j2["expected"][str(A)]["reps"].items():
            un = [s["res"][str(A)]["reps"][nm] for s in j2["empirical"] if s["kind"] == "unif"]
            cb = [s["res"][str(A)]["reps"][nm] for s in j2["empirical"] if s["kind"] == "cb3"]
            pi = [s["res"][str(A)]["reps"][nm] for s in j2["empirical"] if s["kind"] == "pi"][0]
            row = dict(A=A, rep=nm, m=e["m"], k=e["k"], E_J_cb3=e["E_J"], null_sd_J=float(np.std([u["J"] for u in un], ddof=1)),
                       cb3_emp_J_mean=float(np.mean([c["J"] for c in cb])), pi_J=pi["J"], coherent_J=e["coherent_J"])
            for l in (1, 2, 3):
                key = "J2_l%d" % l
                sd = float(np.std([u[key] for u in un], ddof=1))
                row["E_J2_l%d_cb3" % l] = e["E_J2_l%d" % l]
                row["E_J2_l%d_uniform_control" % l] = e["E_J2_uniform_control_l%d" % l]
                row["null_sd_J2_l%d" % l] = sd
                row["null_mean_J2_l%d" % l] = float(np.mean([u[key] for u in un]))
                row["cb3_emp_J2_l%d_mean13" % l] = float(np.mean([c[key] for c in cb]))
                row["cb3_emp_J2_l%d_sd13" % l] = float(np.std([c[key] for c in cb], ddof=1))
                row["pi_J2_l%d" % l] = pi[key]
                row["coherent_J2_l%d" % l] = e["coherent_J2_l%d" % l]
                row["z_expected_over_null_sd_l%d" % l] = (e["E_J2_l%d" % l] / sd) if sd > 0 else None
            row["z_expectedJ_over_null_sd"] = e["E_J"] / row["null_sd_J"] if row["null_sd_J"] > 0 else None
            rows.append(row)
    out["j2_rows"] = rows
    # headline aggregates over all rows
    def mx(key):
        return max(abs(r[key]) for r in rows)
    out["max_abs_E_J_cb3"] = mx("E_J_cb3")
    for l in (1, 2, 3):
        out["max_abs_E_J2_l%d_cb3" % l] = mx("E_J2_l%d_cb3" % l)
        out["max_abs_E_J2_l%d_uniform_control" % l] = mx("E_J2_l%d_uniform_control" % l)
        zs = [abs(r["z_expected_over_null_sd_l%d" % l]) for r in rows if r["z_expected_over_null_sd_l%d" % l] is not None]
        out["max_abs_z_E_J2_over_null_sd_l%d" % l] = max(zs)
    zs = [abs(r["z_expectedJ_over_null_sd"]) for r in rows if r["z_expectedJ_over_null_sd"]]
    out["max_abs_z_E_J_over_null_sd"] = max(zs)
    # scale invariance of E_J2 (l=1) under A -> 4A (same tau-window), balanced rep
    inv = {}
    for A in [2048, 2896]:
        seq = [A * 4 ** i for i in range(0, 4) if A * 4 ** i <= 131072 or int(round(A * 4 ** i)) in As]
        vals = []
        for B in As:
            if B in [2048, 8192, 32768, 131072] and A == 2048:
                r = [x for x in rows if x["A"] == B and x["rep"] == "balanced"][0]
                vals.append((B, r["E_J2_l1_cb3"], r["E_J2_l2_cb3"], r["E_J2_l3_cb3"], r["E_J_cb3"]))
            if A == 2896 and B in [2896, 11585, 46341]:
                r = [x for x in rows if x["A"] == B and x["rep"] == "balanced"][0]
                vals.append((B, r["E_J2_l1_cb3"], r["E_J2_l2_cb3"], r["E_J2_l3_cb3"], r["E_J_cb3"]))
        inv[str(A)] = vals
    out["E_J2_A_to_4A_balanced(A,l1,l2,l3,E_J)"] = inv
    # null-sd decay slope of J and J2(l=1), balanced rep, over all A
    for key in ("null_sd_J", "null_sd_J2_l1"):
        xs = np.log([r["A"] for r in rows if r["rep"] == "balanced"])
        ys = np.log([max(r[key], 1e-300) for r in rows if r["rep"] == "balanced"])
        out["slope_" + key + "_balanced"] = float(np.polyfit(xs, ys, 1)[0])
    # witnesses
    sw = cb3["sweeps"]
    wrows = []
    for A in cb3["As"]:
        cbw = [s["res"][str(A)]["wit"] for s in sw if s["kind"] == "cb3"]
        unw = [s["res"][str(A)]["wit"] for s in sw if s["kind"] == "unif"]
        piw = [s["res"][str(A)]["wit"] for s in sw if s["kind"] == "pi"][0]
        e = cb3["witness_expected_cb3"][str(A)]
        r = dict(A=A, N=2 * A)
        for k in ("f1_minus_f2", "pairs_minus_1_16", "max_dev"):
            r["exp_" + k] = e[k]
            r["cb3_mean13_" + k] = float(np.mean([w[k] for w in cbw]))
            r["cb3_sd13_" + k] = float(np.std([w[k] for w in cbw], ddof=1))
            r["unif_mean12_" + k] = float(np.mean([w[k] for w in unw]))
            r["unif_sd12_" + k] = float(np.std([w[k] for w in unw], ddof=1))
            r["pi_" + k] = piw[k]
        r["z_cb3mean_vs_unif_f1f2"] = (r["cb3_mean13_f1_minus_f2"] - r["unif_mean12_f1_minus_f2"]) / math.sqrt(
            r["unif_sd12_f1_minus_f2"] ** 2 / 12 + r["cb3_sd13_f1_minus_f2"] ** 2 / 13)
        wrows.append(r)
    out["witness_rows"] = wrows
    out["witness_exp_f1f2_min_over_A_ge_1024"] = min(r["exp_f1_minus_f2"] for r in wrows)
    # CB-3 J summary rows
    jrows = []
    for A in cb3["As"]:
        cbr = [s["res"][str(A)] for s in sw if s["kind"] == "cb3"]
        unr = [s["res"][str(A)] for s in sw if s["kind"] == "unif"]
        pir = [s["res"][str(A)] for s in sw if s["kind"] == "pi"][0]
        pre = [s["res"][str(A)]["max_abs_J"] for s in sw if s["kind"] == "cb3" and s["seed"] in (20261105, 1, 2)]
        jrows.append(dict(A=A, dmax=cbr[0]["dmax"], n_triples=cbr[0]["n_triples"],
                          expected_bias_max_abs=cb3["expected_J_bias"][str(A)]["max_abs"],
                          prereg_seeds_maxabsJ=pre, cb3_mean13_maxabsJ=float(np.mean([c["max_abs_J"] for c in cbr])),
                          cb3_mean13_rmsJ=float(np.mean([c["rms_J"] for c in cbr])),
                          unif_mean12_maxabsJ=float(np.mean([c["max_abs_J"] for c in unr])),
                          unif_mean12_rmsJ=float(np.mean([c["rms_J"] for c in unr])),
                          pi_maxabsJ=pir["max_abs_J"], pi_rmsJ=pir["rms_J"],
                          min_margin=min(c["min_margin"] for c in cbr + [pir]),
                          exact_fallbacks=sum(c["ambiguous_fallbacks"] for c in cbr + [pir]),
                          unresolved=sum(c["unresolved"] for c in cbr + [pir])))
    out["cb3_J_rows"] = jrows
    out["largest_A_reached_cb3"] = max(cb3["As"])
    out["cb3_wall_seconds"] = cb3["wall"]
    out["j2_wall_seconds"] = j2["wall"]
    out["max_bias_over_all_A"] = max(r["expected_bias_max_abs"] for r in jrows)
    return out


def stage_receipt():
    rec = dict(scripts={f: sha256_file(os.path.join(HERE, f)) for f in
                        ("carry_transport_probe.py", "oracle_b.py", "countermodel_cb3.py", "test_carry_transport.py")})
    save("summary", stage_summary())
    for nm in ("calibrate", "cb1_summary", "cb1g", "trueseed", "edge", "third", "cb3", "j2", "summary"):
        p = os.path.join(DATA, nm + ".json")
        if os.path.exists(p):
            rec[nm] = json.load(open(p))
    rec["cb1_file"] = "data/cb1.json (full per-triple rows, 2 oracles)"
    rec["numpy"] = __import__("numpy").__version__
    rec["python"] = sys.version
    with open(os.path.join(HERE, "FINITE_RECEIPT.json"), "w") as f:
        json.dump(rec, f, indent=1, default=str)
    return rec


# ====================================================================== main
def sha256_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def save(name, obj):
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, name + ".json"), "w") as f:
        json.dump(obj, f, indent=1, default=lambda o: str(o))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="all")
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--procs", type=int, default=6)
    ap.add_argument("--ref", default=REF_DEFAULT)
    a = ap.parse_args()
    t0 = time.time()
    st = a.stage
    if st in ("calibrate", "all"):
        save("calibrate", stage_calibrate(a.quick))
        print("calibrate done", time.time() - t0, flush=True)
    if st in ("cb1", "all"):
        c = stage_cb1(a.procs, a.quick)
        save("cb1", c)
        save("cb1_summary", summarise_cb1(c))
        print("cb1 done", time.time() - t0, flush=True)
    if st in ("cb1g", "all"):
        save("cb1g", stage_cb1g(a.quick))
        print("cb1g done", time.time() - t0, flush=True)
    if st in ("trueseed", "all"):
        save("trueseed", stage_trueseed(a.procs, a.quick))
        print("trueseed done", time.time() - t0, flush=True)
    if st in ("edge", "all"):
        save("edge", stage_edge(a.quick))
        print("edge done", time.time() - t0, flush=True)
    if st in ("third", "all"):
        save("third", stage_third(a.ref, a.quick))
        print("third done", time.time() - t0, flush=True)
    if st in ("cb3", "all"):
        import countermodel_cb3 as C
        save("cb3", C.stage_cb3(a.quick, a.procs))
        print("cb3 done", time.time() - t0, flush=True)
    if st in ("j2", "all"):
        import countermodel_cb3 as C
        save("j2", C.stage_j2(a.quick, a.procs))
        print("j2 done", time.time() - t0, flush=True)
    if st in ("all", "receipt"):
        stage_receipt()
        print("receipt written", time.time() - t0)


if __name__ == "__main__":
    main()
