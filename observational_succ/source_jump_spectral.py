"""Source-generated Gamma/FUCC spectral partition, exact finite polar Schur, and
an authenticated **bound**, not a computation, of the true Suzuki projector.

The finite matrix solver is an exact rational MODEL.  It never promotes its
spectrum to the original completed Weil source.  The source adapter verifies
original source constants and certifies a coarse spectral-rank/gap budget.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
from dataclasses import dataclass


class JumpSpectralError(ValueError):
    pass


def rat(x):
    if type(x) not in (int, F):
        raise JumpSpectralError('only exact int/Fraction; floats and bool disallowed')
    return F(x)


def vec(v, n=None):
    x = tuple(rat(z) for z in v)
    if not x or (n is not None and len(x) != n):
        raise JumpSpectralError('nonempty exactly dimensioned vector required')
    return x


def matrix(m, n=None):
    x = tuple(tuple(rat(z) for z in row) for row in m)
    if not x or (n is not None and len(x) != n) or any(len(row) != len(x[0]) for row in x):
        raise JumpSpectralError('complete rational matrix required')
    return x


def eye(n):
    return tuple(tuple(F(int(i == j)) for j in range(n)) for i in range(n))


def zero(n):
    return tuple(tuple(F() for j in range(n)) for i in range(n))


def add(a, b, factor=F(1)):
    factor = rat(factor)
    if not a or len(a) != len(b) or any(len(u) != len(v) for u, v in zip(a,b)):
        raise JumpSpectralError('matrix shapes do not match')
    return tuple(tuple(x + factor*y for x,y in zip(u,v)) for u,v in zip(a,b))


def scale(a, factor):
    q = rat(factor)
    return tuple(tuple(q*x for x in row) for row in a)


def mul(a, b):
    if not a or not b or len(a[0]) != len(b):
        raise JumpSpectralError('matrix multiplication shape')
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), F())
                 for j in range(len(b[0]))) for i in range(len(a)))


def transpose(a):
    return tuple(tuple(z for z in row) for row in zip(*a))


def apply(a, v):
    return tuple(sum((x*y for x,y in zip(row,v)),F()) for row in a)


def dot(v, w):
    return sum((x*y for x,y in zip(v,w)),F())


def outer(v, w=None):
    w = v if w is None else w
    return tuple(tuple(a*b for b in w) for a in v)


def symmetric(a):
    return len(a) == len(a[0]) and a == transpose(a)


def witness(a):
    """Exact non-PSD witness x with x^T A x < 0, or None iff A is PSD.

    Recursive complete-the-square with no eigenvalue approximations.
    """
    a = matrix(a)
    n = len(a)
    if any(len(row) != n for row in a) or not symmetric(a):
        raise JumpSpectralError('real symmetric quadratic form required')
    if n == 1:
        return (F(1),) if a[0][0] < 0 else None
    for i in range(n):
        if a[i][i] < 0:
            return tuple(F(int(k == i)) for k in range(n))
    for i in range(n):
        if a[i][i] == 0:
            for j in range(n):
                if a[i][j]:
                    t = -a[i][j]/(abs(a[j][j])+1)
                    x = [F() for _ in range(n)]
                    x[i] = 1
                    x[j] = t
                    assert dot(x,apply(a,x)) < 0
                    return tuple(x)
    if all(a[i][i] == 0 for i in range(n)):
        return None
    p = next(i for i in range(n) if a[i][i] > 0)
    order = [p]+[i for i in range(n) if i != p]
    aa = tuple(tuple(a[i][j] for j in order) for i in order)
    d = aa[0][0]
    b = tuple(aa[0][j] for j in range(1,n))
    short = tuple(tuple(aa[i][j] - b[i-1]*b[j-1]/d for j in range(1,n))
                  for i in range(1,n))
    y = witness(short)
    if y is None:
        return None
    x_perm = (-dot(b,y)/d,)+y
    x = [F() for _ in range(n)]
    for idx,val in zip(order,x_perm):
        x[idx] = val
    assert dot(x,apply(a,x)) < 0
    return tuple(x)


def is_psd(a):
    return witness(a) is None


def exact_spectral_projectors(operator, eigenvalues):
    """Lagrange interpolation of spectral projectors, accepting only a VERIFIED
    annihilating rational polynomial on a real symmetric matrix.
    """
    op = matrix(operator)
    n = len(op)
    if any(len(row)!=n for row in op) or not symmetric(op):
        raise JumpSpectralError('symmetric source generator required')
    values = tuple(rat(q) for q in eigenvalues)
    if not values or len(set(values)) != len(values) or any(q < 0 for q in values):
        raise JumpSpectralError('distinct nonnegative rational eigenvalue claims')
    ident = eye(n)
    product = ident
    for lam in values:
        product = mul(product,add(op,ident,-lam))
    if product != zero(n):
        raise JumpSpectralError('claimed spectral values do not annihilate source operator')
    proj = {}
    for lam in values:
        result = ident
        for mu in values:
            if mu != lam:
                result = mul(result,scale(add(op,ident,-mu),1/(lam-mu)))
        if not symmetric(result) or mul(result,result) != result or not is_psd(result):
            raise JumpSpectralError('false spectral projector')
        if mul(op,result) != scale(result,lam):
            raise JumpSpectralError('projector not an actual source eigenprojector')
        proj[lam] = result
    if sum_matrices(tuple(proj.values()),n) != ident:
        raise JumpSpectralError('incomplete spectral decomposition')
    return proj


def sum_matrices(mats,n):
    out=zero(n)
    for mat in mats:
        out=add(out,mat)
    return out


def exact_polar_schur(operator, eigenvalues, contact, cosh, sinh, cutoff, reflection=None):
    """EXACT finite rational spectral low/high short; NOT original infinite Weil.

    H = L_plus - contact*I +2|cosh><cosh| -2|sinh><sinh|.
    A guaranteed positive high block makes the short exact.  The two polar
    channels are orthogonal by reflection and independently renormalize.
    """
    L=matrix(operator)
    n=len(L)
    if any(len(row)!=n for row in L) or not symmetric(L):
        raise JumpSpectralError('symmetric generator')
    m=rat(contact)
    c=vec(cosh,n)
    s=vec(sinh,n)
    cutoff=rat(cutoff)
    if m<0 or cutoff <= m+2*dot(s,s):
        raise JumpSpectralError('cutoff does not certify high positivity')
    if not is_psd(L):
        raise JumpSpectralError('positive Gamma+FUCC source generator required')
    if reflection is not None:
        ref=matrix(reflection,n)
        if any(len(row)!=n for row in ref) or not symmetric(ref) or mul(ref,ref)!=eye(n) or mul(ref,L)!=mul(L,ref):
            raise JumpSpectralError('reflection symmetry must be real, exact, and source-commuting')
        if apply(ref,c)!=c or apply(ref,s)!=tuple(-x for x in s):
            raise JumpSpectralError('original cosh even/sinh odd parity misidentified')
    if dot(c,s):
        raise JumpSpectralError('original polar vectors not orthogonal: cannot split parity')
    pr=exact_spectral_projectors(L,eigenvalues)
    # Ordinary orthogonality of c,s is NOT enough.  Require their orthogonality
    # in EACH eigenvalue sector: only then every high resolvent cross vanishes.
    if any(dot(c,apply(pp,s)) != 0 for pp in pr.values()):
        raise JumpSpectralError('polar channels mix inside a jump eigenspace')
    P=sum_matrices(tuple(t for lam,t in pr.items() if lam<=cutoff),n)
    Q=add(eye(n),P,-1)
    cp,sp=apply(P,c),apply(P,s)
    cq,sq=apply(Q,c),apply(Q,s)
    alpha_c=sum((dot(cq,apply(p,cq))/(lam-m) for lam,p in pr.items() if lam>cutoff),F())
    alpha_s=sum((dot(sq,apply(p,sq))/(lam-m) for lam,p in pr.items() if lam>cutoff),F())
    if not 1-2*alpha_s > 0:
        raise JumpSpectralError('high negative polar channel would invalidate Schur inverse')
    beta_c=2/(1+2*alpha_c)
    beta_s=2/(1-2*alpha_s)
    baseline=mul(add(L,eye(n),-m),P)
    short=add(add(baseline,outer(cp),beta_c),outer(sp),-beta_s)
    H=add(add(add(L,eye(n),-m),outer(c),2),outer(s),-2)
    high=mul(Q,mul(H,Q))
    # Apply the exact long Schur identity to original full ambient basis.
    cross=mul(P,mul(H,Q))
    expected=add(outer(cp,cq),outer(sp,sq),-1) # cross is 2*cP*cQ -2*sP*sQ
    if cross != scale(expected,2):
        raise JumpSpectralError('unexplained Gamma/FUCC mixed-source cross term')
    low_w=witness(short)
    full_w=witness(H)
    if (low_w is None)!=(full_w is None):
        raise JumpSpectralError('high-positive finite Schur does not preserve inertia')
    return {
        'source_type':'EXACT_RATIONAL_FINITE_SURROGATE_NOT_SUZUKI',
        'rank':n, 'low_spectral_rank':sum(P[i][i] for i in range(n)),
        'low_projector':P, 'high_projector':Q,
        'high_gap_lower':cutoff-m-2*dot(s,s),
        'cosh_high_resolvent':alpha_c, 'sinh_high_resolvent':alpha_s,
        'cosh_effective_strength':beta_c, 'sinh_effective_strength':beta_s,
        'polar_cross_rank_at_most_two':True,
        'low_schur':short, 'full_signed_operator':H,
        'positive_certified_in_finite_model':low_w is None,
        'negative_witness':None if low_w is None else apply(P,low_w),
        'original_signed_Weil_certified':False, 'RH_proved':False,
    }


def exact_gamma_prefix_multiplier(radius, rungs):
    """Entirely rational finite prefix of the ORIGINAL real-Gamma symbol.

    Each d=4j+1 is a genuine Gamma OU rung, not an independent arithmetic
    source/prime.  Every term increases with |xi|, and omitted terms are PSD.
    """
    if type(radius) is not int or radius<1 or type(rungs) is not int or not 1<=rungs<=4096:
        raise JumpSpectralError('positive integer Gamma multiplier inputs')
    R=radius
    return sum((F(16*R*R,(4*j+1)*(4*R*R+(4*j+1)**2))
                for j in range(rungs)),F())


def effective_gamma_rank_budget():
    """Source *PAPER* spectral rank bound with direct finite Gamma coefficient.

    True 256-rung mGamma(76)>3927/500 (Fraction EXACT).  On the kernel of
    averaging over 453 cells in I=(-1/2,1/2):
      E_gamma(F) >= [3927/500]*(1-76/(3*453))² ||F||² > 7||F||².
    Any source jump spectral low subspace at eigenvalue<=7 therefore has
    dimension <=453.  No original jump eigenvector is computed here.
    """
    R=76; J=256; N=453
    gamma_prefix=exact_gamma_prefix_multiplier(R,J)
    finite_floor=F(3927,500)
    if not gamma_prefix>finite_floor:
        raise ArithmeticError('source real-Gamma rung lower bound failed')
    # ||F_R - cell_average(F_R)|| <=h R/pi ||F|| and pi>3; h=1/N.
    coercivity=finite_floor*(1-F(R,3*N))**2
    cap_M=F(51,8)
    cap_s_sq=F(1,32)
    B=cap_M+2*cap_s_sq
    cutoff=F(7)
    if not coercivity>cutoff>B:
        raise ArithmeticError('claimed effective source spectrum rank bound invalid')
    return {
        'radius':F(1,2),
        'cutoff':cutoff,
        'frequency_band_radius':R,
        'original_real_Gamma_prefix_rungs':J,
        'Gamma_exact_prefix_greater_than':finite_floor,
        'Gamma_source_prefix_checked_in_exact_Fraction':True,
        'cell_rank_upper':N,
        'band_Gamma_energy_floor':finite_floor,
        'high_cell_complement_energy_floor':coercivity,
        'legacy_crude_cell_rank_upper':262144,
        'negative_source_potential_upper':cap_M,
        'sinh_norm_squared_upper':cap_s_sq,
        'full_negative_budget_upper':B,
        'high_signed_spectral_gap_lower':cutoff-B,
        'odd_high_scalar_resolvent_upper':cap_s_sq/(cutoff-cap_M),
        'odd_polar_effective_strength_upper':2/(1-2*(cap_s_sq/(cutoff-cap_M))),
        'spectral_projector_explicitly_computed':False,
        'first_window_S4_sign_proved':False,
        'RH_proved':False,
    }


def authenticate_original_jump_rank_budget():
    """Pin original Suzuki source, true prime tape and Gamma/contact upper,
    then return inherited-analytic PAPER rank/gap implication.

    The source module exports outward rationals; implementation proof of the
    compact-resolvent and logarithmic Fourier/cell theorems remains paper.
    """
    from . import source_weil_hierarchy as src
    from .tate_suzuki_shorting import verify_original_suzuki_source
    contract=verify_original_suzuki_source()
    if src.authenticated_prime_wavefront(F(1,2))!=((2,2),):
        raise JumpSpectralError('wrong true prime-wavefront at a=1/2')
    C=src.contact_iv()
    w=src.log2_iv()*src.sqrt_inverse(2)
    if not (C.lo>0 and C.hi<F(43,8) and w.lo>0 and w.hi<F(1,2)):
        raise JumpSpectralError('original Gamma prime/contact normalization failed')
    packet=effective_gamma_rank_budget()
    # Independent inherited ORIGINAL-source WB4 theorem: true four-low
    # complement positive, so negative index(full signed H) <=4.  Subtracting
    # one even cosh rank-one can add at most one negative baseline mode.
    from .tate_weighted_bessel_four_schur import source_parity_split_four_moment_coercivity_certificate
    wb4=source_parity_split_four_moment_coercivity_certificate()
    if (wb4['source_suzuki_blob'] !=contract['source_git_blob'] or
        wb4['global_kappa_lower'] != F(63,500)):
        raise JumpSpectralError('genuine infinite-source WB4 high positivity not authenticated')
    return dict(packet,
                negative_jump_baseline_index_upper=5,
                negative_even_jump_baseline_index_upper=3,
                negative_odd_jump_baseline_index_upper=2,
                source_high_WB4_global_kappa=wb4['global_kappa_lower'],
                source_contract=contract,
                contact_upper_rational=C.hi,
                true_prime2_half_density_upper=w.hi,
                actual_source_identified_by_archival_sha=True,
                actual_source_spectrum_computed=False,
                original_signed_Weil_certified=False)


def canonical_cycle_control(potential=1, pole_mutation=False):
    """EXACT four-site positive jump graph with rational spectrum 0,20,40.
    This is a *TOY* for checking source spectral partitioning and polar shorting.
    """
    L=((20,-10,0,-10),(-10,20,-10,0),(0,-10,20,-10),(-10,0,-10,20))
    T=((1,0,0,0),(0,0,0,1),(0,0,1,0),(0,1,0,0))
    c=(1,0,1,0) if not pole_mutation else (0,0,0,0)
    s=(0,1,0,-1)
    return exact_polar_schur(L,(0,20,40),potential,c,s,F(25),T)


def authentic_primitive_ritz_packet(mode=1, gamma_modes=20):
    """Authentic SOURCE interval for one low jump-generator Rayleigh quotient.

    This does not yield the jump source eigenprojector: it is a Ritz *trial* in
    the original primitive F=V P_mode(2t) (not a made-up eigenfunction).
    The omitted gamma convolution is true PSD and bounded in original u norm.
    """
    from . import source_weil_hierarchy as src
    from .suzuki_legendre_source import authentic_full_low_entry, authentic_pole_low_entry
    from .suzuki_moment_schur import inverse_neumann_entry
    from .tate_suzuki_shorting import verify_original_suzuki_source
    verify_original_suzuki_source()
    if src.authenticated_prime_wavefront(F(1,2)) != ((2,2),):
        raise JumpSpectralError('prime power activation not authenticated')
    if type(mode) is not int or not 1 <= mode <= 4 or type(gamma_modes) is not int or not 1 <= gamma_modes <= 75:
        raise JumpSpectralError('only modes 1..4, Gamma modes 1..75')
    a=F(1,2)
    k=inverse_neumann_entry(a,mode,mode)
    if k <= 0:
        raise ArithmeticError('Neumann primitive norm must be positive')
    M=src.contact_iv()+2*src.log2_iv()*src.sqrt_inverse(2)
    full_trunc=authentic_full_low_entry(mode,mode,a,gamma_modes)
    polar=authentic_pole_low_entry(mode,mode,a)
    bare_trunc=full_trunc-polar  # L_plus - M, i.e. completed polar-free baseline
    plus_trunc=bare_trunc+M*k
    tail=src.authentic_positive_gamma_tail_norm(gamma_modes)/F(2*mode+1)
    return {
       'mode':mode, 'gamma_modes':gamma_modes,
       'original_source_blob':verify_original_suzuki_source()['source_git_blob'],
       'original_source_energy_truncated_interval':(full_trunc.lo,full_trunc.hi),
       'original_polar_interval':(polar.lo,polar.hi),
       'polar_free_baseline_energy_interval':(bare_trunc.lo,bare_trunc.hi+tail),
       'baseline_rigorously_negative_on_this_trial':bare_trunc.hi+tail<0,
       'signed_contact_and_prime_mass_interval':(M.lo,M.hi),
       'primitive_K_norm_squared':k,
       'positive_jump_ritz_energy_interval':(plus_trunc.lo,plus_trunc.hi+tail),
       'positive_jump_ritz_rayleigh_interval':(plus_trunc.lo/k,(plus_trunc.hi+tail)/k),
       'omitted_original_Gamma_energy_cap':tail,
       'source_generated_jump_eigenfunction_claimed':False,
       'original_S4_sign_proved':False,
       'RH_proved':False,
    }


def source_fourier_band_certificate_budget(k=16, absolute_error=F(1,4)):
    """Constructive, intentionally huge uniform rational finite-rank *sufficient*
    certificate for the authentic first-prime Fourier LOWER envelope.

    For R=2^k and mu=(69/125)k <= mGamma(R), set
    H_R=mu I + T_R*(h_plus-mu)T_R.  Then H_R<=L_plus as forms.
    The midpoint finite-rank sum on the band differs in operator norm by at
    most (4k+65)R²/(12*N).  Source h_j interval certificates and Fourier
    feature Grams still must be computed!  The budget is a theorem, not a
    performed 10^11-point spectral computation.
    """
    if type(k) is not int or not 1<=k<=1000:
        raise JumpSpectralError('positive exact dyadic frequency exponent')
    err=rat(absolute_error)
    if err<=0:
        raise JumpSpectralError('positive error target required')
    R=2**k
    mu=F(69*k,125)
    # For the original a=1/2, active p=2, the genuine Γ multiplier:
    # |h_plus'|<17/2 and sup_[0,R] |h_plus-mu| <= 2k+24.
    # |Fhat|² <= ||F||²/6 and |(|Fhat|²)'| <= ||F||²/6.
    derivative=F(4*k+65,12)
    N=derivative*R*R/err
    count=N.numerator//N.denominator+1
    guaranteed=derivative*R*R/count
    if not guaranteed<err:
        raise ArithmeticError('quadrature rank does not meet declared strict error')
    # One pair of real cos/sin features at each positive-frequency node.
    return {
        'original_source_geometry':'FIRST_TRUE_PRIME_LOG_CLOCK_A_EQUALS_ONE_HALF',
        'R':R, 'mu_gamma_lower':mu,
        'absolute_operator_quadrature_error_requested':err,
        'absolute_operator_quadrature_error_certified_upper':guaranteed,
        'two_sided_midpoint_frequency_nodes':count,
        'worst_case_real_feature_rank':count+2,
        'valid_only_with_certified_sample_lower_coefficients':True,
        'actual_source_frequency_coefficients_sampled':False,
        'original_signed_Weil_positivity_certified':False,
        'RH_proved':False,
    }


def exact_feature_gram_decision(base_margin, gram, signed_weights):
    """Exact finite feature-space reduction of c*I+Phi diag(w)Phi*.

    gram=Phi*Phi, so for F=Phi v the quadratic is
        v*(c gram+gram diag(w) gram)v.
    The complement has eigenvalue c>0.  A PSD finite Gram is REQUIRED;
    'positive covariance' is not substituted for the signed weights.
    """
    c=rat(base_margin)
    K=matrix(gram)
    n=len(K)
    weights=vec(signed_weights,n)
    if c<=0 or not symmetric(K) or not is_psd(K):
        raise JumpSpectralError('strict scalar floor and authentic PSD feature Gram needed')
    if any(len(row)!=n for row in K):
        raise JumpSpectralError('square Gram required')
    D=tuple(tuple(weights[i] if i==j else F() for j in range(n)) for i in range(n))
    restricted=add(scale(K,c),mul(K,mul(D,K)))
    bad=witness(restricted)
    return {
        'finite_restricted_matrix':restricted,
        'positive_certified_in_finite_feature_model':bad is None,
        'negative_coefficient_witness':bad,
        'analytic_source_coefficient_authentication_required':True,
        'original_signed_Weil_certified':False,
        'RH_proved':False,
    }
