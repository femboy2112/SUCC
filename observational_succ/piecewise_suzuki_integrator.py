"""Analytic finite Suzuki Gamma+prime-2 derivative integrals; no spatial quadrature.

A positive-half interval is split at the EXACT source-defined hinge
x=log(2)-1/2. On each side, original (G_J P_k)' is an exponential-polynomial
with rational-interval coefficients. Integrals of products and degree<=3
polynomial moments use antiderivatives; no midpoint/Lipschitz sampling.
The infinite Gamma tail, high Schur inverse and RH sign are separate gates.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb


def _q(x):
    if type(x) not in (int,F):raise ValueError("exact int/Fraction required")
    return F(x)


@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __post_init__(self):
        lo,hi=_q(self.lo),_q(self.hi)
        if lo>hi:raise ValueError("reversed source interval")
        object.__setattr__(self,"lo",lo);object.__setattr__(self,"hi",hi)
    @staticmethod
    def of(x):
        if isinstance(x,I):return x
        if isinstance(x,(tuple,list)) and len(x)==2:return I(x[0],x[1])
        return I(_q(x),_q(x))
    def __add__(self,o):
        o=I.of(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-I.of(o)
    def __rsub__(self,o):return I.of(o)+-self
    def __mul__(self,o):
        o=I.of(o);x=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(x),max(x))
    __rmul__=__mul__
    def inverse(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError("uncertain denominator")
        return I(F(1,self.hi),F(1,self.lo))
    def __truediv__(self,o):return self*I.of(o).inverse()
    def __rtruediv__(self,o):return I.of(o)*self.inverse()
    def __pow__(self,k):
        if type(k) is not int or k<0:raise ValueError("nonnegative exact power")
        z=I.of(1)
        for _ in range(k):z=z*self
        return z
    def mid(self):return (self.lo+self.hi)/2
    def rad(self):return (self.hi-self.lo)/2
    def intersects(self,o):
        o=I.of(o);return self.lo<=o.hi and o.lo<=self.hi


def _pc(p):
    p=[I.of(x) for x in p]
    while len(p)>1 and p[-1]==I.of(0):p.pop()
    return tuple(p) if p else (I.of(0),)


def _pa(a,b):
    return _pc([(a[i] if i<len(a) else I.of(0))+
                (b[i] if i<len(b) else I.of(0))
                for i in range(max(len(a),len(b)))])


def _pm(a,b):
    out=[I.of(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
    return _pc(out)


def _pe(p,x):
    z=I.of(0);x=I.of(x)
    for c in reversed(p):z=z*x+c
    return z


def _pshift(p,d):
    d=I.of(d);out=[I.of(0)]*len(p)
    for k,c in enumerate(p):
        for j in range(k+1):out[j]=out[j]+I.of(c)*comb(k,j)*d**(k-j)
    return _pc(out)


def _exp_iv(x,digits):
    """Source-independent interval arithmetic, inherited exact exp proof."""
    from . import suzuki_legendre_source as L
    x=I.of(x)
    def lower(t):
        if t<=0:return L.tight_exp_neg(-t,digits)[0]
        return F(1,L.tight_exp_neg(t,digits)[1])
    def upper(t):
        if t<=0:return L.tight_exp_neg(-t,digits)[1]
        return F(1,L.tight_exp_neg(t,digits)[0])
    return I(lower(x.lo),upper(x.hi))


def _integral(p,rate,left,right,digits):
    """Exact polynomial-exponential antiderivative, interval evaluated endpoints."""
    p=_pc(p);rate=_q(rate);left=I.of(left);right=I.of(right)
    if left.hi>right.lo:raise ValueError("unproved interval endpoint ordering")
    if not rate:
        return sum((c*(right**(i+1)-left**(i+1))/F(i+1)
                    for i,c in enumerate(p)),I.of(0))
    anti=[I.of(0)]*len(p)
    for k,c in enumerate(p):
        factor=F(1,rate)
        for m in range(k,-1,-1):
            anti[m]=anti[m]+c*factor
            factor=-factor*m/rate
    return _exp_iv(rate*right,digits)*_pe(_pc(anti),right)-_exp_iv(rate*left,digits)*_pe(_pc(anti),left)


@dataclass(frozen=True)
class ExponentialPolynomial:
    """Sum rate->interval-coefficient polynomial times exp(rate*x)."""
    terms:tuple
    def __post_init__(self):
        data={}
        for rate,p in self.terms:
            rate=_q(rate);data[rate]=_pa(data.get(rate,(I.of(0),)),_pc(p))
        object.__setattr__(self,"terms",tuple(sorted(
            (r,p) for r,p in data.items() if any(v!=I.of(0) for v in p))))
    @classmethod
    def polynomial(cls,p):return cls(((F(0),_pc(p)),))
    def __add__(self,o):
        if not isinstance(o,ExponentialPolynomial):o=ExponentialPolynomial.polynomial((o,))
        return ExponentialPolynomial(self.terms+o.terms)
    __radd__=__add__
    def scale(self,c):
        return ExponentialPolynomial(tuple((r,tuple(I.of(c)*v for v in p))
                                           for r,p in self.terms))
    def __mul__(self,o):
        if not isinstance(o,ExponentialPolynomial):return self.scale(o)
        return ExponentialPolynomial(tuple((r+s,_pm(p,q))
                                           for r,p in self.terms for s,q in o.terms))
    __rmul__=__mul__
    def integrate(self,left,right,digits=100):
        return sum((_integral(p,r,left,right,digits) for r,p in self.terms),I.of(0))
    def value(self,x,digits=100):
        return sum((_pe(p,x)*_exp_iv(r*I.of(x),digits) for r,p in self.terms),I.of(0))


def authentic_mode_piecewise(k,J,*,digits=100):
    """Original signed Weil source formula, not fitted/interpolated data.

    Positive half: region 0<=x<=log2-1/2 has no prime atom.
    Region log2-1/2<=x<=1/2 has one genuine p=2 primitive shift.
    """
    from . import suzuki_legendre_source as L
    from .tate_suzuki_shorting import verify_original_suzuki_source
    if type(k) is not int or not 1<=k<=12 or type(J) is not int or not 1<=J<=20:
        raise ValueError("original Legendre mode 1..12 and Gamma J 1..20 required")
    if type(digits) is not int or not 40<=digits<=180:raise ValueError("digits 40..180")
    verify_original_suzuki_source()
    src=L._pinned_source();a=F(1,2)
    p=L.legendre_polynomial(k,a)
    v=L.poly_primitive_zero_at_left(p,a)
    if L.poly_eval(v,a):raise ArithmeticError("mean-zero source violation")
    contact=src.contact_iv()
    # One SHARED global scalar C_inf, never independent interval copies inside
    # products: exact midpoint packet; omitted correlated uncertainty is bounded
    # on the polynomial quotient by the source Schur adapter.
    contact_mid=(contact.lo+contact.hi)/2
    base=ExponentialPolynomial.polynomial(v).scale(I.of(contact_mid))
    # Both genuine completed pole channels in source derivative convention.
    plus=L.exp_antiderivative_poly(p,F(1,2),+1)
    minus=L.exp_antiderivative_poly(p,F(1,2),-1)
    ea=_exp_iv(F(1,4),digits);em=_exp_iv(F(-1,4),digits)
    integral_plus=ea*L.poly_eval(plus,a)-em*L.poly_eval(plus,-a)
    integral_minus=em*L.poly_eval(minus,a)-ea*L.poly_eval(minus,-a)
    # IMPORTANT sign/orientation: the original source has
    # -2*exp_minus(-x/2)*I_minus + 2*exp_minus(x/2)*I_plus.
    # exp_minus(-x/2)=exp(+x/2). Reversing these pole exponents is a
    # very plausible but DECISIVELY REFUTED source-normalization mutation.
    base=base+ExponentialPolynomial(((F(1,2),(-2*integral_minus,)),
                                     (F(-1,2),(2*integral_plus,))))
    # Authentic Gamma OU coefficients. Finite J can be integrated analytically.
    for j in range(J):
        d=4*j+1;alpha=F(d,2)
        fp=L.exp_antiderivative_poly(p,alpha,+1)
        fm=L.exp_antiderivative_poly(p,alpha,-1)
        bulk=L.poly_add(fp,fm)
        ea=_exp_iv(-alpha*a,digits)
        base=base+ExponentialPolynomial((
            (F(0),tuple(-F(2,d)*I.of(c) for c in bulk)),
            (-alpha,(F(2,d)*ea*L.poly_eval(fp,-a),)),
            (alpha,(F(2,d)*ea*L.poly_eval(fm,a),))
        ))
    b=I(*L.tight_log2(digits))
    recorded=src.log2_iv()
    if not (b.intersects((recorded.lo,recorded.hi)) and F(1,2)<b.lo and b.hi<1):
        raise ArithmeticError("source-justified log2 prime boundary absent")
    inv=src.sqrt_inverse(2)
    prime=ExponentialPolynomial.polynomial(_pshift(v,-b)).scale(b*I(inv.lo,inv.hi))
    return base,base+prime,b


def genuine_piecewise_gram(J=3,rank=4,*,digits=100):
    """Exact-analytic finite-Gamma H'_J and Q_(poly<=3) derivative Grams.

    All arithmetic outward rational, only original p=2 activation:
      [0,b-1/2] no prime, [b-1/2,1/2] prime.
    Full and projected matrices are interval enclosures, NOT PSD assertions.
    """
    from . import suzuki_legendre_source as L
    if type(rank) is not int or not 1<=rank<=8:
        raise ValueError("rank 1..8 for certified finite Legendre packet")
    modes=[authentic_mode_piecewise(k,J,digits=digits) for k in range(1,rank+1)]
    b=modes[0][2]
    if any(row[2]!=b for row in modes):raise ArithmeticError("prime source drift")
    hinge=b-F(1,2)
    if hinge.lo<=0 or hinge.hi>=F(1,2):raise ArithmeticError("wrong first-prime window")
    low=[m[0] for m in modes];high=[m[1] for m in modes]
    H=[[I.of(0) for _ in range(rank)] for _ in range(rank)]
    moments=[[I.of(0) for _ in range(rank)] for _ in range(4)]
    for i in range(rank):
        for j in range(i,rank):
            if (i-j)%2:continue
            v=(low[i]*low[j]).integrate(0,hinge,digits)+(high[i]*high[j]).integrate(hinge,F(1,2),digits)
            H[i][j]=H[j][i]=2*v
        for m in range(4):
            if (m-(i+1))%2:continue
            poly=ExponentialPolynomial.polynomial(L.legendre_polynomial(m,F(1,2)))
            moments[m][i]=2*((low[i]*poly).integrate(0,hinge,digits)+
                               (high[i]*poly).integrate(hinge,F(1,2),digits))
    projected=[[I.of(0) for _ in range(rank)] for _ in range(rank)]
    projection=[[I.of(0) for _ in range(rank)] for _ in range(rank)]
    for i in range(rank):
        for j in range(i,rank):
            if (i-j)%2:continue
            p=sum(((2*m+1)*moments[m][i]*moments[m][j] for m in range(4)),I.of(0))
            projection[i][j]=projection[j][i]=p
            projected[i][j]=projected[j][i]=H[i][j]-p
    return {
        "source":"PINNED_SUZUKI_FINITE_GAMMA_ANALYTIC_EXP_POLY",
        "genuine_prime2_hinge":hinge,
        "Hprime":tuple(tuple(row) for row in H),
        "moments":tuple(tuple(row) for row in moments),
        "polynomial_projection_gram":tuple(tuple(row) for row in projection),
        "quotient_gram":tuple(tuple(row) for row in projected),
        "contact_midpoint_only":True,
        "contact_source_rational_mid":(L._pinned_source().contact_iv().lo+
                                       L._pinned_source().contact_iv().hi)/2,
        "contact_source_rational_radius":(L._pinned_source().contact_iv().hi-
                                          L._pinned_source().contact_iv().lo)/2,
        "source_authenticated":True,"Gamma_J":J,"rank":rank,
        "spatial_quadrature_used":False,"RH_proved":False
    }
