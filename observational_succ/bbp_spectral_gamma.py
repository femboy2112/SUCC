"""Finite exact 16x16 BBP transition diagnostics, spectrum/entropy firewalls.

The one-digit 2-adic spatial Haar lift from SUCC #566 is NOT the real digit
normality assertion. Eigenvalues of a finite transition matrix do not
identify its joint digit law, and no spectral Euler-gamma law is asserted.

This instrument uses exact integer/Fraction arithmetic and no numpy. The
opt-in research script handles the empirical numerical matrix spectrum.
"""
from __future__ import annotations
from fractions import Fraction
from math import log

DIM = 16


def _matrix(counts):
    if len(counts) != DIM or any(len(row) != DIM for row in counts):
        raise ValueError('16x16 counts required')
    if any(type(v) is not int or v < 0 for row in counts for v in row):
        raise ValueError('nonnegative integer counts required')
    return tuple(tuple(row) for row in counts)


def transition_counts(digits: str, *, cyclic: bool = False):
    """Counts of REAL chronological adjacent hex digits; cyclic wrap opt-in."""
    if not isinstance(digits, str) or len(digits) < 2:
        raise ValueError('two or more hexadecimal digits required')
    if any(ch not in '0123456789ABCDEFabcdef' for ch in digits):
        raise ValueError('invalid hexadecimal digit')
    ds = [int(ch, 16) for ch in digits]
    out = [[0]*DIM for _ in range(DIM)]
    for i in range(len(ds) if cyclic else len(ds)-1):
        out[ds[i]][ds[(i+1)%len(ds)]] += 1
    return _matrix(out)


def margins(counts):
    c = _matrix(counts)
    return (tuple(map(sum, c)),
            tuple(sum(c[a][b] for a in range(DIM)) for b in range(DIM)))


def energies(counts):
    """Exactly Erow, Ecol, E2, E225; finite 16x16 Parseval."""
    c = _matrix(counts)
    row, col = margins(c)
    n = sum(row)
    if n == 0:
        raise ValueError('positive sample count required')
    e_row = Fraction(16*sum(a*a for a in row), n*n)-1
    e_col = Fraction(16*sum(b*b for b in col), n*n)-1
    e_two = Fraction(256*sum(v*v for r in c for v in r),n*n)-1
    mixed = e_two-e_row-e_col
    if mixed < 0:
        raise ArithmeticError('orthogonal mixed projection negative')
    return e_row, e_col, e_two, mixed


def difference_counts(counts):
    """Counts of delta = current_digit - next_digit modulo 16."""
    c = _matrix(counts)
    return tuple(sum(c[a][b] for a in range(DIM) for b in range(DIM)
                     if (a-b)%DIM == k) for k in range(DIM))


def opposite_frequency_energy(counts):
    """Exact sum_{h=1}^{15}|M(h,-h)|^2, no complex roundoff."""
    q = difference_counts(counts)
    n = sum(q)
    if n == 0:
        raise ValueError('positive sample count required')
    return Fraction(DIM*sum(v*v for v in q),n*n)-1


def empirical_transition(counts):
    """Conditional row transition P, exact Fractions; rejects empty rows."""
    c = _matrix(counts)
    row,_=margins(c)
    if min(row) == 0:
        raise ValueError('all conditional rows need observations')
    return tuple(tuple(Fraction(c[a][b],row[a]) for b in range(DIM))
                 for a in range(DIM))


def haar_matrix():
    return tuple(tuple(Fraction(1,DIM) for _ in range(DIM)) for _ in range(DIM))


def time_spatial_map(d: int) -> int:
    """Exact low 2-adic nibble successor of source #566, NOT real π."""
    if type(d) is not int or not 0 <= d < 16:
        raise ValueError('digit 0..15')
    return ((d+1) if d % 2 == 0 else (d-3)) % 16


def time_spatial_permutation():
    return tuple(tuple(int(b == time_spatial_map(a)) for b in range(DIM))
                 for a in range(DIM))


def permutation_clock(d: int) -> int:
    """Inverse of f(n)=2(n mod2)-n mod16 (it is an involution)."""
    if type(d) is not int or not 0 <= d < 16:
        raise ValueError('digit 0..15')
    return (2*(d%2)-d)%16


def root_of_unity_eigenvector(clock_mode: int):
    """Exact exponents q(d) in v(d)=exp(2πi q(d)/16)."""
    if type(clock_mode) is not int:
        raise ValueError('integer mode required')
    return tuple(clock_mode*permutation_clock(d)%16 for d in range(DIM))


def nilpotent_nonhaar_matrix():
    """Positive doubly stochastic P != J/16 with P^2=J/16 exactly.

    P=J/16 + u v^T/64, u=(1,-1,0...), v=(1,1,-2,0...).
    Its eigenvalues match Haar: 1 and 0 (multiplicity 15), while its
    pair distribution has strictly positive 225-mode energy.
    """
    u = (1,-1) + (0,)*(DIM-2)
    v = (1,1,-2) + (0,)*(DIM-3)
    return tuple(tuple(Fraction(1,DIM)+Fraction(u[a]*v[b],64)
                       for b in range(DIM)) for a in range(DIM))


def matmul(A,B):
    if len(A) != DIM or len(B) != DIM or any(len(r)!=DIM for r in A) or any(len(r)!=DIM for r in B):
        raise ValueError('16x16 input required')
    return tuple(tuple(sum(A[a][i]*B[i][b] for i in range(DIM))
                       for b in range(DIM)) for a in range(DIM))


def nonhaar_markov_pair_energy():
    """E225 for the nilpotent control, with stationary digit law uniform."""
    P = nilpotent_nonhaar_matrix()
    return sum((P[a][b]-Fraction(1,DIM))**2 for a in range(DIM) for b in range(DIM))


def harmonic_finite_part(n: int):
    """H_n - log(n): a generic harmonic-clock reference, NOT π data."""
    if type(n) is not int or n < 1:
        raise ValueError('positive integer')
    return sum(1/k for k in range(1,n+1))-log(n)


def dobrushin_coefficient(counts):
    """Exact contraction bound for NONTRIVIAL eigenvalues of row-stochastic P.

    delta(P)=max_(a<b) 1/2 sum_c |P_ac-P_bc|. Every eigenvalue
    different from 1 has modulus <=delta(P). This says nothing about
    higher-order conditional digit laws of the deterministic π stream.
    """
    P = empirical_transition(counts)
    return max(sum(abs(P[a][c]-P[b][c]) for c in range(DIM))/2
               for a in range(DIM) for b in range(a+1,DIM))
