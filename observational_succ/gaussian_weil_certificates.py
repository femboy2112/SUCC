"""Exact Gaussian SUCC sphere and conditional signed-Weil finite-step bounds.

The positive six-state Gaussian kernel is an auxiliary prior, NOT the genuine
completed Weil quadratic form. All nonrational evaluations are diagnostics,
never rigorous interval eigenvalue certificates. RH remains open.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import isqrt

POINTS = {"N": (0,0,1), "S": (0,0,-1),
          "E0": (1,0,0), "E1": (0,1,0),
          "E2": (-1,0,0), "E3": (0,-1,0)}
ORDER = tuple(POINTS)


class GaussianSourceError(ValueError):
    pass


def is_prime(p):
    if type(p) is not int or p < 2: return False
    if p % 2 == 0: return p == 2
    return all(p % d for d in range(3, isqrt(p)+1, 2))


def covariance(u, v):
    if u not in POINTS or v not in POINTS:
        raise GaussianSourceError("unknown source vertex")
    distance2 = sum((x-y)**2 for x,y in zip(POINTS[u], POINTS[v]))
    if distance2 % 2: raise GaussianSourceError("non-rational exponent")
    return F(1,2)**(distance2//2)


def gram(vertices=ORDER):
    if len(vertices) != len(set(vertices)):
        raise GaussianSourceError("duplicate source vertex")
    return tuple(tuple(covariance(u,v) for v in vertices) for u in vertices)


def ldl_pivots(matrix):
    n = len(matrix)
    if any(len(r) != n for r in matrix): raise GaussianSourceError("nonsquare")
    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)):
        raise GaussianSourceError("nonsymmetric")
    L = [[F(i==j) for j in range(n)] for i in range(n)]
    D = []
    for j in range(n):
        d = F(matrix[j][j])-sum(L[j][k]**2*D[k] for k in range(j))
        if d == 0: raise GaussianSourceError("zero LDL pivot")
        D.append(d)
        for i in range(j+1,n):
            L[i][j]=(F(matrix[i][j])-sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/d
    return tuple(D)


def solve(a, y):
    n=len(y)
    if len(a)!=n or any(len(r)!=n for r in a):
        raise GaussianSourceError("matrix dimension")
    T=[[F(v) for v in a[i]]+[F(y[i])] for i in range(n)]
    for col in range(n):
        pivot=next((r for r in range(col,n) if T[r][col]),None)
        if pivot is None: raise GaussianSourceError("singular source")
        T[col],T[pivot]=T[pivot],T[col]
        c=T[col][col]
        T[col]=[v/c for v in T[col]]
        for r in range(n):
            if r != col:
                c=T[r][col]
                T[r]=[v-c*w for v,w in zip(T[r],T[col])]
    return [T[i][-1] for i in range(n)]


def posterior(observed, values, target, noise=F(0)):
    """Conditional mean/variance only under the DECLARED six-state GP prior."""
    if target not in POINTS or any(p not in POINTS for p in observed):
        raise GaussianSourceError("unknown vertex")
    if len(observed)!=len(values) or len(set(observed))!=len(observed):
        raise GaussianSourceError("invalid observation list")
    if type(noise) not in (F,int) or noise<0:
        raise GaussianSourceError("noise variance negative/nonrational")
    if not observed: return (F(0),F(1))
    A=[[covariance(p,q)+(F(noise) if i==j else F(0))
        for j,q in enumerate(observed)] for i,p in enumerate(observed)]
    k=[covariance(target,p) for p in observed]
    w=solve(A,k)
    variance=covariance(target,target)-sum(x*y for x,y in zip(k,w))
    mean=sum(x*y for x,y in zip(k,solve(A,values)))
    if variance<0: raise GaussianSourceError("non-positive source")
    return mean,variance


def equator_action(multiplier):
    if type(multiplier) is not int or multiplier<1:
        raise GaussianSourceError("positive integer required")
    return {"N":"N","S":"S",**{f"E{j}":f"E{multiplier*j%4}" for j in range(4)}}


def prime_chart_action(p):
    if not is_prime(p): raise GaussianSourceError("not a genuine prime")
    if p==2: raise GaussianSourceError("dyadic conductor is not invertible")
    return equator_action(p)


def oriented_area(action):
    x=POINTS[action["E0"]]; y=POINTS[action["E1"]]
    return x[0]*y[1]-x[1]*y[0]


def rank_one_hidden_sign(n, observed_dim):
    if type(n) is not int or type(observed_dim) is not int or not 0<observed_dim<n:
        raise GaussianSourceError("need hidden direction")
    return tuple(tuple(-1 if i==j==observed_dim else int(i==j) for j in range(n))
                 for i in range(n))


def gamma_tail(J):
    """Exact sup norm bound for the missing genuine Suzuki g Gamma rungs."""
    if type(J) is not int or J<1: raise GaussianSourceError("J>=1")
    d=4*J+1
    return F(1,d)+F(4,d*d)


def step_operator_error(a,J,N,L):
    """||P0T_gP0 - P0T_{g_J,step}P0|| <= 2a(tau_J+2a L/N).

    L must already be a RIGOROUS Lipschitz upper bound. A numerical value
    rounded without outward enclosure is NOT a certificate.
    """
    if type(N) is not int or N<2 or a<=0 or L<0:
        raise GaussianSourceError("invalid step bound inputs")
    return 2*a*(gamma_tail(J)+2*a*L/N)


def signed_suzuki_g(t,J,dps=55):
    """Actual signed screw g_J (Suzuki 2026 Eq 1.3), NUMERIC ONLY.

    Uses the existing SUCC von-Mangoldt prime-power source tape; no zeros.
    """
    try: import mpmath as mp
    except ImportError as e: raise GaussianSourceError("install research mpmath") from e
    from .completed_weil_transport import von_mangoldt_labels
    gamma_tail(J)
    mp.mp.dps=dps
    r=abs(mp.mpf(t))
    nmax=int(mp.floor(mp.exp(r)))
    if nmax>200000: raise GaussianSourceError("parent source tape budget")
    jets=von_mangoldt_labels(max(2,nmax))
    poles=-4*(mp.exp(r/2)+mp.exp(-r/2)-2)
    prime=mp.fsum(mp.log(p)/mp.sqrt(n)*(r-mp.log(n))
                  for n,p in jets if mp.log(n)<=r)
    contact=-r/2*(-mp.euler-mp.pi/2-3*mp.log(2)-mp.log(mp.pi))
    gamma=-4*mp.fsum((1-mp.exp(-(4*j+1)*r/2))/(4*j+1)**2 for j in range(J))
    return poles+prime+contact+gamma


def signed_lipschitz(a,J,dps=55):
    """Derived L_J(a); evaluated numerically, NOT rounded rigorously."""
    try: import mpmath as mp
    except ImportError as e: raise GaussianSourceError("install research mpmath") from e
    from .completed_weil_transport import von_mangoldt_labels
    gamma_tail(J)
    mp.mp.dps=dps
    a=mp.mpf(a)
    if a<=0: raise GaussianSourceError("a>0")
    r=2*a
    nmax=int(mp.floor(mp.exp(r)))
    if nmax>200000: raise GaussianSourceError("parent source tape budget")
    jets=von_mangoldt_labels(max(2,nmax))
    return (2*(mp.exp(a)-mp.exp(-a))
            +abs(-mp.euler-mp.pi/2-3*mp.log(2)-mp.log(mp.pi))/2
            +mp.fsum(mp.log(p)/mp.sqrt(n) for n,p in jets if mp.log(n)<=r)
            +mp.fsum(mp.mpf(2)/(4*j+1) for j in range(J)))


def centered_screw_matrix(a,J,N,dps=55):
    """Finite signed step matrix after mean-zero projection; NOT interval data."""
    try: import mpmath as mp
    except ImportError as e: raise GaussianSourceError("install research mpmath") from e
    if type(N) is not int or N<2: raise GaussianSourceError("N>=2")
    gamma_tail(J)
    mp.mp.dps=dps
    a=mp.mpf(a)
    if a<=0: raise GaussianSourceError("a>0")
    h=2*a/N
    # g is even: block differences depend on the difference of cell indices.
    values=[signed_suzuki_g(h*k,J,dps=dps) for k in range(N)]
    A=mp.matrix([[h*values[abs(i-j)] for j in range(N)] for i in range(N)])
    row=[sum(A[i,j] for j in range(N))/N for i in range(N)]
    ave=sum(row)/N
    return mp.matrix([[A[i,j]-row[i]-row[j]+ave for j in range(N)] for i in range(N)])
