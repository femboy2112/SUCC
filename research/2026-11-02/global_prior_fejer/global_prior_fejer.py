"""Research-only exact BBP source / positive Fejer energy diagnostic.

Proofs and strict error bounds are in PROOFS.md. All trigonometric
evaluations here use floats and are exploratory, NOT interval certificates.
"""
from fractions import Fraction
from math import cos, sin, pi, isqrt


def original_r(n: int) -> Fraction:
    """The authentic four signed BBP poles. n starts at 1."""
    if n < 1:
        raise ValueError("n must be positive")
    return (Fraction(4, 8*n - 7) - Fraction(2, 8*n - 4)
            - Fraction(1, 8*n - 3) - Fraction(1, 8*n - 2))


def alpha_cutoff(b: int) -> Fraction:
    """The exact selected rational completion alpha_b."""
    if b < 0:
        raise ValueError("b must be nonnegative")
    total = Fraction(0)
    power = 1
    for j in range(1, b+1):
        power *= 16
        total += original_r(j) / power
    return total


def orbit_mod_one(q: Fraction, n: int):
    """Exact rational residues {16**t * q}, t=0,...,n-1."""
    a, d = q.numerator % q.denominator, q.denominator
    for _ in range(n):
        yield a, d
        a = (16*a) % d


def fourier_means(q: Fraction, n: int, h_max: int):
    """Exploratory complex Fourier means from exact rational phases."""
    if n <= 0 or h_max < 0:
        raise ValueError("invalid n or bandwidth")
    residues = list(orbit_mod_one(q, n))
    out = [complex(1.0)]
    for h in range(1, h_max+1):
        # Never divide huge ints as ordinary floats: this overflows.
        cs = [cos(2*pi*float(Fraction((h*a) % d, d))) for a, d in residues]
        ss = [sin(2*pi*float(Fraction((h*a) % d, d))) for a, d in residues]
        out.append(complex(sum(cs)/n, sum(ss)/n))
    return out


def fejer_energy(q: Fraction, n: int, h_max: int) -> float:
    """Positive Fejer pair energy, floating *observation* only."""
    cs = fourier_means(q, n, h_max)
    return 1.0 + 2.0 * sum((1-h/(h_max+1))*abs(cs[h])**2
                           for h in range(1, h_max+1))


def finite_completion_error_bound(n: int, h_max: int, b: int) -> Fraction:
    """Strict analytic bound on energy difference to actual pi orbit.

    Uses inherited original-source Gamma tail and rational pi<22/7:
    abs(E(alpha)-E(alpha_b)) <
       88*H*(H+2)/(315*n*(8*b+1)*(8*b+2)*16**(b-n)).
    For n>=1 and b>=n. This Fraction bound is rigorous; numerical
    fejer_energy is not an enclosure for the trigonometric expression.
    """
    if not 1 <= n <= b or h_max < 0:
        raise ValueError("require b>=n>=1 and h_max>=0")
    return (Fraction(88, 7)*h_max*(h_max+2)
            / (45*n*(8*b+1)*(8*b+2)*16**(b-n)))


def fib_pair_power(k: int):
    """Integer (a,b) with phi**k=a+b*phi in Z[phi]."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    a,b = 1,0
    for _ in range(k):
        a,b = b,a+b
    return a,b


def golden_bezout(k: int):
    """Exact signed inverse for both golden conjugate sheets."""
    a,b = fib_pair_power(k)
    aa,bb = fib_pair_power(k+1)
    d = a*bb-aa*b
    assert d in (-1,1)
    return d*bb,-d*b


def lucas_trace(k: int):
    """Integer trace phi**k + (1-phi)**k."""
    a,b = fib_pair_power(k)
    return 2*a+b


if __name__ == "__main__":
    for n in (32,64,128,256,512):
        H = isqrt(n)
        q = alpha_cutoff(n)
        print("N=%d H=%d E_observed=%.9f exact_Gamma_error_lt=%.3e" %
              (n,H,fejer_energy(q,n,H),
               float(finite_completion_error_bound(n,H,n))))
