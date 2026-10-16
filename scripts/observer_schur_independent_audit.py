#!/usr/bin/env python3
"""Hostile Round II audit, independent rational oracles and bounded API probes.

No Git, Lean compilation, full suite, network, or product writes. Only --output
is written. The direct-sum mathematics uses Fraction and elementary 2x2 algebra;
producer routines are imported solely as subjects of comparison/mutation tests.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import product
import json
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
COUNTS = {}
FAILURES = []


def check(lane, label, condition, detail=None):
    COUNTS[lane] = COUNTS.get(lane, 0) + 1
    if not condition:
        FAILURES.append({"lane": lane, "label": label, "detail": repr(detail)})


def rejects(lane, label, operation):
    try:
        operation()
    except (ValueError, TypeError, KeyError):
        check(lane, label, True)
    else:
        check(lane, label, False, "unexpected acceptance")


def mv(a, x):
    return tuple(sum((v*w for v, w in zip(row, x)), F()) for row in a)


def dot(x, y):
    return sum((v*w for v, w in zip(x, y)), F())


def q(a, x):
    return dot(x, mv(a, x))


def det2(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]


def solve2(a, b):
    d = det2(a)
    return ((a[1][1]*b[0]-a[0][1]*b[1])/d,
            (a[0][0]*b[1]-a[1][0]*b[0])/d)


def determinant(a):
    if not a:
        return F(1)
    return sum(((-1)**j*a[0][j]*determinant(tuple(
        tuple(row[k] for k in range(len(a)) if k != j) for row in a[1:]))
        for j in range(len(a))), F())


def imul(a, b):
    corners = [x*y for x in a for y in b]
    return min(corners), max(corners)


def iadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def iscale(a, c):
    return imul(a, (c, c))


def interval_majorant(vv, cross, kinv, kap):
    m = []
    for i in range(3):
        row = []
        for j in range(3):
            entry = vv[i][j]
            for u in range(4):
                for v in range(4):
                    entry = iadd(entry, iscale(imul(cross[u][i], cross[v][j]), -kinv[u][v]/kap))
            row.append(entry)
        m.append(row)
    center = tuple(tuple((z[0]+z[1])/2 for z in row) for row in m)
    radius = max(sum(((z[1]-z[0])/2 for z in row), F()) for row in m)
    upper = tuple(tuple(z+(radius if i == j else 0) for j, z in enumerate(row))
                  for i, row in enumerate(center))
    return m, upper, radius


def certify_negative_majorant(upper):
    leading = [determinant(tuple(tuple(-upper[i][j] for j in range(n))
                               for i in range(n))) for n in (1, 2, 3)]
    hh = tuple(tuple(upper[i][j] for j in (1, 2)) for i in (1, 2))
    b = (upper[1][0], upper[2][0])
    maximum = upper[0][0] - dot(b, solve2(hh, b))
    return leading, maximum


def source_certificate_audit(independent_integrals=False):
    path = ROOT/"research/2026-10-16/source-schur-exact.json"
    if not path.is_file():
        return {"status": "NOT_AVAILABLE_AT_AUDIT"}
    receipt = json.loads(path.read_text())
    source_bytes = (ROOT/"observational_succ/source_weil_hierarchy.py").read_bytes()
    blob = sha1(b"blob "+str(len(source_bytes)).encode()+b"\0"+source_bytes).hexdigest()
    check("source_identity", "actual Suzuki source blob", blob == "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
    certs = receipt["exact_certificates"]
    parse_matrix = lambda a: tuple(tuple(F(x) for x in row) for row in a)
    parse_intervals = lambda a: tuple(tuple(tuple(map(F, z)) for z in row) for row in a)
    rows = []
    for cert in certs:
        k, ki = map(parse_matrix, (cert["K_probe_Gram"], cert["K_probe_inverse"]))
        check("source_interval", "K inverse",
              all(sum((k[i][l]*ki[l][j] for l in range(4)), F()) == int(i == j)
                  for i in range(4) for j in range(4)))
        check("source_interval", "K positive by Sylvester",
              all(determinant(tuple(tuple(k[i][j] for j in range(n)) for i in range(n))) > 0
                  for n in range(1, 5)))
        vv, cross, stored = map(parse_intervals, (cert["full_source_vv_intervals"],
                                                 cert["full_source_cross_intervals"],
                                                 cert["criterion_interval_matrix"]))
        computed, _, _ = interval_majorant(vv, cross, ki, F(cert["kappa_tested"]))
        check("source_interval", "rounded intervals enclose independent exact expression",
              all(stored[i][j][0] <= computed[i][j][0] <= computed[i][j][1] <= stored[i][j][1]
                  for i in range(3) for j in range(3)))
        radius = max(sum(((z[1]-z[0])/2 for z in row), F()) for row in stored)
        upper = tuple(tuple((z[0]+z[1])/2+(radius if i == j else 0)
                            for j, z in enumerate(row)) for i, row in enumerate(stored))
        check("source_interval", "Loewner majorant", upper == parse_matrix(cert["criterion_Loewner_upper"]))
        dets, maximum = certify_negative_majorant(upper)
        pivots = tuple(dets[i]/(dets[i-1] if i else 1) for i in range(3))
        check("source_interval", "negative definite by independent determinants", all(d > 0 for d in dets))
        check("source_interval", "LDL pivots match determinant ratios", pivots == tuple(map(F, cert["minus_upper_LDL_pivots"])))
        check("source_interval", "all-coefficient maximum", maximum == F(cert["criterion_uniform_upper_for_P2"]) and maximum < 0)
        check("source_authority", "no source sign promotion", cert["source_original_sign"] == "OPEN"
              and cert["source_original_negative_direction"] is False and cert["RH_PROVED"] is False)
        rows.append({"kappa": cert["kappa_tested"], "uniform_upper": str(maximum),
                     "upper_decimal_display_only": float(maximum)})
    independent = None
    if independent_integrals:
        # Reuse the previous INDEPENDENT auditor's Rodrigues/correlation route,
        # never the producer's OU pair, interval, contact, or tail helpers.
        review = ROOT/"reviews/2026-10-15_PROOF_TEETH_SCHUR_INDEPENDENT_AUDIT.md"
        code = review.read_text().split("```python\n", 1)[1].split("\n```", 1)[0]
        code = code.split("start=time.monotonic()", 1)[0]
        ns = {}
        exec(compile(code, str(review)+"::definitions-only", "exec"), ns)
        J = 512
        tau = F(2, (4*J+1)**2) + F(16, (4*J+1)**3)
        cache = {}
        def source_pair(i, j):
            key = tuple(sorted((i, j)))
            if key in cache:
                return cache[key]
            p = ns["rho"](ns["leg"](i), ns["leg"](j))
            assert ns["integ"](p) == 0
            contact = ns["scale"](ns["CONTACT"], ns["integ"]([F()]+p)/2)
            pole = ns["scale"](ns["add"](ns["epair"](p, F(-1, 2)), ns["epair"](p, F(1, 2))), -4)
            prime = ns["mul"](ns["WEIGHT"], ns["hinge"](p))
            gamma = ns["sumiv"](ns["scale"](ns["epair"](p, F(4*j+1, 2)), F(4, (4*j+1)**2)) for j in range(J))
            truncated = ns["sumiv"]((contact, pole, prime, gamma))
            error = tau/min(2*i+1, 2*j+1)
            cache[key] = truncated[0]-error, truncated[1]+error
            return cache[key]
        vmodes, qmodes = (2, 6, 8), (6, 8, 10, 12)
        vv = tuple(tuple(source_pair(i, j) for j in vmodes) for i in vmodes)
        cross = tuple(tuple(source_pair(i, j) for j in vmodes) for i in qmodes)
        primitive = lambda n: [F()] + [x/F(j+1) for j, x in enumerate(ns["leg"](n))]
        k = tuple(tuple(ns["integ"](ns["pmul"](primitive(i), primitive(j))) for j in qmodes) for i in qmodes)
        check("source_independent", "primitive Gram agrees", k == parse_matrix(certs[0]["K_probe_Gram"]))
        cases = []
        for cert in certs:
            ki = parse_matrix(cert["K_probe_inverse"])
            m, upper, radius = interval_majorant(vv, cross, ki, F(cert["kappa_tested"]))
            dets, maximum = certify_negative_majorant(upper)
            check("source_independent", "fresh full-source all-family certificate "+cert["kappa_tested"],
                  all(d > 0 for d in dets) and maximum < 0)
            cases.append({"kappa": cert["kappa_tested"], "leading_minors_minus_upper": list(map(str, dets)),
                          "uniform_upper": str(maximum), "upper_decimal_display_only": float(maximum)})
        independent = {"implementation_lineage": str(review.relative_to(ROOT)),
                       "implementation_sha256": sha_file(review), "Gamma_modes": J,
                       "whole_tail": str(tau), "source_pair_intervals": {
                           f"P{i},P{j}": list(map(str, val)) for (i, j), val in cache.items()},
                       "cases": cases, "producer_source_helpers_imported": False}
    return {"certificate_sha256": sha_file(path), "matrix_checks": rows,
            "independent_source_integration": independent,
            "original_S0_sign": "OPEN", "scope": "ALL complex c6,c8 in the P2 degree-eight trial family only"}


def clamped_controls():
    def integral(p):
        return sum((x/F(i+1) for i, x in enumerate(p)), F())
    def derivative(p):
        return tuple(i*x for i, x in enumerate(p) if i) or (F(),)
    def multiply(p, r):
        out = [F()]*(len(p)+len(r)-1)
        for i, x in enumerate(p):
            for j, y in enumerate(r):
                out[i+j] += x*y
        return tuple(out)
    # C1=t^2(1-t)^2/24 is the inverse clamped biharmonic source vector.
    b = (F(), F(), F(1, 24), F(-1, 12), F(1, 24))
    fourth = b
    for _ in range(4):
        fourth = derivative(fourth)
    check("clamped", "C1 explicit", fourth == (F(1),) and b[0] == sum(b) == 0
          and derivative(b)[0] == sum(derivative(b)) == 0)
    optimum = (F(), F(1, 2), F(-1, 2))
    check("clamped", "variational response", 2*integral(optimum)-integral(multiply(derivative(optimum), derivative(optimum))) == F(1, 12))
    check("clamped", "maximizer not clamped", derivative(optimum)[0] != 0 and sum(derivative(optimum)) != 0)
    for coefficients in product(range(-2, 3), repeat=2):
        # Every polynomial below is an admissible clamped f, hence f=C(f'''').
        f = multiply((F(), F(), F(1), F(-2), F(1)), tuple(map(F, coefficients)))
        fp, fpp = derivative(f), derivative(derivative(f))
        c2, d2, f2 = (integral(multiply(p, p)) for p in (fpp, fp, f))
        check("clamped", "moment annihilation "+repr(coefficients), integral(fpp) == 0 and integral((F(),)+fpp) == 0)
        check("clamped", "Sobolev bounds "+repr(coefficients), f2 <= d2/6 and d2 <= c2/6 and integral(f)**2 <= c2/36)
        lower = F(1, 6)-(2*integral(f)-d2)-(1+c2)
        check("clamped", "all-trial inequality control "+repr(coefficients), lower <= -F(4, 5))
    for c in (F(), F(1, 5), F(1), F(7, 2)):
        check("clamped", "completed bound square "+str(c),
              -F(5, 6)+c/3-5*c*c/6 == -F(4, 5)-F(5, 6)*(c-F(1, 5))**2)
    # Exact Gaussian-integer counterexample to the ORIGINAL printed square.
    g = ((1, 1j), (-1j, 1)); u = (1j, 1)
    energy = sum(mv(g, u)[i]*u[i].conjugate() for i in range(2))
    wrong, corrected = abs(u[0]-1j*u[1])**2, abs(u[0]+1j*u[1])**2
    check("paper_mutant", "wrong conjugation exact control", energy == corrected == 4 and wrong == 0)
    return {"clamped_response": "1/12", "A": "1/6", "true_short": "1/12",
            "declared_kappa": "1", "every_trial_sufficient_lower_upper": "-4/5",
            "minimum_relative_residual_squared": "1",
            "source": "SYNTHETIC_CLAMPED_BIHARMONIC_NOT_SUZUKI",
            "conjugation_mutant": {"a": 1, "d": 1, "z": "i", "x": "i", "y": 1,
                                    "true_energy": 4, "old_printed_square": 0}}


def direct_sum_audit():
    from observational_succ.compact_galerkin import graph_failure_stage
    rows = []
    for j in range(1, 17):
        s = F(1, 2**j)
        d = ((s**8, s**7/2), (s**7/2, s**6))
        k = s**8/2
        b = (s**5, F())
        dk = ((d[0][0]-k, d[0][1]), (d[1][0], d[1][1]-k))
        u = (b[0]/d[0][0], F())
        v = solve2(d, b)
        residual = tuple(x-y for x, y in zip(b, mv(d, u)))
        # All tails are full infinite geometric sums, not finite truncations.
        tail_s2 = s*s/3
        response_tail = F(4, 3)*tail_s2
        relative_tail = 2*tail_s2
        energy_gap = dot(b, v)-dot(b, u)+response_tail
        c_odd = dot(residual, residual)/k+relative_tail
        relative_hs = sum((x*x/k for row in d for x in row), F())
        check("direct_sum", f"coercivity {j}", dk[0][0] > 0 and det2(dk) > 0)
        check("direct_sum", f"determinant {j}", det2(dk) == s**14*(1-s*s)/4)
        check("direct_sum", f"response {j}", dot(b, v) == 4*s*s/3)
        check("direct_sum", f"HS {j}", relative_hs == 2*s**8+s**6+2*s**4)
        check("direct_sum", f"odd residual {j}", c_odd == F(1, 2)+2*s*s/3)
        check("direct_sum", f"odd gap {j}", energy_gap == 7*s*s/9)
        for complete, gap, c in ((False, energy_gap, c_odd),
                                  (True, response_tail, relative_tail)):
            got = graph_failure_stage(j, complete)
            check("direct_sum_api", f"stage {j},{complete}",
                  got["R0"] == F(4, 9)
                  and got["true_D_relative_residual_squared"] == gap
                  and got["full_K_relative_residual_squared"] == c
                  and got["authentic_weil_source"] is False)
        rows.append({"j": j, "odd_C": str(c_odd), "odd_energy_gap": str(energy_gap),
                     "even_C": str(relative_tail), "even_energy_gap": str(response_tail)})
    # Sum_j s_j^p = 1/(2^p-1), j starts at one.
    check("direct_sum", "global response", F(4, 3)/3 == F(4, 9))
    return {"R0": "4/9", "relative_source_squared": "2/3",
            "relative_map_HS_squared": str(F(2, 255)+F(1, 63)+F(2, 15)),
            "source": "SYNTHETIC_DIRECT_SUM_NOT_SUZUKI", "rows": rows}


def observer_audit():
    from observational_succ import observer_schur as s
    from observational_succ.source_field_inverse_limits import FieldSourcePassport
    space = s.RationalSourceSpace(FieldSourcePassport("hostile-rational-model", "linear", 0), ("x", "y"))
    for a, b, d in product(range(-3, 4), range(-3, 4), range(4)):
        g = ((F(a), F(b)), (F(b), F(d)))
        model = s.QuadraticModel(space, g)
        split = s.BlockModel(model, 1)
        for c, e in ((1, 0), (0, 1), (1, 1), (1, -2), (0, 0)):
            obs = s.LinearObservation(space, ((c, e),))
            # Nullspace is explicit; no producer elimination algorithm is used.
            zs = ((F(e), F(-c)),) if (c, e) != (0, 0) else ((F(1), F()), (F(), F(1)))
            expected = all(mv(g, z) == (0, 0) for z in zs)
            answer = s.energy_factorization(model, obs)
            check("energy", repr((a, b, d, c, e)), answer["factors"] == expected)
            if not expected:
                u, v = answer["witness"]
                check("energy_witness", repr((a, b, d, c, e)),
                      c*u[0]+e*u[1] == c*v[0]+e*v[1] and q(g, u) != q(g, v))
        expected_sign = (b == 0 if d == 0 else a >= 0 and a*d >= b*b)
        answer = s.sign_factorization(split)
        check("sign", repr((a, b, d)), answer["factors"] == expected_sign)
        if not expected_sign:
            u, v = answer["witness"]
            check("sign_witness", repr((a, b, d)), u[0] == v[0] and q(g, u) < 0 < q(g, v))
        for x in (F(-2), F(), F(3, 2)):
            env = s.fiber_envelope(split, (x,))
            finite = bool(d or b*x == 0)
            check("envelope", repr((a, b, d, x)), env["finite"] == finite)
            if finite:
                value = a*x*x - (F(b*b, d)*x*x if d else 0)
                check("envelope_value", repr((a, b, d, x)), env["value"] == value)
            else:
                h = env["hidden_ray"][0]
                check("envelope_ray", repr((a, b, d, x)),
                      q(g, (x, 7*h))-q(g, (x, F())) == -14)
    # Congruence-free 2x2 criterion compared to a separately written determinant.
    for a, b, d in product(range(-3, 4), repeat=3):
        got = s.psd_two_by_two(((a, b), (b, d)))
        check("PSD2", repr((a, b, d)), got["psd"] == (a >= 0 and d >= 0 and a*d-b*b >= 0))
    wrong = s.LinearObservation(s.RationalSourceSpace(
        FieldSourcePassport("different-source", "linear", 0), ("x", "y")), ((1, 0),))
    rejects("source_identity", "same matrix wrong source", lambda: s.energy_factorization(model, wrong))


def rehash(packet):
    packet.pop("digest", None)
    packet["digest"] = sha256(json.dumps(packet, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return packet


def bridge_audit():
    from observational_succ import formal_instance_bridge as b
    good = [b.affine_packet([("S", 1), ("V", 2), ("S", 3)], source_id="audit-source", epoch=7),
            b.retract_packet(6, 2, source_id="audit-source", epoch=7)]
    b.verify_pins(ROOT, b.RUNTIME_PINS)
    check("bridge", "runtime source pins", True)
    for index, original in enumerate(good):
        result = b.replay_packet(original, source_id="audit-source", epoch=7)
        check("bridge", f"baseline {index}", result["kernel_verification_performed"] is False)
        for key, value in (
            ("source_id", "forged-source"), ("epoch", 8), ("epoch", True),
            ("source_obligations", []), ("source_obligations", b.SOURCE_OBLIGATIONS[:-1]),
            ("universal_python_correctness", True), ("physical_source_authenticated", True),
            ("requested_scope", "UNIVERSAL_THEOREM"), ("parameter_mapping", {}),
            ("runtime_pins", {}), ("lean_pins", {}),
        ):
            bad = deepcopy(original)
            bad[key] = value
            rehash(bad)
            rejects("bridge_forged_hash", f"{index}:{key}:{value!r}",
                    lambda bad=bad: b.replay_packet(bad, source_id="audit-source", epoch=7))
        for role in original["parameter_mapping"]:
            bad = deepcopy(original)
            bad["parameter_mapping"].pop(role)
            rehash(bad)
            rejects("bridge_mapping", f"missing {index}:{role}",
                    lambda bad=bad: b.replay_packet(bad, source_id="audit-source", epoch=7))
        for role in original["outputs"]:
            bad = deepcopy(original)
            if index == 0:
                bad["outputs"][role] += 1
            else:
                bad["outputs"][role][0][0] = "99"
            rehash(bad)
            rejects("bridge_wrong_model", f"wrong output {index}:{role}",
                    lambda bad=bad: b.replay_packet(bad, source_id="audit-source", epoch=7))
    # The source label is intentionally NOT authenticated. If all callers agree
    # on a false label, success must remain model-only with obligations retained.
    relabeled = deepcopy(good[0]); relabeled["source_id"] = "genuine-Weil-source"
    rehash(relabeled)
    result = b.replay_packet(relabeled, source_id=relabeled["source_id"], epoch=7)
    check("bridge_authority", "self-consistent false label grants no semantics",
          result["kernel_verification_performed"] is False
          and result["universal_python_correctness"] is False
          and len(result["retained_source_obligations"]) == 3
          and relabeled["physical_source_authenticated"] is False)
    source, _ = b.lean_source(b.affine_packet([], source_id="x\naxiom danger : False", epoch=0))
    check("bridge_authority", "source label is not Lean syntax", "axiom danger" not in source)
    rejects("bridge_domain", "composite multiplication", lambda: b.affine_packet([("V", 6)], source_id="s", epoch=0))
    rejects("bridge_domain", "boolean modulus", lambda: b.retract_packet(True, 2, source_id="s", epoch=0))


def capsule_audit():
    from observational_succ.source_proof_certificate import audit_capsules, evidence_file
    evidence = evidence_file(ROOT, "observational_succ/source_proof_certificate.py", "AUDIT_INPUT")
    base = {"claim_id": "T", "authority": "PAPER_PROVED", "statement": "0=1: intentionally false",
            "source": "synthetic", "operations_relations": "addition", "target_carrier": "Q",
            "observation_morphisms": "identity", "topology_measure": "discrete",
            "universal_property": "none claimed", "comparison_maps": "identity",
            "source_identity": "declared-model", "source_epoch": 0, "hypotheses": [],
            "dependencies": [], "scope": "UNIVERSAL", "conclusion_mode": "THEOREM_UNDER_HYPOTHESES",
            "evidence": [evidence],
            "access": {k: "explicit audit model" for k in ("permitted_observations", "constructible_witness", "oracle", "probe_discrimination", "proof_theory", "execution_cost")},
            "adversarial": {k: "hostile control" for k in ("domain_tests", "negative_examples", "source_mutations", "replay")}}
    result = audit_capsules([base], ROOT)
    check("capsule_authority", "matching hash cannot prove false theorem",
          result["theorems_proved_by_this_audit"] == []
          and result["claims"][0]["semantic_authority_issued"] is None)
    for label in ("UNVERIFIED", "REFUTED", "TESTED_MODEL"):
        u = dict(base, claim_id="U", authority=label,
                 conclusion_mode={"UNVERIFIED": "OPEN_TARGET", "REFUTED": "COUNTEREXAMPLE", "TESTED_MODEL": "INSTANCE_ONLY"}[label],
                 scope="NUMERICAL_MODEL" if label == "TESTED_MODEL" else "UNIVERSAL")
        b = dict(base, claim_id="B", dependencies=["U"], hypotheses=["ASSUME:U"])
        c = dict(base, claim_id="C", dependencies=["B"])
        rejects("capsule_regression", label+": transitive laundering", lambda: audit_capsules([u, b, c], ROOT))
        c["hypotheses"] = ["ASSUME:U"]
        result = audit_capsules([u, b, c], ROOT)
        check("capsule_regression", label+": explicit debt retained", result["claims"][-1]["open_dependencies"] == ["U"])
    for authority in ("PAPER_PROVED", "CLASSICAL_IMPORTED", "LEAN_KERNEL_PROVED"):
        rejects("capsule_regression", authority+": open target", lambda authority=authority:
                audit_capsules([dict(base, authority=authority, conclusion_mode="OPEN_TARGET")], ROOT))
    b = dict(base, claim_id="B", hypotheses=["A bounded", "D square-root range"])
    c = dict(base, claim_id="C", dependencies=["B"])
    result = audit_capsules([b, c], ROOT)
    check("capsule_regression", "ordinary inherited conditions", result["claims"][-1]["retained_hypotheses"] == ["A bounded", "D square-root range"])


def sha_file(path):
    return sha256(path.read_bytes()).hexdigest()


def repository_head(root):
    """Read metadata directly; does not execute Git or alter repository state."""
    marker = root / ".git"
    gd = (root / marker.read_text().strip().split(":", 1)[1].strip()).resolve() if marker.is_file() else marker
    common = (gd / (gd/"commondir").read_text().strip()).resolve() if (gd/"commondir").is_file() else gd
    head = (gd/"HEAD").read_text().strip()
    if not head.startswith("ref: "):
        return {"head": head, "branch": None}
    ref = head[5:]
    if (common/ref).is_file():
        commit = (common/ref).read_text().strip()
    else:
        commit = next(line.split()[0] for line in (common/"packed-refs").read_text().splitlines()
                      if line.endswith(" " + ref))
    return {"head": commit, "branch": ref.removeprefix("refs/heads/")}


def snapshot():
    paths = ["observational_succ/observer_schur.py", "observational_succ/compact_galerkin.py",
             "observational_succ/formal_instance_bridge.py", "scripts/formal_instance_bridge_probe.py",
             "observational_succ/source_proof_certificate.py", "observational_succ/finite_affine_presentation.py",
             "observational_succ/finite_quotient_retract.py", "scripts/observer_schur_independent_audit.py",
             "observational_succ/observer_schur_source.py", "observational_succ/source_weil_hierarchy.py",
             "observational_succ/suzuki_legendre_source.py", "observational_succ/observer_discovery.py",
             "observational_succ/recursive_operator_gluing.py", "provenance/IMPORT_MANIFEST.json",
             "research/2026-10-16/source-schur-exact.json", "research/2026-10-16/OBSERVER_SCHUR_THEOREMS.md",
             "research/2026-10-16/COMPACT_SOURCE_GALERKIN.md",
             "research/2026-10-16/FORMAL_SOURCE_APPLICATION_CONTRACT.md",
             "reviews/2026-10-15_PROOF_TEETH_SCHUR_INDEPENDENT_AUDIT.md"]
    return {name: sha_file(ROOT/name) for name in paths if (ROOT/name).is_file()}


def main():
    started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--source-integrals", action="store_true",
                        help="also independently integrate 12 full-source polynomial pairs at Gamma512")
    args = parser.parse_args()
    before = snapshot()
    blocks = direct_sum_audit()
    observer_audit()
    bridge_audit()
    capsule_audit()
    clamped = clamped_controls()
    source = source_certificate_audit(args.source_integrals)
    after = snapshot()
    check("source_stability", "audited source unchanged during run", before == after)
    result = {"schema": "OBSERVER_SCHUR_INDEPENDENT_HOSTILE_AUDIT_v1",
              "timestamp_utc": datetime.now(timezone.utc).isoformat(), "argv": sys.argv,
              "python": sys.version, "executable": sys.executable, "cwd": str(Path.cwd()),
              "repository": repository_head(ROOT), "source_sha256_before": before,
              "source_sha256_after": after, "counts": COUNTS, "checks": sum(COUNTS.values()),
              "failures": FAILURES, "direct_sum": blocks, "clamped": clamped,
              "source_ansatz_certificate": source,
              "elapsed_seconds": round(time.monotonic()-started, 6),
              "kernel_replayed_by_this_audit": False, "full_suite_run": False,
              "original_S0_sign": "OPEN", "RH_proved": False,
              "status": "PASS_WITH_DECLARED_SCOPE" if not FAILURES else "DEFECTS_FOUND"}
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text)
    return bool(FAILURES)


if __name__ == "__main__":
    raise SystemExit(main())
