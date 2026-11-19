"""SUCC: exact, stdlib-only Jacobian/probe-lattice certificates.

Research-only. Nothing here establishes R0 or base-16 normality of pi.
Run: python research/2026-11-19/causal_jacobian_probe_lattice/probe.py
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd

T = (
    (16, 32, 24, 8, 1),
    (8, 20, 18, 7, 1),
    (4, 12, 13, 6, 1),
    (2, 7, 9, 5, 1),
    (1, 4, 6, 4, 1),
)


def det(a):
    """Exact integer determinant by the Leibniz formula (size at most 5)."""
    n = len(a)
    if not n:
        return 1
    total = 0
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        v = 1
        for i in range(n):
            v *= a[i][p[i]]
        total += (-1 if inversions % 2 else 1) * v
    return total


def charpoly(a):
    """Coefficients descending, using integer principal minors, not eigenvalue fits."""
    n = len(a)
    coeff = [1]
    for k in range(1, n + 1):
        s = sum(det([[a[i][j] for j in ix] for i in ix])
                for ix in combinations(range(n), k))
        coeff.append((-1 if k % 2 else 1) * s)
    return tuple(coeff)


def mat_mul(a, b, p):
    n = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(n)) % p
                       for j in range(n)) for i in range(n))


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def matrix_order(a, p, cap=10000):
    m = identity(len(a))
    for k in range(1, cap + 1):
        m = mat_mul(m, a, p)
        if m == identity(len(a)):
            return k
    raise AssertionError(f"unresolved matrix order mod {p}")


def scalar_order(a, p):
    if gcd(a, p) != 1:
        return None
    x = 1
    for k in range(1, p + 1):
        x = x * a % p
        if x == 1:
            return k
    raise AssertionError("unresolved scalar order")


def left_action(row, a, p):
    return tuple(sum(row[i] * a[i][j] for i in range(len(a))) % p
                 for j in range(len(a)))


def rank_mod(a, p):
    x = [[z % p for z in row] for row in a]
    nr, nc = len(x), len(x[0]); rank = 0
    for col in range(nc):
        piv = next((i for i in range(rank, nr) if x[i][col]), None)
        if piv is None:
            continue
        x[rank], x[piv] = x[piv], x[rank]
        u = pow(x[rank][col], -1, p)
        x[rank] = [(z * u) % p for z in x[rank]]
        for i in range(nr):
            if i != rank:
                f = x[i][col]
                x[i] = [(c - f*d) % p for c, d in zip(x[i], x[rank])]
        rank += 1
    return rank


def r(n):
    assert n >= 1
    return 4*Fraction(1,8*n-7) - 2*Fraction(1,8*n-4) - Fraction(1,8*n-3) - Fraction(1,8*n-2)


def source_states(N):
    out = [Fraction(0)]
    for n in range(1,N+1):
        out.append(16*out[-1]+r(n))
    return out


def v_p(n, p):
    if not n:
        return None
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def ppart(x,p):
    """Canonical p-primary projection in Q/Z, value in [0,1)."""
    d = x.denominator
    ppower=1
    while d % p == 0:
        d //= p
        ppower *= p
    if ppower == 1:
        return Fraction(0)
    return Fraction((x.numerator * pow(d, -1, ppower)) % ppower, ppower)


def modone(x):
    return x - x.numerator // x.denominator


def factor_primes(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:
                n//=d
        d+=1
    if n>1:out.append(n)
    return out


def torus_sq(x):
    t=modone(x)
    d=min(t,1-t)
    return d*d


def holonomy_energy(states, B, ell, h):
    """Rational unsmeared relative-source holonomy squared torus norm."""
    k = h*(16**ell-1)
    drift = lambda n: sum((16**(ell-j)*r(n+j) for j in range(1,ell+1)),Fraction(0))
    assert len(states) >= 2*B+ell
    for n in range(B,2*B):
        assert states[n+ell]-states[n]-drift(n) == (16**ell-1)*states[n]
    return sum((torus_sq(k*states[n]) for n in range(B,2*B)),Fraction(0))/B


def run():
    assert charpoly(T) == (1,-55,385,-385,55,-1)
    assert det(T) == 1
    assert det([[16*int(i==j)-T[i][j] for j in range(5)] for i in range(5)]) == -1076625
    assert 1076625 == 3**3 * 5**3 * 11 * 29
    orders={p:(scalar_order(16,p),matrix_order(T,p)) for p in (2,3,5,7,11,29)}
    assert orders[2] == (None,3)
    assert orders[3] == (1,2)
    assert orders[5] == (1,5)
    assert orders[7] == (3,4)
    assert orders[11] == (5,5)
    v11=(4,2,10,10,1)
    v29=(4,6,14,20,1)
    for p,v in ((11,v11),(29,v29)):
        assert left_action(v,T,p) == tuple(16*x%p for x in v)
    assert rank_mod([[T[j][i]-16*int(i==j) for j in range(5)] for i in range(5)], 11)==4
    # With rank 4 mod 11 and det of valuation 1, the nonzero mod-11 kernel
    # cannot lift to a primitive kernel mod 121 (Smith invariant 11, not 121).
    assert v_p(1076625,11) == 1
    assert 2**3 % 7 == 1 and 2**5 % 11 == 10
    assert 16**3 % 7 == 1 and 16**5 % 11 == 1
    for j in range(15):
        assert all(modone(Fraction((16**ell-1)*j,15)) == 0 for ell in range(1,7))
    # A 15-point gauge persists for every holonomy-only probe.
    states=source_states(70)
    for n in range(0,20):
        assert states[n+1]==16*states[n]+r(n+1)
        primes=factor_primes(states[n+1].denominator)
        assert modone(sum((ppart(states[n+1],p) for p in primes),Fraction(0))) == modone(states[n+1])
        for p in (7,11,29):
            assert modone(ppart(states[n+1],p)) == modone(16*ppart(states[n],p)+ppart(r(n+1),p))
    for B in (3,5,8,16):
        for ell,h in ((3,11),(5,7),(4,1)):
            H=holonomy_energy(states,B,ell,h)
            R=sum((torus_sq(states[n]) for n in range(B,2*B)),Fraction(0))/B
            assert 0 <= H <= (h*(16**ell-1))**2 * R
    assert 8*7-5*11 == 1
    print('Exact Jacobian certificates passed.')
    print('charpoly:',charpoly(T),'det(16I-T):',-1076625)
    print('orders (radix16,Fibonacci):',orders)
    print('11-channel:',v11,'29-control:',v29)
    print('p-primary/source transport, 15-point gauge, and source-holonomy bounds: pass')

if __name__=='__main__':
    run()
