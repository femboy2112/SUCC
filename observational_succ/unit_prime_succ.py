"""Exact finite controls for the additive/prime SUCC weighted-state theorem.

All operations use rational Fractions. Hilbert and Euler convergence are
paper proofs, not conclusions from bounded computation. RH remains open.
"""
from fractions import Fraction as Q
from math import isqrt


class SourceError(ValueError):
    pass


def integer(x, lo=1, hi=10000):
    if type(x) is not int or not lo <= x <= hi:
        raise SourceError("Typed positive finite integer and resource budget required")
    return x


def prime(p):
    return type(p) is int and p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def prime_list(P):
    integer(P, 2, 300)
    return tuple(p for p in range(2, P+1) if prime(p))


def path(word, beta, start=1):
    """Chronological S(n)=n+t, V_p(n)=pn, each step weighted (old/new)^beta."""
    integer(beta,1,12); integer(start,1,1000000)
    if type(word) is not tuple or len(word)>100:
        raise SourceError("Finite tuple of <=100 source actions required")
    n=start; weight=Q(1)
    for action in word:
        if type(action) is not tuple or len(action)!=2:
            raise SourceError("Typed action required")
        op,val=action
        if op=="S":
            integer(val,1,1000000); nxt=n+val
        elif op=="V":
            integer(val,2,1000000)
            if not prime(val): raise SourceError("Composite prime-FUCC mutation")
            nxt=n*val
        else: raise SourceError("Unknown carrier action")
        if nxt>10**9: raise SourceError("Endpoint exceeds runtime budget")
        weight*=Q(n,nxt)**beta; n=nxt
    if weight!=Q(start,n)**beta: raise AssertionError("Flat cocycle failed")
    return n,weight


def braid(n,p,beta):
    integer(n,1,1000000); integer(p,2,1000000)
    if not prime(p): raise SourceError("Nonprime generator")
    left=path((("S",1),("V",p)),beta,n)
    right=path((("V",p),("S",p)),beta,n)
    if left!=right: raise AssertionError("V_p S = S^p V_p violated")
    return left


def prime_smooth(primes,cap,beta):
    """Distinct prime-power jet traversal, independent of linear successor."""
    integer(cap,1,10000); integer(beta,1,12)
    if (type(primes) is not tuple or tuple(sorted(set(primes)))!=primes
            or not all(prime(p) for p in primes)):
        raise SourceError("Genuine strictly ordered prime coordinates required")
    result={}
    def recur(i,n,w):
        if i==len(primes):
            if n in result: raise AssertionError("Prime normal form duplicated")
            result[n]=w; return
        p=primes[i]
        while n<=cap:
            recur(i+1,n,w)
            n*=p; w/=p**beta
    recur(0,1,Q(1))
    return result


def finite_equivalence(P,cap,beta):
    """On shared finite states, prime jets equal the independent S prefix."""
    integer(P,2,300); integer(cap,P,10000); integer(beta,1,12)
    state=prime_smooth(prime_list(P),cap,beta)
    assert all(w==Q(1,n**beta) for n,w in state.items())
    assert all(n in state for n in range(1,P+1))
    return {"P":P,"cap":cap,"beta":beta,"matched":len(state),
            "unseen":tuple(n for n in range(1,cap+1) if n not in state),
            "unit_weight":state[1],"infinite_theorem_by_tests":False,
            "RH_proved":False}


def ratio_bounds(P,beta):
    """Exact rational enclosure of zeta(beta)-1 for integer beta>=2."""
    integer(beta,2,12)
    zp=Q(1)
    for p in prime_list(P): zp*=Q(p**beta,p**beta-1)
    tail=Q(1,(beta-1)*P**(beta-1))
    return zp-Q(1),zp-Q(1)+tail


def linear_ratio_bounds(cap,beta):
    integer(cap,2,10000); integer(beta,2,12)
    mass=sum((Q(1,n**beta) for n in range(2,cap+1)),Q())
    return mass,mass+Q(1,(beta-1)*cap**(beta-1))


def log_successor_bounds(n):
    """Rational 1/(n+1) <= log(1+1/n) <= 1/n; proof in dossier."""
    integer(n,1,10**9)
    return Q(1,n+1),Q(1,n)


def adjoint_defect_prefix(P,p):
    """Finite diagnostic only: infinite adjoint-defect theorem is in dossier."""
    integer(P,2,10000); integer(p,2,1000000)
    if not prime(p): raise SourceError("Genuine prime required")
    return (1,),tuple(n for n in range(1,P+1) if n%p)


def probe():
    a=finite_equivalence(11,100,2)
    x=ratio_bounds(11,2); y=linear_ratio_bounds(11,2)
    assert x[0]<=y[1] and y[0]<=x[1]
    assert braid(7,3,2)==(24,Q(7,24)**2)
    assert path(tuple([("S",1)]*11),2)==path((("V",2),("V",2),("V",3)),2)
    return {"matched":a["matched"],"unit":str(a["unit_weight"]),
            "prime_ratio":tuple(map(str,x)),"linear_ratio":tuple(map(str,y)),
            "exact_finite_checks":True,"RH_proved":False}
