"""Exact finite Witt/dual carry and source-relative learning-in-the-limit probes.

Two choices of arithmetic law on the same p-digit tree:
  MIXED : Z/p^k Z (W_k(F_p) as rings, NOT standard Witt coordinates)
  EQUAL : F_p[t]/t^k (equal-characteristic truncated series).
No physical measurements; tests are deterministic independent finite oracles.
The universal inverse-limit/learning statements are PAPER math, not finite tests.
"""
from __future__ import annotations
from fractions import Fraction
from math import factorial, isqrt


class LearningSourceError(ValueError):
    """Ill-typed source, unresolved probe, or unlicensed inference."""


def _nat(x, lower=0):
    if type(x) is not int or x < lower:
        raise LearningSourceError(f"exact int >= {lower} required")
    return x


def genuine_prime(p):
    return type(p) is int and p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def _p(p):
    if not genuine_prime(p):
        raise LearningSourceError("actual rational prime label required")
    return p


def _k(k, limit=12):
    _nat(k,1)
    if k > limit:
        raise LearningSourceError("exact finite resource cap; paper theorem all depths")
    return k


def digits_of(n,p,k):
    """Canonical p-adic integer digit representatives; no Witt-Teich coordinates."""
    _nat(n);_p(p);_k(k)
    n%=p**k
    return tuple((n//p**i)%p for i in range(k))


def integer_of(digits,p):
    _p(p)
    if type(digits) not in (tuple,list) or not digits:
        raise LearningSourceError("nonempty finite digit tuple required")
    if any(type(v) is not int or not 0<=v<p for v in digits):
        raise LearningSourceError("invalid exact digits")
    if len(digits)>12:
        raise LearningSourceError("exact finite resource cap")
    return sum(d*p**i for i,d in enumerate(digits))


def _pair(a,b,p):
    _p(p)
    for v in (a,b):
        if type(v) is not tuple or not v or any(type(x) is not int or not 0<=x<p for x in v):
            raise LearningSourceError("typed p-digits required")
    if len(a)!=len(b) or len(a)>12:
        raise LearningSourceError("equal bounded p-digit depth required")


def mixed_add(a,b,p):
    """Z/p^k addition; carry history is a source-bearing intermediate record."""
    _pair(a,b,p)
    carry=0;out=[];history=[]
    for ai,bi in zip(a,b):
        z=ai+bi+carry
        out.append(z%p)
        carry=z//p
        history.append(carry)
    return tuple(out),tuple(history)


def equal_add(a,b,p):
    """F_p[t]/t^k addition, with no carry between degrees."""
    _pair(a,b,p)
    return tuple((ai+bi)%p for ai,bi in zip(a,b))


def mixed_mul(a,b,p):
    _pair(a,b,p)
    return digits_of(integer_of(a,p)*integer_of(b,p),p,len(a))


def equal_mul(a,b,p):
    _pair(a,b,p)
    return tuple(sum(a[i]*b[j-i] for i in range(j+1))%p for j in range(len(a)))


def carry_cocycle(a,b,p):
    """Standard digits: the carry 2-cocycle for 0->C_p->C_p²->C_p->0."""
    _p(p);_nat(a);_nat(b)
    if a>=p or b>=p:
        raise LearningSourceError("first residue digits only")
    return (a+b)//p


def cocycle_square(a,b,c,p):
    _p(p);_nat(c)
    if c>=p:raise LearningSourceError("third residue digit must be < p")
    lhs=carry_cocycle(a,b,p)+carry_cocycle((a+b)%p,c,p)
    rhs=carry_cocycle(b,c,p)+carry_cocycle(a,(b+c)%p,p)
    return lhs,rhs


def extension_witness(p):
    """Same residue+square-zero graded shadow, different whole ring character."""
    _p(p)
    return {"p":p,"size":p*p,"maximal_ideal_size":p,
            "residue_field_size":p,"graded_dual_dimension":2,
            "mixed_ring_characteristic":p*p,
            "equal_ring_characteristic":p,
            "mixed_p_times_one":digits_of(p,p,2),
            "equal_p_times_one":(0,0),
            "carry_cocycle_nonzero":carry_cocycle(p-1,1,p)==1,
            "whole_rings_isomorphic":False}


def first_carry_witness(p):
    _p(p)
    a=digits_of(p-1,p,2)
    b=digits_of(1,p,2)
    w,h=mixed_add(a,b,p)
    e=equal_add(a,b,p)
    return {"a":a,"b":b,"mixed_sum":w,"equal_sum":e,
            "carry_history":h,"first_difference_level":2}


def distance_exponent(a,b,p):
    """Common first differing digit; None means identical finite readouts."""
    _pair(a,b,p)
    return next((i for i,(x,y) in enumerate(zip(a,b)) if x!=y),None)


def finite_distance(a,b,p):
    """Exact p-adic distance if unequal within chart, else UPPER BOUND only."""
    v=distance_exponent(a,b,p)
    return {"observational_status":"exact" if v is not None else "unresolved",
            "value":Fraction(1,p**v) if v is not None else None,
            "upper_bound":Fraction(1,p**len(a)) if v is None else None}


def digit_map_preserves_distance(p,k,x,y):
    """Digitwise Z/p^k <-> F_p[t]/t^k isometry, not ring homomorphism."""
    _p(p);_k(k);_nat(x);_nat(y)
    N=p**k
    a=digits_of(x%N,p,k);b=digits_of(y%N,p,k)
    v=distance_exponent(a,b,p)
    difference=(x-y)%N
    val=0
    if difference:
        while difference%p==0:
            val+=1
            difference//=p
    else:val=None
    return v==val


def learning_signature(p,k,model,toolkit):
    """Only the declared observer alphabet is readable; no guessing hidden law."""
    _p(p);_k(k)
    if model not in ("mixed", "equal"):
        raise LearningSourceError("declared ring family has only two model types")
    if toolkit=="geometry":
        return (p**k,p,Fraction(1,p**k))
    if toolkit=="marked_addition":
        return digits_of(p,p,k) if model=="mixed" else (0,)*k
    if toolkit=="full_operations":
        return (p**k,p,Fraction(1,p**k),
                digits_of(p,p,k) if model=="mixed" else (0,)*k)
    raise LearningSourceError("unknown admissible observer instrument")


def update_version_space(p,transcript,toolkit):
    """Finite exact filter; no inference that supplied transcript is physical."""
    _p(p)
    if type(transcript) not in (tuple,list):
        raise LearningSourceError("typed finite staged transcript expected")
    candidates={"mixed","equal"};history=[]
    prev=0
    for record in transcript:
        if type(record) is not tuple or len(record)!=2:
            raise LearningSourceError("each record is (positive level, exact signature)")
        level,observed=record
        _k(level)
        if level<=prev:raise LearningSourceError("observation levels must strictly increase")
        prev=level
        candidates={model for model in candidates
                    if learning_signature(p,level,model,toolkit)==observed}
        history.append((level,tuple(sorted(candidates))))
    return {"survivors":tuple(sorted(candidates)),"history":tuple(history),
            "source_physically_authenticated":False,
            "infinite_completion_proved_by_finite_records":False}


def append_verified_digit(prefix, digit,p):
    """One lawful new finite source observation; exact parent compatibility."""
    _p(p);_nat(digit)
    if digit>=p or type(prefix) is not tuple or any(type(x) is not int or not 0<=x<p for x in prefix):
        raise LearningSourceError("invalid sourced next digit")
    if len(prefix)>=11:raise LearningSourceError("resource cap")
    new=prefix+(digit,)
    if prefix and new[:-1]!=prefix:raise ArithmeticError("inconsistent source maps")
    return {"digits":new,"representative":integer_of(new,p),
            "horizon":len(new),"cylinder_diameter_bound":Fraction(1,p**len(new))}


def compatible_observer_prefixes(prefixes,p):
    _p(p)
    if type(prefixes) not in (tuple,list) or not prefixes:
        raise LearningSourceError("one or more actual finite observation stages")
    parent=()
    for item in prefixes:
        if type(item) is not tuple or len(item)!=len(parent)+1:
            raise LearningSourceError("strictly increasing one-digit stages")
        if item[:-1]!=parent:
            raise LearningSourceError("causally incompatible observation histories")
        integer_of(item,p)
        parent=item
    return {"finite_prefix":parent,"levels":len(prefixes),
            "limit_would_be_unique_if_all_levels_source_compatible":True,
            "all_infinite_stages_were_observed":False,
            "last_cylinder_diameter_bound":Fraction(1,p**len(parent))}


def sparse_factorial_prefix(p,k):
    """Finite prefix of x=sum_{j>=2} p^(j!), a genuine Zp point not in Z.

    Every finite prefix is realized by a natural integer, but no ordinary
    integer has the all-level sparse factorial digit pattern (paper proof).
    """
    _p(p);_k(k)
    ds=[0]*k;j=2
    while factorial(j)<k:
        ds[factorial(j)]=1
        j+=1
    return tuple(ds)


def delayed_tower_counterfeit(p,K,other=None):
    _p(p);_k(K)
    if other is None:other=3 if p!=3 else 2
    _p(other)
    if p==other:raise LearningSourceError("second prime must differ")
    baseline=tuple(p**k for k in range(1,K+3))
    mutant=tuple(p**k if k<=K else p**k*other for k in range(1,K+3))
    if not all(mutant[j+1]%mutant[j]==0 for j in range(len(mutant)-1)):
        raise ArithmeticError("fake must itself be a compatible inverse tower")
    return {"honest":baseline,"counterfeit":mutant,
            "indistinguishable_through":K,"divergence_level":K+1}


def full_ring_tables(p,k,model):
    """Enumerate the ENTIRE finite arithmetic carrier, not just one path."""
    _p(p);_k(k)
    if model not in ('mixed','equal'):
        raise LearningSourceError('unknown source ring')
    N=p**k
    if N>64:raise LearningSourceError('complete exact table limited to <=64 elements')
    rows_add=[];rows_mul=[]
    for x in range(N):
        a=digits_of(x,p,k)
        add=[];mul=[]
        for y in range(N):
            b=digits_of(y,p,k)
            if model=='mixed':
                ap=mixed_add(a,b,p)[0]; mp=mixed_mul(a,b,p)
            else:
                ap=equal_add(a,b,p);mp=equal_mul(a,b,p)
            add.append(integer_of(ap,p));mul.append(integer_of(mp,p))
        rows_add.append(tuple(add));rows_mul.append(tuple(mul))
    return {'size':N,'add':tuple(rows_add),'mul':tuple(rows_mul),
            'source_model':model,'physical_source_authenticated':False}


def full_ring_homogeneous_projection(p,k,model):
    """Finite direct exhaustive proof oracle that ring projections commute."""
    _p(p);_k(k)
    if k<2:raise LearningSourceError('two successive stages required')
    high=full_ring_tables(p,k,model)
    low=full_ring_tables(p,k-1,model)
    M=p**(k-1)
    for operation in ('add','mul'):
        for x in range(high['size']):
            for y in range(high['size']):
                if high[operation][x][y]%M!=low[operation][x%M][y%M]:
                    raise ArithmeticError('source ring operation fails descent')
    return high['size']**2*2


def geometric_bt_ball_profile(p,radius):
    """Unlabelled rooted BT ball shell counts; same for Qp and Fp((t))."""
    _p(p);_nat(radius)
    if radius>16:raise LearningSourceError('finite graph census limit')
    counts=(1,)+tuple((p+1)*p**(r-1) for r in range(1,radius+1))
    return {'per_shell':counts,'total':sum(counts),
            'ring_characteristic_identifiable_from_unlabelled_graph':False}


def p_step_unipotent_probe(p,k,model,x=0):
    """S^p on an independently labelled ring-source orbit, not just tree shape."""
    _p(p);_k(k);_nat(x)
    if model not in ('mixed','equal'):
        raise LearningSourceError('unknown complete ring model')
    N=p**k
    x%=N
    one=digits_of(1,p,k)
    digits=digits_of(x,p,k)
    for _ in range(p):
        digits=(mixed_add(digits,one,p)[0] if model=='mixed'
                else equal_add(digits,one,p))
    return integer_of(digits,p)


def majority_failure_probability(error_probability,repetitions):
    """Exact rational probability that the majority of odd repeated binary reads is wrong.

    Assumes independent within-stage errors; stage-to-stage independence
    is not needed for union bounds or first Borel-Cantelli lemma.
    """
    from math import comb
    if type(error_probability) not in (Fraction,int):
        raise LearningSourceError('exact rational error probability required')
    e=Fraction(error_probability)
    if not 0<=e<=1:
        raise LearningSourceError('error probability outside [0,1]')
    if type(repetitions) is not int or repetitions<1 or repetitions%2!=1 or repetitions>301:
        raise LearningSourceError('odd sample count 1..301')
    return sum((Fraction(comb(repetitions,j))*e**j*(1-e)**(repetitions-j)
                for j in range(repetitions//2+1,repetitions+1)),Fraction())


def calibrated_majority_budget(stage,error_probability=Fraction(1,4),risk_budget=Fraction(1,8)):
    """Finite stage error <= delta 2^-stage; global union bound <=delta IF all stages run.

    No claim that the stated independent error rate is established by code.
    """
    _nat(stage,1)
    if stage>10:raise LearningSourceError('finite rational calibration stage budget')
    if type(error_probability) not in (Fraction,int) or type(risk_budget) not in (Fraction,int):
        raise LearningSourceError('exact rational calibration parameters required')
    e=Fraction(error_probability);delta=Fraction(risk_budget)
    if not 0<=e<Fraction(1,2) or not 0<delta<1:
        raise LearningSourceError('majority requires error <1/2 and 0<risk<1')
    target=delta/Fraction(2**stage)
    for repeats in range(1,302,2):
        err=majority_failure_probability(e,repeats)
        if err<=target:
            return {'stage':stage,'repetitions':repeats,
                    'actual_error_upper_bound':err,'allocated_error_budget':target,
                    'finite_calibration_not_physical_measurement':True}
    raise LearningSourceError('exact resource budget exhausted; no claim of impossibility')


def calibrated_ring_table_budget(p,k,error_probability=Fraction(1,4),total_risk=Fraction(1,8)):
    """Finite per-query majority budget for the ENTIRE level-k addition/multiplication tables.

    2*(p^k)^2 independent state-pair operations. Per-query failure <=
    total_risk * 2^-k / query_count. A double union bound (query/stage)
    shows probability >=1-total_risk of NO mislabeled table cell at ANY
    level in a theoretically indefinite campaign, conditional on sensor law.
    """
    _p(p);_k(k)
    count=2*p**(2*k)
    if count>10000:raise LearningSourceError('bounded finite table calibration budget')
    if type(total_risk) not in (Fraction,int):
        raise LearningSourceError('exact probability budget required')
    risk=Fraction(total_risk)
    if not 0<risk<1:raise LearningSourceError('risk must lie strictly between 0 and 1')
    report=calibrated_majority_budget(k,error_probability,risk/count)
    return {'level':k,'table_queries':count,
            'repetitions_per_query':report['repetitions'],
            'per_query_failure_bound':report['actual_error_upper_bound'],
            'total_level_error_bound':count*report['actual_error_upper_bound'],
            'allocated_level_error':risk/Fraction(2**k),
            'infinite_campaign_claim_conditional_on_independent_repeated_reads':True,
            'actual_measurements_performed':False}
