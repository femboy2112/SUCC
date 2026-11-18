"""Exact, preregistered four-pole Frobenius cancellation cutoff audit.

Candidate before evaluation: for a born odd prime p>max(7,sqrt(8n)),
K=floor((8n-2)/p), normalized rational coefficient F is nonzero,
|F|<64/15, and den(F) divides 2^floor(K/2)*lcm(1,...,K).
Thus p^2>=19*32^K suffices for v_p(U_n)=-1.
Finite checks do not prove the all-n statement; see paper derivation.
Holdouts n=17,33,65,129,257,513,1025 were fixed before computation.
Hostile p19 at n10..16 and p73 at n274 must be preserved.
"""
from fractions import Fraction as Q
from math import isqrt, lcm
import json


def primes(m):
    f=bytearray(b'\1')*(m+1)
    f[:2]=b'\0\0'
    for p in range(2,isqrt(m)+1):
        if f[p]:f[p*p::p]=bytes(len(f[p*p::p]))
    return [p for p in range(2,m+1) if f[p]]


def original(n):
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def collapsed(n):
    return Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def modular(q,p):
    assert q.denominator%p
    return q.numerator*pow(q.denominator,-1,p)%p


def coefficient(n,p):
    K=(8*n-2)//p
    chi=1 if p%8 in (1,7) else -1
    F=Q()
    events=[]
    for a,b,c in [(8,7,Q(4)),(8,3,-Q(1)),(4,1,-Q(1,2)),(2,1,-Q(1,2))]:
        for k in range(1,K+1,2):
            if (k*p+b)%a:continue
            j=(k*p+b)//a
            if j>n:continue
            if a==8:
                v=chi*Q(2)**((8-k-b)//2)
            elif a==4:
                v=Q(2)**(3-k)
            else:
                v=Q(2)**(2-2*k)
            F+=c*v/k
            events.append((j,a,b,k,str(c*v/k)))
    return F,K,sorted(events)


def run():
    holds=[17,33,65,129,257,513,1025]
    indices=sorted(set(holds+[10,11,12,13,14,15,16,274]))
    us={};u=Q();native=1
    for n in range(1,max(indices)+1):
        r=original(n)
        assert r==collapsed(n)
        u=16*u+r
        native=lcm(native,2*n-1,4*n-1,8*n-7,8*n-3)
        assert native%u.denominator==0
        if n in indices:us[n]=(u,native)
    allp=primes(8*max(indices));rows=[];count=0;certs=0;mutations=0;observed_cancellations=[]
    for n in holds:
        u,native=us[n];nr=nc=0
        for p in allp:
            if p>8*n:break
            if p<=7 or p*p<=8*n:continue
            F,K,ev=coefficient(n,p)
            if not ev:continue
            assert K<p
            assert F
            assert abs(F)<Q(64,15)
            if p%4==1:assert F>=Q(692,225)
            else:assert F<=-Q(202,105)
            den_bound=2**(K//2)*lcm(*range(1,K+1))
            assert den_bound%F.denominator==0
            assert F.numerator**2 < 19*32**K
            predicted=modular(F,p)*pow(16,n-(p+1)//2,p)%p
            assert modular(p*u,p)==predicted
            assert (u.denominator%p!=0)==(predicted==0)
            if not predicted:
                observed_cancellations.append({"n":n,"p":p,"K":K,"coefficient":str(F)})
            # A sign-erasing mutation must not pass whenever the residue is nonzero.
            if predicted:
                assert modular(-p*u,p)!=predicted
                mutations+=1
            if p*p>=19*32**K:
                assert predicted and u.denominator%p==0
                certs+=1;nc+=1
            nr+=1;count+=1
        rows.append({'n':n,'exact_prime_checks':nr,'cutoff_certified_primes':nc,
                     'native_denominator_bits':native.bit_length(),
                     'reduced_denominator_bits':u.denominator.bit_length()})
    controls=[]
    for n,p in [(n,19) for n in range(10,17)]+[(274,73)]:
        u,_=us[n];F,K,ev=coefficient(n,p)
        assert F and F.numerator%p==0
        assert u.denominator%p
        assert p*p<19*32**K
        controls.append({'n':n,'p':p,'coefficient':str(F),'K':K,'cancelled':True,'cutoff_correctly_not_satisfied':True})
    return {'candidate':'p^2 >= 19*32^K implies p survives, K=floor((8n-2)/p)',
            'holdouts':holds,'exact_residue_checks':count,'certificate_cases':certs,
            'sign_mutation_rejections':mutations,'rows':rows,'known_cancellations':controls,
            'observed_cancellations':observed_cancellations,
            'scope':'Exact finite rational observations; universal proof separate. R0 and normality OPEN.'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
