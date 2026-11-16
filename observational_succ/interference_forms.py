"""Finite, source-labelled interference forms with exact rational coefficients.

The matrix convention is z* H z (conjugate-linear in the first slot).
Rows act as sum a_j z_j; their Gram is conjugate(a_i)*a_j.  This differs
from the linear-first convention of collective_spectral.HermitianForm;
only that module's strict Gaussian arithmetic is reused here.

SourceCharacter computes turns from the inherited, original zero-seeded
BBP recurrence.  A generic source character is NOT Gaussian rational.
Exact fixture evaluation is explicitly separate from source phase access;
no supplied fixture is authenticated merely by carrying source labels.
Only genuine quarter turns can be converted to exact Gaussian phases.

Normalized intensity coins are a declared mathematical instrument.  The
sampling budget assumes fresh independent trials, the specified selection
law and access to the selected source response.  It supplies neither free
phase access nor a signed asymptotic estimate.  Proofs and scope are in
research/2026-11-15/pi_interference_atlas/CONSTRUCTOR_NOTES.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product

from .bbp_binwindow_conjugacy import authentic_state
from .collective_spectral import Gaussian


MAX_CHANNELS = 32
MAX_TERMS = 4096
MAX_SOURCE_FACTORS = 32
MAX_TENSOR_FACTORS = 8
MAX_SOURCE_CLOCK = 512
MAX_HARMONIC = 1_000_000

ZERO = Gaussian()
ONE = Gaussian(1)
I = Gaussian(0, 1)


def _integer(value, name, minimum=None, maximum=None):
    if type(value) is not int:
        raise ValueError(f"{name} must be an exact integer, not bool or float")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} is below its declared domain")
    if maximum is not None and value > maximum:
        raise ValueError(f"{name} exceeds its declared budget")
    return value


def _rational(value, name="coefficient", nonnegative=False):
    if type(value) not in (int, Q):
        raise ValueError(f"{name} must be an exact int/Fraction")
    value = Q(value)
    if nonnegative and value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def _gaussian(value):
    if type(value) is Gaussian:
        return Gaussian(_rational(value.real), _rational(value.imag))
    return Gaussian(_rational(value))


def _sequence(values, name, maximum, minimum=0):
    if type(values) not in (tuple, list) or not minimum <= len(values) <= maximum:
        raise ValueError(f"{name} must be a finite tuple/list within its size budget")
    return tuple(values)


def _norm_squared(value):
    return value.real ** 2 + value.imag ** 2


def _coefficient_bound(value):
    """Rational upper bound on modulus, avoiding square roots."""
    return abs(value.real) + abs(value.imag)


def _ceil(value):
    return -((-value.numerator) // value.denominator)


@lru_cache(maxsize=128)
def _state(clock):
    return authentic_state(clock)


@dataclass(frozen=True)
class SourceCharacter:
    """e(reference_turns + sum h_n U_n), with the literal U_0=0 source.

    Empty powers give a declared phase reference.  Factors are combined by
    source clock, not treated as independent random variables.  Source time
    zero is retained as a label even though its state is identically zero.
    No completed Y, digit/carry or prime-clock label is accepted here.
    """
    powers: tuple = ()
    reference_turns: Q = Q()

    def __post_init__(self):
        factors = _sequence(self.powers, "source factors", MAX_SOURCE_FACTORS)
        combined = {}
        for factor in factors:
            pair = _sequence(factor, "(clock, harmonic)", 2, 2)
            clock = _integer(pair[0], "source clock", 0, MAX_SOURCE_CLOCK)
            harmonic = _integer(pair[1], "source harmonic", -MAX_HARMONIC, MAX_HARMONIC)
            combined[clock] = combined.get(clock, 0) + harmonic
        for harmonic in combined.values():
            _integer(harmonic, "combined source harmonic", -MAX_HARMONIC, MAX_HARMONIC)
        object.__setattr__(self, "powers", tuple(sorted(
            (clock, harmonic) for clock, harmonic in combined.items() if harmonic)))
        object.__setattr__(self, "reference_turns", _rational(self.reference_turns) % 1)

    def exact_turns(self):
        """Exact rational turns, with no trigonometric approximation."""
        return self.reference_turns + sum(
            (harmonic * _state(clock) for clock, harmonic in self.powers), Q())

    def conjugate(self):
        return SourceCharacter(tuple((n, -h) for n, h in self.powers), -self.reference_turns)

    def multiply(self, other):
        if type(other) is not SourceCharacter:
            raise ValueError("a source character is required")
        combined = dict(self.powers)
        for clock, harmonic in other.powers:
            combined[clock] = combined.get(clock, 0) + harmonic
        factors = tuple((clock, harmonic) for clock, harmonic in combined.items() if harmonic)
        return SourceCharacter(factors, self.reference_turns + other.reference_turns)

    def power(self, exponent):
        exponent = _integer(exponent, "tensor exponent", -MAX_HARMONIC, MAX_HARMONIC)
        return SourceCharacter(tuple((n, exponent * h) for n, h in self.powers),
                               exponent * self.reference_turns)

    def quarter_turn_value(self):
        """Exact phase conversion only if the authentic turns are quarters."""
        index = 4 * (self.exact_turns() % 1)
        if index.denominator != 1:
            raise ValueError("authentic phase is not a Gaussian-rational quarter turn")
        return (ONE, I, -ONE, -I)[index.numerator]


def source_character(clock, harmonic=1):
    return SourceCharacter(((clock, harmonic),))


def reference_character(turns=0):
    return SourceCharacter((), turns)


def _channels(channels):
    channels = _sequence(channels, "channels", MAX_CHANNELS, 1)
    if any(type(channel) is not SourceCharacter for channel in channels):
        raise ValueError("channels must retain SourceCharacter labels")
    return channels


def authentic_turns(channels):
    return tuple(channel.exact_turns() for channel in _channels(channels))


def tensor_channels(*families):
    """Joint character products, requiring joint access; not independence.

    The Cartesian order is explicit.  This budgeted primitive supports
    finite higher interactions without asserting a product sampling law.
    """
    families = _sequence(families, "tensor factors", MAX_TENSOR_FACTORS, 1)
    families = tuple(_channels(family) for family in families)
    size = 1
    for family in families:
        size *= len(family)
        if size > MAX_CHANNELS:
            raise ValueError("tensor channel count exceeds budget")
    result = []
    for factors in product(*families):
        channel = reference_character()
        for factor in factors:
            channel = channel.multiply(factor)
        result.append(channel)
    return tuple(result)


def _fixture(values, size):
    values = tuple(_gaussian(value) for value in
                   _sequence(values, "exact fixture", MAX_CHANNELS, 1))
    if len(values) != size:
        raise ValueError("one exact fixture value is required per labelled channel")
    if any(_norm_squared(value) > 1 for value in values):
        raise ValueError("normalized fixture values must lie in the unit disk")
    return values


def _row(values, size):
    values = tuple(_gaussian(value) for value in
                   _sequence(values, "row", MAX_CHANNELS, 1))
    if len(values) != size:
        raise ValueError("row dimension differs from channel dimension")
    return values


def _weights(weights, size):
    if weights is None:
        return (Q(1, size),) * size
    weights = tuple(_rational(value, "probability weight", True) for value in
                    _sequence(weights, "weights", MAX_CHANNELS, 1))
    if len(weights) != size or sum(weights) != 1:
        raise ValueError("one nonnegative weight per channel must sum to one")
    return weights


@dataclass(frozen=True)
class IntensityTerm:
    """weight * |row dot z|^2 with sum(|Re row|+|Im row|)<=1."""
    weight: Q
    row: tuple

    def __post_init__(self):
        weight = _rational(self.weight)
        row = tuple(_gaussian(value) for value in
                    _sequence(self.row, "intensity row", MAX_CHANNELS, 1))
        if not weight or not any(_norm_squared(value) for value in row):
            raise ValueError("omit zero-weight and zero-row measurements")
        if sum((_coefficient_bound(value) for value in row), Q()) > 1:
            raise ValueError("intensity row is not normalized to the unit bound")
        object.__setattr__(self, "weight", weight)
        object.__setattr__(self, "row", row)


@dataclass(frozen=True)
class IntensityProgram:
    channels: tuple
    terms: tuple = ()

    def __post_init__(self):
        channels = _channels(self.channels)
        terms = _sequence(self.terms, "signed intensity terms", MAX_TERMS)
        if any(type(term) is not IntensityTerm or len(term.row) != len(channels)
               for term in terms):
            raise ValueError("typed intensity terms must use the labelled channel dimension")
        object.__setattr__(self, "channels", channels)
        object.__setattr__(self, "terms", terms)

    @property
    def measurement_mass(self):
        return sum((abs(term.weight) for term in self.terms), Q())

    @property
    def sampling_probabilities(self):
        mass = self.measurement_mass
        return tuple(abs(term.weight) / mass for term in self.terms)

    def intensities_fixture(self, values):
        values = _fixture(values, len(self.channels))
        return tuple(_norm_squared(sum((a * z for a, z in zip(term.row, values)), ZERO))
                     for term in self.terms)

    def evaluate_fixture(self, values):
        return sum((term.weight * intensity for term, intensity in
                    zip(self.terms, self.intensities_fixture(values))), Q())

    def score(self, term_index, outcome):
        """Single selected-row Bernoulli score, not an executed random trial."""
        term_index = _integer(term_index, "term index", 0, len(self.terms) - 1)
        outcome = _integer(outcome, "Bernoulli outcome", 0, 1)
        sign = 1 if self.terms[term_index].weight > 0 else -1
        return sign * self.measurement_mass * outcome

    def independent_trial_budget(self, error, failure_probability):
        """Exact sufficient Hoeffding budget, using log(2/delta)<=ceil(log2(2/delta)).

        Independent fresh selection and correct intensity responses are
        hypotheses.  The potentially large returned integer is a resource
        count, not an allocation or a claim that these trials were executed.
        """
        error = _rational(error, "absolute error", True)
        delta = _rational(failure_probability, "failure probability", True)
        if error == 0 or not 0 < delta < 1:
            raise ValueError("require error>0 and 0<failure_probability<1")
        mass = self.measurement_mass
        if not mass:
            return 0
        ratio = 2 / delta
        exponent = max(0, ratio.numerator.bit_length() - ratio.denominator.bit_length())
        if Q(2 ** exponent) < ratio:
            exponent += 1
        return _ceil(2 * mass ** 2 * exponent / error ** 2)

    def intensity_noise_bound(self, error):
        return self.measurement_mass * _rational(error, "intensity error", True)

    def phase_error_pi_units(self, turn_errors):
        """Multiply by pi for a bound under coordinate turn errors.

        Both true and perturbed coordinates must be unit phases; the bound
        includes any reference error and does not assume independent noise.
        For a product character its turn error must first include every
        factor and harmonic.  These are error bounds, not source estimates.
        """
        errors = tuple(_rational(value, "turn error", True) for value in
                       _sequence(turn_errors, "turn errors", MAX_CHANNELS, 1))
        if len(errors) != len(self.channels):
            raise ValueError("one turn-error bound is required per channel")
        return 4 * sum((abs(term.weight) * sum(
            (_coefficient_bound(a) * error for a, error in zip(term.row, errors)), Q())
            for term in self.terms), Q())

    def as_form(self):
        size = len(self.channels)
        matrix = tuple(tuple(sum((term.weight * term.row[i].conjugate() * term.row[j]
                                  for term in self.terms), ZERO)
                             for j in range(size)) for i in range(size))
        return HermitianResponse(self.channels, matrix)


@dataclass(frozen=True)
class HermitianResponse:
    """z* H z with a declared ordered tuple of source/reference characters."""
    channels: tuple
    matrix: tuple

    def __post_init__(self):
        channels = _channels(self.channels)
        size = len(channels)
        matrix = tuple(_row(row, size) for row in
                       _sequence(self.matrix, "matrix", MAX_CHANNELS, 1))
        if len(matrix) != size or any(matrix[i][j] != matrix[j][i].conjugate()
                                      for i in range(size) for j in range(size)):
            raise ValueError("a square Hermitian matrix in the channel order is required")
        object.__setattr__(self, "channels", channels)
        object.__setattr__(self, "matrix", matrix)

    def evaluate_fixture(self, values):
        values = _fixture(values, len(self.channels))
        result = sum((values[i].conjugate() * coefficient * values[j]
                      for i, row in enumerate(self.matrix)
                      for j, coefficient in enumerate(row)), ZERO)
        if result.imag:
            raise ArithmeticError("Hermitian response lost its real-valued identity")
        return result.real

    def compile(self):
        """Exact signed polarization with at most 2*d*d-d normalized rows.

        For H_ij=a+ib, the pair contributes a/2 times the +/- difference
        and b/2 times the +/-i difference of UNnormalized intensities.
        Normalizing those rows by 2 changes their weights to +/-2a, +/-2b.
        No eigendecomposition, positivity assumption or square root is used.
        """
        size = len(self.channels)
        terms = []
        for i in range(size):
            diagonal = self.matrix[i][i].real
            if diagonal:
                row = [ZERO] * size
                row[i] = ONE
                terms.append(IntensityTerm(diagonal, tuple(row)))
            for j in range(i + 1, size):
                entry = self.matrix[i][j]
                for coefficient, direction in ((entry.real, ONE), (entry.imag, I)):
                    if coefficient:
                        for sign in (1, -1):
                            row = [ZERO] * size
                            row[i], row[j] = Gaussian(Q(1, 2)), direction * Q(sign, 2)
                            terms.append(IntensityTerm(2 * sign * coefficient, tuple(row)))
        return IntensityProgram(self.channels, tuple(terms))


def linear_response_forms(channels, coefficients, reference=None):
    """Re/Im of conjugate(reference) * sum coefficients[j]*z_j.

    The returned ordered channels start with the explicit phase reference.
    The default is the declared reference e(0)=1, not an unknown target.
    """
    channels = _channels(channels)
    coefficients = _row(coefficients, len(channels))
    if reference is None:
        reference = reference_character()
    if type(reference) is not SourceCharacter:
        raise ValueError("declare the reference as a SourceCharacter")
    all_channels = _channels((reference,) + channels)
    size = len(all_channels)
    forms = []
    for direction in (ONE, -I):
        matrix = [[ZERO] * size for _ in range(size)]
        for j, coefficient in enumerate(coefficients, 1):
            matrix[0][j] = direction * coefficient * Q(1, 2)
            matrix[j][0] = matrix[0][j].conjugate()
        forms.append(HermitianResponse(all_channels, tuple(tuple(row) for row in matrix)))
    return tuple(forms)


def complex_quadratic_forms(channels, matrix):
    """Re/Im of z* K z for an arbitrary exact complex matrix K.

    Each returned Hermitian form has its own signed intensity compiler.
    This is sesquilinear quadratic algebra; z_i*z_j without conjugation
    requires the explicitly declared product-character lift instead.
    """
    channels = _channels(channels)
    size = len(channels)
    matrix = tuple(_row(row, size) for row in
                   _sequence(matrix, "complex matrix", MAX_CHANNELS, 1))
    if len(matrix) != size:
        raise ValueError("complex quadratic matrix must be square")
    real_part = tuple(tuple((matrix[i][j] + matrix[j][i].conjugate()) * Q(1, 2)
                            for j in range(size)) for i in range(size))
    imag_part = tuple(tuple((matrix[i][j] - matrix[j][i].conjugate()) * (-I) * Q(1, 2)
                            for j in range(size)) for i in range(size))
    return HermitianResponse(channels, real_part), HermitianResponse(channels, imag_part)


def weighted_mean_energy_program(channels, weights=None):
    """|sum w_j z_j|^2, with a declared probability weighting."""
    channels = _channels(channels)
    weights = _weights(weights, len(channels))
    return IntensityProgram(channels, (IntensityTerm(1, weights),))


def reference_escape_program(channels, weights=None, reference=None):
    """For unit phases: sum w_j(1-Re(conj(reference)*z_j)).

    The exact polynomial is one half the weighted squared distance to the
    reference, implemented with positive, two-channel rows and mass 2.
    """
    channels = _channels(channels)
    weights = _weights(weights, len(channels))
    if reference is None:
        reference = reference_character()
    all_channels = _channels((reference,) + channels)
    terms = []
    for j, weight in enumerate(weights, 1):
        if weight:
            row = [ZERO] * len(all_channels)
            row[0], row[j] = Gaussian(Q(1, 2)), Gaussian(Q(-1, 2))
            terms.append(IntensityTerm(2 * weight, tuple(row)))
    return IntensityProgram(all_channels, tuple(terms))


def pair_dispersion_program(channels, weights=None):
    """For unit phases: 1-|sum w_j z_j|^2, with no phase reference.

    For general disk fixtures this is sum w_j|z_j|^2-|sum w_jz_j|^2.
    Independent index draws with replacement are an alternative realization;
    copied/same-index draws are not that experiment.
    """
    channels = _channels(channels)
    weights = _weights(weights, len(channels))
    terms = []
    for i in range(len(channels)):
        for j in range(i + 1, len(channels)):
            weight = 4 * weights[i] * weights[j]
            if weight:
                row = [ZERO] * len(channels)
                row[i], row[j] = Gaussian(Q(1, 2)), Gaussian(Q(-1, 2))
                terms.append(IntensityTerm(weight, tuple(row)))
    return IntensityProgram(channels, tuple(terms))


def fourier_purity_program(base_channels, width, weights=None):
    """2*sum_(h=1..width-1)(width-h)*|sum w_n z_n**h|^2.

    This equals tr(A^2)-width for A=sum w_n v_n v_n*,
    v_n=(1,z_n,...,z_n**(width-1)), when all base phases have modulus one.
    Exact source products retain the harmonic h; width and clock count
    must fit the finite channel budget.  No growing-window saving follows.
    """
    base_channels = _channels(base_channels)
    width = _integer(width, "Fourier width", 2, MAX_CHANNELS + 1)
    weights = _weights(weights, len(base_channels))
    if len(base_channels) * (width - 1) > MAX_CHANNELS:
        raise ValueError("purity lift exceeds the channel budget")
    channels = tuple(channel.power(h) for h in range(1, width) for channel in base_channels)
    terms = []
    for h in range(1, width):
        row = [ZERO] * len(channels)
        for j, weight in enumerate(weights):
            row[(h - 1) * len(base_channels) + j] = Gaussian(weight)
        terms.append(IntensityTerm(2 * (width - h), tuple(row)))
    return IntensityProgram(channels, tuple(terms))
