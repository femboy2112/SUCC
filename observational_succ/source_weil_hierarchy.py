"""Finite-source signed Weil hierarchy with rational outward spectral certificates.

Only Suzuki's genuine Q(zeta) prime powers, Gamma(1/4), pole and half density
are admitted. Rational 0<a<=1; finite J,N are research budgets.
No zeta zeros are read. A vanishing negative depth is NOT assumed.

Source anchor: Suzuki arXiv:2606.09096v3 (1.3), (1.5), (1.8).
Analytic error follows GWC-5 of parent PR #76. Euler gamma enclosure uses
the classical alternating Euler-Maclaurin harmonic-number remainder.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, isqrt

class WeilHierarchyError(ValueError):
    pass

SCALE=10**32
def q(x):
    if type(x) not in (int,F):
        raise WeilHierarchyError("exact integer or Fraction required; float is not a proof")
    return F(x)
def down(x):
    x=q(x);return F(x.numerator*SCALE//x.denominator,SCALE)
def up(x):return -down(-q(x))

@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __post_init__(self):
        if type(self.lo) is not F or type(self.hi) is not F or self.lo>self.hi:
            raise WeilHierarchyError("invalid rational interval")
    def __add__(self,other):
        b=iv(other);return I(down(self.lo+b.lo),up(self.hi+b.hi))
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-iv(other)
    def __rsub__(self,other):return iv(other)+-self
    def __mul__(self,other):
        b=iv(other);v=(self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi)
        return I(down(min(v)),up(max(v)))
    __rmul__=__mul__
    def inverse(self):
        if self.lo<=0<=self.hi:raise WeilHierarchyError("reciprocal contains zero")
        return I(down(1/self.hi),up(1/self.lo))
    def __truediv__(self,other):return self*iv(other).inverse()
    def __rtruediv__(self,other):return iv(other)*self.inverse()
    def mid(self):return (self.lo+self.hi)/2
    def radius(self):return (self.hi-self.lo)/2

def iv(x):
    if isinstance(x,I):return x
    v=q(x);return I(v,v)

@lru_cache(maxsize=10000)
def exp_pos(x):
    """Outward exp(x), 0<=x<=128 by scaled positive Taylor/geometric remainder."""
    x=q(x)
    if not 0<=x<=128:raise WeilHierarchyError("exp range")
    m=0;y=x
    while y>F(1,2):
        y/=2;m+=1
    term=F(1);total=F(1)
    for k in range(1,49):
        term=term*y/k;total+=term
    nxt=term*y/49
    remainder=nxt/(1-y/50)
    result=I(down(total),up(total+remainder))
    for _ in range(m):result=result*result
    return result

def exp_neg(x):return exp_pos(x).inverse()

def _atan(z,K=32):
    z=q(z);total=sum(((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(K)),F())
    nxt=(-1)**K*z**(2*K+1)/F(2*K+1)
    return I(down(min(total,total+nxt)),up(max(total,total+nxt)))

@lru_cache(maxsize=1)
def pi_iv():
    a=_atan(F(1,5));b=_atan(F(1,239))
    return 16*a-4*b

def _atanh_log_unit(x,K=40):
    """1<=x<=2, log x=2atanh((x-1)/(x+1)), exact geometric bound."""
    x=q(x)
    if not 1<=x<=2:raise WeilHierarchyError("dyadic log unit")
    t=(x-1)/(x+1)
    total=sum((2*t**(2*k+1)/F(2*k+1) for k in range(K)),F())
    rem=2*t**(2*K+1)/(F(2*K+1)*(1-t*t))
    return I(down(total),up(total+rem))

@lru_cache(maxsize=1)
def log2_iv():return _atanh_log_unit(F(2))

@lru_cache(maxsize=2000)
def log_iv(x):
    x=q(x)
    if x<=0:raise WeilHierarchyError("log positive")
    if x<1:return -log_iv(1/x)
    n=0;z=x
    while z>=2:
        z/=2;n+=1
    return _atanh_log_unit(z)+n*log2_iv()

def log_interval(t):
    t=iv(t)
    if t.lo<=0:raise WeilHierarchyError("log positive interval")
    a=log_iv(t.lo);b=log_iv(t.hi)
    return I(a.lo,b.hi)

def gamma_iv():
    """Classical alternating Euler-Maclaurin bound at n=16; next term <1/(240*n^8)."""
    n=16
    H=sum((F(1,k) for k in range(1,n+1)),F())
    constant=H-F(1,2*n)+F(1,12*n*n)-F(1,120*n**4)+F(1,252*n**6)
    upper=iv(constant)-log_iv(n)
    return I(down(upper.lo-F(1,240*n**8)),upper.hi)

@lru_cache(maxsize=1)
def contact_iv():
    """-psi(1/4)+log(pi)=gamma+pi/2+3log2+log(pi)."""
    return gamma_iv()+pi_iv()/2+3*log2_iv()+log_interval(pi_iv())

@lru_cache(maxsize=32)
def sqrt_inverse(n):
    if type(n) is not int or n<1:raise WeilHierarchyError("sqrt integer")
    Q=10**34
    k=isqrt(n*Q*Q)
    low=F(k,Q);high=F(k+1,Q)
    return I(down(1/high),up(1/low))

def _prime(p):
    if type(p) is not int or p<2:return False
    return all(p%d for d in range(2,isqrt(p)+1))
def real_prime_power(n):
    if type(n) is not int or n<2:raise WeilHierarchyError("source index")
    if _prime(n):return n
    for p in range(2,isqrt(n)+1):
        if not _prime(p):continue
        m=p*p
        while m<n:m*=p
        if m==n:return p
    return None

AUTHENTIC_TAPE=tuple((n,real_prime_power(n)) for n in range(2,9) if real_prime_power(n))
def assert_original_source_tape(tape=AUTHENTIC_TAPE):
    if tuple(tape)!=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2)):
        raise WeilHierarchyError("false/composite/omitted independent source place")
    return True

def positive_part_interval(z):
    z=iv(z);return I(max(F(),z.lo),max(F(),z.hi))

@lru_cache(maxsize=4096)
def screw_interval(r,J):
    """Suzuki signed g_J(r), 0<=r<=2, true original prime powers only."""
    r=q(r)
    if not 0<=r<=2 or type(J) is not int or not 1<=J<=128:
        raise WeilHierarchyError("domain: rational |t|<=2, 1<=J<=128")
    assert_original_source_tape()
    pole=-4*(exp_pos(r/2)+exp_neg(r/2)-2)
    contact=iv(r)/2*contact_iv()
    prime=iv(0)
    for n,p in AUTHENTIC_TAPE:
        logn=log_iv(n)
        displacement=positive_part_interval(iv(r)-logn)
        prime+=log_iv(p)*sqrt_inverse(n)*displacement
    gamma=iv(0)
    for j in range(J):
        d=4*j+1
        gamma+=-F(4,d*d)*(1-exp_neg(F(d,2)*r))
    return pole+prime+contact+gamma

def gamma_tail(J):
    if type(J) is not int or J<1:raise WeilHierarchyError("J>=1")
    return F(1,4*J+1)+F(4,(4*J+1)**2)

def lipschitz_safe(a,J):
    """Rational L_J(a) from source, a<=1; no evaluated transcendental needed.

    For a<=1/2, only prime-power 2 enters; L<=9+sum 2/(4j+1).
    For a<=1, all true source atoms have n<=8; L<=45+same sum.
    """
    a=q(a)
    if not 0<a<=1 or type(J) is not int or not 1<=J<=128:
        raise WeilHierarchyError("source Lipschitz domain")
    return (9 if a<=F(1,2) else 45)+sum((F(2,4*j+1) for j in range(J)),F())

def continuous_error(a,J,N):
    a=q(a)
    if type(N) is not int or N<2 or N>256 or not 0<a<=1:
        raise WeilHierarchyError("bounded source hierarchy N<=256, a<=1")
    h=2*a/N
    return 2*a*(gamma_tail(J)+h*lipschitz_safe(a,J))

@dataclass(frozen=True)
class FiniteSourceStage:
    a:F
    J:int
    N:int
    center:tuple[tuple[F,...],...]
    kernel_entry_radius:F
    norm_error:F
    source:str="AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3"
    nontrivial_zeros_used:bool=False

@lru_cache(maxsize=64)
def stage(a,J,N):
    a=q(a)
    if not 0<a<=1 or type(N) is not int or not 2<=N<=24:
        raise WeilHierarchyError("finite exact step stage budget 2<=N<=24")
    if type(J) is not int or not 1<=J<=36:
        raise WeilHierarchyError("stage J budget 1..36")
    h=2*a/N
    vals=[screw_interval(k*h,J) for k in range(N)]
    M=tuple(tuple(h*vals[abs(i-j)].mid() for j in range(N)) for i in range(N))
    entry=max((v.radius() for v in vals),default=F())
    # each normalized cell entry has <=h*entry error; operator <=N*h*entry
    total=continuous_error(a,J,N)+2*a*entry
    return FiniteSourceStage(a,J,N,M,entry,total)

def _authenticated(st):
    if type(st) is not FiniteSourceStage or st.source!="AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3":
        raise WeilHierarchyError("source-authenticated finite signed stage required")
    if st!=stage(st.a,st.J,st.N):
        raise WeilHierarchyError("forged or stale signed source matrix/error")

def _contrast_quadratic(M,delta):
    """B^T(M+delta I)B, columns B=e_i-e_{N-1}, Gram B^TB=I+11^T."""
    n=len(M);last=n-1
    return tuple(tuple(M[i][j]-M[i][last]-M[last][j]+M[last][last]
                       +delta*(F(i==j)+1)
                       for j in range(last)) for i in range(last))

def ldl_positive(M):
    n=len(M)
    if n==0:return False
    if any(len(row)!=n for row in M):raise WeilHierarchyError("square")
    if any(M[i][j]!=M[j][i] for i in range(n) for j in range(n)):
        raise WeilHierarchyError("symmetric")
    d=[]
    L=[[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=M[j][j]-sum((L[j][k]*L[j][k]*d[k] for k in range(j)),F())
        if p<=0:return False
        d.append(p)
        for i in range(j+1,n):
            L[i][j]=(M[i][j]-sum((L[i][k]*L[j][k]*d[k] for k in range(j)),F()))/p
    return True

def certified_upper_negative_depth(st:FiniteSourceStage,iterations=12):
    """Exact positive-definite shifted *finite* compression lower bound.

    Returns d >= max(0,-min Rayleigh of the exact rational center on meanzero).
    It does NOT prove d<=0 or sign of genuine Q_W.
    """
    if type(iterations) is not int or not 0<=iterations<=20:
        raise WeilHierarchyError("iterations 0..20")
    _authenticated(st)
    M=st.center
    def okay(d):return ldl_positive(_contrast_quadratic(M,d))
    if okay(F(0)):return F(0)
    hi=F(1)
    for _ in range(20):
        if okay(hi):break
        hi*=2
    else:raise WeilHierarchyError("upper offset search budget")
    lo=F(0)
    for _ in range(iterations):
        mid=(lo+hi)/2
        if okay(mid):hi=mid
        else:lo=mid
    assert okay(hi)
    return hi

def certified_lower_negative_depth(st:FiniteSourceStage):
    """Contrast Rayleigh witnesses. >0 proves actual negative Q_W direction."""
    _authenticated(st)
    N=st.N;M=st.center
    qmax=F()
    for i in range(N):
        for j in range(i+1,N):
            qval=(M[i][i]+M[j][j]-2*M[i][j])/2
            # |Rayleigh(G)-Rayleigh(M)|<= norm_error for every meanzero u
            qmax=max(qmax,-qval-st.norm_error)
    return qmax

def depth_enclosure(st,iterations=12):
    """Combined source interval for genuine negative spectral depth of G_a."""
    lower=certified_lower_negative_depth(st)
    upper=certified_upper_negative_depth(st,iterations)+st.norm_error
    assert lower<=upper
    return lower,upper

def simple_rank_one_negative(N,T):
    """Computable-rank-one-halting toy stage: T=None or T>=1 is externally declared.

    For stage N, simulate only N steps: coefficient -2^-T if T<=N, else 0.
    Missing eventual true coefficient <=2^-N. Toy, not authentic zeta.
    """
    if type(N) is not int or N<1 or (T is not None and (type(T) is not int or T<1)):
        raise WeilHierarchyError("positive finite stage and halting time")
    observed=F(1,2**T) if T is not None and T<=N else F()
    error=F(1,2**N)
    return -observed,error


def exact_rayleigh(matrix, vector):
    """Exact finite signed energy. Not a source certificate by itself."""
    n=len(matrix)
    if n<2 or any(len(row)!=n for row in matrix) or len(vector)!=n:
        raise WeilHierarchyError("finite exact source matrix dimensions")
    if any(matrix[i][j]!=matrix[j][i] for i in range(n) for j in range(n)):
        raise WeilHierarchyError("non-Hermitian signed candidate")
    v=tuple(q(x) for x in vector)
    if sum(v)!=0 or all(x==0 for x in v):
        raise WeilHierarchyError("nonzero mean-zero original test required")
    return (sum((v[i]*matrix[i][j]*v[j] for i in range(n) for j in range(n)),F())
            /sum((x*x for x in v),F()))


def finite_multiway_search(matrix, amplitude=2):
    """Rational multivariate contrasts; strictly stronger than pairwise tests.

    Searches <=6 cell directions, bounded to a small integer grid. This is an
    instrument, not a proof of positivity from absence of a counterexample.
    """
    from itertools import product
    n=len(matrix)
    if type(amplitude) is not int or not 1<=amplitude<=4 or n<2 or n>6:
        raise WeilHierarchyError("bounded exact joint interaction witness")
    best=F(1<<60);best_vector=None
    for first in product(range(-amplitude,amplitude+1),repeat=n-1):
        last=-sum(first);v=tuple(first)+(last,)
        if not any(v):continue
        val=exact_rayleigh(matrix,v)
        if val<best:
            best=val;best_vector=v
    assert best_vector is not None
    return best,best_vector


def authenticated_multiway_witness(st:FiniteSourceStage,amplitude=2):
    """Verified negative witness iff the source multivariate upper is < 0.

    A non-witness says NOTHING about all tests or RH.
    """
    _authenticated(st)
    minimum,vector=finite_multiway_search(st.center,amplitude)
    upper=minimum+st.norm_error
    return {"vector":vector,"rational_center_rayleigh":minimum,
            "source_upper_rayleigh":upper,
            "certified_negative_original_weil":upper<0,
            "certified_global_positive":False,
            "nontrivial_zero_input":False}
