"""Source-first reciprocal-cell dilation and half-density Mellin covariance.

Zero-extended x->q*x induces (D_q f)(k)=f(floor(k/q)) for k>=q,
and zero for k<q. With w_k=1/[k(k+1)], sqrt(q)*D_q is an
isometry but NOT a surjective unitary. Critical-line Mellin characters
do not imply any zeta zero. All calculations here are exact rational.
"""
from __future__ import annotations
from fractions import Fraction as Q


class DilationError(ValueError):
    pass


def _integer(x,lo=1,hi=100_000):
    if type(x) is not int or not lo<=x<=hi:
        raise DilationError("invalid bounded integer")
    return x


def cell_weight(k:int)->Q:
    _integer(k)
    return Q(1,k*(k+1))


def mellin_weight(s:int,k:int)->Q:
    _integer(s,1,16)
    _integer(k)
    return (Q(1,k)**s-Q(1,k+1)**s)/s


def dilated_cell_index(q:int,k:int)->int:
    _integer(q,2)
    _integer(k)
    return k//q   # index 0 is zero extension outside (0,1)


def arch_dilate(values:dict[int,Q],q:int)->dict[int,Q]:
    """An exact finite cell sequence under x->q*x (zero extension)."""
    _integer(q,2)
    if not values or any(type(k) is not int or k<1 or
                         type(v) not in (int,Q) for k,v in values.items()):
        raise DilationError("nonempty finite exact rational source required")
    if q*(max(values)+1)>100_000:
        raise DilationError("dilated support exceeds budget")
    return {k:Q(values.get(k//q,0))
            for k in range(q,q*(max(values)+1))
            if values.get(k//q,0)}


def weighted_norm2(values:dict[int,Q])->Q:
    return sum((Q(v)**2*cell_weight(k) for k,v in values.items()),Q())


def integer_mellin(values:dict[int,Q],s:int)->Q:
    return sum((Q(v)*mellin_weight(s,k) for k,v in values.items()),Q())


def block_certificate(q:int,j:int,s:int)->dict:
    """Telescoping gives block measure w_j/q and Mellin moment m_s(j)/q^s."""
    _integer(q,2)
    _integer(j)
    _integer(s,1,16)
    if q*(j+1)>100_000:
        raise DilationError("block exceeds budget")
    w=sum((cell_weight(k) for k in range(q*j,q*(j+1))),Q())
    m=sum((mellin_weight(s,k) for k in range(q*j,q*(j+1))),Q())
    if w!=cell_weight(j)/q or m!=mellin_weight(s,j)/q**s:
        raise ArithmeticError("exact block telescope failed")
    return {"q":q,"j":j,"s":s,"block_weight":str(w),
            "block_mellin":str(m),"exact":True,"RH_proved":False}


def finite_dilation_receipt(values:dict[int,Q],q:int,s:int)->dict:
    d=arch_dilate(values,q)
    norm=weighted_norm2(values)
    moment=integer_mellin(values,s)
    if weighted_norm2(d)!=norm/q or integer_mellin(d,s)!=moment/q**s:
        raise ArithmeticError("norm or Mellin covariance failed")
    return {"q":q,"s":s,"norm_before":str(norm),
            "norm_after":str(weighted_norm2(d)),
            "mellin_before":str(moment),
            "mellin_after":str(integer_mellin(d,s)),
            "normalized_dilation_isometry_exact":True,
            "Mellin_covariance_exact":True,
            "isometry_is_surjective":False,
            "critical_line_alone_forces_zeros":False,
            "nontrivial_zero_positions_used":False,"RH_proved":False}
