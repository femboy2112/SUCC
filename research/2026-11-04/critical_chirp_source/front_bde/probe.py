"""Exact arithmetic checks for BDE source controls; not an asymptotic proof."""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, gcd, lcm
import json

TAPS = ((6, 8), (5, 4), (4, 8), (1, -1), (7, -8), (3, 2), (2, 2))


def r(n):
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def rp(n):
    return F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def sharp(n):
    return F(8, 8*n-6)+F(4, 8*n-5)+F(4, 8*n-4)-F(1, 8*n-1)


def sharpp(n):
    return F(2*(480*n**3-628*n*n+229*n-16),
             (2*n-1)*(4*n-3)*(8*n-5)*(8*n-1))


def d3(x):
    z=x.denominator
    p=1
    while z % 3 == 0:
        p*=3
        z//=3
    return p


def ternary_only(x):
    return d3(x)==x.denominator


def power_floor(base, limit):
    if limit < 1:
        raise ValueError('positive limit required')
    result=1
    while result*base<=limit:
        result*=base
    return result


def log_floor(base, n):
    result=0
    while n>=base:
        n//=base
        result+=1
    return result


def tail_interval(n, terms):
    lo=sum((r(n+k)/16**k for k in range(1, terms+1)), F(0))
    return lo, lo+r(n+terms+1)/F(15*16**terms)


def radial_derivative_interval(n, order, terms=32):
    def derivative(x):
        return (-1)**order*factorial(order)*8**order*sum(
            (F(c, (8*x-e)**(order+1)) for e,c in TAPS), F(0))
    mid=sum((derivative(n+k)/F(4*16**k)
             for k in range(1, terms+1)), F(0))
    err=F(33*factorial(order)*8**order,
          60*16**terms*(8*(n+terms+1)-7)**(order+1))
    return mid-err, mid+err


def derivative_constant(order):
    return factorial(order+1)*(F(1,30)+F(167,3840)*F(16,9)**(order+2))


def lock_adjustment(x, partial_tail, B, D):
    if gcd(B,D)!=1:
        raise ValueError('frequency must be a unit on the ternary grid')
    a=(D*B*(x+partial_tail)+F(1,2)).__floor__()
    k=((-a)*pow(B,-1,D)) % D if D>1 else 0
    return F(k,D)


def source_streams(N):
    u=w=F(0)
    us=[u]
    ws=[w]
    for n in range(1,N+1):
        assert r(n)==rp(n)
        assert sharp(n)==sharpp(n)
        u=16*u+r(n)
        w=16*w+sharp(n)
        us.append(u)
        ws.append(w)
    # A separate common-LCM integer register uses the expanded source polynomials.
    M=1
    for n in range(1,N+1):
        M=lcm(M,rp(n).denominator,sharpp(n).denominator)
    a=b=0
    for n in range(1,N+1):
        p,q=rp(n),sharpp(n)
        a=16*a+p.numerator*(M//p.denominator)
        b=16*b+q.numerator*(M//q.denominator)
        assert F(a,M)==us[n]
        assert F(b,M)==ws[n]
    return us,ws


def checksum(values):
    return sha256('\n'.join(str(x) for x in values).encode()).hexdigest()


def run():
    N=540
    us,ws=source_streams(N)
    radial=[]
    for n in (8,16,32,37,83,173):
        z=(2*us[n]-ws[n])/4
        for m in range(4):
            low,high=radial_derivative_interval(n,m)
            lead=F((-1)**m*factorial(m),32*n**(m+1))
            allowance=derivative_constant(m)/n**(m+2)
            assert lead-allowance<low<high<lead+allowance
            if m==0:
                assert low<z<high
            if m==2:
                assert low>0
            if m==3:
                assert high<0
        radial.append({'n':n,'radial_exact_sha256':checksum([z]),
                       'orders_checked':[0,1,2,3]})
    assert 32*derivative_constant(2)<128
    assert F(16,3)*derivative_constant(3)<128
    reset_times=set(range(86,N+1,105))
    v=F(0)
    vs=[v]
    record=[]
    genuine_lcm=mutant_lcm=1
    max_D=1
    for n in range(1,N+1):
        f=r(n)
        x=16*v+f
        if n in reset_times:
            m=log_floor(16,n)
            # Finite startup cap; eventually redundant in the infinite theorem.
            cap=max(1,(8*(n-1)-1)//27)
            D=power_floor(3,min(m**6,cap))
            B=power_floor(16,n*n)
            K=0
            while 16**K<D:
                K+=1
            low,high=tail_interval(n,K)
            e=lock_adjustment(x,low,B,D)
            v=x+e
            f+=e
            center=(B*(v+low)+F(1,2)).__floor__()
            residual_low=B*(v+low)-center
            residual_high=B*(v+high)-center
            assert -F(33,64*D)<residual_low<=residual_high<F(33,64*D)
            assert 0<=e<1
            assert (8*n-7)%3==0 and (8*n-3)%5==0 and (4*n-1)%7==0
            # Exact no-new-prime check through source LCM, allowing prime powers.
            new={p for p in factor_support(r(n).denominator) if genuine_lcm%p}
            assert not new
            max_D=max(max_D,D)
            record.append({'n':n,'D':D,'B':B,'tail_terms':K,'correction':str(e),
                           'residual_interval':[str(residual_low),str(residual_high)],
                           'max_absolute_bound':str(F(33,64*D))})
        else:
            v=x
        assert f>0
        assert us[n].denominator==v.denominator
        assert ternary_only(v-us[n])
        genuine_lcm=lcm(genuine_lcm,r(n).denominator)
        mutant_lcm=lcm(mutant_lcm,f.denominator)
        assert genuine_lcm==mutant_lcm
        vs.append(v)
    protected=0
    changed=0
    pairs=0
    for n in range(257,385):
        for t in range(n+1,385):
            a=us[t]-us[n]
            b=vs[t]-vs[n]
            assert ternary_only(b-a)
            if d3(a)>max_D:
                assert a.denominator==b.denominator
                protected+=1
            changed+=(a.denominator!=b.denominator)
            pairs+=1
    return {'status':'FINITE_EXACT_CHECKS_PASS',
            'source_horizon':N,'source_routes':['four-term Fraction','polynomial integer LCM'],
            'radial':radial,'reset_records':record,
            'state_denominator_checks':N,'prefix_lcm_checks':N,
            'pair_audit':{'interval':[257,385],'unordered_pairs':pairs,
                          'protected_pairs':protected,'changed_denominator_pairs':changed,
                          'conservative_grid':max_D},
            'original_stream_sha256':checksum(us),
            'mutant_stream_sha256':checksum(vs),
            'limitations':['No asymptotic statement is inferred from this receipt.',
                            'The finite reset gaps do not reach their asymptotic regime.',
                            'The mutant changes forcing and is not the original pi source.']}


def factor_support(n):
    result=set()
    p=2
    while p*p<=n:
        if n%p==0:
            result.add(p)
            while n%p==0:
                n//=p
        p+=1 if p==2 else 2
    if n>1:
        result.add(n)
    return result


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
