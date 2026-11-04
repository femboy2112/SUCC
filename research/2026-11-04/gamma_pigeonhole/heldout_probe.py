"""Independently written post-preregistration exact Fraction holdouts."""
from fractions import Fraction as F
from math import ceil
import hashlib,json
from gamma_pigeonhole import forcing,clock_state

PS=(193,241,257,281,337,353)
EXPECTED="845730b09ea18e4eaa30645aa948d98f9e753be2428fa8e587f36da9acbeaf29"

def solve(p):
    assert p%8==1 and p>5 and all(p%a for a in range(2,int(p**.5)+1))
    n=(p+7)//8
    D=(p+3)*(p+4)*(p+5);C=D//8
    rhs=F(15*p*p+121*p+240,p*D)
    beta=F(-4*p*p-33*p-67,D)
    original=forcing(n)
    assert original==rhs and original.denominator==p*C and beta.denominator==C
    prev=clock_state(n-1);now=clock_state(n)
    assert prev[1]%p!=0 and now[1]%p==0 and now[1]%(p*p)!=0
    assert now[0]*pow((now[1]//p),-1,p)%p==4
    # Independently declared four-term rational Euler interval
    dlo=F(1,2*p*p)-F(1,3*p**3)+F(1,4*p**4)-F(1,5*p**5)
    dhi=dlo+F(1,5*p**5)
    left=30*dlo-F(49,p**3)
    right=30*dhi-F(49,p**3)+F(236,p**4)
    assert left<original<right and (right-left)*C<1
    k=ceil(C*(left-F(4,p)))
    candidate=(F(4,p)+F(k,C))%1
    assert candidate==original
    neighbor=original+F(1,C)
    assert neighbor<30*dlo and not(left<neighbor<right)
    assert (p*neighbor).numerator*pow((p*neighbor).denominator,-1,p)%p==4
    return {"p":p,"n":n,"C":C,"original":str(original),"p_residue":4,
            "window_lo":str(left),"window_hi":str(right),
            "certificate_width_over_spacing":str(C*(right-left)),
            "coarse_mutant":str(neighbor),"mutant_rejected":True}

def replay():
    rows=[solve(p) for p in PS]
    digest=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    assert digest==EXPECTED,"PREREGISTERED_HOLDOUT_DIGEST_CHANGED"
    return rows,digest

if __name__=="__main__":
    rows,digest=replay()
    print("FRESH_HOLDOUTS_6_PASS")
    print("SHA256",digest)
    for row in rows:
        print("p",row["p"],"n",row["n"],"C",row["C"],
              "scaled_width",float(F(row["certificate_width_over_spacing"])))
