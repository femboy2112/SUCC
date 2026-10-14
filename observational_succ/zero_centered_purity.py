"""Exact rational projection of the normalized Archimedean dilation range.

U_q f(x)=sqrt(q)f(qx) with zero extension on L²(0,1) is a pure isometry,
not unitary. U_q* has no nonzero unit-modulus eigenvectors.
All finite checks are source-first and use exact rational cell weights.
"""
from fractions import Fraction as Q


class PurityError(ValueError):
    pass


def _valid(q, nmax=100000):
    if type(q) is not int or not 2 <= q <= nmax:
        raise PurityError("dilation must be a bounded integer q>=2")
    return q


def w(k):
    if type(k) is not int or k < 1:
        raise PurityError("positive integer cell required")
    return Q(1,k*(k+1))


def check(f):
    if not isinstance(f,dict) or any(type(k) is not int or k<1 or
                                      type(v) not in (int,Q) for k,v in f.items()):
        raise PurityError("finite rational cell map required")
    if len(f)>100000 or (f and max(f)>100000):
        raise PurityError("finite cell budget exceeded")
    return f


def inner(a,b):
    check(a);check(b)
    return sum((w(k)*Q(x)*Q(b.get(k,0)) for k,x in a.items()),Q())


def norm2(f):
    return inner(f,f)


def range_projection(f,q):
    """U_q U_q* projects onto q-cell block-constant functions (zero for k<q).

    The normalization cancels: each block is replaced by its w-weighted
    average, using the exact telescoping cell weight w_j/q.
    """
    check(f);_valid(q)
    if not f:
        return {}
    result={}
    for j in range(1,max(f)//q+1):
        numerator=sum((w(k)*Q(f.get(k,0))
                       for k in range(q*j,q*(j+1))),Q())
        avg=q*numerator/w(j)
        if avg:
            for k in range(q*j,q*(j+1)):
                result[k]=avg
    if result and max(result)>100000:
        raise PurityError("projection exceeds cell budget")
    return result


def escape_receipt(f,q,n):
    """Exact finite witness of purity once q**n exceeds observed support."""
    check(f);_valid(q)
    if type(n) is not int or not 1<=n<=50:
        raise PurityError("bounded positive horizon required")
    Qn=q**n
    if Qn<=100000:
        escaped=not range_projection(f,Qn)
    else:
        escaped=not f or Qn>max(f)
    return {"q":q,"n":n,"first_possible_image_cell":Qn,
            "every_finite_source_cell_escaped":escaped,
            "no_bounded_unit_circle_eigenvector":"THEOREM_from_purity_not_finite_test",
            "zero_positions_used":False,"RH_proved":False}
