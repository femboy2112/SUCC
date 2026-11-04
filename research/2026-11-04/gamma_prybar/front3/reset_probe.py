"""Exact sparse-reset holdout. Invoke from this directory; no external code."""
from fractions import Fraction as F
from math import gcd, lcm, isqrt
from hashlib import sha256
import json


def four(n):
    return 4*F(1,8*n-7)-2*F(1,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def other(n):
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def prime_sieve(N):
    ok = bytearray([1])*(N+1)
    ok[:2] = bytes(2)
    for p in range(2,isqrt(N)+1):
        if ok[p]:
            ok[p*p::p] = bytes((N-p*p)//p+1)
    return [p for p in range(2,N+1) if ok[p]]


def protected_modulus(s,d,ps,causal):
    m = 8*s+(s+3)//4 if causal else (17*s+1)//2
    width = (s+1)//2+10 if causal else s+3
    lower = m-width
    M = 1
    for p in ps:
        if m//p == lower//p:
            continue
        while d%p==0:
            M *= p
            d //= p
    return M


def past_predictor(s):
    # Exact backward differences of the four reciprocal progressions.
    L = s//2
    result = F()
    for offset, weight in [(7,4),(4,-2),(3,-1),(2,-1)]:
        term = F(weight,15*(8*s-offset))
        for k in range(L):
            result += term
            term *= F(-128*(k+1),15*(8*(s-k-1)-offset))
    return result


def run(s0=194, causal=False):
    resets=[s0]
    while len(resets)<18 or resets[-1]<3*s0:
        s=resets[-1]
        resets.append(s+3*(s//96))
    N=resets[-1]+12
    terms=[F()] + [four(i) for i in range(1,2*N+1)]
    ps=prime_sieve(9*N)
    # Independent ascending polynomial/LCM integer reconstruction.
    full_d = lcm(*(other(j).denominator for j in range(1,N+1)))
    integer = 0
    if causal:
        prefix = sum(terms[j]/16**j for j in range(1,s0+1)) + past_predictor(s0)/16**s0
    else:
        prefix = sum(terms[j]/16**j for j in range(1,2*s0+1))
    C=F((16**(2*s0)*prefix).__floor__(),16**(2*s0))
    U=V=F()
    source_lcm=mutant_lcm=1
    last=F(10)
    births={}
    rows=[]
    errors=[]
    final_phases=[]
    for n in range(1,N+1):
        f=terms[n]
        U=16*U+f
        g=other(n)
        integer=16*integer+g.numerator*(full_d//g.denominator)
        assert U==F(integer,full_d)
        oldV=V
        if n in resets:
            d=U.denominator
            M=protected_modulus(n,d,ps,causal)
            future=F()
            for j in range(2*n,n,-1):
                future=(future+terms[j])/16
            if causal:
                predicted=past_predictor(n)
                # The forward sum appears solely in this validation assertion.
                tail_ceiling=F(1,16**n*256*n*n)
                bound=F(4,15)**(n//2+1)
                assert max(abs(predicted-future),abs(predicted-future-tail_ceiling)) <= bound
                t=16**n*C-predicted
            else:
                t=16**n*C-future
            k=((t*d-U.numerator)/M).__ceil__()
            a=U.numerator+M*k
            trials=1
            while gcd(a,d)!=1:
                a+=M
                trials+=1
            V=F(a,d)
            assert V.denominator==d and (a-U.numerator)%M==0
            # Independent finite rounding certificate stronger than 2^(-n).
            err=abs(V-t)
            assert err < F(1,2**n)
            if d>1:
                p=next(p for p in ps if d%p==0)
                assert F(p*(a//p),d).denominator < d
            rows.append({"n":n, "d_bits":d.bit_length(), "M_bits":M.bit_length(),
                         "unit_search_trials":trials, "error_lt_2_to_minus_n":True})
        else:
            V=16*V+f
        newf=V-16*oldV
        assert newf>0 and last>newf
        last=newf
        if n not in resets or 8*n-7 in ps:
            assert newf==f
        assert V.denominator==U.denominator
        source_lcm=lcm(source_lcm,f.denominator)
        mutant_lcm=lcm(mutant_lcm,newf.denominator)
        assert source_lcm==mutant_lcm
        for p in ps:
            if f.denominator%p==0 and p not in births:
                births[p]=n
            if p in births and n<=births[p]+births[p]//64:
                assert (V-U).denominator%p and (newf-f).denominator%p
        if n>N-32:
            # T_n in [future, future+16^(-n)/(64(2n)^2)].
            future=F()
            for j in range(2*n,n,-1):
                future=(future+terms[j])/16
            err=abs(V-16**n*C+future)+F(1,16**n*256*n*n)
            assert err < F(1,2**(n//2))
            errors.append(err)
            final_phases.append(V%1)
    tent_total=F()
    for x in final_phases:
        for y in final_phases:
            z=(x-y)%1
            tent_total+=max(0,1-16*min(z,1-z))
    J=16*tent_total/len(final_phases)**2
    assert J>F(1599,100)
    # Encode via integer bytes rather than CPython's decimal-length threshold.
    h=sha256()
    for value in (J.numerator,J.denominator):
        data=value.to_bytes((value.bit_length()+7)//8,'big')
        h.update(len(data).to_bytes(8,'big'))
        h.update(data)
    return {"s0":s0,"N":N,"birth_primes":len(births),"resets":rows,
            "final_window":[N-31,N],"q":16,"J_ppm_floor":int(J*10**6),
            "J_exact_num_den_sha256":h.hexdigest(),
            "max_tail_error_below_2_to_minus_floor_n_over_2":True}


if __name__=="__main__":
    import sys
    if sys.argv[1:] not in ([], ["--causal"]):
        raise SystemExit("Usage: reset_probe.py [--causal]")
    print(json.dumps(run(causal=bool(sys.argv[1:])),indent=2))
