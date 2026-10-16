"""Source-gated, outward rational enclosures for genuine prime-active Weil B-spline Grams.

Original zeta, conductor 1, even Gamma_R(s), both poles, original contact
-(EulerGamma+log(4*pi)), authentic von Mangoldt p^k/sqrt(n) atoms.
No nontrivial zeros, no RH claim; a two-dimensional subspace is not a global Schur sign.

All analytic enclosures are derived from rational bounds (Taylor alternating,
Euler harmonic inequalities and analytic Gamma ladder tail). No floating rounding.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, factorial, isqrt
from functools import lru_cache

SCALE = 10 ** 55


class WeilSplineGate(ValueError):
    pass


def rat(x):
    if type(x) is int or isinstance(x, Q):
        return Q(x)
    raise WeilSplineGate("exact rational source, no float")


def _floor(q: Q) -> int:
    return q.numerator // q.denominator


def _ceil(q: Q) -> int:
    return -_floor(-q)


@dataclass(frozen=True)
class Iv:
    """Outward rational interval at fixed scale 10^-55. Endpoints are integers."""
    lo: int
    hi: int

    def __post_init__(self):
        if type(self.lo) is not int or type(self.hi) is not int or self.lo > self.hi:
            raise WeilSplineGate("invalid rational interval")

    @classmethod
    def q(cls, q):
        z = rat(q) * SCALE
        return cls(_floor(z), _ceil(z))

    @classmethod
    def bracket(cls, lo, hi):
        a, b = rat(lo)*SCALE, rat(hi)*SCALE
        if a > b:
            raise WeilSplineGate("reversed interval")
        return cls(_floor(a), _ceil(b))

    @property
    def lower(self):
        return Q(self.lo, SCALE)

    @property
    def upper(self):
        return Q(self.hi, SCALE)

    def __add__(self, other):
        b = other if isinstance(other, Iv) else Iv.q(other)
        return Iv(self.lo+b.lo,self.hi+b.hi)

    def __radd__(self, other):
        return self+other

    def __neg__(self):
        return Iv(-self.hi,-self.lo)

    def __sub__(self, other):
        return self+(-as_iv(other))

    def __rsub__(self, other):
        return as_iv(other)-self

    def __mul__(self, other):
        if isinstance(other,Iv):
            values=(self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi)
            return Iv(min(values)//SCALE,-((-max(values))//SCALE))
        x=rat(other)
        a=Q(self.lo)*x
        b=Q(self.hi)*x
        return Iv(_floor(min(a,b)),_ceil(max(a,b)))

    def __rmul__(self,other):
        return self*other

    def __truediv__(self,other):
        x=rat(other)
        if x == 0: raise ZeroDivisionError
        return self* (1/x)

    def __pow__(self,k):
        if type(k) is not int or not 0<=k<=100:
            raise WeilSplineGate("nonnegative finite integer power only")
        if k==0: return Iv.q(1)
        out=Iv.q(1)
        base=self
        while k:
            if k&1: out=out*base
            base=base*base
            k//=2
        return out

    def widen(self,eps):
        e=rat(eps)
        if e<0: raise WeilSplineGate("negative error")
        return self + Iv.bracket(-e,e)

    def positive_part(self):
        return Iv(max(0,self.lo),max(0,self.hi))

    def positive_inverse(self):
        if self.lo<=0: raise WeilSplineGate("reciprocal requires positive interval")
        return Iv(_floor(Q(SCALE*SCALE,self.hi)),_ceil(Q(SCALE*SCALE,self.lo)))


def as_iv(x):
    return x if isinstance(x,Iv) else Iv.q(x)


@lru_cache(maxsize=8192)
def exp_minus(q):
    """Enclosure e^-q for rational q>=0 using alternating Taylor + squaring."""
    r=rat(q)
    if r<0: raise WeilSplineGate("exp_minus requires q>=0")
    if not r: return Iv.q(1)
    m=0
    y=r
    while y>Q(1,2):
        y/=2
        m+=1
        if m>40: raise WeilSplineGate("exponent budget exceeded")
    term=Q(1)
    partial=term
    low=None
    high=None
    for k in range(1,35):
        term*= -y/k
        partial+=term
        if k==33: low=partial
        if k==34: high=partial
    ans=Iv.bracket(low,high)
    for _ in range(m):
        ans=ans*ans
    return ans


def exp_any(q):
    z=rat(q)
    if z>=0:
        return exp_minus(z).positive_inverse()
    return exp_minus(-z)


def log_point_over_one(x,terms=100):
    """Rational atanh lower/upper logs for rational x>1."""
    x=rat(x)
    if not x>1 or type(terms) is not int or not 1<=terms<=1000:
        raise WeilSplineGate("log requires x>1 and positive terms")
    r=(x-1)/(x+1)
    r2=r*r
    term=r
    partial=Q(0)
    for k in range(terms):
        partial+=2*term/(2*k+1)
        term*=r2
    tail=2*term/((2*terms+1)*(1-r2))
    return Iv.bracket(partial,partial+tail)


def log_int(n):
    if type(n) is not int or not 2<=n<=100_000:
        raise WeilSplineGate("bounded positive integer log")
    if n==2: return log_point_over_one(2,55)
    if n & (n-1)==0:
        return (n.bit_length()-1)*log_int(2)
    return log_point_over_one(n,160)


def _arctan_01_inv(n,terms):
    # for 1/n, alternating terms. 2k odd upper, 2k+1 even lower.
    assert n>1
    y=Q(1,n)
    acc=Q(0)
    for k in range(2*terms):
        term=(-1)**k * y**(2*k+1)/Q(2*k+1)
        acc+=term
        if k==2*terms-2: upper=acc
    return Iv.bracket(acc,upper)


@lru_cache(maxsize=1)
def pi_interval():
    return 16*_arctan_01_inv(5,12) - 4*_arctan_01_inv(239,12)


@lru_cache(maxsize=1)
def euler_gamma_interval():
    # Classical sharp Euler harmonic inequality:
    # 1/(2(n+1)) < H_n-log n-gamma < 1/(2n).
    n=1024
    h=sum((Q(1,k) for k in range(1,n+1)),Q(0))
    ln_n=10*log_int(2)
    return Iv.q(h)-ln_n-Iv.bracket(Q(1,2*(n+1)), Q(1,2*n))


@lru_cache(maxsize=1)
def zeta_contact():
    pi=pi_interval()
    if pi.lo <= 0: raise AssertionError("pi bound bad")
    log_pi=Iv.bracket(log_point_over_one(pi.lower,100).lower,
                      log_point_over_one(pi.upper,100).upper)
    return -euler_gamma_interval() - 2*log_int(2) - log_pi


def central_bspline7_at_rational(x):
    xx=rat(x)
    return sum((Q((-1)**j*comb(8,j))*max(xx+4-j,0)**7 for j in range(9)),Q(0))/5040


def _spline_interval(x,h,d):
    """Autocorrelation of two shifted cubic B-spline densities."""
    h,d=rat(h),rat(d)
    y=(as_iv(x)-d)/h
    terms=Iv.q(0)
    for j in range(9):
        terms+= (-1)**j * comb(8,j) * (y+4-j).positive_part()**7
    return terms/Q(5040)/h


def _split_poly(h,d,sign,mid):
    h,d=rat(h),rat(d)
    out=[Q(0) for _ in range(8)]
    for j in range(9):
        knot=d+Q(j-4)*h
        if sign*mid<=knot: continue
        weight=Q((-1)**j*comb(8,j), factorial(7)) / (h**8)
        for k in range(8):
            out[k]+=weight*comb(7,k)*(sign**k)*(-knot)**(7-k)
    return out


def _spline_symmetric_poly(h,d,mid):
    a=_split_poly(h,d,1,mid)
    b=_split_poly(h,d,-1,mid)
    return [u+v for u,v in zip(a,b)]


def _spline_knots(h,d):
    h,d=rat(h),rat(d)
    radius=4*h+abs(d)
    knots={Q(0),radius}
    for j in range(9):
        k=d+Q(j-4)*h
        for v in (k,-k):
            if 0<v<radius: knots.add(v)
    return tuple(sorted(knots))


def _laplace_moments(a,left,right):
    a,left,right=rat(a),rat(left),rat(right)
    L=exp_minus(a*left)
    R=exp_minus(a*right)
    moments=[(L-R)/a]
    for k in range(1,8):
        moments.append((left**k*L-right**k*R)/a + (Q(k)/a)*moments[-1])
    return moments


def symmetric_spline_laplace(h,d,a):
    """Outward analytic integral ∫_0∞ e^-a x [g(x)+g(-x)] dx."""
    out=Iv.q(0)
    cuts=_spline_knots(h,d)
    for left,right in zip(cuts[:-1],cuts[1:]):
        mid=(left+right)/2
        coeff=_spline_symmetric_poly(h,d,mid)
        moments=_laplace_moments(a,left,right)
        out+=sum((coef*v for coef,v in zip(coeff,moments)),Iv.q(0))
    return out


def pole_integral(h,d):
    """Exact spline uniform-convolution MGF, enclosed via exp arithmetic."""
    h,d=rat(h),rat(d)
    sh=(exp_any(h/4)-exp_minus(h/4))/2
    si=sh/(h/4)
    return (exp_any(d/2)+exp_any(-d/2))*si**8


def _prime_label(n):
    if type(n) is not int or n<2: raise WeilSplineGate("prime powers n>=2 only")
    # Detect genuine prime p^k; reject anything with two different prime factors.
    for p in range(2,isqrt(n)+2):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return p if m==1 else None
    return n


def _sqrt_interval(n):
    q=isqrt(n*SCALE*SCALE)
    return Iv(q,q+1)


def _prime_single(h,d,n):
    p=_prime_label(n)
    if p is None: raise WeilSplineGate("fake composite impulses refused")
    logn=log_int(n)
    lp=log_int(p)
    weight=lp*_sqrt_interval(n).positive_inverse()
    return weight*(_spline_interval(logn,h,d)+_spline_interval(-logn,h,d))


def genuine_prime_tape(h,d):
    """Finite support with conservative integer cutoff and certified log comparisons."""
    h,d=rat(h),rat(d)
    radius=4*h+abs(d)
    if not Q(0)<radius<=Q(3):
        raise WeilSplineGate("proved implementation support 0<R<=3")
    # 3^ceil(R) is a sufficient cutoff from e<3, including all genuine labels.
    ceiling=(_ceil(radius))
    limit=3**ceiling
    out=[]
    for n in range(2,limit+1):
        p=_prime_label(n)
        if p is None: continue
        x=log_int(n)
        if x.upper < radius: out.append((n,p))
        elif x.lower <= radius:
            raise WeilSplineGate("support boundary ambiguous, refine logarithm")
    return tuple(out)


def gamma_tail_error(h,J):
    h=rat(h)
    if not h>0 or type(J) is not int or not 1<=J<=512:
        raise WeilSplineGate("positive rational h, J in 1..512")
    # ||B7||infty <= ||B3||infty=2/3; ||B7''|| <= ||B3''||=2.
    m0=Q(2,3)/h
    m2=Q(2)/h**3
    a=Q(2*J)+Q(1,2)
    return m0/a**2+(m2+m0/4)*(Q(1,2)/a**2+Q(2)/a**3)


def completed_weil_bspline_entry(h,d,J=64, *,tape=None):
    """Fully rational enclosure W_zeta(g_h(.-d)), using completed signed source."""
    h,d=rat(h),rat(d)
    if not Q(0)<h<=Q(1,2) or abs(d)>Q(1,2):
        raise WeilSplineGate("scoped source basis h<=1/2 and |d|<=1/2")
    expected=genuine_prime_tape(h,d)
    if tape is None: tape=expected
    if type(tape) is not tuple or tape!=expected:
        raise WeilSplineGate("source tape mismatch; counterfeit or missing prime-power")
    g0=central_bspline7_at_rational((-d)/h)/h
    pole=pole_integral(h,d)
    contact=zeta_contact()*g0
    gamma=Iv.q(0)
    for j in range(J):
        a=Q(2*j)+Q(1,2)
        gamma+=symmetric_spline_laplace(h,d,a) - Q(2)*g0/(a+Q(1,2))
    arch=contact-gamma
    tail_a=Q(2*J)+Q(1,2)
    arch-=Q(g0)/(2*tail_a)
    prime=sum((_prime_single(h,d,n) for n,p in expected),Iv.q(0))
    total=pole+arch-prime
    err=gamma_tail_error(h,J)
    return {
        "value":total.widen(err),
        "central_approximation":total,
        "pole":pole,
        "contact":contact,
        "finite_ladder":-gamma,
        "tail_correction":Q(-g0,1)/(2*tail_a),
        "prime":-prime,
        "analytic_tail_error":err,
        "source_tape":expected,
        "half_density":Q(1,2),
        "conductor":1,
        "parity":0,
        "poles":(0,1),
        "RH_proved":False,
    }


def two_spline_prime_active_gram(J=64):
    """Two cubic log-test translates inside Suzuki (-1/2,1/2) support."""
    h=Q(1,5)
    d=Q(1,10)
    a=completed_weil_bspline_entry(h,Q(0),J)
    b=completed_weil_bspline_entry(h,d,J)
    # Matrix [[a,b],[b,a]]. Eigenvalues exactly a+b and a-b.
    lo1=a["value"].lower+b["value"].lower
    lo2=a["value"].lower-b["value"].upper
    upper1=a["value"].upper+b["value"].upper
    upper2=a["value"].upper-b["value"].lower
    K=contact_neumann_gram(h,d)
    rel_lower=min(lo1/K["eigenvalues"][0],lo2/K["eigenvalues"][1])
    return {
        "h":h,"shift":d,"Suzuki_radius":Q(1,2),
        "diag":a,"cross":b,
        "source_relative_neumann_lower":rel_lower,
        "certified_relative_neumann_coercive":rel_lower>0,
        "smallest_eigenvalue_lower":min(lo1,lo2),
        "eigenvalue_intervals":((lo1,upper1),(lo2,upper2)),
        "is_positive_certified":min(lo1,lo2)>0,
        "original_low_schur_sign_verified":False,
        "all_a_or_RH_proved":False,
    }


def cubic_spline_derivative_segments(h,t):
    """Piecewise rational polynomial (coeff u^0..u^2) for f_t'(u)."""
    h,t=rat(h),rat(t)
    if h<=0: raise WeilSplineGate("positive mesh required")
    knots=[t+Q(j-2)*h for j in range(5)]
    cuts=sorted(set([Q(-1,2),Q(1,2)]+[x for x in knots if Q(-1,2)<x<Q(1,2)]))
    out=[]
    for lo,hi in zip(cuts[:-1],cuts[1:]):
        mid=(lo+hi)/2
        coeff=[Q(0),Q(0),Q(0)]
        for j,knot in enumerate(knots):
            if mid<=knot: continue
            pref=Q((-1)**j*comb(4,j),2*h**4)
            coeff[0]+=pref*knot*knot
            coeff[1]+=-2*pref*knot
            coeff[2]+=pref
        out.append((lo,hi,tuple(coeff)))
    return tuple(out)


def _poly_prod(a,b):
    ans=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            ans[i+j]+=x*y
    return ans


def _poly_integral(coeff,lo,hi):
    return sum((x*(hi**(k+1)-lo**(k+1))/(k+1) for k,x in enumerate(coeff)),Q(0))


def _legendre_polynomials_u(max_degree):
    if type(max_degree) is not int or not 1<=max_degree<=128:
        raise WeilSplineGate("finite Legendre projection degree")
    prev=[Q(1)]
    curr=[Q(0),Q(2)] # P1(2u)
    out=[prev,curr]
    for n in range(1,max_degree):
        u_times=[Q(0)]+curr
        nxt=[Q(0)]*len(u_times)
        for k,c in enumerate(u_times):nxt[k]+=Q(2*n+1,n+1)*2*c
        for k,c in enumerate(prev):nxt[k]-=Q(n,n+1)*c
        out.append(nxt)
        prev,curr=curr,nxt
    return out


def original_legendre_spline_projection(h=Q(1,5),t=Q(0),rank=30):
    """Exact L2 projection of i*f'_t to original meanzero Legendre low modes.

    Caution: does NOT supply source G P/Q blocks or the low Schur sign.
    """
    h,t=rat(h),rat(t)
    if 2*h+abs(t)>Q(1,2):
        raise WeilSplineGate("spline must be supported within Suzuki a=1/2")
    segments=cubic_spline_derivative_segments(h,t)
    norm=sum((_poly_integral(_poly_prod(c,c),lo,hi)
              for lo,hi,c in segments),Q(0))
    modes=_legendre_polynomials_u(rank)
    coeff=[]
    for k in range(rank+1):
        ck=sum((_poly_integral(_poly_prod(c,modes[k]),lo,hi)
                 for lo,hi,c in segments),Q(0))
        coeff.append(ck)
    if coeff[0]!=0:raise AssertionError("derivative does not have zero mean")
    low=sum(((2*k+1)*coeff[k]**2 for k in range(1,rank+1)),Q(0))
    high=norm-low
    if high<0:raise AssertionError("Legendre Parseval remainder negative")
    return {"center":t,"mesh":h,"rank":rank,"full_L2_norm_squared":norm,
            "low_projection_norm_squared":low,
            "high_residual_norm_squared":high,
            "high_residual_nonzero":high>0,
            "first_mode_integrals":tuple(coeff[:min(6,len(coeff))]),
            "low_Schur_sign_proved":False}


def contact_neumann_gram(h=Q(1,5),d=Q(1,10)):
    """Exact K=(-Delta_N)^-1 relative Neumann metric on source u=i f'."""
    h,d=rat(h),rat(d)
    if 2*h+abs(d)>Q(1,2):raise WeilSplineGate("not within radius a=1/2")
    c0=central_bspline7_at_rational(0)/h
    c1=central_bspline7_at_rational(d/h)/h
    return {"diag":c0,"cross":c1,"eigenvalues":(c0+c1,c0-c1),
            "Neumann_Gram_equal_spline_L2":True,"contact_perturbation_same_metric":True}


def contact_mutant_gram(c=Q(-1,8), J=64):
    """Artificial delta_0 contact shift; negative witness is against MUTANT only."""
    c=rat(c)
    src=two_spline_prime_active_gram(J)
    K=contact_neumann_gram()
    wp=src["eigenvalue_intervals"][0]
    wm=src["eigenvalue_intervals"][1]
    cp,cm=K["eigenvalues"]
    def interval_shift(w,k):
        return (w[0]+c*k,w[1]+c*k)
    return {"mutant_contact":c,"positive_vector_branch":interval_shift(wp,cp),
            "negative_vector_branch":interval_shift(wm,cm),
            "mutant_has_certified_negative":interval_shift(wp,cp)[1]<0,
            "genuine_source_changed":True,"RH_disproved":False}


def fake6_source_probe(h=Q(1,2)):
    """Detect a fake composite at six only after log-source activation."""
    h=rat(h)
    if h!=Q(1,2):raise WeilSplineGate("mutant witness fixed at h=1/2")
    w=log_int(6)*_sqrt_interval(6).positive_inverse()
    bp=_spline_interval(log_int(6),h,Q(0))
    bm=_spline_interval(-log_int(6),h,Q(0))
    defect= -w*(bp+bm)
    if defect.hi>=0:raise AssertionError("fake6 signed effect not certified negative")
    return {"fake6_signed_effect":defect,"strictly_negative":True,
            "mutant_not_original_euler":True,"true_source_tape_contains_six":False}


def arbitrarily_hidden_positive_non_euler_source(m=4):
    """Exact countermodel for positive σ>1 Mellin data -> global zero constraints.

    For N=6^(4m), A=6^(3m), the positive Dirichlet multiplier
       F_m(s)=1+A*N^(-s)
    has zeros at s=3/4+(2k+1)i*pi/log(N). For Re(s)>=5/4,
       |F_m(s)-1|<=6^(-2m).
    This source is NON-Euler and not self-dual; it is not a counterfeit of the
    original completed zeta's exact normalization, and does NOT refute RH.
    """
    if type(m) is not int or not 1<=m<=100:
        raise WeilSplineGate("finite exact positive integer epoch 1..100")
    N=6**(4*m)
    A=6**(3*m)
    bound=Q(1,6**(2*m))
    return {
        "source_label":"POSITIVE_NON_EULER_COUNTERMODEL",
        "N":N,"positive_dirichlet_weight":A,
        "offcritical_zero_real_part":Q(3,4),
        "zero_imaginary_height_formula":f"(2*k+1)*pi/({4*m}*log(6))",
        "uniform_multiplier_error_on_Re_s_at_least_5_over_4":bound,
        "normalization_at_sigma_5_over_4":1+bound,
        "all_coefficients_positive":True,
        "functional_equation_authenticated":False,
        "Euler_prime_source_authenticated":False,
        "RH_refuted":False,
    }


def normalized_test_continuity_budget(radius, norm_f, norm_v, delta_f0,delta_f1):
    """Exact rational inherited source W C1 continuity through f*tilde f.

    Premises: supp(f),supp(v)⊂[-a,a]; real ||f||∞<=norm_f,
    ||v||∞<=norm_v, ||f-v||∞<=delta_f0,
    ||(f-v)'||∞<=delta_f1; g,h supports in [-2a,2a].
    Uses the repository's CTW-06 zeta fixed-support rational constants.
    Not a numerical proof of these user-supplied norm premises.
    """
    a=rat(radius)
    nf,nv,d0,d1=map(rat,(norm_f,norm_v,delta_f0,delta_f1))
    if a<=0 or any(v<0 for v in (nf,nv,d0,d1)):
        raise WeilSplineGate("positive radius, nonnegative verified norm premises")
    R=2*a
    if R>Q(3):raise WeilSplineGate("continuity implementation declared R<=3")
    # Overcount the authentic prime events using p as rational upper envelope.
    labels=genuine_prime_tape(R/4,Q(0))
    bprime=2*sum((p for n,p in labels),0)
    ceil_half=_ceil(R/2)
    pole=4*R*3**ceil_half
    alpha=Q(1,2)
    I=1/alpha**2+1/(2*alpha)
    C0=pole+bprime+4+I
    C1=2*I
    return 2*a*(nf+nv)*(C0*d0+C1*d1)


_ORIGINAL_LEGENDRE_AUTOCORRELATIONS = {
    # u1(x)=P1(2x)=2x; v1=D^-1 u1=x*x-1/4 on [-1/2,1/2].
    # For 0<=r<=1, g1(r)=int v1(x)v1(x-r) dx.
    1:(Q(1,30),Q(0),Q(-1,6),Q(1,6),Q(0),Q(-1,30)),
    # u2(x)=P2(2x)=6x*x-1/2; v2=2x^3-x/2.
    2:(Q(1,210),Q(0),Q(-1,10),Q(1,6),Q(0),Q(-1,10),Q(0),Q(1,35)),
}


def _poly_interval_value(coeff,x):
    x=as_iv(x)
    out=Iv.q(0)
    for c in reversed(coeff):out=out*x+c
    return out


def _poly_exp_moments(a,left,right,degree):
    a,left,right=rat(a),rat(left),rat(right)
    if a==0:raise WeilSplineGate("nonzero exponential rate required")
    L=exp_any(-a*left)
    R=exp_any(-a*right)
    moments=[(L-R)/a]
    for k in range(1,degree+1):
        moments.append((left**k*L-right**k*R)/a+(Q(k)/a)*moments[-1])
    return moments


def _poly_exp_integral(coeff,a,left=Q(0),right=Q(1)):
    ms=_poly_exp_moments(a,left,right,len(coeff)-1)
    return sum((c*m for c,m in zip(coeff,ms)),Iv.q(0))


def genuine_original_low_legendre_diagonal(mode,J=64):
    """ORIGINAL Suzuki low A principal entry for first two unnormalized Legendre modes.

    u=P_mode(2x), v=iD^-1u (phase harmless), g=v*tilde v; W(g)=<G u,u>.
    This is actual low A, not Schur S0=A-R0. No result for remaining 28 modes.
    """
    if type(mode) is not int or mode not in (1,2):
        raise WeilSplineGate("only original first two low Legendre modes certified")
    if type(J) is not int or not 1<=J<=512:
        raise WeilSplineGate("valid source Gamma J")
    coeff=_ORIGINAL_LEGENDRE_AUTOCORRELATIONS[mode]
    g0=coeff[0]
    # For even g compact on [-1,1], P=2 int_0^1 (exp(+x/2)+exp(-x/2))*g(x) dx.
    pole=Q(2)*(_poly_exp_integral(coeff,-Q(1,2))+
               _poly_exp_integral(coeff,Q(1,2)))
    # one true prime-power impulse n=2 only, since log2 < 1 < log3.
    source=((2,2),)
    if not log_int(2).upper<Q(1)<log_int(3).lower:
        raise WeilSplineGate("prime activation bounds lost")
    gamma=Iv.q(0)
    for j in range(J):
        a=Q(2*j)+Q(1,2)
        gamma+=2*_poly_exp_integral(coeff,a)-2*g0/(a+Q(1,2))
    arch=zeta_contact()*g0-gamma-g0/(2*(Q(2*J)+Q(1,2)))
    prime=2*log_int(2)*_sqrt_interval(2).positive_inverse()*_poly_interval_value(coeff,log_int(2))
    total=pole+arch-prime
    # Exact Cauchy bounds for g=v*tilde v: ||g||∞<=||v||_2^2 = g0;
    # ||g''||∞<=||v'||_2^2, source u1^2=1/3; u2^2=1/5.
    M0=g0
    M2={1:Q(1,3),2:Q(1,5)}[mode]
    a=Q(2*J)+Q(1,2)
    err=M0/a**2+(M2+M0/4)*(Q(1,2)/a**2+2/a**3)
    enclosure=total.widen(err)
    return {"mode":mode,"source":source,"Suzuki_radius":Q(1,2),
            "unnormalized_Legendre":f"P_{mode}(2x)",
            "interval":enclosure,"central_approximation":total,
            "pole":pole,"arch":arch,"prime":-prime,
            "tail_error":err,"original_low_A_positive_certified":enclosure.lower>0,
            "original_low_Schur_S0_positive":False,"RH_proved":False}


def original_two_mode_low_block(J=64):
    """Original P1/P2 source-computed principal block of A=P30 G P30.

    Offdiag 0 exactly by parity: v1 even, v2 odd, W even. DOES NOT bound R0.
    """
    p1=genuine_original_low_legendre_diagonal(1,J)
    p2=genuine_original_low_legendre_diagonal(2,J)
    return {"low_A11":p1,"low_A22":p2,
            "offdiag":Q(0),
            "smallest_diagonal_lower":min(p1['interval'].lower,p2['interval'].lower),
            "original_low_A_on_span_P1_P2_positive":min(p1['interval'].lower,p2['interval'].lower)>0,
            "source_zero_shift_R0_computed":False,
            "Schur_S0_proved":False,"RH_proved":False}
