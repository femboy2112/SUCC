from fractions import Fraction as F
from math import isqrt
import json
import spectral_probe as s


def sqrt_upper(x):
    D=2**80
    return F(isqrt(x.numerator*D*D//x.denominator)+1,D)


def phase_sum_interval(values,A,N,k):
    bounds=[]
    for shift in (F(0),F(-1,4)):
        bs=[s.cos_interval(k*values[n]+shift) for n in range(A,A+N)]
        bounds.append((sum(x[0] for x in bs)/N,sum(x[1] for x in bs)/N))
    lower=F(0)
    upper=F(0)
    for a,b in bounds:
        lower+=0 if a<=0<=b else min(a*a,b*b)
        upper+=max(a*a,b*b)
    return lower,upper


u=s.orbit(750)
rows=[]
energies_below_one=[]
for A,N in ((61,127),(113,257),(229,509)):
    for k in (1,3,7):
        es={d:s.mean_energy_interval(u,A,N,k*s.m(d)) for d in range(1,5)}
        actual_sq=phase_sum_interval(u,A,N,k)
        for d,(lo,hi) in es.items():
            if hi<1:
                energies_below_one.append({"A":A,"N":N,"h":k*s.m(d),"upper":s.dump_fraction(hi),"upper_decimal":float(hi)})
        for J in (2,3,4,5):
            b=s.gram_transport_bound(u,A,N,k,J,es)
            bound=b['outside_boundary']+sqrt_upper(b['radicand_upper'])
            assert actual_sq[1]<=bound*bound
            rows.append({"A":A,"N":N,"k":k,"J":J,
                "mean_energy_intervals":{str(k*s.m(d)):[s.dump_fraction(t) for t in es[d]] for d in range(1,J)},
                "mean_energy_decimal":{str(k*s.m(d)):[float(t) for t in es[d]] for d in range(1,J)},
                "phase_mean_squared_interval":[s.dump_fraction(x) for x in actual_sq],
                "phase_mean_squared_decimal":[float(x) for x in actual_sq],
                "radicand_upper":s.dump_fraction(b['radicand_upper']),
                "signed_mean_upper":s.dump_fraction(bound),"signed_mean_upper_decimal":float(bound),
                "source_error_upper":s.dump_fraction(b['source_error']),
                "inside_boundary":s.dump_fraction(b['inside_boundary']),
                "outside_boundary":s.dump_fraction(b['outside_boundary'])})
        print(f"A={A},N={N},k={k}: 4 certified Gram rows; |mean|^2={float(actual_sq[1]):.9f}",flush=True)

out={"status":"CERTIFIED FINITE ONLY; no asymptotic inference",
     "source":[4,-2,-1,-1],"seed":"0","rows":rows,
     "finite_floor1_refutations":energies_below_one,
     "nontrivial_bound_count":sum(x['signed_mean_upper_decimal']<1 for x in rows)}
with open('probe_receipt.json','x') as f:
    json.dump(out,f,indent=2)
print(f"PASS {len(rows)} rows, {out['nontrivial_bound_count']} bounds below1; {len(energies_below_one)} finite floor1 refutations")
