"""Finite rational certificates for stable Green source versus isometric circle time.

General impossibility of nonzero bounded source-to-Koopman intertwiners,
and of nonconstant continuous strongly-stable-to-expanding-circle
semiconjugacies, are proved on paper. Finite tests verify only scoped algebra.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import lcm

def _natural(n):
    if type(n) is not int or n<0:
        raise ValueError("nonnegative integer required")
    return n

def validated_permutation(indices):
    p=tuple(indices)
    if not p or any(type(x) is not int for x in p) or set(p)!=set(range(len(p))):
        raise ValueError("bijective finite target clock required")
    return p

def target_cycle_order(indices):
    p=validated_permutation(indices)
    visited=set();order=1
    for j in range(len(p)):
        if j in visited:
            continue
        cur=j;length=0
        while cur not in visited:
            visited.add(cur);length+=1;cur=p[cur]
        if cur!=j:
            raise ArithmeticError("invalid permutation cycle")
        order=lcm(order,length)
    return order

def finite_intertwiner_obstruction(source_spectrum,target_permutation):
    """P J=J diag(u_j), P^L=I, u_j<1 => (1-u_j^L)*column_j=0."""
    p=validated_permutation(target_permutation)
    u=tuple(Q(x) for x in source_spectrum)
    if not u or any(x<0 or x>=1 for x in u):
        raise ValueError("nonempty strict source spectrum in [0,1) required")
    length=target_cycle_order(p)
    factors=tuple(1-x**length for x in u)
    assert all(f>0 for f in factors)
    return length,factors

def finite_green_iterate_norm_squared(spectrum,vector,power):
    _natural(power)
    u=tuple(Q(v) for v in spectrum);f=tuple(Q(v) for v in vector)
    if not u or len(u)!=len(f) or any(v<0 or v>1 for v in u):
        raise ValueError("spectrum/vector dimension or bound mismatch")
    return sum(((v**power*x)**2 for v,x in zip(u,f)),Q())

def rational_circle_iterate(base,phase,n):
    _natural(n)
    if type(base) is not int or base<2:
        raise ValueError("base >=2 required")
    return (base**n*Q(phase))%1

def rational_orbit_eventually_fixed(base,phase,horizon):
    """Rational preperiodic check; genuine irrational pi is not a tool input."""
    _natural(horizon)
    if type(base) is not int or base<2:
        raise ValueError("base >=2 required")
    x=Q(phase)%1
    for n in range(horizon+1):
        if ((base-1)*base**n*x).denominator==1:
            return n
    return None

def finite_stable_source_vs_circle(base,contraction,phase,horizon):
    """Only a finite comparison; proves no asymptotic statistical statement."""
    if type(base) is not int or base<2 or type(horizon) is not int or horizon<1:
        raise ValueError("invalid base or horizon")
    lam=Q(contraction)
    if not 0<lam<1:
        raise ValueError("strictly decaying source required")
    return tuple((lam**n,rational_circle_iterate(base,phase,n))
                 for n in range(horizon))
