"""SUCC original source: finite Gamma OU bath + first-prime partial involution.

Research-only. Exact source-independent identities, rational interval/finite-model
oracles, and one SHA-gated source adapter. Never claims RH, full Weil positivity,
or that a finite Gamma prefix is the entire positive Archimedean tower.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


class FredholmError(ValueError):
    pass


def q(x):
    if type(x) not in (int, F):
        raise FredholmError('exact rational required: floats and booleans rejected')
    return F(x)


def mat(a):
    out=tuple(tuple(q(v) for v in row) for row in a)
    if not out or any(len(row)!=len(out[0]) for row in out):
        raise FredholmError('nonempty rectangular rational matrix required')
    return out


def eye(n):
    return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))


def trans(a):
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def mul(a,b):
    if len(a[0])!=len(b):
        raise FredholmError('matrix dimension mismatch')
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),F())
                       for j in range(len(b[0]))) for i in range(len(a)))


def add(a,b,c=1):
    c=q(c)
    if len(a)!=len(b) or any(len(x)!=len(y) for x,y in zip(a,b)):
        raise FredholmError('matrix sizes')
    return tuple(tuple(x+c*y for x,y in zip(row,col)) for row,col in zip(a,b))


def scale(a,c):
    c=q(c)
    return tuple(tuple(c*x for x in row) for row in a)


def dot(x,y):
    if len(x)!=len(y):raise FredholmError('vector sizes')
    return sum((q(a)*q(b) for a,b in zip(x,y)),F())


def apply(a,x):
    if len(a[0])!=len(x):raise FredholmError('matrix/vector sizes')
    return tuple(sum((z*q(v) for z,v in zip(row,x)),F()) for row in a)


def form(a,x):
    return dot(x,apply(a,x))


def det(a):
    a=mat(a);n=len(a)
    if n!=len(a[0]):raise FredholmError('square determinant')
    t=[list(r) for r in a]; d=F(1)
    for j in range(n):
        p=next((k for k in range(j,n) if t[k][j]),None)
        if p is None:return F(0)
        if p!=j:t[j],t[p]=t[p],t[j];d=-d
        pivot=t[j][j];d*=pivot
        for k in range(j+1,n):
            fac=t[k][j]/pivot
            for h in range(j+1,n):t[k][h]-=fac*t[j][h]
            t[k][j]=0
    return d


def psd(a):
    a=mat(a);n=len(a)
    if any(len(row)!=n for row in a) or a!=trans(a):
        raise FredholmError('symmetric square matrix required')
    # Exhaustive principal minors for small *exact finite controls*, not large source matrices.
    if n>7:raise FredholmError('exact finite-control PSD budget dimension <=7')
    return all(det(tuple(tuple(a[i][j] for j in ids) for i in ids))>=0
               for k in range(1,n+1) for ids in combinations(range(n),k))


def inverse(a):
    a=mat(a);n=len(a)
    if n!=len(a[0]):raise FredholmError('square inverse')
    aug=[list(a[i])+list(eye(n)[i]) for i in range(n)]
    for j in range(n):
        i=next((k for k in range(j,n) if aug[k][j]),None)
        if i is None:raise FredholmError('singular matrix')
        aug[j],aug[i]=aug[i],aug[j]
        v=aug[j][j]
        aug[j]=[x/v for x in aug[j]]
        for k in range(n):
            if k==j:continue
            f=aug[k][j]
            aug[k]=[x-f*y for x,y in zip(aug[k],aug[j])]
    return tuple(tuple(aug[i][n:]) for i in range(n))


def gamma_scalar_prefix(J):
    if type(J) is not int or J<1 or J>4096:
        raise FredholmError('positive genuine Gamma rung count 1..4096')
    return sum((F(4,4*j+1) for j in range(J)),F())


def source_baseline_threshold(J=8,N=64):
    """PAPER source conditional: original C<43/8, w2<1/2 and pi>3.

    For J>=8 Gamma prefix: H_J = B_J - sum E_(d/2) + poles.
    B_J = (c_J-C)I - w2 A_log2, B_J>=c_J-43/8-1/2 > 3/8.
    Replace sum E by cell compression: error <=2J/(pi N)<2J/(3N).
    The resulting lower operator is source faithful when interval entries
    and exact polar functions are authenticated; no sign is returned here.
    """
    if type(J) is not int or not 8<=J<=4096 or type(N) is not int or not N>=2:
        raise FredholmError('J>=8 and N>=2 exact input required')
    prefix=gamma_scalar_prefix(J)
    gap=prefix-F(43,8)-F(1,2)
    budget=F(2*J,3*N)
    trace=(F(J)+F(1,16))/gap
    if not prefix>F(25,4) or not gap>F(3,8):
        raise ArithmeticError('Gamma scalar authentic prefix proof failed')
    return {
      'first_prime_halfwidth':'1/2','true_source_coefficient_limits':'C<43/8;w2<1/2',
      'gamma_prefix_J':J,'gamma_scalar':str(prefix),
      'positive_swap_baseline_gap_strictly_greater':str(gap),
      'positive_prefix_compact_trace_exact':J,
      'polar_negative_trace_upper':'1/16',
      'number_of_negative_Gamma_prefix_modes_strictly_less_than':str(trace),
      'cell_count':N,'K_J_cell_compression_error_strictly_less_than':str(budget),
      'source_minus_cell_compact_baseline_gap_lower':str(gap-budget),
      'positive_compact_cell_lower_available':gap>budget,
      'full_source_sign_proved':False,'RH_proved':False,
    }


def first_prime_partial_swap(N,shift):
    """Exact N-cell shift when shift is an INTEGER cell offset.

    For N/2<shift<N the source-continuum analogue A_b^3=A_b.
    Distinguish this exact aligned finite model from irrational log2.
    """
    if type(N) is not int or N<3 or type(shift) is not int or not N/2<shift<N:
        raise FredholmError('strict first-prime birth region N/2 < shift < N')
    A=tuple(tuple(F(int(abs(i-j)==shift)) for j in range(N)) for i in range(N))
    if mul(mul(A,A),A)!=A:
        raise ArithmeticError('first-prime chiral cubic identity failed')
    return A


def cell_compressed_shift(N,b):
    """Exact irrational-lag representation for rational stand-in b in (1/2,1).

    The true source uses b=log 2 (irrational), authenticated separately. This
    matrix is P_N A_b P_N; its cube is GENERALLY NOT ITSELF. Do not apply the
    continuum inverse polynomial directly to this compression.
    """
    b=q(b)
    if type(N) is not int or N<3 or not F(1,2)<b<1:
        raise FredholmError('first-prime overlap source window')
    return tuple(tuple(max(F(0),1-abs(F(abs(i-j))-N*b)) for j in range(N)) for i in range(N))


def exact_swap_inverse(A,gamma,prime_weight):
    """Exact source-aligned functional calculus; A^3=A REQUIRED."""
    A=mat(A);n=len(A);gamma=q(gamma);w=q(prime_weight)
    if len(A[0])!=n or A!=trans(A) or mul(mul(A,A),A)!=A or not gamma>w>=0:
        raise FredholmError('source-aligned cubic swap and strictly positive baseline required')
    I=eye(n); A2=mul(A,A)
    #  (gamma I -w A)^-1 = I/gamma + w A/(gamma^2-w^2)
    #                          + w^2 A^2/[gamma(gamma^2-w^2)].
    inv=add(add(scale(I,1/gamma),scale(A,w/(gamma*gamma-w*w))),
            scale(A2,w*w/(gamma*(gamma*gamma-w*w))))
    if mul(add(scale(I,gamma),A,-w),inv)!=I:
        raise ArithmeticError('genuine cubic inverse identity failed')
    return inv


def finite_gamma_fredholm_model(A,gamma,w,K,c,s):
    """Exact rational finite counterpart of H_J = B - K +2cc* -2ss*.

    Checks 1) full signed matrix; 2) direct inverse of cubic source baseline;
    3) Sherman-Morrison even-polar compensation; 4) compact Birman-Schwinger
    trace necessary bound. This is NOT the frozen infinite Suzuki source.
    """
    A=mat(A);n=len(A);K=mat(K);gamma=q(gamma);w=q(w)
    if len(A)!=n or len(K)!=n or any(len(r)!=n for r in A+K) or K!=trans(K):
        raise FredholmError('complete finite rational source matrices')
    if len(c)!=n or len(s)!=n:raise FredholmError('source polar vectors length')
    c=tuple(q(x) for x in c);s=tuple(q(x) for x in s)
    if not psd(K):raise FredholmError('source OU kernel must be positive')
    Binv=exact_swap_inverse(A,gamma,w)
    B=add(scale(eye(n),gamma),A,-w)
    polarpos=tuple(tuple(2*c[i]*c[j] for j in range(n)) for i in range(n))
    polarneg=tuple(tuple(2*s[i]*s[j] for j in range(n)) for i in range(n))
    H=add(add(add(B,K,-1),polarpos),polarneg,-1)
    # B+ = B + 2cc*: its inverse remains explicit using Sherman-Morrison.
    v=apply(Binv,c);den=1+2*dot(c,v)
    Bplusinv=add(Binv,tuple(tuple(v[i]*v[j] for j in range(n)) for i in range(n)),-F(2)/den)
    if mul(add(B,polarpos),Bplusinv)!=eye(n):
        raise ArithmeticError('rank-one authentic-polar inverse failed')
    # Birman-Schwinger without matrix square roots: H>=0 iff Bplus-K-2ss>=0.
    Kneg=add(K,polarneg)
    Bplus=add(B,polarpos)
    gram=mul(Kneg,mul(Bplusinv,Kneg))
    bs=add(Kneg,gram,-1)
    # For PSD Kneg, Bplus-Kneg >=0 iff Kneg-Kneg Bplus^-1 Kneg>=0.
    # This follows by conjugation and equality of nonzero spectra (including
    # singular Kneg), and exact finite PSD is checked independently.
    same=psd(H)==psd(bs)
    if not same:raise ArithmeticError('Birman-Schwinger equivalence failure')
    return {
      'source_type':'EXACT_RATIONAL_FINITE_SURROGATE_NOT_SUZUKI',
      'full_signed_matrix':H,'compact_negative_kernel':Kneg,
      'rank_one_cosh_compensated_B_inverse':Bplusinv,
      'B_inverse_source_cubic_identity':True,
      'full_signed_positive':psd(H),'compact_Birman_Schwinger_positive':psd(bs),
      'signed_Birman_Schwinger_matrix':bs,
      'original_source_sign_proved':False,'RH_proved':False,
    }


@dataclass(frozen=True)
class RationalInterval:
    lo:F
    hi:F
    def __post_init__(self):
        if type(self.lo) is not F or type(self.hi) is not F or self.lo>self.hi:
            raise FredholmError('outward exact Fraction intervals required')


def exp_minus_interval(x):
    """Proof-producing elementary rational Taylor exponential for 0<=x<=64."""
    x=q(x)
    if x<0 or x>64:raise FredholmError('range for rational exponential Taylor')
    m=0;t=x
    while t>F(1,2):t/=2;m+=1
    term=F(1);total=F(1)
    for j in range(1,41):term*=t/j;total+=term
    tail=term*t/41/(1-t/42)
    lo,hi=total,total+tail
    for _ in range(m):lo=lo*lo;hi=hi*hi
    return RationalInterval(1/hi,1/lo)


def ou_cell_integral(alpha,h,offset,exp_eval=exp_minus_interval):
    """Authenticated-form OU cell-average matrix element, interval exact.

    Matrix M_ii=2/alpha -2(1-e^-alpha h)/(alpha^2*h).
    M_i,i+k=(1-e^-alpha h)^2 e^-alpha (k-1)h/(alpha^2*h).
    Valid for equal cell indicators normalized in L2, including adjacent k=1.
    """
    alpha=q(alpha);h=q(h)
    if alpha<=0 or h<=0 or type(offset) is not int or offset<0:
        raise FredholmError('positive alpha/h and nonnegative integral lag')
    ep=exp_eval(alpha*h)
    if not isinstance(ep,RationalInterval):raise FredholmError('trusted outward exp interval expected')
    lo_t,hi_t=1-ep.hi,1-ep.lo
    if offset==0:
        return RationalInterval(2/alpha-2*hi_t/(alpha*alpha*h),
                                2/alpha-2*lo_t/(alpha*alpha*h))
    ef=exp_eval(alpha*h*(offset-1))
    denom=alpha*alpha*h
    return RationalInterval(lo_t*lo_t*ef.lo/denom, hi_t*hi_t*ef.hi/denom)


def gamma_cell_interval_matrix(J,N,exp_eval=exp_minus_interval):
    """Finite ORIGINAL Gamma OU compact-prefix cell matrix, not entire Gamma.

    Every interval encloses <e_i, sum_(j<J) exp(-d_j|x-y|/2) e_k>.
    These entries are not by themselves an infinite-dimensional sign proof.
    """
    if type(J) is not int or not 1<=J<=40 or type(N) is not int or not 2<=N<=32:
        raise FredholmError('small exact trial constraints J<=40, N<=32')
    h=F(1,N)
    table=[]
    for off in range(N):
        z=[ou_cell_integral(F(4*j+1,2),h,off,exp_eval) for j in range(J)]
        table.append(RationalInterval(sum((x.lo for x in z),F()),sum((x.hi for x in z),F())))
    return tuple(tuple(table[abs(i-k)] for k in range(N)) for i in range(N))


def source_authenticated_fredholm_packet(J=8,N=8):
    """Source SHA gate; ORIGINAL first-prime contact, half-density and Gamma.

    Replays exact interval OU prefix matrix for bounded N/J; certifies baseline
    gap, original prime partial shift regime and rational compact error.
    It does not evaluate an infinite Fredholm determinant or claim RH.
    """
    if type(J) is not int or not 8<=J<=16 or type(N) is not int or not 4<=N<=10:
        raise FredholmError('source replay budgets only J=8..16,N=4..10')
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from . import source_weil_hierarchy as src
    contract=verify_original_suzuki_source()
    if src.authenticated_prime_wavefront(F(1,2))!=((2,2),):
        raise FredholmError('only genuine prime-2 true wavefront at first window')
    C=src.contact_iv(); w=src.log2_iv()*src.sqrt_inverse(2); b=src.log2_iv()
    if not (F(1,2)<b.lo<=b.hi<1 and 0<C.lo<=C.hi<F(43,8) and 0<w.lo<=w.hi<F(1,2)):
        raise FredholmError('original source bounds unexpected')
    def sourceexp(x):
        val=src.exp_neg(x)
        return RationalInterval(val.lo,val.hi)
    cells=gamma_cell_interval_matrix(J,N,sourceexp)
    q0=source_baseline_threshold(J,N)
    # The SOURCE-CALIBRATED trace bound is tighter than the coarse C,w caps:
    # K_J has trace J, and 2||s||² <1/16 in the original interval.
    effective_gap=gamma_scalar_prefix(J)-C.hi-w.hi
    trace_bound=(F(J)+F(1,16))/effective_gap
    if effective_gap <=0 or (J==8 and not trace_bound<20):
        raise FredholmError('source-trace negative-index budget failed')
    from .suzuki_legendre_source import authentic_full_low_entry
    p1_8=authentic_full_low_entry(1,1,F(1,2),8)
    p1_18=authentic_full_low_entry(1,1,F(1,2),18)
    p1_19=authentic_full_low_entry(1,1,F(1,2),19)
    p1_64=authentic_full_low_entry(1,1,F(1,2),64)
    if not (p1_8.hi < p1_18.hi < 0 < p1_19.lo < p1_64.lo):
        raise FredholmError('frozen source Gamma-clock P1 sign flip at rung 19 failed')
    return {
      'source_type':'AUTHENTIC_SUZUKI_GAMMA_PRIME_FINITE_PREFIX',
      'source_sha':contract['source_git_blob'],
      'original_source_contact_interval':(str(C.lo),str(C.hi)),
      'true_prime_weight_interval':(str(w.lo),str(w.hi)),
      'original_prime_log_clock_interval':(str(b.lo),str(b.hi)),
      'source_gamma_rung_count':J,
      'exact_first_prime_cubic_identity_paper':True,
      'gamma_compact_cell_matrix_trace_interval':(str(sum((cells[i][i].lo for i in range(N)),F())),
                                                   str(sum((cells[i][i].hi for i in range(N)),F()))),
      'one_offdiag_cell_integral_interval':(str(cells[0][1].lo),str(cells[0][1].hi)),
      'cell_source_error_upper':q0['K_J_cell_compression_error_strictly_less_than'],
      'genuine_Gamma8_original_P1_interval':(str(p1_8.lo),str(p1_8.hi)),
      'genuine_Gamma18_original_P1_interval':(str(p1_18.lo),str(p1_18.hi)),
      'genuine_Gamma19_original_P1_interval':(str(p1_19.lo),str(p1_19.hi)),
      'Gamma_P1_first_certified_positive_rung':19,
      'genuine_Gamma64_original_P1_interval':(str(p1_64.lo),str(p1_64.hi)),
      'P1_positive_after_true_64_modes_but_negative_with_8':True,
      'true_finite_Gamma_prefix_negative_index_upper_at_J8':19,
      'negative_index_trace_upper_rational':str(trace_bound),
      'source_prefix_signed_positivity_certified':False,
      'original_Schur_sign_proved':False,'RH_proved':False,
    }


def source_original_four_mode_gamma_clock():
    """Source-authenticated first Γ-rung positivity for each original P1..P4.

    Discovery targets 19/10/20/7 were selected by an independent, explicitly
    NON-CERTIFIED scipy integral. This checker derives all eight strict sign
    inequalities from ORIGINAL frozen completed Q-zeta Suzuki interval entries.
    Every genuine Γ rung is PSD, so bracketing J-1<0<J proves first-positive J
    without silently checking all earlier integer J or using nontrivial zeros.
    DOES NOT prove the 4x4 low Gram PSD or Schur sign.
    """
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from .suzuki_legendre_source import authentic_full_low_entry
    contract=verify_original_suzuki_source()
    from . import source_weil_hierarchy as src
    if src.authenticated_prime_wavefront(F(1,2))!=((2,2),):
        raise FredholmError('fake independent Euler source / wrong prime window')
    crosses=((1,19),(2,10),(3,20),(4,7))
    report=[]
    for mode,J in crosses:
        before=authentic_full_low_entry(mode,mode,F(1,2),J-1)
        after=authentic_full_low_entry(mode,mode,F(1,2),J)
        if not (before.hi<0<after.lo):
            raise FredholmError(f'authentic Gamma-clock rung {mode},{J} was not rigorously certified')
        report.append({'true_original_low_mode':mode,
                       'first_strictly_positive_gamma_rungs':J,
                       'previous_true_source_energy_interval':(str(before.lo),str(before.hi)),
                       'crossed_true_source_energy_interval':(str(after.lo),str(after.hi)),
                       'completed_Gamma_tail_kept_positive':True,
                       'four_low_Gram_positive_proved_here':False})
    return {'source_sha':contract['source_git_blob'],
            'original_signed_completed_polar_pair_retained':True,
            'genuine_four_mode_first_positive_clock':tuple(report),
            'no_nontrivial_zeta_zero_coordinates':True,
            'original_full_Schur_sign_proved':False,'RH_proved':False}
