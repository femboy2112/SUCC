"""Exact finite Schur telescope and explicitly hypothetical infinite controls.

This module does NOT authenticate the completed Weil/Suzuki kernel or solve RH.
The analytic first-window source oracle remains a separately named obligation.
Finite witnesses are checked in Fraction arithmetic against complete declared
finite matrices; infinite toys have paper-proved tail bounds, not source data.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations


class TelescopeError(ValueError):
    """Bad exact certificate, missing source law, or mathematical contract."""


def exact(x):
    if type(x) not in (int, Q):
        raise TelescopeError('only int/Fraction accepted, no float/bool')
    return Q(x)


def matrix(rows, *, height=None, width=None):
    if type(rows) is not tuple or not rows or any(type(row) is not tuple for row in rows):
        raise TelescopeError('nonempty immutable rectangular matrix required')
    n = len(rows[0]); m = len(rows)
    if not n or any(len(row) != n for row in rows):
        raise TelescopeError('nonempty rectangular matrix required')
    if height is not None and m != height or width is not None and n != width:
        raise TelescopeError('incorrect matrix dimension')
    return tuple(tuple(exact(x) for x in row) for row in rows)


def trans(a):
    return tuple(tuple(row[j] for row in a) for j in range(len(a[0])))


def mul(a,b):
    if len(a[0]) != len(b):
        raise TelescopeError('matrix multiplication dimension mismatch')
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),Q())
                       for j in range(len(b[0]))) for i in range(len(a)))


def add(a,b,scale=1):
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
        raise TelescopeError('matrix addition dimension mismatch')
    scale=exact(scale)
    return tuple(tuple(x+scale*y for x,y in zip(row_a,row_b))
                 for row_a,row_b in zip(a,b))


def diag(values):
    values=tuple(exact(x) for x in values)
    if not values:
        raise TelescopeError('nonempty diagonal required')
    return tuple(tuple(x if i==j else Q() for j,x in enumerate(values)) for i in range(len(values)))


def minor_det(rows):
    rows=matrix(rows)
    if len(rows)!=len(rows[0]):
        raise TelescopeError('determinant of nonsquare matrix')
    a=[list(row) for row in rows]; n=len(a); value=Q(1)
    for col in range(n):
        pivot=next((i for i in range(col,n) if a[i][col]),None)
        if pivot is None: return Q()
        if pivot!=col:
            a[col],a[pivot]=a[pivot],a[col]; value=-value
        value*=a[col][col]
        for i in range(col+1,n):
            f=a[i][col]/a[col][col]
            for j in range(col+1,n):a[i][j]-=f*a[col][j]
            a[i][col]=Q()
    return value


def symmetric(a):
    return len(a)==len(a[0]) and a==trans(a)


def psd(a):
    a=matrix(a)
    if not symmetric(a):return False
    n=len(a)
    # All principal minors, including nonleading minors, are necessary for PSD.
    for m in range(1,n+1):
        for indices in combinations(range(n),m):
            block=tuple(tuple(a[i][j] for j in indices) for i in indices)
            if minor_det(block)<0:return False
    return True


def solve(a,b):
    a=matrix(a); b=matrix(b,height=len(a))
    n=len(a)
    if len(a[0])!=n:raise TelescopeError('square solve required')
    rhs=len(b[0]); rows=[list(a[i])+list(b[i]) for i in range(n)]
    for col in range(n):
        pivot=next((i for i in range(col,n) if rows[i][col]),None)
        if pivot is None:raise TelescopeError('singular high block: no inverse asserted')
        rows[col],rows[pivot]=rows[pivot],rows[col]
        w=rows[col][col]
        rows[col]=[v/w for v in rows[col]]
        for i in range(n):
            if i!=col:
                t=rows[i][col]
                rows[i]=[x-t*y for x,y in zip(rows[i],rows[col])]
    return tuple(tuple(row[n:]) for row in rows)


@dataclass(frozen=True)
class FiniteCarrier:
    """Complete DECLARED finite test model. It is not the genuine Weil source.

    B=-V^T Y, D=-V^T R, D>=kappa V^T V>=(0) are proved by
    exact matrix arithmetic, not by trusting a caller-provided `certified` flag.
    This is the finite counterpart of the Suzuki integration-by-parts identity.
    """
    A: tuple
    B: tuple
    D: tuple
    V: tuple
    Y: tuple
    R: tuple
    kappa: Q

    def __post_init__(self):
        a=matrix(self.A)
        if not symmetric(a):raise TelescopeError('A must be symmetric')
        p=len(a)
        d=matrix(self.D)
        if not symmetric(d):raise TelescopeError('D must be symmetric')
        q=len(d)
        b=matrix(self.B,height=q,width=p)
        v=matrix(self.V,width=q)
        y=matrix(self.Y,height=len(v),width=p)
        r=matrix(self.R,height=len(v),width=q)
        k=exact(self.kappa)
        if k<=0:raise TelescopeError('positive inherited coercivity constant required')
        if add(b,mul(trans(v),y))!=tuple(tuple(Q() for _ in range(p)) for _ in range(q)):
            # Equivalent to B=-V^TY, but rejects mismatched source squares.
            raise TelescopeError('wrong source B=-V*Y integration identity')
        if add(d,mul(trans(v),r))!=tuple(tuple(Q() for _ in range(q)) for _ in range(q)):
            raise TelescopeError('wrong source D=-V*R integration identity')
        if not psd(add(d,mul(trans(v),v),scale=-k)):
            raise TelescopeError('declared high coercivity inequality fails')
        if not psd(d) or minor_det(d)==0:
            raise TelescopeError('finite high D must be positive definite')
        for name,obj in (('A',a),('B',b),('D',d),('V',v),('Y',y),('R',r)):
            object.__setattr__(self,name,obj)
        object.__setattr__(self,'kappa',k)

    @property
    def low_dimension(self):return len(self.A)

    @property
    def high_dimension(self):return len(self.D)

    def actual_short(self):
        return add(self.A,mul(trans(self.B),solve(self.D,self.B)),scale=-1)

    def trial(self,u):
        u=matrix(u,height=self.high_dimension,width=self.low_dimension)
        # H=(J-U)*G(J-U), with source identity, no inverse used.
        h=add(add(self.A,mul(trans(self.B),u),scale=-1),
              mul(trans(u),self.B),scale=-1)
        h=add(h,mul(mul(trans(u),self.D),u))
        f=add(self.Y,mul(self.R,u),scale=-1)
        c=mul(trans(f),f)
        bound=add(h,c,scale=-Q(1)/self.kappa)
        actual=self.actual_short()
        if not psd(add(h,actual,scale=-1)) or not psd(add(actual,bound,scale=-1)):
            raise AssertionError('finite source identities failed to imply Schur sandwich')
        return FiniteTrial(u,h,c,bound,actual,source_authenticated=False)


@dataclass(frozen=True)
class FiniteTrial:
    response: tuple
    upper: tuple
    residual_gram: tuple
    lower: tuple
    reference_short: tuple
    source_authenticated: bool=False


@dataclass(frozen=True)
class ConditionalSourceEnvelope:
    """An *untrusted-to-source* numeric Loewner packet; assumptions never vanish.

    Matrices, source hashes and premise names are caller assertions, NOT a
    verification of the original analytic inequalities. Meant for integration
    with a future independently verified original-source interval evaluator.
    """
    source_sha: str
    radius: Q
    channels: tuple[str,...]
    low_metric: tuple[Q,...]
    center: tuple
    energy_operator_error: Q
    residual_trace_upper: Q
    kappa: Q
    premises: tuple[str,...]

    def __post_init__(self):
        if self.source_sha != "0cc8510b71d178fc79e8d410a86d8b6014cf9178":
            raise TelescopeError('exact original Suzuki source blob identity required (still not analytic authentication)')
        if self.channels != ("prime2_half_density", "real_gamma", "pole_plus", "pole_minus", "contact"):
            raise TelescopeError('complete pinned signed source channel contract required')
        if type(self.premises) is not tuple or not self.premises:
            raise TelescopeError('declared paper/source premises required')
        if exact(self.radius)!=Q(1,2):
            raise TelescopeError('fixed first-prime source window only')
        metric=tuple(exact(v) for v in self.low_metric)
        if metric != (Q(1,3),Q(1,5),Q(1,7),Q(1,9)):
            raise TelescopeError('original four-low Legendre metric W required')
        c=matrix(self.center,height=4,width=4)
        if not symmetric(c):raise TelescopeError('Hermitian (real) low center required')
        if exact(self.kappa)<=0 or exact(self.energy_operator_error)<0 or exact(self.residual_trace_upper)<0:
            raise TelescopeError('nonnegative verified-error claims and positive coercivity needed')
        object.__setattr__(self,'radius',Q(1,2))
        object.__setattr__(self,'center',c)
        object.__setattr__(self,'low_metric',metric)
        object.__setattr__(self,'kappa',exact(self.kappa))
        object.__setattr__(self,'energy_operator_error',exact(self.energy_operator_error))
        object.__setattr__(self,'residual_trace_upper',exact(self.residual_trace_upper))

    def bracket(self):
        w=diag(self.low_metric)
        e=self.energy_operator_error
        residual=self.residual_trace_upper/self.kappa
        return {'lower':add(self.center,w,scale=-e-residual),
                'upper':add(self.center,w,scale=e),
                'width_in_W_operator_norm':2*e+residual,
                'authority':'CONDITIONAL_ON_SUPPLIED_SOURCE_ENCLOSURES',
                'source_identification_authenticated':False,
                'completed_Weil_sign_established':False,
                'RH_proved':False,
                'premises':self.premises}


def genuine_source_obligations() -> tuple[str,...]:
    return (
        'original signed Suzuki source blob identified with completed Weil form',
        'genuine prime-2 hinge, both poles, contact and whole real Gamma',
        'whole high coercivity D>=kappa V*V (paper premise)',
        'source-specific dense range of projected derivative R (paper premise)',
        'certified arbitrary-precision finite G_J and projected gprime_J energy',
        'source-tail errors scale with norm of each selected high response',
        'metric W and all source/basis/channel conventions verified',
        'no nontrivial zero data and no auxiliary positive host substituted'
    )


@dataclass(frozen=True)
class DiagonalToy:
    """EXPLICIT INFINITE ARTIFICIAL model; no numeric approximations to Weil.

    D_j=r_j^2, V_j=r_j, R_j=-r_j, Y_j=-y_j, B_j=r_j*y_j;
    kappa<=1. Then S0=A-sum y_j^2, H_N=A-sum_(j<=N)y_j^2,
    C_N=sum_(j>N)y_j^2 and U_N,j=y_j/r_j. Source range is dense.
    """
    variant: str
    delay: int=6

    def __post_init__(self):
        if self.variant not in ('delayed','unbounded','singular'):
            raise TelescopeError('unknown finite example family')
        if type(self.delay) is not int or self.delay<1:
            raise TelescopeError('positive delayed depth required')

    @property
    def kappa(self):return Q(1,2) if self.variant=='singular' else Q(1)

    @property
    def a(self):
        return Q(1,2) if self.variant=='delayed' else Q(2) if self.variant=='unbounded' else Q(1,3)

    def stage(self,n):
        if type(n) is not int or n<0:raise TelescopeError('nonnegative finite stage required')
        if self.variant=='delayed':
            energy=Q(int(n>=self.delay)); residual=Q(int(n<self.delay))
            response_norm_squared=Q(2**(2*self.delay)) if n>=self.delay else Q()
        elif self.variant=='singular':
            energy=(Q(1)-Q(4)**(-n))/3
            residual=Q(4)**(-n)/3
            response_norm_squared=Q(4)*(Q(4)**n-Q(1))/3
        else:
            energy=sum((Q(1,j*j) for j in range(1,n+1)),Q())
            residual=Q(2) if n==0 else Q(1,n)  # rigorous integral upper for zeta(2) tail
            response_norm_squared=Q(n*(n+1)*(2*n+1),6)
        h=self.a-energy
        return {
            'stage':n,'upper':h,'lower':h-residual/self.kappa,
            'residual_upper':residual,'width':residual/self.kappa,
            'response_norm_squared':response_norm_squared,
            'source':'EXPLICIT_SYNTHETIC_DIAGONAL',
            'original_Weil_authenticated':False,'RH_proved':False,
        }


def search_toy(toy:DiagonalToy,*,accuracy:Q|None=None,max_stage:int=1000,sign:bool=False):
    """Finite budget exhaustion is UNKNOWN, never a mathematical impossibility."""
    if type(toy) is not DiagonalToy:raise TelescopeError('explicit synthetic family required')
    if type(max_stage) is not int or max_stage<0:raise TelescopeError('finite search budget required')
    if accuracy is not None and exact(accuracy)<=0:
        raise TelescopeError('strict positive accuracy required')
    if accuracy is None and not sign:raise TelescopeError('ask for accuracy and/or sign')
    for n in range(max_stage+1):
        r=toy.stage(n)
        if sign and r['upper']<0:
            return {**r,'status':'CERTIFIED_NEGATIVE_SYNTHETIC'}
        if sign and r['lower']>0:
            return {**r,'status':'CERTIFIED_POSITIVE_SYNTHETIC'}
        if accuracy is not None and r['width']<exact(accuracy):
            return {**r,'status':'ACCURACY_CERTIFIED_SYNTHETIC'}
    return {'status':'BUDGET_UNRESOLVED','visited':max_stage+1,'RH_proved':False}
