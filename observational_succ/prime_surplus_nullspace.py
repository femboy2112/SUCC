"""Exact prime edge kernel: arithmetic surplus is directional, not scalar.

For b in (a,2a), f=phi + T_b(phi) with phi supported strictly in the
left edge satisfies center=0 and right=T_b left, hence M_b(f)=0.
Four ordinary polynomial moments impose only four linear constraints on
the infinite-dimensional smooth left-edge test class. Therefore there are
infinitely many nonzero smooth high-moment-null functions in ker M_b.

This kills any claim M_b >= eps * ||f||² on the whole legitimate high
test space, even though source-specific P5/P6 directions have strong gains.

This module supplies independent exact rational five-left-cell witnesses.
They are mathematical finite MODELS (piecewise constants, not smooth);
the full smooth theorem uses the finite-codimension kernel argument.
"""
from __future__ import annotations
from fractions import Fraction as F

from .authentic_prime_surplus import require_2edge,poly_int


class PrimeKernelError(ValueError):
    pass


def exact_finite_four_moment_edge_kernel(a=F(1,2),b=F(7,10),cells=5):
    """Solve four exact global moments on paired left/right source cells.

    A source interval proof is required before substituting irrational log2;
    this exact rational model calibrates the universal linear-algebra theorem.
    """
    a,b=require_2edge(a,b)
    if type(cells) is not int or not 5<=cells<=32:
        raise PrimeKernelError("at least 5 independently weighted paired cells")
    left_start=-a
    width=(2*a-b)/cells
    segments=tuple((left_start+i*width,left_start+(i+1)*width)
                   for i in range(cells))
    matrix=tuple(tuple(
        (right**(degree+1)-left**(degree+1)+
         (right+b)**(degree+1)-(left+b)**(degree+1))/F(degree+1)
        for left,right in segments
    ) for degree in range(4))
    # Exact rational Gaussian nullspace pivoting.
    rows=[list(line) for line in matrix]
    pivotcols=[]
    row=0
    for col in range(cells):
        pivot=next((i for i in range(row,4) if rows[i][col]),None)
        if pivot is None:continue
        rows[row],rows[pivot]=rows[pivot],rows[row]
        d=rows[row][col]
        rows[row]=[x/d for x in rows[row]]
        for i in range(4):
            if i!=row:
                t=rows[i][col]
                if t:rows[i]=[v-t*w for v,w in zip(rows[i],rows[row])]
        pivotcols.append(col)
        row+=1
        if row==4:break
    free=next((j for j in range(cells) if j not in pivotcols),None)
    if free is None:raise ArithmeticError("four moments falsely determine all five cells")
    x=[F(0)]*cells
    x[free]=F(1)
    for i,pivot in reversed(list(enumerate(pivotcols))):
        x[pivot]=-sum((rows[i][j]*x[j] for j in range(pivot+1,cells)),F(0))
    x=tuple(x)
    residuals=tuple(sum((m*v for m,v in zip(row,x)),F(0)) for row in matrix)
    if any(residuals):raise ArithmeticError("fake moment-null high witness")
    norm=2*width*sum((v*v for v in x),F(0))
    if norm<=0:raise ArithmeticError("nullvector must be nonzero")
    return {
        "a":a,"b":b,"left_segments":segments,"right_segments":
            tuple((l+b,r+b) for l,r in segments),
        "left_amplitudes":x,"right_amplitudes":x,
        "four_exact_moments":residuals,
        "prime_shift_center_mass":F(0),
        "prime_shift_mismatch_mass":F(0),
        "prime_edge_surplus":F(0),
        "whole_primitive_norm2":norm,
        "source_type":"FINITE_PIECEWISE_CONSTANT_COUNTERMODEL_NOT_GENUINE_WEIL_SOURCE",
        "smooth_all_high_kernel_theorem":"PAPER: finite-codimension kernel of C_c^infty(left edge)",
        "full_high_uniform_scalar_gain":False,
        "RH_proved":False,
    }


def source_prime_kernel_no_uniform_gap():
    """Actual frozen b=log2 theorem, without inventing computable phi.

    For any N>4 choose N independent smooth left-edge test bumps;
    the four genuine moment functionals on phi+T_b phi have rank <=4;
    a nonzero linear combination survives and is exact phase-locked.
    Infinite arbitrary N means infinite-dimensional kernel.
    """
    from .authentic_prime_surplus import original_prime_surplus_source_passport
    src=original_prime_surplus_source_passport()
    if not (F(1,2)<src["log2_interval"][0]<src["log2_interval"][1]<F(1)):
        raise PrimeKernelError("authentic two-edge original b window missing")
    return {
        "source_sha":src["source_sha"],
        "real_prime_shift":"log(2)",
        "high_polynomial_constraints":4,
        "independent_smooth_bumps":5,
        "nonzero_smooth_moment_null_shift_coherent_source_test_exists":True,
        "infinite_dimensional_nullspace":True,
        "source_prime_surplus_uniform_positive_scalar":False,
        "legendre_P5_which_has_positive_source_surplus_is_not_counterexample":True,
        "RH_proved":False,
    }
