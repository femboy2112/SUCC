"""Field of definition of positive carriers: the irrational-contact obstruction.

Exact-rational companion to ``carrier_realization.py`` (Part II of the
positive carrier dossier).  Everything here is about one question:

    a behavior with RATIONAL data may have a positive carrier over the reals
    and none over the rationals -- how small can the linear dimension be, and
    what finite certificate proves it?

Answer (Theorem II.2 / II.3 in research/2026-10-13/POSITIVE_CARRIER_REALIZATION_THEORY_II.md):

* ``rational cone theorem``: a rational behavior has a positive carrier with
  entries in a subfield F of the reals iff its minimal realization carries an
  F-rational polyhedral cone K with  reach(R) subset K subset P  invariant
  under every event operator (R = closure of the reachable cone, P = the
  nonnegative-prediction cone).  Over F = R this is Heller's criterion; the
  field-sensitivity is the point.

* ``irrational contact``: if some extreme ray of P lies in R and is not
  spanned by a rational vector, then NO rational positive carrier exists, of
  any size, although a real one may.  The ray must be an extreme ray of every
  sandwiched cone, and rational polyhedral cones have rational extreme rays.

* ``Fibonacci cat system`` (dimension 2, two actions, rational data):
  action ``a`` runs the hyperbolic automorphism [[2,1],[1,1]]/4 (outcome
  ``tick``) or resets (outcome ``reset``); action ``b`` runs its INVERSE
  [[1,-1],[-1,2]]/4 (``tock``) or resets.  The unstable and stable directions
  e = (1, (sqrt5-1)/2) and e' = (1, -(1+sqrt5)/2) are the only extreme rays
  of both R and P, so  R = P = cone(e, e').  Consequences, all exact:
      linear dimension r = 2,
      d+ over R  = 2   (explicit carrier with entries in Q(sqrt5), below),
      d+ over Q  = infinity.
  This is the smallest conceivable Q/R separation (r <= 2 forces d+_R = r)
  and it is infinite.  The number-theoretic core -- x^2 + x - 1 has no
  rational root, i.e. no integers p, q with q != 0 and p^2 + p q - q^2 = 0 --
  is kernel-checked in ``formal/EODCS_PositiveCarrierII.lean``.

* ``two_dimensional_contact_certificate``: the finite certificate in general
  for r = 2: two event WORDS whose operators share a quadratic-irrational
  eigenvector that is strictly dominant for one and strictly subdominant for
  the other, with the right sign conditions.  Exact arithmetic in Q(sqrt D).

Nothing here is a physical claim; a "carrier over F" is a mathematical
object whose transition probabilities lie in F.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Hashable, Sequence

from .carrier_indexed import rat
from .carrier_realization import (
    LinearRealization, LinearSystem, Mat, RealizationError, Vec, Word,
    charpoly, dot, identity, mat, matmul, matvec, minimal_realization,
    mscale, vec, vecmat,
)


# --------------------------------------------------------------------------
# exact arithmetic in the real quadratic field Q(sqrt D)
# --------------------------------------------------------------------------

def _is_square(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


@dataclass(frozen=True)
class Quad:
    """a + b*sqrt(D) with a, b in Q and D a positive non-square integer.
    Exact field arithmetic and exact ordering (sign determination)."""
    a: Q
    b: Q
    D: int

    def __post_init__(self):
        if type(self.D) is not int or self.D <= 1 or _is_square(self.D):
            raise RealizationError("Quad needs a positive non-square integer radicand")
        object.__setattr__(self, "a", rat(self.a) if not isinstance(self.a, Q) else self.a)
        object.__setattr__(self, "b", rat(self.b) if not isinstance(self.b, Q) else self.b)

    @staticmethod
    def of(x, D: int) -> "Quad":
        if isinstance(x, Quad):
            if x.D != D:
                raise RealizationError("Mixed radicands")
            return x
        return Quad(rat(x), Q(0), D)

    def _same(self, other) -> "Quad":
        return Quad.of(other, self.D)

    def __add__(self, o):
        o = self._same(o)
        return Quad(self.a + o.a, self.b + o.b, self.D)

    __radd__ = __add__

    def __neg__(self):
        return Quad(-self.a, -self.b, self.D)

    def __sub__(self, o):
        return self + (-self._same(o))

    def __rsub__(self, o):
        return self._same(o) - self

    def __mul__(self, o):
        o = self._same(o)
        return Quad(self.a * o.a + self.D * self.b * o.b, self.a * o.b + self.b * o.a, self.D)

    __rmul__ = __mul__

    def conj(self) -> "Quad":
        return Quad(self.a, -self.b, self.D)

    def norm(self) -> Q:
        return self.a * self.a - self.D * self.b * self.b

    def inv(self) -> "Quad":
        n = self.norm()
        if n == 0:
            raise ZeroDivisionError("zero in Q(sqrt D)")
        c = self.conj()
        return Quad(c.a / n, c.b / n, self.D)

    def __truediv__(self, o):
        return self * self._same(o).inv()

    def __rtruediv__(self, o):
        return self._same(o) * self.inv()

    def sign(self) -> int:
        """Exact sign of a + b sqrt D."""
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        # compare a and -b sqrt D: sign(a + b sqrtD) = sign(a) if a^2 > D b^2 and
        # signs differ; if signs agree, it is that common sign.
        if (a > 0) == (b > 0):
            return 1 if a > 0 else -1
        if a * a > self.D * b * b:
            return 1 if a > 0 else -1
        if a * a < self.D * b * b:
            return 1 if b > 0 else -1
        raise RealizationError("sqrt D rational; impossible for a non-square D")

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def __eq__(self, o):
        if not isinstance(o, Quad):
            try:
                o = self._same(o)
            except Exception:
                return NotImplemented
        return self.D == o.D and self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b, self.D))

    def __lt__(self, o):
        return (self - self._same(o)).sign() < 0

    def __le__(self, o):
        return (self - self._same(o)).sign() <= 0

    def __gt__(self, o):
        return (self - self._same(o)).sign() > 0

    def __ge__(self, o):
        return (self - self._same(o)).sign() >= 0

    def is_rational(self) -> bool:
        return self.b == 0

    def __repr__(self):
        return f"({self.a} + {self.b}*sqrt{self.D})"

    def __float__(self):
        return float(self.a) + float(self.b) * math.sqrt(self.D)


QVec = tuple[Quad, ...]
QMat = tuple[tuple[Quad, ...], ...]


def q_matvec(m: Sequence[Sequence], v: Sequence, D: int) -> QVec:
    return tuple(sum((Quad.of(x, D) * Quad.of(y, D) for x, y in zip(row, v)), Quad.of(0, D))
                 for row in m)


def q_dot(u: Sequence, v: Sequence, D: int) -> Quad:
    return sum((Quad.of(x, D) * Quad.of(y, D) for x, y in zip(u, v)), Quad.of(0, D))


def q_solve_2x2(g1: Sequence, g2: Sequence, x: Sequence, D: int) -> tuple[Quad, Quad]:
    """Coefficients (c1, c2) with c1 g1 + c2 g2 = x in Q(sqrt D)^2 (Cramer)."""
    a, c = Quad.of(g1[0], D), Quad.of(g1[1], D)
    b, d = Quad.of(g2[0], D), Quad.of(g2[1], D)
    x0, x1 = Quad.of(x[0], D), Quad.of(x[1], D)
    det = a * d - b * c
    if det.is_zero():
        raise RealizationError("Generators are dependent")
    return ((x0 * d - b * x1) / det, (a * x1 - x0 * c) / det)


# --------------------------------------------------------------------------
# the Fibonacci cat system
# --------------------------------------------------------------------------

def fibonacci_cat_system() -> LinearSystem:
    """V = Q^2, tau = (1, 0), v_* = (1, 0).
    action a: tick = [[2,1],[1,1]]/4, reset = v_* (tau - tau tick) = v_* (1/2, -1/4)
    action b: tock = [[1,-1],[-1,2]]/4 (the inverse automorphism /4),
              reset = v_* (tau - tau tock) = v_* (3/4, 1/4).
    Mass is conserved exactly; every word probability is >= 0 because every
    event preserves cone(e, e') (Theorem II.3)."""
    T1 = mat([[2, 1], [1, 1]])
    Tinv = mat([[1, -1], [-1, 2]])
    if matmul(T1, Tinv) != identity(2):
        raise RealizationError("internal: inverse")
    tau = vec([1, 0])
    vstar = vec([1, 0])
    Ta = mscale(Q(1, 4), T1)
    Tb = mscale(Q(1, 4), Tinv)
    ra = tuple(t - u for t, u in zip(tau, vecmat(tau, Ta)))
    rb = tuple(t - u for t, u in zip(tau, vecmat(tau, Tb)))
    Ra = tuple(tuple(vstar[i] * ra[j] for j in range(2)) for i in range(2))
    Rb = tuple(tuple(vstar[i] * rb[j] for j in range(2)) for i in range(2))
    return LinearSystem(2, {"a": {"tick": Ta, "reset": Ra}, "b": {"tock": Tb, "reset": Rb}},
                        {"s": vstar}, tau)


def golden_rays() -> tuple[QVec, QVec]:
    """e = (1, (sqrt5 - 1)/2) (unstable direction of [[2,1],[1,1]]) and
    e' = (1, -(1 + sqrt5)/2) (stable direction); both tau-normalized."""
    e = (Quad(Q(1), Q(0), 5), Quad(Q(-1, 2), Q(1, 2), 5))
    ep = (Quad(Q(1), Q(0), 5), Quad(Q(-1, 2), Q(-1, 2), 5))
    return e, ep


@dataclass(frozen=True)
class RealCarrierCertificate:
    """A positive carrier over Q(sqrt D): generators G (columns), event
    coefficient matrices B[a][z] (entries in Q(sqrt D)), preparation
    coefficients lam[sigma]; all checked exactly."""
    D: int
    generators: tuple[QVec, ...]
    event_matrices: dict[str, dict[Hashable, QMat]]
    preparations: dict[Hashable, QVec]
    intertwining_exact: bool
    nonnegative: bool
    column_stochastic: bool
    preparations_convex: bool
    all_entries_rational: bool


def quadratic_cone_carrier(system: LinearSystem, generators: Sequence[QVec], D: int
                           ) -> RealCarrierCertificate:
    """Theorem 4.1 over Q(sqrt D) for a 2-dimensional system: given two
    tau-normalized generators g1, g2, solve T_{a,z} g_i = sum_j B[j][i] g_j and
    v_sigma = sum_i lam_i g_i exactly in Q(sqrt D) and check nonnegativity,
    column-stochasticity and convexity.  Nothing is numerical."""
    if system.dimension != 2 or len(generators) != 2:
        raise RealizationError("quadratic_cone_carrier handles dimension 2 with two generators")
    g1, g2 = generators
    tau = system.mass
    for g in (g1, g2):
        if q_dot(tau, g, D) != Quad.of(1, D):
            raise RealizationError("generators must be tau-normalized")
    B: dict[str, dict[Hashable, QMat]] = {}
    nonneg = True
    inter = True
    colstoch = True
    for a in system.actions:
        B[a] = {}
        for z in system.outcomes(a):
            cols = []
            for g in (g1, g2):
                img = q_matvec(system.events[a][z], g, D)
                c1, c2 = q_solve_2x2(g1, g2, img, D)
                # exact re-check of the intertwining T g = c1 g1 + c2 g2
                recon = tuple(c1 * Quad.of(x, D) + c2 * Quad.of(y, D) for x, y in zip(g1, g2))
                if any(not (r - i).is_zero() for r, i in zip(recon, img)):
                    inter = False
                if c1.sign() < 0 or c2.sign() < 0:
                    nonneg = False
                cols.append((c1, c2))
            B[a][z] = tuple(tuple(cols[i][j] for i in range(2)) for j in range(2))
        for i in range(2):
            colsum = sum((B[a][z][j][i] for z in system.outcomes(a) for j in range(2)), Quad.of(0, D))
            if colsum != Quad.of(1, D):
                colstoch = False
    lam = {}
    convex = True
    for s_, v in system.preparations.items():
        c1, c2 = q_solve_2x2(g1, g2, v, D)
        if c1.sign() < 0 or c2.sign() < 0 or (c1 + c2) != Quad.of(1, D):
            convex = False
        lam[s_] = (c1, c2)
    allrat = all(x.is_rational() for blk in B.values() for m in blk.values()
                 for row in m for x in row) and all(x.is_rational() for v in lam.values() for x in v)
    return RealCarrierCertificate(D, (tuple(g1), tuple(g2)), B, lam, inter, nonneg, colstoch,
                                  convex, allrat)


def golden_carrier() -> RealCarrierCertificate:
    """The 2-state positive carrier of the Fibonacci cat system over Q(sqrt5)."""
    e, ep = golden_rays()
    return quadratic_cone_carrier(fibonacci_cat_system(), (e, ep), 5)


# --------------------------------------------------------------------------
# the irrational-contact certificate in dimension 2
# --------------------------------------------------------------------------

def _quadratic_eigen(T: Mat) -> dict:
    """For a 2x2 rational matrix with real irrational eigenvalues, return the
    radicand D (squarefree-ish positive integer: the discriminant's non-square
    part), the eigenvalues as Quad, and tau-free eigenvectors."""
    cp = charpoly(T)  # x^2 - t x + d
    t, d = -cp[1], cp[2]
    disc = t * t - 4 * d
    if disc <= 0:
        return {"real_irrational": False, "discriminant": disc}
    # disc = num/den; sqrt(disc) = sqrt(num*den)/den
    n = disc.numerator * disc.denominator
    # extract square factors
    sq = 1
    rest = n
    f = 2
    while f * f <= rest:
        while rest % (f * f) == 0:
            rest //= f * f
            sq *= f
        f += 1
    if rest == 1:
        return {"real_irrational": False, "discriminant": disc, "rational_sqrt": Q(sq, disc.denominator)}
    D = rest
    root = Quad(Q(0), Q(sq, disc.denominator), D)  # sqrt(disc)
    lam_plus = (Quad.of(t, D) + root) / 2
    lam_minus = (Quad.of(t, D) - root) / 2

    def eigvec(lam: Quad) -> QVec:
        # (T - lam I) v = 0 ; use first row unless degenerate
        a, b = Quad.of(T[0][0], D), Quad.of(T[0][1], D)
        c, dd = Quad.of(T[1][0], D), Quad.of(T[1][1], D)
        if not b.is_zero():
            return (b, lam - a)
        if not c.is_zero():
            return (lam - dd, c)
        raise RealizationError("diagonal matrix cannot have irrational eigenvalues")
    return {"real_irrational": True, "discriminant": disc, "D": D,
            "eigenvalues": (lam_plus, lam_minus),
            "eigenvectors": (eigvec(lam_plus), eigvec(lam_minus))}


def _normalize(v: QVec, tau: Vec, D: int) -> QVec | None:
    t = q_dot(tau, v, D)
    if t.sign() == 0:
        return None
    if t.sign() < 0:
        v = tuple(-x for x in v)
        t = -t
    return tuple(x / t for x in v)


def two_dimensional_contact_certificate(system: LinearSystem, word_in: Word, word_out: Word
                                        ) -> dict:
    """Irrational-contact obstruction for a 2-dimensional rational behavior.

    Let R be the minimal realization (must have dimension 2), T = T_{word_in},
    T' = T_{word_out}.  The certificate establishes, exactly in Q(sqrt D):

      (C1) T has real irrational eigenvalues lam > |lam'| >= 0 with (tau-normalized)
           dominant eigenvector e; some source has a positive e-coefficient, so
           the rays of T^n v_sigma converge to e and e lies in the closed
           reachable cone R.
      (C2) e is an eigenvector of T' with eigenvalue mu, the other eigenvalue
           nu of T' is real with nu > |mu|, and tau(f') != 0 for the other
           eigenvector f'.  Then tau(T'^n x) ~ c'' nu^n tau(f') for x = c e + c'' f',
           so P is contained in the closed half-plane {c'' tau(f') >= 0}, whose
           boundary is the line through e: e is an extreme ray of P.
      (C3) e is irrational (D is not a square).

    Theorem II.2: every sandwiched invariant polyhedral cone has e as an
    extreme ray; a rational polyhedral cone has rational extreme rays; hence
    NO positive carrier over Q exists (any size).  Over R, Theorem 5.1 gives a
    2-state carrier; so d+_R = 2 and d+_Q = infinity.
    """
    R = minimal_realization(system)
    if R.dimension != 2:
        return {"verdict": "NOT_APPLICABLE", "reason": f"linear dimension {R.dimension} != 2"}
    T = R.word_operator(word_in)
    Tp = R.word_operator(word_out)
    tau = R.mass
    eig = _quadratic_eigen(T)
    if not eig["real_irrational"]:
        return {"verdict": "NOT_APPLICABLE", "reason": "word_in operator lacks real irrational eigenvalues",
                "charpoly": charpoly(T)}
    D = eig["D"]
    lp, lm = eig["eigenvalues"]
    vp, vm = eig["eigenvectors"]
    # dominant: larger modulus
    if (lp * lp - lm * lm).sign() > 0:
        lam, lam2, e_raw, f_raw = lp, lm, vp, vm
    elif (lp * lp - lm * lm).sign() < 0:
        lam, lam2, e_raw, f_raw = lm, lp, vm, vp
    else:
        return {"verdict": "NOT_APPLICABLE", "reason": "no strictly dominant eigenvalue"}
    e = _normalize(e_raw, tau, D)
    if e is None:
        return {"verdict": "NOT_APPLICABLE", "reason": "dominant eigenvector has zero mass"}
    # (C1) a source with positive e-coefficient (in basis e, f)
    f = f_raw
    reach_ok = False
    source_coeffs = {}
    for s_, v in R.vectors.items():
        c, cf = q_solve_2x2(e, f, v, D)
        source_coeffs[s_] = (c, cf)
        if c.sign() > 0:
            reach_ok = True
    # (C2) e eigenvector of T' ; other eigenvalue nu real > |mu|
    img = q_matvec(Tp, e, D)
    # proportionality img = mu e
    mu = None
    if not Quad.of(e[0], D).is_zero():
        mu = img[0] / e[0]
    elif not Quad.of(e[1], D).is_zero():
        mu = img[1] / e[1]
    if mu is None or any(not (x - mu * y).is_zero() for x, y in zip(img, e)):
        return {"verdict": "NOT_APPLICABLE", "reason": "contact ray is not an eigenvector of word_out"}
    cp2 = charpoly(Tp)
    t2 = Quad.of(-cp2[1], D)
    nu = t2 - mu  # trace = mu + nu
    out_ok = (nu * nu - mu * mu).sign() > 0 and nu.sign() > 0
    # other eigenvector f' of T' for nu: solve (T' - nu I) f' = 0
    a_, b_ = Quad.of(Tp[0][0], D), Quad.of(Tp[0][1], D)
    c_, d_ = Quad.of(Tp[1][0], D), Quad.of(Tp[1][1], D)
    if not b_.is_zero():
        fp = (b_, nu - a_)
    elif not c_.is_zero():
        fp = (nu - d_, c_)
    else:
        fp = (Quad.of(1, D), Quad.of(0, D)) if (a_ - nu).is_zero() else (Quad.of(0, D), Quad.of(1, D))
    chk = q_matvec(Tp, fp, D)
    if any(not (x - nu * y).is_zero() for x, y in zip(chk, fp)):
        return {"verdict": "NOT_APPLICABLE", "reason": "internal: eigenvector of word_out"}
    tau_fp = q_dot(tau, fp, D)
    out_ok = out_ok and tau_fp.sign() != 0
    irrational = not all(x.is_rational() for x in e)
    verdict = "FINITE_OBSTRUCTION" if (reach_ok and out_ok and irrational) else "NOT_APPLICABLE"
    return {
        "verdict": verdict,
        "field": f"Q(sqrt{D})",
        "D": D,
        "contact_ray_tau_normalized": e,
        "word_in": word_in, "word_in_eigenvalues_dominant_first": (lam, lam2),
        "word_out": word_out, "word_out_eigenvalue_on_contact": mu,
        "word_out_other_eigenvalue": nu, "word_out_other_eigenvector": fp, "tau_of_other": tau_fp,
        "source_coefficients_in_(e,f)": source_coeffs,
        "C1_contact_ray_reachable_limit": reach_ok,
        "C2_contact_ray_extreme_in_prediction_cone": out_ok,
        "C3_contact_ray_irrational": irrational,
        "conclusion": ("no positive carrier over Q of any finite size; a 2-state carrier exists over "
                       + f"Q(sqrt{D}) (Theorem 5.1 / quadratic_cone_carrier)") if verdict == "FINITE_OBSTRUCTION"
                      else "certificate conditions not met (no claim)",
        "theorem": ("rational cone theorem II.2: d+_F < infinity iff an F-rational polyhedral invariant "
                    "cone K with closure(reach) subset K subset P exists; an irrational extreme ray of P "
                    "inside closure(reach) is an extreme ray of every such K"),
    }


def rational_root_free(coeffs: Sequence[Q]) -> dict:
    """Rational-root-theorem check that a monic integer quadratic x^2 + b x + c
    has no rational root; returns the finite candidate list that was tried."""
    cs = [Q(c) for c in coeffs]
    if len(cs) != 3 or cs[0] != 1 or any(c.denominator != 1 for c in cs):
        raise RealizationError("monic integer quadratic expected")
    c0 = int(cs[2])
    cands = set()
    if c0 == 0:
        cands.add(Q(0))
    else:
        for dv in range(1, abs(c0) + 1):
            if c0 % dv == 0:
                cands.add(Q(dv))
                cands.add(Q(-dv))
    tried = sorted(cands)
    vals = [(x, cs[0] * x * x + cs[1] * x + cs[2]) for x in tried]
    return {"polynomial": "x^2 + (%s) x + (%s)" % (cs[1], cs[2]),
            "candidates": tried, "values": vals,
            "no_rational_root": all(v != 0 for _, v in vals)}


# --------------------------------------------------------------------------
# dimension-2 dichotomy helper: interval-invariance of a rational slice
# --------------------------------------------------------------------------

def rational_interval_invariance(realization: LinearRealization, p: Q, q: Q) -> dict:
    """For a 2-dimensional realization with tau = (1, 0) in its coordinates --
    or any coordinates: the slice is parametrized by x = x0 + t k with
    tau(x0) = 1, tau(k) = 0 -- check whether the rational interval [p, q] of
    slice parameters gives a sandwiched invariant cone (sources inside, every
    event maps both endpoints into the interval or to 0).  This is the
    r = 2 decision for a PROPOSED interval; Theorem II.4 says d+_Q is 2 or
    infinity, and 2 iff some rational interval passes this test."""
    if realization.dimension != 2:
        raise RealizationError("dimension 2 required")
    tau = realization.mass
    # x0 with tau(x0)=1, k with tau(k)=0
    if tau[0] != 0:
        x0 = (1 / tau[0], Q(0))
        k = (-tau[1] / tau[0], Q(1))
    elif tau[1] != 0:
        x0 = (Q(0), 1 / tau[1])
        k = (Q(1), -tau[0] / tau[1])
    else:
        raise RealizationError("zero mass functional")

    def point(t: Q) -> Vec:
        return tuple(a + t * b for a, b in zip(x0, k))

    def param(x: Vec) -> Q | None:
        m = dot(tau, x)
        if m <= 0:
            return None
        y = tuple(c / m for c in x)
        d = tuple(a - b for a, b in zip(y, x0))
        # d = t k
        for i in range(2):
            if k[i] != 0:
                return d[i] / k[i]
        return None

    gens = (point(p), point(q))
    checks = []
    ok = p <= q
    for s_, v in realization.vectors.items():
        t = param(v)
        inside = t is not None and p <= t <= q
        checks.append({"source": s_, "parameter": t, "inside": inside})
        ok = ok and inside
    for a in realization.actions:
        for z in realization.outcomes[a]:
            for name, g in (("p", gens[0]), ("q", gens[1])):
                img = matvec(realization.operators[a][z], g)
                if all(x == 0 for x in img):
                    checks.append({"event": (a, z), "endpoint": name, "image": "zero", "inside": True})
                    continue
                t = param(img)
                inside = t is not None and p <= t <= q
                checks.append({"event": (a, z), "endpoint": name, "parameter": t, "inside": inside})
                ok = ok and inside
    return {"interval": (p, q), "generators": gens, "invariant_sandwiched": ok, "checks": checks}


def rational_interval_search(realization: LinearRealization, *, denominators: Sequence[int] = (1, 2, 3, 4),
                             bound: int = 4) -> dict:
    """Grid search over rational intervals [p, q] for the r = 2 decision of
    Theorem II.4: a hit is a 2-state RATIONAL carrier (via ``verify_cone``);
    exhausting the grid is UNRESOLVED, never an impossibility verdict (the
    irrational-contact certificate is the impossibility route)."""
    if realization.dimension != 2:
        raise RealizationError("dimension 2 required")
    from .carrier_realization import verify_cone
    vals = sorted({Q(p, q) for q in denominators for p in range(-bound * q, bound * q + 1)})
    tried = 0
    for i, p in enumerate(vals):
        for q in vals[i + 1:]:
            tried += 1
            res = rational_interval_invariance(realization, p, q)
            if res["invariant_sandwiched"]:
                cert = verify_cone(realization, res["generators"])
                if cert.valid:
                    return {"verdict": "LAWFUL_REALIZATION", "interval": (p, q), "certificate": cert,
                            "tried": tried}
    return {"verdict": "UNRESOLVED", "tried": tried, "reason": "grid exhausted (not an impossibility proof)"}
