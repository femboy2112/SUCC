"""OPUS IV (second seat), hostile referee, round 2: executable receipts.

Targets: OPUS_II_CAUSAL_GEOMETER.md (CG-1..CG-13) and OPUS_I_FINITE_OBSERVER.md
(FO-1..FO-10), Operation Principia Observatoris -- Second Forge.

Independence rule: every check below uses this file's OWN brute-force
implementations (quantale tables, Kleene closure, quotients, partitions,
Mobius transforms, GF(2)/Z/4 certification, network evaluation, carrier
minimisation, belief game).  The modules under review are NOT imported.
Exact arithmetic only (ints, bitmasks, fractions.Fraction).

Findings are numbered as in
research/2026-11-14/principia_observatoris_second_forge/agents/OPUS_IV_REFEREE_ROUND2.md
(S-1, S-2, ...).  Each test docstring names the finding it backs.
"""

import random
import unittest
from fractions import Fraction as Fr
from itertools import combinations, product
from math import comb

INF = "inf"   # tropical bottom (no path); never mixed with arithmetic


# ===========================================================================
# Part 0. Independent finite quantales
# ===========================================================================

class FQ:
    """A finite quantale given by explicit operations (own implementation)."""

    def __init__(self, name, els, leq, join2, meet2, tensor, unit, bottom, top):
        self.name, self.els = name, tuple(els)
        self.leq, self.join2, self.meet2, self.t = leq, join2, meet2, tensor
        self.unit, self.bottom, self.top = unit, bottom, top

    def join(self, it):
        r = self.bottom
        for v in it:
            r = self.join2(r, v)
        return r

    def meet(self, it):
        r = self.top
        for v in it:
            r = self.meet2(r, v)
        return r


def bool_q():
    return FQ("Bool", (0, 1), lambda a, b: a <= b, max, min, min, 1, 0, 1)


def _rel2_compose(a, b):
    r = 0
    for i in (0, 1):
        for j in (0, 1):
            if a >> (2 * i + j) & 1:
                for k in (0, 1):
                    if b >> (2 * j + k) & 1:
                        r |= 1 << (2 * i + k)
    return r


_REL2 = [[_rel2_compose(a, b) for b in range(16)] for a in range(16)]


def rel2_q():
    """Quantale of binary relations on a 2-element set: NONcommutative,
    NON-integral (unit = identity = 0b1001 != top = 0b1111), not of the form
    P(monoid).  Not used by the reviewed lab."""
    return FQ("Rel(2)", range(16), lambda a, b: a & ~b == 0, lambda a, b: a | b,
              lambda a, b: a & b, lambda a, b: _REL2[a][b], 0b1001, 0, 15)


def _lz_mult(x, y):            # monoid {e=0, a=1, b=2}, xy = x for x != e
    return y if x == 0 else x


_LZ = [[0] * 8 for _ in range(8)]
for _A in range(8):
    for _B in range(8):
        _r = 0
        for _x in range(3):
            if _A >> _x & 1:
                for _y in range(3):
                    if _B >> _y & 1:
                        _r |= 1 << _lz_mult(_x, _y)
        _LZ[_A][_B] = _r


def leftzero_q():
    return FQ("P(left-zero)", range(8), lambda a, b: a & ~b == 0, lambda a, b: a | b,
              lambda a, b: a & b, lambda a, b: _LZ[a][b], 0b001, 0, 7)


def _pz2_t(a, b):
    r = 0
    for x in (0, 1):
        if a >> x & 1:
            for y in (0, 1):
                if b >> y & 1:
                    r |= 1 << ((x + y) % 2)
    return r


def pz2_q():
    return FQ("P(Z/2)", range(4), lambda a, b: a & ~b == 0, lambda a, b: a | b,
              lambda a, b: a & b, _pz2_t, 0b01, 0, 3)


def _num(a):
    return 10 ** 9 if a == INF else a


def sat_trop(c):
    """{0..c, inf}, order reversed, a(x)b = min(a+b, c), inf absorbing."""
    return FQ(f"sat{c}", tuple(range(c + 1)) + (INF,), lambda a, b: _num(a) >= _num(b),
              lambda a, b: a if _num(a) <= _num(b) else b,
              lambda a, b: a if _num(a) >= _num(b) else b,
              lambda a, b: INF if INF in (a, b) else min(a + b, c), 0, INF, 0)


def budget_trop(c):
    """{0..c, inf}, order reversed, a(x)b = a+b if <= c else inf."""
    return FQ(f"budget{c}", tuple(range(c + 1)) + (INF,), lambda a, b: _num(a) >= _num(b),
              lambda a, b: a if _num(a) <= _num(b) else b,
              lambda a, b: a if _num(a) >= _num(b) else b,
              lambda a, b: INF if INF in (a, b) or a + b > c else a + b, 0, INF, 0)


# ---- V-relations -----------------------------------------------------------

def ident(V, n):
    return tuple(tuple(V.unit if i == j else V.bottom for j in range(n)) for i in range(n))


def comp(V, R, S):
    n, k = len(R), len(S[0])
    return tuple(tuple(V.join(V.t(R[i][j], S[j][l]) for j in range(len(S)))
                       for l in range(k)) for i in range(n))


def rjoin(V, R, S):
    return tuple(tuple(V.join2(a, b) for a, b in zip(r, s)) for r, s in zip(R, S))


def kstar(V, R):
    """Least S >= I with S;R <= S, by Kleene iteration on a finite lattice."""
    n = len(R)
    I = ident(V, n)
    S = I
    while True:
        S2 = rjoin(V, I, comp(V, S, R))
        if S2 == S:
            return S
        S = S2


def fibs(q, m):
    return [[x for x in range(len(q)) if q[x] == a] for a in range(m)]


def q_may(V, R, q, m):
    F = fibs(q, m)
    return tuple(tuple(V.join(R[u][v] for u in F[a] for v in F[b]) for b in range(m))
                 for a in range(m))


def q_must(V, R, q, m):
    F = fibs(q, m)
    return tuple(tuple(V.meet(V.join(R[u][v] for v in F[b]) for u in F[a]) for b in range(m))
                 for a in range(m))


def q_back(V, R, q, m):
    F = fibs(q, m)
    return tuple(tuple(V.meet(V.join(R[u][v] for u in F[a]) for v in F[b]) for b in range(m))
                 for a in range(m))


def profiles(V, Rs, q, m):
    return [tuple(V.join(Rs[x][z] for z in range(len(q)) if q[z] == b) for b in range(m))
            for x in range(len(q))]


def closed(V, R, phi):
    n = len(R)
    return all(V.leq(V.t(phi[u], R[u][v]), phi[v]) for u in range(n) for v in range(n))


def push(V, phi, q, m):
    return tuple(V.join(phi[x] for x in range(len(q)) if q[x] == b) for b in range(m))


def push_all(V, phi, q, m):
    return tuple(V.meet(phi[x] for x in range(len(q)) if q[x] == b) for b in range(m))


def rel_leq(V, A, B):
    return all(V.leq(a, b) for r, s in zip(A, B) for a, b in zip(r, s))


def rand_rel(V, n, rng, density=0.5):
    return tuple(tuple(rng.choice(V.els) if rng.random() < density else V.bottom
                       for _ in range(n)) for _ in range(n))


def rgs(n):
    """Restricted growth strings = set partitions of range(n)."""
    out = []

    def rec(pre, mx):
        if len(pre) == n:
            out.append(tuple(pre))
            return
        for v in range(mx + 2):
            rec(pre + [v], max(mx, v))
    rec([0], 0)
    return out


# ===========================================================================
# Part A. Causal Geometer (CG)
# ===========================================================================

def cg3_conditions(V, R, q, m, preds):
    """Own evaluation of CG-3 (1),(2),(3),(4),(5),(6) on image rows."""
    n = len(R)
    Rs = kstar(V, R)
    Q = q_may(V, R, q, m)
    Qs = kstar(V, Q)
    prof = profiles(V, Rs, q, m)
    img = sorted(set(q))
    c1 = all(prof[x] == Qs[q[x]] for x in range(n))
    c2 = all(prof[x] == prof[y] for x in range(n) for y in range(n) if q[x] == q[y])
    c3 = all(closed(V, Q, push(V, p, q, m)) for p in preds)
    c4 = all(closed(V, R, tuple(push(V, p, q, m)[q[x]] for x in range(n))) for p in preds)
    must_star = q_must(V, Rs, q, m)
    c5 = all(V.leq(Q[a][b], must_star[a][b]) for a in img for b in range(m))
    may_star = q_may(V, Rs, q, m)
    c6 = all(may_star[a] == must_star[a] for a in img)
    return (c1, c2, c3, c4, c5, c6)


def all_closed_preds(V, R):
    return [phi for phi in product(V.els, repeat=len(R)) if closed(V, R, phi)]


class S01_CG3_SevenWaySurvives(unittest.TestCase):
    """S-1: CG-3 survives in a NONcommutative, NON-integral quantale that is not
    P(monoid) (Rel(2)), with non-surjective q and empty fibres."""

    def test_rel2_three_states_noncommutative_nonsurjective(self):
        V = rel2_q()
        self.assertNotEqual(V.t(0b0010, 0b0100), V.t(0b0100, 0b0010))   # noncommutative
        self.assertNotEqual(V.unit, V.top)                              # non-integral
        rng = random.Random(20261114)
        maps = [((0, 0, 1), 2), ((0, 1, 1), 2), ((0, 0, 0), 1), ((0, 0, 2), 4),
                ((1, 1, 3), 4), ((0, 1, 2), 3)]
        seen = set()
        for _ in range(14):
            R = rand_rel(V, 3, rng, 0.55)
            preds = all_closed_preds(V, R)
            for q, m in maps:
                conds = cg3_conditions(V, R, q, m, preds)
                self.assertEqual(len(set(conds)), 1, (R, q, conds))
                seen.add(conds[0])
        self.assertEqual(seen, {True, False})

    def test_boolean_exhaustive_with_off_image_reports(self):
        V = bool_q()
        for n in (1, 2, 3):
            for bits in product((0, 1), repeat=n * n):
                R = tuple(tuple(bits[i * n + j] for j in range(n)) for i in range(n))
                preds = all_closed_preds(V, R)
                for q in rgs(n):
                    m = max(q) + 2                  # one unused report (empty fibre)
                    qq = tuple(v if v == 0 else v + 1 for v in q)  # gap at report 1
                    conds = cg3_conditions(V, R, qq, m + 1, preds)
                    self.assertEqual(len(set(conds)), 1, (R, qq, conds))


class S02_CG7_CensusAndSandwich(unittest.TestCase):
    """S-2 (census reproduced) and S-3 (receipt for 'both outer links strict')."""

    @staticmethod
    def _bool_flags(n, E, q):
        V = bool_q()
        m = max(q) + 1
        R = tuple(tuple(int((u, v) in E) for v in range(n)) for u in range(n))
        Rs = kstar(V, R)
        Q, QA = q_may(V, R, q, m), q_must(V, R, q, m)
        Qs, QAs = kstar(V, Q), kstar(V, QA)
        prof = profiles(V, Rs, q, m)
        img = range(m)
        F = fibs(q, m)
        exact = all(prof[x] == Qs[q[x]] for x in range(n))
        lump = all(Q[a] == QA[a] for a in img)
        mm = all(Qs[a] == QAs[a] for a in img)
        S = [tuple(max(prof[x][b] for x in F[a]) for b in img) for a in img]
        unp = all(S[a] == Qs[a] for a in img)
        bex = all(Qs[a][q[z]] == max(Rs[x][z] for x in F[a]) for a in img for z in range(n))
        return lump, mm, exact, unp, bex

    def test_boolean_census_2594(self):
        c = dict(models=0, mm_nl=0, ex_nmm=0, unp_nex=0, f_nb=0, b_nf=0)
        for n in (1, 2, 3):
            pairs = [(u, v) for u in range(n) for v in range(n)]
            for bits in product((0, 1), repeat=n * n):
                E = {p for p, b in zip(pairs, bits) if b}
                for q in rgs(n):
                    lump, mm, ex, unp, bex = self._bool_flags(n, E, q)
                    c["models"] += 1
                    self.assertTrue((not lump or mm) and (not mm or ex) and (not ex or unp))
                    c["mm_nl"] += mm and not lump
                    c["ex_nmm"] += ex and not mm
                    c["unp_nex"] += unp and not ex
                    c["f_nb"] += ex and not bex
                    c["b_nf"] += bex and not ex
        self.assertEqual(c, dict(models=2594, mm_nl=462, ex_nmm=384, unp_nex=384,
                                 f_nb=240, b_nf=240))

    def test_sandwich_rel2_nonsurjective(self):
        V = rel2_q()
        rng = random.Random(7)
        for _ in range(60):
            n = rng.choice((3, 4))
            R = rand_rel(V, n, rng, 0.45)
            q = tuple(rng.choice((0, 2, 3)) for _ in range(n))
            m = 4
            Rs = kstar(V, R)
            Qs, QAs = kstar(V, q_may(V, R, q, m)), kstar(V, q_must(V, R, q, m))
            prof = profiles(V, Rs, q, m)
            F = fibs(q, m)
            for x in range(n):
                a = q[x]
                for b in range(m):
                    M = V.meet(prof[y][b] for y in F[a])
                    S = V.join(prof[y][b] for y in F[a])
                    chain = (QAs[a][b], M, prof[x][b], S, Qs[a][b])
                    self.assertTrue(all(V.leq(u, w) for u, w in zip(chain, chain[1:])), chain)

    def test_S3_cited_receipt_does_not_witness_outer_links_but_tropical_one_does(self):
        V = sat_trop(3)

        def chain(n, edges, q, x, b):
            R = [[INF] * n for _ in range(n)]
            for (u, v), w in edges.items():
                R[u][v] = w
            R = tuple(map(tuple, R))
            m = max(q) + 1
            Rs = kstar(V, R)
            Qs, QAs = kstar(V, q_may(V, R, q, m)), kstar(V, q_must(V, R, q, m))
            prof = profiles(V, Rs, q, m)
            F = fibs(q, m)
            M = V.meet(prof[y][b] for y in F[q[x]])
            S = V.join(prof[y][b] for y in F[q[x]])
            return (QAs[q[x]][b], M, prof[x][b], S, Qs[q[x]][b])
        # The report's receipt "(inf, 2, 1)": outer links Q_forall* <= M and S <= Q_exists*
        # are EQUALITIES there (only the middle links are strict).
        cited = chain(4, {(0, 3): 2, (1, 3): 1}, (0, 0, 0, 1), 0, 1)
        self.assertEqual(cited, (INF, INF, 2, 1, 1))
        # Referee receipt: ALL FOUR links strict at one (x, b) = (5, B).
        # A = {0,1,5}, C = {2,3}, B = {4}; 0->4 (1), 5->4 (2), 1->5 (1), 0->2 (0), 3->4 (0).
        q = (0, 0, 1, 1, 2, 0)
        mine = chain(6, {(0, 4): 1, (5, 4): 2, (1, 5): 1, (0, 2): 0, (3, 4): 0}, q, 5, 2)
        self.assertEqual(mine, (INF, 3, 2, 1, 0))

    def test_S3_boolean_can_never_have_both_outer_links_strict(self):
        # Q_forall* < M <= S < Q_exists* needs three distinct values; exhaustive check anyway.
        V = bool_q()
        for n in (1, 2, 3):
            for bits in product((0, 1), repeat=n * n):
                R = tuple(tuple(bits[i * n + j] for j in range(n)) for i in range(n))
                Rs = kstar(V, R)
                for q in rgs(n):
                    m = max(q) + 1
                    Qs, QAs = kstar(V, q_may(V, R, q, m)), kstar(V, q_must(V, R, q, m))
                    prof = profiles(V, Rs, q, m)
                    F = fibs(q, m)
                    for a in range(m):
                        for b in range(m):
                            M = min(prof[y][b] for y in F[a])
                            S = max(prof[y][b] for y in F[a])
                            self.assertFalse(QAs[a][b] < M and S < Qs[a][b])


class S04_CG8_RightBeckChevalley(unittest.TestCase):
    """S-4: right BC = q_* preserves closedness = Q_exists(R) <= Q_back(R*) = backward
    exactness, checked with NON-surjective q over Boolean (exhaustive) and Rel(2)."""

    def _three(self, V, R, q, m, preds):
        n = len(R)
        Rs = kstar(V, R)
        Q = q_may(V, R, q, m)
        Qs = kstar(V, Q)
        F = fibs(q, m)
        i = all(closed(V, Q, push_all(V, p, q, m)) for p in preds)
        ii = rel_leq(V, Q, q_back(V, Rs, q, m))
        iii = all(Qs[a][q[z]] == V.join(Rs[x][z] for x in F[a]) for a in range(m) for z in range(n))
        return i, ii, iii

    def test_boolean_exhaustive_nonsurjective(self):
        V = bool_q()
        for n in (1, 2, 3):
            for bits in product((0, 1), repeat=n * n):
                R = tuple(tuple(bits[i * n + j] for j in range(n)) for i in range(n))
                preds = all_closed_preds(V, R)
                for q in rgs(n):
                    qq = tuple(2 * v for v in q)            # odd reports have empty fibres
                    r = self._three(V, R, qq, 2 * max(q) + 2, preds)
                    self.assertEqual(len(set(r)), 1, (R, qq, r))

    def test_rel2_random(self):
        V = rel2_q()
        rng = random.Random(99)
        seen = set()
        for _ in range(10):
            R = rand_rel(V, 3, rng, 0.5)
            preds = all_closed_preds(V, R)
            for q, m in (((0, 0, 1), 2), ((0, 1, 1), 3), ((2, 0, 0), 3)):
                r = self._three(V, R, q, m, preds)
                self.assertEqual(len(set(r)), 1)
                seen.add(r[0])
        self.assertEqual(seen, {True, False})

    def test_adjunctions_and_residual_side_noncommutative(self):
        """CG-8(1),(3),(4): Int_R uses the RIGHT residual c/b; the left-residual variant is
        refuted in Rel(2).  L = Cl_Q q_! is left adjoint to q^*|; counit = psi on image."""
        V = rel2_q()
        rdiv = lambda c, b: V.join(a for a in V.els if V.leq(V.t(a, b), c))
        ldiv = lambda a, c: V.join(b for b in V.els if V.leq(V.t(a, b), c))
        rng = random.Random(55)
        wrong_side_failures = 0
        for _ in range(12):
            R = rand_rel(V, 2, rng, 0.8)
            Rs = kstar(V, R)
            preds = list(product(V.els, repeat=2))
            cl = [p for p in preds if closed(V, R, p)]
            for phi in preds:
                Int = tuple(V.meet(rdiv(phi[v], Rs[u][v]) for v in range(2)) for u in range(2))
                self.assertTrue(closed(V, R, Int))
                self.assertTrue(all(V.leq(a, b) for a, b in zip(Int, phi)))
                for psi in cl:
                    le = all(V.leq(a, b) for a, b in zip(psi, phi))
                    self.assertEqual(le, all(V.leq(a, b) for a, b in zip(psi, Int)))
                bad = tuple(V.meet(ldiv(Rs[u][v], phi[v]) for v in range(2)) for u in range(2))
                ok = closed(V, R, bad) and all(V.leq(a, b) for a, b in zip(bad, phi)) and all(
                    all(V.leq(a, b) for a, b in zip(psi, bad)) == all(V.leq(a, b) for a, b in zip(psi, phi))
                    for psi in cl)
                wrong_side_failures += not ok
        self.assertGreater(wrong_side_failures, 0)
        q, m = (0, 0, 1), 3                      # report 2 has an empty fibre
        for _ in range(6):
            R = rand_rel(V, 3, rng, 0.5)
            Q = q_may(V, R, q, m)
            Qs = kstar(V, Q)
            clR = all_closed_preds(V, R)
            clQ = all_closed_preds(V, Q)
            L = lambda phi: tuple(V.join(V.t(push(V, phi, q, m)[a], Qs[a][b]) for a in range(m))
                                  for b in range(m))
            for _k in range(150):
                phi, psi = rng.choice(clR), rng.choice(clQ)
                lhs = all(V.leq(a, b) for a, b in zip(L(phi), psi))
                rhs = all(V.leq(phi[x], psi[q[x]]) for x in range(3))
                self.assertEqual(lhs, rhs)
            for psi in clQ[:200]:
                self.assertEqual(L(tuple(psi[q[x]] for x in range(3))),
                                 (psi[0], psi[1], V.bottom))

    def test_q_lower_star_pairing_receipt(self):
        V = bool_q()
        R = ((0, 0, 1), (0, 0, 0), (0, 0, 0))     # 0 -> 2
        q, phi = (0, 1, 1), (1, 0, 1)
        self.assertTrue(closed(V, R, phi))
        star = push_all(V, phi, q, 2)
        self.assertEqual(star, (1, 0))
        self.assertFalse(closed(V, q_must(V, R, q, 2), star))
        self.assertTrue(closed(V, q_back(V, R, q, 2), star))


def p_join(p, r):
    n = len(p)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for lab in (p, r):
        first = {}
        for x in range(n):
            if lab[x] in first:
                parent[find(x)] = find(first[lab[x]])
            else:
                first[lab[x]] = x
    return norm(tuple(find(x) for x in range(n)))


def norm(lab):
    idx = {}
    return tuple(idx.setdefault(v, len(idx)) for v in lab)


def p_meet(p, r):
    return norm(tuple(zip(p, r)))


def p_refines(p, r):        # p finer than r
    return all(r[x] == r[y] for x in range(len(p)) for y in range(len(p)) if p[x] == p[y])


def exact_partition(V, Rs, lab):
    m = max(lab) + 1
    prof = profiles(V, Rs, lab, m)
    return all(prof[x] == prof[y] for x in range(len(lab)) for y in range(len(lab))
               if lab[x] == lab[y])


def my_coarsest(V, Rs, q):
    P = norm(q)
    while True:
        prof = profiles(V, Rs, P, max(P) + 1)
        P2 = norm(tuple(zip(P, prof)))
        if P2 == P:
            return P
        P = P2


class S05_CG10_JoinClosure(unittest.TestCase):
    """S-5: CG-10 join closure / unique coarsest exact refinement SURVIVES on four states
    over Rel(2) and P(left-zero); meet and selected-start receipts reproduced."""

    def test_join_closure_weighted_noncommutative_four_states(self):
        parts = rgs(4)
        for V, seed in ((rel2_q(), 5), (leftzero_q(), 6)):
            rng = random.Random(seed)
            nontrivial = 0
            for _ in range(25):
                R = rand_rel(V, 4, rng, 0.4)
                Rs = kstar(V, R)
                ex = [p for p in parts if exact_partition(V, Rs, p)]
                self.assertIn((0, 1, 2, 3), ex)
                exs = set(ex)
                for p, r in combinations(ex, 2):
                    self.assertIn(p_join(p, r), exs)
                for q in parts:
                    below = [p for p in ex if p_refines(p, q)]
                    top = below[0]
                    for p in below[1:]:
                        top = p_join(top, p)
                    self.assertTrue(all(p_refines(p, top) for p in below))
                    self.assertEqual(my_coarsest(V, Rs, q), top)
                nontrivial += len(ex) > 2
            self.assertGreater(nontrivial, 0)

    def test_meet_failure_and_selected_start_receipts(self):
        V = bool_q()
        E = {(0, 0), (0, 3), (1, 0), (1, 2), (2, 3), (3, 0)}
        R = tuple(tuple(int((u, v) in E) for v in range(4)) for u in range(4))
        Rs = kstar(V, R)
        p, r = (0, 0, 0, 1), (0, 0, 1, 1)
        self.assertTrue(exact_partition(V, Rs, p) and exact_partition(V, Rs, r))
        self.assertFalse(exact_partition(V, Rs, p_meet(p, r)))
        # selected start 0
        E = {(2, 0), (2, 1), (3, 0)}
        R = tuple(tuple(int((u, v) in E) for v in range(4)) for u in range(4))
        Rs = kstar(V, R)

        def sel(lab):
            m = max(lab) + 1
            return profiles(V, Rs, lab, m)[0] == kstar(V, q_may(V, R, lab, m))[lab[0]]
        a, b = (0, 1, 2, 0), (0, 1, 2, 2)
        self.assertTrue(sel(a) and sel(b))
        self.assertFalse(sel(p_join(a, b)))

    def test_no_meet_failure_possible_below_four_states_any_quantale(self):
        # Structural: on <= 3 points two exact partitions are comparable or meet to discrete.
        for n in (1, 2, 3):
            parts = rgs(n)
            for p, r in product(parts, repeat=2):
                mt = p_meet(p, r)
                self.assertTrue(mt in (norm(p), norm(r)) or max(mt) == n - 1)


class S06_CG5_BaseChange(unittest.TestCase):
    """S-6: CG-5 receipts and strictness on the finite truncations (own tables)."""

    @staticmethod
    def kind(V, W, h):
        e = V.els
        joins = all(h(V.join2(a, b)) == W.join2(h(a), h(b)) for a in e for b in e) \
            and h(V.bottom) == W.bottom
        strict = all(h(V.t(a, b)) == W.t(h(a), h(b)) for a in e for b in e) and h(V.unit) == W.unit
        oplax = all(W.leq(h(V.t(a, b)), W.t(h(a), h(b))) for a in e for b in e) \
            and W.leq(h(V.unit), W.unit)
        lax = all(W.leq(W.t(h(a), h(b)), h(V.t(a, b))) for a in e for b in e) \
            and W.leq(W.unit, h(V.unit))
        return joins, strict, oplax, lax

    def test_language_cost_bool_strict_on_truncations(self):
        words = ["", "x", "y", "xx", "xy", "yx", "yy", "#"]
        idx = {w: i for i, w in enumerate(words)}

        def mult(u, v):
            if "#" in (u, v) or len(u) + len(v) > 2:
                return "#"
            return u + v
        tab = [[idx[mult(u, v)] for v in words] for u in words]

        def lt(A, B):
            r = 0
            for i in range(8):
                if A >> i & 1:
                    for j in range(8):
                        if B >> j & 1:
                            r |= 1 << tab[i][j]
            return r
        L = FQ("lang", range(256), lambda a, b: a & ~b == 0, lambda a, b: a | b,
               lambda a, b: a & b, lt, 1, 0, 255)
        S3 = sat_trop(3)

        def length(A):
            if A == 0:
                return INF
            return min(3 if words[i] == "#" else len(words[i]) for i in range(8) if A >> i & 1)
        self.assertEqual(self.kind(L, S3, length)[:2], (True, True))
        B = bool_q()
        fin = lambda a: int(a != INF)
        self.assertEqual(self.kind(S3, B, fin)[:2], (True, True))
        jb, sb, ob, lb = self.kind(budget_trop(3), B, fin)
        self.assertTrue(jb and ob and not sb and not lb)          # budget -> Bool only oplax
        # a SATURATING target is needed: sending # to the BUDGET quantale breaks strictness
        T3 = budget_trop(3)
        self.assertFalse(self.kind(L, T3, length)[1])

    def test_oplax_half_receipt_and_lax_receipts(self):
        T3 = budget_trop(3)
        half = lambda a: INF if a == INF else a // 2
        j, s, o, l = self.kind(T3, T3, half)
        self.assertTrue(j and o and not s)

        def trop_rel(n, edges):
            R = [[INF] * n for _ in range(n)]
            for (u, v), w in edges.items():
                R[u][v] = w
            return tuple(map(tuple, R))

        def exact_at(V, R, q, x):
            m = max(q) + 1
            return profiles(V, kstar(V, R), q, m)[x] == kstar(V, q_may(V, R, q, m))[q[x]]
        R = trop_rel(4, {(0, 1): 1, (0, 3): 2, (2, 3): 1})
        q = (0, 1, 1, 2)
        hR = tuple(tuple(half(v) for v in r) for r in R)
        self.assertTrue(exact_at(T3, R, q, 0))
        self.assertFalse(exact_at(T3, R, q, 1))          # the non-exact reachable state
        self.assertFalse(exact_at(T3, hR, q, 0))
        # 5a: Bool -> P(Z/2), 1 |-> {0,1}: tensor strict, unit lax
        B, Z2 = bool_q(), pz2_q()
        top = lambda a: 3 if a else 0
        j, s, o, l = self.kind(B, Z2, top)
        self.assertTrue(j and l and not s)
        allx = lambda V, R, q: all(exact_at(V, R, q, x) for x in range(len(q)))
        R = ((0, 0), (0, 1))
        self.assertTrue(allx(B, R, (0, 0)))
        self.assertFalse(allx(Z2, tuple(tuple(top(v) for v in r) for r in R), (0, 0)))
        # 5b: P(Z/2) -> Bool, A |-> [0 in A]: strict unit, strict joins, lax tensor
        even = lambda A: A & 1
        j, s, o, l = self.kind(Z2, B, even)
        self.assertTrue(j and l and not s and even(Z2.unit) == B.unit)
        R = ((0, 0, 0), (0, 0, 0b10), (0b01, 0, 0b10))
        self.assertTrue(allx(Z2, R, (0, 1, 1)))
        self.assertFalse(allx(B, tuple(tuple(even(v) for v in r) for r in R), (0, 1, 1)))

    def test_oplax_transports_all_start_random(self):
        T3, B = budget_trop(3), bool_q()
        rng = random.Random(31)
        maps = ((T3, lambda a: INF if a == INF else a // 2),
                (B, lambda a: int(a != INF and a <= 1)))
        for W, h in maps:
            for _ in range(150):
                R = rand_rel(T3, 3, rng, 0.6)
                hR = tuple(tuple(h(v) for v in r) for r in R)
                for q in rgs(3):
                    m = max(q) + 1
                    if all(p == kstar(T3, q_may(T3, R, q, m))[q[x]]
                           for x, p in enumerate(profiles(T3, kstar(T3, R), q, m))):
                        Qs = kstar(W, q_may(W, hR, q, m))
                        self.assertTrue(all(p == Qs[q[x]] for x, p in
                                            enumerate(profiles(W, kstar(W, hR), q, m))))


class S07_CG6_GradedTheorem(unittest.TestCase):
    """S-7: graded theorem holds on truncated language quantales (deg must be valued in
    N u {inf}: no N-valued monoid degree exists on Sigma^{<=L} + #)."""

    def test_no_nat_valued_degree_on_truncated_monoid(self):
        # deg(#.x) = deg(#) forces deg(x) = 0 for x = 'x', contradicting deg('x') = 1.
        # Exhibited as arithmetic: for every candidate deg(#) in 0..50, deg(#)+1 != deg(#).
        self.assertTrue(all(d + 1 != d for d in range(51)))

    def test_letter_valued_exact_iff_one_step_lumpable(self):
        rng = random.Random(4)
        for Lmax in (2, 3):
            def mult(u, v):
                if "#" in (u, v) or len(u) + len(v) > Lmax:
                    return "#"
                return u + v
            V = FQ("lang", (), lambda a, b: a <= b, lambda a, b: a | b, lambda a, b: a & b,
                   lambda A, B: frozenset(mult(u, v) for u in A for v in B),
                   frozenset({""}), frozenset(), None)
            letters = (frozenset(), frozenset({"x"}), frozenset({"y"}), frozenset({"x", "y"}))
            both = set()
            for _ in range(70):
                n = rng.choice((3, 4))
                R = tuple(tuple(rng.choice(letters) if rng.random() < 0.5 else frozenset()
                                for _ in range(n)) for _ in range(n))
                Rs = kstar(V, R)
                for q in (tuple(rng.randrange(2) for _ in range(n)),
                          tuple(rng.randrange(3) for _ in range(n))):
                    q = norm(q)
                    m = max(q) + 1
                    prof = profiles(V, Rs, q, m)
                    exact = all(prof[x] == kstar(V, q_may(V, R, q, m))[q[x]] for x in range(n))
                    one = [tuple(V.join(R[x][z] for z in range(n) if q[z] == b) for b in range(m))
                           for x in range(n)]
                    lump = all(one[x] == one[y] for x in range(n) for y in range(n) if q[x] == q[y])
                    self.assertEqual(exact, lump)
                    both.add(exact)
            self.assertEqual(both, {True, False})


class S08_CG12_WholeDistance(unittest.TestCase):
    """S-8: whole-distance preservation <=> ker q within V-isomorphism (Rel(2), tropical)."""

    def test_random(self):
        for V, seed in ((rel2_q(), 2), (sat_trop(3), 3)):
            rng = random.Random(seed)
            seen = set()
            for _ in range(60):
                n = rng.choice((3, 4))
                R = rand_rel(V, n, rng, 0.5)
                Rs = kstar(V, R)
                q = norm(tuple(rng.randrange(n) for _ in range(n)))
                m = max(q) + 1
                Qs = kstar(V, q_may(V, R, q, m))
                whole = all(Rs[x][z] == Qs[q[x]][q[z]] for x in range(n) for z in range(n))
                iso = all(V.leq(V.unit, Rs[x][y]) and V.leq(V.unit, Rs[y][x])
                          for x in range(n) for y in range(n) if q[x] == q[y])
                self.assertEqual(whole, iso)
                seen.add(whole)
            self.assertEqual(seen, {True, False})


class S09_CG13_SignedInventDelete(unittest.TestCase):
    """S-9: REFUTES the scoped observation 'none [invent+delete] on 3 states at tau = 1'
    (CG-13(4)).  Three states, weights in {-1,0,1}, one step suffice."""

    @staticmethod
    def both(A, q, m, x):
        n = len(q)
        size = [sum(1 for u in range(n) if q[u] == a) for a in range(m)]
        src = [sum((A[z][x] for z in range(n) if q[z] == b), Fr(0)) for b in range(m)]
        Abar = [[sum((A[z][u] for u in range(n) for z in range(n) if q[u] == a and q[z] == b),
                     Fr(0)) / size[a] for a in range(m)] for b in range(m)]
        quo = [Abar[b][q[x]] for b in range(m)]
        deleted = [b for b in range(m) if src[b] != 0 and quo[b] == 0]
        invented = [b for b in range(m) if src[b] == 0 and quo[b] != 0]
        return src, quo, deleted, invented

    def test_three_state_one_step_receipts(self):
        # (i) with self-loops: x->x (1), x'->x' (-1), x'->z (1); q = (A, A, B)
        A = [[Fr(0)] * 3 for _ in range(3)]
        A[0][0], A[1][1], A[2][1] = Fr(1), Fr(-1), Fr(1)       # A[y][x] = weight x -> y
        src, quo, dl, inv = self.both(A, (0, 0, 1), 2, 0)
        self.assertEqual((src, quo), ([1, 0], [0, Fr(1, 2)]))
        self.assertEqual((dl, inv), ([0], [1]))
        # (ii) loop-free: x->x' (1), x'->x (-1), x'->z (1)
        A = [[Fr(0)] * 3 for _ in range(3)]
        A[1][0], A[0][1], A[2][1] = Fr(1), Fr(-1), Fr(1)
        src, quo, dl, inv = self.both(A, (0, 0, 1), 2, 0)
        self.assertEqual((dl, inv), ([0], [1]))

    def test_exhaustive_three_state_one_step_count(self):
        hits = 0
        for vs in product((-1, 0, 1), repeat=9):
            A = [[Fr(vs[3 * i + j]) for j in range(3)] for i in range(3)]
            for q in ((0, 0, 1), (0, 1, 1), (0, 1, 0)):
                for x in range(3):
                    _, _, dl, inv = self.both(A, q, 2, x)
                    hits += bool(dl and inv)
        self.assertGreater(hits, 0)
        # two states can never do both (at most one report is non-trivial)
        for vs in product((-1, 0, 1), repeat=4):
            A = [[Fr(vs[2 * i + j]) for j in range(2)] for i in range(2)]
            for x in range(2):
                _, _, dl, inv = self.both(A, (0, 0), 1, x)
                self.assertFalse(dl and inv)

    def test_resolvent_lumpability_wider_entries(self):
        """CG-13(6) SURVIVES on entries {-2..2}, n = 3 (sample) and n = 4 (sample)."""
        def inv(M):
            n = len(M)
            W = [[Fr(v) for v in row] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
            for c in range(n):
                p = next((r for r in range(c, n) if W[r][c] != 0), None)
                if p is None:
                    return None
                W[c], W[p] = W[p], W[c]
                pv = W[c][c]
                W[c] = [v / pv for v in W[c]]
                for r in range(n):
                    if r != c and W[r][c] != 0:
                        f = W[r][c]
                        W[r] = [a - f * b for a, b in zip(W[r], W[c])]
            return [row[n:] for row in W]

        def lump(A, q):
            n, m = len(q), max(q) + 1
            cols = [tuple(sum((A[z][x] for z in range(n) if q[z] == b), Fr(0)) for b in range(m))
                    for x in range(n)]
            return all(cols[x] == cols[y] for x in range(n) for y in range(n) if q[x] == q[y])
        rng = random.Random(13)
        yes = 0
        for _ in range(400):
            n = rng.choice((3, 4))
            q = norm(tuple(rng.randrange(2) for _ in range(n)))
            A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
            if rng.random() < 0.5:             # force lumpability half the time
                F = fibs(q, max(q) + 1)
                for fb in F:
                    for blk in F:
                        x0 = blk[0]
                        for x in blk[1:]:
                            d = sum(A[z][x0] for z in fb) - sum(A[z][x] for z in fb)
                            A[fb[0]][x] += d
            N = inv([[Fr(int(i == j)) - A[i][j] for j in range(n)] for i in range(n)])
            if N is None:
                continue
            self.assertEqual(lump(N, q), lump(A, q))
            yes += lump(A, q)
        self.assertGreater(yes, 20)

    def test_sign_balance_global_sign(self):
        rng = random.Random(17)
        for _ in range(150):
            n = rng.choice((2, 3, 4))
            d = [rng.choice((1, -1)) for _ in range(n)]
            eps = rng.choice((1, -1))
            Bm = [[rng.choice((0, 0, 1, 2)) for _ in range(n)] for _ in range(n)]
            A = [[eps * d[i] * Bm[i][j] * d[j] for j in range(n)] for i in range(n)]
            P = [[int(i == j) for j in range(n)] for i in range(n)]
            W = [[i == j for j in range(n)] for i in range(n)]
            for _t in range(4):
                P = [[sum(A[i][k] * P[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
                W = [[any(Bm[i][k] and W[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
                for i in range(n):
                    for j in range(n):
                        self.assertEqual(P[i][j] != 0, W[i][j])


class S10_CG1_BackwardForm(unittest.TestCase):
    """S-10: CG-1(a'') backward form, reported 'proved by symmetry only; not separately
    tested', SURVIVES an exhaustive noncommutative check (P(left-zero), n = 2) and Rel(2)."""

    def test_backward_hereditary_meet(self):
        for V, rels in ((leftzero_q(), None), (rel2_q(), 120)):
            n = 2
            if rels is None:
                Rlist = [((a, b), (c, d)) for a, b, c, d in product(V.els, repeat=4)]
            else:
                rng = random.Random(41)
                Rlist = [rand_rel(V, n, rng, 0.7) for _ in range(rels)]
            preds = list(product(V.els, repeat=n))
            for R in Rlist:
                Rs = kstar(V, R)
                back = [psi for psi in preds
                        if all(V.leq(V.t(R[u][v], psi[v]), psi[u]) for u in range(n) for v in range(n))]
                for x in range(n):
                    for z in range(n):
                        val = V.meet(psi[x] for psi in back if V.leq(V.unit, psi[z]))
                        self.assertEqual(val, Rs[x][z])


# ===========================================================================
# Part B. Finite Observer (FO)
# ===========================================================================

def classes(n, R, T):
    lab = [0] * n
    while True:
        sig = [tuple(R[a][x] for a in range(len(R))) + tuple(lab[T[a][x]] for a in range(len(T)))
               for x in range(n)]
        idx = {}
        new = [idx.setdefault(s, len(idx)) for s in sig]
        if len(set(new)) == len(set(lab)):
            return new
        lab = new


def canon_core(n, R, T, start=0):
    cl = classes(n, R, T)
    p = len(R)
    order, reps, i = {cl[start]: 0}, [start], 0
    while i < len(reps):
        x = reps[i]
        i += 1
        for a in range(p):
            y = T[a][x]
            if cl[y] not in order:
                order[cl[y]] = len(order)
                reps.append(y)
    return tuple((tuple(R[a][x] for a in range(p)), tuple(order[cl[T[a][x]]] for a in range(p)))
                 for x in reps)


def all_carriers(n, p):
    cells = list(product((0, 1), range(n)))
    for ch in product(cells, repeat=n * p):
        yield ([[ch[a * n + x][0] for x in range(n)] for a in range(p)],
               [[ch[a * n + x][1] for x in range(n)] for a in range(p)])


def run_word(core, word):
    s, out = 0, []
    for a in word:
        out.append(core[s][0][a])
        s = core[s][1][a]
    return tuple(out)


def win_depth(n, R, T, S, labels):
    """Belief game on ORIGINAL states, with NO fusion pruning (independent of FO-10's
    fused-is-lost lemma).  Returns the optimal worst-case depth or None."""
    p = len(R)
    init = frozenset((labels[x], x) for x in S)
    seen, order, moves, i = {init}, [init], {}, 0
    while i < len(order):
        B = order[i]
        i += 1
        if len({l for l, _ in B}) == 1:
            moves[B] = None
            continue
        opts = []
        for a in range(p):
            kids = {}
            for l, x in B:
                kids.setdefault(R[a][x], set()).add((l, T[a][x]))
            kk = [frozenset(v) for v in kids.values()]
            opts.append(kk)
            for k in kk:
                if k not in seen:
                    seen.add(k)
                    order.append(k)
        moves[B] = opts
    rank = {B: 0 for B in order if moves[B] is None}
    r = 0
    while True:
        r += 1
        new = [B for B in order if B not in rank and any(all(k in rank for k in kk) for kk in moves[B])]
        if not new:
            return rank.get(init)
        for B in new:
            rank[B] = r


class S11_FO2_CoresAndSharpness(unittest.TestCase):
    """S-11: FO-2 core counts (48, 11 500), n+m-1 bound and n+m-2 sharpness re-derived."""

    def test_core_counts(self):
        for p, nmax, expect in ((1, 4, 48), (2, 3, 11500)):
            cores = set()
            for n in range(1, nmax + 1):
                for R, T in all_carriers(n, p):
                    cores.add(canon_core(n, R, T))
            self.assertEqual(len(cores), expect)

    def test_bound_and_sharpness_two_instruments_exhaustive(self):
        for p, nmax in ((1, 4), (2, 3)):
            cores = set()
            for n in range(1, nmax + 1):
                for R, T in all_carriers(n, p):
                    cores.add(canon_core(n, R, T))
            cores = sorted(cores)
            Lmax = 2 * nmax - 1
            wl = [w for L in range(1, Lmax + 1) for w in product(range(p), repeat=L)]
            # response of word w = output at its last letter (prefix outputs come from prefixes)
            vec = {c: tuple(run_word(c, w)[-1] for w in wl) for c in cores}
            best = {}
            for L in range(0, Lmax + 1):
                cut = sum(p ** i for i in range(1, L + 1))
                groups = {}
                for c in cores:
                    groups.setdefault(vec[c][:cut], []).append(len(c))
                for sizes in groups.values():
                    if len(sizes) < 2:
                        continue
                    s = sorted(sizes)
                    self.assertGreaterEqual(s[0] + s[1] - 1, L + 1)     # disagree by n+m-1
                    for a, b in combinations(s, 2):
                        best[(a, b)] = max(best.get((a, b), -1), L)
            for n in range(1, nmax + 1):
                for m in range(n, nmax + 1):
                    self.assertEqual(best[(n, m)], n + m - 2)

    def test_sharp_family_own_construction(self):
        def cycle_chain(n, m):
            # cycle of p states emits d iff k = q-1 (mod p); chain of q states.
            def build(p, q):
                cyc = [(1 if (k + 1) % p == (q - 1) % p else 0) for k in range(p)]
                ch = [(1 if (k + 1) % p == (q - 1) % p else 0) for k in range(q - 1)] + [0]
                cR = [[cyc[k] for k in range(p)]]
                cT = [[(k + 1) % p for k in range(p)]]
                hR = [ch]
                hT = [[min(k + 1, q - 1) for k in range(q)]]
                return (p, cR, cT), (q, hR, hT)
            if n == 1 and m == 1:
                return (1, [[0]], [[0]]), (1, [[1]], [[0]])
            if n >= 2:
                return build(n, m)
            b, a = build(m, n)
            return a, b
        for n in range(1, 7):
            for m in range(1, 7):
                (n1, R1, T1), (n2, R2, T2) = cycle_chain(n, m)
                k1, k2 = canon_core(n1, R1, T1), canon_core(n2, R2, T2)
                self.assertEqual((len(k1), len(k2)), (n, m))
                w = (0,) * (n + m + 3)
                o1, o2 = run_word(k1, w), run_word(k2, w)
                agree = next(i for i in range(len(w)) if o1[i] != o2[i])
                self.assertEqual(agree, n + m - 2)


class S12_FO3_Exposure(unittest.TestCase):
    """S-12: FO-3 pure-intervention exposure: receipt and 2-state impossibility (own code)."""

    def test_receipt_and_minimality(self):
        R = [[0, 0, 1], [0, 0, 0]]
        T = [[0, 1, 2], [0, 2, 2]]
        self.assertEqual(classes(3, [R[0]], [T[0]])[0], classes(3, [R[0]], [T[0]])[1])
        full = classes(3, R, T)
        self.assertNotEqual(full[0], full[1])
        for Rr, Tt in all_carriers(2, 2):
            if len(set(Rr[1])) != 1:
                continue
            A = classes(2, [Rr[0]], [Tt[0]])
            if A[0] == A[1]:
                F = classes(2, Rr, Tt)
                self.assertEqual(F[0], F[1])


def mobius(f, k, c0, mod=None):
    out = []
    for S in range(1 << k):
        s = 0
        T = S
        while True:
            s += (-1) ** (bin(S).count("1") - bin(T).count("1")) * f[c0 ^ T]
            if T == 0:
                break
            T = (T - 1) & S
        out.append(s % mod if mod else s)
    return out


def horizon(f, k, c0, j, mod=None):
    co = mobius(f, k, c0, mod)
    hs = [bin(S).count("1") for S in range(1 << k) if S >> j & 1 and co[S]]
    return min(hs) if hs else None


class S13_FO4_FO5_Horizons(unittest.TestCase):
    """S-13: FO-4/FO-5 survive; NAND receipt and the 192/720 count reproduced."""

    def test_nand_receipt_and_count(self):
        f = [((x >> 2) & 1) * (1 - ((x & 1) & (x >> 1 & 1))) for x in range(8)]
        co0 = mobius(f, 3, 0, 2)
        self.assertEqual([S for S in range(8) if co0[S]], [4, 7])
        self.assertEqual([horizon(f, 3, c, 2, 2) for c in range(8)], [1, 1, 1, 2, 1, 1, 1, 2])
        strict = ess = 0
        for g in product((0, 1), repeat=8):
            co = mobius(g, 3, 0, 2)
            for j in range(3):
                if all(g[x] == g[x ^ (1 << j)] for x in range(8)):
                    continue
                ess += 1
                dj = max(bin(S).count("1") for S in range(8) if S >> j & 1 and co[S])
                if max(horizon(g, 3, c, j, 2) for c in range(8)) < dj:
                    strict += 1
        self.assertEqual((strict, ess), (192, 720))

    def test_transport_formula_signs_integer(self):
        rng = random.Random(23)
        for _ in range(200):
            k = rng.randrange(1, 6)
            f = [rng.randrange(-6, 7) for _ in range(1 << k)]
            b, c0 = rng.randrange(1 << k), rng.randrange(1 << k)
            C = b ^ c0
            ab, ac = mobius(f, k, b), mobius(f, k, c0)
            for Vs in range(1 << k):
                tot = 0
                for S in range(1 << k):
                    if S & Vs == Vs and S & ~(Vs | C) == 0:
                        tot += ab[S]
                self.assertEqual(ac[Vs], (-1) ** bin(Vs & C).count("1") * tot)

    def test_horizon_equals_ball_and_extension_exists(self):
        for mod, k in ((2, 3), (4, 2)):
            for f in product(range(mod), repeat=1 << k):
                for c0 in range(1 << k):
                    for j in range(k):
                        h = horizon(f, k, c0, j, mod)
                        ball = None
                        for r in range(k + 1):
                            pts = [x for x in range(1 << k) if bin(x ^ c0).count("1") <= r]
                            if any(f[x] != f[x ^ (1 << j)] for x in pts if x ^ (1 << j) in pts):
                                ball = r
                                break
                        self.assertEqual(h, ball)


class S14_FO6_CertificationCost(unittest.TestCase):
    """S-14: FO-6 exact cost 2*sum_{i<d} C(k-1,i) SURVIVES: independent GF(2) kernel test
    (k <= 4) and full brute force over the NON-field group Z/4 (k <= 3) and Z/6 (k <= 2)."""

    @staticmethod
    def gf2_certifies(Q, k, d, j):
        def rank(vecs):
            basis = []
            for v in vecs:
                for b in basis:
                    v = min(v, v ^ b)
                if v:
                    basis.append(v)
            return len(basis)
        mon = [S for S in range(1 << k) if bin(S).count("1") <= d]
        ind = [S for S in mon if not S >> j & 1]
        ev = lambda S: sum(1 << i for i, x in enumerate(Q) if S & ~x == 0)
        # ker on P_d equals ker on the j-free part  <=>  certification
        return len(mon) - rank([ev(S) for S in mon]) == len(ind) - rank([ev(S) for S in ind])

    def test_gf2_k_le_4(self):
        for k in range(1, 5):
            for d in range(0, k + 1):
                for j in {0, k - 1}:
                    cost = 2 * sum(comb(k - 1, i) for i in range(d))
                    pair = [x for x in range(1 << k) if bin(x & ~(1 << j)).count("1") <= d - 1]
                    self.assertEqual(len(pair), cost)
                    self.assertTrue(self.gf2_certifies(pair, k, d, j))
                    if cost:
                        for Q in combinations(range(1 << k), cost - 1):
                            self.assertFalse(self.gf2_certifies(Q, k, d, j))

    def test_nonfield_groups_full_minimum(self):
        for mod, kmax in ((4, 3), (6, 2)):
            for k in range(1, kmax + 1):
                N = 1 << k
                for d in range(0, k + 1):
                    mon = [S for S in range(N) if bin(S).count("1") <= d]
                    j = 0
                    zero_masks = set()
                    for cs in product(range(mod), repeat=len(mon)):
                        h = [sum(c for c, S in zip(cs, mon) if S & ~x == 0) % mod for x in range(N)]
                        if any(h[x] != h[x ^ 1] for x in range(N)):
                            zero_masks.add(sum(1 << x for x in range(N) if h[x] == 0))
                    best = min(bin(Qm).count("1") for Qm in range(1 << N)
                               if not any(Qm & ~z == 0 for z in zero_masks))
                    self.assertEqual(best, 2 * sum(comb(k - 1, i) for i in range(d)), (mod, k, d))
                    # FO-6(3): the order-r ball at 0 certifies iff r >= d (d >= 1)
                    if d >= 1:
                        for r in range(k + 1):
                            ball = sum(1 << x for x in range(N) if bin(x).count("1") <= r)
                            ok = not any(ball & ~z == 0 for z in zero_masks)
                            self.assertEqual(ok, r >= d)


def net_eval(spec, decl, clamps):
    """spec: list of (name, values, parents, table-dict or None for roots)."""
    val = {}
    for name, vals, parents, table in spec:
        if name in clamps:
            val[name] = clamps[name]
        elif not parents:
            val[name] = decl[name]
        else:
            val[name] = table[tuple(val[p] for p in parents)]
    return val


class S15_FO9_IdentifiabilityOwnDAG(unittest.TestCase):
    """S-15: FO-9 criterion SURVIVES on a different DAG with a TERNARY root and a node
    with two root parents (joint clamping genuinely needed)."""

    def test_two_parent_ternary_class(self):
        VR, VS, VB = (0, 1, 2), (0, 1), (0, 1)
        ctx_u = list(product(VR, VS))
        nets = []
        for dr in VR:
            for ds in VS:
                for outs in product(VB, repeat=len(ctx_u)):
                    tu = dict(zip(ctx_u, outs))
                    for tv in product(VB, repeat=2):
                        tvd = {(0,): tv[0], (1,): tv[1]}
                        nets.append(({"r": dr, "s": ds},
                                     [("r", VR, (), None), ("s", VS, (), None),
                                      ("u", VB, ("r", "s"), tu), ("v", VB, ("u",), tvd)]))
        self.assertEqual(len(nets), 3 * 2 * 64 * 4)

        def graph(spec):
            g = set()
            for name, vals, parents, table in spec:
                for i, p in enumerate(parents):
                    for c in table:
                        for alt in dict(spec_vals(spec))[p]:
                            c2 = c[:i] + (alt,) + c[i + 1:]
                            if table[c] != table[c2]:
                                g.add((p, name))
            return frozenset(g)

        def spec_vals(spec):
            return [(n, v) for n, v, _, _ in spec]

        def identifies(fam):
            seen = {}
            for decl, spec in nets:
                data = tuple(tuple(net_eval(spec, decl, dict(cl))[r] for r in reads)
                             for cl, reads in fam)
                g = graph(spec)
                if seen.setdefault(data, g) != g:
                    return False
            return True

        def criterion(fam):
            for c in ctx_u:
                if not any("u" in reads and dict(cl).get("r") == c[0] and dict(cl).get("s") == c[1]
                           and "u" not in dict(cl) for cl, reads in fam):
                    return False
            for b in VB:
                if not any("v" in reads and dict(cl).get("u") == b and "v" not in dict(cl)
                           for cl, reads in fam):
                    return False
            return True

        E = lambda cl, reads: (tuple(sorted(cl.items())), tuple(reads))
        required = [E({"r": a, "s": b}, ["u"]) for a, b in ctx_u] + [E({"u": b}, ["v"]) for b in VB]
        self.assertTrue(criterion(required) and identifies(required))
        for drop in required:
            fam = [e for e in required if e != drop]
            self.assertFalse(criterion(fam))
            self.assertFalse(identifies(fam))
        # single-parent clamping (each root clamped separately, the other free) fails
        single = [E({"r": a}, ["u", "s"]) for a in VR] + [E({"s": b}, ["u", "r"]) for b in VS] \
            + [E({"u": b}, ["v"]) for b in VB]
        self.assertFalse(identifies(single))
        # observing everything without clamps fails
        self.assertFalse(identifies([E({}, ["r", "s", "u", "v"])]))
        rng = random.Random(77)
        universe = []
        for mr in ("read", "hide") + VR:
            for ms in ("read", "hide") + VS:
                for mu in ("read", "hide") + VB:
                    for mv in ("read", "hide"):
                        cl = {k: v for k, v in (("r", mr), ("s", ms), ("u", mu)) if isinstance(v, int)}
                        reads = [k for k, v in (("r", mr), ("s", ms), ("u", mu), ("v", mv)) if v == "read"]
                        universe.append(E(cl, reads))
        agree = 0
        for _ in range(40):
            fam = set(rng.sample(universe, rng.randrange(1, 10)))
            if rng.random() < 0.6:
                fam |= set(rng.sample(required, rng.randrange(5, 9)))
            fam = sorted(fam)
            c = criterion(fam)
            self.assertEqual(c, identifies(fam))
            agree += c
        self.assertGreater(agree, 0)


class S15b_FO9_SingletonValueSetBoundary(unittest.TestCase):
    """S-15 boundary: the hypothesis |V_p| >= 2 is load-bearing.  With a single-valued
    potential parent p, a family that never clamps p still identifies the class, so the
    literal 'clamp ALL of pa*(i)' condition is not necessary there."""

    def test_singleton_parent(self):
        nets = []
        for dr in (0, 1):
            for outs in product((0, 1), repeat=2):
                ti = {(0, 0): outs[0], (0, 1): outs[1]}      # context (p, r), p in {0}
                nets.append(({"p": 0, "r": dr},
                             [("p", (0,), (), None), ("r", (0, 1), (), None), ("i", (0, 1), ("p", "r"), ti)]))
        fam = [({"r": 0}, ["i"]), ({"r": 1}, ["i"])]          # p never clamped
        seen = {}
        for decl, spec in nets:
            data = tuple(tuple(net_eval(spec, decl, cl)[r] for r in reads) for cl, reads in fam)
            t = spec[2][3]
            g = frozenset({("r", "i")} if t[(0, 0)] != t[(0, 1)] else set())
            self.assertEqual(seen.setdefault(data, g), g)


class S16_FO8_Gating(unittest.TestCase):
    """S-16: FO-8 minimality claims reproduced with own evaluator."""

    def test_monotone_single_hidden_node_paths_compose(self):
        mono1 = [(0, 0), (1, 1), (0, 1)]                        # F_z(0), F_z(1)
        ctx = [(0, 0), (0, 1), (1, 0), (1, 1)]
        mono2 = [t for t in product((0, 1), repeat=4)
                 if all(t[i] <= t[j] for i in range(4) for j in range(4)
                        if ctx[i][0] <= ctx[j][0] and ctx[i][1] <= ctx[j][1])]
        self.assertEqual(len(mono2), 6)
        for fz in mono1:
            for fy in mono2:
                Fy = dict(zip(ctx, fy))
                ess_xz = fz[0] != fz[1]
                ess_zy = any(Fy[(a, 0)] != Fy[(a, 1)] for a in (0, 1))
                resp = [Fy[(x, fz[x])] for x in (0, 1)]
                if ess_xz and ess_zy:
                    self.assertNotEqual(resp[0], resp[1])

    def test_binary_chain_composes(self):
        for fz in product((0, 1), repeat=2):
            for fy in product((0, 1, 2), repeat=2):
                if fz[0] != fz[1] and fy[0] != fy[1]:
                    self.assertNotEqual(fy[fz[0]], fy[fz[1]])


class S17_FO10_FreeObservability(unittest.TestCase):
    """S-17: FO-10 census (46 916 carriers) reproduced by an independent belief game WITHOUT
    fusion pruning; receipts (A,B,C), (A,B,C,D) and depth bounds re-checked.  Also: the
    class-injective bound (s-1)(q-1) is NOT attained at q = 3 in this census (max 3 < 4)."""

    def test_census(self):
        st = dict(total=0, free=0, nd=0, inj=0, free_not_inj=0, ci=0, ci_not_free=0)
        maxd, injd = {}, {}
        for n in (1, 2, 3):
            for R, T in all_carriers(n, 2):
                st["total"] += 1
                cl = classes(n, R, T)
                q = len(set(cl))
                d = win_depth(n, R, T, range(n), cl)
                free = d is not None
                st["free"] += free
                if free:
                    maxd[q] = max(maxd.get(q, 0), d)
                    self.assertLessEqual(d, q * (q - 1) // 2)
                nd = all(cl[T[a][x]] == cl[x] for a in range(2) for x in range(n))
                rep = {}
                for x in range(n):
                    rep.setdefault(cl[x], x)
                inj = all(len({cl[T[a][rep[c]]] for c in rep}) == q for a in range(2))
                st["nd"] += nd
                st["inj"] += inj
                if nd or inj:
                    self.assertTrue(free)
                if inj:
                    self.assertLessEqual(d, (q - 1) * (q - 1))
                    injd[q] = max(injd.get(q, 0), d)
                st["free_not_inj"] += free and not inj
                ci = all(T[a][T[a][x]] == T[a][x] for a in range(2) for x in range(n)) and \
                    all(T[a][T[b][x]] == T[b][T[a][x]] for a in range(2) for b in range(2) for x in range(n))
                st["ci"] += ci
                st["ci_not_free"] += ci and not free
        self.assertEqual(st, dict(total=46916, free=42380, nd=3596, inj=6344, free_not_inj=36036,
                                  ci=3828, ci_not_free=384))
        self.assertEqual(maxd, {1: 0, 2: 1, 3: 3})
        self.assertEqual(injd, {1: 0, 2: 1, 3: 3})      # (s-1)(q-1) = 4 not attained at q = 3

    def test_receipts(self):
        # destructive A,B,C: a flags A, b flags B, both send everything to A
        R, T = [[1, 0, 0], [0, 1, 0]], [[0, 0, 0], [0, 0, 0]]
        cl = classes(3, R, T)
        self.assertEqual(len(set(cl)), 3)
        self.assertIsNone(win_depth(3, R, T, range(3), cl))
        self.assertIsNone(win_depth(3, R, T, range(3), [0, 0, 1]))       # 1[C]
        # separately-but-not-jointly: states A,B,C,D; start set {A,B,C}
        R = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]
        T = [[3, 3, 3, 3]] * 3
        cl = classes(4, R, T)
        self.assertEqual(len(set(cl)), 4)
        for bits in product((0, 1), repeat=3):
            self.assertEqual(win_depth(4, R, T, range(3), list(bits) + [0]),
                             0 if len(set(bits)) == 1 else 1)
        self.assertIsNone(win_depth(4, R, T, range(3), cl))
        # reset_and_readout (free, not class-injective); readout_swap (free, disturbing)
        R, T = [[0, 1], [0, 0]], [[0, 1], [0, 0]]
        self.assertEqual(win_depth(2, R, T, range(2), classes(2, R, T)), 1)
        R, T = [[0, 1]], [[1, 0]]
        self.assertEqual(win_depth(2, R, T, range(2), classes(2, R, T)), 1)


if __name__ == "__main__":
    unittest.main()
