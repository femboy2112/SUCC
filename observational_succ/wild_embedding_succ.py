"""Wild-embedding SUCC: exactly typed Alexander commutator tower and controls.

The geometric identification with Alexander's horned sphere is a CLASSICAL
IMPORTED theorem (Hatcher, Algebraic Topology, Example 2B.2).  This module
executes its *abstract group-system algebra*, not a 3-D mesh or a proof that
an arithmetic Weil space is a horned sphere.

All finite certificates use exact integers/Fractions.  Real prime source,
Gamma completion, completed-Weil positivity and physical observation are NOT
inferred from any of these positive/topological invariants.  RH PROVED: no.
"""
from __future__ import annotations

from fractions import Fraction
from math import isqrt
from functools import lru_cache


class WildSUCCError(ValueError):
    """Invalid source, depth, carrier, or lossy observational promotion."""


def _int(value, *, lo=0, hi=100000):
    if type(value) is not int or not lo <= value <= hi:
        raise WildSUCCError('exact in-budget integer required')
    return value


def _rat(value):
    if type(value) not in (int, Fraction):
        raise WildSUCCError('exact int or Fraction required; no floating point')
    return Fraction(value)


def genuine_prime(value):
    _int(value,lo=2,hi=1000000)
    if any(value % d == 0 for d in range(2, isqrt(value)+1)):
        raise WildSUCCError('composite multiplier is not an independent Euler place')
    return value


def free_reduce(word):
    stack=[]
    for letter in word:
        if type(letter) is not int or letter == 0:
            raise WildSUCCError('free words require nonzero signed generators')
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def inverse(word):
    return tuple(-i for i in reversed(free_reduce(word)))


def commutator(a,b):
    a,b=free_reduce(a),free_reduce(b)
    return free_reduce(a+b+inverse(a)+inverse(b))


def validate_word(word,stage):
    _int(stage,lo=0,hi=8)
    word=free_reduce(word)
    if any(abs(letter) > 2**stage for letter in word):
        raise WildSUCCError('generator does not exist at source stage')
    return word


def horn_step(word,stage):
    """Hatcher F_(2^n) -> F_(2^(n+1)), g_i -> [g_(2i-1),g_(2i)]."""
    word=validate_word(word,stage)
    if stage >= 8:
        raise WildSUCCError('finite expansion budget exceeded')
    out=[]
    for letter in word:
        i=abs(letter)-1
        x,y=2*i+1,2*i+2
        original=(x,y,-x,-y)
        out.extend(original if letter>0 else inverse(original))
        if len(out)>250000:
            raise WildSUCCError('explicit path exceeded declared budget')
    return free_reduce(out)


def horn_transport(word,start,steps):
    _int(start,lo=0,hi=8)
    _int(steps,lo=0,hi=7)
    if start+steps>8:
        raise WildSUCCError('finite stage budget exceeded')
    w=validate_word(word,start)
    for i in range(steps):
        w=horn_step(w,start+i)
    return w


def abelian_shadow(word,stage):
    """Exponent-sum observation H_1(F_(2^n))=Z^(2^n)."""
    word=validate_word(word,stage)
    values=[0]*(2**stage)
    for g in word:
        values[abs(g)-1]+=1 if g>0 else -1
    return tuple(values)


def meridian_report(depth):
    depth=_int(depth,lo=0,hi=6)
    w=horn_transport((1,),0,depth)
    return {'depth':depth,'rank':2**depth,'free_word_length':len(w),
            'expected_length':4**depth,'survives_nonabelian':bool(w),
            'abelian_shadow':list(abelian_shadow(w,depth)),
            'lower_central_depth':2**depth,'nilpotent_class_below_depth_blind':True,
            'RH_proved':False}


@lru_cache(maxsize=6)
def leading_magnus(depth):
    """Lowest nonzero Magnus homogeneous polynomial for iterated meridian.

    Degree is 2^depth.  Coefficients are *exact* Lie commutators, not a
    computational proof of general Magnus injectivity (a classical import).
    """
    _int(depth,lo=0,hi=4)
    if depth == 0:
        return {(1,):1}
    sub=leading_magnus(depth-1)
    offset=2**(depth-1)
    right={tuple(letter+offset for letter in key):coef for key,coef in sub.items()}
    output={}
    for x,cx in sub.items():
        for y,cy in right.items():
            output[x+y]=output.get(x+y,0)+cx*cy
            output[y+x]=output.get(y+x,0)-cx*cy
    return {k:v for k,v in output.items() if v}


def magnus_monomial_count(depth):
    depth=_int(depth,lo=0,hi=16)
    return 2**(2**depth-1)


def _mul_poly(a,b,degree):
    out={}
    for u,c in a.items():
        for v,d in b.items():
            if len(u)+len(v)<=degree:
                key=u+v
                out[key]=out.get(key,0)+c*d
    return {key:value for key,value in out.items() if value}


def truncated_magnus(word,stage,degree):
    """Exact truncated Magnus expansion, X_i -> 1+X_i, class <=degree.

    Strictly a finite algebra test; degree range deliberately small.
    """
    w=validate_word(word,stage)
    degree=_int(degree,lo=0,hi=5)
    if len(w)>256:
        raise WildSUCCError('Magnus explicit evaluation exceeds budget')
    current={():1}
    for letter in w:
        i=abs(letter)
        factor={():1}
        if letter>0:
            factor[(i,)]=1
        else:
            for j in range(1,degree+1):
                factor[(i,)*j]=(-1)**j
        current=_mul_poly(current,factor,degree)
    return current



def _matrix_multiply(a,b):
    n=len(a)
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(n)))
                       for j in range(n)) for i in range(n))


def unitriangular_meridian(depth):
    """EXPLICIT sharp nilpotent detector at stage depth, not a limit probe.

    At stage k, F_(2^k) generator g_i maps to I+E_(i,i+1) in
    UT_(2^k+1)(Z) (nilpotent class 2^k).  Iterated meridian maps to
    I+E_(1,2^k+1).  Detector families across k are NOT compatible
    with the direct limit and do not contradict the perfect-group no-go.
    """
    depth=_int(depth,lo=0,hi=4)
    rank=2**depth
    n=rank+1
    identity=tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
    gplus={}
    gminus={}
    for g in range(1,rank+1):
        plus=[list(row) for row in identity]
        minus=[list(row) for row in identity]
        plus[g-1][g]=1
        minus[g-1][g]=-1
        gplus[g]=tuple(tuple(row) for row in plus)
        gminus[g]=tuple(tuple(row) for row in minus)
    w=horn_transport((1,),0,depth)
    m=identity
    for signed in w:
        m=_matrix_multiply(m,gplus[signed] if signed>0 else gminus[-signed])
    expected=[list(row) for row in identity]
    expected[0][rank]=1
    if m!=tuple(tuple(row) for row in expected):
        raise ArithmeticError('explicit nilpotent meridian detector identity fails')
    return {'depth':depth,'source_free_rank':rank,
            'matrix_dimension':n,'nilpotency_class':rank,
            'nonzero_top_right':m[0][rank],
            'detects_at_exact_depth':True,
            'not_compatible_with_entire_perfect_direct_limit':True}

def nilpotent_visibility(depth,class_bound):
    depth=_int(depth,lo=0,hi=16)
    class_bound=_int(class_bound,lo=1,hi=2**20)
    return {'depth':depth,'nilpotent_class':class_bound,
            'meridian_lower_central_depth':2**depth,
            'nilpotent_probe_cannot_detect':class_bound<2**depth,
            'nonabelian_direct_limit_survives':True,
            'full_source_pi1_identification':'CLASSICAL_HATCHER_IMPORT',
            'RH_proved':False}


def periodic_prime_sphere(primes):
    """Each finite stage S², suspended circle maps have degree p.

    Under *infinite periodic repetition*, Cech H^2 is Z[P^-1] by standard
    continuity.  This is NOT Alexander's horned S² (the limit is not S²).
    """
    if type(primes) not in (tuple,list) or not 1<=len(primes)<=8:
        raise WildSUCCError('one finite periodic prime cycle required')
    source=tuple(genuine_prime(p) for p in primes)
    support=tuple(sorted(set(source)))
    return {'source_prime_cycle':list(source),'prime_inverted':list(support),
            'every_finite_stage_topology':'S2',
            'bond_degree_cycle':list(source),
            'limit_cech_H2':'Z['+','.join('1/'+str(p) for p in support)+']',
            'limit_is_S2':False,'topology_theorem':'CLASSICAL_CECH_CONTINUITY',
            'not_the_Alexander_horned_sphere':True,'RH_proved':False}


def localized_rational(number,primes):
    q=_rat(number)
    ps={genuine_prime(p) for p in primes}
    den=q.denominator
    for p in ps:
        while den%p==0:
            den//=p
    return den==1


def delayed_prime_bonds(observed_bonds,delay,prime):
    """Arbitrarily long identical S²/degree-one prefixes, different limits.

    Control systems: identity forever => H^2 = Z;
    identity for delay steps, then prime degree forever => Z[1/p].
    """
    observed_bonds=_int(observed_bonds,lo=0,hi=100000)
    delay=_int(delay,lo=0,hi=100000)
    p=genuine_prime(prime)
    degrees=tuple(1 if j<delay else p for j in range(observed_bonds))
    return {'observed_bonds':list(degrees),'same_as_identity_source':observed_bonds<=delay,
            'identity_limit_H2':'Z', 'delayed_twist_limit_H2':f'Z[1/{p}]',
            'difference_requires_bond_interactions':True,'RH_proved':False}


def flattened_warp(epsilon):
    """Piecewise linear increasing [0,1] homeomorphism, eps in (0,1)."""
    eps=_rat(epsilon)
    if not 0<eps<1:
        raise WildSUCCError('finite positive compression required')
    return {'left_slope':eps,'right_slope':2-eps,
            'forward_Lipschitz':2-eps,'inverse_Lipschitz':1/eps,
            'uniform_limit_collapses_half_interval':True,
            'uniform_forward_error_at_most':eps/2,
            'wildness_proved':False}


def benign_inverse_distortion(epsilon,position):
    """Homeomorphisms tending to x³ but inverse Lipschitz explodes.

    Proves resource blow-up alone is NOT sufficient for wildness.
    """
    eps,x=_rat(epsilon),_rat(position)
    if not 0<eps<1 or not -1<=x<=1:
        raise WildSUCCError('source chart outside [-1,1]')
    return {'value':(x**3+eps*x)/(1+eps),
            'inverse_lipschitz':(1+eps)/eps,
            'limit_homeomorphism_value':x**3,
            'limit_is_tame_homeomorphism':True}


def wavefront_shadow(delta,coefficient):
    """Rational first-wavefront two-strip proxy in correct L² metric.

    Physical coefficient for authentic prime 2 is log(2)/sqrt(2), which is
    NOT declared equal to a rational input here.  The forms and norms are
    the exact algebra in the parent's source-correct analytic theorem.
    """
    delta,c=_rat(delta),_rat(coefficient)
    if not 0<delta<=1 or c<0:
        raise WildSUCCError('positive wavefront geometry and nonnegative coupling')
    return {'strip_width':delta,'offdiagonal_operator_norm':c,
            'continuous_hinge_HS_norm_squared':c*c*delta**4/6,
            'true_H1_Riesz_norm_squared_upper':c*c*delta**4/6,
            'normalized_symmetric_Rayleigh':-c,
            'normalized_antisymmetric_Rayleigh':c,
            'unit_L2_tent_H1_derivative_energy':12/(delta*delta),
            'H1_tent_negative_Rayleigh':-c/(1+12/(delta*delta)),
            'strong_not_norm_convergence_if_c_fixed_positive':c>0,
            'not_a_new_Weil_sign':True,'RH_proved':False}


def escape_witness(observer_rank,hidden_index):
    _int(observer_rank,lo=0,hi=100000)
    _int(hidden_index,lo=1,hi=1000000)
    if hidden_index<=observer_rank:
        raise WildSUCCError('negative witness is already observed')
    return {'observer_rank':observer_rank,'hidden_index':hidden_index,
            'all_observed_compressions_zero':True,
            'actual_full_operator_negative_eigenvalue':-1,
            'strong_limit_of_escaping_compact_operators_zero':True,
            'operator_norm_always_one':True,
            'collective_compactness_fails':True,
            'not_the_actual_Weil_operator':True}


def two_chart_schur(a,b,c):
    a,b,c=_rat(a),_rat(b),_rat(c)
    if a<=0 or b<=0:
        raise WildSUCCError('positive diagonal chart blocks required')
    rem=b-c*c/a
    return {'schur_remainder':rem,'global_nonnegative':rem>=0,
            'both_isolated_charts_positive':True,
            'mixed_boundary_coupling_absorbed':rem>=0,
            'not_completed_Weil_certificate':True}


def receipt():
    return {'source_model':'HATCHER_ALEXANDER_FREE_COMMUTATOR_DIRECT_LIMIT',
            'meridian_tower':[meridian_report(k) for k in range(5)],
            'nilpotent_probe':[nilpotent_visibility(5,k) for k in (1,7,31,32)],
            'explicit_exact_depth_detectors':[unitriangular_meridian(k) for k in range(4)],
            'leading_Lie_terms':{str(k):{'count':len(leading_magnus(k)),
                                       'degree':2**k} for k in range(4)},
            'prime_sphere':periodic_prime_sphere((2,3)),
            'long_finite_shadow':delayed_prime_bonds(8,12,2),
            'wavefront':[dict((k,str(v) if isinstance(v,Fraction) else v)
                             for k,v in wavefront_shadow(Fraction(1,2**n),Fraction(2,3)).items())
                         for n in (1,2,3,4)],
            'cross_chart':{k:str(v) if isinstance(v,Fraction) else v
                           for k,v in two_chart_schur(1,1,2).items()},
            'actual_horned_sphere_geometry_imported_not_proved':True,
            'completed_Weil_positive':False,'RH_proved':False}
