"""Exact finite weighted-path semantics over Q(i), with actual SUCC adapters.

This is a finite presentation of matrices, not a quantization procedure for
arbitrary lambda programs. Scalars reuse collective_spectral.Gaussian. Matrix
coordinates are column-vector coordinates; the inner product is conjugate-linear
in its first argument. No arbitrary complex scalar oracle, infinite path sum,
continuum Yang--Mills construction, or quantum speedup is supplied.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product

from .collective_spectral import Gaussian, gaussian


class GraphSemanticsError(ValueError):
    """A boundary, coefficient, state or composability contract failed."""


def _dimension(value: int) -> int:
    if type(value) is not int or value < 1:
        raise GraphSemanticsError("positive exact dimension required")
    return value


def _index(value: int, dimension: int) -> int:
    if type(value) is not int or not 0 <= value < dimension:
        raise GraphSemanticsError("index outside declared finite boundary")
    return value


def squared_norm(values) -> Q:
    """Exact Euclidean squared norm; values need not be normalized."""
    return sum((z.real*z.real + z.imag*z.imag
                for z in (gaussian(x) for x in values)), Q())


@dataclass(frozen=True)
class Matrix:
    """A nonempty rectangular matrix with exactly representable Q(i) entries."""

    entries: tuple[tuple[Gaussian, ...], ...]

    def __post_init__(self):
        if not isinstance(self.entries, (tuple, list)) or not self.entries:
            raise GraphSemanticsError("nonempty row family required")
        rows = tuple(tuple(gaussian(x) for x in row) for row in self.entries)
        if not rows[0] or any(len(row) != len(rows[0]) for row in rows):
            raise GraphSemanticsError("nonempty rectangular matrix required")
        object.__setattr__(self, "entries", rows)

    @property
    def shape(self) -> tuple[int, int]:
        return len(self.entries), len(self.entries[0])

    @classmethod
    def zero(cls, rows: int, columns: int) -> "Matrix":
        return cls(tuple(tuple(0 for _ in range(_dimension(columns)))
                         for _ in range(_dimension(rows))))

    @classmethod
    def identity(cls, size: int) -> "Matrix":
        _dimension(size)
        return cls(tuple(tuple(int(i == j) for j in range(size))
                         for i in range(size)))

    def __add__(self, other: "Matrix") -> "Matrix":
        if type(other) is not Matrix or self.shape != other.shape:
            raise GraphSemanticsError("addition requires equal boundary dimensions")
        return Matrix(tuple(tuple(a+b for a, b in zip(left, right))
                            for left, right in zip(self.entries, other.entries)))

    def scaled(self, coefficient) -> "Matrix":
        c = gaussian(coefficient)
        return Matrix(tuple(tuple(c*x for x in row) for row in self.entries))

    def __matmul__(self, other: "Matrix") -> "Matrix":
        if type(other) is not Matrix or self.shape[1] != other.shape[0]:
            raise GraphSemanticsError("composition has mismatched middle boundary")
        rows, inner = self.shape
        columns = other.shape[1]
        return Matrix(tuple(tuple(sum((self.entries[i][k]*other.entries[k][j]
                                      for k in range(inner)), Gaussian())
                                  for j in range(columns)) for i in range(rows)))

    def dagger(self) -> "Matrix":
        rows, columns = self.shape
        return Matrix(tuple(tuple(self.entries[i][j].conjugate()
                                  for i in range(rows)) for j in range(columns)))

    def tensor(self, other: "Matrix") -> "Matrix":
        if type(other) is not Matrix:
            raise GraphSemanticsError("matrix tensor factor required")
        a, b = self.shape
        c, d = other.shape
        return Matrix(tuple(tuple(self.entries[i][j]*other.entries[k][ell]
                                  for j in range(b) for ell in range(d))
                            for i in range(a) for k in range(c)))

    def apply(self, values) -> tuple[Gaussian, ...]:
        v = tuple(gaussian(x) for x in values)
        if len(v) != self.shape[1]:
            raise GraphSemanticsError("state and input boundary differ")
        return tuple(sum((a*x for a, x in zip(row, v)), Gaussian())
                     for row in self.entries)

    def trace(self) -> Gaussian:
        if self.shape[0] != self.shape[1]:
            raise GraphSemanticsError("trace requires square matrix")
        return sum((self.entries[i][i] for i in range(self.shape[0])), Gaussian())

    def is_isometry(self) -> bool:
        return self.dagger() @ self == Matrix.identity(self.shape[1])

    def is_unitary(self) -> bool:
        return self.shape[0] == self.shape[1] and self.is_isometry()


@dataclass(frozen=True)
class Edge:
    """An edge from layer k to k+1; parallel edges are allowed."""

    layer: int
    source: int
    target: int
    amplitude: Gaussian = Gaussian(1)

    def __post_init__(self):
        object.__setattr__(self, "amplitude", gaussian(self.amplitude))


@dataclass(frozen=True)
class LayeredGraph:
    """Finite acyclic amplitude graph with ordered input/output boundaries.

    A one-layer graph has no edges and denotes the identity. Empty edge
    families with two or more layers denote zero maps. Each complete path
    contributes its ordered weight product; alternative paths add coherently.
    """

    dimensions: tuple[int, ...]
    edges: tuple[Edge, ...]

    def __post_init__(self):
        if type(self.dimensions) is not tuple or not self.dimensions:
            raise GraphSemanticsError("nonempty immutable dimension sequence required")
        for n in self.dimensions:
            _dimension(n)
        if type(self.edges) is not tuple:
            raise GraphSemanticsError("immutable edge family required")
        for edge in self.edges:
            if type(edge) is not Edge or type(edge.layer) is not int:
                raise GraphSemanticsError("declared exact edge required")
            if not 0 <= edge.layer < len(self.dimensions)-1:
                raise GraphSemanticsError("edge does not join successive layers")
            _index(edge.source, self.dimensions[edge.layer])
            _index(edge.target, self.dimensions[edge.layer+1])

    @classmethod
    def from_matrix(cls, matrix: Matrix) -> "LayeredGraph":
        if type(matrix) is not Matrix:
            raise GraphSemanticsError("exact matrix required")
        rows, columns = matrix.shape
        edges = tuple(Edge(0, j, i, matrix.entries[i][j])
                      for i in range(rows) for j in range(columns)
                      if matrix.entries[i][j] != Gaussian())
        return cls((columns, rows), edges)

    def matrix(self) -> Matrix:
        result = Matrix.identity(self.dimensions[0])
        for layer, (columns, rows) in enumerate(zip(self.dimensions,
                                                  self.dimensions[1:])):
            coefficients = [[Gaussian() for _ in range(columns)] for _ in range(rows)]
            for edge in self.edges:
                if edge.layer == layer:
                    coefficients[edge.target][edge.source] += edge.amplitude
            result = Matrix(tuple(tuple(row) for row in coefficients)) @ result
        return result

    def path_sum(self, source: int, target: int) -> Gaussian:
        """Independent explicit edge-path enumeration; exponential on dense graphs."""
        _index(source, self.dimensions[0])
        _index(target, self.dimensions[-1])

        def walk(layer, vertex):
            if layer == len(self.dimensions)-1:
                return Gaussian(int(vertex == target))
            return sum((edge.amplitude * walk(layer+1, edge.target)
                        for edge in self.edges
                        if edge.layer == layer and edge.source == vertex), Gaussian())

        return walk(0, source)

    def then(self, after: "LayeredGraph") -> "LayeredGraph":
        if type(after) is not LayeredGraph or self.dimensions[-1] != after.dimensions[0]:
            raise GraphSemanticsError("graph composition boundary mismatch")
        offset = len(self.dimensions)-1
        shifted = tuple(Edge(e.layer+offset, e.source, e.target, e.amplitude)
                        for e in after.edges)
        return LayeredGraph(self.dimensions+after.dimensions[1:], self.edges+shifted)

    def dagger(self) -> "LayeredGraph":
        last_edge_layer = len(self.dimensions)-2
        return LayeredGraph(tuple(reversed(self.dimensions)),
                            tuple(Edge(last_edge_layer-e.layer, e.target, e.source,
                                       e.amplitude.conjugate()) for e in self.edges))

    def tensor(self, other: "LayeredGraph") -> "LayeredGraph":
        """Canonical bipartite presentation of the tensor's matrix equivalence class."""
        if type(other) is not LayeredGraph:
            raise GraphSemanticsError("graph tensor factor required")
        return LayeredGraph.from_matrix(self.matrix().tensor(other.matrix()))

    def equivalent(self, other: "LayeredGraph") -> bool:
        return type(other) is LayeredGraph and self.matrix() == other.matrix()


def born_probabilities(state) -> tuple[Q, ...]:
    """Born readout of an already normalized pure state; never silently renormalize."""
    v = tuple(gaussian(x) for x in state)
    if not v or squared_norm(v) != 1:
        raise GraphSemanticsError("unit norm required for deterministic Born readout")
    return tuple(z.real*z.real+z.imag*z.imag for z in v)


def pure_density(values) -> Matrix:
    """Normalize a nonzero Q(i) ray as a density, without adjoining square roots."""
    v = tuple(gaussian(x) for x in values)
    norm = squared_norm(v)
    if not v or not norm:
        raise GraphSemanticsError("nonzero pure-state ray required")
    return Matrix(tuple(tuple(x*y.conjugate()*Q(1, norm) for y in v) for x in v))


def channel_action(kraus: tuple[Matrix, ...], matrix: Matrix) -> Matrix:
    """Linear Kraus action on any square matrix; density validity is a separate premise.

    Completeness is checked exactly. For a genuine density the returned matrix
    is a genuine density by the standard Kraus argument. This function does not
    certify a supplied matrix positive merely because its trace is one.
    """
    if not kraus or any(type(k) is not Matrix for k in kraus):
        raise GraphSemanticsError("nonempty exact Kraus family required")
    rows, columns = kraus[0].shape
    if matrix.shape != (columns, columns) or any(k.shape != (rows, columns) for k in kraus):
        raise GraphSemanticsError("Kraus boundaries or matrix dimensions differ")
    completeness = Matrix.zero(columns, columns)
    result = Matrix.zero(rows, rows)
    for k in kraus:
        completeness = completeness + k.dagger() @ k
        result = result + k @ matrix @ k.dagger()
    if completeness != Matrix.identity(columns):
        raise GraphSemanticsError("Kraus family is not trace preserving")
    return result


def kraus_graph(kraus: tuple[Matrix, ...]) -> LayeredGraph:
    """V|psi> = sum_o |o> tensor K_o|psi>; order is outcome then system."""
    if not kraus or any(type(k) is not Matrix for k in kraus):
        raise GraphSemanticsError("nonempty exact Kraus family required")
    rows, columns = kraus[0].shape
    if any(k.shape != (rows, columns) for k in kraus):
        raise GraphSemanticsError("Kraus boundaries differ")
    stacked = Matrix(tuple(row for k in kraus for row in k.entries))
    if not stacked.is_isometry():
        raise GraphSemanticsError("record-retaining Kraus map must be an isometry")
    return LayeredGraph.from_matrix(stacked)


def compile_record_instrument(instrument) -> LayeredGraph:
    """Compile the existing exact real-qubit Instrument, preserving outcome order."""
    from .quantum_records import Instrument
    if type(instrument) is not Instrument:
        raise GraphSemanticsError("existing quantum_records.Instrument required")
    return kraus_graph(tuple(Matrix(k) for _, k in instrument.outcomes))


def linearize_function(table: tuple[int, ...], output_size: int) -> LayeredGraph:
    """L_f|x> = |f(x)>; an isometry exactly when the finite table is injective."""
    _dimension(output_size)
    if type(table) is not tuple or not table:
        raise GraphSemanticsError("nonempty immutable finite function table required")
    for y in table:
        _index(y, output_size)
    return LayeredGraph((len(table), output_size),
                        tuple(Edge(0, x, y) for x, y in enumerate(table)))


def reversible_oracle(table: tuple[int, ...], output_size: int) -> LayeredGraph:
    """Permutation |x,y> -> |x,y+f(x) mod m>, retaining the source register."""
    linearize_function(table, output_size)  # validates the exact table
    size = len(table)*output_size
    return LayeredGraph((size, size), tuple(
        Edge(0, x*output_size+y, x*output_size+(y+table[x]) % output_size)
        for x, y in product(range(len(table)), range(output_size))))


def compile_source_lambda(modulus: int, operation: str, prime: int | None = None) -> LayeredGraph:
    """Compile actual source_lambda residue Succ or PrimeMul evaluation tables.

    This is a finite extensional adapter, not a compiler for arbitrary recursive
    programs. No primitive observation is performed and no source history is
    authenticated by the declared passport.
    """
    from .source_lambda import Atlas, Passport, PrimeMul, Residue, Succ, execute
    if type(modulus) is not int or modulus < 2:
        raise GraphSemanticsError("residue modulus must be at least two")
    if operation not in ("succ", "prime_mul") or (operation == "succ" and prime is not None):
        raise GraphSemanticsError("choose an actual Succ or PrimeMul source operation")
    atlas = Atlas(Passport("ym_graph_source_lambda", 0, "modular-Z"), ())
    table = []
    for value in range(modulus):
        residue = Residue(modulus, value)
        term = Succ(residue) if operation == "succ" else PrimeMul(prime, residue)
        outcome = execute(term, atlas)
        if outcome.observed:
            raise ArithmeticError("closed residue arithmetic unexpectedly read a source")
        table.append(outcome.value)
    return linearize_function(tuple(table), modulus)


def truncated_successor(size: int) -> LayeredGraph:
    """P_N S P_N: last basis state is killed; this is not cyclic successor."""
    _dimension(size)
    return LayeredGraph((size, size), tuple(Edge(0, j, j+1) for j in range(size-1)))
