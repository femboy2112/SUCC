"""Exact arithmetic-weighted qutrit codes on genuine binary Bruhat--Tits balls.

The root tensor is the classical three-qutrit polynomial code, with a declared
amplitude deformation. Nonroot tensors are coherent copy ISOMETRIES, not cloning
channels. All outputs below use rational numerators and an explicit squared norm;
no floating square root is used as an exact certificate. The paper dossier proves
the statements for complex Hilbert spaces. This oracle tests rational amplitudes.
There is no gravitational, adelic, or RH claim.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Iterable

from .unit_prime_succ import prime as is_prime

Word = tuple[int, ...]
SparseVector = dict[Word, Fraction]
SparseMatrix = dict[tuple[Word, Word], Fraction]


def _q(value: int | Fraction) -> Fraction:
    if type(value) is not int and not isinstance(value, Fraction):
        raise ValueError("Exact integer or Fraction coordinates required")
    return Fraction(value)


def _trit(value: int) -> int:
    if type(value) is not int or value not in range(3):
        raise ValueError("A qutrit index is 0, 1, or 2")
    return value


def _region(region: Iterable[int], sites: int) -> tuple[int, ...]:
    result = tuple(region)
    if any(type(i) is not int or not 0 <= i < sites for i in result):
        raise ValueError("Boundary region contains an invalid site")
    if len(set(result)) != len(result):
        raise ValueError("Boundary sites must be distinct")
    return tuple(sorted(result))


def pair_decoder(pair: tuple[int, int], x: int, y: int) -> tuple[int, int]:
    """Unitary permutation coordinates (x_i,x_j) -> (logical k, erased t)."""
    pair = _region(pair, 3)
    if len(pair) != 2:
        raise ValueError("Exactly two root shares are needed")
    x, y = _trit(x), _trit(y)
    i, j = pair
    e = next(iter(set(range(3)) - set(pair)))
    k = ((y - x) * pow(j - i, -1, 3)) % 3
    return k, (x + (e - i) * k) % 3


@dataclass(frozen=True)
class ArithmeticTreeCode:
    """W_f|k> = sum_r f_r |r,r+k,r+2k> / sqrt(sum_r f_r^2).

    At radius R, each of the three entries is repeated 2^(R-1) times by
    actual binary descendant copy tensors. The root has valence three;
    internal nonroot vertices have one parent and two children. There is ONE
    logical qutrit at the root, not a hidden logical qutrit at every vertex.
    """

    amplitudes: tuple[Fraction, Fraction, Fraction] = (
        Fraction(1), Fraction(1), Fraction(1)
    )
    radius: int = 1

    def __post_init__(self) -> None:
        if type(self.radius) is not int or self.radius < 1:
            raise ValueError("A finite radius of at least one is required")
        if len(self.amplitudes) != 3:
            raise ValueError("Exactly three amplitude numerators are required")
        amplitudes = tuple(_q(f) for f in self.amplitudes)
        if not any(amplitudes):
            raise ValueError("The zero tensor cannot be normalized")
        object.__setattr__(self, "amplitudes", amplitudes)

    @property
    def squared_norm(self) -> Fraction:
        return sum((f * f for f in self.amplitudes), Fraction(0))

    @property
    def weights(self) -> tuple[Fraction, ...]:
        return tuple(f * f / self.squared_norm for f in self.amplitudes)

    @property
    def block_size(self) -> int:
        return 2 ** (self.radius - 1)

    @property
    def sites(self) -> int:
        return 3 * self.block_size

    def column(self, k: int) -> SparseVector:
        """Numerator of W|k>; divide by sqrt(squared_norm) mathematically."""
        k = _trit(k)
        return {
            tuple(value for i in range(3) for value in [(r + i * k) % 3] * self.block_size): f
            for r, f in enumerate(self.amplitudes) if f
        }

    def gram(self) -> tuple[tuple[Fraction, ...], ...]:
        columns = [self.column(k) for k in range(3)]
        return tuple(tuple(sum((v * columns[l].get(w, 0) for w, v in columns[k].items()), Fraction(0))
                           / self.squared_norm for l in range(3)) for k in range(3))

    def reduce_matrix_unit(self, k: int, l: int, keep: Iterable[int]) -> SparseMatrix:
        """Exact Tr_complement(W |k><l| W*), including coherences."""
        keep = _region(keep, self.sites)
        erased = tuple(i for i in range(self.sites) if i not in keep)
        result: SparseMatrix = {}
        for x, a in self.column(k).items():
            for y, b in self.column(l).items():
                if all(x[i] == y[i] for i in erased):
                    key = (tuple(x[i] for i in keep), tuple(y[i] for i in keep))
                    result[key] = result.get(key, 0) + a * b / self.squared_norm
        return {key: value for key, value in result.items() if value}

    def corrects_erasure(self, erased: Iterable[int]) -> bool:
        """Full complementary-channel/KL test on all nine logical matrix units."""
        erased = _region(erased, self.sites)
        fixed = self.reduce_matrix_unit(0, 0, erased)
        return all(self.reduce_matrix_unit(k, l, erased) == (fixed if k == l else {})
                   for k in range(3) for l in range(3))

    def full_branches(self, keep: Iterable[int]) -> tuple[int, ...]:
        keep = set(_region(keep, self.sites))
        m = self.block_size
        return tuple(i for i in range(3) if all(j in keep for j in range(i * m, (i + 1) * m)))

    def reconstructing_pair(self, keep: Iterable[int]) -> tuple[int, int]:
        """Choose a proved *-preserving decoder, never an arbitrary inverse."""
        branches = self.full_branches(keep)
        for pair in combinations(branches, 2):
            erased = tuple(i for i in range(3) if i not in pair)
            root_code = ArithmeticTreeCode(self.amplitudes)
            if root_code.corrects_erasure(erased):
                # The simple decoder below handles positive amplitudes or the
                # privileged pair, whose erased coordinate is exactly r.
                if pair == (1, 2) or len(set(self.amplitudes)) == 1:
                    return pair
        raise ValueError("No supported exact decoder on this boundary region")

    def boundary_matrix_unit(self, word: Word, a: int, b: int, keep: Iterable[int]) -> SparseVector:
        """Action of a boundary representative of |a><b| on one basis word.

        For refined balls this is a *-representation into the corner where
        both selected branch blocks are constant. It acts as identity on all
        unselected sites. Its unit equals identity ON THE CODE, not globally.
        """
        a, b = _trit(a), _trit(b)
        if len(word) != self.sites or any(type(x) is not int or x not in range(3) for x in word):
            raise ValueError("Wrong boundary word")
        i, j = self.reconstructing_pair(keep)
        e = next(iter(set(range(3)) - {i, j}))
        m = self.block_size
        if any(len(set(word[z * m:(z + 1) * m])) != 1 for z in (i, j)):
            return {}
        k, t = pair_decoder((i, j), word[i * m], word[j * m])
        if k != b:
            return {}
        result = list(word)
        for z in (i, j):
            result[z * m:(z + 1) * m] = [(t + (z - e) * a) % 3] * m
        return {tuple(result): Fraction(1)}

    def intertwining_defect(self, a: int, b: int, k: int, keep: Iterable[int]) -> SparseVector:
        """Exact numerator of (O_A W - W |a><b|)|k>."""
        result: SparseVector = {}
        for word, value in self.column(k).items():
            for image, coefficient in self.boundary_matrix_unit(word, a, b, keep).items():
                result[image] = result.get(image, 0) + value * coefficient
        if k == b:
            for word, value in self.column(a).items():
                result[word] = result.get(word, 0) - value
        return {word: value for word, value in result.items() if value}

    def refined(self) -> ArithmeticTreeCode:
        return ArithmeticTreeCode(self.amplitudes, self.radius + 1)

    def root_permutation_defect(self, permutation: tuple[int, int, int], k: int) -> SparseVector:
        """Exact (I-WW*) P_permutation W|k> numerator at radius one."""
        if self.radius != 1 or tuple(sorted(permutation)) != (0, 1, 2):
            raise ValueError("A root three-site permutation is required")
        vector = {tuple(word[i] for i in permutation): value for word, value in self.column(k).items()}
        result = dict(vector)
        for logical in range(3):
            column = self.column(logical)
            coefficient = sum((value * vector.get(word, 0) for word, value in column.items()), Fraction(0)) / self.squared_norm
            for word, value in column.items():
                result[word] = result.get(word, 0) - coefficient * value
        return {word: value for word, value in result.items() if value}

    def geometric_boundary(self):
        """Actual PGL_2(Q_2) lattice vertices, in root-branch DFS order."""
        from .padic_bulk_network import bt_sphere
        boundary = []
        for vertex in bt_sphere(2, 1):
            frontier = [vertex]
            for _ in range(self.radius - 1):
                frontier = [child for parent in frontier for child in parent.children()]
            boundary.extend(frontier)
        return tuple(boundary)


def arithmetic_code(prime: int, half_beta: int, radius: int = 1) -> ArithmeticTreeCode:
    """Authentic truncated prime-mode weights q=p^(-2*half_beta), exactly.

    Positivity/normalizability here is finite dimensional; it does not remove
    the global beta>1 condition for the full infinite-prime thermofield state.
    """
    if type(prime) is not int or not is_prime(prime):
        raise ValueError("Authentic prime required, not a composite generator")
    if type(half_beta) is not int or half_beta < 1:
        raise ValueError("Exact oracle requires positive integral half_beta")
    ratio = Fraction(1, prime**half_beta)
    return ArithmeticTreeCode((Fraction(1), ratio, ratio * ratio), radius)


def copy_refinement(vector: SparseVector) -> SparseVector:
    """Basis-copy isometry C: |x_1...x_n> -> |x_1,x_1,...,x_n,x_n>."""
    return {tuple(value for x in word for value in (x, x)): coefficient
            for word, coefficient in vector.items()}


def minimum_tree_cut(radius: int, keep: Iterable[int]) -> int:
    """Exact edge cut on the trivalent rooted binary-descendant ball.

    Boundary sites carry fixed colors A/complement; minimize disagreements
    over internal colors with dynamic programming, independent of code data.
    """
    code = ArithmeticTreeCode(radius=radius)
    keep = set(_region(keep, code.sites))
    infinity = code.sites + 1

    def subtree(start: int, size: int) -> tuple[int, int]:
        if size == 1:
            return (infinity, 0) if start in keep else (0, infinity)
        left = subtree(start, size // 2)
        right = subtree(start + size // 2, size // 2)
        return tuple(sum(min(cost[c] + (c != color) for c in (0, 1)) for cost in (left, right))
                     for color in (0, 1))

    children = [subtree(i * code.block_size, code.block_size) for i in range(3)]
    return min(sum(min(cost[c] + (c != root) for c in (0, 1)) for cost in children) for root in (0, 1))


def logical_filter_gram(factors: Iterable[int | Fraction]) -> tuple[tuple[Fraction, ...], ...]:
    """(W diag(f))* (W diag(f)); unlike internal weights, not generally I."""
    factors = tuple(_q(x) for x in factors)
    if len(factors) != 3:
        raise ValueError("Three logical filter factors required")
    return tuple(tuple(factors[i] ** 2 if i == j else Fraction(0) for j in range(3)) for i in range(3))


def nonstar_pair_control(code: ArithmeticTreeCode, pair: tuple[int, int],
                         word: Word, a: int, b: int) -> SparseVector:
    """Hostile control: bare intertwiner that generally FAILS adjoint transport.

    This is not a quantum recovery channel or a valid observable decoder.
    Nonuniform full-support weights permit algebraic inverse filtering, so
    O_A W=W O alone can yield a false positive for quantum error correction.
    """
    if code.radius != 1 or not all(code.amplitudes):
        raise ValueError("This countercontrol requires a radius-one full-support code")
    pair = _region(pair, 3)
    if len(pair) != 2 or len(word) != 3:
        raise ValueError("A two-share region and a three-site basis word are required")
    for x in word:
        _trit(x)
    a, b = _trit(a), _trit(b)
    i, j = pair
    e = next(iter(set(range(3)) - set(pair)))
    k, t = pair_decoder(pair, word[i], word[j])
    if k != b:
        return {}
    coefficient = code.amplitudes[(t - e * a) % 3] / code.amplitudes[(t - e * b) % 3]
    image = list(word)
    for z in pair:
        image[z] = (t + (z - e) * a) % 3
    return {tuple(image): coefficient}
