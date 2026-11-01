"""Exact 3-by-5 conductor countermodels for authentic BBP forcing.

The seeds c/q - pi/16 are symbolic irrational COUNTERFACTUALS. They never
replace the selected zero seed. All returned certificates are rational.
Paper proof: ARITHMETIC.md. No asymptotic claim is inferred from these tests.
"""
from fractions import Fraction as F
from math import gcd, isqrt


def _positive(n):
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")


def _harmonic(h):
    if type(h) is not int or not h:
        raise ValueError("nonzero integer harmonic required")


def conductor(a, b):
    """q=3**a*5**b and the exact order L=ord_q(16)=q/15."""
    _positive(a)
    _positive(b)
    q = 3**a * 5**b
    return q, q // 15


def _unit(c):
    if type(c) is not int or gcd(c, 15) != 1:
        raise ValueError("integer c coprime to 15 required")


def orbit_residues(a, b, c=1):
    """Literal chronological orbit, useful for bounded finite experiments."""
    q, period = conductor(a, b)
    _unit(c)
    state = c % q
    out = []
    for _ in range(period):
        out.append(state)
        state = 16 * state % q
    return tuple(out)


def period_character_phase(a, b, c, h):
    """Full-period mean: zero (None), or exactly exp(2*pi*i*phase)."""
    q, period = conductor(a, b)
    _unit(c)
    _harmonic(h)
    return None if h % period else F(h * c, q) % 1


def lag_character_phase(a, b, c, h, k):
    """Exact mean of the completed lag phase on a whole time period."""
    _positive(k)
    _harmonic(h)
    return period_character_phase(a, b, c, h * (16**k - 1))


def critical_signed_lag_limit(a, b, h):
    """Paper-proved limit for every unit c: 1 iff L divides h, else 0."""
    _, period = conductor(a, b)
    _harmonic(h)
    return int(h % period == 0)


def ceiling_sqrt(n):
    _positive(n)
    root = isqrt(n)
    return root if root * root == n else root + 1


def completed_tail_lag_error(k, h):
    """All-horizon |D_BBP-D_completed| < 3*ceil(sqrt|h|)*4**k.

    Original T_n<1/(64*n*n); split at ceil(sqrt|h|)*4**k and
    use min(2, 2*pi*|h|*(16**k-1)*T_n), pi<22/7.
    """
    _positive(k)
    _harmonic(h)
    return 3 * ceiling_sqrt(abs(h)) * 4**k


def completed_tail_score_error(N, K, h):
    """Exact weighted sum of the stated rational per-lag upper bounds."""
    _positive(N)
    _positive(K)
    _harmonic(h)
    if K > N:
        raise ValueError("K<=N required")
    return F(2, K*K*N) * sum(
        (K-k) * completed_tail_lag_error(k, h) for k in range(1, K))


def shadow_score_bounds(N, K, a, b, h):
    """All-horizon signed-lag bounds for any unit c; source tails paid.

    Low modes use zero-mean periodic window energy. Multiples of L have
    constant completed phases, hence the exact coherent baseline.
    """
    _, period = conductor(a, b)
    error = completed_tail_score_error(N, K, h)
    if h % period == 0:
        coherent = F(K-1, K) * (1-F(K+1, 3*N))
        return coherent-error, coherent+error
    energy_upper = F((N+K-1)*period*period, K*K*N)
    return -F(1, K)-error, energy_upper-F(1, K)+error


def original_source(n):
    """Independent combined-polynomial form of all four original poles."""
    _positive(n)
    return F(120*n*n-89*n+16,
             (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def original_prefix(M):
    _positive(M)
    return sum((original_source(n) / 16**n for n in range(1, M+1)), F(0))


def near_zero_shadow(a, b, M):
    """Choose c=1 mod15 below a rational original BBP prefix.

    Returns rational q/c metadata and an upper bound for |c/q-pi/16|.
    The irrational seed itself is not represented as a Fraction.
    """
    q, period = conductor(a, b)
    prefix = original_prefix(M)
    cell = (q*prefix-1) / 15
    c = 15*(cell.numerator // cell.denominator)+1
    return {"q": q, "period": period, "c": c,
            "completed_seed": F(c, q), "source_prefix": prefix,
            "seed_absolute_upper": F(15, q)+F(1, 64*M*M*16**M)}


def source_tail_interval(n, J):
    """Enclose T_n from finite original forcing, with an explicit remainder."""
    _positive(n)
    _positive(J)
    lower = sum((original_source(n+j)/16**j for j in range(1, J+1)), F(0))
    return lower, lower+F(1, 64*(n+J)**2*16**J)


def exact_receipt():
    """Deterministic finite metadata; limit labels refer to the paper proof."""
    cases = []
    for a, b, c in ((2, 2, 1), (3, 3, 7), (4, 3, 11)):
        q, period = conductor(a, b)
        rows = []
        for h in (1, 3, 5, 7, 11, period):
            rows.append({
                "h": h,
                "full_period_mean_phase": str(period_character_phase(a, b, c, h)),
                "critical_signed_lag_limit": critical_signed_lag_limit(a, b, h),
                "lag_mean_phases": {
                    str(k): str(lag_character_phase(a, b, c, h, k))
                    for k in (1, 2, 3, 5, 9, 15, 25, 45)}})
        cases.append({"a": a, "b": b, "c": c, "q": q,
                      "period": period, "harmonics": rows})
    shadows = []
    for depth in (3, 5, 8, 12):
        row = near_zero_shadow(depth, depth, depth)
        shadows.append({key: str(value) if not isinstance(value, int) else value
                        for key, value in row.items()})
    return {
        "status": "EXACT_FINITE_PARAMETERS_AND_PAPER_PROVED_LIMIT_LABELS",
        "phase_encoding": "None means exact zero complex mean; rational t means exp(2*pi*i*t)",
        "limit_authority": "ARITHMETIC.md A9 paper proof, not inferred from this JSON",
        "cases": cases,
        "nearzero_source_prefix_choices": shadows}


if __name__ == "__main__":
    import json
    print(json.dumps(exact_receipt(), indent=2))
