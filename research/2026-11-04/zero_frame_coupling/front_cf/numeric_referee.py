"""Independent numerical diagnostic of four actual coupled source maxima.

Fixed integer common carrier, raw source taps, mpmath exponentials, convex
hull diameter. Does not import the rational certificate implementation.
This is corroborating numerical evidence, not a rigorous enclosure proof.
"""
from fractions import Fraction as Q
from math import lcm
from pathlib import Path
import hashlib
import json
import mpmath as mp


def integer_source(N):
    carrier=4
    for k in range(1,8*N+1):
        carrier=lcm(carrier,4*k)
    U=[0]
    Z=[0]
    # Literal eight-slot source, intentionally independent of maininstrument.
    original=(Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0))
    radial=(Q(2),Q(-2),Q(-1),Q(-2),-Q(1,2),-Q(1,2),Q(1,4),Q(0))
    for n in range(1,N+1):
        injections=[]
        for taps in (original,radial):
            total=0
            for j,c in enumerate(taps,1):
                denominator=c.denominator*(8*(n-1)+j)
                assert carrier % denominator==0
                total+=c.numerator*(carrier//denominator)
            injections.append(total)
        U.append((16*U[-1]+injections[0]) % carrier)
        Z.append((16*Z[-1]+injections[1]) % carrier)
    return carrier,U,Z


def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(points):
    ordered=sorted(points,key=lambda x:(x[0],x[1]))
    lower=[]
    for p in ordered:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(ordered):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


def number(text):
    value=Q(text)
    return mp.mpf(value.numerator)/value.denominator


def compute(A,h,lag,carrier,U,Z,dps):
    with mp.workdps(dps):
        H=abs(h)
        depth=0
        threshold=mp.mpf(A)**2*mp.log(A)
        while 16*H<=threshold:
            H*=16
            depth+=1
        H=H if h>0 else -H
        values=[]
        for n in range(A,2*A):
            phase=(H*(U[n]-Z[n]+Z[n+lag])) % carrier
            values.append(mp.exp(2j*mp.pi*(mp.mpf(phase)/carrier)))
        mean=mp.mpc(mp.fsum(x.real for x in values),mp.fsum(x.imag for x in values))/A
        prefix=mp.mpc(0)
        points=[(mp.mpf(0),mp.mpf(0),0)]
        for i,z in enumerate(values,1):
            prefix+=z
            points.append((prefix.real,prefix.imag,i))
        vertices=hull(points)
        maximum=mp.mpf(-1)
        witness=None
        for i,p in enumerate(vertices):
            for q in vertices[i+1:]:
                distance=(p[0]-q[0])**2+(p[1]-q[1])**2
                if distance>maximum:
                    maximum=distance
                    witness=sorted((p[2],q[2]))
        return {"A":A,"h":h,"lag":lag,"signed_H":H,"depth":depth,
                "M":mp.sqrt(maximum)/A,"mean":mean,"witness":witness,
                "hull_vertices":len(vertices),"precision_dps":dps}


def main():
    root=Path(__file__).resolve().parents[1]
    path=root/"FINITE_RECEIPT.json"
    content=path.read_bytes()
    receipt=json.loads(content)
    carrier,U,Z=integer_source(1025)
    rows=[]
    for A,h in ((256,7),(512,-3)):
        case=next(c for c in receipt["cases"] if c["A"]==A and c.get("h")==h)
        for lag in (0,1):
            target=next(c for c in case["factor_cells"]
                        if c["angular_orientation"]==1 and c["seed"]=="0"
                        and c["measure"]=="uniform" and c["lag"]==lag)
            low=compute(A,h,lag,carrier,U,Z,80)
            high=compute(A,h,lag,carrier,U,Z,110)
            with mp.workdps(110):
                assert high["signed_H"]==case["signed_H"]
                assert low["witness"]==high["witness"]==target["witness_offsets"]
                lower,upper=map(number,target["M_interval"])
                assert lower<=high["M"]<=upper
                center=mp.mpc(*(number(v) for v in target["signed_mean_grid"]))
                mean_error=abs(high["mean"]-center)
                assert mean_error<=number(target["complex_error"])
                precision_difference=max(abs(high["M"]-low["M"]),abs(high["mean"]-low["mean"]))
                assert precision_difference<mp.mpf("1e-70")
                rows.append({"A":A,"h":h,"lag":lag,"signed_H":high["signed_H"],
                             "depth":high["depth"],"M_numeric":mp.nstr(high["M"],70),
                             "mean_real_numeric":mp.nstr(high["mean"].real,70),
                             "mean_imag_numeric":mp.nstr(high["mean"].imag,70),
                             "witness_offsets":high["witness"],"hull_vertices":high["hull_vertices"],
                             "M_inside_certificate":True,"mean_inside_certificate":True,
                             "mean_error_from_grid":mp.nstr(mean_error,12),
                             "precision_80_vs_110_difference":mp.nstr(precision_difference,12)})
    print(json.dumps({"authority":"independent numerical diagnostic only; not a rational proof",
                      "method":"literal raw taps, common integer carrier, mpmath, convex hull diameter",
                      "receipt_sha256":hashlib.sha256(content).hexdigest(),"rows":rows},indent=2,sort_keys=True))


if __name__=="__main__":
    main()
