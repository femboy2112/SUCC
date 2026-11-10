"""Exact finite oracle for source-tail jets; no pi/Gamma source input.

The independent comparison uses the positive forcing series, not the Taylor
approximation under test. Asymptotic claims remain paper proofs.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path


def positive(n):
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")


def source(n):
    positive(n)
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def source_integral(n):
    positive(n)
    return sum((F(c,8*(n-1)+k+1)-F(c,8*(n-1)+k+2)
                for k,c in enumerate((4,4,4,2,1))),F())


def coefficients(order):
    if type(order) is not int or order < 0:
        raise ValueError("nonnegative integer order required")
    result=[1]
    for j in range(1,order+1):
        result.append(sum(c*result[j-k] for k,c in ((1,2),(3,2),(4,1))
                          if j>=k))
    return result


def coefficients_uncancelled(order):
    """Independent recurrence from Q(1+v)/(16-(1+v)^8)."""
    result=[]
    q=(4,4,4,2,1)
    for j in range(order+1):
        numerator=sum(q[k]*comb(k,j) for k in range(j,5))
        numerator+=sum(comb(8,k)*result[j-k] for k in range(1,min(8,j)+1))
        result.append(F(numerator,15))
    return result


def beta(n,k):
    positive(n)
    positive(k)
    denominator=1
    for j in range(k):
        denominator*=n+j
    return F(factorial(k-1),denominator)


def approximation(n,m):
    positive(n)
    if type(m) is not int or m < -1:
        raise ValueError("integer order at least -1 required")
    coeff=coefficients(m+1)
    value=sum(((-1)**j*coeff[j]*beta(8*n+1,j+2)
               for j in range(m+1)),F())
    bound=coeff[m+1]*beta(8*n+1,m+3)
    return value,bound


def tail_interval(n,depth=40):
    positive(n)
    positive(depth)
    lower=sum((source(n+j)/16**j for j in range(1,depth+1)),F())
    # For k>=2, source(k)<1/k^2 (also independently checked below).
    # sum_(j>depth)16^-j/(n+j)^2 <=16^-depth/[15(n+depth+1)^2].
    upper=lower+F(1,15*16**depth*(n+depth+1)**2)
    return lower,upper


def signed(interval,sign):
    return interval if sign==1 else (-interval[1],-interval[0])


def encode(q):
    return f"{q.numerator}/{q.denominator}"


def run():
    development=(1,2,7,19,53)
    holdouts=(101,257,521)
    lags=(1,2,7,13,31)
    coefficients_checked=coefficients(20)
    assert coefficients_checked==coefficients_uncancelled(20)
    source_checks=0
    for n in range(1,594):
        assert source(n)==source_integral(n)
        if n>=2:
            assert 0<source(n)<F(1,n*n)
        source_checks+=1
    point_checks=lag_checks=0
    records=[]
    for n in development+holdouts:
        t=tail_interval(n)
        for m in range(-1,6):
            approximation_n,bound=approximation(n,m)
            residual=signed((t[0]-approximation_n,t[1]-approximation_n),(-1)**(m+1))
            assert 0<residual[0]<=residual[1]<bound
            point_checks+=1
            row={"n":n,"order":m,"held_out":n in holdouts,
                 "bound":encode(bound),"scaled_lower":encode(residual[0]*n**(m+3)),
                 "scaled_upper":encode(residual[1]*n**(m+3)),"lags":[]}
            for ell in lags:
                later=tail_interval(n+ell)
                approximation_later,_=approximation(n+ell,m)
                gap=(t[0]-later[1]-approximation_n+approximation_later,
                     t[1]-later[0]-approximation_n+approximation_later)
                gap=signed(gap,(-1)**(m+1))
                lag_bound=8*ell*coefficients(m+1)[m+1]*beta(8*n+1,m+4)
                assert 0<gap[0]<=gap[1]<lag_bound
                lag_checks+=1
                row["lags"].append({"ell":ell,"bound":encode(lag_bound)})
            records.append(row)
    # Mutating the first pole adds sum16^-j/(8(n+j)-7) to T_n.
    mutation_checks=0
    for n in (19,101,521):
        original=tail_interval(n)
        mutated_lower=original[0]+sum((F(1,16**j*(8*(n+j)-7)) for j in range(1,41)),F())
        assert mutated_lower>F(1,64*n*n)
        mutation_checks+=1
    # Verify triangular signed-lag cost exactly, including H=1.
    triangle_checks=0
    for h in (1,2,3,7,16,37,101):
        actual=sum((F(2*(h-ell)*ell,h*h) for ell in range(1,h)),F())
        assert actual==F(h*h-1,3*h)
        triangle_checks+=1
    return {"status":"PASS", "authority":"Exact finite rational checks; infinite claims are paper-proved",
            "parent":"86327467191420d2157eeae5f4cfa1c2c62810da",
            "code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "coefficients":coefficients_checked,"source_checks":source_checks,
            "point_checks":point_checks,"lag_checks":lag_checks,
            "mutation_checks":mutation_checks,"triangle_checks":triangle_checks,
            "development":development,"holdouts":holdouts,"records":records}


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    result=run()
    payload=json.dumps(result,indent=2)+"\n"
    if args.output:
        args.output.write_text(payload)
    else:
        print(payload,end="")
