"""Exact finite factor/Koopman controls; standard library, no numerical fit."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys


def transpose(a):
    return tuple(zip(*a))


def mm(a, b):
    return tuple(tuple(sum((x*y for x, y in zip(row, col)), F())
                       for col in transpose(b)) for row in a)


def koopman(t):
    return tuple(tuple(F(j == t[i]) for j in range(len(t)))
                 for i in range(len(t)))


def pullback(q):
    return tuple(tuple(F(y == x) for y in range(max(q)+1)) for x in q)


def constant_on_fibers(v, q):
    return all(v[i] == v[j] for i in range(len(q))
               for j in range(len(q)) if q[i] == q[j])


def pf(u, weights):
    # Adjoint in the declared weighted L2 inner product, not raw mass push.
    return tuple(tuple(u[j][i]*weights[j]/weights[i]
                       for j in range(len(weights))) for i in range(len(weights)))


def run():
    t, q, s = (1, 2, 3, 0), (0, 1, 0, 1), (1, 0)
    u, j, us = koopman(t), pullback(q), koopman(s)
    assert mm(u, j) == mm(j, us)
    mu = tuple(F(i, 10) for i in (1, 2, 3, 4))
    nu = tuple(sum((mu[i] for i in range(4) if q[i] == y), F())
               for y in range(2))
    l, ls = pf(u, mu), pf(us, nu)
    c = tuple(tuple(j[i][y]*mu[i]/nu[y] for i in range(4)) for y in range(2))
    assert mm(c, l) == mm(ls, c)
    r = transpose(j)
    assert mm(r, transpose(u)) == mm(transpose(us), r)
    one = ((F(1),),)*4
    l_one = tuple(row[0] for row in mm(l, one))
    assert l_one == (F(4), F(1, 2), F(2, 3), F(3, 4))
    assert not constant_on_fibers(l_one, q)
    uniform_l = pf(u, (F(1, 4),)*4)
    assert mm(uniform_l, one) == one
    assert all(constant_on_fibers(col, q) for col in transpose(mm(uniform_l, j)))
    assert mm(u, j) != mm(j, koopman((0, 1)))  # mutated factor

    bad_q = (0, 0, 1, 1)
    g = tuple(F(x == 1) for x in bad_q)
    ug = tuple(g[t[i]] for i in range(4))
    assert bad_q[0] == bad_q[1] and bad_q[t[0]] != bad_q[t[1]]
    assert not constant_on_fibers(ug, bad_q)

    # V=span{1,v} invariant under reflection, but v*v is outside V.
    v, reflection = (F(-1), F(0), F(1)), (2, 1, 0)
    assert tuple(v[reflection[i]] for i in range(3)) == tuple(-x for x in v)
    v_squared = tuple(x*x for x in v)
    a, b = v_squared[1], v_squared[2]-v_squared[1]
    assert v_squared != tuple(a+b*x for x in v)

    # Fresh exhaustive finite domain: 27 transitions times 5 partitions.
    partitions = [p for p in product(range(3), repeat=3)
                  if p[0] == 0 and all(p[i] <= max(p[:i])+1 for i in (1, 2))]
    checked = factors = 0
    for tx in product(range(3), repeat=3):
        ux = koopman(tx)
        for qx in partitions:
            m = max(qx)+1
            exists = any(all(qx[tx[i]] == sx[qx[i]] for i in range(3))
                         for sx in product(range(m), repeat=m))
            columns = transpose(mm(ux, pullback(qx)))
            invariant = all(constant_on_fibers(col, qx) for col in columns)
            assert exists == invariant
            checked += 1
            factors += exists
    assert checked == 135
    return {
        "status": "TESTED MODEL; universal theorem has a separate written proof",
        "baseline_commit": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "command": "python research/2026-10-13/SWARM_ATLAS/D27_probe.py",
        "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "python_version": sys.version.split()[0], "exact_arithmetic": "Fraction",
        "positive": {"T": t, "q": q, "S": s, "U": u, "J": j,
                     "mu": mu, "nu": nu, "L": l, "C": c, "L_S": ls,
                     "U_J_equals_J_U_S": True, "C_L_equals_L_S_C": True,
                     "mass_push_square": True, "L_one": l_one,
                     "measure_preserved": False, "PF_range_invariant": False,
                     "uniform_measure_preserved": True,
                     "uniform_PF_range_invariant": True,
                     "mutated_S_rejected": True},
        "lossy_nonfactor": {"q": bad_q, "fiber_witness": (0, 1),
                            "q_T_witness": (bad_q[t[0]], bad_q[t[1]]), "U_g": ug},
        "linear_nonalgebra": {"T": reflection, "v": v, "v_squared": v_squared,
                             "U_v_equals_minus_v": True, "square_in_V": False},
        "exhaustive_three_state": {"transitions": 27, "partitions": len(partitions),
                                   "cases": checked, "factor_cases": factors,
                                   "mismatches": 0},
        "physical_source_authenticated": False,
        "canonical_invariant_measure_selected": False,
        "academic_originality_claimed": False,
    }


if __name__ == "__main__":
    print(json.dumps(run(), default=str, indent=2, sort_keys=True))
