"""Independently implemented rational prefix and Machin-pi calibrations.

This program does not import selected_boundary.py, and numerical runs do not
validate the unbounded irrationality-exponent theorem.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from json import dumps
from math import pi,cos


def source_direct(k):
    s=Q(0)
    for j in range(1,k+1):
        r=Q(4,8*j-7)-Q(2,8*j-4)-Q(1,8*j-3)-Q(1,8*j-2)
        s+=Q(16**(k-j))*r
    return s


def truncated_arctan(x,terms):
    s=Q(0)
    for j in range(terms):
        s+=Q((-1)**j,(2*j+1)*x**(2*j+1))
    return s


def machin_pi_interval():
    # arctan(x) alternating: even truncation lower, odd truncation upper.
    lo=16*truncated_arctan(5,220)-4*truncated_arctan(239,65)
    hi=16*truncated_arctan(5,221)-4*truncated_arctan(239,64)
    assert lo<hi
    return lo,hi


def frac(x): return x-(x.numerator//x.denominator)


def direct_lag_dist(n,h):
    t=Q(h)*(source_direct(n+1)-source_direct(n))
    f=frac(t)
    return min(f,1-f)


def boundary_check(n,lo,hi):
    u=source_direct(n)
    # Source identity 16^(n-1)pi=U_n+T_n, 0<T_n<(8n+1)^-2.
    low=16**(n-1)*lo-u
    high=16**(n-1)*hi-u
    assert low>0,(n,'bad Green lower')
    assert high<Q(1,(8*n+1)**2),(n,'bad Green upper')
    return low,high


def run():
    lo,hi=machin_pi_interval()
    assert Q(3141592653589793,10**15)<lo<hi<Q(3141592653589794,10**15)
    points=[1,2,5,10,17,31,59,89,127]
    for n in points: boundary_check(n,lo,hi)
    rows=[]
    for h in [1,3,7]:
        for A in [4,8,16,32,64]:
            # no numerical phase fitting: exact Fraction comparison to rational 1/20.
            first=next((n for n in range(A,8*A)
                        if direct_lag_dist(n,h)>=Q(1,20)),None)
            assert first is not None
            rows.append({'h':h,'A':A,'first_slip':first,'within_range':True})
    results={'oracle':'independent direct-prefix Fractions + Machin rational pi interval',
       'machin_pi_interval_width_log10_approx':len(str((hi-lo).denominator))-len(str((hi-lo).numerator))-1,
       'green_verified_indices':points,
       'slip_rows':rows,'rows_passed':len(rows),
       'scope':'finite calibration; no asymptotic claims'}
    print(dumps(results,indent=2))
    return results

if __name__=='__main__':run()
