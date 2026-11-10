"""Exact finite equal-weight moment codecs; no asymptotic claims.

Gaussian rationals are (real, imaginary) Fraction pairs. This research adapter
adds no competing SUCC category hierarchy and changes no source module.
"""
from fractions import Fraction as Q

ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def neg(a):
    return (-a[0], -a[1])


def sub(a, b):
    return add(a, neg(b))


def scale(a, c):
    c=Q(c)
    return (a[0]*c, a[1]*c)


def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def conjugate(a):
    return (a[0], -a[1])


def norm2(a):
    return a[0]*a[0]+a[1]*a[1]


def div(a, b):
    denominator=norm2(b)
    if not denominator:
        raise ZeroDivisionError('moment codec is singular at the antipodal mean')
    return scale(mul(a,conjugate(b)),1/denominator)


def power(a, n):
    if type(n) is not int or n<0:
        raise ValueError('nonnegative integer power required')
    result=ONE
    while n:
        if n&1: result=mul(result,a)
        a=mul(a,a);n//=2
    return result


def mean(values):
    values=tuple(values)
    if not values: raise ValueError('nonempty values required')
    out=ZERO
    for value in values:out=add(out,value)
    return scale(out,Q(1,len(values)))


def unit(t):
    """Rational parametrization of the unit circle, not a phase evaluator."""
    t=Q(t)
    return ((1-t*t)/(1+t*t),2*t/(1+t*t))


def moments(atoms, last):
    if not atoms:raise ValueError('nonempty atoms required')
    if any(norm2(a)!=1 for a in atoms):raise ValueError('unit atoms required')
    return tuple(mean(power(z,k) for z in atoms) for k in range(last+1))


def newton_coefficients(prefix):
    """Return e0..eq from precisely q normalized moments M1..Mq."""
    q=len(prefix)
    if not q:raise ValueError('positive known replica count required')
    e=[ONE]
    for k in range(1,q+1):
        total=ZERO
        for i in range(1,k+1):
            total=add(total,scale(mul(e[k-i],prefix[i-1]),q*(-1)**(i-1)))
        e.append(scale(total,Q(1,k)))
    return tuple(e)


def reconstruct_moments(prefix,last):
    q=len(prefix)
    if last<q:raise ValueError('last must include the supplied prefix')
    coeff=newton_coefficients(prefix)
    result=[ONE,*prefix]
    for k in range(q+1,last+1):
        total=ZERO
        for i in range(1,q+1):
            total=add(total,scale(mul(coeff[i],result[k-i]),(-1)**(i-1)))
        result.append(total)
    return tuple(result)


def even_half_coefficients(prefix):
    """Recover all e_k for q=2*len(prefix) unit atoms if middle e_d!=0."""
    d=len(prefix);q=2*d
    if not d:raise ValueError('positive even replica count required')
    e=[ONE]
    for k in range(1,d+1):
        total=ZERO
        for i in range(1,k+1):
            total=add(total,scale(mul(e[k-i],prefix[i-1]),q*(-1)**(i-1)))
        e.append(scale(total,Q(1,k)))
    product=div(e[d],conjugate(e[d]))
    for k in range(d+1,q+1):
        e.append(mul(product,conjugate(e[q-k])))
    return tuple(e)


def pair_moment_from_mean(s,k):
    """Exact q=2 closure; rejects the genuine singularity s=0."""
    product=div(s,conjugate(s))
    return pair_moment(s,product,k)


def pair_moment(s,product,k):
    if type(k) is not int or k<0:raise ValueError('nonnegative order required')
    if k==0:return ONE
    previous,current=ONE,s
    for _ in range(2,k+1):
        previous,current=current,sub(scale(mul(s,current),2),mul(product,previous))
    return current


def chronology_predictions(z,w,factor_f,factor_g):
    """Two possible next means and their exact minimax center/radius squared."""
    z16,w16=power(z,16),power(w,16)
    plus=scale(add(mul(z16,factor_f),mul(w16,factor_g)),Q(1,2))
    minus=scale(add(mul(w16,factor_f),mul(z16,factor_g)),Q(1,2))
    center=scale(add(plus,minus),Q(1,2))
    radius2=norm2(scale(sub(plus,minus),Q(1,2)))
    return plus,minus,center,radius2


def forcing_difference_bound(n,m):
    if type(n) is not int or n<1 or type(m) is not int or m<1:
        raise ValueError('positive integers required')
    return Q(240*m,(8*n-7)*(8*n-6)*(8*n-5))
