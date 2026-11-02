"""Exact original four-pole BBP/Gamma source and conditional dyadic Haar machinery.

Research-only: provides all-M finite-tail certificates, not pi normality.
"""
from fractions import Fraction
from functools import lru_cache

COEFFICIENTS = (4, -2, -1, -1)
OFFSETS = (1, 4, 5, 6)


def source(n):
    if n < 1:
        raise ValueError("n >= 1")
    return sum((Fraction(c, 8 * (n - 1) + a)
                for c, a in zip(COEFFICIENTS, OFFSETS)), Fraction())


def source_independent_polynomial(n):
    if n < 1:
        raise ValueError("n >= 1")
    return Fraction(120 * n * n - 89 * n + 16,
                    (2 * n - 1) * (4 * n - 1) * (8 * n - 7) * (8 * n - 3))


def source_gamma_ratio_derivative(n):
    """One eighth log derivative of the Gamma unit ratio; rational by Gamma recurrence."""
    if n < 1:
        raise ValueError("n >= 1")
    t = n - 1
    return sum((Fraction(c, 8) / Fraction(8*t+a, 8)
                for c, a in zip(COEFFICIENTS, OFFSETS)), Fraction())


def laplace_polynomial_coefficients():
    """Product (1-u)(u^2+2)(u^2+2u+2); exact independent convolution."""
    def multiply(a, b):
        out = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] += x * y
        return out
    return tuple(multiply(multiply((1, -1), (2, 0, 1)), (2, 2, 1)))


def source_from_laplace(n):
    """Integral from 0 to 1 of u^(8n-8)P(u) du, computed exactly."""
    if n < 1:
        raise ValueError("n >= 1")
    return sum((Fraction(c, 8*n-7+i)
                for i, c in enumerate(laplace_polynomial_coefficients())), Fraction())


@lru_cache(maxsize=32)
def bbp_alpha_partial(M):
    """Exact original alpha_M; no preloaded pi digits."""
    if M < 0:
        raise ValueError("M >= 0")
    alpha = Fraction()
    for n in range(1, M+1):
        alpha += Fraction(1, 16**n) * source(n)
    return alpha


def gamma_tail_bracket(M):
    """Entire infinite tail alpha-alpha_M lies in returned exact rational bracket."""
    if M < 0:
        raise ValueError("M >= 0")
    den = (8*M+1)*(8*M+2)*16**M
    return Fraction(1, 4*den), Fraction(1, den)


def gamma_tail_l1_fourier_error_upper(h, M):
    """RATIONAL MULTIPLE OF PI bounding the TOTAL first-M phase error.

    Actual total error is <=pi * returned fraction.
    """
    if M < 1:
        raise ValueError("M >= 1")
    return Fraction(2*abs(h)*(16**(M+1)-16),
                    15*16**M*(8*M+1)*(8*M+2))


def original_states(N):
    """Actual unwrapped BBP U_n, with literal U_0=0."""
    u = Fraction()
    out = []
    for n in range(1, N+1):
        u = 16*u + source(n)
        out.append(u)
    return out


def exact_finite_future(n, M):
    """Finite original future correction U_n + T_n^M = 16^n alpha_M."""
    if not 0 <= n <= M:
        raise ValueError("0 <= n <= M")
    return sum((Fraction(1, 16**(k-n))*source(k)
                for k in range(n+1, M+1)), Fraction())


def gamma_weighted_lag(n, k):
    """Original source F(n,k)=U_(n+k)-16^k*U_n."""
    if n < 0 or k < 0:
        raise ValueError("n,k >= 0")
    return sum((16**(k-j)*source(n+j) for j in range(1,k+1)), Fraction())


def dyadic_level_energy(z, half_length):
    """(E_child, W_difference, E_parent) at one dyadic level.

    This numerical helper merely checks the algebra of the phase sequence
    supplied by the caller. A positive finite W is NOT an asymptotic theorem.
    """
    N = len(z)
    if half_length < 1 or N % (2*half_length):
        raise ValueError("2*half_length must divide the sequence length")
    child = difference = parent = 0
    for start in range(0, N, 2*half_length):
        left = sum(z[start:start+half_length])
        right = sum(z[start+half_length:start+2*half_length])
        child += abs(left)**2 + abs(right)**2
        difference += abs(left-right)**2
        parent += abs(left+right)**2
    return child, difference, parent


def certified_dyadic_bound(N, leaf_length, delta):
    """CONDITIONAL: requires full tree differential W>=delta*E at all levels."""
    if (N < 1 or N & (N-1) or leaf_length < 1 or
        leaf_length & (leaf_length-1) or N < leaf_length):
        raise ValueError("N and leaf_length must be powers of two")
    if not 0 <= delta <= 2:
        raise ValueError("0 <= delta <= 2")
    layers = (N//leaf_length).bit_length()-1
    return (1-delta/2)**(layers/2)


def mean_prefix_bound(N, leaf_length, delta):
    """CONDITIONAL: bound every prefix / N under the per-node dyadic hypothesis."""
    if (N < 1 or N & (N-1) or leaf_length < 1 or
        leaf_length & (leaf_length-1) or N < leaf_length):
        raise ValueError("N and leaf_length must be powers of two")
    if not 0 <= delta <= 2:
        raise ValueError("0 <= delta <= 2")
    q = 1-delta/2
    return leaf_length/N + sum(
        (ell/N)*q**(((ell//leaf_length).bit_length()-1)/2)
        for ell in (leaf_length*2**j for j in range((N//leaf_length).bit_length())))
