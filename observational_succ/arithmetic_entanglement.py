"""Exact rational quantum controls for a declared arithmetic factorization.

Rational rays are normalized at the density-matrix level, so Bell examples
need no floating square roots. These functions do not identify geometry.
Paper proofs: research/2026-10-22/INTERACTING_ARITHMETIC_TFD.md.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import gcd

from .unit_prime_succ import SourceError, integer, prime


def _q(x):
    if type(x) is not int and not isinstance(x, Q):
        raise SourceError("Exact integer/Fraction coefficients required")
    return Q(x)


def prime_split(n, p=2):
    """The genuine bijection n <-> (v_p(n), p-free part)."""
    integer(n, 1, 10**12)
    if not prime(p):
        raise SourceError("Genuine prime factor required")
    k = 0
    while n % p == 0:
        k, n = k + 1, n // p
    return k, n


def crt_split(n, a, b):
    """Finite CRT factorization; its carrier is Z/(ab), including zero."""
    integer(a, 2, 10000); integer(b, 2, 10000)
    integer(n, 0, a*b - 1)
    if gcd(a, b) != 1:
        raise SourceError("Coprime CRT factors required")
    return n % a, n % b


def rational_ray_density(amplitudes, coordinates=prime_split):
    """Return sparse rho[(left,right),(left,right)] for a nonzero real ray.

The coordinate map must be injective on the supplied support; silently
merging source basis states is not an allowed Hilbert identification.
"""
    vector = {}
    for n, amplitude in amplitudes.items():
        integer(n, 1, 10**12)
        amplitude = _q(amplitude)
        if not amplitude:
            continue
        pair = coordinates(n)
        if type(pair) is not tuple or len(pair) != 2 or pair in vector:
            raise SourceError("Injective two-factor coordinates required")
        vector[pair] = amplitude
    norm2 = sum((x*x for x in vector.values()), Q())
    if not norm2:
        raise SourceError("Nonzero ray required")
    return {(x, y): a*b/norm2 for x, a in vector.items()
            for y, b in vector.items()}


def reduced_density(rho, keep=0):
    """Exact partial trace of a supplied sparse bipartite matrix."""
    if type(keep) is not int or keep not in (0, 1):
        raise SourceError("Keep factor 0 or 1")
    out = defaultdict(Q)
    for (x, y), value in rho.items():
        if x[1-keep] == y[1-keep]:
            out[x[keep], y[keep]] += _q(value)
    return {key: value for key, value in out.items() if value}


def partial_transpose(rho, factor=1):
    if type(factor) is not int or factor not in (0, 1):
        raise SourceError("Transpose factor 0 or 1")
    out = {}
    for (x, y), value in rho.items():
        a, b = list(x), list(y)
        a[factor], b[factor] = b[factor], a[factor]
        out[tuple(a), tuple(b)] = _q(value)
    return out


def purity(matrix):
    """tr(M^2), exact; caller supplies the matrix whose purity is wanted."""
    return sum((_q(value)*_q(matrix.get((j, i), 0))
                for (i, j), value in matrix.items()), Q())


def dephase(rho):
    """Classical mixture control: retain only diagonal matrix entries."""
    return {(i, j): _q(x) for (i, j), x in rho.items() if i == j}


def exact_eigenvector(matrix, vector, eigenvalue):
    """Certify a supplied rational eigenpair, without a numerical eigensolver."""
    value = _q(eigenvalue)
    vec = {i: _q(x) for i, x in vector.items() if _q(x)}
    if not vec:
        raise SourceError("Nonzero eigenvector required")
    labels = set(vec) | {i for pair in matrix for i in pair}
    return all(sum((_q(matrix.get((i, j), 0))*x for j, x in vec.items()), Q())
               == value*vec.get(i, Q()) for i in labels)


def successor_entanglement_witness():
    before = rational_ray_density({1: 1, 2: 1})
    after = rational_ray_density({2: 1, 3: 1})
    pt = partial_transpose(after)
    # |v2=0,odd=1> - |v2=1,odd=3> is the negative PT eigenvector.
    negative = {(0, 1): Q(1), (1, 3): Q(-1)}
    return {
        "before_purity": purity(reduced_density(before)),
        "after_purity": purity(reduced_density(after)),
        "negative_eigenvalue": Q(-1, 2),
        "negative_eigenpair_verified": exact_eigenvector(pt, negative, Q(-1, 2)),
        "classical_control_pt_unchanged": partial_transpose(dephase(after)) == dephase(after),
        "successor_is_unitary": False,
        "geometry_reconstructed": False,
    }
