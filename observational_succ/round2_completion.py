"""Exact finite calibration for completion debt; no infinite theorem solver."""
from fractions import Fraction as Q
from math import prod, isqrt


def _prime(p):
    return type(p) is int and p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def alpha(primes):
    """Haar measure of a finite genuine-prime avoidance cylinder."""
    values = tuple(primes)
    if any(not _prime(p) for p in values):
        raise ValueError('genuine primes required')
    f = frozenset(values)
    return prod((1-Q(1,p) for p in f), start=Q(1))


def squared_vacuum_overlap(f, g):
    f, g = frozenset(f), frozenset(g)
    return alpha(f | g)**2 / (alpha(f)*alpha(g))


def crt_intersection(f, g):
    """Independent residue count; cap prevents accidental huge CRT loops."""
    f, g = frozenset(f), frozenset(g)
    alpha(f | g)
    modulus = prod(f | g)
    if modulus > 100000:
        raise ValueError('finite counting cap exceeded')
    return Q(sum(all(x % p for p in f | g) for x in range(modulus)), modulus)


def dual_mass(weights):
    w = tuple(Q(x) for x in weights)
    if any(x <= 0 for x in w):
        raise ValueError('strictly positive weights required')
    return sum((1/(n*x) for n,x in enumerate(w,1)), Q(0))


def continuity_witness(weights):
    """Represent a_n=c_n/sqrt(n); J a has rational atom c_n/n.

    For c_n=1/(w_n*mass), test 1 is exactly 1 and norm²=1/mass.
    """
    w = tuple(Q(x) for x in weights)
    mass = dual_mass(w)
    if not w:
        raise ValueError('nonempty finite truncation required')
    c = tuple(1/(x*mass) for x in w)
    norm2 = sum((x*y*y/n for n,(x,y) in enumerate(zip(w,c),1)), Q(0))
    atoms = tuple(y/n for n,y in enumerate(c,1))
    return dict(coefficients=c, atoms=atoms, norm_squared=norm2,
                constant_pairing=sum(atoms,Q(0)), dual_mass=mass)


def action_ratios(weight, p, indices):
    if not _prime(p):
        raise ValueError('genuine prime required')
    out = []
    for n in indices:
        if type(n) is not int or n < 1:
            raise ValueError('positive indices required')
        a,b = Q(weight(n)),Q(weight(p*n))
        if min(a,b) <= 0:
            raise ValueError('strictly positive weights required')
        out.append((b/a,a/b))
    return tuple(out)


def transpose_test_tables(p, values):
    """Exact test pullbacks, stripping the explicit sqrt(p) scalar.

    Return sqrt(p)*U_p*phi on Z/q, and U_p phi/sqrt(p) on Z/(pq).
    The latter needs the larger modulus; division on Z/q alone is illegal.
    """
    if not _prime(p) or not values:
        raise ValueError('prime and nonempty residue table required')
    phi = tuple(Q(x) for x in values)
    q = len(phi)
    return (tuple(phi[(p*x)%q] for x in range(q)),
            tuple(phi[(x//p)%q] if x%p == 0 else Q(0) for x in range(p*q)))
