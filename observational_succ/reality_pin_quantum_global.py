"""Exact finite witnesses for the Reality Pin thermal/source obstruction.

No logarithm or matrix exponential is approximated: diagonal energies cancel
from the tested commutator. These are synthetic mathematical witnesses.
"""
from fractions import Fraction as Q

from .boundary_realization_selection import matrix_inverse, matmul, rational
from .reciprocal_succ_fucc import genuine_prime


def arithmetic_interaction(size, sigma=2, additive=Q(1), primes=(2, 3)):
    """P_N [lambda(S+S*)+sum p^-sigma(Vp+Vp*)] P_N."""
    if type(size) is not int or size < 1:
        raise ValueError("positive integer source cutoff required")
    if type(sigma) is not int or sigma < 2:
        raise ValueError("exact witness uses integer sigma >= 2")
    additive = rational(additive)
    if len(set(primes)) != len(primes):
        raise ValueError("primitive source labels must not repeat")
    for p in primes:
        genuine_prime(p)
    result = [[Q(0) for _ in range(size)] for _ in range(size)]
    for n in range(1, size):
        result[n - 1][n] += additive
        result[n][n - 1] += additive
    for p in primes:
        for n in range(1, size // p + 1):
            result[n - 1][p * n - 1] += Q(1, p ** sigma)
            result[p * n - 1][n - 1] += Q(1, p ** sigma)
    return tuple(tuple(row) for row in result)


def arithmetic_density(size, beta=2):
    """Finite conditional arithmetic Gibbs density, not Gibbs for K."""
    if type(size) is not int or size < 1 or type(beta) is not int or beta < 2:
        raise ValueError("positive cutoff and integer beta >= 2 required")
    weights = tuple(Q(1, n ** beta) for n in range(1, size + 1))
    total = sum(weights)
    return tuple(w / total for w in weights)


def diagonal_commutator(matrix, weights):
    """[matrix, diag(weights)]; unspecified diagonal energies cancel."""
    weights = tuple(rational(w) for w in weights)
    if len(matrix) != len(weights) or any(len(row) != len(weights) for row in matrix):
        raise ValueError("matrix/density dimension mismatch")
    return tuple(tuple(rational(matrix[i][j]) * (weights[j] - weights[i])
                       for j in range(len(weights))) for i in range(len(weights)))


def transpose(matrix):
    return tuple(zip(*matrix))


def rational_mirror(operator, schmidt_matrix):
    """(D^-1 A D)^T for a real invertible rational D.

    Identity AD = D M^T is algebraic. A physical canonical purification
    separately requires D positive and normalization Tr(D^2)=1.
    """
    return transpose(matmul(matmul(matrix_inverse(schmidt_matrix), operator),
                            schmidt_matrix))


def quantum_global_receipt():
    interaction = arithmetic_interaction(3, 2, Q(-1, 4))
    density = arithmetic_density(3, 2)
    defect = diagonal_commutator(interaction, density)[0][2]
    return {
        "scope": "synthetic exact finite rational witnesses; no empirical data",
        "cutoff": 3,
        "sigma": 2,
        "beta": 2,
        "additive_lambda": "-1/4",
        "cancelled_1_to_2_edge": str(interaction[0][1]),
        "uncancelled_1_to_3_edge": str(interaction[0][2]),
        "conditional_density": [str(x) for x in density],
        "K_rho_minus_rho_K_1_3": str(defect),
        "old_arithmetic_density_stationary_for_new_K": False,
        "full_infinite_theorem_proved_by_this_finite_run": False,
    }
