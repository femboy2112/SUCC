"""Independent direct interval phase sums for mixed-quadratic extrema/probes.

Shared source interval data, separate MPIntervalContext transcendental path.
Does not recertify the exhaustive maximum or claim independent source data.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
from mpmath.ctx_iv import MPIntervalContext

HERE=Path(__file__).resolve().parent
ROUND=HERE.parent.parent


def rational(t):
    sign,man,exp,_=t
    v=F((-1 if sign else 1)*man)
    return v*(2**exp) if exp>=0 else v/F(2**(-exp))


def main():
    sp=ROUND/'complement_budget/results/source_1103.json'
    rp=HERE/'MIXED_QUADRATIC_1103.json'
    source=json.loads(sp.read_text());result=json.loads(rp.read_text())
    assert sha256(sp.read_bytes()).hexdigest()==result['source_receipt_sha256']
    p,m=source['p'],source['m'];L=(p-1)//4
    xi=4*pow(16,L+1-(p+7)//8,p)%p
    xs=[xi*pow(16,r,p)%p for r in range(m)]
    assert len(set(xs))==m and pow(16,m,p)==1
    iv=MPIntervalContext();iv.dps=70
    scale=1<<80;checks=[]
    for sr,row in zip(source['rows'],result['rows']):
        assert sr['h']==row['h']
        B=[iv.mpc(iv.mpf([a,b])/scale,iv.mpf([c,d])/scale) for a,b,c,d in sr['B']]
        rad=row['correlation_L1_error'];radius=F(rad['numerator'],rad['denominator'])
        den=row['correlation_denominator']
        for probe in row['direct_checks']:
            a,b=probe['a'],probe['b'];total=iv.mpc(0)
            for x,z in zip(xs,B):
                angle=-2*iv.pi*((a*x*x+b*x)%p)/p
                total+=z*iv.mpc(iv.cos(angle),iv.sin(angle))
            total/=m
            lr,ur=[rational(t) for t in total.real._mpi_]
            li,ui=[rational(t) for t in total.imag._mpi_]
            cr,ci=[F(c,den) for c in probe['center_numerator']]
            distance=max(abs(lr-cr),abs(ur-cr))+max(abs(li-ci),abs(ui-ci))
            assert distance<=radius
            checks.append({'h':sr['h'],'a':a,'b':b,
                           'independent_rectangle':[str(lr),str(ur),str(li),str(ui)],
                           'distance_upper':str(distance),'radius':str(radius),'contained':True})
    out={'checks':checks,'direct_terms':len(checks)*m,
         'source_sha256':sha256(sp.read_bytes()).hexdigest(),
         'certificate_sha256':sha256(rp.read_bytes()).hexdigest(),
         'review_code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'scope':'Separate interval transcendental/direct-sum algorithm on shared source boxes; no independent source reconstruction or exhaustive-max replay.'}
    (HERE/'INDEPENDENT_REVIEW.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(len(checks),'probes',len(checks)*m,'direct terms PASS')


if __name__=='__main__':main()
