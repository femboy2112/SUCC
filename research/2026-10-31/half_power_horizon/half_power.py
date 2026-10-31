"""Exact dual-place geometric successor, two-adic half-powers and BBP pole costs.

Research only. No pi normality, RH, source-to-Haar or half-density theorem.
No floating arithmetic: integer/Fraction finite certificates.
"""
from fractions import Fraction
from math import comb
from functools import reduce


def _check_int(n, lower=0):
    if type(n) is not int or n < lower:
        raise ValueError("integer required")


def v_p(z, p):
    """Valuation for a nonzero exact rational; the proof uses p=2 and p=3."""
    if type(p) is not int or p < 2:
        raise ValueError("prime p required")
    z = Fraction(z)
    if not z:
        raise ValueError("valuation of zero is infinite")
    def v(n):
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        return k
    return v(abs(z.numerator)) - v(z.denominator)


def geometric_prefix(base, m):
    """Finite sum of nonnegative integer powers, with declared start at k=0."""
    _check_int(base, 2)
    _check_int(m)
    return (base**m - 1) // (base - 1)


def successor_snapshot(x, base, m):
    """x-(base-1)*sum_(j<m)base**j = x+1-base**m exactly over Q."""
    _check_int(base, 2)
    _check_int(m)
    return Fraction(x) - (base - 1) * geometric_prefix(base, m)


def product_formula_power(base, m):
    """Archimedean norm times all finite prime norms of base**m, exactly 1."""
    _check_int(base, 2)
    _check_int(m)
    n = base
    fac = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            fac.append((p, e))
        p += 1
    if n > 1:
        fac.append((n, 1))
    return Fraction(base**m) * reduce(
        lambda t, pe: t * Fraction(1, pe[0]**(pe[1]*m)), fac,
        Fraction(1))


def square_roots_one_mod2(bits):
    """The four roots mod 2^bits for bits>=3; two are non-lifting ghosts."""
    _check_int(bits, 3)
    q = 2**bits
    return tuple(sorted({1, q-1, 1+q//2, q//2-1}))


def half_binomial_term(k, t):
    """Exact (1/2 choose k)(8t)^k, the branch near 1 at the 2-adic place."""
    _check_int(k)
    t = Fraction(t)
    value = Fraction(1)
    for j in range(k):
        value *= Fraction(1 - 2*j, 2) * 8*t / (j+1)
    return value


def half_sqrt_mod(t, bits):
    """2-adic square root of 1+8t, selected congruent to 1 mod4.

    Truncation at k=bits is valid: all omitted terms have v2>=bits+1.
    This asserts no real-principal-branch identity.
    """
    _check_int(bits, 3)
    if type(t) is not int:
        raise ValueError("integer parameter required")
    q = 2**bits
    z = sum((half_binomial_term(k, t) for k in range(bits)),
            Fraction(0))
    assert z.denominator % 2 == 1
    r = (z.numerator * pow(z.denominator, -1, q)) % q
    assert r % 4 == 1 and (r*r - (1+8*t)) % q == 0
    return r


def half_geometric_term(k):
    """k-th term of (1-z)^(-1/2) at z=2: C(2k,k)/2^k.

    Its 2-adic valuation is popcount(k)-k, so terms do NOT tend to 0.
    """
    _check_int(k)
    return Fraction(comb(2*k, k), 2**k)


def bbp_source(n):
    """The unchanged original four signed BBP poles at any integer index."""
    if type(n) is not int:
        raise ValueError("integer source index required")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def bbp_denominator(n):
    if type(n) is not int:
        raise ValueError("integer index required")
    return (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)


def bbp_joint_successor(n, m):
    """Original signed source at n+1-6^m compared with n+1.

    v2 difference = m exactly. If m>d=v3(D(n+1)), then
    v3 difference >= m-2*d. No global 3-adic isometry is claimed.
    """
    if type(n) is not int or type(m) is not int or m < 1:
        raise ValueError("integer source index and positive m required")
    y = n+1
    x = successor_snapshot(n, 6, m)
    assert x.denominator == 1
    diff = bbp_source(int(x)) - bbp_source(y)
    d = v_p(bbp_denominator(y), 3)
    return {"difference": diff, "v2": v_p(diff, 2), "v3": v_p(diff, 3),
            "pole_order": d, "qualified": m > d,
            "v3_lower_bound": m - 2*d}


def gaussian_mul(x, y):
    """Gaussian integers (a,b)=a+bi."""
    a,b = x
    c,d = y
    return (a*c-b*d, a*d+b*c)


def eisenstein_uniformizer():
    """u=1+i: u^2=2i; minimal polynomial X^2-2X+2."""
    u = (1,1)
    return {"u2": gaussian_mul(u,u), "two_times_i": (0,2),
            "minimal_polynomial": (1,-2,2), "norm": 2}


def three_sqrt_mod(target, bits):
    """Unique 3-adic square root of target=1 mod3 selected 1 mod3."""
    _check_int(bits, 1)
    if type(target) is not int or target % 3 != 1:
        raise ValueError("integer target congruent 1 mod3 required")
    r = 1
    for k in range(1, bits):
        q = 3**(k+1)
        step = 3**k
        candidates = [r+d*step for d in range(3)
                      if ((r+d*step)**2-target) % q == 0]
        assert len(candidates) == 1
        r = candidates[0]
    assert (r*r-target) % (3**bits) == 0 and r % 3 == 1
    return r


def joint_sqrt_successor(m):
    """One rational 1-6^m has 2- and 3-adic roots but no REAL root.

    At p=2 the selected root differs from 1 at valuation m-1.
    At p=3 the selected root differs from 1 at valuation m.
    """
    _check_int(m, 3)
    target = 1-6**m
    r2 = half_sqrt_mod(-(6**m)//8, m+4)
    r3 = three_sqrt_mod(target, m+4)
    assert (r2*r2-target) % (2**(m+4)) == 0
    assert (r3*r3-target) % (3**(m+4)) == 0
    assert v_p(r2-1, 2) == m-1 and v_p(r3-1, 3) == m
    return {"target": target, "root2_residue": r2,
            "root3_residue": r3, "precision": m+4,
            "v2_root_minus_one": m-1, "v3_root_minus_one": m}
