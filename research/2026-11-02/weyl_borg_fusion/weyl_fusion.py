"""Research-only, exact-rational probes for SUCC's selected BBP Weyl interfaces.

No claim of pi normality; no floating-point phase equality is used.
"""
from fractions import Fraction as F

C3 = F(77, 864)
C4 = F(28339, 172800)


def forcing(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("BBP source index must be a positive integer")
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def combined_forcing(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("BBP source index must be a positive integer")
    return F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def selected_states(N):
    if N < 0:
        raise ValueError("N must be nonnegative")
    u = F(0)
    result = []
    for n in range(1, N+1):
        u = 16*u + forcing(n)
        result.append(u)
    return result


def fractional(x):
    return x - (x.numerator // x.denominator)


def phase_coordinates(x, M):
    """Exact floor-cell label and residual, x interpreted on R/Z."""
    if not isinstance(M, int) or M < 1:
        raise ValueError("M must be a positive integer")
    f = fractional(x)
    a = (M*f).numerator // (M*f).denominator
    s = M*f-a
    assert 0 <= a < M and 0 <= s < 1
    return a, s


def fiber_exponent(x, M, h, q=0):
    """Exact exponent of Fourier frequency h+qM, assembled from the fiber."""
    a, s = phase_coordinates(x, M)
    return fractional(F(h*a, M) + (F(h, M)+q)*s)


def direct_exponent(x, h):
    return fractional(h*x)


def tau2(n):
    return F(1, 64*n*n)


def tau3(n):
    return tau2(n)-F(7, 512*n*n*n)


def green_interval(n, L):
    """Source-only rational enclosure for T_n; use r(m)<=m^-2 for m>=2."""
    if n < 1 or L < 1:
        raise ValueError("n and L must be positive")
    lower = sum((F(1, 16**j)*forcing(n+j) for j in range(1, L+1)), F(0))
    return lower, lower+F(1, 15*16**L*(n+L+1)**2)


def verify_green_bound(n, order, L):
    """Check the proved all-n Laurent bound against an independent finite tail enclosure."""
    lo, hi = green_interval(n, L)
    tau, C = (tau2(n), C3) if order == 2 else (tau3(n), C4) if order == 3 else (None, None)
    if tau is None:
        raise ValueError("order must be 2 or 3")
    eps = C / n**(order+1)
    return tau-eps <= lo and hi <= tau+eps


def moving_weyl_bound(N, h, order, J):
    """(2J + 2*pi*C_d*|h|/(d*J**d))/N; coefficients exact apart from pi."""
    if N < 1 or not 1 <= J <= N or not isinstance(h, int):
        raise ValueError("N,h,J invalid")
    if order not in (2, 3):
        raise ValueError("order must be 2 or 3")
    C = C3 if order == 2 else C4
    return F(2*J, N), F(2, order*N)*C*abs(h)/J**order  # bound = first + pi*second


def shifted_frequency_bound(N, h, k, J):
    """Bound |S_N(16^k h)-S_N(h)|/N by first + pi*second."""
    if N < 1 or k < 0 or not 1 <= J <= N or not isinstance(h, int):
        raise ValueError("invalid N,h,k,J")
    return F(2*(k+J), N), F(2*abs(h)*16**k, 15*N*J)


def source_clock_residue(n, power):
    """Original odd-denominator BBP source residue modulo 16**power."""
    if power < 1:
        raise ValueError("positive refinement required")
    q = 16**power
    value = forcing(n)
    return (value.numerator * pow(value.denominator, -1, q)) % q
