"""Exact finite Beurling prime-jet reconstruction in source (word) coordinates.

No ordinary-positive-integer successor or prime oracle is an input to this
module. Python integers are *metatheoretic* finite indices and costs.

This is a finite, source-declared arithmetic chart, not a universal theorem
checker, numerical logarithm calculator, physical source oracle, or RH proof.
"""

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial


class SourceError(ValueError):
    """Malformed generator passport, horizon, or finite proof obligation."""


def _rational(value):
    if type(value) not in (int, F):
        raise SourceError("exact int/Fraction required; floats and booleans rejected")
    return F(value)


@dataclass(frozen=True)
class JetSource:
    """Generator labels and real-scale q_j=exp(lambda_j), encoded exactly.

    Declares that generators are formally *independent words*, not that their
    spectral evaluation is injective. This distinction detects ghost composites.
    """

    generators: tuple[tuple[str, F], ...]
    horizon: F

    def __post_init__(self):
        if type(self.generators) is not tuple or len(self.generators) > 24:
            raise SourceError("at most 24 declared generators in a finite tuple")
        labels = set()
        for entry in self.generators:
            if type(entry) is not tuple or len(entry) != 2:
                raise SourceError("generator must be a (name, q) pair")
            label, size = entry
            if type(label) is not str or not label or label in labels:
                raise SourceError("distinct nonempty generator names required")
            if _rational(size) <= 1:
                raise SourceError("all generator sizes must exceed one")
            labels.add(label)
        if not 1 <= _rational(self.horizon) <= 10000:
            raise SourceError("finite exact horizon must be in [1, 10000]")

    @property
    def sizes(self):
        return tuple(_rational(size) for _, size in self.generators)

    @property
    def H(self):
        return _rational(self.horizon)

    @property
    def vacuum(self):
        return (0,) * len(self.generators)

    def word_size(self, alpha):
        if type(alpha) is not tuple or len(alpha) != len(self.sizes):
            raise SourceError("wrong generator coordinates")
        value = F(1)
        for q, exponent in zip(self.sizes, alpha):
            if type(exponent) is not int or exponent < 0:
                raise SourceError("nonnegative integer word exponents required")
            value *= q ** exponent
        return value


def prime_power_jets(source):
    """Symbolic J/t=Pi: k-fold generator jet carries 1/k, not a fake unit."""
    result = {}
    for j, q in enumerate(source.sizes):
        k, value = 1, q
        while value <= source.H:
            alpha = list(source.vacuum)
            alpha[j] = k
            result[tuple(alpha)] = F(1, k)
            value *= q
            k += 1
            if k > 512:
                raise SourceError("prime-power jet depth exceeds finite resource budget")
    return result


def _word_convolution(source, left, right, budget):
    out = defaultdict(F)
    for alpha, a in left.items():
        for beta, b in right.items():
            word = tuple(x+y for x, y in zip(alpha, beta))
            if source.word_size(word) <= source.H:
                out[word] += a*b
                if len(out) > budget:
                    raise SourceError("word convolution exceeded certified finite budget")
    return dict(out)


def convolution_words(source, *, budget=25000, jet_scale=F(1)):
    """Truncated exp_*(Pi) with every coefficient an exact Fraction.

    The optional jet_scale is a *mutation control*; only scale=1 is canonical.
    """
    if type(source) is not JetSource:
        raise SourceError("JetSource passport required")
    if type(budget) is not int or not 1 <= budget <= 250000:
        raise SourceError("typed finite budget required")
    scale = _rational(jet_scale)
    jets = {a: scale*w for a, w in prime_power_jets(source).items()}
    result = {source.vacuum: F(1)}
    term = {source.vacuum: F(1)}
    r = 0
    # Every nonempty jet increases its positive multiplicative size.
    while term:
        term = _word_convolution(source, term, jets, budget)
        r += 1
        if not term:
            break
        for word, weight in term.items():
            result[word] = result.get(word, F(0)) + weight/F(factorial(r))
        if len(result) > budget or r > budget:
            raise SourceError("convolution exponential exceeded finite budget")
    return result


def counting_measure(source, *, budget=25000, jet_scale=F(1)):
    """Pushforward of exp_*(Pi) by q(word), keeping spectral collisions."""
    atoms = defaultdict(F)
    for word, coefficient in convolution_words(
        source, budget=budget, jet_scale=jet_scale
    ).items():
        atoms[source.word_size(word)] += coefficient
    return dict(sorted(atoms.items()))


def direct_word_oracle(source, *, budget=25000):
    """Independently enumerate geometric FUCC powers (no jets/exp/convolution)."""
    result = {F(1): 1}
    for q in source.sizes:
        next_atoms = defaultdict(int)
        for position, multiplicity in result.items():
            value = position
            while value <= source.H:
                next_atoms[value] += multiplicity
                if len(next_atoms) > budget:
                    raise SourceError("direct word oracle exceeded finite budget")
                value *= q
                if value <= source.H and len(next_atoms) > budget:
                    raise SourceError("finite generator enumeration exceeded budget")
        result = dict(next_atoms)
    return dict(sorted((x, F(y)) for x, y in result.items()))


def _position_convolution(left, right, horizon, budget):
    out = defaultdict(F)
    for x, a in left.items():
        for y, b in right.items():
            v = x*y
            if v <= horizon:
                out[v] += a*b
                if len(out) > budget:
                    raise SourceError("numeric convolution exceeded budget")
    return dict(out)


def convolution_log(atoms, *, budget=25000):
    """Inverse log_*(mu) from the *composite* measure, not original jets.

    Multiplicative coordinate q=exp(t) turns additive t-convolution into
    multiplication; gap >1 makes the local alternating series finite.
    """
    if not atoms or atoms.get(F(1)) != 1:
        raise SourceError("a unit atom of mass one is required")
    horizon = max(atoms)
    if any(_rational(x) < 1 or _rational(c) < 0 for x, c in atoms.items()):
        raise SourceError("positive source measure on q>=1 required")
    positive = {x: _rational(c) for x, c in atoms.items() if x != 1 and c}
    term = {F(1): F(1)}
    result = defaultdict(F)
    order = 0
    while term:
        term = _position_convolution(term, positive, horizon, budget)
        order += 1
        if not term:
            break
        sign = F(1 if order % 2 else -1, order)
        for value, coeff in term.items():
            result[value] += sign * coeff
        if order > budget:
            raise SourceError("finite convolution logarithm did not terminate")
    return dict(sorted((x,c) for x,c in result.items() if c))


def expected_prime_power_measure(source):
    """Independent direct geometric prime-power Pi, as numeric exact weights."""
    out = defaultdict(F)
    for q in source.sizes:
        value, k = q, 1
        while value <= source.H:
            out[value] += F(1, k)
            k += 1
            value *= q
            if k > 512:
                raise SourceError("prime-power oracle depth exceeds finite budget")
    return dict(sorted(out.items()))


def rediscover_generators(atoms, *, budget=25000):
    """Greedily recover a multiset of primitive generators from composite mass.

    Each discrepancy at the least still-unexplained position is the number of
    new primitive generators there. This accepts repeated independent labels.
    """
    if not atoms or atoms.get(F(1)) != 1:
        raise SourceError("a unit of mass one is required")
    horizon = max(atoms)
    discovered = []
    for value, mass in sorted(atoms.items()):
        if value == 1:
            continue
        prior = direct_word_oracle(
            JetSource(tuple((f"found_{i}", q) for i, q in enumerate(discovered)),value),
            budget=budget
        ).get(value,F(0))
        difference = _rational(mass) - prior
        if difference < 0 or difference.denominator != 1:
            raise SourceError("composite measure not compatible with free prime species")
        discovered.extend([value] * int(difference))
        if len(discovered)>24:
            raise SourceError("finite reconstruction exceeds 24 generator species")
    source = JetSource(tuple((f"found_{i}", q) for i,q in enumerate(discovered)),horizon)
    if direct_word_oracle(source,budget=budget) != atoms:
        raise SourceError("primitive extraction did not reconstruct all observed mass")
    return tuple(discovered)


def affine_braid_defects(source, atoms):
    """Only full interior source rectangles count; absent images are not failures."""
    if any(mass != 1 for mass in atoms.values()):
        raise SourceError("a spectral collision makes rank non-canonical")
    ordered = sorted(atoms)
    rank = {x: j+1 for j,x in enumerate(ordered)}
    defects = []
    tested = 0
    for label, raw_q in source.generators:
        q = _rational(raw_q)
        if q not in rank:
            continue
        d = rank[q]
        for x, y in zip(ordered, ordered[1:]):
            if q*x not in rank or q*y not in rank:
                continue
            tested += 1
            difference = rank[q*y] - rank[q*x] - d
            if difference:
                defects.append({
                    "generator":label,"q":str(q),"x":str(x),"Sx":str(y),
                    "rank_q":d,"rank_qx":rank[q*x],"rank_qSx":rank[q*y],
                    "defect":difference,
                })
    return tested, defects


def first_archimedean_cell(atoms):
    """Exact dx=e^t dt cell mass = x_2-x_1, using rational q=e^t."""
    if any(weight != 1 for weight in atoms.values()):
        raise SourceError("colliding or signed atoms do not define rank cells")
    xs = sorted(atoms)
    if len(xs) < 2 or xs[0] != 1:
        raise SourceError("need a vacuum and a successor atom")
    return xs[1]-xs[0]


def fucc_path_receipt(source, alpha, beta):
    """Shortest undirected prime-edge zigzag and its exact endpoint ratio.

    Reversing a prime edge is legal only when that coordinate is positive.
    Ascent through the coordinatewise minimum realizes the L1 lower bound.
    """
    a, b = source.word_size(alpha), source.word_size(beta)
    shared = tuple(min(u,v) for u,v in zip(alpha,beta))
    backward = sum(u-m for u,m in zip(alpha,shared))
    forward = sum(v-m for v,m in zip(beta,shared))
    return {"from":str(a),"to":str(b),"ratio":str(b/a),
            "backward_edges":backward,"forward_edges":forward,
            "minimum_fucc_edges":backward+forward,
            "meet":str(source.word_size(shared))}
