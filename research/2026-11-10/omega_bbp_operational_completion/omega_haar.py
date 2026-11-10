"""Source-first Omega(4/5)-Haar operations (research prototype).

All source/projection algebra is exact Fraction arithmetic. Complex branch
DFT is approximate and is only used for calibration of algebraic identities.
No claim of source-selected parity balance or pi normality is made.
"""
from fractions import Fraction
from cmath import exp, pi

Q = Fraction(1, 16)


def source(n: int, *, mutate: bool = False) -> Fraction:
    """BBP R(n), n>=0. mutate removes final negative pole."""
    assert isinstance(n, int) and n >= 0
    r = (Fraction(4, 8*n+1) - Fraction(2, 8*n+4)
         - Fraction(1, 8*n+5))
    return r if mutate else r - Fraction(1, 8*n+6)


def source_block(n: int, width: int = 6, *, mutate: bool = False) -> tuple[Fraction, ...]:
    assert width >= 1
    return tuple(source(n+j, mutate=mutate) for j in range(width))


def block_forcing(n: int, width: int, *, mutate: bool = False) -> Fraction:
    return sum((Q**j * source(n+j, mutate=mutate) for j in range(width)), Fraction())


def fold(n: int, width: int, future: Fraction, *, mutate: bool = False) -> Fraction:
    return block_forcing(n, width, mutate=mutate) + Q**width * future


def grouped_fold(n: int, widths: tuple[int, ...], future: Fraction, *, mutate: bool = False) -> Fraction:
    """F_(w0)(F_(w1)(... future shifted by later blocks))."""
    residual = future
    # Construct from the right, at corresponding source index.
    for i in range(len(widths)-1, -1, -1):
        residual = fold(n+sum(widths[:i]), widths[i], residual, mutate=mutate)
    return residual


def partition_mean(values: tuple[Fraction, ...], group_size: int) -> tuple[Fraction, ...]:
    assert len(values) == 6 and group_size in (2, 3)
    out = []
    for j in range(0, 6, group_size):
        chunk = values[j:j+group_size]
        out.extend([sum(chunk, Fraction()) / group_size] * group_size)
    return tuple(out)


def commutator(values: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    """P2 P3 - P3 P2 for chronological adjacent-block Haar coarse means."""
    a = partition_mean(partition_mean(values, 3), 2)
    b = partition_mean(partition_mean(values, 2), 3)
    return tuple(x-y for x,y in zip(a,b))


def commutator_closed(values: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    r = values
    x = (r[2]-r[3])/6
    y = (r[4]+r[5]-r[0]-r[1])/6
    return (x,x,y,-y,-x,-x)


def energy(values):
    return sum((x*x for x in values), Fraction())


def norm_squared_formula(values: tuple[Fraction, ...]) -> Fraction:
    r = values
    # Rank-two skew plane: squared singular value 2/9.
    return Fraction(2,9)*( ((r[0]+r[1]-r[4]-r[5])/2)**2
                           + ((r[3]-r[2])**2)/2 )


def inverse_scalar_reconstruction(values: tuple[Fraction, ...]):
    """Minimum-Euclidean-norm inverse of the one-dimensional q-weighted six-block observation.

    No source constraint is imposed.  Loss of the five-dimensional kernel is exact.
    """
    assert len(values) == 6
    w = tuple(Q**j for j in range(6))
    scalar = sum((a*b for a,b in zip(values, w)), Fraction())
    denom = energy(w)
    guess = tuple(scalar*a/denom for a in w)
    lost = tuple(a-b for a,b in zip(values,guess))
    assert sum((a*b for a,b in zip(lost,w)), Fraction()) == 0
    return scalar, guess, lost


def branch_dft(values: tuple[complex, ...]) -> tuple[complex, ...]:
    assert len(values)==16
    return tuple(sum(values[k]*exp(-2j*pi*m*k/16) for k in range(16))/16
                 for m in range(16))


def branch_idft(details: tuple[complex, ...]) -> tuple[complex, ...]:
    assert len(details)==16
    return tuple(sum(details[m]*exp(2j*pi*m*k/16) for m in range(16))
                 for k in range(16))


def fiber_at(t: float, f) -> tuple[complex, ...]:
    return tuple(complex(f((t+k)/16)) for k in range(16))


def branch_parity_detail(values: tuple[complex, ...]) -> complex:
    assert len(values)==16
    return sum(((-1)**k)*values[k] for k in range(16))/16


def residue_23_mixed(values: tuple[Fraction, ...]) -> tuple[Fraction, Fraction]:
    """CRT-grid mixed Haar contrasts, unnormalized but exactly rational.

    CRT 2x3 matrix rows [r0,r4,r2] and [r3,r1,r5].
    Mixed contrasts vanish iff row difference is constant in the 3 column positions.
    """
    assert len(values)==6
    d0 = values[0] - values[3]
    d1 = values[4] - values[1]
    d2 = values[2] - values[5]
    return (d0-d1, d0+d1-2*d2)


def reversal(values):
    return tuple(reversed(values))


def chronological_area(n: int, *, mutate: bool = False) -> Fraction:
    """Source-oriented two-window skew pairing <r_n, [P2,P3]r_(n+1)>.

    Its sign is fixed relative to the declared positive clock direction and
    projection order; swapping observer order reverses it.
    """
    r = source_block(n, mutate=mutate)
    r_next = source_block(n+1, mutate=mutate)
    return sum((a*b for a,b in zip(r,commutator(r_next))), Fraction())

def forward_branch_erasure(t: Fraction, j: int) -> tuple[Fraction, ...]:
    """Exact phase output of all sixteen inverse branches after j>=0 forward steps."""
    assert isinstance(t,Fraction) and 0<=t<1 and j>=0
    return tuple((16**j * (t+k)/16)%1 for k in range(16))
