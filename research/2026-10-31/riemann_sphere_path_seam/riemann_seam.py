"""Original BBP rational sphere / Pascal sampling contour -- finite exact arithmetic.

No analytic normality assertion. All arithmetic computations use Fraction.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial

SHIFTS=(7,4,3,2)
WEIGHTS=(4,-2,-1,-1)
POLES=tuple(F(c,8) for c in SHIFTS)


def _valid_n(n):
    if type(n) is not int or not (1 <= n <= 32):
        raise ValueError('finite integer horizon must lie in [1,32]')


def source(z):
    z=F(z)
    return sum((F(w,1)/(8*z-c) for w,c in zip(WEIGHTS,SHIFTS)),F(0))


def combined_source(n):
    _valid_n(n)
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def atomic_moment(k):
    if type(k) is not int or k<0:
        raise ValueError('nonnegative integer moment required')
    return sum(w*c**k for w,c in zip(WEIGHTS,SHIFTS))


def pole_residues():
    return tuple(F(w,8) for w in WEIGHTS)


def add_poly(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return tuple(out)


def mul_poly(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return tuple(out)


def evaluate_poly(a,x):
    x=F(x);y=F(0)
    for v in reversed(a):y=y*x+v
    return y


def pascal_weight_poly(n):
    """Degree n-1 Newton interpolant to 16^{-j}, at j=1,...,n."""
    _valid_n(n)
    acc=(F(0),)
    falling=(F(1),)
    for k in range(n):
        acc=add_poly(acc,tuple(v*F(1,16)*(-F(15,16))**k/factorial(k) for v in falling))
        falling=mul_poly(falling,(-F(k+1),F(1))) # (z-1)(z-2)...
    return acc


def sample_kernel(x,n):
    _valid_n(n); x=F(x)
    return sum((F(1)/(x-j) for j in range(1,n+1)),F(0))


def action(n):
    _valid_n(n)
    return sum((source(j)/16**j for j in range(1,n+1)),F(0))


def state(n):
    _valid_n(n)
    u=F(0)
    for j in range(1,n+1):u=16*u+source(j)
    return u


def sample_residues(n):
    p=pascal_weight_poly(n)
    return tuple(evaluate_poly(p,j)*source(j) for j in range(1,n+1))


def source_residues(n):
    p=pascal_weight_poly(n)
    return tuple(rho*evaluate_poly(p,pole)*sample_kernel(pole,n)
                 for rho,pole in zip(pole_residues(),POLES))


def residue_at_infinity(n):
    """INDEPENDENT Laurent calculation, not residue-balance by definition.

    At z=1/w, the w^-1 coefficient of -P(1/w)r(1/w)K(1/w)/w^2
    equals -sum_{k>=2} p_k sum_{j=1}^{k-1} m_j*sum_{a<=n} a^(k-1-j)/8^(j+1).
    """
    p=pascal_weight_poly(n)
    return -sum((p[k]*sum((F(atomic_moment(j),8**(j+1))*
              sum(a**(k-1-j) for a in range(1,n+1)) for j in range(1,k)),F(0))
              for k in range(2,len(p))),F(0))


def harmonic(n):
    _valid_n(n)
    return sum((F(1,j) for j in range(1,n+1)),F(0))


def harmonic_defect(p,n):
    p=F(p);_valid_n(n)
    return sum((F(1)/(j-p)-F(1,j) for j in range(1,n+1)),F(0))


def source_harmonic_decomposition(n):
    weights=pascal_weight_poly(n)
    coeff=sum((rho*evaluate_poly(weights,p) for rho,p in zip(pole_residues(),POLES)),F(0))
    defect=sum((rho*evaluate_poly(weights,p)*harmonic_defect(p,n) for rho,p in zip(pole_residues(),POLES)),F(0))
    return (-harmonic(n)*coeff-defect,coeff,defect)


def cross_ratio():
    a,b,c,d=POLES
    return (a-c)*(b-d)/((a-d)*(b-c))


def elliptic_j():
    lam=cross_ratio()
    return 256*(1-lam+lam**2)**3/(lam**2*(1-lam)**2)


def affine_product(a,b):
    """Affine matrices [[16,r(a)],[0,1]] [[16,r(b)],[0,1]]."""
    _valid_n(a);_valid_n(b)
    return (F(256),16*source(b)+source(a))


def source_newton_weight(n,j):
    """A direct binomial-path polynomial evaluator, independent of coefficients."""
    from math import comb
    _valid_n(n)
    return sum((F(1,16)*F(comb(j-1,k))*(-F(15,16))**k
                for k in range(min(n,j))),F(0))
