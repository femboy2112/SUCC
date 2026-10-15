"""One-object zero-shift Suzuki residual certificates (RH remains OPEN).

Pure Fraction finite block verifiers are SYNTHETIC calibrations.  The separate
original_source_contract uses the exact archived zeta Suzuki object from PR85,
Tate's genuine zeta source profile, and PR106's finite contact reconciliation.

The infinite-dimensional theorems, including the Sobolev kernel estimate,
are proved in research/2026-10-15/ONE_OBJECT_RESIDUAL_SHORTING.md, not by code.
No nontrivial zero coordinates are used.  No positive surrogate is substituted.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from hashlib import sha1
from pathlib import Path

ORIGINAL_SUZUKI_BLOB = "0cc8510b71d178fc79e8d410a86d8b6014cf9178"
KAPPA = F(369, 10000)
FIRST_WINDOW_A = F(1, 2)
PR104_HEAD = "88eca261bae1381b83d018163d0945c3434a3385"
PR106_PARENT = "04b6d8ede12c58afe4a244b11297663c33260de1"


class ResidualShortingError(ValueError):
    pass


def exact(x):
    if type(x) not in (int, F):
        raise ResidualShortingError("Source/math certificate requires exact int/Fraction, not bool/float")
    return F(x)


def matrix(rows):
    if type(rows) not in (tuple, list) or not rows:
        raise ResidualShortingError("Nonempty rational matrix required")
    m = tuple(tuple(exact(x) for x in row) for row in rows)
    if not m[0] or any(len(row) != len(m[0]) for row in m):
        raise ResidualShortingError("Rectangular matrix required")
    return m


def dims(a):
    return len(a), len(a[0])


def trans(a):
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def mul(a, b):
    if len(a[0]) != len(b):
        raise ResidualShortingError("Invalid domain/codomain for source morphism")
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), F())
                       for j in range(len(b[0]))) for i in range(len(a)))


def add(a, b, sign=1):
    s = exact(sign)
    if dims(a) != dims(b):
        raise ResidualShortingError("Incompatible source matrix dimensions")
    return tuple(tuple(a[i][j]+s*b[i][j] for j in range(len(a[0])))
                 for i in range(len(a)))


def scale(a, factor):
    s=exact(factor)
    return tuple(tuple(s*x for x in row) for row in a)


def eye(n):
    if type(n) is not int or not 1 <= n <= 12:
        raise ResidualShortingError("Finite rational test dimension 1..12")
    return matrix(tuple(tuple(int(i==j) for j in range(n)) for i in range(n)))


def is_symmetric(a):
    return len(a)==len(a[0]) and a==trans(a)


def det(a):
    if len(a)!=len(a[0]):
        raise ResidualShortingError("Determinant requires square matrix")
    a=[list(row) for row in a]
    n=len(a); val=F(1)
    for j in range(n):
        pivot=next((k for k in range(j,n) if a[k][j]), None)
        if pivot is None:
            return F(0)
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
            val=-val
        p=a[j][j]
        val*=p
        for k in range(j+1,n):
            c=a[k][j]/p
            for l in range(j+1,n):
                a[k][l]-=c*a[j][l]
            a[k][j]=F(0)
    return val


def psd(a):
    """Exact PSD via all principal minors; bounded finite control (n<=6)."""
    a=matrix(a)
    if not is_symmetric(a) or len(a)>6:
        raise ResidualShortingError("Real symmetric source matrix, <=6, required")
    return all(det(tuple(tuple(a[i][j] for j in indices) for i in indices))>=0
               for n in range(1,len(a)+1)
               for indices in combinations(range(len(a)),n))


def inverse(a):
    a=matrix(a)
    if not is_symmetric(a):
        raise ResidualShortingError("Symmetric finite Hilbert metric required")
    n=len(a)
    z=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next((k for k in range(j,n) if z[k][j]),None)
        if pivot is None:raise ResidualShortingError("Singular high metric/inverse")
        z[j],z[pivot]=z[pivot],z[j]
        p=z[j][j]
        z[j]=[t/p for t in z[j]]
        for k in range(n):
            if k==j:continue
            v=z[k][j]
            z[k]=[z[k][q]-v*z[j][q] for q in range(2*n)]
    return matrix(tuple(tuple(row[n:]) for row in z))


def rayleigh(a, x):
    x=tuple(exact(v) for v in x)
    if len(a)!=len(a[0]) or len(a)!=len(x) or not any(x):
        raise ResidualShortingError("Nonzero exact test vector on correct carrier")
    return sum((x[i]*a[i][j]*x[j] for i in range(len(x)) for j in range(len(x))),F())/sum((v*v for v in x),F())


@dataclass(frozen=True)
class FiniteResidualCertificate:
    """Signed scalar/MATRIX Schur bracket on finite declared toy high space.

    A=PGP, B=PGQ, D=QGQ, K=Q(-Delta_N)^(-1)Q calibration;
    H maps low to a trial high solution. K is positive definite in finite model.
    No row of this dataclass is an original zeta coefficient.
    """
    low: tuple[tuple[F,...],...]
    cross: tuple[tuple[F,...],...]
    high: tuple[tuple[F,...],...]
    inverse_neumann: tuple[tuple[F,...],...]
    trial: tuple[tuple[F,...],...]
    kappa: F
    lower_schur: tuple[tuple[F,...],...]
    upper_schur: tuple[tuple[F,...],...]
    exact_short: tuple[tuple[F,...],...]
    lower_resolvent: tuple[tuple[F,...],...]
    upper_resolvent: tuple[tuple[F,...],...]
    residual: tuple[tuple[F,...],...]
    mathematically_synthetic: bool = True
    RH_proved: bool = False


def finite_residual_certificate(A, B, D, K, H, kappa):
    """Exact source-NEUTRAL matrix verifier of the infinite-domain theorem.

    L=BH+H*B*-H*DH <= R0=B D^-1 B* <= L+1/k R*K^-1*R.
    This only runs finite rational block matrices and assumes verified D>=k K.
    Authentic infinite dimensions require the paper Sobolev argument.
    """
    A,B,D,K,H=map(matrix,(A,B,D,K,H))
    k=exact(kappa)
    r,s=dims(B)
    if not (0<k and 1<=r<=5 and 1<=s<=6 and dims(A)==(r,r)
            and dims(D)==(s,s) and dims(K)==(s,s) and dims(H)==(s,r)):
        raise ResidualShortingError("Bad low/high source dimensions or positivity constant")
    if not (is_symmetric(A) and is_symmetric(D) and is_symmetric(K)):
        raise ResidualShortingError("Authentic signed source blocks must be selfadjoint")
    if not psd(add(D,scale(K,k),-1)):
        raise ResidualShortingError("High source positivity D>=k K NOT established")
    if not psd(K) or det(K)==0:
        raise ResidualShortingError("Invalid high derivative metric K")
    bh=mul(B,H)
    hd=mul(trans(H),mul(D,H))
    lowR=add(add(bh,trans(bh)),hd,-1)
    residual=add(trans(B),mul(D,H),-1)
    derivGram=mul(trans(residual),mul(inverse(K),residual))
    upperR=add(lowR,scale(derivGram,1/k))
    actualR=mul(B,mul(inverse(D),trans(B)))
    trueShort=add(A,actualR,-1)
    lowShort=add(A,upperR,-1)
    highShort=add(A,lowR,-1)
    assert psd(add(actualR,lowR,-1))
    assert psd(add(upperR,actualR,-1))
    assert psd(add(trueShort,lowShort,-1))
    assert psd(add(highShort,trueShort,-1))
    return FiniteResidualCertificate(A,B,D,K,H,k,lowShort,highShort,trueShort,lowR,upperR,residual)


def original_source_cancellation_certificate(cells=4096):
    """Recompute source-correct signed cancellation, never trust decimals.

    g' = -4 sinh(r/2) + C_G/2 + (log 2)/sqrt(2) 1_(r>log 2)
         -atanh(e^(-r/2))-atan(e^(-r/2)), for 0<r<=1.

    All constants/function ranges are outward Fraction intervals, using
    fixed source Gamma contact, true p2 wavefront and an analytic bound for
    the logarithmic r=0 cell. See proof dossier for rigor and limitations.
    """
    from .signed_gprime_enclosure import original_first_window_l1_certificate
    if type(cells) is not int or cells < 4096:
        raise ResidualShortingError('Sharp source certificate requires >=4096 verified cells')
    r=original_first_window_l1_certificate(cells)
    if not (r['source']=='ORIGINAL_ZETA_GAMMA_CONTACT_POLES_PRIME2'
            and r['gprime_L1_STRICT_upper'] < F(11,40)
            and r['gprime_L2_squared_STRICT_upper'] < F(4,25)
            and r['gprime_L1_lower']>F(1,4)):
        raise ResidualShortingError('SOURCE-CANCELLATION_CERTIFICATION_FAILED')
    return r


def original_first_window_source_budget():
    """Two independently proved analytic source-norm budgets at a=1/2.

    A coarse triangle inequality gives ||g'||L1<65/3<22 and L2<16.
    Exact contact/Γ/pole/prime2 *cancellation* interval proof strengthens
    both to ||g'||L1<11/40 and ||g'||L2<2/5.  No zero coordinates.
    """
    certified=original_source_cancellation_certificate()
    return {'a':F(1,2), 'true_primitive_prime':2,
            'original_suzuki_blob':ORIGINAL_SUZUKI_BLOB,
            'coarse_gamma_L1_upper':F(10),'coarse_pole_L1_upper':F(8,3),
            'coarse_contact_L1_upper':F(8),'coarse_prime_L1_upper':F(1),
            'coarse_gprime_L1_upper':F(65,3),
            'sharpened_gprime_L1_strict_upper':F(11,40),
            'sharpened_gprime_L2_strict_upper':F(2,5),
            'exact_cell_certificate':certified,
            'kappa':KAPPA,
            'coarse_resolvent_operator_norm_upper':F(22*22)/KAPPA,
            'resolvent_operator_norm_strict_upper':F(11,40)**2/KAPPA,
            'no_spectral_gap_claimed':True,'RH_proved':False}


def hilbert_signed_operator_norm_budget(depth, gamma_modes, source_original=True):
    """Authentic first-window dyadic signed CELL-AVERAGE operator bound.

    ||G-E_N G_J E_N||_op < (4/5)/N + tau_J,
    N=2^depth, tau_J=1/(4J+1)+4/(4J+1)^2.

    This uses a true Fraction certificate of ||g'||L2<2/5 and 2-axis
    dyadic Poincare, not invalid midpoint quadrature at Gamma's diagonal.
    The finite-J CELL INTEGRALS from PR105 must be used, not midpoints.
    """
    if type(depth) is not int or not 1<=depth<=30:
        raise ResidualShortingError('Hilbert dyadic stage must be exact depth 1..30')
    if type(gamma_modes) is not int or not 1<=gamma_modes<=10**7:
        raise ResidualShortingError('Positive finite authentic Gamma depth required')
    if source_original is not True:
        raise ResidualShortingError('No counterfeit source allowed into signed norm certificate')
    certified=original_source_cancellation_certificate()
    N=2**depth;J=gamma_modes
    tail=F(1,4*J+1)+F(4,(4*J+1)**2)
    return {'Hilbert_depth':depth,'tiles':N*N,'cell_width':F(1,N),
            'kernel_H1_projection_error_strict_upper':F(4,5*N),
            'authentic_gamma_tail_upper':tail,
            'total_signed_operator_error_strict_upper':F(4,5*N)+tail,
            'signed_gprime_L2_squared_cell_upper':certified['gprime_L2_squared_STRICT_upper'],
            'requires_original_signed_source_cell_integrals':True,
            'is_operator_norm_not_just_pointwise':True,'RH_proved':False}


def hilbert_scan(depth):
    """Finite Hilbert XY visit permutation, not a positivity operator."""
    if type(depth) is not int or not 0<=depth<=7:
        raise ResidualShortingError("Finite Hilbert scan depth 0..7")
    N=2**depth
    xy=[]
    def rot(s,x,y,rx,ry):
        if ry==0:
            if rx==1:x,y=s-1-x,s-1-y
            x,y=y,x
        return x,y
    for d in range(N*N):
        t=d;x=y=0;s=1
        while s<N:
            rx=1&(t//2);ry=1&(t^rx)
            x,y=rot(s,x,y,rx,ry)
            x+=s*rx;y+=s*ry
            t//=4;s*=2
        xy.append((x,y))
    return tuple(xy)


def signed_hilbert_matrix_sum(a, depth):
    """Finite source-neutral signed observable: Hilbert order = row-major.

    Does NOT imply positive matrices or original Weil source by itself.
    """
    a=matrix(a)
    N=2**depth
    if dims(a)!=(N,N):
        raise ResidualShortingError("Signed tile matrix must fit Hilbert dyadic square")
    return sum((a[x][y] for x,y in hilbert_scan(depth)),F()),sum((v for row in a for v in row),F())


def parent_original_source_contract():
    """Live exact-head authenticity gate, fails closed outside stacked checkout.

    Checks the current PR106 Tate profile + finite Weil contact + original
    PR85 source evaluator through a strict SHA-pinned source adapter.
    Does NOT assert trace/Weil positivity, only identity of source labels.
    """
    from .suzuki_legendre_source import _pinned_source
    from .tate_weil_source_bridge import TateWeilProfile
    from .one_object_transport import contact_rational_increment
    source=_pinned_source()
    if sha1(b'blob '+str(Path(source.__file__).stat().st_size).encode()+b'\0'+Path(source.__file__).read_bytes()).hexdigest()!=ORIGINAL_SUZUKI_BLOB:
        raise ResidualShortingError("True PR85 source blob differs")
    profile=TateWeilProfile.canonical('zeta')
    if (profile.conductor!=1 or profile.parity!=0 or profile.has_completed_poles is not True
            or profile.half_density!=F(1,2) or profile.root_number!=1):
        raise ResidualShortingError("Tate/Suzuki conductor, Gamma, pole or half-density mismatch")
    if contact_rational_increment(1)!=F(4)-F(2):
        raise ResidualShortingError("Real contact normalization disagreement")
    if source.assert_original_source_tape() is not True:
        raise ResidualShortingError("Prime-power source not authenticated")
    from .signed_gprime_enclosure import (original_contact_interval,
                                          original_primitive_interval)
    # Two completely different source derivations of the genuine value at
    # r=1/4 MUST agree: original infinite-contact g_J with the omitted
    # negative Gamma modes versus the source's exact-rational derivative
    # (Tate/real contact + one Gamma + genuine p2) integrated from g(0)=0.
    contact=original_contact_interval()
    original=source.contact_iv()
    if contact[1]<original.lo or original.hi<contact[0]:
        raise ResidualShortingError('Real Tate/Suzuki contact profiles disjoint')
    at=F(1,4)
    v=source.screw_interval(at,128)
    whole=(v.lo-source.gamma_tail(128),v.hi)
    primitive=original_primitive_interval(at,512)
    if whole[1]<primitive[0] or primitive[1]<whole[0]:
        raise ResidualShortingError('ORIGINAL source g and integral of gprime disagree')
    if not (whole[0]+at/2>primitive[1]):
        raise ResidualShortingError('Contact +1 mutation not excluded')
    return {"zeta_profile":"CONDUCTOR1_EVEN_TRUE_PRIME_ONLY",
            "source_git_blob_sha":ORIGINAL_SUZUKI_BLOB,
            "true_half_density":F(1,2),"true_gamma_once":True,
            "contact_one_mode_increment":contact_rational_increment(1),
            "original_screw_value_checked_against_derivative":True,
            "wrong_contact_mutation_rejected":True,
            "Connes_global_trace_identified":False,"Weil_positivity_proved":False}


def schema_receipt():
    """Deterministic exact rational finite experiments + unresolved source gate."""
    K=matrix(((F(1,4),0),(0,F(1,9))))
    D=matrix(((F(1,2),0),(0,F(1,3))))
    B=matrix(((F(1,4),F(1,6)),))
    R=F(5,24)
    A=matrix(((R+F(1,120),),))
    zero=matrix(((0,),(0,)))
    correct=matrix(((F(1,2),),(F(1,2),)))
    z=finite_residual_certificate(A,B,D,K,zero,F(1,2))
    w=finite_residual_certificate(A,B,D,K,correct,F(1,2))
    budget=hilbert_signed_operator_norm_budget(8,32)
    return {"source":"SYNTHETIC_FINITE_BLOCK_PLUS_SEPARATE_AUTHENTIC_ANALYTIC_THEOREM",
            "trial_zero_lower_schur":z.lower_schur[0][0],
            "trial_correct_lower_schur":w.lower_schur[0][0],
            "trial_correct_upper_schur":w.upper_schur[0][0],
            "actual_schur":w.exact_short[0][0],
            "gprime_L1_upper":original_first_window_source_budget()["sharpened_gprime_L1_strict_upper"],
            "cross_resolvent_upper":original_first_window_source_budget()["resolvent_operator_norm_strict_upper"],
            "hilbert_stage":budget,"one_object_source_contract_requires_checkout":True,
            "RH_proved":False}
