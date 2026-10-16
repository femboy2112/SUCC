"""Exact finite observer/Schur models, with explicit source and authority limits.

Paper theorems: research/2026-10-16/OBSERVER_SCHUR_THEOREMS.md.
The declared scalar field is Q with the Euclidean bilinear metric. Matrix
identities also hold after scalar extension to R. These finite models are NOT
the Suzuki source, a Lean importer, or an infinite-dimensional sign oracle.
Existing exact matrix operations are reused; no numerical package is loaded.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
import json

from .recursive_operator_gluing import (
    block, determinant, inverse, matrix, pd, principal_minors, product, psd,
    symmetric, transpose,
)
from .source_field_inverse_limits import FieldSourcePassport


class ObserverSchurError(ValueError):
    """A finite type, range, metric, or positivity hypothesis failed."""


def _rat(value):
    if type(value) not in (int, F):
        raise ObserverSchurError("Exact int or Fraction required; no bool/float")
    return F(value)


def _mat(rows):
    if type(rows) not in (tuple, list) or not 1 <= len(rows) <= 8:
        raise ObserverSchurError("Matrix row budget is 1..8")
    if any(type(row) not in (tuple, list) or not 1 <= len(row) <= 8 for row in rows):
        raise ObserverSchurError("Matrix column budget is 1..8")
    if any(len(row) != len(rows[0]) for row in rows):
        raise ObserverSchurError("Ragged matrix")
    return matrix(tuple(tuple(_rat(x) for x in row) for row in rows))


def _vec(values, n):
    if type(values) not in (tuple, list) or len(values) != n:
        raise ObserverSchurError("Vector dimension mismatch")
    return tuple(_rat(x) for x in values)


def _dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F())


def _mv(a, x):
    return tuple(_dot(row, x) for row in a)


def _add(a, b, scale=F(1)):
    return tuple(tuple(x + scale*y for x, y in zip(row, other))
                 for row, other in zip(a, b))


def _zero(a):
    return all(x == 0 for row in a for x in row)


def _basis(n, i):
    return tuple(F(int(j == i)) for j in range(n))


def _rref(a):
    """Exact elimination; caller supplies a nonempty rectangular matrix."""
    rows = [list(row) for row in a]
    pivots = []
    r = 0
    for c in range(len(rows[0])):
        p = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        v = rows[r][c]
        rows[r] = [x/v for x in rows[r]]
        for i in range(len(rows)):
            if i != r:
                v = rows[i][c]
                rows[i] = [x-v*y for x, y in zip(rows[i], rows[r])]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    return tuple(tuple(row) for row in rows), tuple(pivots)


def kernel_basis(rows):
    """A complete rational nullspace basis, not a sampled nullspace test."""
    a = _mat(rows)
    r, pivots = _rref(a)
    out = []
    for c in range(len(a[0])):
        if c not in pivots:
            z = list(_basis(len(a[0]), c))
            for i, p in enumerate(pivots):
                z[p] = -r[i][c]
            out.append(tuple(z))
    return tuple(out)


def solve_linear(rows, values):
    """Return one rational solution with free variables zero, or None."""
    a = _mat(rows)
    b = _vec(values, len(a))
    n = len(a[0])
    r, pivots = _rref(tuple(row+(v,) for row, v in zip(a, b)))
    if n in pivots:
        return None
    x = [F()]*n
    for i, p in enumerate(pivots):
        x[p] = r[i][-1]
    return tuple(x)


def quadratic(rows, values):
    a = _mat(rows)
    if not symmetric(a):
        raise ObserverSchurError("Symmetric quadratic form required")
    x = _vec(values, len(a))
    return _dot(x, _mv(a, x))


def negative_direction(rows):
    """Construct rational v with v'Av<0, or None iff A is PSD.

    Congruence elimination, independent of the existing principal-minor PSD
    test. Zero diagonal/nonzero row is retained as an indefinite control.
    """
    a = _mat(rows)
    if not symmetric(a):
        raise ObserverSchurError("Symmetric form required")
    n = len(a)
    for i in range(n):
        if a[i][i] < 0:
            return _basis(n, i)
        if a[i][i] == 0:
            for j in range(n):
                if a[i][j]:
                    v = list(_basis(n, i))
                    v[j] = -a[i][j]/(abs(a[j][j])+1)
                    return tuple(v)
    pivot = next((i for i in range(n) if a[i][i] > 0), None)
    if pivot is None or n == 1:
        return None
    rest = tuple(i for i in range(n) if i != pivot)
    s = tuple(tuple(a[i][j]-a[i][pivot]*a[pivot][j]/a[pivot][pivot]
                    for j in rest) for i in rest)
    y = negative_direction(s)
    if y is None:
        return None
    v = [F()]*n
    for i, value in zip(rest, y):
        v[i] = value
    v[pivot] = -sum((a[pivot][i]*v[i] for i in rest), F())/a[pivot][pivot]
    return tuple(v)


@dataclass(frozen=True)
class RationalSourceSpace:
    passport: FieldSourcePassport
    basis: tuple[str, ...]

    def __post_init__(self):
        if type(self.passport) is not FieldSourcePassport:
            raise ObserverSchurError("Existing typed source passport required")
        if (type(self.basis) is not tuple or not 1 <= len(self.basis) <= 8 or
                any(type(s) is not str or not s.strip() for s in self.basis) or
                len(set(self.basis)) != len(self.basis)):
            raise ObserverSchurError("One to eight distinct named coordinates required")

    @property
    def metric(self):
        return "EUCLIDEAN_RATIONAL_BILINEAR"


@dataclass(frozen=True)
class QuadraticModel:
    space: RationalSourceSpace
    gram: tuple[tuple[F, ...], ...]

    def __post_init__(self):
        if type(self.space) is not RationalSourceSpace:
            raise ObserverSchurError("Typed rational source space required")
        g = _mat(self.gram)
        if not symmetric(g) or len(g) != len(self.space.basis):
            raise ObserverSchurError("Symmetric form on the declared coordinates required")
        object.__setattr__(self, "gram", g)

    @property
    def fingerprint(self):
        payload = (self.space.passport.source, self.space.passport.observer,
                   self.space.passport.epoch, self.space.basis, self.space.metric,
                   [[str(x) for x in row] for row in self.gram])
        return sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()

    def energy(self, values):
        return quadratic(self.gram, values)


@dataclass(frozen=True)
class LinearObservation:
    space: RationalSourceSpace
    rows: tuple[tuple[F, ...], ...]

    def __post_init__(self):
        if type(self.space) is not RationalSourceSpace:
            raise ObserverSchurError("Typed rational source space required")
        o = _mat(self.rows)
        if len(o[0]) != len(self.space.basis):
            raise ObserverSchurError("Observation/source dimension mismatch")
        object.__setattr__(self, "rows", o)

    def observe(self, values):
        return _mv(self.rows, _vec(values, len(self.space.basis)))


def _same_space(model, observation):
    if (type(model) is not QuadraticModel or type(observation) is not LinearObservation
            or model.space != observation.space):
        raise ObserverSchurError("Exact source, epoch, basis, and metric must agree")


def _receipt(model):
    return {"authority": "EXACT_FINITE_CHECK", "model_sha256": model.fingerprint,
            "source_kind": "DECLARED_FINITE_RATIONAL_MODEL",
            "source_identification_discharged": False,
            "Lean_kernel_replayed": False, "infinite_operator_sign_certified": False}


def energy_factorization(model, observation):
    """OS-01: ker(O) subset ker(G), with an exact hidden-fiber witness on failure."""
    _same_space(model, observation)
    basis = kernel_basis(observation.rows)
    for z in basis:
        gz = _mv(model.gram, z)
        if any(gz):
            if model.energy(z):
                u = (F(),)*len(z)
            else:
                u = _basis(len(z), next(i for i, x in enumerate(gz) if x))
            v = tuple(x+y for x, y in zip(u, z))
            return dict(_receipt(model), factors=False, kernel_basis=basis,
                        witness=(u, v), observations=(observation.observe(u), observation.observe(v)),
                        energies=(model.energy(u), model.energy(v)))
    return dict(_receipt(model), factors=True, kernel_basis=basis,
                decoder="decode_energy on the reachable observation image only")


def decode_energy(model, observation, artifact):
    """No hidden source argument; refuses both nonfactorization and unreachable data."""
    if not energy_factorization(model, observation)["factors"]:
        raise ObserverSchurError("Energy is not constant on observation fibers")
    u = solve_linear(observation.rows, artifact)
    if u is None:
        raise ObserverSchurError("Observation artifact is unreachable")
    return model.energy(u)


def linear_factorization(observation, target_rows, bound=None):
    """Exact finite linear decoder and optional ||h v|| <= C ||O v|| gate.

    Finite dimensionality makes every induced decoder bounded. There is no
    promotion of bounds from finitely many truncations to an infinite source.
    """
    if type(observation) is not LinearObservation:
        raise ObserverSchurError("Typed linear observation required")
    h = _mat(target_rows)
    if len(h[0]) != len(observation.space.basis):
        raise ObserverSchurError("Target/source dimension mismatch")
    for z in kernel_basis(observation.rows):
        if any(_mv(h, z)):
            return {"factors": False, "kernel_witness": z,
                    "target_difference": _mv(h, z), "authority": "EXACT_FINITE_CHECK"}
    decoder = tuple(solve_linear(transpose(observation.rows), row) for row in h)
    if any(row is None for row in decoder) or product(decoder, observation.rows) != h:
        raise ArithmeticError("Exact decoder construction failed")
    answer = {"factors": True, "decoder_rows": decoder,
              "bounded_extension_scope": "THIS_FINITE_RATIONAL_MODEL_ONLY",
              "authority": "EXACT_FINITE_CHECK"}
    if bound is not None:
        c = _rat(bound)
        if c < 0:
            raise ObserverSchurError("Nonnegative domination constant required")
        oo = product(transpose(observation.rows), observation.rows)
        hh = product(transpose(h), h)
        gap = _add(tuple(tuple(c*c*x for x in row) for row in oo), hh, -1)
        answer.update(bound=c, bound_valid=psd(gap), domination_gap=gap)
    return answer


@dataclass(frozen=True)
class BlockModel:
    model: QuadraticModel
    low_dimension: int

    def __post_init__(self):
        if (type(self.model) is not QuadraticModel or type(self.low_dimension) is not int
                or not 1 <= self.low_dimension < len(self.model.gram)):
            raise ObserverSchurError("A nonempty low/high split of the typed model is required")
        if not psd(self.d):
            raise ObserverSchurError("This theorem family requires D >= 0")

    @property
    def a(self):
        p = self.low_dimension
        return tuple(row[:p] for row in self.model.gram[:p])

    @property
    def b(self):
        return tuple(row[self.low_dimension:] for row in self.model.gram[:self.low_dimension])

    @property
    def d(self):
        return tuple(row[self.low_dimension:] for row in self.model.gram[self.low_dimension:])

    @property
    def observation(self):
        n = len(self.model.gram)
        return LinearObservation(self.model.space, tuple(_basis(n, i) for i in range(self.low_dimension)))


def sign_factorization(split):
    """OS-02, including D=0: exact sign classification and fiber witnesses."""
    if type(split) is not BlockModel:
        raise ObserverSchurError("Typed PSD-high split required")
    g, p = split.model, split.low_dimension
    if _zero(split.d):
        if _zero(split.b):
            return dict(_receipt(g), factors=True, case="D_ZERO_B_ZERO",
                        decoder="1_{x' A x >= 0}; A may be indefinite")
        # At x=e_i a nonzero cross term is affine and unbounded in h.
        i, j = next((i, j) for i, row in enumerate(split.b) for j, x in enumerate(row) if x)
        x = _basis(p, i)
        k = len(split.d)
        cross = split.b[i][j]
        center = -split.a[i][i]/(2*cross)
        hm = [F()]*k
        hp = [F()]*k
        hm[j], hp[j] = center-1/(2*cross), center+1/(2*cross)
        u, v = x+tuple(hm), x+tuple(hp)
    else:
        u = negative_direction(g.gram)
        if u is None:
            return dict(_receipt(g), factors=True, case="D_NONZERO_G_PSD",
                        decoder="constant 1")
        # Positive curvature exists on a coordinate because D is PSD/nonzero.
        j = next(j for j in range(len(split.d)) if split.d[j][j] > 0)
        x = u[:p]
        alpha = split.d[j][j]
        beta = sum((x[i]*split.b[i][j] for i in range(p)), F())
        a = quadratic(split.a, x)
        t = 1+(2*abs(beta)+abs(a))/alpha
        h = tuple(t if i == j else F() for i in range(len(split.d)))
        v = x+h
    if not (g.energy(u) < 0 < g.energy(v) and u[:p] == v[:p]):
        raise ArithmeticError("Exact opposite-sign fiber construction failed")
    return dict(_receipt(g), factors=False, case="OPPOSITE_SIGNS_IN_ONE_FIBER",
                witness=(u, v), observation=u[:p], energies=(g.energy(u), g.energy(v)))


def fiber_envelope(split, low):
    """OS-03 finite version. Failure means -infinity in THIS fiber."""
    if type(split) is not BlockModel:
        raise ObserverSchurError("Typed PSD-high split required")
    x = _vec(low, split.low_dimension)
    b = _mv(transpose(split.b), x)
    y = solve_linear(split.d, b)
    if y is None:
        z = next(z for z in kernel_basis(split.d) if _dot(b, z))
        c = _dot(b, z)
        direction = tuple(-v/c for v in z)
        return dict(_receipt(split.model), finite=False, infimum="NEGATIVE_INFINITY",
                    low=x, hidden_ray=direction, ray_constant=quadratic(split.a, x),
                    ray_linear_coefficient=F(-2), attained=False)
    hidden = tuple(-v for v in y)
    return dict(_receipt(split.model), finite=True, low=x, attained=True,
                minimizing_high=hidden, value=split.model.energy(x+hidden),
                normal_equation_solution=y)


def schur_envelope(split):
    """All-fiber finite range gate; X solves D X=B*, S=A-BX."""
    if type(split) is not BlockModel:
        raise ObserverSchurError("Typed PSD-high split required")
    cols = []
    for i, b in enumerate(split.b):
        y = solve_linear(split.d, b)
        if y is None:
            return dict(_receipt(split.model), all_fibers_finite=False,
                        obstruction=fiber_envelope(split, _basis(split.low_dimension, i)))
        cols.append(y)
    xmap = transpose(cols)
    response = product(split.b, xmap)
    s = _add(split.a, response, -1)
    if not symmetric(response) or not psd(response):
        raise ArithmeticError("Positive range response construction failed")
    return dict(_receipt(split.model), all_fibers_finite=True, response=response,
                schur=s, response_map=xmap, schur_psd=psd(s),
                full_model_psd=psd(split.model.gram), all_fibers_attained=True)


def psd_two_by_two(rows):
    a = _mat(rows)
    if len(a) != 2 or not symmetric(a):
        raise ObserverSchurError("Symmetric 2x2 matrix required")
    det = determinant(a)
    return {"diagonals": (a[0][0], a[1][1]), "determinant": det,
            "psd": a[0][0] >= 0 and a[1][1] >= 0 and det >= 0}


def parity_sectors(split, signs):
    """Verify full source reflection before extracting low/high parity sectors."""
    if type(split) is not BlockModel:
        raise ObserverSchurError("Typed split required")
    n = len(split.model.gram)
    if (type(signs) not in (tuple, list) or len(signs) != n or
            any(type(x) is not int or x not in (-1, 1) for x in signs)):
        raise ObserverSchurError("One exact +/-1 reflection eigenvalue per coordinate")
    if any(split.model.gram[i][j] and signs[i] != signs[j] for i in range(n) for j in range(n)):
        raise ObserverSchurError("Full form fails reflection intertwining; do not erase cross entries")
    env = schur_envelope(split)
    if not env["all_fibers_finite"]:
        raise ObserverSchurError("Parity does not discharge the Schur range condition")
    out = []
    for sign in (-1, 1):
        low = tuple(i for i in range(split.low_dimension) if signs[i] == sign)
        high = tuple(i-split.low_dimension for i in range(split.low_dimension, n) if signs[i] == sign)
        sector = tuple(tuple(env["schur"][i][j] for j in low) for i in low)
        out.append({"sign": sign, "low_indices": low, "high_indices": high,
                    "schur": sector, "psd": psd(sector) if low else True})
    return tuple(out)


def contraction_certificate(split):
    """OS-05: avoid square roots by testing R <= A exactly, with A positive definite."""
    if type(split) is not BlockModel or not pd(split.a):
        raise ObserverSchurError("A positive definite is required for the contraction equivalence")
    env = schur_envelope(split)
    if not env["all_fibers_finite"]:
        raise ObserverSchurError("D square-root range condition fails")
    return dict(_receipt(split.model), contraction_at_most_one=env["schur_psd"],
                generalized_loewner_gap=env["schur"], response=env["response"],
                gap_principal_minors=principal_minors(env["schur"]),
                explicit_matrix_square_root_computed=False)


def trial_enclosure(split, trial_rows, relative_metric, kappa):
    """Finite OS-06: exact two-sided bracket using D >= kappa K, K>0.

    K here is a declared finite positive definite matrix. Its inverse is not
    applied to an infinite compact operator. Trial U maps LOW to HIGH.
    """
    if type(split) is not BlockModel:
        raise ObserverSchurError("Typed split required")
    u, k, c = _mat(trial_rows), _mat(relative_metric), _rat(kappa)
    if (len(u) != len(split.d) or len(u[0]) != split.low_dimension or
            len(k) != len(split.d) or not symmetric(k) or c <= 0 or not pd(k)):
        raise ObserverSchurError("High/low trial shape, K>0, and kappa>0 required")
    if not psd(_add(split.d, k, -c)):
        raise ObserverSchurError("The declared D >= kappa K hypothesis is false")
    r = _add(transpose(split.b), product(split.d, u), -1)
    bu = product(split.b, u)
    lu = _add(_add(bu, transpose(bu)), product(transpose(u), product(split.d, u)), -1)
    correction = product(transpose(r), product(inverse(k), r))
    upper = _add(split.a, lu, -1)
    lower = _add(upper, correction, -1/c)
    env = schur_envelope(split)
    if not env["all_fibers_finite"]:
        raise ArithmeticError("Finite positive definite high range unexpectedly failed")
    s = env["schur"]
    if not psd(_add(s, lower, -1)) or not psd(_add(upper, s, -1)):
        raise ArithmeticError("Exact trial bracket verification failed")
    return dict(_receipt(split.model), lower=lower, upper=upper, exact_schur=s,
                residual=r, relative_residual_gram=correction, kappa=c,
                sufficient_lower_psd=psd(lower), exact_schur_psd=psd(s))
