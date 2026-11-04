"""Exact source-selected BBP circle-current shift-average and Gamma bridge.

Add-only research instrument. No pi digits, fitted randomness, Galois average,
physical current law, or pi-normality proof. All numerics are exact Fractions.
Original four signed Mellin terms and U_0=0 are immutable.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from math import lcm


def _positive_mesh(m: int, min_value: int = 2) -> int:
    if type(m) is not int or m < min_value:
        raise ValueError(f"integer mesh >= {min_value} required")
    return m


def _phase_cloud(phases) -> tuple[F, ...]:
    p = tuple(F(x) % 1 for x in phases)
    if not p:
        raise ValueError("at least one source-selected phase required")
    return p


def circle_distance(x: F) -> F:
    x = F(x) % 1
    return min(x, 1 - x)


def tent_kernel(x: F, mesh: int) -> F:
    """Circle-periodized triangular kernel (1-m*||x||)_+, m>=2."""
    _positive_mesh(mesh)
    return max(F(0), 1 - mesh * circle_distance(x))


def source_force(n: int) -> F:
    """Exactly the original BBP four signed terms; n is source time."""
    if type(n) is not int or n < 1:
        raise ValueError("original BBP source time n>=1 required")
    return F(4, 8*n-7) - F(2, 8*n-4) - F(1, 8*n-3) - F(1, 8*n-2)


def source_epoch(A: int) -> tuple[F, ...]:
    """Literal zero-seeded original real phase, n in [A,2A), no pi inputs."""
    if type(A) is not int or A < 1:
        raise ValueError("original positive epoch required")
    z = F(0)
    out = []
    for n in range(1, 2*A):
        z = (16*z + source_force(n)) % 1
        if n >= A:
            out.append(z)
    return tuple(out)


def independent_modular_epoch(A: int) -> tuple[F, ...]:
    """Second source evaluator: single common *odd* integer conductor."""
    if type(A) is not int or A < 1:
        raise ValueError("A positive integer required")
    fs = tuple(source_force(n) for n in range(1, 2*A))
    M = 1
    for f in fs:
        M = lcm(M, f.denominator)
    if M % 2 != 1:
        raise AssertionError("original BBP conductor must be odd")
    z = 0
    out = []
    for n, r in enumerate(fs, 1):
        z = (16*z + r.numerator * (M // r.denominator)) % M
        if n >= A:
            out.append(F(z, M))
    return tuple(out)


def bin_index(x: F, mesh: int, origin: F = F(0)) -> int:
    _positive_mesh(mesh, 1)
    y = (F(x) + F(origin)) % 1
    return (mesh*y).numerator // (mesh*y).denominator


def cylinder_counts(phases, mesh: int, origin: F = F(0)) -> Counter:
    phases = _phase_cloud(phases)
    _positive_mesh(mesh, 1)
    return Counter(bin_index(x, mesh, origin) for x in phases)


def cylinder_energy(phases, mesh: int, origin: F = F(0)) -> F:
    phases = _phase_cloud(phases)
    cnt = cylinder_counts(phases, mesh, origin)
    return F(mesh * sum(z*z for z in cnt.values()), len(phases)**2)


def translated_energy(phases, mesh: int) -> F:
    """Integral_0^1 E_mesh(phases+origin) d origin, via exact tent pairs."""
    phases = _phase_cloud(phases)
    _positive_mesh(mesh, 1)
    if mesh == 1:
        return F(1)  # one circle cylinder; tent formula starts at mesh>=2
    N = len(phases)
    sum_kernel = sum((tent_kernel(x-y, mesh) for x in phases for y in phases), F(0))
    return F(mesh, N*N) * sum_kernel


def independent_origin_integral(phases, mesh: int) -> F:
    """Independent exact *piecewise-constant* integration, no tent formula.

    Intended only for small oracle holdouts: all changes occur at
    origin=(j/mesh - x) mod1. Integrates rational-valued histogram energy.
    """
    phases = _phase_cloud(phases)
    _positive_mesh(mesh, 1)
    edges = {F(0), F(1)}
    for x in phases:
        edges.update((F(j, mesh)-x) % 1 for j in range(mesh))
    edges = sorted(edges)
    return sum(((hi-lo)*cylinder_energy(phases, mesh, (lo+hi)/2)
                for lo, hi in zip(edges, edges[1:])), F(0))


def exact_current_increment(phases, level: int, origin: F=F(0)) -> F:
    if type(level) is not int or level < 0:
        raise ValueError("level must be nonnegative")
    return cylinder_energy(phases, 16**(level+1), origin) - cylinder_energy(phases, 16**level, origin)


def independent_branch_square(phases, level: int, origin: F=F(0)) -> F:
    """Exact actual 16-child current imbalance formula, independent of E-difference."""
    if type(level) is not int or level < 0:
        raise ValueError("level must be nonnegative")
    cloud = _phase_cloud(phases)
    N = len(cloud)
    parents = cylinder_counts(cloud, 16**level, origin)
    children = cylinder_counts(cloud, 16**(level+1), origin)
    return 16**(level+1) * sum(
        ((F(children.get(16*w+j, 0),N) - F(a,16*N))**2
         for w,a in parents.items() for j in range(16)), F(0))


def translated_branch_increment(phases, level: int) -> F:
    """Average of nonnegative branch-current square, by exact pair kernels."""
    if type(level) is not int or level < 0:
        raise ValueError("nonnegative level required")
    return translated_energy(phases, 16**(level+1)) - translated_energy(phases, 16**level)


def canonical_vs_translated_bound(phases, mesh: int) -> dict:
    """E_mesh(origin=0) <= 4 * J_(mesh/2) for every even mesh>=4."""
    if _positive_mesh(mesh, 4) % 2:
        raise ValueError("even mesh>=4 required")
    E = cylinder_energy(phases, mesh)
    J = translated_energy(phases, mesh//2)
    if E > 4*J:
        raise AssertionError("deterministic two-scale domination failed")
    return {'canonical_energy': E, 'translation_averaged_half_mesh': J,
            'certified_upper': 4*J, 'proved_for_every_phase_cloud': True}


def gamma_tail_energy_transport_bound(A: int, mesh: int) -> F:
    """|J_m(X)-J_m(U)| <= m² (A-1)/(64 A³) by original monotone Gamma tail.

    The actual X_n=16^n*pi/16, U_n is original rational zero-seeded,
    and 0<T_n=X_n-U_n<1/(64n²), T_n strictly decreasing.
    This is a theorem bound, not a numerical verification of unknown pi.
    """
    if type(A) is not int or A<1:
        raise ValueError("A>=1 required")
    _positive_mesh(mesh)
    return F(mesh*mesh*(A-1),64*A*A*A)


def periodic_fixed_point_control(mesh: int, sample_count: int=32) -> dict:
    """T(1/5)=1/5 and J_m(point mass)=m: no false Haar inference."""
    _positive_mesh(mesh)
    if type(sample_count) is not int or sample_count < 1:
        raise ValueError("sample_count>=1")
    point=F(1,5)
    assert (16*point)%1==point
    p=(point,)*sample_count
    return {'original_seed': False, 'periodic_point':point,
            'canonical_energy':cylinder_energy(p,mesh),
            'translated_energy':translated_energy(p,mesh),
            'source_normality_proved':False}


def forced_boundary_mean(A: int, mesh: int) -> F:
    """Average over bin origins of the actual one-step forcing boundary crossings.

    For n in [A,2A), x_(n+1) = (16*x_n + r(n+1)) mod1.
    In the common translated partition, disagreement with unforced
    (16*x_n) mod1 has measure min(1,m*||r(n+1)||), independent of x_n.
    """
    if type(A) is not int or A < 1:
        raise ValueError("A>=1")
    _positive_mesh(mesh)
    return sum((min(F(1), mesh*circle_distance(source_force(n+1)))
                for n in range(A,2*A)), F(0))/A


def forced_boundary_cap(A: int, mesh: int) -> F:
    """Original source polynomial P(x)<15(1-x) yields expectation cap."""
    if type(A) is not int or A<1:
        raise ValueError("A positive")
    _positive_mesh(mesh)
    return F(15*mesh, (8*A+1)*(8*A+2))


def source_stationarity_ell1_cap(A: int, mesh: int) -> F:
    """Mean over shifts of L1 histogram distance mu_A - T_*mu_A.

    Endpoint contributes at most 2/A. Each forcing crossing contributes
    at most 2/A; this is still NOT a mixing estimate (periodic 1/5 control).
    """
    return F(2,A) + 2*forced_boundary_cap(A,mesh)
