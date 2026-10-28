"""Exact refinements; universal proofs live in the referee dossier.

These functions compute necessary bounds, not cover decisions. Existing
classical exact-value code is deliberately not imported by the unit witness.
"""
from fractions import Fraction as F
from math import gcd


def _integer(x):
    if type(x) is not int:
        raise TypeError('an exact integer excluding bool is required')


def short_unit_set(r):
    """At most four explicit units with controlled cyclic gaps."""
    _integer(r)
    if r < 1:
        raise ValueError('positive modulus required')
    if r <= 2:
        return (1 % r,)
    if r % 2:
        q = r // 2
        units = (1, q, q+1, r-1)
    elif r % 4 == 0:
        units = (1, r//2-1, r//2+1, r-1)
    else:
        units = (1, r//2-2, r//2+2, r-1)
    return tuple(sorted(set(units)))


def short_coprime_denominator(n, r):
    """First representative >=n+r of the explicit unit subset; no gcd scan."""
    for x in (n, r):
        _integer(x)
    if n < 5 or not 1 <= r <= (n-1)//2:
        raise ValueError('require n>=5 and a lower-half deletion')
    start = n+r
    return min(a + ((start-a+r-1)//r)*r for a in short_unit_set(r))


def inverse_time(n, r):
    d = short_coprime_denominator(n,r)
    if gcd(d,r) != 1:
        raise ArithmeticError('unit construction failed')
    return F(pow(r,-1,d),d), F(2,d)


def refined_bounds(n, r1, r2):
    """Pair bounds from independently proved height, density and two bands."""
    for x in (n,r1,r2):
        _integer(x)
    if n < 5 or not 1 <= r1 < r2 < n:
        raise ValueError('require n>=5 and two distinct baseline deletions')
    from observational_succ.lonely_runner_deletion import exact_deletion_value
    retained_max = max(i for i in range(1,n) if i not in (r1,r2))
    mu = max(exact_deletion_value(n,r1),exact_deletion_value(n,r2))
    length = 2*(mu-F(1,n))/retained_max
    density = F(4*(n-2),n*(n-4))/length
    geometry = F(6,n)/length
    strict = min(density,geometry)
    return {'height':mu,'safe_length':length,'retained_max':retained_max,
            'density_bound':density,'two_band_bound':geometry,
            'first_strict_bound':strict,
            'first_integer_max':(strict.numerator-1)//strict.denominator,
            'second_multiplier':2*retained_max}


def endpoint_spacing(n, u, v):
    """Arithmetic lower bound for right-u/left-v gap endpoints.

For u!=v the positive numerator is g times an integer congruent to
-(u/g+v/g) modulo n. For u=v consecutive bands give (n-2)/(n*v).
Existence of an actual residual component is a separate premise.
"""
    for x in (n,u,v):
        _integer(x)
    if n < 3 or min(u,v) < 1:
        raise ValueError('require n>=3 and positive velocities')
    if u == v:
        return F(n-2,n*v)
    g = gcd(u,v)
    residue = (-(u//g+v//g)) % n or n
    return F(g*residue,n*u*v)


def phase_unit(r, w):
    """Exact unit lift with ||w*p/r||>=1/6; theorem in referee/GAMMA_AUDIT.md."""
    for x in (r,w):
        _integer(x)
    if r<2 or w<1 or w%r==0:
        raise ValueError('positive nonmultiple velocity and modulus>=2 required')
    g=gcd(r,w); q=r//g
    if q==2:a=1
    elif q%2:a=(q-1)//2
    elif q%4==0:a=q//2-1
    else:a=q//2-2
    target=(a*pow(w//g,-1,q))%q
    # Finite CRT lift. Termination follows from unit-surjectivity, proved
    # independently in the dossier; no primality heuristic is used.
    p=next(p for p in range(target,r,q) if gcd(p,r)==1)
    return p


def upper_half_gap(n, r, s, w):
    """Actual open gap after one insertion, retaining rational endpoint labels.

    n>=7 is required for the uniform nonmultiple phase margin. The shared
    multiple branch remains meaningful for n5/6 but is not exposed here.
    """
    for x in (n,r,s,w):_integer(x)
    if n<7 or not n-1<2*r<2*s<=2*(n-1) or w<n:
        raise ValueError('require n>=7, upper-half pair and inserted w>=n')
    for a in (r,s):
        if w%a:
            p=phase_unit(a,w); center=F(p,a)
            radius=min(F(n-a,n*a*(n-1)),F(n-6,6*n*w))
            return {'branch':'unit phase','deleted':a,'unit':p,
                    'left':center-radius,'right':center+radius,
                    'second_bound':max(F(a*(n-1),n-a),F(6*w,n-6))}
    center=F(1,r); radius=F(n-r,n*r*(n-1))
    left=center+F(1,n*w)
    right=center+min(radius,F(n-1,n*w))
    return {'branch':'common multiple','deleted':r,'unit':1,
            'left':left,'right':right,
            'second_bound':max(F(2*r*(n-1)),F(2*w,n-2)),
            'length_lower':min(F(1,n*r*(n-1)),F(n-2,n*w))}
