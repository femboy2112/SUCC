"""Exact arithmetic CRT / selected-cylinder probes. No asymptotic inference."""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, gcd, isqrt, lcm
import json
import sys

C = (4, -2, -1, -1)
OFF = (1, 4, 5, 6)
NULL_C = (-8, 8, 4, 8, 2, 2, -1)
FRESH = (1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123)


def source(n, coefficients=C, offsets=OFF):
    if n < 1 or len(coefficients) != len(offsets):
        raise ValueError('positive n, matching coefficients and offsets required')
    return sum((F(c, 8*(n-1)+d) for c,d in zip(coefficients,offsets)), F())


def circle(x):
    return x - x.numerator // x.denominator


def centered(x):
    x = circle(x)
    return x if x <= F(1,2) else x-1


def distance(x):
    return abs(centered(x))


def orbit(stop, coefficients=C, offsets=OFF, seed=F()):
    result = [circle(F(seed))]
    for n in range(1,stop+1):
        result.append(circle(16*result[-1]+source(n,coefficients,offsets)))
    return result


def valuation(n,p):
    if not n:
        raise ValueError('valuation zero undefined')
    v=0
    while n%p==0:
        n//=p;v+=1
    return v


def primary(x,p):
    q=x.denominator
    v=0
    while q%p==0:
        q//=p;v+=1
    if not v:
        return F()
    P=p**v
    return F((x.numerator*pow(q,-1,P))%P,P)


def rational_mod(x,p):
    if x.denominator%p==0:
        raise ValueError('nonintegral reduction')
    return x.numerator*pow(x.denominator,-1,p)%p


def is_prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def order16(p):
    if gcd(p,16)!=1:
        raise ValueError('odd modulus required')
    a=16%p;k=1
    while a!=1:
        a=a*16%p;k+=1
    return k


def birth(Q):
    return (Q+7)//8 if Q%8==1 else (Q+3)//8 if Q%8==5 else (Q+1)//4


def next_Q_event(Q,b):
    n=b+1
    while not any((8*(n-1)+d)%Q==0 for d in OFF):
        n+=1
    return n


def interval_lcm_bound(m,s):
    """Exact divisor certificate: lcm(m+1,...,m+s) | C(m+s,s) lcm(1,...,s)."""
    if m<0 or s<1:
        raise ValueError('m>=0,s>=1')
    actual=lcm(*range(m+1,m+s+1))
    bound=comb(m+s,s)*lcm(*range(1,s+1))
    assert bound%actual==0
    return actual,bound


def filter_certificate(n,coefficients,u):
    d=len(coefficients)-1
    M=sum(c*16**j for j,c in enumerate(coefficients))
    result=sum((c*u[n+j] for j,c in enumerate(coefficients)),F())
    forcing_terms=[sum(coefficients[j]*16**(j-t) for j in range(t,d+1)) for t in range(1,d+1)]
    remainder=sum((a*source(n+t) for t,a in enumerate(forcing_terms,1)),F())
    assert circle(result-M*u[n]-remainder)==0
    Q=lcm(*(source(n+t).denominator for t in range(1,d+1))) if d else 1
    D=u[n].denominator; V=result.denominator
    assert Q%remainder.denominator==0
    assert (D*Q)%V==0
    if M:
        assert V*Q*abs(M)>=D
        assert (V*Q)%(D//gcd(D,abs(M)))==0
    if d:
        s=8*d; m=8*n
        _,upper=interval_lcm_bound(m,s)
        assert upper%Q==0
    else:
        upper=1
    return {'n':n,'coefficients':coefficients,'degree':d,'P16':str(M),
            'original_denominator_bits':D.bit_length(),'filtered_denominator_bits':V.bit_length(),
            'remainder_lcm_bits':Q.bit_length(),'interval_bound_bits':upper.bit_length(),
            'finite_inequalities':True}


def cylinder(A,L,h=1,delta=F(1,20)):
    if A<1 or L<1 or not h or not 0<delta<F(1,17):
        raise ValueError('positive A,L; nonzero h; 0<delta<1/17')
    g=F(); lo=-delta;hi=delta
    for j in range(L):
        lo=max(lo,(-delta-g)/16**j)
        hi=min(hi,(delta-g)/16**j)
        if j<L-1:
            f=h*(source(A+j+2)-source(A+j+1))
            if 17*delta+abs(f)>=1:
                raise ValueError('no-wrap margin fails')
            g=16*g+f
    assert hi-lo<=2*delta/F(16**(L-1))
    return lo,hi


def green_prefix(A,M):
    return sum((source(A+j)/16**j for j in range(1,M+1)),F())


def dyadic_shadow(A,L,u,padding=5):
    """Construct a tiny rational seed with all odd-primary data unchanged.

    The desired state at A is a Green prefix's negative modulo one; round
    only the seed to denominator 16^(A+L+padding). The eventual circle alias
    time is A+L+padding. No irrational seed is projected p-adically.
    """
    R=L+padding
    tail=green_prefix(A,R)
    target=centered(-u[A]-tail)
    x=target*16**R
    integer=(x+F(1,2)).numerator//(x+F(1,2)).denominator
    seed=F(integer,16**(A+R))
    assert abs(seed)<=F(1,16**A)
    # The Green truncation error at A is <=16^-R*r(A+R+1)/15.
    state_error=F(1,2*16**R)+source(A+R+1)/F(15*16**R)
    # At A+j the real state differs from -T_(A+j) modulo one by <=16^j error.
    lag_error=15*16**(L-1)*state_error
    maximum_lag=F(16,(8*A+1)**3)+lag_error
    return seed, maximum_lag, A+R


def joint_row(p,h,u):
    b=birth(p); next_event=next_Q_event(p,b);order=order16(p)
    native=p%4==1
    L=order if native else next_event-b
    eligible=native and order*order>=p
    values=u[b:b+L+1]
    rows=[]
    counts={'full_slips':0,'primary_slips':0,'cofiber_slips':0,'primary_large_full_small':0}
    for j in range(L-1):
        x=h*(values[j+1]-values[j])
        a=primary(x,p);v=circle(x-a)
        assert primary(v,p)==0 and circle(a+v)==circle(x)
        fs=distance(x)>=F(1,20);ps=distance(a)>=F(1,20);vs=distance(v)>=F(1,20)
        counts['full_slips']+=fs;counts['primary_slips']+=ps;counts['cofiber_slips']+=vs
        counts['primary_large_full_small']+=ps and not fs
    return {'p':p,'class_mod8':p%8,'birth':b,'next_p_event':next_event,'order16':order,
            'states':L,'lags':L-1,'h':h,'SC06_eligible':eligible,
            'window_type':'native_complete_cycle' if native else 'reflected_short_first_window',
            **counts,'half_slips_pass':2*counts['full_slips']>=L-1}


def run():
    sys.set_int_max_str_digits(0)
    assert all(is_prime(p) for p in FRESH)
    u=orbit(3000)
    filters=[]
    for n in (17,43,101,233,509):
        for d in (1,3,isqrt(n),max(1,n//7)):
            c=[-1]+[0]*(d-1)+[1]
            filters.append(filter_certificate(n,c,u))
            c=[1]+[(-1)**j*(j+1) for j in range(1,d+1)]
            filters.append(filter_certificate(n,c,u))
    filters.append(filter_certificate(101,[-16,1],u))
    lcm_rows=[]
    for m in (0,1,17,99,997):
        for s in (1,2,7,19,41):
            a,b=interval_lcm_bound(m,s)
            lcm_rows.append({'m':m,'s':s,'lcm_bits':a.bit_length(),'bound_bits':b.bit_length(),'divides':True})
    joint=[joint_row(p,h,u) for p in FRESH for h in (1,3,7)]
    shadows=[]
    for p in (1033,1061):
        A=birth(p);L=order16(p)-1
        seed,upper,alias=dyadic_shadow(A,L,u)
        distances=[distance(u[n+1]-u[n]+15*16**n*seed) for n in range(A,A+L)]
        assert max(distances)<=upper<F(1,20)
        lo,hi=cylinder(A,L)
        theta=centered(u[A+1]-u[A]+15*16**A*seed)
        authentic=centered(u[A+1]-u[A])
        assert lo<=theta<=hi
        assert not lo<=authentic<=hi
        for q in (3,5,7,13,19,73,1033,1061):
            for n in (1,A,A+L,alias):
                assert primary(u[n]+16**n*seed,q)==primary(u[n],q)
        assert circle(16**alias*seed)==0
        shadows.append({'p':p,'A':A,'L':L,'seed':str(seed),'max_lag_distance':str(max(distances)),
            'proved_lag_upper':str(upper),'odd_primary_checks':32,'alias_time':alias,
            'cylinder_width':str(hi-lo),'authentic_outside':True,'shadow_inside':True,
            'early_state_error_at_A_minus_8_upper':str(F(1,16**8))})
    powers=[]
    for p,a in ((7,3),(11,2),(13,2),(19,2),(73,2)):
        Q=p**a;b=birth(Q);end=next_Q_event(Q,b)
        initial=primary(u[b],p)
        mismatches=[];top_ok=True
        for j,n in enumerate(range(b,end)):
            top_ok &= rational_mod(Q*u[n],p)==pow(16,j,p)*rational_mod(Q*u[b],p)%p
            if primary(u[n],p)!=circle(16**j*initial):
                mismatches.append(n)
        assert top_ok
        powers.append({'p':p,'a':a,'Q':Q,'birth':b,'next_Q_event':end,'top_mod_p_pure':top_ok,
            'full_p_primary_pure':not mismatches,'first_failure':mismatches[0] if mismatches else None})
    null=orbit(400,NULL_C,tuple(range(1,8)))
    controls=[]
    for name,v in [('authentic',u),('seven_pole_null',null),('wrong_ratio',orbit(400,(5,-2,-1,-1))),
                   ('same_ratio',orbit(400,(4,0,-1,0))),('rank_matched_ratio',orbit(400,(F(2),F(11,4),F(-1,2),F(-17,4))))]:
        A=127;L=127
        ds=[distance(v[n+1]-v[n]) for n in range(A,A+L)]
        controls.append({'family':name,'A':A,'L':L,'slips':sum(d>=F(1,20) for d in ds),
                         'min_distance':str(min(ds)),'max_distance':str(max(ds))})
    cancellations={'p19':{str(n):str(primary(u[n],19)) for n in range(9,18)},
                   'p73_n274':str(primary(u[274],73))}
    assert all(primary(u[n],19)==0 for n in range(10,17))
    assert primary(u[17],19)!=0 and primary(u[274],73)==0
    result={'scope':'exact finite observations; no selected asymptotic SC06 proof',
            'filter_certificates':filters,'lcm_certificates':lcm_rows,'joint_windows':joint,
            'dyadic_shadows':shadows,'prime_power_windows':powers,'controls':controls,'cancellations':cancellations}
    print(json.dumps(result,indent=2))
    return result

if __name__=='__main__':
    run()
