"""Exact Legendre matrix elements of authentic Suzuki g_J, without cell grids.

The algebra is rational; only original-source transcendental intervals are
imported from pinned PR85 source module. No zeta zeros, no invented covariance.
Every computed low entry retains prime-2 hinge, completed contact/poles,
and the first J POSITIVE authentic Gamma OU modes on mean-zero u.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, factorial, isqrt
from hashlib import sha1
from pathlib import Path
from functools import lru_cache

from .suzuki_moment_schur import (
    SchurSourceError, integer, q, low_inverse_neumann, PARENT_SOURCE_BLOB,
)


def _pinned_source():
    """Fail closed unless the *exact* PR85 original-source module is present.

    No source value is constructed from an auxiliary bath, a fitted matrix, or
    an unpinned module. Keep this check even for symmetry-zero entries.
    """
    try:
        from . import source_weil_hierarchy as source
    except ImportError as exc:
        raise SchurSourceError('pinned parent #85 source module not mounted') from exc
    data=Path(source.__file__).read_bytes()
    digest=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if digest!=PARENT_SOURCE_BLOB:
        raise SchurSourceError('pinned parent #85 source module SHA drift')
    return source


def decimal_floor(x, digits):
    """Directed rational rounding to a declared decimal grid."""
    x=q(x)
    digits=integer(digits,10,350)
    S=10**digits
    return F(x.numerator*S//x.denominator,S)


def decimal_ceil(x,digits):
    return -decimal_floor(-q(x),digits)


def tight_exp_neg(x, digits=80):
    """Rigorous arbitrary-precision exp(-rational), no floating point.

    Positive Taylor for exp(y), geometric first-omitted bound, reciprocal,
    then repeated squaring with directed rounding. This upgrades the original
    PR85 32-decimal source primitive *without changing its mathematics*.
    """
    x=q(x);digits=integer(digits,20,300)
    if x<0 or x>256:raise SchurSourceError('positive exp(-x) source range')
    if not x:return F(1),F(1)
    y=x;m=0
    while y>F(1,2):y/=2;m+=1
    # Reserve logarithmically many digits for m outward-squaring operations.
    work=min(350,digits+max(8,m+3))
    # Each positive term is exact. Its next term times a geometric majorant
    # bounds the entire omitted tail while y<=1/2.
    term=F(1);e=F(1);n=0
    target=F(1,10**work)
    while True:
        n+=1
        term=term*y/n;e+=term
        nextterm=term*y/(n+1)
        rem=nextterm/(1-y/F(n+2))
        if rem<target:break
        if n>max(300,2*work):raise SchurSourceError('positive exponential tail budget')
    lo=decimal_floor(1/(e+rem),work)
    hi=decimal_ceil(1/e,work)
    for _ in range(m):
        lo=decimal_floor(lo*lo,work)
        hi=decimal_ceil(hi*hi,work)
    return decimal_floor(lo,digits),decimal_ceil(hi,digits)


def tight_log2(digits=80):
    """Rational enclosure 2 atanh(1/3) with positive geometric tail."""
    digits=integer(digits,20,300)
    z=F(1,3);term=z;total=F();j=0
    target=F(1,10**(digits+8))
    while True:
        total+=2*term/F(2*j+1)
        j+=1
        term*=z*z
        rem=2*term/(F(2*j+1)*(1-z*z))
        if rem<target:break
        if j>max(400,2*digits):raise SchurSourceError('log2 atanh tail budget')
    return decimal_floor(total,digits),decimal_ceil(total+rem,digits)


def interval_add(a,b):
    return a[0]+b[0],a[1]+b[1]


def interval_scale(a,x):
    x=q(x)
    return (a[0]*x,a[1]*x) if x>=0 else (a[1]*x,a[0]*x)


def interval_mul(a,b):
    v=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return min(v),max(v)


def interval_poly_eval(poly,rng):
    acc=(F(),F())
    for c in reversed(poly):
        acc=interval_add(interval_mul(acc,rng),(q(c),q(c)))
    return acc


def adaptive_precision_budget(coeff, guard=45):
    """Sufficient decimal digits to tame exact rational cancellation, not runtime lower bound."""
    coeff=q(coeff)
    guard=integer(guard,10,80)
    if not coeff:return guard
    # Integer log10 bound without floating arithmetic.
    size=max(abs(coeff.numerator)//coeff.denominator,1)
    dec=len(str(size))
    return min(300,max(60,dec+guard))


def source_interval_round(source,rng):
    return source.I(source.down(rng[0]),source.up(rng[1]))


def poly_add(a,b,scale=F(1)):
    scale=q(scale); n=max(len(a),len(b)); res=[F()]*n
    for i,x in enumerate(a):res[i]+=q(x)
    for i,x in enumerate(b):res[i]+=scale*q(x)
    while len(res)>1 and res[-1]==0:res.pop()
    return tuple(res)


def poly_scale(a,k):return tuple(q(k)*q(v) for v in a)


def poly_mul(a,b):
    ans=[F()]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=q(x)*q(y)
    return tuple(ans)


def poly_derivative(a):
    return tuple(a[i]*i for i in range(1,len(a))) or (F(),)


def poly_integral(a,l,r):
    l,r=q(l),q(r)
    return sum((x*(r**(i+1)-l**(i+1))/(i+1) for i,x in enumerate(a)),F())


def poly_eval(a,x):
    x=q(x);out=F()
    for c in reversed(a):out=out*x+c
    return out


def legendre_polynomial(n,a):
    n=integer(n,0,40);a=q(a)
    if a<=0:raise SchurSourceError('positive interval required')
    if n==0:return (F(1),)
    if n==1:return (F(),1/a)
    p=(F(1),);v=(F(),1/a)
    for k in range(1,n):
        p,v=v,poly_add(poly_scale(poly_mul(v,(F(),1/a)),F(2*k+1,k+1)),p,-F(k,k+1))
    return v


def poly_primitive_zero_at_left(poly,a):
    a=q(a)
    tmp=(F(),)+tuple(poly[i]/(i+1) for i in range(len(poly)))
    return poly_add(tmp,(-poly_eval(tmp,-a),))


def exp_antiderivative_poly(poly,alpha,sign):
    """F_(±) with d[e^(±αx)F_(±)]/dx = e^(±αx)*poly."""
    alpha=q(alpha);sign=integer(sign,-1,1)
    if alpha<=0 or sign not in (-1,1):raise SchurSourceError('positive alpha and ± sign')
    derivatives=tuple(q(v) for v in poly)
    acc=(F(),)
    for j in range(len(poly)):
        acc=poly_add(acc,derivatives,F((-1)**j,1)/(sign*alpha)**(j+1))
        derivatives=poly_derivative(derivatives)
    return acc


def source_ou_pair_affine(i,j,a,alpha):
    """EXACT rational (A,B) for ∫∫L_i(x)e^-α|x-y|L_j(y) dxdy.

    Value equals A + B*exp(-2 α a). No gamma, source or zero oracle.
    """
    i=integer(i,1,30);j=integer(j,1,30)
    a,alpha=q(a),q(alpha)
    if not 0<a<=1 or not alpha>0:raise SchurSourceError('positive genuine compact domain/alpha')
    if (i+j)%2:return F(),F()
    p=legendre_polynomial(i,a); v=legendre_polynomial(j,a)
    pp=exp_antiderivative_poly(p,alpha,+1)
    pm=exp_antiderivative_poly(p,alpha,-1)
    vp=exp_antiderivative_poly(v,alpha,+1)
    vm=exp_antiderivative_poly(v,alpha,-1)
    bulk=poly_integral(poly_mul(p,poly_add(vp,vm,-1)),-a,a)
    aa=bulk+poly_eval(vp,-a)*poly_eval(pm,-a)+poly_eval(vm,a)*poly_eval(pp,a)
    bb=-(poly_eval(vp,-a)*poly_eval(pm,a)+poly_eval(vm,a)*poly_eval(pp,-a))
    return aa,bb


def poly_two_variable_cross(i,j,a):
    """Exact ρ_ij(t)=∫_-a^(a-t)[L_i(y+t)L_j(y)+L_j(y+t)L_i(y)]dy.

    Result is rational polynomial for 0≤t≤2a. No source parameters.
    """
    i=integer(i,1,30);j=integer(j,1,30);a=q(a)
    if not 0<a<=1:raise SchurSourceError('positive halfwidth')
    if (i+j)%2:return (F(),)
    pi=legendre_polynomial(i,a);pj=legendre_polynomial(j,a)
    def cross(P,Q):
        # Result polynomial t, before/after integration in y.
        out=[F()]*(i+j+2)
        for k,pk in enumerate(P):
            if not pk:continue
            for l,ql in enumerate(Q):
                if not ql:continue
                for m in range(k+1):
                    coeff=pk*ql*comb(k,m)/F(k-m+l+1)
                    ypower=k-m+l+1
                    # ∫ y^(ypower-1) from -a to (a-t).
                    for h in range(ypower+1):
                        out[m+h]+=coeff*comb(ypower,h)*a**(ypower-h)*(-1)**h
                    out[m]-=coeff*(-a)**ypower
        return tuple(out)
    result=poly_add(cross(pi,pj),cross(pj,pi))
    return result


def prime_hinge_integral_polynomial(i,j,a):
    """Polynomial in b=log2 of ∫_b^(2a)(t-b)ρ_ij(t)dt, when b<2a."""
    i=integer(i,1,30);j=integer(j,1,30);a=q(a)
    rho=poly_two_variable_cross(i,j,a)
    L=2*a
    out=[F()]*(len(rho)+2)
    for k,r in enumerate(rho):
        if not r:continue
        out[0]+=r*L**(k+2)/F(k+2)
        out[1]-=r*L**(k+1)/F(k+1)
        out[k+2]+=r/F((k+1)*(k+2))
    return tuple(out)


def polynomial_interval(poly,interval):
    """Horner with authenticated parent interval type I."""
    source=_pinned_source()
    out=source.iv(0)
    for c in reversed(poly):out=out*interval+c
    return out


def source_ou_pair_interval(i,j,a,alpha):
    """Pinned source e^-αL interval applied to exact (A,B)."""
    source=_pinned_source()
    a,alpha=q(a),q(alpha)
    A,B=source_ou_pair_affine(i,j,a,alpha)
    digits=adaptive_precision_budget(B)
    exponential=tight_exp_neg(2*alpha*a,digits)
    rng=interval_add((A,A),interval_scale(exponential,B))
    return source_interval_round(source,rng)


def authentic_gamma_low_entry(i,j,a,J):
    """Exactly the first J TRUE positive Gamma OU modes (not aux)."""
    integer(J,1,75)
    source=_pinned_source()
    x=source.iv(0)
    for k in range(J):
        d=4*k+1
        x+=F(4,d*d)*source_ou_pair_interval(i,j,a,F(d,2))
    return x


def authentic_first_prime_low_entry(i,j,a=F(1,2)):
    """Only at first-prime window 0<a<=log3/2, with 2a>log2."""
    source=_pinned_source()
    a=q(a)
    if a!=F(1,2):
        raise SchurSourceError('exact certified first-prime a=1/2 only')
    b=source.log2_iv()
    if not b.hi<2*a:raise SchurSourceError('prime wavefront not source-verified')
    polynomial=prime_hinge_integral_polynomial(i,j,a)
    digits=adaptive_precision_budget(max(polynomial,key=abs))
    exact_log=tight_log2(digits)
    # Same source as the immutable original PR85 log2 enclosure, refined by a
    # separate positive rational series. Require exact interval consistency.
    if not (exact_log[0]<=b.hi and exact_log[1]>=b.lo):
        raise SchurSourceError('true prime-clock log2 source disagreement')
    poly_rng=interval_poly_eval(polynomial,exact_log)
    invsqrt2=source.sqrt_inverse(2)
    source_weight=interval_mul(exact_log,(invsqrt2.lo,invsqrt2.hi))
    return source_interval_round(source,interval_mul(source_weight,poly_rng))


def source_low_entry_gamma_prime_contact(i,j,a=F(1,2),J=3):
    """Genuine Gamma J+prime+contact partial WITHOUT the pole part.

    This is an explicitly scoped partial operator; NEVER full Weil sign.
    The positive missing Gamma tail can be added by Loewner order.
    """
    i=integer(i,1,30);j=integer(j,1,30);a=q(a);integer(J,1,75)
    source=_pinned_source()
    C=source.contact_iv()  # exact source: gamma + pi/2+3log2+logpi
    K=low_inverse_neumann(a,max(i,j))[i-1][j-1]
    return authentic_gamma_low_entry(i,j,a,J)-C*K+authentic_first_prime_low_entry(i,j,a)


def authentic_pole_low_entry(i,j,a=F(1,2)):
    """Original signed source pole operator in u=i v' coordinates:
       -8 <u_i,cosh(x/2)><cosh(x/2),u_j>
       +8 <u_i,sinh(x/2)><sinh(x/2),u_j>.
    No auxiliary Gaussian or deleted rank-one term.
    """
    i=integer(i,1,30);j=integer(j,1,30);a=q(a)
    source=_pinned_source()
    if (i+j)%2:return source.iv(0)
    # Polynomial exponential primitives can cancel >10^100 at degree 30:
    # evaluate all signed combinations in arbitrary-precision rationals and
    # round only the complete channel to the parent's proof interval.
    def channels(k):
        p=legendre_polynomial(k,a)
        plus=exp_antiderivative_poly(p,F(1,2),+1)
        minus=exp_antiderivative_poly(p,F(1,2),-1)
        xp=poly_eval(plus,a);xm=poly_eval(plus,-a)
        yp=poly_eval(minus,a);ym=poly_eval(minus,-a)
        digits=adaptive_precision_budget(max(map(abs,(xp,xm,yp,ym))))
        em=tight_exp_neg(a/2,digits)
        ep=(F(1)/em[1],F(1)/em[0])
        Eplus=interval_add(interval_scale(ep,xp),interval_scale(em,-xm))
        Eminus=interval_add(interval_scale(em,yp),interval_scale(ep,-ym))
        return interval_scale(interval_add(Eplus,Eminus),F(1,2)),interval_scale(interval_add(Eplus,interval_scale(Eminus,-1)),F(1,2))
    ci,si=channels(i);cj,sj=channels(j)
    pole=interval_add(interval_scale(interval_mul(ci,cj),-8),interval_scale(interval_mul(si,sj),8))
    return source_interval_round(source,pole)


def authentic_full_low_entry(i,j,a=F(1,2),J=3):
    """Exact-rational INTERVAL of actual signed Suzuki G_(a,J) on Legendre modes.

    Parent PR85 source only. Real 1-Gamma completion, pole +/- channels,
    contact and genuine n=2 first-prime hinge; no missing coefficients.
    Its omitted Gamma rungs are PSD, so G >= G_J as source operators.
    This is a true low Galerkin block, not a full Weil sign certificate.
    """
    if (i+j)%2:
        source=_pinned_source()
        return source.iv(0)
    return (source_low_entry_gamma_prime_contact(i,j,a,J)
            +authentic_pole_low_entry(i,j,a))


def authentic_direct_low_matrix(rank=3,J=3,a=F(1,2)):
    """Compute true source signed low block WITHOUT finite spatial cell grid.

    Runtime cost O(J*rank^2) exact rational+exp interval operations. At high
    rank, cancellations may make intervals broad; never silently turn them
    into sharp enclosures or assert positivity from a midpoint eigensystem.
    """
    rank=integer(rank,1,30);J=integer(J,1,75);a=q(a)
    if a!=F(1,2):raise SchurSourceError('a=1/2 genuine first-prime window')
    entries=[]
    for i in range(1,rank+1):
        row=[]
        for j in range(1,rank+1):
            row.append(authentic_full_low_entry(i,j,a,J))
        entries.append(tuple(row))
    for i in range(rank):
        for j in range(rank):
            if entries[i][j].lo!=entries[j][i].lo or entries[i][j].hi!=entries[j][i].hi:
                raise ArithmeticError('source signed low symmetry mismatch')
            if (i-j)%2 and (entries[i][j].lo!=0 or entries[i][j].hi!=0):
                raise ArithmeticError('source parity mismatch')
    return {'source':'AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3',
            'source_module_blob':PARENT_SOURCE_BLOB,
            'rank':rank,'J':J,'a':str(a),'interval_matrix':tuple(entries),
            'is_complete_source_after_gamma_J':True,
            'omitted_gamma_tail_positive':True,
            'is_exact_whole_Weil_form':False,
            'RH_proved':False}
