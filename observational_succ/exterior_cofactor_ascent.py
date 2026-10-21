"""Exact SUCC exterior/cofactor ascent: finite mathematical certificates.

Research-only, classical elementary arithmetic, novelty UNVERIFIED.
No claim to an abc-moment theorem beyond t<2/3 or to global source positivity.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb, factorial, gcd, isqrt, prod


class ExteriorAscentError(ValueError):
    pass


def _pos(n, name="parameter"):
    if type(n) is not int or n <= 0:
        raise ExteriorAscentError(f"{name} must be a positive integer")
    return n


def _x(X):
    if type(X) not in (int, Fraction):
        raise ExteriorAscentError("X must be an exact int or Fraction")
    X = Fraction(X)
    if X < 0:
        raise ExteriorAscentError("X must be nonnegative")
    return X


def residue_simplex_count(m, W, X, residues):
    """Exact count of positive m-tuples with sum<=X and residues mod W.

    For each canonical residue row r_i in [0,W), use representative W if r_i=0.
    Stars-and-bars gives C(floor((X-sum r_i)/W)+m,m) when nonempty.
    """
    _pos(m, "m")
    _pos(W, "W")
    X = _x(X)
    seen = set()
    ans = 0
    for row in residues:
        row = tuple(row)
        if (len(row) != m or
            any(type(r) is not int or r < 0 or r >= W for r in row) or
            row in seen):
            raise ExteriorAscentError("noncanonical or duplicated residue vector")
        seen.add(row)
        n = (X - sum(r if r else W for r in row)) // W
        if n >= 0:
            ans += comb(n + m, m)
    return ans


def simplex_error_bound(m, W, X, residue_count):
    """Certified |N-r*(X/W)^m/m!| <= r*m^2*(X/W+m)^(m-1)/m!."""
    _pos(m, "m")
    _pos(W, "W")
    X = _x(X)
    if (type(residue_count) is not int or
        residue_count < 0 or residue_count > W**m):
        raise ExteriorAscentError("invalid number of residue classes")
    t = X / W
    return Fraction(residue_count * m*m, factorial(m)) * (t+m)**(m-1)


def simplex_relative_bound(m, W, X):
    """For nonempty residue sets, relative discrepancy bound m^2*s*(1+m*s)^(m-1),
    s=W/X. Therefore m^2*W/X->0 suffices for uniform simultaneous dimension growth.
    """
    _pos(m, "m")
    _pos(W, "W")
    X = _x(X)
    if X == 0:
        raise ExteriorAscentError("relative bound requires X>0")
    s = W/X
    return m*m*s*(1+m*s)**(m-1)


def unrestricted_simplex_count(m, X):
    """Count = C(floor X,m), not X^m/m! uniformly as m grows."""
    _pos(m, "m")
    X = _x(X)
    n = X.numerator // X.denominator
    return comb(n,m) if n >= m else 0


def _coprime(ds):
    return all(gcd(ds[i],ds[j]) == 1
               for i,j in combinations(range(len(ds)),2))


def cofactor_certificate(moduli, cofactors, X):
    """For m>=2: x_i=d_i*u_i, sum first m equals last, D*U<=X^(m+1)/m^m."""
    m = len(moduli)-1
    if m < 2 or len(cofactors) != m+1:
        raise ExteriorAscentError("need m+1 moduli and cofactors")
    ds = tuple(_pos(x,"modulus") for x in moduli)
    us = tuple(_pos(x,"cofactor") for x in cofactors)
    X = _x(X)
    values = tuple(a*b for a,b in zip(ds,us))
    if sum(values[:-1]) != values[-1] or values[-1] > X:
        raise ExteriorAscentError("not an admissible positive source incidence")
    D,U = prod(ds),prod(us)
    if D*U > X**(m+1)/m**m:
        raise AssertionError("AM-GM contradiction")
    return dict(dimension=m,D=D,U=U,coordinates=values,
                cofactor_upper=X**(m+1)/(m**m*D),
                high_divisor=D>X**m)


def determinant(matrix):
    """Integer determinant by exact fraction-free Bareiss elimination."""
    n = len(matrix)
    if n == 0 or any(len(row)!=n or any(type(v) is not int for v in row)
                     for row in matrix):
        raise ExteriorAscentError("nonempty square integer matrix required")
    a = [list(row) for row in matrix]
    sign,old = 1,1
    for k in range(n-1):
        if a[k][k] == 0:
            i = next((j for j in range(k+1,n) if a[j][k]),None)
            if i is None:
                return 0
            a[k],a[i] = a[i],a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z = a[i][j]*p-a[i][k]*a[k][j]
                if z%old:
                    raise AssertionError("nonexact Bareiss division")
                a[i][j] = z//old
            a[i][k] = 0
        old = p
    return sign*a[-1][-1]


def exterior_certificate(moduli, points, X):
    """m source points: D divides m-by-m exterior determinant; |det|<=X^m.

    For D>X^m all top minors vanish, so all admissible point vectors
    span a rational subspace of dimension at most m-1. NOT a singleton
    when m>=3 (see rank_drop_family).
    """
    m = len(moduli)-1
    if m<2 or len(points)!=m:
        raise ExteriorAscentError("need exactly m points and m+1 moduli")
    ds = tuple(_pos(d,"modulus") for d in moduli)
    if not _coprime(ds):
        raise ExteriorAscentError("moduli must be pairwise coprime")
    X = _x(X)
    for point in points:
        if (len(point)!=m+1 or
            any(type(v) is not int or v<=0 for v in point) or
            sum(point[:-1])!=point[-1] or point[-1]>X or
            any(point[i]%ds[i] for i in range(m+1))):
            raise ExteriorAscentError("point violates source or divisibility")
    A = [[points[j][i] for j in range(m)] for i in range(m)]
    det = determinant(A)
    D = prod(ds)
    if det%D or abs(det)>X**m or (D>X**m and det):
        raise AssertionError("exterior theorem contradicted")
    return dict(determinant=det,D=D,X=X,
                rank_drop_forced=D>X**m)


def rank_drop_family(n, K):
    """For odd n and K>=3, return K-1 distinct primitive 3-summand points.
    
    d=(n,n+1,2n+1,3n+2); x(k)=((k-1)n,(2k-1)(n+1),
    2n+1,k(3n+2)), k=2..K. Choose n large and divisible by
    the odd primes <=K-1 so D>X^3 and every point primitive.
    The points all lie in a rational 2-plane, proving the
    higher-dimensional singleton conjecture FALSE.
    """
    _pos(n,"n")
    _pos(K,"K")
    if n%2==0 or K<3:
        raise ExteriorAscentError("requires odd n and K>=3")
    ds=(n,n+1,2*n+1,3*n+2)
    X=K*ds[-1]
    pts=tuple(((k-1)*n,(2*k-1)*(n+1),2*n+1,k*ds[-1])
              for k in range(2,K+1))
    if (not _coprime(ds) or prod(ds)<=X**3 or
        any(gcd(gcd(p[0],p[1]),p[2])!=1 for p in pts)):
        raise ExteriorAscentError("n too small or primitive-family condition fails")
    if any(sum(p[:3])!=p[3] or any(p[i]%ds[i] for i in range(4))
           for p in pts):
        raise AssertionError("family equation failed")
    return dict(moduli=ds,D=prod(ds),X=X,points=pts,count=len(pts))


def weighted_infinite_count(X, affordable_weights):
    """Locally finite infinite carrier: sum(w_j*n_j)<=X, n_j>=0.

    The caller must supply ALL w_j<=X; omissions are a different carrier.
    A source has finite counts for every X iff its integer weights tend to infinity.
    """
    weights=tuple(affordable_weights)
    if type(X) is not int or X<0 or any(type(w) is not int or w<=0
                                        for w in weights):
        raise ExteriorAscentError("invalid exact integer weight budget")
    counts=[0]*(X+1)
    counts[0]=1
    for w in weights:
        for s in range(w,X+1):
            counts[s]+=counts[s-w]
    return sum(counts)


def local_prime_clock_factors(m, p):
    """Exact source-local p-residue laws for m summand slots only.

    Global primitive (gcd(x_1,...,x_m)=1 locally): not every residue is 0.
    Pairwise coprime summands: at most one residue is 0.
    The TOTAL c=sum(x_i) is NOT included in the pairwise law; including
    it requires a separate additive-cancellation gate.
    """
    _pos(m, "m")
    _pos(p, "p")
    if p < 2 or any(p%q==0 for q in range(2,isqrt(p)+1)):
        raise ExteriorAscentError("p must be a genuine prime")
    nonzero = Fraction(p-1,p)
    zero = Fraction(1,p)
    return {
        "primitive_gcd": Fraction(1)-zero**m,
        "pairwise_summands": nonzero**m + m*zero*nonzero**(m-1),
    }
