"""Independent exact conditional-algebra and Fourier-calibration oracle.

No floating point, numerical special functions, or inherited interval engine.
Machin's identity and alternating Taylor sums give rational enclosures.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import unittest

Z = tuple[F, F]
ZERO: Z = (F(0), F(0))
ONE: Z = (F(1), F(0))
ROOTS: tuple[Z, ...] = (ONE, (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1)))


def add(a: Z, b: Z) -> Z:
    return (a[0]+b[0], a[1]+b[1])


def sub(a: Z, b: Z) -> Z:
    return (a[0]-b[0], a[1]-b[1])


def mul(a: Z, b: Z) -> Z:
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def conj(a: Z) -> Z:
    return (a[0], -a[1])


def mean(xs: list[Z] | tuple[Z, ...]) -> Z:
    return (sum((x[0] for x in xs), F())/len(xs),
            sum((x[1] for x in xs), F())/len(xs))


def project(xs: list[Z] | tuple[Z, ...], labels: list[int]) -> list[Z]:
    values = {j: mean([x for x,k in zip(xs,labels) if k == j]) for j in set(labels)}
    return [values[j] for j in labels]


def residual(a: list[Z] | tuple[Z, ...], b: list[Z] | tuple[Z, ...], labels: list[int]) -> Z:
    pa,pb = project(a,labels),project(b,labels)
    return mean([mul(sub(x,px),sub(y,py)) for x,px,y,py in zip(a,pa,b,pb)])


def atan_bounds(q: F, count: int) -> tuple[F,F]:
    assert 0 < q < 1 and count >= 1
    partial = sum(((-1)**j*q**(2*j+1)/(2*j+1) for j in range(count)),F())
    next_sum = partial + (-1)**count*q**(2*count+1)/(2*count+1)
    return min(partial,next_sum),max(partial,next_sum)


def pi_bounds() -> tuple[F,F]:
    a,b=atan_bounds(F(1,5),80)
    c,d=atan_bounds(F(1,239),24)
    low,high=16*a-4*d,16*b-4*c
    scale=10**60
    return F((low*scale).__floor__(),scale),F((high*scale).__ceil__(),scale)


def sine_bounds(x: tuple[F,F]) -> tuple[F,F]:
    low,high=x
    assert 0 <= low <= high < F(22,7)
    # The alternating terms decrease from index 1; cutoffs here exceed 1.
    def polynomial(last: int) -> tuple[F,F]:
        lo=hi=F()
        fac=1
        for j in range(last+1):
            if j:
                fac *= (2*j)*(2*j+1)
            l,u=low**(2*j+1)/fac,high**(2*j+1)/fac
            if j%2:
                lo-=u;hi-=l
            else:
                lo+=l;hi+=u
        return lo,hi
    return polynomial(27)[0],polynomial(26)[1]


def sinc_bounds(n: int, d: int) -> tuple[F,F]:
    assert 0 < n < d
    plo,phi=pi_bounds()
    lo,hi=plo*n/d,phi*n/d
    sl,sh=sine_bounds((lo,hi))
    scale=10**50
    return F((sl/hi*scale).__floor__(),scale), F((sh/lo*scale).__ceil__(),scale)


def calibration() -> dict:
    rows=[]
    plo,phi=pi_bounds()
    for h in (1,2,3,5):
        for d in range(1,7):
            m=16**d
            sl,sh=sinc_bounds(h,m)
            coherent=(m*m*(1-sh*sh),m*m*(1-sl*sl))
            limit=(plo*plo*h*h/3,phi*phi*h*h/3)
            error=2*phi**4*h**4/(45*m*m)
            assert coherent[0] > 0
            assert coherent[0] >= limit[0]-error
            assert coherent[1] <= limit[1]
            # Alias MR = h/(1-h/M) sinc(pi h/M)^2, independently
            # checked against the product of the two separate sinc bounds.
            tl,th=sinc_bounds(m-h,m)
            alias=(m*sl*tl,m*sh*th)
            equivalent=(F(h*m,m-h)*sl*sl,F(h*m,m-h)*sh*sh)
            assert max(alias[0],equivalent[0]) <= min(alias[1],equivalent[1])
            alias_error=F(h*h,m-h)+F(h*m,m-h)*phi**2*h*h/(3*m*m)
            assert alias[0]>=h-alias_error and alias[1]<=h+alias_error
            rows.append({"h":h,"M":m,
                         "M_squared_coherent_residual":list(map(str,coherent)),
                         "coherent_limit":list(map(str,limit)),
                         "coherent_error_cap":str(error),
                         "M_alias_residual":list(map(str,alias)),
                         "alias_limit":h,"alias_error_cap":str(alias_error)})
    return {"method":"independent rational Machin/Taylor enclosures",
            "pi_interval":list(map(str,(plo,phi))),"rows":rows}


def finite_algebra() -> dict:
    cases=0
    partitions=([0,0,0,0],[0,0,1,1],[0,1,2,3])
    # Exhaust every 4-point root-of-unity pair. Covers both signed failures
    # and exact identities with no probabilistic or numerical tolerance.
    for a in itertools.product(ROOTS,repeat=4):
        for b in itertools.product(ROOTS,repeat=4):
            z=mean([mul(x,y) for x,y in zip(a,b)])
            rs=[]
            projections=[]
            for labels in partitions:
                pa,pb=project(a,list(labels)),project(b,list(labels))
                r=residual(a,b,list(labels))
                coarse=mean([mul(x,y) for x,y in zip(pa,pb)])
                assert add(coarse,r)==z
                projections.append((pa,pb));rs.append(r)
                cases+=1
            for j in range(2):
                pa,pb=projections[j];qa,qb=projections[j+1]
                increment=mean([mul(sub(x,px),sub(y,py)) for x,px,y,py in zip(qa,pa,qb,pb)])
                assert sub(rs[j],rs[j+1])==increment
                cases+=1
    a=list(ROOTS);b=[ROOTS[3],ROOTS[0],ROOTS[1],ROOTS[2]]
    r=[residual(a,b,list(p)) for p in partitions]
    assert r==[ZERO,(F(-1,2),F(0)),ZERO]
    # Gauge failure for a nonmeasurable phase, invariance of product.
    a=[ROOTS[0],ROOTS[2]];b=a;u=a
    transformed_a=[mul(v,x) for v,x in zip(u,a)]
    transformed_b=[mul(conj(v),x) for v,x in zip(u,b)]
    assert residual(a,b,[0,0])==ONE
    assert residual(transformed_a,transformed_b,[0,0])==ZERO
    assert [mul(x,y) for x,y in zip(a,b)]==[mul(x,y) for x,y in zip(transformed_a,transformed_b)]
    return {"finite_identity_checks":cases,
            "signed_refinement_residuals":[[str(x),str(y)] for x,y in r],
            "nonmeasurable_gauge_residual_before":["1","0"],
            "nonmeasurable_gauge_residual_after":["0","0"],
            "status":"exact algebra; model controls, not original BBP complement"}


class CrucibleTests(unittest.TestCase):
    def test_conditional_identity(self):
        a=list(ROOTS);b=[ROOTS[3],ROOTS[0],ROOTS[1],ROOTS[2]]
        self.assertEqual(residual(a,b,[0,0,1,1]),(F(-1,2),F(0)))

    def test_gauge_residual_changes(self):
        a=[ONE,(-F(1),F(0))]
        self.assertEqual(residual(a,a,[0,0]),ONE)
        self.assertEqual(residual([ONE,ONE],[ONE,ONE],[0,0]),ZERO)

    def test_machin_bounds(self):
        lo,hi=pi_bounds()
        self.assertTrue(F(314159265358979323846,10**20)<lo<hi<F(314159265358979323847,10**20))
        self.assertLess(hi-lo,F(1,10**59))

    def test_continuum_calibration(self):
        result=calibration()
        self.assertEqual(len(result["rows"]),24)


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result={"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "finite":finite_algebra(),"continuum":calibration()}
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"finite_checks":result["finite"]["finite_identity_checks"],
                      "continuum_rows":len(result["continuum"]["rows"]),"output":str(args.output)}))


if __name__=="__main__":
    main()
