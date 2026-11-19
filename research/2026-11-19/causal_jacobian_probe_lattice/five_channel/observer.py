"""Exact finite five-channel BBP observer and prime-resolution charts.

The source family is declared, not inferred from arbitrary finite data.  Source
identification and invertible observation are not assertions of Weyl cancellation.
Only standard-library arithmetic is used.  See CONSTRUCTION.md for proofs.
"""

from dataclasses import dataclass
from fractions import Fraction
from math import inf, isqrt, lcm, prod


POLES = (7, 4, 3, 2)
BBP_COEFFICIENTS = (4, -2, -1, -1)


def _prime(p):
    if not isinstance(p, int) or p < 2 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError("p must be prime")


def _clocks(clocks):
    clocks = tuple(clocks)
    if len(clocks) != 4 or any(not isinstance(m, int) or m < 1 for m in clocks):
        raise ValueError("four positive integer clocks are required")
    if len(set(clocks)) != 4:
        raise ValueError("clock observations must be distinct")
    return clocks


def source(n, coefficients=BBP_COEFFICIENTS):
    if not isinstance(n, int) or n < 1 or len(coefficients) != 4:
        raise ValueError("positive clock and four coefficients required")
    return sum((Fraction(c, 8 * n - d) for c, d in zip(coefficients, POLES)), Fraction())


def cauchy_matrix(clocks):
    return tuple(tuple(Fraction(1, 8 * m - d) for d in POLES) for m in _clocks(clocks))


def row_denominator_lcms(clocks):
    """Integral row scales; their growth and measurement units remain explicit."""
    return tuple(lcm(*(8 * m - d for d in POLES)) for m in _clocks(clocks))


def cleared_cauchy_matrix(clocks):
    """The integral matrix diag(LCM of each denominator row) times C."""
    clocks = _clocks(clocks)
    return tuple(tuple(scale // (8 * m - d) for d in POLES)
                 for m, scale in zip(clocks, row_denominator_lcms(clocks)))


def determinant(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("square matrix required")
    result = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Fraction()
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        q = a[j][j]
        result *= q
        for i in range(j + 1, n):
            factor = a[i][j] / q
            for k in range(j + 1, n):
                a[i][k] -= factor * a[j][k]
    return result


def inverse(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("square matrix required")
    a = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        a[j], a[pivot] = a[pivot], a[j]
        q = a[j][j]
        a[j] = [x / q for x in a[j]]
        for i in range(n):
            if i != j:
                q = a[i][j]
                a[i] = [x - q * y for x, y in zip(a[i], a[j])]
    return tuple(tuple(row[n:]) for row in a)


def matvec(matrix, vector):
    return tuple(sum((a * b for a, b in zip(row, vector)), Fraction()) for row in matrix)


def cauchy_determinant(clocks):
    """Signed determinant with the given row order and POLES=(7,4,3,2)."""
    clocks = _clocks(clocks)
    delta = prod(clocks[j] - clocks[i] for i in range(4) for j in range(i + 1, 4))
    denominator = prod(8 * m - d for m in clocks for d in POLES)
    return Fraction(120 * 8 ** 6 * delta, denominator)


def partial_coefficients(horizon):
    if not isinstance(horizon, int) or horizon < 0:
        raise ValueError("nonnegative integer horizon required")
    return tuple(sum((Fraction(1, 16 ** n * (8 * n - d))
                      for n in range(1, horizon + 1)), Fraction()) for d in POLES)


@dataclass(frozen=True)
class Journal:
    """A finite causal journal; the exact integer winding is retained."""
    coefficients: tuple
    seed: Fraction
    states: tuple

    @property
    def horizon(self):
        return len(self.states) - 1


def make_journal(horizon, coefficients=BBP_COEFFICIENTS, seed=0):
    if not isinstance(horizon, int) or horizon < 0 or len(coefficients) != 4:
        raise ValueError("nonnegative horizon and four coefficients required")
    coefficients = tuple(map(Fraction, coefficients))
    seed = Fraction(seed)
    states = [seed]
    for n in range(1, horizon + 1):
        states.append(16 * states[-1] + source(n, coefficients))
    return Journal(coefficients, seed, tuple(states))


def advance(journal, steps=1):
    """Append source ticks; never rewrite an earlier observation."""
    if not isinstance(steps, int) or steps < 0 or not validate_journal(journal):
        raise ValueError("valid journal and nonnegative steps required")
    states = list(journal.states)
    for n in range(journal.horizon + 1, journal.horizon + steps + 1):
        states.append(16 * states[-1] + source(n, journal.coefficients))
    return Journal(journal.coefficients, journal.seed, tuple(states))


def validate_journal(journal, authentic=False):
    if (len(journal.coefficients) != 4 or not journal.states
            or journal.states[0] != journal.seed):
        return False
    if authentic and (journal.seed != 0 or journal.coefficients != BBP_COEFFICIENTS):
        return False
    return all(journal.states[n] - 16 * journal.states[n - 1]
               == source(n, journal.coefficients) for n in range(1, len(journal.states)))


@dataclass(frozen=True)
class Snapshot:
    clocks: tuple
    horizon: int
    innovations: tuple
    anchor: Fraction


def observe(journal, clocks):
    clocks = _clocks(clocks)
    if max(clocks) > journal.horizon or not validate_journal(journal):
        raise ValueError("all probes must lie in the valid elapsed journal")
    innovations = tuple(journal.states[m] - 16 * journal.states[m - 1] for m in clocks)
    return Snapshot(clocks, journal.horizon, innovations,
                    journal.states[-1] / 16 ** journal.horizon)


def recover(snapshot):
    """Recover (c,s) exactly, conditional on the declared four-pole family."""
    if len(snapshot.innovations) != 4 or snapshot.horizon < max(_clocks(snapshot.clocks)):
        raise ValueError("invalid finite snapshot")
    coefficients = matvec(inverse(cauchy_matrix(snapshot.clocks)), snapshot.innovations)
    seed = snapshot.anchor - sum((a * c for a, c in zip(
        partial_coefficients(snapshot.horizon), coefficients)), Fraction())
    return coefficients, seed


def observation_jacobian(clocks, horizon):
    clocks = _clocks(clocks)
    if horizon < max(clocks):
        raise ValueError("noncausal probe clock")
    return tuple(row + (Fraction(),) for row in cauchy_matrix(clocks)) + (
        partial_coefficients(horizon) + (Fraction(1),),)


def valuation(value, p):
    _prime(p)
    value = Fraction(value)
    if not value:
        return inf
    a, b = value.numerator, value.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def reduce_p(value, p, precision=1):
    _prime(p)
    if not isinstance(precision, int) or precision < 1:
        raise ValueError("positive precision required")
    value = Fraction(value)
    if value.denominator % p == 0:
        raise ValueError("a polar rational requires its declared row scaling")
    modulus = p ** precision
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def rank_mod_p(matrix, p):
    a = [[reduce_p(x, p) for x in row] for row in matrix]
    if not a:
        return 0
    rank = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        q = pow(a[rank][j], -1, p)
        a[rank] = [x * q % p for x in a[rank]]
        for i in range(len(a)):
            if i != rank:
                q = a[i][j]
                a[i] = [(x - q * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


@dataclass(frozen=True)
class PrimeChart:
    prime: int
    clocks: tuple
    exponents: tuple
    matrix: tuple
    inverse_matrix: tuple
    rank: int
    loss: int
    determinant_valuation: int

    def measurement_precision(self, coefficient_precision):
        if not isinstance(coefficient_precision, int) or coefficient_precision < 1:
            raise ValueError("positive coefficient precision required")
        return coefficient_precision + self.loss


def prime_chart(clocks, p):
    """Normalize polar rows and compute the exact p-adic inverse precision cost."""
    _prime(p)
    clocks = _clocks(clocks)
    exponents = tuple(max(valuation(8 * m - d, p) for d in POLES) for m in clocks)
    matrix = tuple(tuple(p ** e * x for x in row)
                   for e, row in zip(exponents, cauchy_matrix(clocks)))
    inv = inverse(matrix)
    loss = max(0, -min(valuation(x, p) for row in inv for x in row))
    return PrimeChart(p, clocks, exponents, matrix, inv, rank_mod_p(matrix, p),
                      int(loss), int(valuation(determinant(matrix), p)))


def recover_mod_p(chart, scaled_residues, coefficient_precision):
    """Inputs must be correct modulo p^(coefficient_precision+chart.loss).

    This function checks shape and p-integrality, not an unavailable truth oracle
    for measurement accuracy.  The caller supplies the stated precision contract.
    """
    if len(scaled_residues) != 4:
        raise ValueError("four normalized residue measurements required")
    chart.measurement_precision(coefficient_precision)
    lifted = matvec(chart.inverse_matrix, tuple(map(Fraction, scaled_residues)))
    return tuple(reduce_p(x, chart.prime, coefficient_precision) for x in lifted)


def five_channel_budget(chart, horizon, target_precision):
    """Absolute valuation budgets for recovering both source and seed.

    The anchor may be a polar rational.  'anchor' denotes accuracy modulo p^a
    as a Q_p error, not permission to reduce a nonintegral anchor by reduce_p.
    """
    if horizon < max(chart.clocks):
        raise ValueError("all chart clocks must have elapsed")
    chart.measurement_precision(target_precision)
    a = partial_coefficients(horizon)
    seed_row = tuple(sum((a[i] * chart.inverse_matrix[i][j] for i in range(4)), Fraction())
                     for j in range(4))
    seed_loss = int(max(0, -min(valuation(x, chart.prime) for x in seed_row)))
    return {"innovations": target_precision + max(chart.loss, seed_loss),
            "anchor": target_precision, "coefficient_loss": chart.loss,
            "seed_innovation_loss": seed_loss}


@dataclass(frozen=True)
class RepairPlan:
    prime: int
    history: tuple
    appended_clocks: tuple
    basis_clocks: tuple
    allow_poles: bool


def plan_prime_repair(history, p, allow_poles=None):
    """Choose future clocks from source denominators only, never from phase values.

    Ordinary charts are the default at p>=11. At p=7 the polar default is necessary:
    only three pole-free residue classes exist. For p=2,3,5 use prime_chart.loss;
    plan_polar_repair separately supplies future unit charts at every odd prime.
    Appended clocks are a plan and must actually elapse before observation.
    """
    _prime(p)
    history = tuple(history)
    if p < 7:
        raise ValueError("small-prime collision: use the general precision budget")
    if not history or any(not isinstance(m, int) or m < 1 for m in history):
        raise ValueError("nonempty positive clock history required")
    if tuple(sorted(set(history))) != history:
        raise ValueError("history must preserve distinct chronological observations")
    if allow_poles is None:
        allow_poles = p == 7
    if not allow_poles and p < 11:
        raise ValueError("four pole-free clock residues do not exist at this prime")
    basis, residues = [], set()

    def admissible(m):
        return (m % p not in residues
                and (allow_poles or all((8 * m - d) % p for d in POLES)))

    for m in history:
        if admissible(m):
            basis.append(m)
            residues.add(m % p)
            if len(basis) == 4:
                break
    appended = []
    m = history[-1]
    while len(basis) < 4:
        m += 1
        if admissible(m):
            appended.append(m)
            basis.append(m)
            residues.add(m % p)
    return RepairPlan(p, history + tuple(appended), tuple(appended), tuple(basis), allow_poles)


def polar_clock_depth(p):
    """Smallest pole-separating clock depth for the all-odd-prime repair."""
    _prime(p)
    if p == 2:
        raise ValueError("8 is not a 2-adic unit; the polar-clock theorem does not apply")
    return 1 + max(valuation(POLES[j] - POLES[k], p)
                   for j in range(4) for k in range(j + 1, 4))


def plan_polar_repair(history, p):
    """Append four pole-resolving clocks within p^a ticks at every odd prime.

    Here a=1+max_(j<k) v_p(d_j-d_k), so a=2 at3,5 and1 otherwise.
    Each pole label gets its first future clock8*m=d_j modp^a.  The normalized
    reduction is a scaled permutation matrix. This plans extra observations;
    the exact source clock and all previous journal entries remain unchanged.
    """
    depth = polar_clock_depth(p)
    history = tuple(history)
    if not history or any(not isinstance(m, int) or m < 1 for m in history):
        raise ValueError("nonempty positive clock history required")
    if tuple(sorted(set(history))) != history:
        raise ValueError("history must preserve distinct chronological observations")
    modulus = p ** depth
    inverse_eight = pow(8, -1, modulus)
    horizon = history[-1]
    residues = tuple(d * inverse_eight % modulus for d in POLES)
    appended = tuple(sorted(horizon + ((r - horizon) % modulus or modulus)
                            for r in residues))
    return RepairPlan(p, history + appended, appended, appended, True)


@dataclass(frozen=True)
class UniversalRepairPlan:
    """One future four-clock chart for every odd prime; see FC-07."""
    history: tuple
    appended_clocks: tuple
    basis_clocks: tuple
    binary_loss: int = 11


def plan_universal_repair(history):
    """Append a consecutive four-clock unit chart for all odd primes at once.

    The first future start n satisfies n=2 mod3 and n!=0 mod5; the last
    observation occurs at most nine source ticks after history[-1]. Its cleared
    integer matrix has Smith invariants(1,4,64,2048). The measurement row scales,
    eleven-digit binary inverse cost, and seed-anchor cost are not discarded.
    """
    history = tuple(history)
    if not history or any(not isinstance(m, int) or m < 0 for m in history):
        raise ValueError("nonempty nonnegative clock history required")
    if tuple(sorted(set(history))) != history:
        raise ValueError("history must preserve distinct chronological observations")
    start = history[-1] + 1
    while start % 3 != 2 or start % 5 == 0:
        start += 1
    appended = tuple(range(start, start + 4))
    return UniversalRepairPlan(history + appended, appended, appended)
