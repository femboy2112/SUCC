"""OPUS IV (hostile referee) receipts for the Second Forge, 2026-11-14.

Every test is an exact receipt for one finding ``R-n`` of
research/2026-11-14/principia_observatoris_second_forge/agents/OPUS_IV_HOSTILE_REFEREE.md.

Reading convention:
  * ``test_R*_refutes_*`` PASSES when the defect is present; it records a
    concrete counterexample to a statement AS WORDED in the package.
  * ``test_R*_survives_*`` PASSES when the attacked statement (or the repaired
    statement given in the report) held on every model the attack tried.
    Finite checks are evidence, not proofs, except where a docstring says the
    finite check is a complete certificate.
  * ``test_R*_vacuous_*`` demonstrates that an existing test cannot fail.

Identifiers follow the CURRENT CAUSAL_GEOMETRY.md (QG-n; formerly CG-n).
Exact arithmetic only (Fraction).  No physical, RH or novelty claim.
"""
from __future__ import annotations

from collections import deque
from fractions import Fraction as F
from itertools import product
import os
from pathlib import Path
import random
import shutil
import subprocess
import tempfile
import unittest

from observational_succ.observatoris_response_geometry import (
    SIGNED_DIAMOND,
    diagonal_similarity,
    edges,
    effect_time,
    gauge_invariant_dimension,
    is_balanced_up_to_sign,
    matrix,
    powers,
    quotient_pattern,
    relevance,
    rescale,
    simple_cycle_products,
    structural_distance,
    switching_function,
    triangle_violations,
    walk_exists,
)
from observational_succ.observatoris_classical_appearance import (
    QUBIT_OPERATIONS,
    classical_four_state_transcripts,
    is_free_observation,
    predictive_ambiguity,
    qubit_transcripts,
    window_carrier,
)
from observational_succ.observatoris_finite_horizons import (
    berlekamp_massey,
    extremal_linear_pair,
    founding_b,
    founding_b_order,
    harmonic,
    lcp,
)

ROOT = Path(__file__).resolve().parents[1]


# ----------------------------------------------------------------- helpers

def bfs_dist(n, succ, start):
    """Directed distances from ``start``; None = unreachable."""
    dist = [None] * n
    dist[start] = 0
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in succ[u]:
            if dist[v] is None:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def le_dist(a, b):
    """a <= b for distances where None means +infinity."""
    if b is None:
        return True
    return a is not None and a <= b


def random_rows(rng, n, values, density):
    return tuple(tuple(rng.choice(values) if rng.random() < density else 0
                       for _ in range(n)) for _ in range(n))


def run_network(parents, tables, init, sensors, policy, steps):
    """Synchronous network; the override applied at time t+1 is policy(record
    through time t).  Returns the list of states and the sensor record."""
    n = len(parents)
    states = [tuple(init)]
    record = [tuple(init[s] for s in sensors)]
    for _ in range(steps):
        z = states[-1]
        new = [tables[v][tuple(z[p] for p in parents[v])] for v in range(n)]
        for a, val in policy(tuple(record)).items():
            new[a] = val
        states.append(tuple(new))
        record.append(tuple(new[s] for s in sensors))
    return states, record


def identity_tables(parents):
    """Each node copies its unique parent (values 0/1)."""
    return [{(b,): b for b in (0, 1)} for _ in parents]


def linear_run(a, z0, steps, overrides=None):
    """z_{t+1} = A z_t with optional open-loop overrides {time: {node: value}}."""
    n = len(a)
    out = [tuple(F(v) for v in z0)]
    for t in range(1, steps + 1):
        z = out[-1]
        new = [sum((a[v][u] * z[u] for u in range(n)), F(0)) for v in range(n)]
        for node, val in (overrides or {}).get(t, {}).items():
            new[node] = F(val)
        out.append(tuple(new))
    return out


def mat(rows):
    return [[F(x) for x in r] for r in rows]


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a):
    n = len(a)
    m = [list(r) + [F(int(i == j)) for j in range(n)] for i, r in enumerate(a)]
    for c in range(n):
        p = next((r for r in range(c, n) if m[r][c] != 0), None)
        if p is None:
            return None
        m[c], m[p] = m[p], m[c]
        inv = 1 / m[c][c]
        m[c] = [x * inv for x in m[c]]
        for r in range(n):
            if r != c and m[r][c] != 0:
                f = m[r][c]
                m[r] = [x - f * y for x, y in zip(m[r], m[c])]
    return [row[n:] for row in m]


def rank(rows):
    m = [list(r) for r in rows]
    rk, col, ncols = 0, 0, (len(m[0]) if m else 0)
    while rk < len(m) and col < ncols:
        p = next((r for r in range(rk, len(m)) if m[r][col] != 0), None)
        if p is None:
            col += 1
            continue
        m[rk], m[p] = m[p], m[rk]
        for r in range(len(m)):
            if r != rk and m[r][col] != 0:
                f = m[r][col] / m[rk][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[rk])]
        rk += 1
        col += 1
    return rk


# =================================================== quotient geometry (QG)

class QuotientGeometryReceipts(unittest.TestCase):

    def test_R03_refutes_coarse_graining_cannot_hide_an_ancestor(self):
        # QG-5 / C-6 scope: the MUST-quotient of QG-4 is also a coarse-graining
        # built from the source alone, and it hides a one-step ancestor.
        q = (0, 0, 1)
        R = {(1, 2)}
        fib = {a: [u for u in range(3) if q[u] == a] for a in (0, 1)}
        must = {(a, b) for a in (0, 1) for b in (0, 1)
                if all(any((u, v) in R for v in fib[b]) for u in fib[a]) and a != b}
        self.assertEqual(must, set())               # d_forall(a,b) = infinity
        src = bfs_dist(3, [[v for (u, v) in R if u == w] for w in range(3)], 1)
        self.assertEqual(src[2], 1)                 # d_C(1,2) = 1: an unseen ancestor

    def test_R02_refutes_ghost_detection_without_source_access(self):
        # Two sources with identical quotient data (q, Q_exists, Q_forall and
        # hence their closures) disagree on whether start 0 is a ghost.
        # (Same models as the PI's C-9; here they refute the "no experiment is
        # needed" asymmetry of section 2, which presupposes the source table.)
        q, starts = (0, 0, 1), 0
        fib = {a: [u for u in range(3) if q[u] == a] for a in (0, 1)}

        def data(R):
            ex = {(q[u], q[v]) for (u, v) in R}
            al = {(a, b) for a in (0, 1) for b in (0, 1)
                  if all(any((u, v) in R for v in fib[b]) for u in fib[a])}
            return ex, al

        def ghost(R):
            succ = [[v for (u, v) in R if u == w] for w in range(3)]
            reach = {v for v, d in enumerate(bfs_dist(3, succ, starts)) if d is not None}
            ex, _ = data(R)
            qsucc = [[b for (a, b) in ex if a == c] for c in (0, 1)]
            qreach = {b for b, d in enumerate(bfs_dist(2, qsucc, q[starts])) if d is not None}
            return qreach != {q[v] for v in reach}

        Ra, Rb = {(1, 2), (1, 0)}, {(0, 1), (1, 2)}
        self.assertEqual(data(Ra), data(Rb))
        self.assertTrue(ghost(Ra))
        self.assertFalse(ghost(Rb))

    def test_R04_refutes_hq4_equality_iff_cost_exactness(self):
        # HQ-4: "d_Qexists(q x, q y) = d_C(x,y) iff cost-exactness (QG-3)".
        # Edge 0 -> 2 only, labels (0,1,1): exact at every start, yet
        # d_Q(q0, q1) = 1 < d_C(0,1) = infinity.  Exactness equates d_Q with the
        # distance to the FIBRE, not to the chosen representative.
        a = matrix(((0, 0, 0), (0, 0, 0), (1, 0, 0)))
        labels = (0, 1, 1)
        dq, ds = structural_distance(quotient_pattern(a, labels)), structural_distance(a)
        self.assertEqual(dq[0][1], 1)
        self.assertIsNone(ds[0][1])
        for x in range(3):          # endpoint exactness: may-closure = pushed source closure
            pushed = {labels[v] for v in range(3) if ds[x][v] is not None}
            quot = {b for b in range(2) if dq[labels[x]][b] is not None}
            self.assertEqual(pushed, quot)
            for b in range(2):      # repaired statement: equality with the fibre distance
                fibre = [ds[x][v] for v in range(3) if labels[v] == b and ds[x][v] is not None]
                self.assertEqual(dq[labels[x]][b], min(fibre) if fibre else None)

    def test_R08_refutes_may_equals_must_for_closure_off_image(self):
        # QG-3 item 5 says "equivalently Q_exists(R) <= Q_forall(R*)" (true) and
        # "equivalently may = must for the closure" (false as an equality when q
        # is not surjective: on an empty fibre the must-value is the empty meet,
        # TOP, and the may-value is BOTTOM).  Exhaustive Boolean check over all
        # relations on 3 states and ALL maps into 3 reports (27, most not onto).
        def reach(R, x):
            seen, todo = {x}, [x]
            while todo:
                u = todo.pop()
                for (s, t) in R:
                    if s == u and t not in seen:
                        seen.add(t)
                        todo.append(t)
            return seen
        all_pairs = [(u, v) for u in range(3) for v in range(3)]
        off_image_cases = 0
        for mask in range(1 << 9):
            R = {all_pairs[i] for i in range(9) if mask >> i & 1}
            star = {x: reach(R, x) for x in range(3)}
            Rs = {(u, v) for u in range(3) for v in star[u]}
            for q in product(range(3), repeat=3):
                fib = {a: [u for u in range(3) if q[u] == a] for a in range(3)}
                may = lambda S, a, b: any((u, v) in S for u in fib[a] for v in fib[b])
                must = lambda S, a, b: all(any((u, v) in S for v in fib[b]) for u in fib[a])
                Q = {(a, b) for a in range(3) for b in range(3) if may(R, a, b)}
                exact = all({q[v] for v in star[x]} == reach(Q, q[x]) for x in range(3))
                crit = all(not may(R, a, b) or must(Rs, a, b) for a in range(3) for b in range(3))
                self.assertEqual(exact, crit)
                on_image = all(may(Rs, a, b) == must(Rs, a, b)
                               for a in set(q) for b in range(3))
                self.assertEqual(exact, on_image)
                everywhere = all(may(Rs, a, b) == must(Rs, a, b)
                                 for a in range(3) for b in range(3))
                if exact and len(set(q)) < 3:
                    self.assertFalse(everywhere)
                    off_image_cases += 1
        self.assertGreater(off_image_cases, 0)

    def test_R01_survives_strongest_qg5_quasar_free_iff_every_edge_covered(self):
        # Repaired QG-5 (Boolean/cost instance), exhaustive on 3 source nodes,
        # every labelling and every loop-free observer graph G on the reports:
        #   d_G(qx,qy) <= d_C(x,y) for all x,y   <=>   every source edge u->v has
        #   q(u) = q(v) or q(u)->q(v) in G   <=>   Q_exists (off-diagonal) is a subgraph of G.
        # So the may-quotient is the LEAST quasar-free geometry; quasars are
        # exactly uncovered edges, decidable from (source, G) without experiment.
        labellings = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (0, 1, 2))
        pairs3 = [(u, v) for u in range(3) for v in range(3) if u != v]
        checked = strict = 0
        for mask in range(1 << len(pairs3)):
            R = [pairs3[i] for i in range(len(pairs3)) if mask >> i & 1]
            succ = [[v for (u, v) in R if u == w] for w in range(3)]
            dC = [bfs_dist(3, succ, x) for x in range(3)]
            for q in labellings:
                m = max(q) + 1
                pairs_m = [(a, b) for a in range(m) for b in range(m) if a != b]
                may = {(q[u], q[v]) for (u, v) in R if q[u] != q[v]}
                for gmask in range(1 << len(pairs_m)):
                    G = {pairs_m[i] for i in range(len(pairs_m)) if gmask >> i & 1}
                    gsucc = [[b for (a, b) in G if a == c] for c in range(m)]
                    dG = [bfs_dist(m, gsucc, a) for a in range(m)]
                    free = all(le_dist(dG[q[x]][q[y]], dC[x][y])
                               for x in range(3) for y in range(3))
                    covered = all(q[u] == q[v] or (q[u], q[v]) in G for (u, v) in R)
                    self.assertEqual(free, covered)
                    self.assertEqual(covered, may <= G)
                    checked += 1
                    strict += covered and may < G
        self.assertGreater(checked, 4000)
        self.assertGreater(strict, 0)   # quasar-free geometries strictly coarser than Q_exists exist


# =================================================== response geometry (RG)

class ResponseGeometryReceipts(unittest.TestCase):

    def test_R12_refutes_unscoped_four_node_minimality_self_return(self):
        # RG-1(c) scope: with x = z and POSITIVE lags, three nodes already give
        # a node whose closed walks (every even length) all cancel.
        a = matrix(((0, 1, 1), (1, 0, 0), (-1, 0, 0)))   # x->w (+1), x->z (-1), w->x, z->x
        P, W = powers(a, 12), walk_exists(a, 12)
        for t in range(1, 13):
            self.assertEqual(P[t][0][0], 0)
            self.assertEqual(W[t][0][0], t % 2 == 0)
        # ... and two nodes never do (all 2x2 tables over {-2..2}).
        for flat in product((-2, -1, 0, 1, 2), repeat=4):
            b = matrix((flat[:2], flat[2:]))
            Pb, Wb = powers(b, 4), walk_exists(b, 4)
            for x in range(2):
                if any(Wb[t][x][x] for t in range(1, 5)):
                    self.assertTrue(any(Pb[t][x][x] != 0 for t in range(1, 5)))

    def test_R11_refutes_fixed_horizon_metric_reading_of_rg3(self):
        # RG-3 is a GRADED inequality (horizons S, T, S+T).  At one fixed horizon
        # the triangle inequality fails, and D_T = -log R_T takes negative values.
        chain = matrix(((0, 0, 0), (1, 0, 0), (0, 1, 0)))
        r1 = relevance(chain, 1)
        self.assertEqual(r1[0][2], 0)                       # D_1(x,z) = +infinity
        self.assertEqual(r1[0][1] * r1[1][2], 1)            # D_1(x,y) + D_1(y,z) = 0
        self.assertEqual(relevance(matrix(((2,),)), 1)[0][0], 2)            # D(x,x) = -log 2
        self.assertEqual(relevance(matrix(((0, 0), (5, 0))), 1)[0][1], 5)  # D(x,y) < 0
        # The chosen discount gamma reverses which source is "closer".
        a = matrix(((0, 0, 0, 0, 0), (F(1, 10), 0, 0, 0, 0), (0, 0, 0, 0, 0),
                    (0, 0, 1, 0, 0), (0, 0, 0, 1, 0)))
        slow, fast = relevance(a, 2, F(1, 20)), relevance(a, 2, F(1))
        self.assertGreater(slow[0][1], slow[2][4])
        self.assertLess(fast[0][1], fast[2][4])

    def test_R10_refutes_minus_log_is_derived_founding_transform_also_works(self):
        # The founding note's l = log(1 + 1/R) (and the clamp max(0, -log R))
        # satisfy the same graded triangle inequality on every nonnegative
        # carrier: (1 + 1/R_{S+T}) <= (1 + 1/R_S)(1 + 1/R_T) and
        # min(1,R_{S+T}) >= min(1,R_S) min(1,R_T).  RG-3 does not single out -log.
        rng = random.Random(41)
        checked = 0
        for _ in range(40):
            a = matrix(random_rows(rng, 4, (1, 2, F(1, 2), F(1, 3)), 0.45))
            for gamma in (F(1), F(1, 2), F(3)):
                rel = {h: relevance(a, h, gamma) for h in range(5)}
                for s, t in product(range(3), repeat=2):
                    for x, y, z in product(range(4), repeat=3):
                        r_st, r_s, r_t = rel[s + t][x][z], rel[s][x][y], rel[t][y][z]
                        if r_s == 0 or r_t == 0:
                            continue
                        self.assertGreater(r_st, 0)
                        self.assertLessEqual(1 + 1 / r_st, (1 + 1 / r_s) * (1 + 1 / r_t))
                        self.assertGreaterEqual(min(1, r_st), min(1, r_s) * min(1, r_t))
                        checked += 1
        self.assertGreater(checked, 1000)

    def test_R09_refutes_no_transform_works_for_unbalanced_carriers(self):
        # RG-3 says "for unbalanced carriers no transform of |rho| can work".
        # The package's own unbalanced negative 3-cycle obeys the graded
        # multiplicative triangle inequality at every horizon and discount tried.
        c = matrix(((0, 0, -1), (1, 0, 0), (0, 1, 0)))
        self.assertIsNone(switching_function(c))
        for s, t in product(range(6), repeat=2):
            for gamma in (F(1), F(1, 2), F(2)):
                self.assertEqual(triangle_violations(c, s, t, gamma), ())
        # The failure needs CANCELLATION (the signed diamond), not imbalance.
        self.assertIn((0, 1, 3), triangle_violations(SIGNED_DIAMOND, 1, 1))

    def test_R13_refutes_harary_cycle_criterion_and_unifying_remark_after_eps(self):
        # With the global sign eps (current RG-4), A = [[-1]] is "balanced", yet
        # its only closed walk has NEGATIVE sign (so the quoted Harary criterion
        # "every closed walk positive" no longer characterises the defined
        # notion), and no signed unit change makes it nonnegative (so the
        # section-5 remark "balance = unit-equivalence to a nonnegative carrier"
        # is false for eps = -1).
        a = matrix(((-1,),))
        self.assertTrue(is_balanced_up_to_sign(a))
        for d in (F(1), F(-1), F(3), F(-1, 7)):
            self.assertEqual(d * a[0][0] / d, -1)
        # Repaired criterion, checked independently on every 3x3 sign table:
        # balanced up to sign  <=>  some eps has sign(W) = eps^|W| for every
        # closed walk W (length <= 3 suffices: it covers all simple cycles).
        for flat in product((-1, 0, 1), repeat=9):
            m = matrix((flat[0:3], flat[3:6], flat[6:9]))
            brute = any(all(e * s[v] * m[v][u] * s[u] >= 0 for u in range(3) for v in range(3))
                        for e in (1, -1) for s in product((1, -1), repeat=3))
            self.assertEqual(brute, is_balanced_up_to_sign(m))
            und = [(u, v, 1 if m[v][u] > 0 else -1) for u, v in edges(m)]
            nb = [[] for _ in range(3)]
            for u, v, sg in und:
                nb[u].append((v, sg))
                if u != v:
                    nb[v].append((u, sg))
            walks = []
            for start in range(3):
                frontier = [(start, 1, 0)]
                for _ in range(3):
                    frontier = [(w, sg * s2, L + 1) for (u, sg, L) in frontier for (w, s2) in nb[u]]
                    walks += [(sg, L) for (w, sg, L) in frontier if w == start]
            crit = any(all(sg == e ** L for sg, L in walks) for e in (1, -1))
            self.assertEqual(crit, brute)

    def test_R14_survives_rg5b_with_every_edge_on_a_directed_cycle(self):
        # Strengthening of RG-5(b): strong connectivity is not needed; it is
        # enough that every edge lies on a directed cycle (each weak component
        # strongly connected).  Two disjoint strongly connected blocks.
        rng = random.Random(43)
        agree = differ = 0
        for _ in range(150):
            rows = [[F(0)] * 5 for _ in range(5)]
            for block in ((0, 1), (2, 3, 4)):
                k = len(block)
                for i in range(k):                     # a directed cycle through the block
                    rows[block[(i + 1) % k]][block[i]] = F(rng.choice((1, 2, 3)))
                for u in block:
                    for v in block:
                        if rng.random() < 0.3:
                            rows[v][u] = F(rng.choice((1, 2, 3)))
            a = matrix(rows)
            if rng.random() < 0.5:
                b = rescale(a, tuple(F(rng.randint(1, 4), rng.randint(1, 4)) for _ in range(5)))
            else:
                b = matrix(tuple(tuple(v * rng.choice((1, 1, 2)) for v in r) for r in a))
            same = simple_cycle_products(a) == simple_cycle_products(b)
            self.assertEqual(diagonal_similarity(a, b) is not None, same)
            agree += same
            differ += not same
        self.assertGreater(agree, 0)
        self.assertGreater(differ, 0)

    def test_R15_survives_betti_count_against_independent_incidence_rank(self):
        # RG-5(c): |E| - rank(coboundary) computed from the incidence matrix,
        # with self-loops (zero rows) and two-cycles, equals |E| - |V| + c.
        rng = random.Random(47)
        for _ in range(300):
            n = rng.randint(1, 5)
            a = matrix(random_rows(rng, n, (1, 2), 0.35))
            E = edges(a)
            if not E:
                self.assertEqual(gauge_invariant_dimension(a), 0)
                continue
            inc = [[F((w == v) - (w == u)) for w in range(n)] for (u, v) in E]
            self.assertEqual(len(E) - rank(inc), gauge_invariant_dimension(a))

    def test_R16_survives_rg6_resolvent_lumpability(self):
        # RG-6: with I - A invertible and q surjective, A lumpable <=> (I-A)^{-1}
        # lumpable (Kemeny-Snell row-block sums; q = (0,0,1)).
        rng = random.Random(53)
        q = (0, 0, 1)

        def lumpable(m):
            return all(sum(m[u][v] for v in range(3) if q[v] == b) ==
                       sum(m[0][v] for v in range(3) if q[v] == b) for u in (0, 1) for b in (0, 1))

        seen = {True: 0, False: 0}
        for i in range(200):
            a = [[F(rng.randint(-3, 3), rng.randint(1, 3)) for _ in range(3)] for _ in range(3)]
            if i % 2 == 0:                          # force lumpability
                a[1][2] = a[0][2]
                a[1][1] = a[0][0] + a[0][1] - a[1][0]
            ima = [[F(int(r == c)) - a[r][c] for c in range(3)] for r in range(3)]
            inv = inverse(ima)
            if inv is None:
                continue
            self.assertEqual(lumpable(a), lumpable(inv))
            seen[lumpable(a)] += 1
        self.assertGreater(min(seen.values()), 20)


# ========================================================= horizons (HQ)

class HorizonReceipts(unittest.TestCase):

    def test_R05_survives_hq1_cone_lemma_with_acting_observer_sharpened(self):
        # Random nonlinear networks (values 0..2, self-loops), sensors that are
        # also actuators, H meeting S or the actuators, record-driven policies
        # WITH MEMORY.  Records agree for t < d(H,S); states agree off the cone
        # for all t <= d(H,S) (one step more than HQ-1 states).
        rng = random.Random(59)
        tried = 0
        for _ in range(300):
            n = rng.randint(2, 6)
            parents = [rng.sample(range(n), rng.randint(0, min(2, n))) for _ in range(n)]
            tables = [{key: rng.randrange(3) for key in product(range(3), repeat=len(p))}
                      for p in parents]
            sensors = rng.sample(range(n), rng.randint(1, min(2, n)))
            actuators = rng.sample(range(n), rng.randint(0, min(2, n)))
            H = rng.sample(range(n), rng.randint(1, min(2, n)))
            memo = {}

            def policy(record, memo=memo, actuators=actuators):
                if record not in memo:
                    memo[record] = {a: rng.randrange(3) for a in actuators if rng.random() < 0.7}
                return memo[record]

            base = [rng.randrange(3) for _ in range(n)]
            other = list(base)
            for h in H:
                other[h] = (other[h] + rng.randint(1, 2)) % 3
            steps = 8
            s1, r1 = run_network(parents, tables, base, sensors, policy, steps)
            s2, r2 = run_network(parents, tables, other, sensors, policy, steps)
            succ = [[v for v in range(n) if u in parents[v]] for u in range(n)]
            dH = [min((d for d in (bfs_dist(n, succ, h)[v] for h in H) if d is not None),
                      default=None) for v in range(n)]
            dS = min((dH[s] for s in sensors if dH[s] is not None), default=None)
            for t in range(steps + 1):
                if dS is None or t < dS:
                    self.assertEqual(r1[:t + 1], r2[:t + 1])
                if dS is None or t <= dS:
                    for v in range(n):
                        if dH[v] is None or dH[v] > t:
                            self.assertEqual(s1[t][v], s2[t][v])
            tried += 1
        self.assertEqual(tried, 300)

    def test_R05b_refutes_cone_lemma_outside_synchronous_updates(self):
        # Boundary check: chain h -> v -> s with sequential (Gauss-Seidel)
        # updates inside a step; the sensor sees the cause at t = 1 < d(h,s) = 2.
        def run(h0):
            h, v, s = h0, 0, 0
            rec = [s]
            for _ in range(2):
                v = h
                s = v
                rec.append(s)
            return rec
        self.assertNotEqual(run(0)[1], run(1)[1])

    def test_R06_refutes_hq2b_for_multi_node_causes(self):
        # HQ-2(b): "on every nonnegative linear carrier, effect and earliest
        # detection times equal the structural distances exactly".  Cause set
        # H = {h1, h2}, both feeding y with weight 1: the perturbation (+1, -1)
        # never reaches y, although d(H,y) = 1 and A >= 0.
        a = matrix(((1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0), (1, 0, 0, 0)))  # h1,h2,y,s
        d = structural_distance(a)
        self.assertEqual(min(d[0][2], d[1][2]), 1)
        base = linear_run(a, (0, 0, 0, 0), 12)
        twin = linear_run(a, (1, -1, 0, 0), 12)
        self.assertTrue(all(b[2] == w[2] for b, w in zip(base, twin)))     # never an effect
        self.assertNotEqual(base[1][3], twin[1][3])                        # detected at d(H,S)=1
        aligned = linear_run(a, (1, 1, 0, 0), 2)
        self.assertNotEqual(aligned[1][2], 0)       # survives for sign-aligned perturbations

    def test_R06b_refutes_hq2b_under_a_clamping_policy(self):
        # Same claim with a lawful (open-loop) policy that clamps the actuator a
        # on the only route h -> a -> y: no effect ever, although d(h,y) = 2.
        a = matrix(((1, 0, 0), (1, 0, 0), (0, 1, 0)))                       # h, a, y
        self.assertEqual(effect_time(a, 0, 2), 2)
        clamp = {t: {1: 0} for t in range(1, 13)}
        base = linear_run(a, (0, 0, 0), 12, clamp)
        twin = linear_run(a, (1, 0, 0), 12, clamp)
        self.assertTrue(all(b[2] == w[2] for b, w in zip(base, twin)))

    def test_R07_refutes_hq3_observer_channel_without_hidden_wire(self):
        # HQ-3 / HQ-4: an effect of x on y before d_M(x,y) is claimed to witness
        # a hidden source edge.  Model = source exactly (x->s, a->y, persistence);
        # the record-driven policy copies the sensor s into the actuator a.
        parents = [[0], [0], [2], [2]]               # x, s, a, y
        tables = identity_tables(parents)
        policy = lambda record: {2: record[-1][0]}
        s0, _ = run_network(parents, tables, (0, 0, 0, 0), (1,), policy, 6)
        s1, _ = run_network(parents, tables, (1, 0, 0, 0), (1,), policy, 6)
        first = next(t for t in range(7) if s0[t][3] != s1[t][3])
        succ = [[v for v in range(4) if u in parents[v]] for u in range(4)]
        dM = bfs_dist(4, succ, 0)
        self.assertEqual(first, 3)
        self.assertIsNone(dM[3])                     # d_M(x,y) = infinity, no hidden edge
        self.assertEqual(dM[1], 1)                   # repaired HQ-3 needs tau <= d_M(x,S) = 1


# ================================================== classical appearance (CA)

R2 = [[F(1), F(1)], [F(1), F(-1)]]          # sqrt(2) * H
XM = [[F(0), F(1)], [F(1), F(0)]]
RHO = {"0": mat(((1, 0), (0, 0))), "1": mat(((0, 0), (0, 1))),
       "+": mat(((F(1, 2), F(1, 2)), (F(1, 2), F(1, 2)))),
       "-": mat(((F(1, 2), F(-1, 2)), (F(-1, 2), F(1, 2))))}
X_MAP = {"0": "1", "1": "0", "+": "+", "-": "-"}
H_MAP = {"0": "+", "+": "0", "1": "-", "-": "1"}


def conj(u, rho, scale):
    return [[x * scale for x in row] for row in mm(mm(u, rho), u)]


def project(rho, k):
    return [[rho[i][j] if i == j == k else F(0) for j in range(2)] for i in range(2)]


def density_transcripts(word):
    """Independent density-matrix simulation of the declared qubit."""
    branches = {(): RHO["0"]}
    for op in word:
        new = {}
        for out, rho in branches.items():
            if op == "X":
                new[out] = conj(XM, rho, F(1))
            elif op == "H":
                new[out] = conj(R2, rho, F(1, 2))
            else:
                for k in (0, 1):
                    p = project(rho, k)
                    if p[k][k] != 0:
                        new[out + (k,)] = p
        branches = new
    return {k: r[0][0] + r[1][1] for k, r in branches.items()}


class ClassicalAppearanceReceipts(unittest.TestCase):

    def test_R17_survives_ca6_complete_one_step_certificate(self):
        """Complete proof of CA-6 for ALL words over {X, H, Z}.

        The twelve identities below say that the map s -> rho_s from the four
        classical states to density matrices intertwines every operation
        (unitaries X, H; the Z instrument with its outcome).  Since the qubit
        update is linear in rho, induction on the word gives: the unnormalised
        post-record operator equals sum_s P_classical(record, s) rho_s, and its
        trace equals P_classical(record).  Hence the transcript laws agree for
        every word, not only for length <= 6.
        """
        for s, rho in RHO.items():
            self.assertEqual(conj(XM, rho, F(1)), RHO[X_MAP[s]])
            self.assertEqual(conj(R2, rho, F(1, 2)), RHO[H_MAP[s]])
            for k in (0, 1):
                p = F(1) if s == str(k) else F(0) if s in "01" else F(1, 2)
                self.assertEqual(project(rho, k), [[x * p for x in r] for r in RHO[str(k)]])
        # Cross-check of three independent implementations, all words <= 7.
        for length in range(8):
            for word in product(QUBIT_OPERATIONS, repeat=length):
                dens = density_transcripts(word)
                self.assertEqual(dens, classical_four_state_transcripts(word))
                if length <= 5:
                    self.assertEqual(dens, qubit_transcripts(word))

    def test_R18_refutes_ca4_ambiguity_formula(self):
        # CA-4: "ambiguity exactly 2^{min(r,t)}".  The register is CYCLIC, so
        # prediction recovers: (n,r,t) = (4,2,3) gives 2, (4,2,4) gives 1, and
        # (4,3,2) gives 2 < 2^2 inside t <= r.  The tests only sampled t <= n-r.
        self.assertEqual(predictive_ambiguity(window_carrier(4, 2), 3), 2)
        self.assertEqual(predictive_ambiguity(window_carrier(4, 2), 4), 1)
        self.assertEqual(predictive_ambiguity(window_carrier(4, 3), 2), 2)
        # Repaired formula, exhaustive for every register the module allows.
        for n in range(1, 5):
            for r in range(1, n + 1):
                c = window_carrier(n, r)
                for t in range(3 * n + 1):
                    s = t % n
                    unseen = min(s, n - s, r, n - r)
                    self.assertEqual(predictive_ambiguity(c, t), 2 ** unseen, (n, r, t))

    def test_R19_refutes_ca3_witness_table_as_computed_independence(self):
        # (i) The module's own predicate says the shift register is NOT freely
        # observed (its 'step' instrument is counted), contrary to row 1.
        self.assertFalse(is_free_observation(window_carrier(4, 2)))
        # (ii) Even granting every cell, NO pair of diagnostics realises all
        # four pass/fail combinations (each pair misses exactly one), and the
        # implication "free => deterministic core" is never separated, so
        # "pairwise independent" is not exhibited by the table.
        # Row 2's predictive cell is "pass on model-building experiments, fail
        # on the held-out contrast"; both readings are checked.
        for hidden_predictive in (1, 0):
            table = {  # free, predictive, deterministic, aligned (THEOREM_FORGE F, CA-3)
                "shift": (1, 0, 1, 1), "hidden-shortcut": (1, hidden_predictive, 1, 0),
                "qubit-XZ": (1, 1, 1, 1), "qubit-XHZ": (0, 1, 0, 1),
                "destructive-ABC": (0, 1, 1, 1)}
            rows = list(table.values())
            for i in range(4):
                for j in range(i + 1, 4):
                    self.assertEqual(len({(r[i], r[j]) for r in rows}), 3, (i, j))
            self.assertFalse(any(r[0] == 1 and r[2] == 0 for r in rows))
            if hidden_predictive:   # then every other ordered implication is separated
                for i in range(4):
                    for j in range(4):
                        if i != j and (i, j) != (0, 2):
                            self.assertTrue(any(r[i] == 1 and r[j] == 0 for r in rows))
            else:                   # otherwise "predictive => aligned" is not separated either
                self.assertFalse(any(r[1] == 1 and r[3] == 0 for r in rows))


# ===================================================== finite horizons (FH)

class FiniteHorizonReceipts(unittest.TestCase):

    def test_R20_survives_fh7_independent_machine_bruteforce(self):
        # Own enumeration of machines (not of rho-words); distinctness certified
        # by length max(n,m) + n*m >= max preperiod + lcm(periods).
        def outputs(k, L):
            out = set()
            for delta in product(range(k), repeat=k):
                for lam in product((0, 1), repeat=k):
                    q, seq = 0, []
                    for _ in range(L):
                        seq.append(lam[q])
                        q = delta[q]
                    out.add(tuple(seq))
            return out
        for n in range(1, 5):
            for m in range(n, 5):
                if n + m > 7:
                    continue
                L = max(n, m) + n * m + 1
                A = set().union(*(outputs(k, L) for k in range(1, n + 1)))
                B = set().union(*(outputs(k, L) for k in range(1, m + 1)))
                best = max(lcp(x, y) for x in A for y in B if x != y)
                self.assertEqual(best, n + m - 2, (n, m))     # agree n+m-2 terms, never n+m-1

    def test_R21_survives_fh3_independent_gf2_pigeonhole(self):
        def lr(n, L):
            out = set()
            for low in product((0, 1), repeat=n):
                for init in product((0, 1), repeat=n):
                    s = list(init)
                    while len(s) < L:
                        k = len(s) - n
                        s.append(sum(low[j] * s[k + j] for j in range(n)) % 2 if n else 0)
                    out.add(tuple(s[:L]))
            return out
        for n in range(0, 4):
            for m in range(n, 4):
                if n + m == 0:
                    continue
                L = 2 ** (n + m) + n + m       # pigeonhole on the joint state
                A, B = lr(n, L), lr(m, L)
                best = max(lcp(x, y) for x in A for y in B if x != y)
                self.assertEqual(best, n + m - 1, (n, m))

    def test_R22_refutes_fh6_equivalently_clause_at_n1_H0(self):
        # FH-6: "b_H in LR_n iff H = 0 (n >= 1) or 1 <= H <= n-2.  Equivalently,
        # the surviving members are those whose deviation comes at or before
        # index n-1."  At n = 1: b_0 = (1,1,1,...) is in LR_1 but deviates from
        # 1/(k+1) first at index 1 > n-1 = 0.
        b0 = founding_b(0, 20)
        self.assertEqual(berlekamp_massey(b0)[0], 1)
        self.assertEqual(lcp(b0, harmonic(20)), 1)
        # The first sentence survives when checked through BM (not the formula).
        for n in range(1, 7):
            for H in range(0, 9):
                order = berlekamp_massey(founding_b(H, 2 * (H + 2) + 8))[0]
                self.assertEqual(order <= n, (H == 0) or (1 <= H <= n - 2), (n, H))

    def test_R23_vacuous_existing_fh5_and_fh6_tests(self):
        # (a) test_no_learner_is_right_on_both_extremal_sequences_at_2d_minus_1
        # asserts not (g == a and g == b); since a != b this holds for EVERY g,
        # including a learner that is right on a.
        for d in range(1, 6):
            e = extremal_linear_pair(d, d, 2 * d + 2)
            a, b = e["a"], e["b"]
            self.assertNotEqual(a, b)
            for g in (a, b, tuple(F(0) for _ in a)):
                self.assertFalse(g == a and g == b)
        # (b) test_declared_dimension_admits_b_H_iff_H_le_n_minus_2 compares the
        # hard-coded formula with itself: H + 2 <= n  <=>  H <= n - 2.
        for n in range(1, 9):
            for H in range(1, 12):
                self.assertEqual(founding_b_order(H), H + 2)

    def test_R24_survives_fh9_receipts_by_independent_evaluation(self):
        def val(alpha, mats, beta, w):
            v = [F(x) for x in alpha]
            for c in w:
                M = mats[c]
                v = [sum((v[i] * F(M[i][j]) for i in range(len(v))), F(0)) for j in range(len(v))]
            return sum((x * F(y) for x, y in zip(v, beta)), F(0))

        def first_diff(A, B, letters, upto):
            for L in range(upto + 1):
                for w in product(letters, repeat=L):
                    if val(*A, w) != val(*B, w):
                        return L, w
            return None, None
        My = [[0, 1], [1, 0]]
        A = ((1, 0), {"x": [[F(1, 4), F(3, 4)], [0, 1]], "y": My}, (0, F(1, 4)))
        B = ((1, 0), {"x": [[F(1, 4), F(3, 4)], [F(1, 2), F(1, 2)]], "y": My}, (0, F(1, 4)))
        self.assertEqual(first_diff(A, B, "xy", 3), (2, ("x", "x")))
        self.assertEqual((val(*A, "xx"), val(*B, "xx")), (F(15, 64), F(9, 64)))
        H1 = ((F(1, 2), F(1, 2)), {"a": [[0, F(1, 2)], [0, F(1, 4)]],
                                   "b": [[F(1, 4), F(1, 4)], [F(1, 2), F(1, 4)]]}, (1, 1))
        H2 = ((F(1, 4), F(3, 4)), {"a": [[0, 0], [F(1, 4), F(1, 4)]],
                                   "b": [[F(1, 2), F(1, 2)], [0, F(1, 2)]]}, (1, 1))
        self.assertEqual(first_diff(H1, H2, "ab", 4)[0], 3)
        # Sanity for the HMM sharpness family: one-letter generative HMMs are
        # all identical (f = 1), so sharpness witnesses must use >= 2 letters.
        one = ((F(1, 3), F(2, 3)), {"a": [[F(1, 2), F(1, 2)], [0, 1]]}, (1, 1))
        self.assertTrue(all(val(*one, "a" * k) == 1 for k in range(6)))

    def test_R25_survives_fh8_moore_mealy_by_pair_reachability(self):
        # Own certificate: equivalence = no output clash on the finite set of
        # state pairs reachable from (s,t); shortest separator by word search.
        N, letters = 3, (0, 1)
        worst = {"moore": -1, "mealy": -1}
        for flat in product(range(N), repeat=N * 2):
            delta = [flat[2 * i:2 * i + 2] for i in range(N)]
            for kind, outs in (("moore", product((0, 1), repeat=N)),
                               ("mealy", product((0, 1), repeat=2 * N))):
                for out in outs:
                    def o(state, a=None, out=out, kind=kind):
                        return out[state] if kind == "moore" else out[2 * state + a]
                    for s in range(N):
                        for t in range(s + 1, N):
                            if kind == "moore" and o(s) != o(t):
                                worst[kind] = max(worst[kind], 0)
                                continue
                            frontier, found, L = {(s, t)}, None, 0
                            seen = set(frontier)
                            while frontier and found is None:
                                L += 1
                                nxt = set()
                                for p, r in frontier:
                                    for a in letters:
                                        if kind == "mealy" and o(p, a) != o(r, a):
                                            found = L
                                        pp, rr = delta[p][a], delta[r][a]
                                        if kind == "moore" and o(pp) != o(rr):
                                            found = L
                                        if (pp, rr) not in seen:
                                            seen.add((pp, rr))
                                            nxt.add((pp, rr))
                                frontier = nxt
                            if found is not None:
                                worst[kind] = max(worst[kind], found)
        self.assertEqual(worst, {"moore": N - 2, "mealy": N - 1})


# ========================================================= Lean encoding

LEAN = shutil.which("lean") or str(Path.home() / ".elan/bin/lean")

INSTANCES = r"""
open ObservationalSUCC.ObservatorisQuantale

def costQ : LaxQuantale (Nat → Prop) where
  le a b := ∀ n, a n → ∃ m, m ≤ n ∧ b m
  mul a b := fun n => ∃ i j, a i ∧ b j ∧ n = i + j
  one := fun n => n = 0
  sSup S := fun n => ∃ a, S a ∧ a n
  le_refl _ := fun n h => ⟨n, Nat.le_refl n, h⟩
  le_trans f g := fun n h =>
    match f n h with
    | ⟨m, hm, hb⟩ => match g m hb with
      | ⟨k, hk, hc⟩ => ⟨k, Nat.le_trans hk hm, hc⟩
  le_sSup hS := fun n h => ⟨n, Nat.le_refl n, _, hS, h⟩
  sSup_le h := fun n ⟨a, ha, han⟩ => h a ha n han
  mul_mono f g := fun n ⟨i, j, hi, hj, e⟩ =>
    match f i hi, g j hj with
    | ⟨i', hi', hb⟩, ⟨j', hj', hd⟩ => ⟨i' + j', by omega, i', j', hb, hd, rfl⟩
  mul_sSup_le _ _ := fun n ⟨i, j, hi, ⟨s, hs, hsj⟩, e⟩ =>
    ⟨n, Nat.le_refl n, _, ⟨s, hs, rfl⟩, i, j, hi, hsj, e⟩
  sSup_mul_le _ _ := fun n ⟨i, j, ⟨s, hs, hsi⟩, hj, e⟩ =>
    ⟨n, Nat.le_refl n, _, ⟨s, hs, rfl⟩, i, j, hsi, hj, e⟩
  mul_assoc_le _ _ _ := fun n ⟨i, j, hi, ⟨k, l, hk, hl, e2⟩, e⟩ =>
    ⟨n, Nat.le_refl n, i + k, l, ⟨i, k, hi, hk, rfl⟩, hl, by omega⟩
  mul_assoc_ge _ _ _ := fun n ⟨i, j, ⟨k, l, hk, hl, e2⟩, hj, e⟩ =>
    ⟨n, Nat.le_refl n, k, l + j, hk, ⟨l, j, hl, hj, rfl⟩, by omega⟩
  mul_one_le _ := fun n ⟨i, j, hi, hj, e⟩ => ⟨i, by omega, hi⟩
  le_mul_one _ := fun n h => ⟨n, Nat.le_refl n, n, 0, h, rfl, rfl⟩
  le_one_mul _ := fun n h => ⟨n, Nat.le_refl n, 0, n, rfl, h, by omega⟩

def langQ (α : Type) : LaxQuantale (List α → Prop) where
  le a b := ∀ w, a w → b w
  mul a b := fun w => ∃ u v, a u ∧ b v ∧ w = u ++ v
  one := fun w => w = []
  sSup S := fun w => ∃ a, S a ∧ a w
  le_refl _ := fun _ h => h
  le_trans f g := fun w h => g w (f w h)
  le_sSup hS := fun _ h => ⟨_, hS, h⟩
  sSup_le h := fun w ⟨a, ha, haw⟩ => h a ha w haw
  mul_mono f g := fun w ⟨u, v, hu, hv, e⟩ => ⟨u, v, f u hu, g v hv, e⟩
  mul_sSup_le _ _ := fun w ⟨u, v, hu, ⟨s, hs, hsv⟩, e⟩ => ⟨_, ⟨s, hs, rfl⟩, u, v, hu, hsv, e⟩
  sSup_mul_le _ _ := fun w ⟨u, v, ⟨s, hs, hsu⟩, hv, e⟩ => ⟨_, ⟨s, hs, rfl⟩, u, v, hsu, hv, e⟩
  mul_assoc_le _ _ _ := fun w ⟨u, v, hu, ⟨k, l, hk, hl, e2⟩, e⟩ =>
    ⟨u ++ k, l, ⟨u, k, hu, hk, rfl⟩, hl, by subst e; subst e2; simp [List.append_assoc]⟩
  mul_assoc_ge _ _ _ := fun w ⟨u, v, ⟨k, l, hk, hl, e2⟩, hv, e⟩ =>
    ⟨k, l ++ v, hk, ⟨l, v, hl, hv, rfl⟩, by subst e; subst e2; simp [List.append_assoc]⟩
  mul_one_le _ := fun w ⟨u, v, hu, hv, e⟩ => by subst hv; subst e; simpa using hu
  le_mul_one _ := fun w h => ⟨w, [], h, rfl, by simp⟩
  le_one_mul _ := fun w h => ⟨[], w, rfl, h, by simp⟩

example {X Y : Type} (R : X → X → (Nat → Prop)) (q : X → Y) (x z : X) :
    costQ.le (star costQ R x z) (star costQ (quot costQ R q) (q x) (q z)) :=
  star_le_quot_star costQ R q x z
example (R : Empty → Empty → (List Bool → Prop)) (q : Empty → Bool) :
    EndpointExact (langQ Bool) R q ↔ FibreConstant (langQ Bool) R q :=
  exact_iff_fibreConstant (langQ Bool) R q
"""

TRUE_MUTATION = r"""
open ObservationalSUCC.ObservatorisQuantale
example {V X Y : Type} (K : LaxQuantale V) (R : X → X → V) (q : X → Y)
    (x : X) (b : Y) :
    K.le (K.sSup (fun _ => False)) (push K q (star K R x) b) :=
  quotAll_star_le_push_star K R q x b
"""

TRUE_MUTATION_PROOF = r"""
open ObservationalSUCC.ObservatorisQuantale
example {V X Y : Type} (K : LaxQuantale V) (R : X → X → V) (q : X → Y)
    (x : X) (b : Y) :
    K.le (K.sSup (fun _ => False)) (push K q (star K R x) b) :=
  K.sSup_le (fun _ h => h.elim)
"""


def lean_ok():
    try:
        out = subprocess.run([LEAN, "--version"], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return False
    return out.returncode == 0 and out.stdout.startswith("Lean (version 4.14.0,")


@unittest.skipUnless(lean_ok(), "pinned Lean 4.14.0 not available")
class LeanEncodingReceipts(unittest.TestCase):

    def compile(self, suffix):
        base = (ROOT / "formal/ObservatorisQuantale.lean").read_text()
        with tempfile.TemporaryDirectory(prefix="opus-iv-") as d:
            path = os.path.join(d, "check.lean")
            Path(path).write_text(base + "\n" + suffix)
            return subprocess.run([LEAN, path], capture_output=True, text=True, timeout=180)

    def test_R26_survives_reversed_cost_and_noncommutative_language_instances(self):
        # LaxQuantale admits ([0,inf] as sets of achievable costs, >=, +, inf)
        # and the noncommutative path-language quantale, in core Lean.
        done = self.compile(INSTANCES)
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)

    def test_R27_refutes_must_is_not_may_control_as_a_falsity_control(self):
        # The control harness accepts "exit 1 with a type error" as rejection.
        # A TRUE mutated statement is rejected in exactly that way ...
        bad = self.compile(TRUE_MUTATION)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("type mismatch", bad.stdout)
        for marker in ("unexpected token", "unknown identifier", "unknown constant"):
            self.assertNotIn(marker, bad.stdout)
        # ... although that statement is a theorem.
        good = self.compile(TRUE_MUTATION_PROOF)
        self.assertEqual(good.returncode, 0, good.stdout + good.stderr)


if __name__ == "__main__":
    unittest.main()
