"""Exact, explicitly synthetic model selection and boundary composition.

Paper proofs and source domains: REALITY_PIN_SELECTION_GLUING.md.  Source
passports here are consistency checks, never authentication of real equipment.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
import json

from .boundary_realization_selection import matrix_inverse, matmul, rational


class PinContractError(ValueError):
    """Malformed exact model family, source passport or boundary operation."""


def _matrix(matrix):
    out = tuple(tuple(rational(v) for v in row) for row in matrix)
    if not out or not out[0] or any(len(r) != len(out[0]) for r in out):
        raise PinContractError("nonempty rectangular exact matrix required")
    return out


def transpose(matrix):
    return tuple(zip(*_matrix(matrix)))


def pullback(matrix, trace):
    """Energy/flux pullback T^t L T, with u_local=T u_shared."""
    matrix, trace = _matrix(matrix), _matrix(trace)
    if len(matrix) != len(matrix[0]) or len(trace) != len(matrix):
        raise PinContractError("square energy and compatible trace required")
    return matmul(transpose(trace), matmul(matrix, trace))


def schur(matrix, retained):
    """Retain ordered ports; eliminate the complement by exact linear solve."""
    matrix = _matrix(matrix)
    n = len(matrix)
    if len(matrix[0]) != n or matrix != transpose(matrix):
        raise PinContractError("symmetric finite energy matrix required")
    retained = tuple(retained)
    if not retained or len(set(retained)) != len(retained) or any(
        type(i) is not int or not 0 <= i < n for i in retained
    ):
        raise PinContractError("distinct valid retained ports required")
    inside = tuple(i for i in range(n) if i not in retained)
    c = tuple(tuple(matrix[i][j] for j in retained) for i in retained)
    if not inside:
        return c
    a = tuple(tuple(matrix[i][j] for j in inside) for i in inside)
    b = tuple(tuple(matrix[i][j] for j in retained) for i in inside)
    correction = matmul(transpose(b), matmul(matrix_inverse(a), b))
    return tuple(tuple(c[i][j] - correction[i][j]
                       for j in range(len(c))) for i in range(len(c)))


def glue(responses, traces):
    """Sum T_i^t Lambda_i T_i; shared coordinates fix flux orientation."""
    responses, traces = tuple(responses), tuple(traces)
    if not responses or len(responses) != len(traces):
        raise PinContractError("one trace map per component required")
    pieces = tuple(pullback(lam, t) for lam, t in zip(responses, traces))
    n = len(pieces[0])
    if any(len(p) != n for p in pieces):
        raise PinContractError("all components need one shared boundary space")
    return tuple(tuple(sum((p[i][j] for p in pieces), Q())
                       for j in range(n)) for i in range(n))


def schur_perturbation_bound(interior_gap, coupling_norm, delta_a, delta_b, delta_c):
    """Operator-norm bound from certified A>=a I and block perturbation bounds.

    Input norm/gap certificates are assumptions; this routine does not infer
    them from sampled matrices or authenticate them by metadata.
    """
    a, b, da, db, dc = map(rational, (interior_gap, coupling_norm, delta_a, delta_b, delta_c))
    if a <= 0 or min(b, da, db, dc) < 0 or da >= a:
        raise PinContractError("positive gap, nonnegative bounds, and delta_a < gap required")
    return dc + (2 * b * db + db * db) / (a - da) + b * b * da / (a * (a - da))


@dataclass(frozen=True)
class Prediction:
    """A model or model-family prediction; grouping meaning is typed by PinPlan."""
    model: str
    gauge_class: str
    values: tuple
    errors: tuple

    def __post_init__(self):
        if not self.model or not self.gauge_class or not self.values:
            raise PinContractError("named model/gauge and nonempty predictions required")
        if len(self.values) != len(self.errors):
            raise PinContractError("one theoretical uncertainty per probe required")
        object.__setattr__(self, "values", tuple(rational(v) for v in self.values))
        object.__setattr__(self, "errors", tuple(rational(e) for e in self.errors))
        if any(e < 0 for e in self.errors):
            raise PinContractError("negative theoretical uncertainty")


@dataclass(frozen=True)
class PinPlan:
    source_id: str
    probe_ids: tuple
    predictions: tuple
    instrument_errors: tuple
    identification_scope: str = "model_gauge"

    def __post_init__(self):
        object.__setattr__(self, "probe_ids", tuple(self.probe_ids))
        object.__setattr__(self, "predictions", tuple(self.predictions))
        if self.identification_scope not in ("model_gauge", "topology_family"):
            raise PinContractError("explicit model-gauge or topology-family scope required")
        if not self.source_id or not self.probe_ids or len(set(self.probe_ids)) != len(self.probe_ids):
            raise PinContractError("source identity and distinct probe identities required")
        if any(not isinstance(p, Prediction) for p in self.predictions):
            raise PinContractError("typed predictions required")
        if not self.predictions or len({p.model for p in self.predictions}) != len(self.predictions):
            raise PinContractError("nonempty family with distinct model names required")
        k = len(self.probe_ids)
        if len(self.instrument_errors) != k or any(len(p.values) != k for p in self.predictions):
            raise PinContractError("probe/prediction dimension mismatch")
        object.__setattr__(self, "instrument_errors", tuple(rational(e) for e in self.instrument_errors))
        if any(e < 0 for e in self.instrument_errors):
            raise PinContractError("negative instrument uncertainty")

    def digest(self):
        """Commitment of predicted values, source labels and declared budgets."""
        data = [self.source_id, self.probe_ids, self.identification_scope,
                [(p.model, p.gauge_class, list(map(str, p.values)), list(map(str, p.errors)))
                 for p in self.predictions], list(map(str, self.instrument_errors))]
        return sha256(json.dumps(data, separators=(",", ":")).encode()).hexdigest()


def identify(plan, source_id, commitment, readings):
    """Intersect exact uncertainty boxes; readings can cover any probe subset.

    A matching digest prevents accidental within-transcript model mutation.
    It cannot establish when a human actually chose the model family.
    """
    if not isinstance(plan, PinPlan) or source_id != plan.source_id or commitment != plan.digest():
        raise PinContractError("wrong source or prediction commitment")
    if not readings or any(key not in plan.probe_ids for key in readings):
        raise PinContractError("nonempty readings from the declared probe language required")
    readings = {key: rational(value) for key, value in readings.items()}
    survivors = tuple(p for p in plan.predictions if all(
        abs(p.values[j] - readings[key]) <= p.errors[j] + plan.instrument_errors[j]
        for j, key in enumerate(plan.probe_ids) if key in readings
    ))
    classes = tuple(sorted({p.gauge_class for p in survivors}))
    return {"models": tuple(p.model for p in survivors), "target_classes": classes,
            "gauge_classes": classes if plan.identification_scope == "model_gauge" else (),
            "identification_scope": plan.identification_scope,
            "unique_within_family": len(classes) == 1,
            "unique_gauge_within_family": plan.identification_scope == "model_gauge" and len(classes) == 1,
            "empty_fiber": not survivors, "physical_authentication": False}


def separation_witnesses(plan):
    """Every distinct-class pair needs a coordinate separated by tau_i+tau_j+2eps."""
    result = []
    for i, p in enumerate(plan.predictions):
        for q in plan.predictions[i + 1:]:
            if p.gauge_class == q.gauge_class:
                continue
            margins = tuple(abs(v - w) - a - b - 2 * e for v, w, a, b, e in
                            zip(p.values, q.values, p.errors, q.errors, plan.instrument_errors))
            result.append((p.model, q.model, tuple(
                plan.probe_ids[j] for j, m in enumerate(margins) if m > 0)))
    return tuple(result)


def series_rc(g_left, g_right, capacitance, laplace):
    """One port: left--hidden--ground, hidden shunt capacitor; normalized units."""
    a, b, c, s = map(rational, (g_left, g_right, capacitance, laplace))
    if a <= 0 or b <= 0 or c < 0 or s < 0:
        raise PinContractError("positive conductances and nonnegative capacitance/Laplace s")
    return a * (b + s * c) / (a + b + s * c)


def series_rc_box(g_left, g_right, capacitance, laplace):
    """Exact extremizers on a component box, by coordinatewise monotonicity."""
    intervals = tuple(tuple(map(rational, interval)) for interval in (g_left, g_right, capacitance))
    if any(len(i) != 2 or i[0] > i[1] for i in intervals):
        raise PinContractError("ordered component intervals required")
    return (series_rc(*(i[0] for i in intervals), laplace),
            series_rc(*(i[1] for i in intervals), laplace))


def _center_radius(interval):
    low, high = interval
    return (low + high) / 2, (high - low) / 2


def rc_plan():
    """Freeze a 1%-component family at DC, s=1 calibration and s=3 holdout."""
    bounds = (Q(99, 100), Q(101, 100))
    boxes = tuple(series_rc_box(bounds, bounds, bounds, s) for s in (0, 1, 3))
    mids, radii = zip(*map(_center_radius, boxes))
    return PinPlan("synthetic-rc-source-v1", ("dc", "laplace-1", "holdout-laplace-3"),
                   (Prediction("direct", "direct", (Q(1, 2),) * 3, (Q(1, 200),) * 3),
                    Prediction("series-capacitor", "series-capacitor", mids, radii)),
                   (Q(1, 500),) * 3, identification_scope="topology_family")


def synthetic_rc_receipt():
    """Predeclared predictions, followed by generated data; no empirical claim."""
    plan = rc_plan()
    commitment = plan.digest()
    # Data are created only after the entire prediction/holdout plan is frozen.
    actual_components = (Q(201, 200), Q(199, 200), Q(501, 500))
    dc = series_rc(*actual_components, 0)
    calibration = series_rc(*actual_components, 1)
    holdout = series_rc(*actual_components, 3)
    return {
        "source_kind": "synthetic", "physical_measurements_performed": False,
        "plan_sha256": commitment,
        "component_intervals": ["99/100", "101/100"],
        "instrument_error_per_probe": "1/500",
        "data": {"dc": str(dc), "laplace-1": str(calibration), "holdout-laplace-3": str(holdout)},
        "dc_selection": identify(plan, plan.source_id, commitment, {"dc": dc}),
        "calibration_selection": identify(plan, plan.source_id, commitment, {"dc": dc, "laplace-1": calibration}),
        "heldout_selection": identify(plan, plan.source_id, commitment, {"holdout-laplace-3": holdout}),
        "separation_witnesses": separation_witnesses(plan),
    }


def refine_equal_series(interval, reading, error, laplace, rounds):
    """Certified dyadic cover for equal-conductance g in [lo,hi], known c=1.

    Output covers every feasible g, allowing near-threshold false survivors.
    With leaf width h and true-source error eps, diameter <= 4eps+2h.
    """
    low, high = map(rational, interval)
    reading, error, s = map(rational, (reading, error, laplace))
    if low <= 0 or low > high or error < 0 or s < 0 or type(rounds) is not int or not 0 <= rounds <= 16:
        raise PinContractError("positive bounded interval, valid error and 0..16 rounds required")
    leaves = [(low, high)]
    for _ in range(rounds):
        leaves = [(a, (a+b)/2) for a, b in leaves] + [((a+b)/2, b) for a, b in leaves]
    feasible = tuple((a, b) for a, b in leaves if
                     series_rc(a, a, 1, s) <= reading + error and
                     series_rc(b, b, 1, s) >= reading - error)
    return tuple(sorted(feasible))
