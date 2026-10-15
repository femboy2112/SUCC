"""Authenticated Suzuki low/high moment bridge; exact finite algebra.

Parent: SUCC PR #85 at dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc.
Sibling AMW-06B theorem: PR #86 at 205ffd020dd2a320eeac70a91a2a2700c969c048.

True source is supplied ONLY by the pinned parent module, which is imported
inside the source adapter. Everything else here is classical exact rational
finite matrix/Legendre arithmetic. No zero readings, no RH or Weil-sign claim.
"""
from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha1
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from typing import Iterable

class SchurSourceError(ValueError):
    pass

PARENT_SHA = "dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc"
AMW_SIBLING_SHA = "205ffd020dd2a320eeac70a91a2a2700c969c048"
PARENT_SOURCE_BLOB = "0cc8510b71d178fc79e8d410a86d8b6014cf9178"
CANONICAL_KAPPA = F(369, 10000)


def q(x):
    if type(x) not in (int, F):
        raise SchurSourceError('source coordinates must be exact int/Fraction')
    return F(x)


def integer(x, lo=0, hi=1000):
    if type(x) is not int or not lo <= x <= hi:
        raise SchurSourceError('integer outside exact finite budget')
    return x


def zeros(m,n):
    return tuple(tuple(F() for _ in range(n)) for _ in range(m))


def eye(n):
    return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))


def transpose(A):
    return tuple(tuple(x for x in row) for row in zip(*A))


def matmul(A,B):
    if not A or not B or len(A[0])!=len(B):
        raise SchurSourceError('matrix multiplication dimension mismatch')
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),F())
                       for j in range(len(B[0]))) for i in range(len(A)))


def matadd(A,B,factor=F(1)):
    if len(A)!=len(B) or any(len(x)!=len(y) for x,y in zip(A,B)):
        raise SchurSourceError('matrix sum dimension mismatch')
    factor=q(factor)
    return tuple(tuple(x+factor*y for x,y in zip(ra,rb)) for ra,rb in zip(A,B))


def matinv(A):
    n=len(A)
    if not n or any(len(row)!=n for row in A):
        raise SchurSourceError('square matrix required')
    x=[[q(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for col in range(n):
        pivot=next((r for r in range(col,n) if x[r][col]!=0),None)
        if pivot is None:raise SchurSourceError('matrix singular: no lawful resolvent')
        x[col],x[pivot]=x[pivot],x[col]
        v=x[col][col]
        x[col]=[y/v for y in x[col]]
        for r in range(n):
            if r==col:continue
            v=x[r][col]
            if v:x[r]=[x[r][j]-v*x[col][j] for j in range(2*n)]
    return tuple(tuple(x[i][n:]) for i in range(n))


def symmetric(A):
    return bool(A) and all(len(row)==len(A) for row in A) and all(A[i][j]==A[j][i] for i in range(len(A)) for j in range(len(A)))


def positive_definite(A):
    """Exact rational symmetric LDL >0; PSD with zero pivots not asserted."""
    if not symmetric(A):return False
    n=len(A);L=[[F(i==j) for j in range(n)] for i in range(n)];d=[]
    for j in range(n):
        dj=A[j][j]-sum((L[j][k]**2*d[k] for k in range(j)),F())
        if dj<=0:return False
        d.append(dj)
        for i in range(j+1,n):
            L[i][j]=(A[i][j]-sum((L[i][k]*L[j][k]*d[k] for k in range(j)),F()))/dj
    return True


def legendre(n,x):
    """P_n(x) over exact Q, no approximate normalization."""
    integer(n,0,64); x=q(x)
    if n==0:return F(1)
    if n==1:return x
    a,b=F(1),x
    for k in range(1,n):
        a,b=b,((2*k+1)*x*b-k*a)/(k+1)
    return b


def legendre_primitive(n,a,x):
    """V P_n(x/a)=a*(P_(n+1)(x/a)-P_(n-1)(x/a))/(2n+1)."""
    integer(n,1,64);a=q(a);x=q(x)
    if not 0<a<=2 or not -a<=x<=a:
        raise SchurSourceError('legal compact interval endpoint required')
    return a*(legendre(n+1,x/a)-legendre(n-1,x/a))/(2*n+1)


def low_gram(a,rank):
    """On H=L²_0, basis L_k(x)=P_k(x/a), k=1..rank."""
    a=q(a);integer(rank,1,30)
    if not 0<a<=1: raise SchurSourceError('compact source halfwidth 0<a<=1')
    return tuple(tuple(F(2*a,2*i+1) if i==j else F() for j in range(1,rank+1))
                 for i in range(1,rank+1))


def low_inverse_neumann(a,rank):
    """Exact Klow=<V L_i,V L_j>_L2, K=V*V inverse Neumann on H.

    Source supports v_i=V L_i in H0¹, with V(L_i)(±a)=0.
    A nonzero low/high cross K is retained; NOT K-inverse on Hhigh.
    """
    a=q(a);integer(rank,1,30)
    if not 0<a<=1:raise SchurSourceError('halfwidth')
    ans=[]
    for i in range(1,rank+1):
        row=[]
        for j in range(1,rank+1):
            cs=F(a*a*2*a,(2*i+1)*(2*j+1))
            v=F()
            if i==j:v+=F(1,2*i+3)+F(1,2*i-1)
            if i+1==j-1:v-=F(1,2*i+3)
            if i-1==j+1:v-=F(1,2*i-1)
            row.append(cs*v)
        ans.append(tuple(row))
    return tuple(ans)


def inverse_neumann_entry(a,i,j):
    """K_(ij) in unnormalized Legendre u basis (indices i,j>=1)."""
    a=q(a);integer(i,1,128);integer(j,1,128)
    if not 0<a<=1:raise SchurSourceError('halfwidth')
    v=F()
    if i==j:v+=F(1,2*i+3)+F(1,2*i-1)
    if i+1==j-1:v-=F(1,2*i+3)
    if i-1==j+1:v-=F(1,2*i-1)
    return F(2*a**3,(2*i+1)*(2*j+1))*v


def inverse_neumann_boundary_channels(a,rank=30):
    """K low/high boundary has rank exactly two for rank>=2.

    Infinite u Legendre carrier is indexed k>=1. Source metric
    K=V*V has |i-j|=0,2 ONLY; crossing cut i<=rank<j gives
    two channels (rank-1,rank+1),(rank,rank+2).
    """
    a=q(a);integer(rank,2,30)
    rows=((rank-1,rank+1),(rank,rank+2))
    cross=tuple((i,j,inverse_neumann_entry(a,i,j)) for i,j in rows)
    orthonormal_frobenius_squared=sum((z*z/F(2*a,2*i+1)/F(2*a,2*j+1) for i,j,z in cross),F())
    assert all(z<0 for _,_,z in cross)
    return {'rank':rank,'channels':tuple((i,j,str(z)) for i,j,z in cross),
            'normalized_boundary_frobenius_squared':str(orthonormal_frobenius_squared),
            'K_low_high_cross_rank':2,'source_G_cross_rank_only_two':False}


def parity_blocks(S,rank):
    """Canonical even/odd Legendre low blocks; off-parity must vanish."""
    integer(rank,1,30)
    if len(S)!=rank or not symmetric(S):raise SchurSourceError('symmetric canonical low matrix required')
    for i in range(rank):
        for j in range(rank):
            if (i-j)%2 and S[i][j]!=0:
                raise SchurSourceError('actual reflection symmetry violated')
    odd=tuple(i for i in range(rank) if (i+1)%2)
    even=tuple(i for i in range(rank) if not (i+1)%2)
    return {'odd':tuple(tuple(S[i][j] for j in odd) for i in odd),
            'even':tuple(tuple(S[i][j] for j in even) for i in even),
            'odd_rank':len(odd),'even_rank':len(even)}


def cell_legendre_overlap(a,rank,N):
    """M_(ki)=<P_k(x/a), 1_(cell_i)-1/N>, exact via primitive."""
    a=q(a);integer(rank,1,30);integer(N,2,256)
    if not 0<a<=1:raise SchurSourceError('halfwidth')
    h=2*a/N
    rows=[]
    for k in range(1,rank+1):
        row=tuple(legendre_primitive(k,a,-a+(i+1)*h)-legendre_primitive(k,a,-a+i*h) for i in range(N))
        if sum(row,F()):raise ArithmeticError('mean-zero Legendre transport lost a source moment')
        rows.append(row)
    return tuple(rows)


def projection_cell_gram(a,rank,N):
    """Hcell=C*P_high C >=0; high is orthogonal to 30 Legendre modes."""
    a=q(a);rank=integer(rank,1,30);N=integer(N,2,256)
    h=2*a/N; M=cell_legendre_overlap(a,rank,N);W=low_gram(a,rank)
    WT=tuple(tuple(F(1,W[i][i]) if i==j else F() for j in range(rank)) for i in range(rank))
    base=tuple(tuple(h*F(i==j)-h*h/(2*a) for j in range(N)) for i in range(N))
    return matadd(base,matmul(matmul(transpose(M),WT),M),-1)


def invert_2x2_and_schur(A,B,D,lam):
    """Toy exact scalar source-independent Schur, not a Weil sign oracle."""
    A,B,D,lam=map(q,(A,B,D,lam))
    if lam<=0 or D+lam<=0:raise SchurSourceError('positive regularization required')
    return A+lam-B*B/(D+lam)


def unprojected_cross_no_go(gap,rayleigh,source_norm=1):
    """Cauchy: ||Af||²>=<Af,f>²/||f||².

    For any f with <Af,f> > gap ||f||², the AMW-07
    *unprojected* R_full=||Af||² sufficient matrix necessarily fails.
    This DOES NOT imply the exact projected Schur is negative.
    """
    k,x,n=map(q,(gap,rayleigh,source_norm))
    if k<=0 or n<=0:raise SchurSourceError('legal coercivity/source norm required')
    bound=x-x*x/(k*n)
    return {"guaranteed_failure":x>k*n,"unprojected_schur_upper":str(bound),
            "projected_cross_required":True,"authentic_Weil_negative":False}


def source_moment30_certificate():
    """Independent Fraction replay of PR #86's AMW-06B assumptions/ratio.

    The actual whole-form analytic theorem is pinned by its SHA, not proved
    by this finite list of rational inequalities or a numerical source table.
    """
    from math import factorial
    T,J,N,a=21,75,29,F(1,2)
    gamma=sum((F(2*T*T)/(F(4*j+1,2)*(F(4*j+1,2)**2+T*T)) for j in range(J)),F())
    leak=F(2*a*T,3)*(a*T)**(2*N+2)/(factorial(N+1)**2)
    if not (gamma>F(131,20) and leak<F(1,500)):
        raise ArithmeticError('inherited 30-moment exact inequalities fail')
    lower=F(131,20)*F(499,500)-F(13,2)
    assert lower==F(369,10000)
    return {'parent_theorem':'AMW-06B','sibling_sha':AMW_SIBLING_SHA,
            'window_halfwidth':'1/2','vanishing_moments':30,
            'gamma_rungs':75,'frequency_threshold':21,
            'rational_source_lower':str(F(131,20)),
            'rational_leak_upper':str(F(1,500)),
            'full_signed_budget':str(F(13,2)),
            'strict_high_L2_coercivity':str(lower),
            'H_u_high_uniform_I_gap':False,'RH_proved':False}


def _git_blob_id(path):
    content=Path(path).read_bytes()
    return sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()


def _same_typed(a,b):
    """Prevent Fraction/float/True equality laundering at nested source gates."""
    if type(a) is not type(b):return False
    if type(a) is tuple:
        return len(a)==len(b) and all(_same_typed(x,y) for x,y in zip(a,b))
    if type(a) is dict:
        return a.keys()==b.keys() and all(_same_typed(a[k],b[k]) for k in a)
    return a==b


def source_stage_bridge(a,rank,J,N):
    """True source adapter; absent outside inherited #85 checkout.

    Full operator G≈G_N=C R C* on H=L²_0; parent stage is authenticated.
    We only use rational stage midpoint and its ORIGINAL source error.
    """
    a=q(a);integer(rank,1,30);integer(J,1,36);integer(N,2,24)
    try:
        from observational_succ import source_weil_hierarchy as source
    except ImportError as exc:
        raise SchurSourceError('pinned parent #85 source is required; cannot invent') from exc
    if _git_blob_id(source.__file__) != PARENT_SOURCE_BLOB:
        raise SchurSourceError('Suzuki original-source module drift; new proof pin required')
    st=source.stage(a,J,N);source._authenticated(st)
    if st.source != 'AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3' or st.nontrivial_zeros_used:
        raise SchurSourceError('original Weil source data refused')
    h=2*a/N
    R=tuple(tuple(z/h for z in row) for row in st.center)
    M=cell_legendre_overlap(a,rank,N)
    H=projection_cell_gram(a,rank,N)
    W=low_gram(a,rank)
    err=st.norm_error
    spatial=source.honest_spatial_error(st)
    positive_tail=source.authentic_positive_gamma_tail_norm(J)
    if spatial > err or positive_tail<0:
        raise ArithmeticError('source-signed Gamma spatial decomposition failed')
    # On whole meanzero H, P0 C(R)C*P0 has matrix hR on cells.
    operator_bound=max((sum((abs(x) for x in row),F()) for row in st.center),default=F())
    return {'source':st.source,'parent_sha':PARENT_SHA,'a':a,'rank':rank,'J':J,'N':N,
            'R':R,'M':M,'H':H,'W':W,'error':err,
            'spatial_error':spatial,'gamma_positive_tail_upper':positive_tail,
            'G_N_norm_upper':operator_bound,
            'RH_proved':False}


def finite_regularized_schur(R,M,H,W,lam):
    """Pure exact finite matrix identity; NOT an arithmetic sign oracle.

    G_N=C R C*; M=L*C, H=C*P_high C, W=L*L.
    Exact Schur in unnormalized low basis:
      S_N=lam W + lam M(lam I+R H)^(-1) R M*.
    The equivalent expanded formula has a -MRH resolver cross term.
    """
    lam=q(lam)
    if lam<=0:raise SchurSourceError('positive regularizer required')
    N=len(R);rank=len(M)
    if not N or any(len(row)!=N for row in R) or not symmetric(R):
        raise SchurSourceError('symmetric square source cell kernel required')
    if len(H)!=N or not symmetric(H) or len(W)!=rank or not symmetric(W) or any(len(row)!=N for row in M):
        raise SchurSourceError('wrong source projection dimension/symmetry')
    RN=matmul(R,H)
    resolver=matadd(tuple(tuple(lam*int(i==j) for j in range(N)) for i in range(N)),RN)
    inv=matinv(resolver)
    source_matrix=matmul(matmul(matmul(M,inv),R),transpose(M))
    S=matadd(W,source_matrix,1)   # multiply ALL of this by lambda below
    S=tuple(tuple(lam*z for z in row) for row in S)
    if not symmetric(S):raise ArithmeticError('exact Schur low-source symmetry lost')
    return S


def regularized_schur_from_stage(stage_data,lam):
    """Certified true 30x30 Schur approximation with a source-error gate.

    For true high D>=0, source ||G-G_N||<=e and ||G_N||<=L:
    ||S(lam)-S_N(lam)|| <= e*[1+(2L+e)/lam +L²/(lam*(lam-e))].
    Certifier requires lam>e. A positive finite *matrix* below its error
    does NOT certify source sign. The high positivity source is PR #86.
    """
    if type(stage_data) is not dict or stage_data.get('source')!='AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3':
        raise SchurSourceError('authentic parent source adapter required')
    trusted=source_stage_bridge(stage_data['a'],stage_data['rank'],stage_data['J'],stage_data['N'])
    if not _same_typed(stage_data,trusted):
        raise SchurSourceError('forged source matrix/error or unsafe float/bool alias')
    lam=q(lam);e=stage_data['error'];L=stage_data['G_N_norm_upper']
    if lam<=e:raise SchurSourceError('regularizer must exceed original signed source error')
    R,M,H,W=tuple(stage_data[k] for k in ('R','M','H','W'))
    S=finite_regularized_schur(R,M,H,W,lam)
    error=e*(1+(2*L+e)/lam+L*L/(lam*(lam-e)))
    # The true g_J cell operator retains reflection symmetry exactly.
    par=parity_blocks(S,stage_data['rank'])
    # A PSD true S(lam) follows ONLY from strict error-corrected tests.
    residual=matadd(S,W,-error)
    res_par=parity_blocks(residual,stage_data['rank'])
    pd=all(positive_definite(sub) for sub in (res_par['odd'],res_par['even']) if sub)

    return {'source':stage_data['source'],'regularization':str(lam),
            'rank':stage_data['rank'],'cells':stage_data['N'],
            'matrix':S,'source_error':str(e),'schur_error':str(error),
            'parity_odd_rank':par['odd_rank'],'parity_even_rank':par['even_rank'],
            'source_certified_G_plus_lambda_positive':pd,
            'negative_depth_upper_if_positive':str(lam) if pd else None,
            'unrestricted_G_positive':False,'RH_proved':False}


def one_sided_gamma_schur_from_stage(stage_data,lam):
    """Improved genuine lower Feshbach bound with NO Gamma-tail penalty.

    G=G_J+T_J, T_J>=0, ||T_J||<=tau_J. High of full G>=0 from
    source AMW-06B. Thus D_J>=-tau_J, while D_N>=-(tau_J+esp).
    lambda>tau_J+esp makes all high resolvents invertible.
    Monotonicity of Schur variational shorting implies S_G(lambda)>=
    S_GJ(lambda). Only esp=||G_J-G_N|| is charged in lower Schur:
      error=esp*(1+(2L+esp)/(lambda-tau)
                    +L²/[(lambda-tau)(lambda-tau-esp)]).
    Stacking positive Gamma rungs is lawful; missing true prime/pole/source
    terms would NOT be protected by this inequality.
    """
    if type(stage_data) is not dict or stage_data.get('source')!='AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3':
        raise SchurSourceError('authentic original-source stage required')
    trusted=source_stage_bridge(stage_data['a'],stage_data['rank'],stage_data['J'],stage_data['N'])
    if not _same_typed(trusted,stage_data):raise SchurSourceError('forged source/gamma error stage')
    lam=q(lam)
    esp=stage_data['spatial_error'];tau=stage_data['gamma_positive_tail_upper'];L=stage_data['G_N_norm_upper']
    if lam<=tau+esp:
        raise SchurSourceError('lambda must exceed positive-tail + spatial defect')
    mu=lam-tau
    bound=esp*(1+(2*L+esp)/mu+L*L/(mu*(mu-esp)))
    S=finite_regularized_schur(stage_data['R'],stage_data['M'],stage_data['H'],stage_data['W'],lam)
    par=parity_blocks(S,stage_data['rank'])
    resid=matadd(S,stage_data['W'],-bound)
    spar=parity_blocks(resid,stage_data['rank'])
    good=all(positive_definite(x) for x in (spar['odd'],spar['even']) if x)
    return {'source':stage_data['source'],'rank':stage_data['rank'],
            'lambda':str(lam),'parity_odd_rank':par['odd_rank'],
            'parity_even_rank':par['even_rank'],
            'source_positive_gamma_monotonicity':True,
            'gamma_tail_charged_against_lower_schur':False,
            'positive_gamma_tail_norm_upper':str(tau),
            'spatial_error_only':str(esp),'lower_schur_error':str(bound),
            'matrix':S,'certified_G_plus_lambda_positive':good,
            'negative_depth_upper_if_positive':str(lam) if good else None,
            'actual_G_positive':False,'RH_proved':False}


def parent_grid_resolution_wall(N,target_lambda=F(1,10000)):
    """Exact declared-error floor of PR #85's uniform-Lipschitz stage.

    At a=1/2, spatial error= (1/N)*[9+2 sum_(j<J)1/(4j+1)] + eta.
    Every legal J>=1 therefore has e_spatial>=11/N. This is a lower
    bound on the *certification budget*, NOT on the actual source error.
    To try any Feshbach shift lambda with lambda>e_sp+tau one must have
    N>11/lambda, even before omitted Gamma mode cost.
    """
    integer(N,2,10**9);target_lambda=q(target_lambda)
    if target_lambda<=0:raise SchurSourceError('strict target shift required')
    floor=F(11,N)
    x=F(11)/target_lambda
    minimal=x.numerator//x.denominator+1
    return {'a':'1/2','N':N,'stage_spatial_error_floor':str(floor),
            'requested_shift':str(target_lambda),'necessary_grid_N_for_target':minimal,
            'this_stage_api_can_even_attempt':N>=minimal,
            'actual_source_negative_depth_certified':False,'RH_proved':False}


def source_small_grid_demonstration():
    """Optional authenticated live source stage; never a stand-in by a toy.

    Only call on the inherited PR #85 checkout. Produces the complete
    30×30 low Schur source matrix at a declared large regularization.
    The result is a diagnostic/source upper-depth test, NOT RH.
    """
    st=source_stage_bridge(F(1,2),30,2,4)
    lam=st['error']+1
    full=regularized_schur_from_stage(st,lam)
    one=one_sided_gamma_schur_from_stage(st,lam)
    return {'stage':'authentic_Suzuki_PR85_J2_N4','low_modes':30,
            'parity_blocks':[15,15],
            'lambda':str(lam),
            'symmetric_schur_error':full['schur_error'],
            'gamma_monotone_lower_schur_error':one['lower_schur_error'],
            'source_gamma_gain':F(one['lower_schur_error']) < F(full['schur_error']),
            'rational_low_diagonal_sample':[str(one['matrix'][i][i]) for i in (0,1,14,15,28,29)],
            'positive_shift_source_certified':one['certified_G_plus_lambda_positive'],
            'RH_proved':False}


def test_toy_schur_stability():
    """Two honest controls: positive source misleading with full-A cross,
    and an indefinite toy detected by exact Schur resolvent."""
    return {'positive_diagonal_unprojected_no_go':unprojected_cross_no_go(1,10),
            'correct_positive_diagonal_schur':str(invert_2x2_and_schur(10,0,1,F(1,10))),
            'indefinite_cross_schur':str(invert_2x2_and_schur(1,2,1,F(1,10))),
            'RH_proved':False}


def receipt():
    a=F(1,2)
    W=low_gram(a,30)
    K=low_inverse_neumann(a,30)
    o=cell_legendre_overlap(a,30,6)
    return {
        'source':'AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3',
        'pinned_hierarchy_parent':PARENT_SHA,
        'pinned_30moment_sibling':AMW_SIBLING_SHA,
        'high_moment_30':source_moment30_certificate(),
        'low_gram_diagonal':[str(W[i][i]) for i in (0,1,28,29)],
        'low_K_selected':{'k_1_1':str(K[0][0]),'k_1_3':str(K[0][2]),'k_29_29':str(K[28][28]),'k_30_30':str(K[29][29])},
        'low_high_K_boundary':{**inverse_neumann_boundary_channels(a,30),
            'channels':[list(x) for x in inverse_neumann_boundary_channels(a,30)['channels']]},
        'parent_resolution_wall':parent_grid_resolution_wall(24),
        'cell_overlap_row_sums_exact':all(sum(row,F())==0 for row in o),
        'low_K_cross_parity_sparsity':all(K[i][j]==0 for i in range(30) for j in range(30) if abs(i-j) not in (0,2)),
        'toy_controls':test_toy_schur_stability(),
        'correct_domain':'u=i*vprime in meanzero L2, K=Volterra*Volterra',
        'canonical_low': 'Legendre k=1..30; moment high orthogonal',
        'actual_source_regularized_schur_matrix_computed':False,
        'all_a_positive':False,
        'RH_proved':False,
    }
