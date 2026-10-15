"""ADELIC-ZENO: successor convergence is place/topology-relative.

Exact rational arithmetic, unique factorization and p-adic valuations. No
physical observation of every place, formal adele functor, or RH implication.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import isqrt


class AdelicZenoError(ValueError):
    pass


def exact(x):
    if type(x) not in (int,Q):raise AdelicZenoError("rational source only")
    return Q(x)


def natural(n,maximum=256):
    if type(n) is not int or not 0<=n<=maximum:
        raise AdelicZenoError("finite integer stage/precision and resource cap")
    return n


def prime(p):
    return type(p) is int and p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def distinct_factors(n):
    if type(n) is not int or n<1 or n>10**12:
        raise AdelicZenoError("bounded exact integer factorization domain")
    out=[]; m=n
    d=2
    while d*d<=m:
        if m%d==0:
            out.append(d)
            while m%d==0:m//=d
        d+=1
    if m>1:out.append(m)
    return tuple(out)


def valuation_integer(n,p):
    if type(n) is not int or n==0 or not prime(p):
        raise AdelicZenoError("integer nonzero and genuine prime place required")
    n=abs(n);v=0
    while n%p==0:
        n//=p;v+=1
    return v


def valuation(x,p):
    x=exact(x)
    if x==0 or not prime(p):
        raise AdelicZenoError("nonzero rational and genuine prime place")
    return valuation_integer(x.numerator,p)-valuation_integer(x.denominator,p)


def local_norm(x,p):
    """True |x|_p=p^(-v_p(x)), never fake composite Euler factor."""
    x=exact(x)
    if x==0:return Q()
    return Q(p)**(-valuation(x,p))


def finite_norm_product(x):
    """Exact finite certificate of the GLOBAL product formula for Q*.

    The validity for every nonzero rational, including unlisted primes
    (which have norm 1), is a UFD theorem, not a finite empirical survey.
    """
    x=exact(x)
    if not x or abs(x.numerator)>10**12 or x.denominator>10**12:
        raise AdelicZenoError("nonzero rational bounded factorization source")
    primes=tuple(sorted(set(distinct_factors(abs(x.numerator))
                            +distinct_factors(x.denominator))))
    norms=tuple((p,local_norm(x,p)) for p in primes)
    global_product=abs(x)
    for _,value in norms:global_product*=value
    if global_product!=1:raise ArithmeticError("global rational norm reciprocity false")
    return {"rational":x,"arch_abs":abs(x),"finite_local_norms":norms,
            "global_norm_product":global_product,
            "all_other_prime_norms_exactly_one":True,
            "all_places_contract_strictly":False,
            "source_formula":"Q_PRODUCT_FORMULA_UFD"}


def geometric_partial(r,n):
    """Finite geometric additive SUCC, same algebra all places."""
    r=exact(r);natural(n)
    if r==1:return Q(n)
    return (1-r**n)/(1-r)


def real_zeno_partial(n):
    """Sum_{j<n}(1/2)^j -> 2 in R, but q is 2-adic EXPANDING."""
    natural(n,128)
    r=Q(1,2)
    s=geometric_partial(r,n)
    return {"stage":n,"partial":s,"real_limit":Q(2),
            "real_error":Q(2,2**n),
            "two_adic_step_norm":Q(2**n),
            "two_adic_contraction":False,
            "source":"SAME_GEOMETRIC_LAW_Q_U_1/2"}


def two_adic_zeno_partial(n):
    """Sum_{j<n}4^j -> -1/3 in Q_2, diverges in R."""
    natural(n,128)
    q=Q(4)
    s=geometric_partial(q,n)
    assert s.denominator==1 and 3*s+1==4**n
    return {"stage":n,"partial_integer":int(s),"two_adic_limit":Q(-1,3),
            "two_adic_error_norm":Q(1,4**n),
            "real_magnitude":abs(s),
            "arch_contraction":False,
            "source":"SAME_GEOMETRIC_LAW_Q_U_4"}


def two_adic_inverse_limit_residue(n,precision):
    """Finite compatible residues; n>=ceil(precision/2) certifies -1/3."""
    natural(n,128);natural(precision,128)
    if precision<1:raise AdelicZenoError("precision at least one dyadic digit")
    mod=2**precision
    s=two_adic_zeno_partial(n)["partial_integer"]
    target=(-pow(3,-1,mod))%mod
    return {"stage":n,"precision":precision,
            "observed_residue":s%mod,"limit_residue":target,
            "proved_at_precision":2*n>=precision,
            "source":"AUTHENTIC_INTEGER_CLOCK_MOD_2^K"}


def finite_place_blindspot(observed_primes):
    """Finite local p menus cannot discover a hidden denominator prime.

    For q=1/ell, |q|_infty<1 and all observed |q|_p=1, but |q|_ell=ell.
    """
    ps=tuple(observed_primes)
    if len(ps)!=len(set(ps)) or len(ps)>64 or not all(prime(p) for p in ps):
        raise AdelicZenoError("independent genuine prime menu required")
    ell=2 if not ps else max(ps)+1
    while not prime(ell):ell+=1
    if ell>10**12:raise AdelicZenoError("source factor budget")
    r=Q(1,ell)
    report=finite_norm_product(r)
    if any(local_norm(r,p)!=1 for p in ps) or local_norm(r,ell)!=ell:
        raise ArithmeticError("finite-menu blindspot violated")
    return {"selected_primes":ps,"hidden_prime":ell,
            "rational_multiplier":r,
            "real_contractive":abs(r)<1,
            "all_selected_finite_places_neutral":True,
            "hidden_place_expansion_norm":Q(ell),
            "global_product_verified":report["global_norm_product"]==1,
            "inference_from_finite_menu_to_all_places_refuted":True}
