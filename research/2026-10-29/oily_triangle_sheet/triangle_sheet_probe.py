"""Exact finite probes for SUCC's Oily order-statistic triangle.

Research-only.  Fractions certify finite identities; no statement about
selected BBP Fourier cancellation or pi normality is implemented here.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb, factorial


def validate_nonnegative_int(n: int) -> None:
    if type(n) is not int or n < 0:
        raise ValueError("expected a nonnegative integer")


def as_source_coordinate(x) -> Q:
    q = Q(x)
    if not 0 <= q <= 1:
        raise ValueError("source coordinate must lie in [0,1]")
    return q


def source_weight(x) -> Q:
    x = as_source_coordinate(x)
    return Q(1) / ((2 - x*x) * (x*x - 2*x + 2))


def source_kernel(x) -> Q:
    x = as_source_coordinate(x)
    return (1-x) * source_weight(x)


def two_geometric_parameters(x) -> tuple[Q, Q]:
    x = as_source_coordinate(x)
    return x - x*x/2, x*x/2


def conditional_grade_pgf(x, z) -> Q:
    """Two authentic conditional geometric stages, rational arguments."""
    u, v = two_geometric_parameters(x)
    z = Q(z)
    if not 0 <= z <= 1:
        raise ValueError("this finite real PGF probe uses z in [0,1]")
    return (1-u)*(1-v)/((1-z*u)*(1-z*v))


def endpoint_grade_pgf(z) -> Q:
    z = Q(z)
    if not 0 <= z <= 1:
        raise ValueError("z must lie in [0,1]")
    return Q(1)/(2-z)**2


def endpoint_shadow(z) -> Q:
    """H(z)=2G(z)-z G'(z), exact inherited boundary coefficient."""
    z = Q(z)
    if not 0 <= z <= 1:
        raise ValueError("z must lie in [0,1]")
    return 4*(1-z)/(2-z)**3


def grade_mass(j: int) -> Q:
    validate_nonnegative_int(j)
    return Q(j+1, 2**(j+2))


def gamma_poisson_posterior_mean(j: int) -> Q:
    """Z|J=j ~ Gamma(shape=j+2, rate=2): mean=(j+2)/2."""
    validate_nonnegative_int(j)
    return Q(j+2, 2)


def uniform_rank_insert(ordered: tuple[Q, ...], value) -> tuple[Q, ...]:
    """Median-of-three row update, including both boundary conventions."""
    if any(ordered[i] > ordered[i+1] for i in range(len(ordered)-1)):
        raise ValueError("row must be nondecreasing")
    value = as_source_coordinate(value)
    if any(not 0 <= x <= 1 for x in ordered):
        raise ValueError("row values must lie in [0,1]")
    old = (Q(0),) + tuple(ordered) + (Q(1),)
    return tuple(sorted((old[r-1], old[r], value))[1] for r in range(1, len(ordered)+2))


def beta_second_minimum_moment(a: int, k: int) -> Q:
    """E[(1-X)^k] for X=second-largest of a+2 uniforms."""
    validate_nonnegative_int(a)
    validate_nonnegative_int(k)
    answer = Q(1)
    for i in range(k):
        answer *= Q(2+i, a+3+i)
    return answer


def rejection_error_bound(a: int) -> Q:
    """For source acceptance: 1-alpha_a <= 6/(a+3)."""
    validate_nonnegative_int(a)
    return Q(6, a+3)


def rejection_first_jet_error(a: int) -> Q:
    """|1-alpha_a - 4/(a+3)| <= 36/((a+3)(a+4))."""
    validate_nonnegative_int(a)
    return Q(36, (a+3)*(a+4))


def forcing(k: int) -> Q:
    """Original signed four-pole BBP forcing; exact positive rational result."""
    if type(k) is not int or k < 1:
        raise ValueError("positive source index required")
    return Q(4,8*k-7)-Q(2,8*k-4)-Q(1,8*k-3)-Q(1,8*k-2)


def zero_seed_prefix(n: int) -> Q:
    """U_0=0, U_n=16 U_(n-1)+r(n)."""
    validate_nonnegative_int(n)
    u = Q()
    for k in range(1, n+1):
        u = 16*u + forcing(k)
    return u


def source_acceptance_counterweight(x, epsilon=Q(0)) -> Q:
    """Hostile family W_e=W*(1-e*(1-x)^2), 0<=e<=1."""
    x = as_source_coordinate(x)
    epsilon = Q(epsilon)
    if not 0 <= epsilon <= 1:
        raise ValueError("epsilon must lie in [0,1]")
    return source_weight(x)*(1-epsilon*(1-x)**2)


def laplace_mellin_rank_integer(r: int, q, s: int) -> Q:
    """E[Y^s e^(-qY)] for Gamma(r,1), integer s>=0."""
    if type(r) is not int or r < 1:
        raise ValueError("positive rank required")
    validate_nonnegative_int(s)
    q = Q(q)
    if q < 0:
        raise ValueError("q must be nonnegative")
    return Q(factorial(r+s-1), factorial(r-1))/(1+q)**(r+s)


def authentic_boundary_mixed(z, s: int) -> Q:
    """Independent Gamma(2) endpoint and two-geometric grade limit."""
    validate_nonnegative_int(s)
    return Q(factorial(s+1))*endpoint_grade_pgf(z)


def falsely_identified_boundary_mixed(z, s: int) -> Q:
    """Mutant model J|Y~Poisson(Y); same marginals, different joint."""
    validate_nonnegative_int(s)
    z = Q(z)
    if not 0 <= z <= 1:
        raise ValueError("z must lie in [0,1]")
    return Q(factorial(s+1))/(2-z)**(s+2)


# Pairs (a,b) represent a+b*lambda, lambda=(sqrt(5)-1)/2,
# satisfying lambda^2=1-lambda.  This is exact Q(sqrt(5)) arithmetic.
def golden_add(p: tuple[Q,Q], v: tuple[Q,Q]) -> tuple[Q,Q]:
    return (p[0]+v[0], p[1]+v[1])


def golden_multiply(p: tuple[Q,Q], v: tuple[Q,Q]) -> tuple[Q,Q]:
    return (p[0]*v[0]+p[1]*v[1], p[0]*v[1]+p[1]*v[0]-p[1]*v[1])


def golden_inverse(p: tuple[Q,Q]) -> tuple[Q,Q]:
    a,b = p
    norm=a*a-a*b-b*b
    if not norm:
        raise ZeroDivisionError("zero golden field element")
    return (Q(a-b,norm),Q(-b,norm))


def golden_power(p: tuple[Q,Q], n: int) -> tuple[Q,Q]:
    validate_nonnegative_int(n)
    out=(Q(1),Q(0))
    for _ in range(n):
        out=golden_multiply(out,p)
    return out


def golden_fixed_point_certificate() -> dict[str, tuple[Q,Q]]:
    """At z=lambda^2, G(z)=z and H(z)=4*lambda^4 (exact)."""
    lam=(Q(0),Q(1))
    one=(Q(1),Q(0))
    z=golden_power(lam,2)
    two_minus_z=golden_add((Q(2),Q(0)),(-z[0],-z[1]))
    gz=golden_power(golden_inverse(two_minus_z),2)
    one_minus_z=golden_add(one,(-z[0],-z[1]))
    hz=golden_multiply((Q(4),Q(0)),golden_multiply(one_minus_z,golden_power(golden_inverse(two_minus_z),3)))
    target=golden_multiply((Q(4),Q(0)),golden_power(lam,4))
    return {"lambda":lam,"z":z,"G(z)":gz,"H(z)":hz,"4lambda4":target}


def gamma_rank_recurrence_difference(r: int) -> tuple[Q, tuple[Q,Q]]:
    """D(r+1)-D(r)=1/r + lambda^(r+2); pieces kept separate."""
    if type(r) is not int or r < 1:
        raise ValueError("positive rank required")
    return Q(1,r),golden_power((Q(0),Q(1)),r+2)


if __name__ == "__main__":
    assert golden_fixed_point_certificate()["z"] == golden_fixed_point_certificate()["G(z)"]
    assert golden_fixed_point_certificate()["H(z)"] == golden_fixed_point_certificate()["4lambda4"]
    print("OILY_TRIANGLE_EXACT_BASIC_PASS")
