"""Golden-weighted Pascal / harmonic identities, exact in Q(sqrt(5)).

Independent research-only instrument. A pair (a,b) means a+b*lambda where
lambda=(sqrt(5)-1)/2 and lambda^2=1-lambda. No π normality inference.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb

ONE = (F(1), F(0))
ZERO = (F(0), F(0))
LAMBDA = (F(0), F(1))
LAMBDA_SQUARED = (F(1), F(-1))


def _natural(n: int) -> None:
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative int required")


def add(x: tuple[F, F], y: tuple[F, F]) -> tuple[F, F]:
    return (x[0] + y[0], x[1] + y[1])


def scale(x: tuple[F, F], a: F | int) -> tuple[F, F]:
    a = F(a)
    return (x[0] * a, x[1] * a)


def mul(x: tuple[F, F], y: tuple[F, F]) -> tuple[F, F]:
    a, b = x
    c, d = y
    # (a+bλ)(c+dλ) = (ac+bd) + (ad+bc-bd)λ
    return (a*c+b*d, a*d+b*c-b*d)


def pow_element(x: tuple[F,F], n: int) -> tuple[F,F]:
    _natural(n)
    ans = ONE
    while n:
        if n & 1:
            ans = mul(ans, x)
        x = mul(x, x)
        n //= 2
    return ans


def harmonic(n: int) -> F:
    _natural(n)
    return sum((F(1, j) for j in range(1, n + 1)), F(0))


def weighted_pascal(n: int, k: int) -> tuple[F,F]:
    _natural(n)
    if type(k) is not int or not 0 <= k <= n:
        raise ValueError("0 <= k <= n required")
    return scale(pow_element(LAMBDA, n + k), comb(n,k))


def pascal_row_mass(n: int) -> tuple[F,F]:
    _natural(n)
    return sum_golden(weighted_pascal(n,k) for k in range(n+1))


def sum_golden(values) -> tuple[F,F]:
    total = ZERO
    for v in values:
        total = add(total,v)
    return total


def harmonic_pascal_direct(n: int) -> tuple[F,F]:
    _natural(n)
    return sum_golden(scale(weighted_pascal(n,k), harmonic(k)) for k in range(n+1))


def harmonic_pascal_closed(n: int) -> tuple[F,F]:
    """A_n = H_n - sum_{j=1}^n λ^j / j, exact."""
    _natural(n)
    return add((harmonic(n),F(0)), scale(sum_golden(
        scale(pow_element(LAMBDA,j),F(1,j)) for j in range(1,n+1)), -1))


def harmonic_pascal_alternating(n: int) -> tuple[F,F]:
    """A_n = sum (-1)^(j+1) C(n,j) (λ²)^j/j, exact."""
    _natural(n)
    return sum_golden(scale(pow_element(LAMBDA_SQUARED,j),
                   F((-1)**(j+1)*comb(n,j),j)) for j in range(1,n+1))


def harmonic_increment(n: int) -> tuple[F,F]:
    """A_(n+1)-A_n = (1-λ^(n+1))/(n+1)."""
    _natural(n)
    return scale(add(ONE, scale(pow_element(LAMBDA,n+1),-1)), F(1,n+1))


def fibonacci_diagonal(n: int) -> int:
    """Sum of Pascal's shallow diagonal: sum_{k<=n/2} C(n-k,k)."""
    _natural(n)
    return sum(comb(n-k,k) for k in range(n//2+1))


def fibonacci(n: int) -> int:
    _natural(n)
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def binomial_golden_transform(n: int) -> tuple[F,F]:
    """Binomial transform of λ^k equals (1+λ)^n = λ^(-n)."""
    _natural(n)
    return sum_golden(scale(pow_element(LAMBDA,k),comb(n,k)) for k in range(n+1))


def golden_packet_fixed_point_residual() -> tuple[F,F]:
    """p*(2-p)^2 - 1 =0, p=λ²; no nonrational arithmetic. """
    p = LAMBDA_SQUARED
    two_minus_p = add((F(2),F(0)), scale(p,-1))
    return add(mul(p,pow_element(two_minus_p,2)),scale(ONE,-1))


if __name__ == "__main__":
    for n in range(21):
        assert pascal_row_mass(n) == ONE
        assert harmonic_pascal_direct(n) == harmonic_pascal_closed(n)
        assert harmonic_pascal_alternating(n) == harmonic_pascal_closed(n)
        assert add(harmonic_pascal_closed(n+1),scale(harmonic_pascal_closed(n),-1)) == harmonic_increment(n)
        assert fibonacci_diagonal(n) == fibonacci(n+1)
        assert binomial_golden_transform(n) == pow_element(add(ONE,LAMBDA),n)
    assert golden_packet_fixed_point_residual() == ZERO
    print("PASCAL_GOLDEN_HARMONIC_EXACT_PASS n=0..20")
