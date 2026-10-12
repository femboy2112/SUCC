"""Residue-one prime Euler units, p-adic limits and Archimedean obstructions.

Exact finite arithmetic checks support three distinct CLASSICAL theorems:
  E_p(-1)=sum_{k>=0}p^k in Q_p, with unit residue 1;
  m!+1 -> 1 in every Q_p while ->+infinity in R;
  any continuous homomorphism prod_p(1+p Z_p)->R_{>0} is trivial
  because the domain is compact and R_{>0} has no compact subgroups
  except {1}. The topological theorem is proved in research prose,
  NOT established by running finitely many tests.

p-adic zeta interpolation is an external theorem, NOT computed here:
  on the correct WEIGHT TWO analytic branch for odd p,
  zeta_{p,weight2}(-1)=(1-p)*zeta(-1)=(p-1)/12.
Do not conflate the weight-two branch with the untwisted single
p-adic zeta branch at p>=5; branch numbering depends on convention.
No global RH theorem or Archimedean Gamma function is constructed.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, gcd, isqrt


class ResidueArchError(ValueError): pass


def prime(n):
    if type(n) is not int or n<2: return False
    if n==2: return True
    if n%2==0: return False
    return all(n%d for d in range(3,isqrt(n)+1,2))


def bounded(n,lo,hi):
    if type(n) is not int or not lo<=n<=hi:
        raise ResidueArchError("Finite integer out of declared domain")
    return n


def valuation(x,p):
    if not prime(p): raise ResidueArchError("Need an actual prime place")
    if type(x) is int: x=Q(x)
    if not isinstance(x,Q) or x==0:
        raise ResidueArchError("Need nonzero rational")
    a,b=abs(x.numerator),x.denominator
    v=0
    while a%p==0: a//=p;v+=1
    while b%p==0: b//=p;v-=1
    return v


def residue(x,p,power=1):
    bounded(power,1,40)
    if type(x) is int: x=Q(x)
    if not isinstance(x,Q) or valuation(x,p)<0:
        raise ResidueArchError("p-adically integral rational needed")
    mod=p**power
    if gcd(x.denominator,mod)!=1:
        raise ResidueArchError("Nonunit rational denominator")
    return x.numerator*pow(x.denominator,-1,mod)%mod


def euler_unit(p,terms):
    """Truncation error p^terms/(1-p) has valuation EXACTLY terms."""
    if not prime(p): raise ResidueArchError("Euler factor needs a prime")
    bounded(terms,1,32)
    full=Q(1,1-p)
    partial=sum((Q(p**k) for k in range(terms)),Q())
    err=full-partial
    if err!=Q(p**terms,1-p) or valuation(err,p)!=terms:
        raise ArithmeticError("p-adic convergence broken")
    if residue(full,p)!=1%p or valuation(full,p)!=0:
        raise ArithmeticError("E_p(-1) is not a residue-one local unit")
    return {"prime":p,"local_value":str(full),"terms":terms,
            "finite_partial":str(partial),"exact_error":str(err),
            "error_valuation":terms,"residue":1,
            "local_absolute_value":"1"}


def rival_units(p):
    if not prime(p): raise ResidueArchError("Actual prime required")
    a=Q(1,1-p); b=Q(1,1-p*p)
    if a==b or residue(a,p)!=1%p or residue(b,p)!=1%p:
        raise ArithmeticError("The two identical-residue values merged")
    return a,b


def prime_factors(n):
    bounded(n,2,10**12)
    remain=n; out=[];d=2
    while d*d<=remain:
        if remain%d==0:
            out.append(d)
            while remain%d==0: remain//=d
        d=3 if d==2 else d+2
    if remain>1: out.append(remain)
    return tuple(out)


def factorial_one(m):
    bounded(m,2,10)
    n=factorial(m)+1
    factors=prime_factors(n)
    if min(factors)<=m: raise ArithmeticError("Euclid prime divisor bound failed")
    exponents={}
    for p in range(2,m+1):
        if prime(p):
            v=valuation(factorial(m),p)
            if v<1 or residue(n,p,v)!=1%(p**v):
                raise ArithmeticError("Local factorial congruence violated")
            exponents[p]=v
    return {"m":m,"N":n,"prime_factors":factors,"prime_N":prime(n),
            "all_factors_larger_than_m":True,"finite_residue_exponents":exponents}


def product_formula(x):
    """For a SINGLE diagonal rational x, |x|_infty*prod |x|_p=1."""
    if not isinstance(x,Q) or x==0:
        raise ResidueArchError("Nonzero exact diagonal rational required")
    a=abs(x.numerator);b=x.denominator
    ps=set(prime_factors(a) if a>1 else ())
    ps.update(prime_factors(b) if b>1 else ())
    finite=Q(1); local={}
    for p in sorted(ps):
        vp=valuation(x,p);norm=Q(p)**(-vp)
        finite*=norm;local[p]={"v_p":vp,"abs_p":str(norm)}
    if finite*abs(x)!=1: raise ArithmeticError("Rational product formula failed")
    return {"x":str(x),"arch_abs":str(abs(x)),
            "finite_abs_product":str(finite),"norm":"1","local":local}


def residue_idele_arch_norm(primes,arch_abs):
    """Non-diagonal family x_p=1/(1-p): all local norms equal 1."""
    if (type(primes) is not tuple or len(set(primes))!=len(primes)
            or any(not prime(p) for p in primes)
            or not isinstance(arch_abs,Q) or arch_abs<=0):
        raise ResidueArchError("Need distinct primes and positive real magnitude")
    if any(valuation(Q(1,1-p),p)!=0 for p in primes):
        raise ArithmeticError("Local factors not p-adic units")
    return {"finite_norm":"1","arch_norm":str(arch_abs),
            "idele_norm":str(arch_abs),"norm_one":arch_abs==1,
            "not_diagonal_product_formula":True}


def kl_weight_two_interpolation(p):
    """CLASSICAL theorem input, not a construction of a p-adic L function.

    A standard weight-indexed branch convention interpolates
    zeta_{p,i}(1-k)=(1-p^(k-1))*zeta(1-k) for k == i mod(p-1).
    The point k=2 uses the corresponding branch; p=2 excluded here.
    """
    if not prime(p) or p==2: raise ResidueArchError("Odd prime required")
    global_special=Q(-1,12)
    local_correction=1-p
    branch_value=local_correction*global_special
    e=Q(1,1-p)
    if e*branch_value!=global_special:
        raise ArithmeticError("Interpolation special-value identity contradicted")
    return {"p":p,"weight":2,"weight_residue":2%(p-1),
            "local_factor":str(e),"euler_removal_factor":str(local_correction),
            "branch_special_value":str(branch_value),
            "global_special_value":str(e*branch_value),
            "p_adic_measure_constructed":False}


def demo():
    ps=(2,3,5,7,11,13)
    units=[euler_unit(p,5) for p in ps]
    assert all(a!=b for a,b in (rival_units(p) for p in ps))
    euclid=[factorial_one(m) for m in (3,4,5,6,7)]
    assert factorial_one(5)["N"]==121 and not factorial_one(5)["prime_N"]
    diag=product_formula(Q(-1,12))
    ideles=[residue_idele_arch_norm(ps,x)
            for x in (Q(1),Q(2),Q(1,12))]
    interpolation=[kl_weight_two_interpolation(p) for p in ps if p!=2]
    assert all(x["global_special_value"]=="-1/12" for x in interpolation)
    return {
        "status":"PRIME_RESIDUE_ONE_ADELIC_LOCAL_GLOBAL_OBSTRUCTION",
        "local_units":units,
        "same_residue_has_nonunique_local_units":True,
        "euler_geometric_series_converges_p_adically":True,
        "finite_local_euler_norms_all_one":True,
        "all_euler_factors_are_residue_one_units":True,
        "euclid_factorial_one":euclid,
        "factorial_one_limit_each_p_adic":"1",
        "factorial_one_limit_real":"+infinity",
        "factorial_one_not_always_prime":True,
        "diagonal_minus_one_twelfth_product_formula":diag,
        "nondiagonal_idelic_example":ideles,
        "positive_real_scale_determined_by_residue_one_alone":False,
        "compact_to_positive_real_continuous_group_hom_trivial":True,
        "topological_group_theorem_tested_by_finite_sampling":False,
        "weight_two_Kubota_Leopoldt_branch_interpolation":interpolation,
        "interpolation_theorem_imported":True,
        "p_adic_zeta_function_constructed":False,
        "Tate_arch_completion_constructed":False,
        "RH_claimed":False,
    }
