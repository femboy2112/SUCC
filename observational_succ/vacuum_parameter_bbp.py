"""Exact normalized-vacuum, parameter integral and BBP moment-resolvent lab.

Authenticated four-pole forcing agrees with bbp_natural_carrier / Gearbox.
No pi numeric values or digit strings are inputs. Finite certificates use
Fraction-only algebra. Classical operator theory and Basel/Machin are cited
separately; these finite results do NOT prove pi normality or RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, isqrt


class VacuumBridgeError(ValueError):
    """Bad parameter, source index, matrix, or domain transport."""


def _nat(n: int, minimum: int = 0, maximum: int = 10000) -> int:
    if type(n) is not int or not minimum <= n <= maximum:
        raise VacuumBridgeError("bounded integer source parameter required")
    return n


def _rational(value, *, strictly_positive=False) -> Q:
    if type(value) not in (int, Q):
        raise VacuumBridgeError("exact rational required, floats/bools refused")
    v = Q(value)
    if strictly_positive and v <= 0:
        raise VacuumBridgeError("positive exact rational required")
    return v


def kernel(t) -> Q:
    """P(t)=(1-t)(t²+2)((t+1)²+1), on rational 0<=t<=1."""
    t = _rational(t)
    if not 0 <= t <= 1:
        raise VacuumBridgeError("positive source is declared only on [0,1]")
    return (1-t)*(t*t+2)*(t*t+2*t+2)


def forcing(n: int) -> Q:
    """r(n) from the original signed FOUR poles, recombined exactly."""
    _nat(n, 1)
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def moment(k: int) -> Q:
    """<1,M^k 1>=r(k+1), M:t->t^8 in L²(P(t)dt)."""
    _nat(k, 0, 1000)
    return forcing(k+1)


def parameter_derivative(n: int, order: int) -> Q:
    """d^k/dr^k r(r) at real r=n, via -8 log(t) generator insertion."""
    _nat(n,1)
    _nat(order,0,24)
    factorial=1
    for j in range(2,order+1):
        factorial*=j
    p=order+1
    signed = (Q(4,(8*n-7)**p)-Q(2,(8*n-4)**p)
              -Q(1,(8*n-3)**p)-Q(1,(8*n-2)**p))
    return ((-8)**order)*factorial*signed


def difference(n: int, depth: int) -> Q:
    """Forward finite difference Delta^k r(n). Alternating signs are exact."""
    _nat(n,1)
    _nat(depth,0,30)
    return sum(((-1)**(depth-j)*comb(depth,j)*forcing(n+j)
                for j in range(depth+1)),Q())


def hankel(size: int, *, offset: int = 0) -> tuple[tuple[Q,...],...]:
    _nat(size,1,12)
    _nat(offset,0,50)
    return tuple(tuple(moment(offset+i+j) for j in range(size)) for i in range(size))


def _solve(matrix, rhs) -> tuple[Q,...]:
    """Exact rational Gaussian elimination; fails closed on a singular matrix."""
    m=len(rhs)
    if len(matrix)!=m or any(len(row)!=m for row in matrix):
        raise VacuumBridgeError("square system required")
    a=[[ _rational(matrix[i][j]) for j in range(m)]+[_rational(rhs[i])]
       for i in range(m)]
    for j in range(m):
        pivot=next((i for i in range(j,m) if a[i][j]),None)
        if pivot is None:
            raise VacuumBridgeError("singular projected matrix")
        a[j],a[pivot]=a[pivot],a[j]
        scale=a[j][j]
        a[j]=[entry/scale for entry in a[j]]
        for i in range(m):
            if i==j:continue
            scale=a[i][j]
            a[i]=[v-scale*u for v,u in zip(a[i],a[j])]
    return tuple(a[i][-1] for i in range(m))


def determinant(matrix) -> Q:
    """Exact determinant, including rational Hankel SPD principal minors."""
    n=len(matrix)
    if n<1 or any(len(row)!=n for row in matrix):
        raise VacuumBridgeError("nonempty square matrix required")
    a=[[ _rational(x) for x in row] for row in matrix]
    sign=1
    det=Q(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:
            return Q(0)
        if pivot!=k:
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        x=a[k][k]
        det*=x
        for i in range(k+1,n):
            t=a[i][k]/x
            for j in range(k+1,n):
                a[i][j]-=t*a[k][j]
            a[i][k]=Q(0)
    return sign*det


def hankel_sylvester(size: int) -> tuple[Q,...]:
    """Every leading principal minor strictly positive (moment integral proof)."""
    H=hankel(size)
    return tuple(determinant(tuple(row[:k] for row in H[:k])) for k in range(1,size+1))


@dataclass(frozen=True)
class KrylovCertificate:
    dimension: int
    parameter: Q
    galerkin_lower: Q
    residual_norm_squared: Q
    lower: Q
    upper: Q
    baseline_neumann_tail_upper: Q
    moments_used: int


def krylov_certificate(dimension: int, parameter=Q(1,16)) -> KrylovCertificate:
    """Exact two-sided certificate of R(z)=<1,(I-zM)^(-1)1>.

    Galerkin on span(1,M1,...,M^(d-1)1). The vector residual e=1-Af_d
    obeys  ||e||² <= <e,A^-1 e> <= ||e||²/(1-z) since
    (1-z)I <= A=I-zM <= I, 0<=M<=I. Hence rational brackets.
    No finite test is used as a proof of the infinite-dimensional statement.
    """
    _nat(dimension,1,12)
    z=_rational(parameter)
    if z<0 or z>=1:
        raise VacuumBridgeError("positive contraction resolvent requires 0<=z<1")
    d=dimension
    moments=[moment(k) for k in range(2*d+1)]
    b=moments[:d]
    G=tuple(tuple(moments[i+j]-z*moments[i+j+1]
                  for j in range(d)) for i in range(d))
    coeff=_solve(G,b)
    L=sum((x*y for x,y in zip(coeff,b)),Q())
    # Polynomial in M: e(M) = 1-(1-zM) sum_i c_i M^i.
    e=[Q(1)-coeff[0]]
    e.extend(-coeff[k]+z*coeff[k-1] for k in range(1,d))
    e.append(z*coeff[d-1])
    E=sum((e[i]*e[j]*moments[i+j]
           for i in range(d+1) for j in range(d+1)),Q())
    if E<0:
        raise ArithmeticError("squared norm cannot be negative")
    lower=L+E
    upper=L+E/(1-z)
    # Independent finite Neumann trial of degree d-1 gives this analytical cap.
    simple=z**(2*d)*moments[2*d]/(1-z)
    if upper<lower or E/(1-z)>simple:
        raise ArithmeticError("Galerkin cannot do worse than the finite Neumann trial")
    return KrylovCertificate(d,z,L,E,lower,upper,simple,2*d+1)


def certified_hex_prefix(dimension: int, digits: int) -> str | None:
    """Exact base16 certificate for pi; no pi value or digit string input."""
    _nat(digits,1,100)
    a=krylov_certificate(dimension)
    scale=16**digits
    l=a.lower*scale
    u=a.upper*scale
    low_digit=l.numerator//l.denominator
    high_digit=u.numerator//u.denominator
    if low_digit!=high_digit:
        return None
    return f"{low_digit//scale:X}.{low_digit%scale:0{digits}X}"


def source_orbit(index: int) -> Q:
    """Exact original BBP recurrence U_0=0, U_n=16U_(n-1)+r(n)."""
    _nat(index,0,1000)
    u=Q(0)
    for n in range(1,index+1):
        u=16*u+forcing(n)
    return u


def source_tail_bracket(index:int) -> tuple[Q,Q]:
    """For n>=1, 16^(n-1) pi = U_n + T_n, r(n+1)/16 <=T<=r(n+1)/15.

    Strictly decreasing r(n) and 0<16^-j establish both bounds.
    This is not the n=0 initial stage and does not certify all future carries.
    """
    _nat(index,1,1000)
    a=forcing(index+1)
    return (a/16,a/15)


def selected_hex_digit(index: int) -> int | None:
    """Digit at position n, with n=1 returning integer hex digit 3.

    Decides only if the authentic U_n plus finite positive tail bracket
    lies wholly within one integer cell. Does not prove frequencies.
    """
    _nat(index,1,300)
    u=source_orbit(index)
    l,h=source_tail_bracket(index)
    a=u+l
    b=u+h
    fa=a.numerator//a.denominator
    fb=b.numerator//b.denominator
    return fa%16 if fa==fb else None


def prime_valuations(rational) -> dict[int,int]:
    """Formal coefficients of log p; diagonal Q^* only, not ideles generally."""
    v=_rational(rational)
    if v==0:
        raise VacuumBridgeError("zero has no multiplicative inverse or log norm")
    a,b=abs(v.numerator),v.denominator
    out={}
    def factor(k,sgn):
        p=2
        while p*p<=k:
            if k%p==0:
                cnt=0
                while k%p==0:
                    k//=p;cnt+=1
                out[p]=out.get(p,0)+sgn*cnt
            p+=1
        if k>1:
            out[k]=out.get(k,0)+sgn
    factor(a,1);factor(b,-1)
    return {p:n for p,n in sorted(out.items()) if n}


def finite_adelic_norm(rational, prime_cutoff:int) -> Q:
    """|q|_infinity prod_{p<=X}|q|_p; equals 1 once source support complete."""
    _nat(prime_cutoff,1,100_000)
    v=_rational(rational)
    if v==0:
        raise VacuumBridgeError("no multiplicative vacuum norm for zero")
    out=abs(v)
    for p,e in prime_valuations(v).items():
        if p<=prime_cutoff:
            out*=Q(p)**(-e)
    return out


def diagonal_product_formula(rational)->bool:
    """Full normalized global product = 1; exact Fraction identity."""
    v=_rational(rational)
    if v==0:
        raise VacuumBridgeError("q must be nonzero")
    support=prime_valuations(v)
    return finite_adelic_norm(v,max(support,default=1))==1


def log_bracket_positive(value, terms:int) -> tuple[Q,Q]:
    """Exact rational logarithm bracket using tanh(0.5 ln x) series.

    For x>0, z=(x-1)/(x+1), log x = 2 sum z^(2j+1)/(2j+1).
    abs remainder <= 2 |z|^(2m+1)/((2m+1)(1-z²)).
    This is a mathematical bound, not an exact rational log value.
    """
    v=_rational(value,strictly_positive=True)
    _nat(terms,1,10000)
    if v==1:
        return Q(0),Q(0)
    z=(v-1)/(v+1)
    partial=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q())
    radius=2*abs(z)**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
    return partial-radius,partial+radius


def vacuum_rank_one_factor(A,u,parameter=Q(1)) -> dict:
    """Rank-one determinant lemma det(A+tuu^T)/det A = 1+t u^T A^-1 u.

    The log-potential is log(1+t c), and derivative c/(1+t c),
    expressible without approximating logarithms. Matrices must be SPD.
    """
    n=len(u)
    if not n or len(A)!=n or any(len(row)!=n for row in A):
        raise VacuumBridgeError("matrix dimensions do not match")
    mat=tuple(tuple(_rational(x) for x in row) for row in A)
    if any(mat[i][j]!=mat[j][i] for i in range(n) for j in range(n)):
        raise VacuumBridgeError("symmetric source matrix required")
    if any(determinant(tuple(row[:k] for row in mat[:k]))<=0 for k in range(1,n+1)):
        raise VacuumBridgeError("positive definite source matrix required")
    u=tuple(_rational(x) for x in u)
    lam=_rational(parameter)
    invu=_solve(mat,u)
    c=sum((x*y for x,y in zip(u,invu)),Q())
    ratio=1+lam*c
    if ratio<=0:
        raise VacuumBridgeError("rank-one path crosses singularity")
    perturbed=tuple(tuple(mat[i][j]+lam*u[i]*u[j] for j in range(n)) for i in range(n))
    if determinant(perturbed)!=determinant(mat)*ratio:
        raise ArithmeticError("rank one determinant lemma contradicted")
    return {"c":c,"determinant_ratio":ratio,"log_potential_derivative":c/ratio,
            "log_potential_at_zero_is_zero":True}


def hidden_determinant_example(w1=Q(1),w2=Q(1)) -> dict:
    """Three-node path with one static boundary port. Port Schur is zero
    independent of positive weights; hidden Dirichlet determinant=w1*w2.
    This is hidden normalizer information, NOT a recovered static response.
    """
    a=_rational(w1,strictly_positive=True)
    b=_rational(w2,strictly_positive=True)
    D=((a+b,-b),(-b,b))
    det=determinant(D)
    if det!=a*b:
        raise ArithmeticError("hidden determinant identity failed")
    return {"static_one_port":Q(0),"hidden_D":D,"hidden_determinant":det}


def rational_moment_counterfeit() -> dict:
    """Atomic measure matches first two authentic moments, but pi_like is rational.

    Positive moments and a vacuum-normalized resolvent do not imply
    normality. The counterfeit is explicitly NONAUTHENTIC.
    """
    mass=moment(0)
    location=moment(1)/mass
    ratio=mass/(1-location/16)
    assert 0<location<1
    assert mass*location==moment(1)
    assert mass*location*location!=moment(2)
    return {"mass":mass,"location":location,"pi_like_rational":ratio,
            "matching_moments":2,"genuine_bbp_source":False}
