"""Exact finite Hilbert dual tower, residual innovations and ghost controls.

This module certifies finite rational Euclidean examples. The corresponding
infinite assertions are classical Hilbert theorems, NOT derived from finite tests.
"""
from fractions import Fraction as F
from .bidirectional_cut import CutSourceError, rat


def dot(x,y):
    if len(x)!=len(y):
        raise CutSourceError('finite Hilbert vectors require common dimension')
    return sum((a*b for a,b in zip(x,y)),F(0))


def vector(v):
    if type(v) is not tuple or not 1<=len(v)<=128:
        raise CutSourceError('finite tuple of 1..128 rational entries required')
    return tuple(rat(x) for x in v)


def subtract(x,y):
    return tuple(a-b for a,b in zip(x,y))


def scaled(k,x):
    return tuple(k*a for a in x)


def orthogonal_innovations(target,observations):
    """Construct exact orthonormal-free Gram-Schmidt innovations in given order.

    Returns d_n^2 for each finite observation span and delta_n. Degenerate
    observation vectors do not acquire phantom dimensions. Exact Pythagorean
    identity d_(n-1)^2-d_n^2=delta_n >=0, and sum delta+d_last=||h||^2.
    """
    h=vector(target)
    if type(observations) is not tuple or len(observations)>64:
        raise CutSourceError('finite typed observation list required')
    basis=[]
    innovations=[]
    energy=[]
    residual=dot(h,h)
    for candidate in observations:
        v=vector(candidate)
        if len(v)!=len(h):
            raise CutSourceError('source observation dimension mismatch')
        w=v
        for b in basis:
            w=subtract(w,scaled(dot(w,b)/dot(b,b),b))
        ww=dot(w,w)
        if ww:
            basis.append(w)
            delta=dot(h,w)**2/ww
        else:
            delta=F(0)
        residual-=delta
        if residual<0:
            raise AssertionError('exact rational Pythagorean residual became negative')
        innovations.append(delta)
        energy.append(residual)
    if sum(innovations,F(0))+residual !=dot(h,h):
        raise AssertionError('telescoping identity not exact')
    return {'norm_sq':dot(h,h),'innovation_energies':tuple(innovations),
            'residual_sq':tuple(energy),'surviving':residual,
            'finite_shadow_not_global_criterion':True,'RH_proved':False}


def compatible_functionals_square_norm(coordinates):
    """ONB finite coordinates give exact squared norm growth of a compatible dual.

    Compatible prefixes do not imply a continuous functional on the infinite
    Hilbert closure. Uniform boundedness of these squared norms is necessary
    and sufficient (Riesz representation/Parseval), in this ONB model.
    """
    cs=vector(coordinates)
    totals=[]
    sq=F(0)
    for a in cs:
        sq+=a*a
        totals.append(sq)
    return tuple(totals)


def hidden_target_counterexample():
    """All forward readings zero although target h is nonzero.

    e_0 is orthogonal to all observations e_1, e_2, ... . Bounded,
    compatible zero readings can never certify target completeness.
    """
    target=(F(1),F(0),F(0),F(0),F(0))
    observations=tuple(tuple(F(int(i==j)) for i in range(5))
                       for j in range(1,5))
    result=orthogonal_innovations(target,observations)
    if result['surviving']!=1 or any(result['innovation_energies']):
        raise AssertionError('ghost target did not survive')
    return result
