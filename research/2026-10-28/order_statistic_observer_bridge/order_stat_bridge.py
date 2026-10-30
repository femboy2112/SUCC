"""Exact integer-order-statistic observer bridges for SUCC's genuine Pólya source.

This is a research-only probability model. No zeta-zero coordinates or physical
work claims enter its definitions. m is observer sample size, not a prime label.
"""
from fractions import Fraction
from math import log


def rising(n, k):
    assert n >= 1 and k >= 0
    result = 1
    for i in range(k):
        result *= n + i
    return result


def native_law(j):
    assert j >= 0
    return [Fraction(1, j + 1)] * (j + 1)


def native_birth(j, k):
    assert 0 <= k <= j
    return Fraction(k + 1, j + 2)


def beta_winner_law(m, j):
    """K_j | (U wins against m-1 IID uniforms), exact BetaBinomial(j;m,1)."""
    assert m >= 1 and j >= 0
    denom = rising(j + 1, m)
    return [Fraction(m * rising(k + 1, m - 1), denom) for k in range(j + 1)]


def winner_h(m, j, k):
    """Finite source/selected Radon-Nikodym martingale h_j(k)=m E[U^(m-1)|K_j=k]."""
    assert m >= 1 and 0 <= k <= j
    return Fraction(m * rising(k + 1, m - 1), rising(j + 2, m - 1))


def winner_acceptance(m, j, k):
    """P(U is maximum of m IID uniforms | observed K_j=k)."""
    return winner_h(m, j, k) / m


def winner_birth(m, j, k):
    assert m >= 1 and 0 <= k <= j
    return Fraction(k + m, j + m + 1)


def evolve(law, j, transition):
    assert len(law) == j + 1
    nxt = [Fraction(0)] * (j + 2)
    for k, p in enumerate(law):
        t = transition(j, k)
        assert 0 <= t <= 1
        nxt[k] += p * (1 - t)
        nxt[k + 1] += p * t
    return nxt


def winner_observed(m, j):
    """Postselection of unchanged source: witness wins among m IID uniforms."""
    u = native_law(j)
    weights = [winner_acceptance(m, j, k) for k in range(j + 1)]
    accept = sum((u[k] * weights[k] for k in range(j + 1)), Fraction(0))
    return [u[k] * weights[k] / accept for k in range(j + 1)], accept


def loss_observed(m, j):
    """Complementary observer branch, restoring unconditioned original source."""
    assert m >= 2
    u = native_law(j)
    accept = Fraction(m - 1, m)
    weights = [1 - winner_acceptance(m, j, k) for k in range(j + 1)]
    return [u[k] * weights[k] / accept for k in range(j + 1)], accept


def discrete_max_law(j, m):
    """Max of m *discrete* uniform grades; deliberately NOT the latent max bridge."""
    assert j >= 1 and m >= 1
    return [Fraction((k + 1) ** m - k ** m, (j + 1) ** m) for k in range(j + 1)]


def polya_history(j, m=1):
    """Exact distribution of complete binary histories under m,1 beta urn."""
    states = {(): Fraction(1)}
    for depth in range(j):
        new = {}
        for history, probability in states.items():
            k = sum(history)
            t = winner_birth(m, depth, k)
            new[history + (0,)] = probability * (1 - t)
            new[history + (1,)] = probability * t
        states = new
    return states


def info_bounds(m, j):
    """Finite forward KL and source-vs-posterior reverse KL, numerical diagnostics."""
    p, q = native_law(j), beta_winner_law(m, j)
    forward = sum(float(y) * log(float(y / x)) for x, y in zip(p, q))
    reverse = sum(float(x) * log(float(x / y)) for x, y in zip(p, q))
    return forward, reverse
