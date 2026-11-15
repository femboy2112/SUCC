"""Exact two-qubit controls for conditioning, disturbance and entanglement.

This real rational submodel extends the inherited quantum_records.Instrument
to either side of a two-qubit density matrix. It does not authenticate a
physical quantum source, a BBP instrument, or an ER=EPR geometry.

The two-axis separability witness assumes trusted orthogonal qubit axes.
The rotated CHSH values are model predictions; experimental interpretation
requires independent setting choices, no inter-wing communication, and no
selective loss. Proofs and adversarial scope are in the round's
research/2026-11-15/observer_haar_causal_volume/ADVERSARY_NOTES.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .quantum_records import Instrument


Matrix = tuple[tuple[Q, ...], ...]
Axis = tuple[Q | int, Q | int]  # coefficients of (X,Z)
MAX_OUTCOMES = 16
I: Matrix = ((Q(1), Q(0)), (Q(0), Q(1)))
X: Matrix = ((Q(0), Q(1)), (Q(1), Q(0)))
Z: Matrix = ((Q(1), Q(0)), (Q(0), Q(-1)))
DEFAULT_ALICE_AXES = ((0, 1), (1, 0))
DEFAULT_BOB_AXES = ((Q(3, 5), Q(4, 5)), (Q(-3, 5), Q(4, 5)))


class QuantumInstrumentError(ValueError):
    """Invalid exact state, axis, side, outcome, or bounded instrument."""


def _rational(value) -> Q:
    if type(value) not in (int, Q):
        raise QuantumInstrumentError("use exact int/Fraction entries, not floats or bools")
    return Q(value)


def _matrix(value, size: int) -> Matrix:
    if not isinstance(value, (tuple, list)) or len(value) != size:
        raise QuantumInstrumentError(f"expected a {size} by {size} matrix")
    rows = []
    for row in value:
        if not isinstance(row, (tuple, list)) or len(row) != size:
            raise QuantumInstrumentError(f"expected a {size} by {size} matrix")
        rows.append(tuple(_rational(x) for x in row))
    return tuple(rows)


def _trace(a: Matrix) -> Q:
    return sum((a[i][i] for i in range(len(a))), Q())


def _transpose(a: Matrix) -> Matrix:
    return tuple(zip(*a))


def _multiply(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(n)), Q())
                       for j in range(n)) for i in range(n))


def _scale(a: Matrix, scalar: Q) -> Matrix:
    return tuple(tuple(scalar*x for x in row) for row in a)


def _add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(x+y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def _tensor(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j]*b[k][ell] for j in range(2) for ell in range(2))
                 for i in range(2) for k in range(2))


def _density(value, size: int) -> Matrix:
    """Exact symmetric PSD test by successive Schur complements.

    A zero diagonal of a PSD matrix has a zero row; positive pivots
    reduce the question to the remaining Schur complement. No tolerance.
    """
    a = _matrix(value, size)
    if a != _transpose(a) or _trace(a) != 1:
        raise QuantumInstrumentError("a density must be symmetric with trace one")
    work = [list(row) for row in a]
    for k in range(size):
        pivot = work[k][k]
        if pivot < 0:
            raise QuantumInstrumentError("density is not positive semidefinite")
        if pivot == 0:
            if any(work[k][j] != 0 for j in range(k+1, size)):
                raise QuantumInstrumentError("zero PSD diagonal requires a zero residual row")
            continue
        for i in range(k+1, size):
            for j in range(k+1, size):
                work[i][j] -= work[i][k]*work[k][j]/pivot
    return a


def validate_density(value) -> Matrix:
    """Validate a two- or four-dimensional real rational density matrix."""
    if not isinstance(value, (tuple, list)) or len(value) not in (2, 4):
        raise QuantumInstrumentError("only qubit and two-qubit densities are supported")
    return _density(value, len(value))


def qubit_state(x: int | Q, z: int | Q) -> Matrix:
    """(I+xX+zZ)/2, with x^2+z^2<=1 in the real-qubit disk."""
    x, z = _rational(x), _rational(z)
    if x*x+z*z > 1:
        raise QuantumInstrumentError("Bloch coordinates lie outside the unit disk")
    return ((Q(1, 2)*(1+z), x/2), (x/2, Q(1, 2)*(1-z)))


def tensor_state(alice, bob) -> Matrix:
    """Product state in basis |00>, |01>, |10>, |11>."""
    return _tensor(_density(alice, 2), _density(bob, 2))


def coherence_state(coherence: int | Q) -> Matrix:
    """rho(c): diagonal 00,11=1/2; coherence 00,11=11,00=c/2."""
    c = _rational(coherence)
    if not -1 <= c <= 1:
        raise QuantumInstrumentError("coherence must lie in [-1,1]")
    return ((Q(1, 2), Q(), Q(), c/2),
            (Q(), Q(), Q(), Q()),
            (Q(), Q(), Q(), Q()),
            (c/2, Q(), Q(), Q(1, 2)))


def _side(side: str) -> str:
    if side not in ("alice", "bob"):
        raise QuantumInstrumentError("side must be 'alice' or 'bob'")
    return side


def partial_trace(state, keep: str = "bob") -> Matrix:
    """Reduced density of the named retained qubit."""
    rho = _density(state, 4)
    keep = _side(keep)
    if keep == "alice":
        result = tuple(tuple(sum((rho[2*i+b][2*j+b] for b in range(2)), Q())
                             for j in range(2)) for i in range(2))
    else:
        result = tuple(tuple(sum((rho[2*a+i][2*a+j] for a in range(2)), Q())
                             for j in range(2)) for i in range(2))
    return _density(result, 2)


def _observable(value) -> Matrix:
    observable = _matrix(value, 2)
    if observable != _transpose(observable):
        raise QuantumInstrumentError("real observable must be symmetric")
    return observable


def bipartite_expectation(state, alice_observable, bob_observable) -> Q:
    rho = _density(state, 4)
    operator = _tensor(_observable(alice_observable), _observable(bob_observable))
    return _trace(_multiply(rho, operator))


def two_axis_score(state) -> Q:
    """|<XX>|+|<ZZ>|; >1 certifies entanglement for trusted qubit axes.

    A score <=1 is inconclusive for general states. This is not a
    device-independent Bell inequality.
    """
    rho = _density(state, 4)
    return sum((abs(_trace(_multiply(rho, _tensor(axis, axis))))
                for axis in (X, Z)), Q())


@dataclass(frozen=True)
class LocalOutcome:
    """Returned branch; posterior is normalized, or None if probability zero."""

    label: str
    probability: Q
    posterior: Matrix | None


def apply_local_instrument(state, instrument: Instrument,
                           side: str = "alice") -> tuple[LocalOutcome, ...]:
    """Apply a complete inherited qubit instrument to one local factor."""
    rho = _density(state, 4)
    side = _side(side)
    if not isinstance(instrument, Instrument) or len(instrument.outcomes) > MAX_OUTCOMES:
        raise QuantumInstrumentError("require a complete instrument with at most 16 outcomes")
    outcomes = []
    for label, kraus in instrument.outcomes:
        local = _matrix(kraus, 2)
        operator = _tensor(local, I) if side == "alice" else _tensor(I, local)
        numerator = _multiply(_multiply(operator, rho), _transpose(operator))
        probability = _trace(numerator)
        if probability < 0:
            raise ArithmeticError("validated positive instrument produced negative probability")
        posterior = None if probability == 0 else _density(_scale(numerator, 1/probability), 4)
        outcomes.append(LocalOutcome(label, probability, posterior))
    if sum((o.probability for o in outcomes), Q()) != 1:
        raise ArithmeticError("complete instrument did not preserve total probability")
    return tuple(outcomes)


def discard_local_outcomes(state, instrument: Instrument, side: str = "alice") -> Matrix:
    """Outcome-forgotten density: sum_o p_o rho_o, never an unweighted mean."""
    result = tuple(tuple(Q() for _ in range(4)) for _ in range(4))
    for branch in apply_local_instrument(state, instrument, side):
        if branch.posterior is not None:
            result = _add(result, _scale(branch.posterior, branch.probability))
    return _density(result, 4)


def postselect_local_outcome(state, instrument: Instrument, label: str,
                            side: str = "alice") -> LocalOutcome:
    """Return an existing positive-probability branch, including its weight."""
    for branch in apply_local_instrument(state, instrument, side):
        if branch.label == label:
            if branch.probability == 0:
                raise QuantumInstrumentError("cannot observe a zero-probability outcome")
            return branch
    raise QuantumInstrumentError("unknown instrument outcome")


def xz_observable(x: int | Q, z: int | Q) -> Matrix:
    """Unit, trusted real-qubit axis xX+zZ, with eigenvalues +/-1."""
    x, z = _rational(x), _rational(z)
    if x*x+z*z != 1:
        raise QuantumInstrumentError("a projective XZ axis must have exact unit length")
    return ((z, x), (x, -z))


def xz_projectors(x: int | Q, z: int | Q) -> tuple[Matrix, Matrix]:
    """Plus and minus rank-one projectors for the declared unit axis."""
    operator = xz_observable(x, z)
    return (_scale(_add(I, operator), Q(1, 2)),
            _scale(_add(I, _scale(operator, Q(-1))), Q(1, 2)))


def _axis(value) -> Axis:
    if not isinstance(value, (tuple, list)) or len(value) != 2:
        raise QuantumInstrumentError("axis requires exactly the (X,Z) coefficients")
    x, z = _rational(value[0]), _rational(value[1])
    xz_observable(x, z)
    return x, z


def joint_axis_probabilities(state, alice_axis: Axis, bob_axis: Axis) -> dict[tuple[int, int], Q]:
    """Exact joint +/-1 outcome probabilities for local projective axes."""
    rho = _density(state, 4)
    alice = xz_projectors(*_axis(alice_axis))
    bob = xz_projectors(*_axis(bob_axis))
    result = {(a, b): _trace(_multiply(rho, _tensor(alice[i], bob[j])))
              for i, a in enumerate((1, -1)) for j, b in enumerate((1, -1))}
    if min(result.values()) < 0 or sum(result.values(), Q()) != 1:
        raise ArithmeticError("invalid projective outcome probabilities")
    return result


def chsh_value(state, alice_axes=DEFAULT_ALICE_AXES,
               bob_axes=DEFAULT_BOB_AXES) -> Q:
    """E00+E01+E10-E11 for two specified unit axes at each wing.

    The defaults give (8+6c)/5 on rho(c). The local-hidden-variable bound
    is 2 in absolute value under the stated Bell assumptions.
    """
    rho = _density(state, 4)
    if any(not isinstance(axes, (tuple, list)) or len(axes) != 2
           for axes in (alice_axes, bob_axes)):
        raise QuantumInstrumentError("CHSH requires two axes on each wing")
    aa = tuple(xz_observable(*_axis(a)) for a in alice_axes)
    bb = tuple(xz_observable(*_axis(b)) for b in bob_axes)
    correlations = [[_trace(_multiply(rho, _tensor(a, b))) for b in bb] for a in aa]
    return correlations[0][0]+correlations[0][1]+correlations[1][0]-correlations[1][1]


def shared_sign_probabilities(alice_axis: str, bob_axis: str) -> dict[tuple[int, int], Q]:
    """Classical control reproducing Bell rho(1)'s restricted X/Z data.

    Share independent uniform signs lambda_X and lambda_Z; each side
    reports the sign for its chosen setting. These simultaneous local
    assignments are not trusted qubit states.
    """
    if alice_axis not in ("X", "Z") or bob_axis not in ("X", "Z"):
        raise QuantumInstrumentError("this classical control has only X and Z settings")
    result = {(a, b): Q() for a in (1, -1) for b in (1, -1)}
    for x in (1, -1):
        for z in (1, -1):
            hidden = {"X": x, "Z": z}
            result[hidden[alice_axis], hidden[bob_axis]] += Q(1, 4)
    return result
