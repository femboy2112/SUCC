"""Exact source-aware Gaussian envelope for completed xi; no RH or GP prior claim.

Parent: source-interaction adelic branch PR #73. Analytic proof: theorem dossier.
F(z)=xi(1/2+z) is in even Bargmann-Fock with norm²<=260/27.
H(z)=exp(-z²/2)F(z) has an even reflected Gaussian RBF kernel.
All finite Euler data are true-prime and have an explicit missing-integers tail.
"""
from fractions import Fraction as Q
from math import isqrt, factorial

B2=Q(260,27)
C0=Q(59,120)
R0=Q(47,100)

class SourceGaussianError(ValueError):
    pass

def rat(v):
    if type(v) not in (int,Q): raise SourceGaussianError("exact rational required")
    return Q(v)

def exp_interval(v,N=70):
    v=rat(v)
    if not 0<=v<N+2: raise SourceGaussianError("unsafe Taylor tail")
    lo=sum((v**k/factorial(k) for k in range(N+1)),Q())
    a=v**(N+1)/factorial(N+1)
    return lo,lo+a/(1-v/Q(N+2))

def expminus_interval(v):
    lo,hi=exp_interval(v)
    return 1/hi,1/lo

def atan_interval(x,N=14):
    x=rat(x)
    if not 0<x<=1: raise SourceGaussianError("atan domain")
    a=sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(N)),Q())
    term=(-1)**N*x**(2*N+1)/Q(2*N+1)
    return min(a,a+term),max(a,a+term)

def pi_interval():
    a,b=atan_interval(Q(1,5))
    c,d=atan_interval(Q(1,239))
    return 16*a-4*d,16*b-4*c

def sqrt_up(v,scale=10**9):
    v=rat(v)
    if v<0: raise SourceGaussianError("negative radius")
    n=(v.numerator*scale*scale+v.denominator-1)//v.denominator
    k=isqrt(n)
    if k*k<n: k+=1
    return Q(k,scale)

def zero_disk(radius=R0):
    radius=rat(radius)
    if radius<=0 or radius**4>=12: raise SourceGaussianError("radius domain")
    upper=B2*radius**4/(2*(1-radius**4/Q(12)))
    return {"radius":radius,"squared_remainder_upper":upper,
            "squared_center_lower":C0*C0,
            "certified":upper<C0*C0, "RH_proved":False}

def primes_through(P):
    if type(P) is not int or not 2<=P<=300:
        raise SourceGaussianError("finite source cutoff")
    return tuple(p for p in range(2,P+1)
                 if all(p%d for d in range(2,isqrt(p)+1)))

def xi_prime_interval(P,sigma,declared=None):
    """Genuine source interval; ONLY integer sigma>=2 in Euler-convergent region."""
    primes=primes_through(P)
    if type(sigma) is not int or not 2<=sigma<=12:
        raise SourceGaussianError("not a convergent positive Euler probe")
    if declared is not None and tuple(declared)!=primes:
        raise SourceGaussianError("missing/forged independent prime place")
    z=Q(1)
    for p in primes: z/=1-Q(1,p**sigma)
    tail=Q(1,(sigma-1)*P**(sigma-1))
    m=sigma//2 if sigma%2==0 else (sigma-1)//2
    gam=factorial(m-1) if sigma%2==0 else Q(factorial(2*m),4**m*factorial(m))
    a=Q(sigma*(sigma-1),2)*gam
    pil,pih=pi_interval()
    return {"primes":primes,"sigma":sigma,"xi_lower":a*z/pih**m,
            "xi_upper":a*(z+tail)/pil**m,"Euler_tail":tail,"RH_proved":False}

def even_gaussian_kernel_interval(x,y):
    """Reflected RBF Gaussian on real axis; full kernel is holomorphic."""
    x,y=rat(x),rat(y)
    a,b=expminus_interval((x-y)**2/2)
    c,d=expminus_interval((x+y)**2/2)
    return (a+c)/2,(b+d)/2

def source_tube(P,sigma,target):
    """Hard source envelope, not a GP confidence interval."""
    z=rat(target)
    x=Q(2*sigma-1,2)
    src=xi_prime_interval(P,sigma)
    el,eh=expminus_interval(x*x/2)
    yl,yu=src["xi_lower"]*el,src["xi_upper"]*eh
    if z==x or z==-x:
        return {"lower":yl,"upper":yu,"radius":Q(),
                "source_value":(yl,yu),"RH_proved":False}
    gl,gh=even_gaussian_kernel_interval(x,x)
    kl,kh=even_gaussian_kernel_interval(z,x)
    tl,th=even_gaussian_kernel_interval(z,z)
    V=max(Q(),th-kl*kl/gh)
    debt=B2-yl*yl/gh
    if debt<0: raise SourceGaussianError("inconsistent source energy")
    rad=sqrt_up(debt*V)
    return {"lower":kl*yl/gh-rad,"upper":kh*yu/gl+rad,
            "radius":rad,"unobserved_radius":sqrt_up(B2*th),
            "source_value":(yl,yu),"RH_proved":False}

def even_fock_tail(R,degree):
    """Sum_(j>degree) R^(4j)/(2j)! <= exact geometric upper bound."""
    R=rat(R)
    if type(degree) is not int or not 0<=degree<=20 or R<0:
        raise SourceGaussianError("invalid even jets")
    q=R**4/Q((2*degree+4)*(2*degree+3))
    if q>=1: raise SourceGaussianError("uncontrolled analytic tail")
    return R**(4*(degree+1))/factorial(2*degree+2)/(1-q)

def rouche(coeff,R,j,budget):
    """Conditional, exact Rouché zero-count from trusted even Taylor jets."""
    a=tuple(rat(c) for c in coeff)
    R,budget=rat(R),rat(budget)
    if not a or type(j) is not int or not 0<=j<len(a) or R<=0 or budget<=0:
        raise SourceGaussianError("invalid zero-count query")
    used=sum((factorial(2*k)*v*v for k,v in enumerate(a)),Q())
    if used>budget: raise SourceGaussianError("infeasible Fock source budget")
    missing=sqrt_up((budget-used)*even_fock_tail(R,len(a)-1))
    dominating=abs(a[j])*R**(2*j)
    others=sum((abs(v)*R**(2*k) for k,v in enumerate(a) if k!=j),Q())
    yes=dominating>others+missing
    return {"zero_count":2*j if yes else None,"certified":yes,
            "tail_upper":missing,"RH_proved":False}

def finite_ambiguity(nodes,d=0):
    """A nonzero even entire polynomial invisible at supplied points and jets."""
    if type(d) is not int or not 0<=d<=10: raise SourceGaussianError("jet depth")
    cs=[Q(1)]
    for val in nodes:
        x=rat(val); nxt=[Q()]*(len(cs)+1)
        for k,c in enumerate(cs):
            nxt[k]-=x*x*c
            nxt[k+1]+=c
        cs=nxt
    cs=[Q()]*(d+1)+cs
    energy=sum((factorial(2*j)*c*c for j,c in enumerate(cs)),Q())
    if not energy: raise ArithmeticError("ghost zero function")
    return {"coefficients":tuple(cs),"energy":energy,
            "does_not_preserve_full_Euler_germ":True}

def receipt():
    a=xi_prime_interval(11,3)
    t=source_tube(11,3,Q(12,5))
    z=zero_disk()
    return {"global_function":"xi(1/2+z)",
            "Fock_norm_squared_upper":str(B2),
            "zero_free_disk":{"radius":str(z["radius"]),"certified":z["certified"],
                              "rational_squared_tail":str(z["squared_remainder_upper"])},
            "prime_cutoff":11,"prime_sigma":3,"observed_primes":list(a["primes"]),
            "xi_three_interval":[str(a["xi_lower"]),str(a["xi_upper"])],
            "source_Gaussian_target":"H(12/5)",
            "source_Gaussian_tube":[str(t["lower"]),str(t["upper"])],
            "conditional_radius":str(t["radius"]),
            "unconditional_radius":str(t["unobserved_radius"]),
            "nontrivial_zeta_zeros_used":False,
            "Gaussian_prior_proved_for_arithmetic":False,
            "RH_proved":False}
