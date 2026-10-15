"""Exact Legendre matrix elements of authentic Suzuki g_J, without cell grids.

The algebra is rational; only original-source transcendental intervals are
imported from pinned PR85 source module. No zeta zeros, no invented covariance.
Every computed low entry retains prime-2 hinge, completed contact/poles,
and the first J POSITIVE authentic Gamma OU modes on mean-zero u.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb
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
    return source.iv(A)+B*source.exp_neg(2*alpha*a)


def authentic_gamma_low_entry(i,j,a,J):
    """Exactly the first J TRUE positive Gamma OU modes (not aux)."""
    integer(J,1,64)
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
    return source.log2_iv()*source.sqrt_inverse(2)*polynomial_interval(polynomial,b)


def source_low_entry_gamma_prime_contact(i,j,a=F(1,2),J=3):
    """Genuine Gamma J+prime+contact partial WITHOUT the pole part.

    This is an explicitly scoped partial operator; NEVER full Weil sign.
    The positive missing Gamma tail can be added by Loewner order.
    """
    i=integer(i,1,30);j=integer(j,1,30);a=q(a);integer(J,1,64)
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
    ep=source.exp_pos(a/2);em=source.exp_neg(a/2)
    def channels(k):
        p=legendre_polynomial(k,a)
        plus=exp_antiderivative_poly(p,F(1,2),+1)
        minus=exp_antiderivative_poly(p,F(1,2),-1)
        Eplus=ep*poly_eval(plus,a)-em*poly_eval(plus,-a)
        Eminus=em*poly_eval(minus,a)-ep*poly_eval(minus,-a)
        return (Eplus+Eminus)/2,(Eplus-Eminus)/2
    ci,si=channels(i);cj,sj=channels(j)
    return -8*ci*cj+8*si*sj


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
    rank=integer(rank,1,30);J=integer(J,1,36);a=q(a)
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
