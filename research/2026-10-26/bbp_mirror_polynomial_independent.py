#!/usr/bin/env python3
"""Independent exact audit of the reduced BBP kernel and binary packets.

Imports no SUCC production code. Finite checks calibrate the accompanying
all-domain paper proofs; they do not certify normality or an infinite limit.
"""
from fractions import Fraction as Q
from math import comb
import json
import sympy as sp


def source_r(n):
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def kernel(x):
    return (1-x)/((2-x*x)*(x*x-2*x+2))


def packet(x,j):
    u=x-x*x/2; v=x*x/2
    return ((2-x)*u**j-x*v**j)/8


def moment_packet(m,j):
    return (sum((comb(j,l)*Q(-1,2)**l*(Q(2,m+j+l+1)-Q(1,m+j+l+2))
                 for l in range(j+1)),Q())-Q(1,2**j*(m+2*j+2)))/8


def finite_moment(m,depth):
    return sum((moment_packet(m,j) for j in range(depth)),Q())


def polynomial_coefficients(depth):
    """Ascending exact rational coefficients of the globally defined R_M."""
    coefficients=[Q() for _ in range(2*depth)]
    for j in range(depth):
        for ell in range(j+1):
            value=comb(j,ell)*Q(-1,2)**ell
            coefficients[j+ell]+=value/4
            coefficients[j+ell+1]-=value/8
        coefficients[2*j+1]-=Q(1,8*2**j)
    while len(coefficients)>1 and coefficients[-1]==0:
        coefficients.pop()
    return tuple(coefficients)


def coefficient_moment(coefficients,m):
    return sum((value/Q(m+power+1) for power,value in enumerate(coefficients)),Q())


def green_interval(n,depth=40):
    lo=sum((source_r(n+j)/16**j for j in range(1,depth+1)),Q())
    return lo,lo+source_r(n+depth+1)/(15*16**depth)


def main():
    x=sp.symbols('x',real=True)
    A=2-x*x; B=x*x-2*x+2; R=(1-x)/(A*B)
    P=(1-x)*(x*x+2)*(x*x+2*x+2)
    J=2*(1-x)/(2-x)
    M=sp.Matrix([[-2,2],[-1,2]])
    simplify=sp.factor
    identities={
        'kernel_factorization':simplify(R-P/(16-x**8))==0,
        'mirror_involution':simplify(J.subs(x,J)-x)==0,
        'mirror_matrix_square_two':M*M==2*sp.eye(2),
        'mirror_A_covariance':simplify(A.subs(x,J)-2*A/(2-x)**2)==0,
        'mirror_B_covariance':simplify(B.subs(x,J)-2*B/(2-x)**2)==0,
        'mirror_density_sum':simplify(R-R.subs(x,J)*sp.diff(J,x)-1/(2*B))==0,
        'log_angle_derivative':simplify(16*R-2*sp.diff(sp.log(A/B),x)-4/B)==0,
        'log_max_square_identity':simplify(2*B*B-A*A-(x*x-4*x+2)**2)==0,
        'partial_fraction_atoms':simplify(R-((2-x)/(4*B)-x/(4*A)))==0,
    }
    assert all(identities.values())
    sampled_bounds=0
    mutations=[]
    for depth in (1,2,4,8,16):
        delta=Q(depth+2,2**(depth+1))
        for numerator in range(101):
            q=Q(numerator,100)
            lower=sum((packet(q,j) for j in range(depth)),Q())
            error=kernel(q)-lower
            assert lower>=0 and error>=0 and error<=delta*kernel(q)
            assert all(packet(q,j)>=0 for j in range(depth))
            sampled_bounds+=1
        q=Q(9999,10000)
        wrong_delta=Q(depth+1,2**(depth+1))
        error=kernel(q)-sum((packet(q,j) for j in range(depth)),Q())
        mutations.append(error>wrong_delta*kernel(q))
    assert all(mutations)
    polynomials={}
    for depth in (1,2,4,8,16,32):
        coefficients=polynomial_coefficients(depth)
        assert sum(coefficients,Q())==0
        polynomials[str(depth)]={'ascending_coefficients':[str(c) for c in coefficients],
                                 'degree':len(coefficients)-1,
                                 'relative_defect':str(Q(depth+2,2**(depth+1))),
                                 'tail_at_zero':str(coefficient_moment(coefficients,0))}
    moments=[]
    for n in (0,1,8,128):
        lo,hi=green_interval(n)
        for depth in (1,2,4,8,16,32):
            delta=Q(depth+2,2**(depth+1))
            approximant=finite_moment(8*n,depth)
            coefficients=polynomial_coefficients(depth)
            assert coefficient_moment(coefficients,8*n)==approximant
            assert 0<approximant<lo<hi<approximant/(1-delta)
            source_gate=True
            if n:
                source_approx=16*coefficient_moment(coefficients,8*(n-1))-approximant
                source_gate=(1-delta)*source_r(n)<=source_approx<=source_r(n)
                assert source_gate
            moments.append({'n':n,'depth':depth,'relative_error_bound':str(delta),
                            'exact_polynomial_moment':str(approximant),
                            'moment_upper':str(approximant/(1-delta)),
                            'forcing_relative_interval_checked_when_n_positive':source_gate,
                            'independent_green_interval_contained':True})
    print(json.dumps({'status':'EXACT FINITE CALIBRATION; ALL-DOMAIN PROOF IS SEPARATE',
                      'production_imports':[], 'symbolic_identities':identities,
                      'pointwise_grid_checks':sampled_bounds,
                      'too_small_tail_bound_mutations_rejected':mutations,
                      'finite_polynomial_compiler':polynomials,
                      'moment_interval_checks':moments,
                      'pi_normality_proved':False},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
