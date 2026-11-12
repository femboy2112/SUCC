"""Finite, exact Q(i) controls for declared intervention readouts.

These are supplied channel models, not a quantum model of BBP dynamics.
The Gaussian scalar is reused from the existing arithmetic_tfd module;
the direct matrix contraction here is separate from the donor's channels.
"""

from fractions import Fraction as Q
from observational_succ.arithmetic_tfd import Gaussian as G


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, Q)):
        raise TypeError("exact rational required")
    return Q(x)


def matrix(rows):
    return tuple(tuple(G.coerce(x) for x in row) for row in rows)


def adjoint(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(len(a)))
                 for i in range(len(a[0])))


def multiply(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), G())
                       for j in range(len(b[0]))) for i in range(len(a)))


def tensor(a, b):
    return tuple(tuple(x * y for x in row_a for y in row_b)
                 for row_a in a for row_b in b)


def scaled(a, factor):
    return tuple(tuple(x * factor for x in row) for row in a)


def trace(a):
    return sum((a[i][i] for i in range(len(a))), G())


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def controlled_rotation(c, s):
    c, s = rational(c), rational(s)
    if c*c + s*s != 1:
        raise ValueError("the declared rotation must be normalized")
    return matrix([[1, 0, 0, 0], [0, 1, 0, 0],
                   [0, 0, c, -s], [0, 0, s, c]])


def input_isometry():
    return matrix([[1, 0], [0, 0], [0, 1], [0, 0]])


def effective_effect(unitary, meter_effect):
    j = input_isometry()
    w = multiply(unitary, j)
    return multiply(multiply(adjoint(w), tensor(eye(2), meter_effect)), w)


def partial_trace_last(rho, first_dim, last_dim):
    if len(rho) != first_dim * last_dim:
        raise ValueError("dimension mismatch")
    return tuple(tuple(sum((rho[i*last_dim+k][j*last_dim+k]
                            for k in range(last_dim)), G())
                       for j in range(first_dim)) for i in range(first_dim))


def partial_trace_first(rho, first_dim, last_dim):
    if len(rho) != first_dim * last_dim:
        raise ValueError("dimension mismatch")
    return tuple(tuple(sum((rho[k*last_dim+i][k*last_dim+j]
                            for k in range(first_dim)), G())
                       for j in range(last_dim)) for i in range(last_dim))


def evolved_pair(rho, c, s):
    w = multiply(controlled_rotation(c, s), input_isometry())
    return multiply(multiply(w, rho), adjoint(w))


def bloch_density(x, y, z):
    x, y, z = rational(x), rational(y), rational(z)
    if x*x + y*y + z*z > 1:
        raise ValueError("Bloch vector is outside the state ball")
    return matrix([[Q(1, 2)*(1+z), G(x/2, -y/2)],
                   [G(x/2, y/2), Q(1, 2)*(1-z)]])


def inverse_coordinate(click_probability, s):
    probability, s = rational(click_probability), rational(s)
    if not s:
        raise ValueError("zero coupling cannot invert this readout")
    if not 0 <= probability <= s*s:
        raise ValueError("probability outside the calibrated response range")
    return 1 - 2*probability/(s*s)
