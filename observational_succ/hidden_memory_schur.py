"""Source-indexed, delay-revealed hidden Schur response: exact rational math.

The original Suzuki source is never replaced by an auxiliary covariance. This
module proves finite-dimensional identities; the real-source adapter imports
and checks the SHA-pinned Gamma/FUCC spectral bound of SUCC #158.

Nature Physics (Muruga et al., 2026, DOI 10.1038/s41567-026-03442-w)
is an experimental *motivation*, not a theorem about SUCC or the Weil form.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import isqrt


class HiddenMemoryError(ValueError):
    pass


def q(x):
    if type(x) not in (int, F):
        raise HiddenMemoryError("exact int/Fraction required, float/bool refused")
    return F(x)


def vec(v):
    out = tuple(q(x) for x in v)
    if not out:
        raise HiddenMemoryError("empty vector")
    return out


def mat(rows):
    out = tuple(tuple(q(x) for x in row) for row in rows)
    if not out or any(len(row) != len(out[0]) for row in out):
        raise HiddenMemoryError("nonempty rectangular exact matrix")
    return out


def zeros(n, m):
    return tuple(tuple(F(0) for _ in range(m)) for _ in range(n))


def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def transpose(a):
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def add(a, b, factor=1):
    f = q(factor)
    if not a or len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise HiddenMemoryError("matrix addition dimensions")
    return tuple(tuple(x+f*y for x, y in zip(ra,rb)) for ra,rb in zip(a,b))


def scale(a, factor):
    f = q(factor)
    return tuple(tuple(f*x for x in row) for row in a)


def mult(a, b):
    if not a or not b or len(a[0]) != len(b):
        raise HiddenMemoryError("matrix product dimensions")
    bt=transpose(b)
    return tuple(tuple(sum((x*y for x,y in zip(ar,bc)),F()) for bc in bt) for ar in a)


def matrix_inv(a):
    a=mat(a)
    n=len(a)
    if any(len(r)!=n for r in a):
        raise HiddenMemoryError("square matrix required")
    aug=[list(row)+list(eye(n)[i]) for i,row in enumerate(a)]
    for j in range(n):
        piv=next((i for i in range(j,n) if aug[i][j]),None)
        if piv is None:
            raise HiddenMemoryError("singular matrix")
        aug[piv],aug[j]=aug[j],aug[piv]
        p=aug[j][j]
        aug[j]=[x/p for x in aug[j]]
        for i in range(n):
            if i==j: continue
            f=aug[i][j]
            aug[i]=[x-f*y for x,y in zip(aug[i],aug[j])]
    return tuple(tuple(row[n:]) for row in aug)


def determinant(a):
    a=mat(a)
    n=len(a)
    if any(len(r)!=n for r in a):raise HiddenMemoryError("square determinant")
    if n==1:return a[0][0]
    return sum(((-1)**j*a[0][j]*determinant(tuple(tuple(r[k] for k in range(n) if k!=j) for r in a[1:])) for j in range(n)),F())


def is_psd(a):
    a=mat(a);n=len(a)
    if any(len(r)!=n for r in a) or transpose(a)!=a:raise HiddenMemoryError("symmetric PSD matrix only")
    from itertools import combinations
    return all(determinant(tuple(tuple(a[i][j] for j in ids) for i in ids))>=0
               for k in range(1,n+1) for ids in combinations(range(n),k))


def psd_diff(a,b):
    return is_psd(add(mat(a),mat(b),-1))


def trace(a):
    return sum((a[i][i] for i in range(len(a))),F())


def inner(v,w):
    return sum((q(x)*q(y) for x,y in zip(v,w)),F())


def sum_powers(memory, length):
    """Exact finite resolvent memory, no numerical exponentials or float inverses."""
    D=mat(memory)
    n=len(D)
    if any(len(r)!=n for r in D):raise HiddenMemoryError("square high block")
    if type(length) is not int or length<0:raise HiddenMemoryError("nonnegative integer depth")
    if not is_psd(D):raise HiddenMemoryError("source high block must be PSD")
    return D


def rational_memory_telescope(low, cross, high, depth, *, step=F(16,9),
                              high_gap=F(9,16), coupling_sq_upper=None):
    """Exact finite rational Schur telescope with certified Loewner tail.

    D=high>=dI>0, C=cross, R=(I+hD)^(-1):
      X_N=h C sum_{j=1}^N R^j C^T
      S_N=A-X_N >= S=A-CD^{-1}C^T
      0<= S_N-S <= beta/d*(1+h*d)^(-N) I.
    Only declared finite rational matrices; never a genuine Weil sign claim.
    """
    A,B,D=mat(low),mat(cross),mat(high)
    n,m=len(A),len(D)
    if any(len(row)!=n for row in A) or any(len(row)!=m for row in D) or len(B)!=n or any(len(row)!=m for row in B):
        raise HiddenMemoryError("block dimension mismatch")
    if type(depth) is not int or depth<0:raise HiddenMemoryError("finite nonnegative observation depth")
    h,d=q(step),q(high_gap)
    if h<=0 or d<=0 or not is_psd(add(D,eye(m),-d)):
        raise HiddenMemoryError("unverified strictly positive high gap")
    BB=mult(B,transpose(B))
    beta=max((BB[i][i] for i in range(n)),default=F()) if coupling_sq_upper is None else q(coupling_sq_upper)
    if beta<0 or not is_psd(add(scale(eye(n),beta),BB,-1)):
        raise HiddenMemoryError("unproved coupling upper bound")
    R=matrix_inv(add(eye(m),D,h))
    if not is_psd(R):raise HiddenMemoryError("resolvent must be positive")
    current=R
    acc=zeros(m,m)
    for _ in range(depth):
        acc=add(acc,current)
        current=mult(current,R)
    Xn=mult(mult(B,scale(acc,h)),transpose(B))
    Sn=add(A,Xn,-1)
    true=add(A,mult(mult(B,matrix_inv(D)),transpose(B)),-1)
    err=beta/d/(1+h*d)**depth
    lo=add(Sn,eye(n),-err)
    if not psd_diff(Sn,true) or not psd_diff(true,lo):
        raise ArithmeticError("false finite-memory Loewner order")
    verdict="AMBIGUOUS"
    if is_psd(lo):verdict="POSITIVE_FINITE_MODEL"
    elif not is_psd(Sn):verdict="NEGATIVE_FINITE_MODEL"
    return {
        'finite_source_kind':'DECLARED_RATIONAL_MODEL_NOT_AUTHENTIC_WEIL',
        'depth':depth,'step':h,'high_gap':d,'coupling_squared_cap':beta,
        'one_step_resolvent':R,'memory_response_prefix':Xn,
        'finite_upper_S':Sn,'finite_lower_S':lo,'actual_finite_S':true,
        'Loewner_error_cap':err,
        'verdict':verdict,'original_Suzuki_sign_proved':False,'RH_proved':False,
    }


def scalar_memory_hankel(cross, high, length):
    """Scalar compressed lag kernels B*(I+D)^(-j)B for a finite hidden bath.

    All returned terms are nonnegative; Hankel matrices of them are PSD.
    These are *time-discrete* observables, not observed physical events.
    """
    b=vec(cross);D=mat(high);m=len(b)
    if len(D)!=m or any(len(r)!=m for r in D):raise HiddenMemoryError("hidden spectrum dimensions")
    if type(length) is not int or length<1:raise HiddenMemoryError("positive number of lag moments")
    if not is_psd(D):raise HiddenMemoryError("passive hidden high needed")
    R=matrix_inv(add(eye(m),D))
    p=eye(m)
    values=[]
    for _ in range(length):
        rp=mult(p,tuple((z,) for z in b))
        values.append(inner(b,tuple(row[0] for row in rp)))
        p=mult(p,R)
    return tuple(values)


def rational_sqrt(x):
    x=q(x)
    if x<0:raise HiddenMemoryError("negative square root")
    a,b=isqrt(x.numerator),isqrt(x.denominator)
    if a*a!=x.numerator or b*b!=x.denominator:
        raise HiddenMemoryError("nonrational spectral roots: no exact inference")
    return F(a,b)


def reconstruct_two_hidden_lags(moments):
    """Recover <=2 rational positive memory eigenmodes from 4 exact moments.

    Positive real Hankel rank and exact exponential-mixture recurrence required.
    Multi-source, noisy and infinite-bath use is prohibited.
    """
    if len(moments)!=4:raise HiddenMemoryError("exactly four temporal moments required")
    a,b,c,d=tuple(q(x) for x in moments)
    if a<=0 or not all(x>=0 for x in (a,b,c,d)):
        raise HiddenMemoryError("nonnegative nontrivial bath moments")
    hd=a*c-b*b
    if hd<0:raise HiddenMemoryError("nonpositive moment Hankel")
    if hd==0:
        ratio=b/a
        if not (0<ratio<1 and c==a*ratio**2 and d==a*ratio**3):
            raise HiddenMemoryError("one-mode moment law violated")
        modes=(ratio,);weights=(a,)
    else:
        rhs=(( -c,),(-d,))
        coeff=mult(matrix_inv(((a,b),(b,c))),rhs)
        p0,p1=coeff[0][0],coeff[1][0]
        disc=p1*p1-4*p0
        root=rational_sqrt(disc)
        q1,q2=(-p1-root)/2,(-p1+root)/2
        if not 0<q1<q2<1:raise HiddenMemoryError("noncontracting or repeated bath modes")
        w1=(q2*a-b)/(q2-q1)
        w2=a-w1
        if min(w1,w2)<=0 or c!=w1*q1*q1+w2*q2*q2 or d!=w1*q1**3+w2*q2**3:
            raise HiddenMemoryError("false positive hidden spectral measure")
        modes=(q1,q2);weights=(w1,w2)
    return {'modes':modes,'weights':weights,
            'zero_shift_inverse_response':sum((w*qx/(1-qx) for qx,w in zip(modes,weights)),F()),
            'physical_thermodynamic_work_computed':False,'original_Weil_source_authenticated':False}


def two_read_hidden_gaussian(*, hidden_coupling=1, noise_variance=1):
    """Conditional *variance* of hidden Y from actual two-time Gaussian readouts.

    X0,Y,E independent N(0,1), N(0,1), N(0,noise). M0=X0,
    M1=X0 + g*Y+E. One read gives no Y information; delayed pair does if g.
    No claim of Maxwell-demon work from this mathematical covariance example.
    """
    g,nv=q(hidden_coupling),q(noise_variance)
    if nv<=0:raise HiddenMemoryError("nonzero independent measurement noise")
    Y_given_M0=F(1)
    Y_given_both=nv/(g*g+nv)
    Y_info_variance_gain=1-Y_given_both
    if not F()<=Y_info_variance_gain<1:raise ArithmeticError("conditional variance bug")
    return {
        'hidden_prior_variance':F(1),'one_read_hidden_conditional_variance':Y_given_M0,
        'two_read_hidden_conditional_variance':Y_given_both,
        'variance_gain':Y_info_variance_gain,
        'conditional_mutual_information_nats_symbolic':'(1/2)*log((g^2+noise)/noise)' if g else '0',
        'independent_environment_negative_control':g==0,
        'thermodynamic_work_claimed':False,'Suzuki_positivity_claimed':False
    }




def positive_jump_projection_memory(generator, projector):
    """Exact finite memory/Markovian-tradeoff diagnostic for a positive L.

    If P commutes with L then P L Q=0: all positive-carrier memory is
    invisible to a spectral reducing observer. With nonreducing P the
    positive jump carrier can have a nonzero hidden memory coupling.
    This has no thermodynamic energy/extractable-work semantics.
    """
    L,P=mat(generator),mat(projector)
    n=len(L)
    if any(len(r)!=n for r in L+P) or len(P)!=n:
        raise HiddenMemoryError("positive jump/projector dimensions")
    if not is_psd(L) or transpose(P)!=P or mult(P,P)!=P:
        raise HiddenMemoryError("nonnegative generator and orthogonal projector required")
    Q=add(eye(n),P,-1)
    B=mult(mult(P,L),Q)
    commutes=mult(P,L)==mult(L,P)
    if commutes != (B==zeros(n,n)):
        raise ArithmeticError("reducing projection must have no memory cross")
    return {
        'source_kind':'DECLARED_RATIONAL_FINITE_GENERATOR_NOT_GENUINE_SUZUKI',
        'positive_carrier_reduces_observer':commutes,
        'source_positive_jump_cross':B,
        'memory_kernel_at_t0':mult(B,transpose(B)),
        'original_signed_Weil_sign_proved':False,
    }

def original_source_memory_budget(depth=12):
    """Source-conditional DYADIC high-response bound; no projector computed.

    Uses a=1/2 and the original #158 rank/gap paper results with SHA gate.
    U=P_[0,7](Lplus) is a *mathematical* projector, not a constructed array.
    High H block D >=9/16, B only two original polar channels.
    Norm B^2 <= ||c||^4 < (33/32)^2; rational proof sinh(1/2)<12/23.
    With h=16/9, R=(I+hD)^-1 <=1/2, thus tail <=121/(64*2^depth).
    """
    if type(depth) is not int or depth<0:raise HiddenMemoryError("nonnegative integer epoch")
    from .source_jump_spectral import authenticate_original_jump_rank_budget
    cert=authenticate_original_jump_rank_budget()
    if cert['source_contract']['source_git_blob']!='0cc8510b71d178fc79e8d410a86d8b6014cf9178':
        raise HiddenMemoryError("original signed source blob mismatch")
    if (cert['cutoff']!=F(7) or cert['high_signed_spectral_gap_lower']!=F(9,16)
        or cert['cell_rank_upper']!=453 or cert['spectral_projector_explicitly_computed']):
        raise HiddenMemoryError("source spectral gate drifted")
    if not F(12,23)<F(17,32) or not F(1,2)+F(12,23)<F(33,32):
        raise ArithmeticError("exact sinh upper failed")
    bound=F(121,64*2**depth)
    return {
        'original_source_blob':cert['source_contract']['source_git_blob'],
        'radius':cert['radius'],'cutoff':cert['cutoff'],
        'source_low_rank_upper':cert['cell_rank_upper'],
        'signed_high_gap_lower':cert['high_signed_spectral_gap_lower'],
        'rational_backward_euler_step':F(16,9),
        'time_steps':depth,
        'discrete_hidden_memory_tail_upper':bound,
        'only_two_completed_polar_channels':True,
        'source_high_projector_built':False,
        'source_delayed_resolvent_probes_computed':False,
        'first_window_Weil_sign_certified':False,'RH_proved':False}


def finite_hankel_nonnegative(moments, block_rank):
    """Hankel PSD for a scalar passive memory sequence (no source promotion)."""
    a=tuple(q(x) for x in moments)
    if type(block_rank) is not int or block_rank<1 or len(a)<2*block_rank-1:
        raise HiddenMemoryError("enough temporal moments and positive block rank required")
    M=tuple(tuple(a[i+j] for j in range(block_rank)) for i in range(block_rank))
    return {'hankel_matrix':M,'nonnegative':is_psd(M),
            'declared_rational_bath_only':True,'completed_Weil_sign_proved':False}


def explicit_cell_source_memory_budget(depth=64):
    """Explicit **453-cell**, source-derived high-memory telescope bound.

    The cell projection is NOT the jump spectral projection, hence mixed
    Gamma+FUCC coupling survives and is NOT rank two. Unlike the spectral P
    route it is exactly defined without computing an infinite eigenspace.

    Source-paper multiplier bound on |xi|>=1: h(xi)<=10+8|xi|^(1/4),
    and on |xi|<=1: h(xi)<18. For normalized cell indicator e_i,
    ||L e_i||^2<324+608*N, using its Fourier sinc tail and pi>3.
    ||(H-L)e_i||<9, hence ||H e_i||^2<810+1216*N.
    Thus ||P H Q||^2 <= N*(810+1216*N), with N=453.
    High signed D_cell >=9/16, hstep=16/9 => response tail
    < 16/9*N*(810+1216*N)*2^-depth =444268576*2^-depth.

    Paper/source-conditional estimate, NOT a numerical calculation of B or K.
    """
    if type(depth) is not int or depth<0:
        raise HiddenMemoryError("nonnegative integer source-memory depth")
    from .source_jump_spectral import authenticate_original_jump_rank_budget
    src=authenticate_original_jump_rank_budget()
    if (src['source_contract']['source_git_blob']!='0cc8510b71d178fc79e8d410a86d8b6014cf9178'
        or src['cell_rank_upper']!=453 or src['high_cell_complement_energy_floor']<=7
        or src['full_negative_budget_upper']!=F(103,16)):
        raise HiddenMemoryError("original source cell/Gamma source contract mismatch")
    n=453
    squared_coupling_cap=n*(810+1216*n)
    assert squared_coupling_cap==249901074
    base=F(16,9)*squared_coupling_cap
    assert base==F(444268576)
    return {
        'original_source_blob':src['source_contract']['source_git_blob'],
        'radius':F(1,2),
        'explicit_equal_cell_observation_rank':453,
        'observable_cell_mean_projection':True,
        'source_positive_carrier_memory_may_be_nonzero':True,
        'polar_cross_only':False,
        'signed_high_gap_lower':F(9,16),
        'rational_backward_euler_step':F(16,9),
        'cell_source_coupling_squared_cap':squared_coupling_cap,
        'depth':depth,
        'source_conditional_memory_tail_upper':base/F(2**depth),
        'actual_original_source_cell_cross_computed':False,
        'actual_original_source_memory_timeline_computed':False,
        'first_window_Weil_sign_proved':False,'RH_proved':False,
    }


def finite_cell_algebraic_budget(depth):
    """Source-independent Fraction arithmetic part; no original-source gate."""
    if type(depth) is not int or depth<0:raise HiddenMemoryError("nonnegative depth")
    n=453
    b=n*(810+1216*n)
    if b!=249901074 or b*16//9!=444268576:
        raise ArithmeticError("source paper integer budget drift")
    return {'rank':n,'squared_cross_cap':b,
            'tail_upper':F(444268576,2**depth),
            'source_verified':False}
