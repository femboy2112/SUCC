"""Hilbert dyadic carrier and rigorously typed Suzuki/Weil finite observers.

Classical Hilbert traversal, area quadrature, authenticated Suzuki midpoint source
transport and shifted Schur control. The parent source is checked by Git blob.
No unshifted sign theorem, completed adelic curve, or RH claim is made.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha1
from math import gcd, isqrt
from pathlib import Path

ORIGINAL_SUZUKI_SOURCE_BLOB = "0cc8510b71d178fc79e8d410a86d8b6014cf9178"
SOURCE_BRANCH_MAIN = "03db44203147a7b28d445bb9f970fa71360e78c4"

class HilbertAtlasError(ValueError):
    pass


def q(x):
    if type(x) not in (int, F):
        raise HilbertAtlasError("only original exact integer/Fraction observations permitted")
    return F(x)


def _depth(d):
    if type(d) is not int or not 0 <= d <= 7:
        raise HilbertAtlasError("Hilbert depth outside bounded observer 0..7")
    return d


def _rot(s, x, y, rx, ry):
    if ry == 0:
        if rx == 1:
            x, y = s - 1 - x, s - 1 - y
        x, y = y, x
    return x, y


def hilbert_xy(depth, index):
    """Standard orientation, zero-based Hilbert visit index to dyadic tile."""
    _depth(depth)
    n = 1 << depth
    if type(index) is not int or not 0 <= index < n*n:
        raise HilbertAtlasError("index outside declared Hilbert row")
    x = y = 0
    s, t = 1, index
    while s < n:
        rx = 1 & (t // 2)
        ry = 1 & (t ^ rx)
        x, y = _rot(s, x, y, rx, ry)
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y


def hilbert_index(depth, x, y):
    """Exact inverse for the finite tile order, no analytic continuum inversion."""
    _depth(depth)
    n = 1 << depth
    if type(x) is not int or type(y) is not int or not (0 <= x < n and 0 <= y < n):
        raise HilbertAtlasError("tile coordinate outside declared dyadic square")
    d, s = 0, n // 2
    while s:
        rx, ry = int(bool(x & s)), int(bool(y & s))
        d += s*s*((3*rx) ^ ry)
        x, y = _rot(s, x, y, rx, ry)
        s //= 2
    return d


@lru_cache(maxsize=8)
def hilbert_cells(depth):
    _depth(depth)
    return tuple(hilbert_xy(depth, i) for i in range(4**depth))


def geometry_receipt(depth):
    cells = hilbert_cells(depth)
    n = 1 << depth
    unique = len(set(cells)) == len(cells) == n*n
    adjacent = all(abs(x[0]-y[0])+abs(x[1]-y[1]) == 1
                   for x, y in zip(cells, cells[1:]))
    parent = depth == 0 or all(
        (cells[4*i+k][0]//2, cells[4*i+k][1]//2) == hilbert_xy(depth-1, i)
        for i in range(4**(depth-1)) for k in range(4))
    return {"depth": depth, "visited_tiles": len(cells),
            "uniform_area_per_tile": str(F(1, n*n)),
            "unique": unique, "adjacent": adjacent,
            "parent_refinement": parent, "physical_infinity_actualized": False}



def hilbert_point_enclosure(time,depth):
    """One lawful finite SUCC prefix bounds its mathematical Hilbert-limit point.

    Nested closed dyadic tiles shrink at rate 2^-depth; this reports an
    enclosing tile, not an infinitely completed physical observation.
    """
    depth=_depth(depth)
    time=q(time)
    if not 0<=time<=1:
        raise HilbertAtlasError("source time outside [0,1]")
    n=1<<depth
    index=min(4**depth-1, (time*4**depth).numerator//(time*4**depth).denominator)
    x,y=hilbert_xy(depth,index)
    return {"time":time,"depth":depth,"index":index,
            "x_interval":(F(x,n),F(x+1,n)),
            "y_interval":(F(y,n),F(y+1,n)),
            "l_infinity_error_radius":F(1,n),
            "euclidean_diameter_strict_upper":F(2,n),
            "source_state_physically_observed_at_infinity":False}


def hilbert_martingale_l2_error_bound(depth,lipschitz):
    """Proved regularity budget: ||f∘H-E_n(f∘H)||₂ < 2 Lip(f)2^-n.

    Rate applies ONLY when a valid Euclidean Lipschitz budget is available.
    Arbitrary L2 original-source data has strong L2 convergence but no rate.
    """
    depth=_depth(depth)
    L=q(lipschitz)
    if L<0:raise HilbertAtlasError("negative Lipschitz budget")
    return {"depth":depth,"rigorous_l2_error_upper":F(2)*L/(1<<depth),
            "requires_external_source_lipschitz_proof":True,
            "L2_convergence_for_arbitrary_source_has_no_uniform_rate":True}


def hilbert_average(depth, function):
    """Exact source-neutral area quadrature of a declared rational function."""
    n = 1 << _depth(depth)
    return sum((q(function(F(2*i+1,2*n), F(2*j+1,2*n)))
                for i,j in hilbert_cells(depth)), F()) / (n*n)


def hilbert_lipschitz_enclosure(depth, function, lx, ly):
    """Conditional on *independently proved* coordinate Lipschitz bounds."""
    lx, ly = q(lx), q(ly)
    if lx < 0 or ly < 0:
        raise HilbertAtlasError("signed Lipschitz claim")
    center = hilbert_average(depth, function)
    err = (lx + ly) / (2*(1 << depth))
    return {"center": center, "error_bound": err,
            "lower": center-err,"upper": center+err,
            "Lipschitz_condition_is_input_not_inferred": True}


def _prime_power(n):
    if type(n) is not int or not 2 <= n <= 100000:
        raise HilbertAtlasError("unsupported original arithmetic address")
    p = next((d for d in range(2,isqrt(n)+1) if n%d == 0),n)
    k = 0
    rest = n
    while rest%p == 0:
        rest //= p
        k += 1
    return (p,k) if rest == 1 else None


def _log_unit(x, count=30):
    if not F(1) <= x <= F(2):
        raise HilbertAtlasError("log unit 1..2 only")
    z = (x-1)/(x+1)
    terms = sum((2*z**(2*j+1)/F(2*j+1) for j in range(count)), F())
    tail = 2*z**(2*count+1)/(F(2*count+1)*(1-z*z))
    return terms, terms+tail


def log_integer_interval(n):
    if type(n) is not int or not 1 <= n <= 100000:
        raise HilbertAtlasError("bounded integer log source")
    u=F(n); power=0
    while u >= 2:
        u/=2
        power+=1
    unit=_log_unit(u)
    two=_log_unit(F(2))
    return unit[0]+power*two[0],unit[1]+power*two[1]


def _dist_interval(xlo,xhi,ylo,yhi):
    low,high = xlo-yhi,xhi-ylo
    minimum = F(0) if low <= 0 <= high else min(abs(low),abs(high))
    return minimum, max(abs(low),abs(high))


def prime_wavefront_tiles(depth, a, prime_power=2):
    """Hilbert-ordered classification of authentic von Mangoldt hinge cells.

    Does NOT make their signed form positive; checks source primality at n=p^k.
    """
    _depth(depth)
    a=q(a)
    if not 0<a<=2:raise HilbertAtlasError("positive interval radius <=2")
    pp = _prime_power(prime_power)
    if pp is None:
        raise HilbertAtlasError("composite fake Euler impulse rejected")
    l0,l1 = log_integer_interval(prime_power)
    n = 1 << depth
    h = 2*a/n
    rows=[]
    for x,y in hilbert_cells(depth):
        xlo,xhi = -a+x*h,-a+(x+1)*h
        ylo,yhi = -a+y*h,-a+(y+1)*h
        d0,d1 = _dist_interval(xlo,xhi,ylo,yhi)
        tag = "inactive" if d1<=l0 else "active" if d0>=l1 else "threshold"
        rows.append(tag)
    counts={v:rows.count(v) for v in ("inactive","active","threshold")}
    return {"depth":depth,"p":pp[0],"exponent":pp[1],
            "prime_power":prime_power,"log_interval":(l0,l1),
            "cell_width":h,"counts":counts,
            "ordered_labels":tuple(rows),
            "source": "genuine_prime_power_hinge_only_not_full_Weil"}



def compressed_prime_trace_blindspot(depth,a,prime_power=2):
    """A genuine log-prime shift can have zero finite-step diagonal trace
    while remaining a nonzero off-diagonal source operator.

    This is NOT Connes's trace formula; it is an obstruction to identifying
    naive Hilbert/step matrix traces with arithmetic prime-orbit distributions.
    """
    _depth(depth)
    a=q(a)
    if a<=0:raise HilbertAtlasError('positive interval needed')
    pp=_prime_power(prime_power)
    if pp is None:raise HilbertAtlasError('fake primitive prime source rejected')
    lo,hi=log_integer_interval(prime_power)
    h=2*a/(1<<depth)
    if hi<h:
        # Every diagonal overlap is (h-ell)/h, with interval uncertainty.
        lower=(1<<depth)*(1-hi/h)
        upper=(1<<depth)*(1-lo/h)
        trace_interval=(lower,upper)
        trace_zero=False
    elif lo>=h:
        trace_interval=(F(),F())
        trace_zero=True
    else:
        trace_interval=(F(),(1<<depth)*(1-lo/h))
        trace_zero=False
    return {'depth':depth,'source_prime_power':prime_power,
            'actual_genuine_prime':pp[0],
            'naive_step_basis_translation_trace_interval':trace_interval,
            'trace_identically_zero':trace_zero,
            'actual_shift_nonzero_on_interval':hi<2*a,
            'Connes_trace_distribution_identified':False,
            'the_prime_term_is_offdiagonal_not_trace_visible':trace_zero and hi<2*a}


def hilbert_prime_index_mutation(depth,index,multiplier):
    """Deliberate toy clock, not arithmetic V_p on the original integer carrier.

    Hilbert prefixes use floor(index/4), unlike low-digit mod-4 clock maps.
    """
    _depth(depth)
    if depth < 2:raise HilbertAtlasError("require a child and parent refinement")
    n = 4**depth
    if type(index) is not int or not 0 <= index < n:
        raise HilbertAtlasError("bad Hilbert index")
    if type(multiplier) is not int or not 2 <= multiplier <= 10000:
        raise HilbertAtlasError("bad affine toy multiplier")
    child=(multiplier*index)%n
    actual_parent=child//4
    naive_parent=(multiplier*(index//4))%(n//4)
    return {"child":child,"actual_parent":actual_parent,
            "naive_parent":naive_parent,"refinement_square_commutes":actual_parent==naive_parent,
            "invertible_on_index_clock":gcd(multiplier,n)==1,
            "image_count":n//gcd(multiplier,n),
            "toy_index_action_not_authenticated_original_FUCC":True}


def invisible_negative_to_level(depth):
    """Exact finite even Toeplitz countermodel on level-(depth+1) cells.

    K_ij=-(-1)^(i-j)/m has negative eigenvalue -1 on the alternating
    vector; compression to each adjacent pair average at coarser level is ZERO.
    Not the genuine prime/Gamma Suzuki source.
    """
    _depth(depth)
    m = 1 << (depth+1)
    u = tuple(F((-1)**i) for i in range(m))
    k = tuple(tuple(-u[i]*u[j]/m for j in range(m)) for i in range(m))
    coarse = tuple(tuple(sum((k[2*i+a][2*j+b] for a in (0,1) for b in (0,1)),F())/2
                         for j in range(m//2)) for i in range(m//2))
    return {"depth":depth,"coarse_block_zero":all(v==0 for row in coarse for v in row),
            "quadratic_unit_alternating":sum((u[i]*k[i][j]*u[j]
                       for i in range(m) for j in range(m)),F())/m,
            "original_arithmetic_source":False,"signed_even_difference_kernel":True}


def shift_projection_defect(theta):
    """Squared norm lost by shifting one normalized step cell fractionally."""
    theta=q(theta)
    if not 0<=theta<=1:raise HilbertAtlasError("fractional shift outside 0..1")
    return 2*theta*(1-theta)


def _pinned_source():
    from . import source_weil_hierarchy as source
    raw=Path(source.__file__).read_bytes()
    digest=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if digest != ORIGINAL_SUZUKI_SOURCE_BLOB:
        raise HilbertAtlasError("Suzuki original source blob drift: stop")
    return source


def authentic_hilbert_rayleigh(depth,vec,a=F(1,2),J=3):
    """Actual signed SOURCE-SUZUKI finite-state Rayleigh interval, no sign guess.

    vec are orthonormal cell-basis coefficients; sum vec=0 is mean-zero.
    Visits every two-cell interaction in Hilbert order, charges full source error.
    """
    depth=_depth(depth)
    n=1<<depth
    if depth<1 or n>16 or type(vec) not in (tuple,list) or len(vec)!=n:
        raise HilbertAtlasError("authentic limited source Hilbert depth 1..4")
    v=tuple(q(x) for x in vec)
    if sum(v,F())!=0 or not any(v):
        raise HilbertAtlasError("source vector must be nonzero and mean-zero")
    source=_pinned_source()
    st=source.stage(q(a),J,n)
    source._authenticated(st)
    total=sum((v[i]*st.center[i][j]*v[j] for i,j in hilbert_cells(depth)),F())
    check=sum((v[i]*st.center[i][j]*v[j] for i in range(n) for j in range(n)),F())
    if total!=check:raise ArithmeticError("Hilbert visit lost a signed source interaction")
    energy=sum((x*x for x in v),F())
    error=st.norm_error*energy
    return {"depth":depth,"J":J,"a":q(a),
            "source":st.source,"original_source_blob":ORIGINAL_SUZUKI_SOURCE_BLOB,
            "rational_center":total,"signed_absolute_error":error,
            "rayleigh_lower":(total-error)/energy,
            "rayleigh_upper":(total+error)/energy,
            "negative_witness_certified":total+error<0,
            "positive_on_whole_space_certified":False,"RH_proved":False}


def authentic_hilbert_shifted_schur_budget(depth,lam,J=3):
    """True G coupling over low=span{first 30 Legendre, n step functions}.

    At a=1/2 its high complement is inside the 30-moment-null positive space.
    Source proof of D>=369/10000 K is imported from integrated AMW-06B.
    The Hilbert dyadic finite source approx has range in the step subspace:
    ||B||<=eps; 0<=B(D+lam)^(-1)B* <=eps²/lam.
    This does NOT certify the low Schur sign.
    """
    depth=_depth(depth)
    if not 1 <= depth <= 4:raise HilbertAtlasError("source stage dyadic N 2..16")
    lam=q(lam)
    if lam<=0:raise HilbertAtlasError("regularized inverse needs lambda>0")
    source=_pinned_source()
    from .suzuki_moment_schur import source_moment30_certificate
    high_proof=source_moment30_certificate()
    if (high_proof['strict_high_L2_coercivity']!=str(F(369,10000))
            or high_proof['vanishing_moments']!=30
            or high_proof['RH_proved'] is not False):
        raise HilbertAtlasError('original high-sector theorem proof witness drift')
    st=source.stage(F(1,2),J,1<<depth)
    source._authenticated(st)
    eps=source.honest_spatial_error(st)+source.authentic_positive_gamma_tail_norm(J)
    return {"a":F(1,2),"depth":depth,"J":J,"lambda":lam,
            "source_operator_norm_error_upper":eps,
            "cross_operator_norm_upper":eps,
            "shifted_high_resolvent_penalty_upper":eps*eps/lam,
            "high_sign_from_authentic_AMW_06B":True,
            "high_relative_K_gap":F(369,10000),
            "source_30_moment_ledger":high_proof['parent_theorem'],
            "Hilbert_order_not_a_new_arithmetic_source":True,
            "unshifted_lambda_zero_certified":False,"RH_proved":False}



def classical_first_window_carleman_range_budget():
    """Entirely rational paper-derived bounds for the ORIGINAL source, a=1/2.

    Original g includes all authentic Gamma/prime/pole/contact terms. For |t|<=1
    derivative is W^{1,1} with ||g'||_1<24, g(0)=0, ||G||<12.
    30 orthonormal nonconstant Legendre functions e_k=sqrt(2k+1)P_k(2x)
    have sum ||e'_k||^2 =922560<961^2.
    Thus ||(QGx)'|| <=11556||x|| on the low-30 sector.
    The original high source theorem D>=369/10000 *QKQ gives
       lim_{lambda->0} <B*x,(D+lambda)^-1 B*x>
       <=(10000/369)*11556^2 ||x||^2.
    Actual LOW SHORTED MATRIX SIGN NOT VERIFIED.
    """
    gamma_derivative_one_side=F(5)
    pole_derivative_one_side=F(2)
    contact_derivative_one_side=F(4)
    true_prime_derivative_one_side=F(1)
    one_side=sum((gamma_derivative_one_side,pole_derivative_one_side,
                  contact_derivative_one_side,true_prime_derivative_one_side),F())
    if one_side!=12:raise ArithmeticError('original source derivative bound misassembled')
    projector_derivative_squared=sum((2*(2*k+1)*k*(k+1) for k in range(1,31)),0)
    if projector_derivative_squared!=922560 or projector_derivative_squared>=961*961:
        raise ArithmeticError('Legendre projector bound does not check')
    derivative_gain=24+961*12
    if derivative_gain!=11556:raise ArithmeticError('source range budget arithmetic drift')
    kappa=F(369,10000)
    return {"a":F(1,2),"original_screw_derivative_L1_strict_upper":F(24),
            "original_screw_kernel_Linfty_strict_upper":F(12),
            "original_compact_G_operator_norm_strict_upper":F(12),
            "legendre_30_derivative_HS_norm_squared":projector_derivative_squared,
            "legendre_projection_derivative_gain_strict_upper":F(961),
            "original_low_to_high_H1_gain_strict_upper":F(derivative_gain),
            "high_relative_Neumann_gap":kappa,
            "uniform_lambda_to_zero_cross_resolvent_upper":F(derivative_gain**2)/kappa,
            "range_condition_proved_conditional_on_original_high_theorem":True,
            "shorted_low_sign_proved":False,"RH_proved":False}


def original_source_cross_derivative_tail_budget(J):
    """Authentic Gamma-rung remainder in the 30-mode CROSS H1 calculation.

    Original finite screw Gamma source: omitted g-g_J has
    ||g-g_J||infty <= gamma_tail(J) and ||(g-g_J)'||_L1<=2 gamma_tail(J)
    on differences [-1,1]. Thus for x in the 30-mode low space,
    ||(Q(G-G_J)x)'|| <= (2+961)gamma_tail(J)||x||.
    This makes the true R_0 upper shorting comparison computable in
    principle from finite J derivative cross-Gram data; the latter are NOT
    evaluated or signed here.
    """
    if type(J) is not int or not 1<=J<=100000:
        raise HilbertAtlasError('positive finite source Gamma rung budget')
    den=4*J+1
    t=F(1,den)+F(4,den*den)
    delta=963*t
    return {"J":J,"omitted_original_Gamma_kernel_Linfty_upper":t,
            "omitted_original_Gamma_derivative_L1_upper":2*t,
            "source_high_cross_derivative_gain_upper":delta,
            "finite_J_true_derivative_Gram_computed":False,
            "unshifted_source_range_proved_by_uniform_analytic_argument":True,
            "low_short_sign_verified":False,"RH_proved":False}


def authenticated_first_window_range_certificate():
    """Pin the genuine original source and independently replay AMW-06B proof.

    This is a proof-of-RANGE/FINITE cross energy, not a proof of sign.
    """
    source=_pinned_source()
    source.assert_original_source_tape()
    from .suzuki_moment_schur import source_moment30_certificate
    high=source_moment30_certificate()
    value=classical_first_window_carleman_range_budget()
    if (high['vanishing_moments']!=30 or
        high['strict_high_L2_coercivity']!=str(value['high_relative_Neumann_gap']) or
        high['RH_proved'] is not False):
        raise HilbertAtlasError('original high-source signed theorem missing')
    return dict(value, original_source_pinned_blob=ORIGINAL_SUZUKI_SOURCE_BLOB,
                high_source_proof_replay=high['parent_theorem'],
                original_source_prime_tape_authenticated=True)


def hilbert_diagonal_completion_budget(level):
    """Analytic (not executable current source-stage) diagonal Schur schedule.

    Assume on a=1/2 genuine Suzuki source the cell evaluator can achieve
    a rigorous kernel rounding radius eta<=N^-2, and J=N=2^level.
    Then genuine gamma norm tail and source Lipschitz bound imply
      ||G-G_(J,N)|| <= ((23+level)/2 + 2/N)/N,
      lambda=1/N, cross shorting <= ((23+level)/2+2/N)^2/N ->0.
    The *low* source spectral sign is still wholly unproved.
    Current stage software budget only goes up to J=36,N=24.
    """
    if type(level) is not int or not 1<=level<=64:
        raise HilbertAtlasError('analytic dyadic schedule level 1..64')
    N=1<<level
    lam=F(1,N)
    eps=(F(23+level,2)+F(2,N))/N
    penalty=eps*eps/lam
    return {'level':level,'J':N,'N':N,'lambda':lam,
            'source_rounding_precision_assumption':F(1,N*N),
            'operator_error_upper_conditional':eps,
            'shifted_cross_penalty_upper_conditional':penalty,
            'all_test_low_schur_sign_verified':False,
            'unshifted_zero_lambda_verified':False,
            'current_source_stage_software_supports_this_level':N<=24 and N<=36,
            'RH_proved':False}


def finite_schur_control(a,b,d,lam,eps):
    """Exact 2x2 toy; proof contract uses d>=0 and abs(b)<=eps."""
    a,b,d,lam,eps=map(q,(a,b,d,lam,eps))
    if d<0 or lam<=0 or eps<abs(b):raise HilbertAtlasError("invalid signed low/high premise")
    penalty=b*b/(d+lam)
    if penalty>eps*eps/lam:raise ArithmeticError("resolvent cross contract failed")
    return {"exact_schur":a+lam-penalty,"certified_schur_lower":a+lam-eps*eps/lam,
            "exact_coupling_penalty":penalty,"upper_coupling_penalty":eps*eps/lam,
            "zero_shift_verified":False}


def _jsonable(value):
    if isinstance(value,F):return str(value)
    if isinstance(value,dict):return {k:_jsonable(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [_jsonable(v) for v in value]
    return value


def receipt():
    return {"main_parent":SOURCE_BRANCH_MAIN,
            "geometry":{str(j):geometry_receipt(j) for j in range(1,5)},
            "quadrature_exact_linear":str(hilbert_average(4,lambda x,y:x+y)),
            "finite_to_complete_example": _jsonable(hilbert_point_enclosure(F(1,5),5)),
            "wavefront_a_half":{str(j):prime_wavefront_tiles(j,F(1,2),2)["counts"]
                                 for j in (2,3,4,5)},
            "p3_refinement_negative_control":hilbert_prime_index_mutation(2,2,3),
            "prime2_trace_blindspot":_jsonable(compressed_prime_trace_blindspot(4,F(1,2),2)),
            "p2_nonunit_control":hilbert_prime_index_mutation(2,2,2),
            "hidden_negative_level_3":{k:str(v) if isinstance(v,F) else v
                                        for k,v in invisible_negative_to_level(3).items()},
            "half_cell_commutator_sq":str(shift_projection_defect(F(1,2))),
            "unshifted_range_analytic_certificate":_jsonable(classical_first_window_carleman_range_budget()),
            "original_Gamma_cross_H1_tail": {str(j):_jsonable(original_source_cross_derivative_tail_budget(j))
                                           for j in (2,8,32,128)},
            "dyadic_diagonal_plan": {str(j):_jsonable(hilbert_diagonal_completion_budget(j))
                                     for j in (4,8,12,16)},
            "no_source_Weil_sign_or_RH_proof":True}
