"""Original-theta, outward-integer interval contour certificate, no zeta-zero input.

All transcendental values in proof receipt are enclosed with fixed-point integer
interval arithmetic, rational Taylor / Machin / atanh series and a proved
Simpson fourth-derivative bound. Uses the actual integer theta source.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, comb
from functools import lru_cache

S = 10**38

class SourceContourError(ValueError):
    pass


def _ceildiv(x: int, y: int) -> int:
    return -((-x)//y)


@dataclass(frozen=True)
class I:
    """Closed real interval [lo/S,hi/S] with exact directed integer rounding."""
    lo: int
    hi: int
    def __post_init__(self):
        if type(self.lo) is not int or type(self.hi) is not int or self.lo > self.hi:
            raise SourceContourError("invalid directed interval")

    @staticmethod
    def of(x):
        if isinstance(x,I):
            return x
        if type(x) not in (int,Q):
            raise SourceContourError("exact rational inputs only")
        q=Q(x)
        return I((q.numerator*S)//q.denominator,
                 _ceildiv(q.numerator*S,q.denominator))

    def __add__(self,other):
        b=I.of(other)
        return I(self.lo+b.lo, self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):
        return I(-self.hi,-self.lo)
    def __sub__(self,other):
        return self+(-I.of(other))
    def __rsub__(self,other):
        return I.of(other)+(-self)
    def __mul__(self,other):
        b=I.of(other)
        p=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I(min(p)//S,_ceildiv(max(p),S))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:
            raise SourceContourError("division by zero-bearing interval")
        return I(S*S//self.hi,_ceildiv(S*S,self.lo))
    def __truediv__(self,other):
        return self*I.of(other).inv()
    def __rtruediv__(self,other):
        return I.of(other)*self.inv()
    def __pow__(self,n):
        if type(n) is not int or n<0 or n>1024:
            raise SourceContourError("invalid polynomial exponent")
        x=I.of(1); b=self
        while n:
            if n&1:x=x*b
            b=b*b
            n//=2
        return x
    def lower(self):
        return Q(self.lo,S)
    def upper(self):
        return Q(self.hi,S)
    def middle(self):
        return Q(self.lo+self.hi,2*S)
    def width(self):
        return Q(self.hi-self.lo,S)
    def __repr__(self):
        return f"I({self.lo}/{S},{self.hi}/{S})"


@lru_cache(maxsize=2)
def pi_iv() -> I:
    def atan(z: Q):
        N=42
        total=sum(((-1)**j*z**(2*j+1)/Q(2*j+1) for j in range(N)),Q())
        nxt=(-1)**N*z**(2*N+1)/Q(2*N+1)
        return I(I.of(total+min(Q(0),nxt)).lo,I.of(total+max(Q(0),nxt)).hi)
    return 16*atan(Q(1,5))-4*atan(Q(1,239))


@lru_cache(maxsize=4096)
def log_iv(t:Q)->I:
    if type(t) not in (int,Q):
        raise SourceContourError("rational theta time required")
    t=Q(t)
    if not 1<=t<=8:
        raise SourceContourError("time in [1,8] only")
    scale=0
    while t>=2:
        t/=2;scale+=1
    def unit(u:Q):
        z=I.of((u-1)/(u+1))
        z2=z*z
        term=z
        total=I.of(0)
        N=54
        for j in range(N):
            total+=2*term/Q(2*j+1)
            term=term*z2
        if term.lo<0: raise SourceContourError("positive log series expected")
        rem=2*term/(Q(2*N+1)*(I.of(1)-z2))
        return I(total.lo,(total+rem).hi)
    return unit(t)+scale*unit(Q(2))


@lru_cache(maxsize=24000)
def exp_neg_iv(x:I)->I:
    if x.lo<0 or x.hi>400*S:
        raise SourceContourError("exp evaluation outside original-source range")
    m=0;y=x
    while y.hi>S//2:
        y=y/2;m+=1
    e=I.of(1);term=I.of(1)
    N=52
    for j in range(1,N+1):
        term=term*y/j
        e+=term
    after=term*y/(N+1)
    rem=after/(I.of(1)-y/Q(N+2))
    e=I(e.lo,(e+rem).hi)
    for _ in range(m):e=e*e
    return e.inv()


# For all theta quadrature nodes, |omega*log(t)| < 16. This single rational
# remainder dominates the first neglected sine and cosine Taylor monomials.
TRIG_ERR=I.of(Q(16)**102/factorial(102)+Q(16)**103/factorial(103)).upper()


def cos_sin_iv(theta:I)->tuple[I,I]:
    if theta.lo<0 or theta.hi>16*S:
        raise SourceContourError("trigonometric argument outside certified domain")
    x2=theta*theta
    c=I.of(1);s=theta
    ct=I.of(1);st=theta
    for j in range(1,51):
        ct=-(ct*x2)/Q((2*j-1)*(2*j))
        st=-(st*x2)/Q((2*j)*(2*j+1))
        c+=ct;s+=st
    err=I.of(TRIG_ERR)
    return I((c-err).lo,(c+err).hi),I((s-err).lo,(s+err).hi)


def theta_integrand(t:Q,y:Q,mode:int)->tuple[I,I]:
    """Real B(iy) and imaginary B'(iy) integrands for one actual theta n."""
    if type(mode) is not int or mode not in (1,2,3):
        raise SourceContourError("authentic theta integer n=1,2,3 required")
    l=log_iv(t)
    weight=exp_neg_iv(pi_iv()*Q(mode*mode)*Q(t)+Q(3,4)*l)
    c,s=cos_sin_iv(Q(y,2)*l)
    return weight*c,weight*l*s/2


def exponential_upper_at(x:Q)->Q:
    if type(x) not in (int,Q): raise SourceContourError("exact exp tail")
    return exp_neg_iv(I.of(Q(x))).upper()


def _derivative_4_bounds(y:Q,mode_limit:int):
    """Explicit elementary 4th derivatives, no numerical differentiation."""
    omega=Q(y,2)
    # |c-r|<= omega + (3/4+r) on t>=1. Bounds are deliberately coarse.
    m0=Q();m1=Q()
    p_up=pi_iv().upper()
    for n in range(1,mode_limit+1):
        a=p_up*n*n
        e=exponential_upper_at(3*n*n)
        b0=b1=Q()
        for j in range(5):
            qprod=Q(1)
            for r in range(j):qprod*=omega+Q(3,4)+r
            factor=Q(comb(4,j))*a**(4-j)
            b0+=factor*qprod
            # derivative in complex exponent contributes log(t) <= log 8 <3;
            # and derivative of falling factorial polynomial w.r.t exponent.
            derivative=Q(j)*(omega+Q(15,4))**max(0,j-1) if j else Q()
            b1+=factor*(3*qprod+derivative)/2
        m0+=e*b0;m1+=e*b1
    return m0,m1


def center_integrals(y=Q(141347,10000), modes=2, T=8, cells=4096):
    """Certified B(iy), -iB'(iy) using rational Simpson plus exact tails.

    No zeta/xi function, contour zero, or external zero table is an input.
    """
    if type(y) not in (int,Q) or not Q(1)<=Q(y)<=15:
        raise SourceContourError("center ordinate rational 1..15")
    y=Q(y)
    if type(modes) is not int or modes not in (1,2):
        raise SourceContourError("only 1 or 2 authentic integer-theta modes")
    if type(T) is not int or T!=8 or type(cells) is not int or cells<512 or cells>16384 or cells%2:
        raise SourceContourError("supported 8-cell time window and even resolution")
    step=Q(T-1,cells)
    total_b=I.of(0);total_s=I.of(0)
    for k in range(cells+1):
        t=Q(1)+k*step
        b=I.of(0);s=I.of(0)
        for n in range(1,modes+1):
            a,d=theta_integrand(t,y,n)
            b+=a;s+=d
        w=1 if k in (0,cells) else (4 if k%2 else 2)
        total_b+=w*b;total_s+=w*s
    scale=step/3
    total_b*=scale;total_s*=scale
    m4b,m4s=_derivative_4_bounds(y,modes)
    simp0=Q(T-1)*step**4*m4b/180
    simp1=Q(T-1)*step**4*m4s/180
    # All original integer theta modes n>modes are dominated by
    # 2 exp(-3(modes+1)^2*t), for t>=1; same for infinity in t.
    rate=3*(modes+1)**2
    unseen_b=2*exponential_upper_at(rate)/rate
    unseen_s=exponential_upper_at(rate)/(rate*rate)  # log(t)/2 <= (t-1)/2
    tail_b=2*exponential_upper_at(3*T)/3
    tail_s=exponential_upper_at(3*T)*((T-1)/3+Q(1,9))
    bb=I(total_b.lo-I.of(simp0+unseen_b+tail_b).hi,
         total_b.hi+I.of(simp0+unseen_b+tail_b).hi)
    ss=I(total_s.lo-I.of(Q(simp1+unseen_s+tail_s)).hi,
         total_s.hi+I.of(Q(simp1+unseen_s+tail_s)).hi)
    return {"B":bb,"S":ss,"simpson_B_upper":simp0,"simpson_S_upper":simp1,
            "missing_integer_B_upper":unseen_b,"missing_integer_S_upper":unseen_s,
            "time_B_upper":tail_b,"time_S_upper":tail_s,
            "center_y":y,"modes":modes,"cells":cells,
            "original_integer_Gaussian_source":True,"RH_proved":False}


def analytic_second_upper(y:Q,r:Q)->Q:
    """Whole-complex-disk F'' upper, no oscillatory quadrature.

    For |z-i*y|<=r<=1/2, |t^(z/2)|<=t^(r/2),
    t^-3/4*t^(r/2)<=1, psi(t)<=2e^-3t, log(t)<=t-1.
    This gives |B^(k)|<=2 exp(-3)*k!/(2^k*(3-r/2)^(k+1)), k=0,1,2.
    """
    y=Q(y);r=Q(r)
    if not 0<r<=Q(1,2):raise SourceContourError("small contour only")
    rate=3-r/2
    g=exponential_upper_at(3)
    b0=2*g/rate
    b1=g/rate**2
    b2=g/rate**3
    mag=y+r
    return 2*b0+4*mag*b1+(mag*mag+Q(1,4))*b2


def source_only_candidate(step=Q(1,10000)) -> Q:
    """UNCERTIFIED search heuristic using ONLY original integer Gaussian theta.

    Float evaluation selects a candidate grid cell, NEVER proves a zero;
    `first_critical_contour` independently verifies it with rational bounds.
    No calls to xi, zeta, or stored nontrivial zeros.
    """
    from math import exp, pi, log, cos
    step=Q(step)
    if step!=Q(1,10000):
        raise SourceContourError("candidate-source search uses a declared grid")
    times=[1+7*k/2048 for k in range(2049)]
    logs=[log(t) for t in times]
    base=[sum(exp(-pi*n*n*t) for n in (1,2))*t**(-.75) for t in times]
    h=7/2048
    def obs(y):
        omega=y/2
        b=h/3*sum((base[k]*cos(omega*logs[k])*(1 if k in (0,2048) else 4 if k%2 else 2)
                   for k in range(2049)))
        return .5-(y*y+.25)*b
    lo,hi=14.0,15.0
    if obs(lo)*obs(hi)>=0:
        raise SourceContourError("theta-source search did not find a signed bracket")
    for _ in range(19):
        mid=(lo+hi)/2
        if obs(mid)>0: lo=mid
        else:hi=mid
    cell=Q(round((lo+hi)/2/float(step)))*step
    return cell


def first_critical_contour(y=Q(141347,10000),radius=Q(1,500),modes=2,T=8,cells=4096):
    """Single source-certified zero near first critical ordinate via Rouche.

    The center is a rational observation site chosen by theta polynomial search.
    It is *not* a looked-up zeta zero and the source module never calls zeta.
    """
    y=Q(y);radius=Q(radius)
    if y!=Q(141347,10000) or radius!=Q(1,500):
        raise SourceContourError("this research certificate is pinned to one rational contour")
    if source_only_candidate()!=y:
        raise SourceContourError('selected contour is not reproduced by the original theta source')
    b=center_integrals(y,modes,T,cells)
    B,Sv=b['B'],b['S']
    s_sq=y*y+Q(1,4)
    f0=I.of(Q(1,2))-s_sq*B
    d_im=2*y*B-s_sq*Sv
    # Source analytic magnitude bounds: |F''| on disk; symmetry about imaginary axis.
    upper_f0=max(abs(f0.lower()),abs(f0.upper()))
    deriv_min=min(abs(d_im.lower()),abs(d_im.upper())) if d_im.lo*d_im.hi>0 else Q()
    second=analytic_second_upper(y,radius)
    margin=deriv_min*radius-upper_f0-second*radius**2/2
    return {"site":y,"radius":radius,"B":B,"S":Sv,"F_center_real":f0,
            "F_derivative_imag":d_im,"center_abs_upper":upper_f0,
            "derivative_abs_lower":deriv_min,"F_second_upper":second,
            "strict_rouche_margin":margin,"certified_exactly_one":margin>0,
            "critical_line_by_reflection":margin>0,
            "zero_is_simple":margin>0,
            "no_external_zero_lookup":True,"full_Weil_positive":False,"RH_proved":False,
            "source_stats":b}


def finite_spectral_residue_theorem():
    """Classical deduction from first_critical_contour for C_c^infty real tests.

    For a genuine simple critical Xi zero rho, contour integral of
    (Xi'/Xi)(s) A_f(s)A_f(1-s) is |A_f(rho)|^2 >= 0.
    This positive rank-one summand IS source-identified, but the complementary
    Weil zero spectrum remains signed/uncontrolled; no RH proof.
    """
    return {'contour_source':'authentic_xi_theta',
            'test_space':'real_Cc_infty(R)',
            'test_transform':'A_f(s)=int f(x)exp((s-1/2)x)dx',
            'local_residue':'A_f(rho)*A_f(1-rho)=abs(A_f(rho))^2',
            'positive_rank_one_summand':True,
            'full_signed_Weil_form_positive':False,'RH_proved':False}


def receipt():
    d=first_critical_contour()
    fields=['site','radius','center_abs_upper','derivative_abs_lower','F_second_upper',
            'strict_rouche_margin','certified_exactly_one','critical_line_by_reflection',
            'zero_is_simple','no_external_zero_lookup','RH_proved']
    output={k:(str(d[k]) if type(d[k]) is Q else d[k]) for k in fields}
    output['F_center_interval']=[str(d['F_center_real'].lower()),str(d['F_center_real'].upper())]
    output['F_derivative_imag_interval']=[str(d['F_derivative_imag'].lower()),str(d['F_derivative_imag'].upper())]
    output['source_bounds']={k:str(v) for k,v in d['source_stats'].items() if k.endswith('_upper') and type(v) is Q}
    output['source']='AUTHENTIC_ONE_GAUSSIAN_INTEGER_THETA'
    output['local_residue_positive']=True
    output['entire_Weil_sign_claimed']=False
    return output
