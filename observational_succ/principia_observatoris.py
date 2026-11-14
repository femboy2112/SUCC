"""Exact finite linear instruments for Principia Observatoris.

Rational model certificates only: no empirical source authentication, spectral
norm approximation, physical sampling, or arithmetic cancellation oracle.
Words are chronological: (a,b) acts by A_b A_a. The proofs are in
docs/principia_observatoris; classical linear realization is the antecedent.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q


class ContractError(ValueError):
    """Malformed or inexact input to the declared rational model."""


def rational(value):
    if type(value) not in (int, Q):
        raise ContractError("Exact int/Fraction required; floats and bools rejected")
    return Q(value)


def matrix(rows):
    result = tuple(tuple(rational(x) for x in row) for row in rows)
    if not result or not result[0] or any(len(r) != len(result[0]) for r in result):
        raise ContractError("Nonempty rectangular matrix required")
    return result


def transpose(a):
    a = matrix(a)
    return tuple(zip(*a))


def identity(n):
    if type(n) is not int or n < 1:
        raise ContractError("Positive dimension required")
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def multiply(a, b):
    a, b = matrix(a), matrix(b)
    if len(a[0]) != len(b):
        raise ContractError("Matrix product shape mismatch")
    return tuple(tuple(sum((x*y for x, y in zip(row, col)), Q())
                       for col in zip(*b)) for row in a)


def subtract(a, b):
    a, b = matrix(a), matrix(b)
    if (len(a), len(a[0])) != (len(b), len(b[0])):
        raise ContractError("Matrix difference shape mismatch")
    return tuple(tuple(x-y for x, y in zip(r, s)) for r, s in zip(a, b))


def row_basis(rows):
    """Canonical reduced row basis; empty input/output represents the zero span."""
    rows = tuple(tuple(rational(x) for x in r) for r in rows)
    if not rows:
        return ()
    if not rows[0] or any(len(r) != len(rows[0]) for r in rows):
        raise ContractError("Ragged or zero-width rows")
    work = [list(r) for r in rows]
    lead = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(lead, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[lead], work[pivot] = work[pivot], work[lead]
        scale = work[lead][col]
        work[lead] = [x/scale for x in work[lead]]
        for i in range(len(work)):
            if i != lead:
                scale = work[i][col]
                work[i] = [x-scale*y for x, y in zip(work[i], work[lead])]
        lead += 1
        if lead == len(work):
            break
    return tuple(tuple(r) for r in work[:lead])


def inverse(a):
    a = matrix(a)
    n = len(a)
    if len(a[0]) != n:
        raise ContractError("Square inverse required")
    augmented = row_basis(tuple(a[i] + identity(n)[i] for i in range(n)))
    if tuple(r[:n] for r in augmented) != identity(n):
        raise ContractError("Singular matrix")
    return tuple(r[n:] for r in augmented)


def right_inverse(p):
    """Euclidean Moore-Penrose right inverse for a full-row-rank P."""
    p = matrix(p)
    if len(row_basis(p)) != len(p):
        raise ContractError("Observer must be surjective onto its stated codomain")
    pt = transpose(p)
    return multiply(pt, inverse(multiply(p, pt)))


def _actions(actions, n):
    actions = tuple(matrix(a) for a in actions)
    if any(len(a) != n or len(a[0]) != n for a in actions):
        raise ContractError("Each action must be square on the carrier")
    return actions


@dataclass(frozen=True)
class LinearModel:
    """Authenticated-by-caller source label and rational switched realization.

    B supplies initial columns/preparations; C reads final outputs. No reset
    capability follows from the existence of multiple columns or words.
    """
    source: str
    actions: tuple
    initial: tuple
    readout: tuple

    def __post_init__(self):
        if not isinstance(self.source, str) or not self.source.strip():
            raise ContractError("Nonempty source label required")
        b, c = matrix(self.initial), matrix(self.readout)
        n = len(b)
        if len(c[0]) != n:
            raise ContractError("Readout dimension mismatch")
        object.__setattr__(self, "initial", b)
        object.__setattr__(self, "readout", c)
        object.__setattr__(self, "actions", _actions(self.actions, n))

    def response(self, word):
        value = self.initial
        for letter in word:
            if type(letter) is not int or not 0 <= letter < len(self.actions):
                raise ContractError("Unknown action letter")
            value = multiply(self.actions[letter], value)
        return multiply(self.readout, value)


def _nonzero(a):
    return any(x for r in a for x in r)


def linear_separator(model):
    """Return a shortest nonzero word response, or an invariant-span certificate.

    Basis vectors retain original preparation/word provenance; no fitted rank
    is treated as a promise about an external source. Rational span closure is
    checked on the actual supplied finite matrices.
    """
    if not isinstance(model, LinearModel):
        raise ContractError("LinearModel required")
    columns = transpose(model.initial)
    basis, provenance, pending = [], [], []
    for j, col in enumerate(columns):
        if len(row_basis(basis + [col])) > len(basis):
            basis.append(col)
            provenance.append(((), j))
            pending.append(len(basis)-1)
    initial_rank = len(basis)
    cursor = 0
    while cursor < len(pending):
        index = pending[cursor]
        cursor += 1
        vector = tuple((x,) for x in basis[index])
        word, preparation = provenance[index]
        if _nonzero(multiply(model.readout, vector)):
            return {"status": "DISTINGUISHED", "word": word,
                    "preparation": preparation, "response": model.response(word),
                    "initial_rank": initial_rank}
        for letter, action in enumerate(model.actions):
            col = tuple(r[0] for r in multiply(action, vector))
            if len(row_basis(basis + [col])) > len(basis):
                basis.append(col)
                provenance.append((word + (letter,), preparation))
                pending.append(len(basis)-1)
    return {"status": "ZERO_ON_ALL_WORDS", "basis": tuple(basis),
            "basis_provenance": tuple(provenance), "initial_rank": initial_rank,
            "reachable_rank": len(basis),
            "horizon_bound": max(0, len(basis)-initial_rank)}


def difference_model(left, right):
    """Direct-sum comparison with a common ordered action/output contract."""
    if (len(left.actions) != len(right.actions)
            or len(left.initial[0]) != len(right.initial[0])
            or len(left.readout) != len(right.readout)):
        raise ContractError("Common action, preparation and output alphabets required")
    n, m = len(left.initial), len(right.initial)
    actions = []
    for a, b in zip(left.actions, right.actions):
        actions.append(tuple(r + (Q(),)*m for r in a)
                       + tuple((Q(),)*n + r for r in b))
    return LinearModel(left.source + " versus " + right.source, tuple(actions),
                       left.initial + right.initial,
                       tuple(a + tuple(-x for x in b)
                             for a, b in zip(left.readout, right.readout)))


def predictive_completion(p, actions):
    """Smallest invariant row space containing P; not an access policy."""
    p = matrix(p)
    actions = _actions(actions, len(p[0]))
    basis = row_basis(p)
    ranks = [len(basis)]
    while basis:
        extended = row_basis(basis + tuple(r for a in actions
                                          for r in multiply(basis, a)))
        if len(extended) == len(basis):
            break
        basis = extended
        ranks.append(len(basis))
    descended = ()
    if basis:
        pinv = right_inverse(basis)
        descended = tuple(multiply(multiply(basis, a), pinv) for a in actions)
        if any(_nonzero(subtract(multiply(basis, a), multiply(b, basis)))
               for a, b in zip(actions, descended)):
            raise AssertionError("Internal closure certificate failed")
    return {"basis": basis, "ranks": tuple(ranks), "actions": descended,
            "added_coordinates": len(basis)-len(row_basis(p)),
            "closure_depth": len(ranks)-1}


def quotient_defect(p, a):
    """Optimal Euclidean linear predictor and exact residual, without norm numerics.

    ||residual|| is also the minimax error over ALL predictors on the unit ball.
    The manuscript proves that universal assertion; this function computes the
    rational matrix attaining its upper bound, and exact vanishing only.
    """
    p = matrix(p)
    a, = _actions((a,), len(p[0]))
    dagger = right_inverse(p)
    hidden = subtract(identity(len(a)), multiply(dagger, p))
    b = multiply(multiply(p, a), dagger)
    defect = subtract(multiply(p, a), multiply(b, p))
    if defect != multiply(multiply(p, a), hidden):
        raise AssertionError("Defect identity failed")
    return {"predictor": b, "hidden_projector": hidden, "defect": defect,
            "descends": not _nonzero(defect)}


def word_matrix(actions, word, dimension):
    actions = _actions(actions, dimension)
    result = identity(dimension)
    for letter in word:
        if type(letter) is not int or not 0 <= letter < len(actions):
            raise ContractError("Unknown action letter")
        result = multiply(actions[letter], result)
    return result


def word_defect(p, source_actions, model_actions, word):
    """Compute both sides of the exact ordered telescoping identity."""
    p = matrix(p)
    n, m = len(p[0]), len(p)
    source_actions, model_actions = _actions(source_actions, n), _actions(model_actions, m)
    if len(source_actions) != len(model_actions):
        raise ContractError("Same action alphabet required")
    word = tuple(word)
    source = word_matrix(source_actions, word, n)
    model = word_matrix(model_actions, word, m)
    direct = subtract(multiply(p, source), multiply(model, p))
    terms = []
    for j, letter in enumerate(word):
        e = subtract(multiply(p, source_actions[letter]), multiply(model_actions[letter], p))
        terms.append(multiply(multiply(word_matrix(model_actions, word[j+1:], m), e),
                              word_matrix(source_actions, word[:j], n)))
    total = tuple(tuple(sum((t[i][j] for t in terms), Q()) for j in range(n))
                  for i in range(m))
    return {"direct": direct, "telescoped": total, "terms": tuple(terms)}


def bbp_forcing(n):
    """Original four-pole forcing; indexing begins at one."""
    if type(n) is not int or n < 1:
        raise ContractError("BBP index starts at one")
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def bbp_hankel_ldl(start, size):
    """Exact finite positive-pivot receipt, not the all-rank analytic proof."""
    if type(start) is not int or start < 1:
        raise ContractError("BBP start is a positive integer")
    if type(size) is not int or size < 1:
        raise ContractError("Positive Hankel size required")
    h = matrix([[bbp_forcing(start+i+j) for j in range(size)] for i in range(size)])
    l = [[Q(int(i == j)) for j in range(size)] for i in range(size)]
    diagonal = []
    for j in range(size):
        d = h[j][j]-sum((l[j][k]**2*diagonal[k] for k in range(j)), Q())
        if d <= 0:
            raise ContractError("Nonpositive pivot; no positive certificate")
        diagonal.append(d)
        for i in range(j+1, size):
            l[i][j] = (h[i][j]-sum((l[i][k]*l[j][k]*diagonal[k]
                                   for k in range(j)), Q()))/d
    return {"matrix": h, "lower": matrix(l), "diagonal": tuple(diagonal)}


def bbp_rank_predictor(start, dimension):
    """Fit exactly 2d authentic forcing values, certify the next positive error.

    Returns a rational order-d recurrence (a d-dimensional stationary linear
    realization). This is an exact sharp finite discrimination instrument,
    never a BBP signed-cancellation estimate.
    """
    if type(dimension) is not int or dimension < 1:
        raise ContractError("Positive integer realization dimension required")
    certificate = bbp_hankel_ldl(start, dimension+1)
    d = dimension
    h = certificate["matrix"]
    head = tuple(tuple(row[:d]) for row in h[:d])
    rhs = tuple((-h[i][d],) for i in range(d))
    coefficients = tuple(row[0] for row in multiply(inverse(head), rhs))
    a = matrix([tuple(Q(int(j == i+1)) for j in range(d)) for i in range(d-1)]
               + [tuple(-c for c in coefficients)])
    model = LinearModel("fitted-bbp-forcing", (a,),
                        tuple((bbp_forcing(start+j),) for j in range(d)),
                        (tuple(Q(int(j == 0)) for j in range(d)),))
    error = bbp_forcing(start+2*d)-model.response((0,)*(2*d))[0][0]
    if error != certificate["diagonal"][-1] or error <= 0:
        raise AssertionError("Hankel next-error certificate failed")
    return {"model": model, "coefficients": coefficients,
            "matched_count": 2*d, "first_disagreement_index": 2*d,
            "next_error": error}


def bbp_rank_error_bound(start, dimension):
    """Positive rational lower bound on any rank-d model's 2d+1-value error.

    The bound applies to stationary linear realizations of dimension at most d,
    with arbitrary real coefficients, not just the rational fitted model.
    """
    if type(dimension) is not int or dimension < 1:
        raise ContractError("Positive integer realization dimension required")
    h = bbp_hankel_ldl(start, dimension+1)["matrix"]
    h_inverse = inverse(h)
    inverse_norm = max(sum(abs(x) for x in row) for row in h_inverse)
    return Q(1) / ((dimension+1)*inverse_norm)
