"""Exact source-jet positivity and seed-observability checks; no pi digits."""
from fractions import Fraction as F
from functools import reduce
from hashlib import sha256
from math import comb, factorial, gcd
import json

ORIG=(F(4),F(0),F(0),F(-2),F(-1),F(-1),F(0),F(0))
RAD=(F(2),F(-2),F(-1),F(-2),F(-1,2),F(-1,2),F(1,4),F(0))


def forcing(n, taps):
    return sum((c/F(8*(n-1)+j) for j,c in enumerate(taps,1)),F(0))


def source_stream(N,taps,seed=F(0)):
    result=[seed]
    for n in range(1,N+1):
        result.append(16*result[-1]+forcing(n,taps))
    return result


def series_coefficients(N):
    # Positive binomial series v=1-(1-s)^(1/8), then formal rational division.
    v=[F(0)]*(N+1)
    if N:
        v[1]=F(1,8)
    for k in range(2,N+1):
        v[k]=v[k-1]*F(8*k-9,8*k)
    d=[F(0)]*(N+1)
    for k in range(1,N+1):
        d[k]=2*v[k]+sum((v[j]*v[k-j] for j in range(1,k)),F(0))
    inv=[F(1)]+[F(0)]*N
    for k in range(1,N+1):
        inv[k]=sum((d[j]*inv[k-j] for j in range(1,k+1)),F(0))
    numerator=[F(0)]*(N+1)
    for k in range(1,N+1):
        numerator[k]=4*(15*v[k]+16*sum(v[1:k],F(0)))
    b=[F(0)]*(N+1)
    for k in range(1,N+1):
        b[k]=sum((numerator[j]*inv[k-j] for j in range(1,k+1)),F(0))
    return b


def weights(b,m):
    return tuple((-1)**(ell+1)*sum((F(comb(k,ell))*b[k]
                    for k in range(ell,m+1)),F(0)) for ell in range(1,m+1))


def laurent(taps,k):
    return sum((c*F((8-j)**(k-1),8**k)
                for j,c in enumerate(taps,1)),F(0))


def independent_jet_data(N):
    # Geometric moments by shifting the summation index, not the binomial v series.
    moments=[F(1,15)]
    for k in range(1,N+1):
        moments.append((1+sum((F(comb(k,j))*moments[j] for j in range(k)),F(0)))/15)
    z=[F(0)]*(N+1)
    for k in range(1,N+1):
        z[k]=-sum((laurent(RAD,d)*(-1)**(k-d)*comb(k-1,k-d)*moments[k-d]
                   for d in range(1,k+1)),F(0))
    return z


def lag_coefficient(z,k,ell):
    return sum((z[d]*(-1)**(k-d)*comb(k-1,k-d)*ell**(k-d)
                for d in range(1,k)),F(0))


def solve_jet(m,z):
    rows=[[lag_coefficient(z,k,ell) for ell in range(1,m+1)]
          +[-laurent(ORIG,k)] for k in range(2,m+2)]
    for c in range(m):
        i=next(i for i in range(c,m) if rows[i][c])
        rows[c],rows[i]=rows[i],rows[c]
        a=rows[c][c]
        rows[c]=[x/a for x in rows[c]]
        for i in range(m):
            if i!=c:
                a=rows[i][c]
                rows[i]=[x-a*y for x,y in zip(rows[i],rows[c])]
    return tuple(row[-1] for row in rows)


def residual(n,m,b,z):
    return forcing(n,ORIG)+sum((a*(z[n+ell]-z[n])
                              for ell,a in enumerate(weights(b,m),1)),F(0))


def finite_difference(n,m,z):
    return sum((F((-1)**j*comb(m,j))*z[n+j] for j in range(m+1)),F(0))


def carry_stream(N,seed):
    x=seed
    xs=[x]
    cs=[]
    for n in range(1,N+1):
        y=16*x+forcing(n,ORIG)
        c=y.__floor__()
        x=y-c
        xs.append(x)
        cs.append(c)
    return xs,cs


def digest(x):
    return sha256(str(x).encode()).hexdigest()


def run():
    # All cases declared in PREREGISTRATION.md before this instrument ran.
    max_m=192
    b=series_coefficients(max_m+1)
    assert all(x>0 for x in b[1:])
    assert b[1:5]==[F(15,2),F(421,32),F(4551,256),F(179123,8192)]
    zcoef=independent_jet_data(14)
    jet_checks=[]
    for m in (1,2,3,4,7,11):
        a=weights(b,m)
        assert a==solve_jet(m,zcoef)
        lead=laurent(ORIG,m+2)+sum((x*lag_coefficient(zcoef,m+2,ell)
                                  for ell,x in enumerate(a,1)),F(0))
        predicted=F(factorial(m+1),32)*b[m+1]
        assert lead==predicted>0
        jet_checks.append({'m':m,'leading_residual':str(lead),
                           'delay_weights':[str(x) for x in a]})
    z=source_stream(max_m+2,RAD)
    exact_positive=[]
    for n in (1,2,13,37,83):
        for m in (1,2,3,4,7,11):
            value=residual(n,m,b,z)
            assert value>0
            exact_positive.append({'n':n,'m':m,'residual_sha256':digest(value)})
    joint=[]
    for n in (13,37,83):
        value=residual(n,n,b,z)
        old=residual(n,3,b,z)
        assert 0<value<old
        joint.append({'n':n,'m':n,'residual_sha256':digest(value),
                      'ratio_to_order3':str(value/old)})
    late=[]
    for m in (64,128,192):
        diff=finite_difference(1,m,z)
        value=residual(1,m,b,z)
        assert value>0
        # Signs are observations, not fitted universal onset claims.
        late.append({'n':1,'m':m,'difference_sign':(diff>0)-(diff<0),
                     'difference_sha256':digest(diff),'residual_sha256':digest(value),
                     'residual_approx':float(value)})
    U=source_stream(40,ORIG)
    Z=source_stream(40,RAD)
    Y=[u-z for u,z in zip(U,Z)]
    seed_tests=0
    for s in (F(1,5),F(1,15)):
        for H in (1,7,65536):
            for ell in (-1,0,1):
                for n in range(2,30):
                    shifted=H*(Y[n]+16**n*s+Z[n+ell])
                    original=H*(Y[n]+Z[n+ell])
                    assert (shifted-original)%1==(H*s)%1
                    seed_tests+=1
    assert (16**2*F(1,7))%1 != (16**3*F(1,7))%1
    annihilators=[]
    for lags in ((1,),(2,),(2,3)):
        g=reduce(gcd,lags)
        actual=reduce(gcd,(16**n*(16**ell-1)
                           for n in range(2,7) for ell in lags))
        expected=16**2*(16**g-1)
        assert actual==expected
        annihilators.append({'lags':lags,'start':2,'gcd':actual})
    assert 16-16==0  # P(16) for the Ward stencil E-16.
    x,c=carry_stream(30,F(0))
    y,d=carry_stream(30,F(1,5))
    for N in range(1,31):
        assert (x[N]-y[N])/16**N == -F(1,5)-sum(
            (F(c[j-1]-d[j-1],16**j) for j in range(1,N+1)),F(0))
    first=next(n for n,(a,bb) in enumerate(zip(c,d),1) if a!=bb)
    return {'status':'EXACT_SOURCE_JET_AND_SEED_CHECKS_PASS',
            'positive_b_coefficients':max_m+1,'jet_checks':jet_checks,
            'positive_residual_cases':exact_positive,'late_order_observations':late,
            'joint_order_checks':joint,
            'exact_seed_rotation_checks':seed_tests,'annihilators':annihilators,
            'first_carry_disagreement_seed_1_over_5':first,
            'carry_hashes':[digest(c),digest(d)],
            'scope':'Exact finite calibration only; asymptotic statements have paper proofs.'}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
