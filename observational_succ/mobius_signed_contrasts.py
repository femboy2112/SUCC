"""Source-authenticated Mobius matrix refinement and CRT clock calibration.

Uses the original IMW four-pole source and formal Q[Q/Z] character carrier.
Atomic Gram blocks are positive after character evaluation. Unordered
Mobius contrasts of EMPIRICAL conditional energies need not be positive.
Balanced CRT clocks repair that issue with an explicit change-of-measure
cost; they do not supply the missing pi-selected cancellation estimate.

All non-diagnostic outputs use exact integers/Fractions/PhasePoly. Proofs,
source hypotheses, controls and asymptotic boundaries are in the dossier.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import factorial, isqrt, prod

from .succ_internal_matrix_walk import PhasePoly, authentic_r, circle


class RefinementError(ValueError):
    """A source, precision, partition, or finite-budget contract failed."""


def integer(n, low=0, high=100000):
    if type(n) is not int or not low <= n <= high:
        raise RefinementError(f"integer in [{low}, {high}] required")
    return n


def rational(x):
    if type(x) not in (int, Q):
        raise RefinementError("exact integer/Fraction required")
    return Q(x)


def prime(p):
    integer(p, 2)
    if any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise RefinementError("genuine prime required")
    return p


def valuation(x, p):
    """v_p(x), with None reserved for x=0 (not a finite valuation)."""
    prime(p); x = rational(x)
    if not x:
        return None
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % p == 0:
        a //= p; v += 1
    while b % p == 0:
        b //= p; v -= 1
    return v


def integral_residue(x, p, k):
    """Retain the integer lift; reject illegal reduction of nonintegral x."""
    prime(p); integer(k, 1, 16); x = rational(x)
    if x.denominator % p == 0:
        raise RefinementError("p-integral source required before reduction")
    modulus = p**k
    return (x.numerator * pow(x.denominator, -1, modulus)) % modulus


def valuation_chart(x, p, k):
    """A valuation plus a p-unit jet; NOT a silent mod-p reduction."""
    prime(p); integer(k, 1, 16); x = rational(x)
    v = valuation(x, p)
    if v is None:
        return (None, 0)
    unit = x / (Q(p)**v)
    return (v, integral_residue(unit, p, k))


def source_states(n):
    integer(n, 0, 8192)
    u, out = Q(), []
    for j in range(1, n+1):
        u = 16*u + authentic_r(j)
        out.append(u)
    return tuple(out)


def authenticate(states):
    if type(states) is not tuple or len(states) > 8192:
        raise RefinementError("finite immutable source history required")
    u = Q()
    for n, value in enumerate(states, 1):
        if type(value) is not Q or value != 16*u + authentic_r(n):
            raise RefinementError(f"original zero-selected BBP failed at n={n}")
        u = value
    return states


def pole_tail_density(p, k):
    """Exact periodic density of v_p(r(n)) <= -k; proof uses all four poles."""
    prime(p); integer(k, 0, 16)
    if k == 0:
        return Q(1)
    if p == 2:
        return Q()
    if k == 1 and p in (3, 5):
        return Q(3, p) - Q(1, p*p)
    return Q(4, p**k)


@dataclass(frozen=True)
class PrimeGrid:
    """Capped pole depths. Integral dyadic digits are a SEPARATE chart."""
    primes: tuple[int, ...] = ()
    depths: tuple[int, ...] = ()

    def __post_init__(self):
        if (type(self.primes) is not tuple or type(self.depths) is not tuple
                or len(self.primes) != len(self.depths)
                or self.primes != tuple(sorted(set(self.primes)))):
            raise RefinementError("sorted distinct prime/depth tuples required")
        for p in self.primes:
            prime(p)
        for k in self.depths:
            integer(k, 1, 10)
        if prod(k+1 for k in self.depths) > 1024:
            raise RefinementError("at most 1024 declared incidence cells")

    @property
    def cells(self):
        return tuple(product(*(range(k+1) for k in self.depths)))

    @property
    def modulus(self):
        # First exceptional-prime pole masks require p^2, not p.
        return prod(p**(max(k, 2) if p in (3, 5) else k)
                    for p, k in zip(self.primes, self.depths) if p != 2)

    def check_cell(self, a):
        if (type(a) is not tuple or len(a) != len(self.depths)
                or any(type(j) is not int or not 0 <= j <= k
                       for j, k in zip(a, self.depths))):
            raise RefinementError("cell outside declared valuation grid")
        return a

    def signature(self, n):
        integer(n, 1)
        r = authentic_r(n)
        return tuple(min(k, max(0, -valuation(r, p)))
                     for p, k in zip(self.primes, self.depths))

    def mobius(self, a, b):
        self.check_cell(a); self.check_cell(b)
        jumps = tuple(y-x for x, y in zip(a, b))
        return (-1)**sum(jumps) if all(j in (0, 1) for j in jumps) else 0

    def refines(self, coarse):
        if not isinstance(coarse, PrimeGrid):
            return False
        caps = dict(zip(self.primes, self.depths))
        return all(caps.get(p, 0) >= k for p, k in zip(coarse.primes, coarse.depths))

    def project(self, cell, coarse):
        self.check_cell(cell)
        if not self.refines(coarse):
            raise RefinementError("not a valid source-grid coarsening")
        values = dict(zip(self.primes, cell))
        return tuple(min(k, values[p]) for p, k in zip(coarse.primes, coarse.depths))

    def density(self, cell):
        self.check_cell(cell)
        out = Q(1)
        for p, k, j in zip(self.primes, self.depths, cell):
            out *= pole_tail_density(p, j) - (pole_tail_density(p, j+1) if j < k else 0)
        return out

    def count_bounds(self, n, cell):
        integer(n, 0)
        period = self.modulus
        residues = period * self.density(cell)
        if residues.denominator != 1:
            raise ArithmeticError("period does not resolve source masks")
        q, r = divmod(n, period)
        size = residues.numerator
        return (q*size + max(0, r-(period-size)), q*size + min(r, size))


def frequencies_checked(frequencies):
    if (type(frequencies) is not tuple or not 1 <= len(frequencies) <= 16
            or len(set(frequencies)) != len(frequencies)
            or any(type(h) is not int for h in frequencies)):
        raise RefinementError("1..16 distinct integer Fourier frequencies required")
    return frequencies


def zero_matrix(h):
    return tuple(tuple(PhasePoly.zero() for _ in range(h)) for _ in range(h))


def matrix_add(a, b):
    if len(a) != len(b) or any(len(r) != len(a) for r in a+b):
        raise RefinementError("matching square matrices required")
    return tuple(tuple(x+y for x, y in zip(r, s)) for r, s in zip(a, b))


def matrix_scale(a, q):
    q = rational(q)
    return tuple(tuple(q*x for x in row) for row in a)


def rank_one(phase, frequencies):
    phase = rational(phase); frequencies_checked(frequencies)
    return tuple(tuple(PhasePoly.monomial((h-k)*phase) for k in frequencies)
                 for h in frequencies)


def atomic_grams(states, labels, frequencies):
    """Generic positive Gram instrument; this alone authenticates NO source."""
    frequencies_checked(frequencies)
    if len(states) != len(labels):
        raise RefinementError("one declared cell label per source state")
    blocks = {}
    for state, label in zip(states, labels):
        blocks[label] = matrix_add(blocks.get(label, zero_matrix(len(frequencies))),
                                   rank_one(state, frequencies))
    return blocks


def invert_thresholds(grid, cumulative, width):
    """Product-of-chains Mobius inverse, with EVERY threshold supplied."""
    integer(width, 1, 16)
    if not isinstance(grid, PrimeGrid) or set(cumulative) != set(grid.cells):
        raise RefinementError("complete declared factorial/threshold table required")
    result = {}
    for a in grid.cells:
        block = zero_matrix(width)
        for steps in product((0, 1), repeat=len(a)):
            b = tuple(x+s for x, s in zip(a, steps))
            if all(y <= k for y, k in zip(b, grid.depths)):
                block = matrix_add(block, matrix_scale(cumulative[b], (-1)**sum(steps)))
        result[a] = block
    return result


@dataclass(frozen=True)
class RefinedMatrixWalk:
    grid: PrimeGrid
    frequencies: tuple[int, ...]
    history: tuple[Q, ...]
    blocks: tuple  # sorted (cell, exact Gram) pairs; empty cells retained

    def __post_init__(self):
        if not isinstance(self.grid, PrimeGrid):
            raise RefinementError("typed source grid required")
        frequencies_checked(self.frequencies); authenticate(self.history)
        if self.blocks != self._replay(self.history, self.grid, self.frequencies):
            raise RefinementError("Gram blocks do not match the authenticated history")

    @staticmethod
    def _replay(history, grid, frequencies):
        blocks = atomic_grams(history, tuple(grid.signature(n) for n in range(1, len(history)+1)), frequencies)
        zero = zero_matrix(len(frequencies))
        return tuple((a, blocks.get(a, zero)) for a in grid.cells)

    @classmethod
    def build(cls, n=0, grid=PrimeGrid(), frequencies=(0, 1)):
        history = source_states(n)
        return cls(grid, frequencies, history, cls._replay(history, grid, frequencies))

    def succ(self):
        n = len(self.history)+1
        u = 16*(self.history[-1] if self.history else Q()) + authentic_r(n)
        blocks = dict(self.blocks); a = self.grid.signature(n)
        blocks[a] = matrix_add(blocks[a], rank_one(u, self.frequencies))
        return type(self)(self.grid, self.frequencies, self.history+(u,), tuple(sorted(blocks.items())))

    def refine(self, grid, frequencies):
        if not grid.refines(self.grid) or not set(self.frequencies) <= set(frequencies):
            raise RefinementError("refinement must retain every old source coordinate")
        frequencies_checked(frequencies)
        # New frequencies / old cells cannot be recovered from a Gram alone.
        return type(self)(grid, frequencies, self.history, self._replay(self.history, grid, frequencies))

    def coarsen(self, grid, frequencies):
        if not self.grid.refines(grid) or not set(frequencies) <= set(self.frequencies):
            raise RefinementError("invalid coordinate restriction")
        frequencies_checked(frequencies)
        indices = tuple(self.frequencies.index(h) for h in frequencies)
        blocks = {a: zero_matrix(len(frequencies)) for a in grid.cells}
        for a, block in self.blocks:
            b = self.grid.project(a, grid)
            restricted = tuple(tuple(block[i][j] for j in indices) for i in indices)
            blocks[b] = matrix_add(blocks[b], restricted)
        return type(self)(grid, frequencies, self.history, tuple(sorted(blocks.items())))

    def prefix(self, n):
        integer(n, 0, len(self.history))
        h = self.history[:n]
        return type(self)(self.grid, self.frequencies, h, self._replay(h, self.grid, self.frequencies))

    def gram(self):
        out = zero_matrix(len(self.frequencies))
        for _, block in self.blocks:
            out = matrix_add(out, block)
        return out

    def thresholds(self):
        out = {}
        for a in self.grid.cells:
            block = zero_matrix(len(self.frequencies))
            for b, atom in self.blocks:
                if all(x <= y for x, y in zip(a, b)):
                    block = matrix_add(block, atom)
            out[a] = block
        return out


def abs2(poly):
    return poly * poly.star()


def sample_moments(states, labels, h=1, weights=None):
    integer(len(states), 1, 8192)
    if type(h) is not int or h == 0 or len(states) != len(labels):
        raise RefinementError("nonzero integer h and matched labels required")
    weights = tuple(Q(1, len(states)) for _ in states) if weights is None else tuple(map(rational, weights))
    if len(weights) != len(states) or any(w <= 0 for w in weights) or sum(weights) != 1:
        raise RefinementError("positive normalized rational source weights required")
    cells = {}
    for x, a, w in zip(states, labels, weights):
        mass, s = cells.get(a, (Q(), PhasePoly.zero()))
        cells[a] = (mass+w, s+w*PhasePoly.monomial(h*rational(x)))
    return cells, weights


def conditional_energy(states, labels, h=1, weights=None):
    cells, _ = sample_moments(states, labels, h, weights)
    return sum((abs2(s)/mass for mass, s in cells.values()), PhasePoly.zero())


def refinement_energy(states, coarse, fine, h=1, weights=None):
    """Exact Pythagoras for a NESTED partition, with a positive-square witness."""
    parents = {}
    if len(coarse) != len(states) or len(fine) != len(states):
        raise RefinementError("partition lengths must match the source sample")
    for a, b in zip(coarse, fine):
        if b in parents and parents[b] != a:
            raise RefinementError("fine partition does not refine coarse partition")
        parents[b] = a
    old, _ = sample_moments(states, coarse, h, weights)
    new, _ = sample_moments(states, fine, h, weights)
    squares = tuple((mass, s/mass-old[parents[b]][1]/old[parents[b]][0])
                    for b, (mass, s) in new.items())
    gain = sum((mass*abs2(delta) for mass, delta in squares), PhasePoly.zero())
    if gain != conditional_energy(states, fine, h, weights)-conditional_energy(states, coarse, h, weights):
        raise ArithmeticError("conditional Pythagoras identity failed")
    return gain, squares


def boolean_energy_contrast(states, feature_columns, h=1, weights=None):
    """Complete factorial contrast; no positivity claim for empirical measures."""
    integer(len(feature_columns), 0, 8)
    if any(len(col) != len(states) for col in feature_columns):
        raise RefinementError("all factorial cells require the same observations")
    out = PhasePoly.zero()
    for bits in product((0, 1), repeat=len(feature_columns)):
        labels = tuple(tuple(col[n] for bit, col in zip(bits, feature_columns) if bit)
                       for n in range(len(states)))
        out += (-1)**(len(bits)-sum(bits))*conditional_energy(states, labels, h, weights)
    return out


def half_turn_evaluation(poly):
    """Exact cyclotomic evaluation for conductors dividing 2 only."""
    if any(p.denominator > 2 for p, _ in poly.terms):
        raise RefinementError("this quotient only evaluates e(0)=1 and e(1/2)=-1")
    return sum((c*(1 if p == 0 else -1) for p, c in poly.terms), Q())


def balancing_cost(n, modulus):
    """Exact l1 cost between actual time counting and residue-balanced weights."""
    integer(n, 1); integer(modulus, 1, n)
    r = n % modulus
    return Q(2*r*(modulus-r), n*modulus)


def balanced_weights(n, modulus):
    integer(n, 1); integer(modulus, 1, n)
    counts = [0]*modulus
    for j in range(1, n+1):
        counts[j % modulus] += 1
    return tuple(Q(1, modulus*counts[j % modulus]) for j in range(1, n+1))


def divisors(n):
    integer(n, 1, 4096)
    return tuple(d for d in range(1, n+1) if n % d == 0)


def integer_mobius(n):
    """Divisor-incidence inversion, not a parity guess at prime powers."""
    ds = divisors(n); mu = {1: 1}
    for d in ds[1:]:
        mu[d] = -sum(v for e, v in mu.items() if d % e == 0)
    return mu[n]


def clock_projection(values, d):
    q = len(values)
    integer(q, 1, 4096); integer(d, 1, q)
    if q % d:
        raise RefinementError("period must divide the complete clock")
    means = tuple(sum(values[a::d], PhasePoly.zero()) / (q//d) for a in range(d))
    return tuple(means[a % d] for a in range(q))


def primitive_clock_budget(states, modulus, h=1):
    """Orthogonal Mobius period energies on the BALANCED clock, not raw time."""
    integer(modulus, 1, min(len(states), 256))
    _, weights = sample_moments(states, (0,)*len(states), h, balanced_weights(len(states), modulus))
    f = []
    for a in range(modulus):
        cell = tuple(x for n, x in enumerate(states, 1) if n % modulus == a)
        f.append(sum((PhasePoly.monomial(h*rational(x)) for x in cell), PhasePoly.zero())/len(cell))
    f = tuple(f); ds = divisors(modulus)
    projections = {d: clock_projection(f, d) for d in ds}
    components, energies = {}, {}
    for d in ds:
        components[d] = tuple(sum((integer_mobius(d//e)*projections[e][a]
                                  for e in divisors(d)), PhasePoly.zero()) for a in range(modulus))
        energies[d] = sum((abs2(x) for x in components[d]), PhasePoly.zero())/modulus
    total = sum((abs2(x) for x in f), PhasePoly.zero())/modulus
    if sum(energies.values(), PhasePoly.zero()) != total:
        raise ArithmeticError("primitive-clock Parseval failed")
    residual = sum((w*abs2(PhasePoly.monomial(h*rational(x))-f[n % modulus])
                    for n, (x, w) in enumerate(zip(states, weights), 1)), PhasePoly.zero())
    if residual+total != PhasePoly.one():
        raise ArithmeticError("within-clock source variance missing")
    return {"components": components, "energies": energies,
            "within_residue": residual, "balanced_mean_squared": energies[1],
            "raw_mean_error_cap": balancing_cost(len(states), modulus)}


def coherent_seed_control(n, start, primes=()):
    """Exact-forcing, odd p-free RATIONAL seed counterfeit for a finite horizon.

    Every clock of the forcing is unchanged, but U0 is NOT zero. It is a
    hostile fixture, never an authenticated replacement for the original.
    On start<=j<=n, |U_j|<1/(32 start^2). Thus ALL partition innovation
    gains there are <=5 h^2/(128 start^4), for each integer h, simultaneously.
    """
    integer(n, 1, 2048); integer(start, 1, n)
    if type(primes) is not tuple or len(set(primes)) != len(primes):
        raise RefinementError("distinct genuine source-prime tuple required")
    for p in primes:
        prime(p)
    target = -sum((authentic_r(j)/16**j for j in range(1, n+1)), Q())
    denominator = 1+128*start*start*prod(primes)*16**n
    rounded = target*denominator+Q(1, 2)
    initial = Q(rounded.numerator//rounded.denominator, denominator)
    state, history = initial, []
    for j in range(1, n+1):
        state = 16*state+authentic_r(j)
        history.append(state)
    radius = Q(1, 32*start*start)
    if initial == 0 or any(abs(x) >= radius for x in history[start-1:]):
        raise ArithmeticError("rational coherent-seed certificate failed")
    return {"initial": initial, "states": tuple(history), "start": start,
            "radius": radius, "all_partition_gain_cap_h1": Q(5, 128*start**4),
            "authentic_zero_initial": False}


def counterfeit_states(n):
    integer(n, 0, 8192)
    return tuple(Q(16**j, 3)-Q(1, (8*j+1)*(8*j+3)) for j in range(1, n+1))


def counterfeit_gain_cap(n, h=1):
    integer(n, 1)
    if type(h) is not int or h == 0:
        raise RefinementError("nonzero integer h")
    # Uniform over ALL partitions, not just fitted pole-mask hierarchies.
    return Q(5*h*h, 384*n)


def real_phase_interval(poly, terms=12):
    """Sound rational enclosure of a Hermitian phase polynomial's real value.

    Machin's identity gives a rational pi enclosure via alternating arctan;
    cosine Taylor/Lagrange plus its 1-Lipschitz bound transports that error.
    Unlike PhasePoly.evaluation, this returns certified rational endpoints.
    """
    if type(poly) is not PhasePoly or poly.star() != poly:
        raise RefinementError("Hermitian phase polynomial required")
    integer(terms, 2, 32)
    def atan_interval(q):
        s = sum((Q((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(2*terms)), Q())
        return s, s+Q(1, (4*terms+1)*q**(4*terms+1))
    a, b = atan_interval(5); c, d = atan_interval(239)
    pi_low, pi_high = 16*a-4*d, 16*b-4*c
    midpoint = (pi_low+pi_high)/2; radius = (pi_high-pi_low)/2
    low, high = Q(), Q()
    for phase, coefficient in poly.terms:
        q = phase if phase <= Q(1, 2) else phase-1
        x = 2*q*midpoint
        value = sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(terms+1)), Q())
        error = abs(x)**(2*terms+2)/factorial(2*terms+2)+2*abs(q)*radius
        lo, hi = coefficient*(value-error), coefficient*(value+error)
        low += min(lo, hi); high += max(lo, hi)
    return low, high


def clock_transport_caps(n, modulus, width=1):
    """Uniform raw/balanced bounds, not empirical assertions of cancellation.

    Conditional energy: <=2*l1. Gram operator norm: <=H*l1.
    Purity: <=2*H^2*l1. To transfer o(H) purity excess it suffices
    that H*l1 -> 0, e.g. H*modulus=o(N), not just modulus=o(N).
    """
    integer(width, 1, 100000)
    cost = balancing_cost(n, modulus)
    return {"mean_error": cost, "conditional_energy_error": min(Q(1), 2*cost),
            "gram_operator_error": width*cost, "purity_error": 2*width*width*cost}


def singleton_energy_floor(labels):
    integer(len(labels), 1)
    counts = {}
    for a in labels:
        counts[a] = counts.get(a, 0)+1
    return Q(sum(c == 1 for c in counts.values()), len(labels))


def source_index_view(history, indices):
    """Retain literal source times: a decimated view is NOT a new BBP orbit."""
    authenticate(history)
    if type(indices) is not tuple:
        raise RefinementError("literal immutable source indices required")
    for n in indices:
        integer(n, 0, len(history))
    return tuple((n, Q() if n == 0 else history[n-1]) for n in indices)


def affine_source_paths(history, n, p):
    """Source-time V_p S=S^p V_p with full histories and declared phase.

    The readout at p*n is U_(p*n), NOT p*U_n. The relative mixed phase
    holds S edges at zero; assigning dU to ALL edges makes the loop flat.
    """
    integer(n, 1); prime(p)
    left = source_index_view(history, (n, n+1, p*(n+1)))
    right = source_index_view(history, (n,)+tuple(range(p*n, p*(n+1)+1)))
    u = lambda j: history[j-1]
    relative = circle(u(p*(n+1))-u(p*n)-u(n+1)+u(n))
    return {"left": left, "right": right, "relative_phase": relative,
            "full_gradient_holonomy": sum((b[1]-a[1] for a, b in zip(left, left[1:])), Q())
            - sum((b[1]-a[1] for a, b in zip(right, right[1:])), Q())}
