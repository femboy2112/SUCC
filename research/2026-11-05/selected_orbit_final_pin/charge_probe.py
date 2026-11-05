"""Independent exact finite-delay, seed and literal-carry calibration."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys


def poles(n):
    return 4*F(1,8*n-7)-2*F(1,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def collapsed(n):
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def states(last, seed, scale):
    u=[seed]
    carries=[]
    for n in range(1,last+1):
        assert poles(n)==collapsed(n)
        nxt=16*u[-1]+scale*poles(n)
        carry=nxt.__floor__()-16*u[-1].__floor__()
        assert nxt-nxt.__floor__()==16*(u[-1]-u[-1].__floor__())+scale*poles(n)-carry
        carries.append(carry)
        u.append(nxt)
    return u,carries


def run():
    cases=[((0,1),(16,-1)),((0,2),(256,-1)),
           ((0,1,3),(2,-1,1)),((0,2,5),(1,1,-1))]
    rows=[]
    for scale in (1,2):
        base,carries=states(178,F(0),scale)
        shift,_=states(178,F(1,5),scale)
        for n in (43,89,173):
            for ds,cs in cases:
                M=sum(c*16**d for c,d in zip(cs,ds))
                a=sum(c*sum((16**(d-k)*scale*collapsed(n+k)
                             for k in range(1,d+1)),F(0)) for c,d in zip(cs,ds))
                lhs=sum(c*base[n+d] for c,d in zip(cs,ds))
                altered=sum(c*shift[n+d] for c,d in zip(cs,ds))
                assert lhs==M*base[n]+a
                assert altered-lhs==M*16**n*F(1,5)
                assert (altered-lhs-M*F(1,5)).denominator==1
                rows.append(dict(scale=scale,n=n,delays=ds,coefficients=cs,
                                 charge=M,forcing_phase=str(a%1),
                                 rational_seed_phase=str((altered-lhs)%1)))
        for h in (-7,1,19):
            assert all((h*(shift[n]-base[n])-F(h,5)).denominator==1
                       for n in range(len(base)))
    return dict(scope='exact Fraction identities, not exponential-sum decay',
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                rows=rows,independent_source_checks=178,complete_lifts=True,
                literal_carries=True,seed_zero=True)


if __name__=='__main__':
    result=run()
    path=Path(__file__).with_name('CHARGE_RECEIPT.json')
    if '--verify' in sys.argv:
        assert json.loads(path.read_text())==json.loads(json.dumps(result))
        print('PASS: 24 exact delayed identities; source, seed and carry controls')
    else:
        path.write_text(json.dumps(result,indent=2)+'\n')
        print('wrote',path)
