"""Source-faithful BBP analytic-tail and Fourier-ladder observation laboratory.

Research-only exact rational certificates. No pi digit inputs, no normality claim.
The nontrivial analytic statements are proved in PROOFS.md, not by finite tests.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import lcm


def authentic_r(n: int) -> Q:
    """The original unmodified FOUR signed BBP Mellin terms."""
    if type(n) is not int or n < 1:
        raise ValueError('positive original source time required')
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def positive_source_cap(n: int) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError('positive original source time required')
    return Q(15,(8*n-7)*(8*n-6))


def gamma_tail_cap(n: int) -> Q:
    """Inherited genuine 0<T_n<B(n), no pi digits as inputs."""
    if type(n) is not int or n < 1:
        raise ValueError('positive original source time required')
    return Q(1,(8*n+1)*(8*n+2))


def original_phases(last_n: int) -> tuple[Q,...]:
    """Q/Z phases only. Unwrapped integers NOT available from these outputs."""
    if type(last_n) is not int or last_n < 0:
        raise ValueError('nonnegative finite horizon')
    x=Q(0)
    out=[x]
    for n in range(1,last_n+1):
        x=(16*x+authentic_r(n))%1
        if x.denominator%2!=1:
            raise AssertionError('original denominator is not odd')
        out.append(x)
    return tuple(out)


def modular_original_phases(last_n: int) -> tuple[Q,...]:
    """Independent source path: one common odd denominator, integer recursion."""
    if type(last_n) is not int or last_n < 0:
        raise ValueError('nonnegative finite horizon')
    source=tuple(authentic_r(n) for n in range(1,last_n+1))
    M=1
    for f in source:
        M=lcm(M, f.denominator)
    if M%2!=1:
        raise AssertionError('source denominator must be odd')
    z=0
    out=[Q(0)]
    for f in source:
        z=(16*z+f.numerator*(M//f.denominator))%M
        out.append(Q(z,M))
    return tuple(out)


def ward_ladder_bound(A: int, h: int, j: int) -> Q:
    """Rigorous algebraic bound with 2*pi < 44/7, valid all A>=2.

    |c_A(16^j*h)-c_A(h)| <= 2j/A + pi*|h|(16^j-1)/(32A^2).
    Here c_A(h)=A^-1 sum_{n=A}^{2A-1}e(hU_n).
    """
    if type(A) is not int or A<2 or type(h) is not int or type(j) is not int or j<0:
        raise ValueError('A>=2, h integer, j>=0')
    return Q(2*j,A) + Q(22,7)*abs(h)*Q(16**j-1,32*A*A)


def band_depth(q: int, h: int) -> int:
    """Largest j>=0 with |h|*16^j<=q/2; -1 if none."""
    if type(q) is not int or q<2 or type(h) is not int or h==0:
        raise ValueError('q>=2, nonzero integer h')
    depth=-1
    x=abs(h)
    while 2*x<=q:
        depth+=1
        x*=16
    return depth


def ward_visibility_certificate(A:int,q:int,h:int,epsilon:Q)->dict:
    """Source-conditional lower bound on J_(A,q)-1, for one witnessed c_A(h).

    If a separately certified |c_A(h)|>=epsilon and the source Ward bound
    through L is <epsilon/2, then J-1 >=2*(7/22)^2 * epsilon^2*(L+1).
    This does NOT certify the antecedent for the original source.
    """
    epsilon=Q(epsilon)
    if not 0<epsilon<=1:raise ValueError('declared hypothesis 0<epsilon<=1')
    L=band_depth(q,h)
    if L<0:return {'useful':False,'reason':'no frequency fits in q/2'}
    bound=ward_ladder_bound(A,h,L)
    if not bound<epsilon/2:
        return {'useful':False,'reason':'ward error has not been paid','L':L,'ward_upper':bound}
    lower=Q(2)*(Q(7,22)**2)*epsilon**2*(L+1)
    return {'useful':True,'L':L,'ward_upper':bound,
            'premise':'separately certify selected |c_A(h)|>=epsilon',
            'conditional_J_minus_one_lower':lower,
            'source_normality_proved':False}


def completion_epoch_coeff_upper(A:int,h:int)->Q:
    """|c_A^X(h)-c_A^U(h)| < pi*|h|/(32 A^2) < this bound.

    X_n=16^n*pi/16, T_n=X_n-U_n. Analytic T_n<1/(64n^2).
    """
    if type(A) is not int or A<1 or type(h) is not int:
        raise ValueError('A>=1 and h integer')
    return Q(22,7)*Q(abs(h),32*A*A)


def completion_band_square_energy_upper(A:int,H:int)->Q:
    """Sum_{1<=|h|<=H} ||c_X(h)|^2-|c_U(h)|^2| is below this."""
    if type(H) is not int or H<0:raise ValueError('H>=0')
    return Q(22,7)*Q(H*(H+1),16*A*A)


def weighted_fourier_tail_upper(q:int,H:int)->Q:
    """Strict universal sinc-square high-frequency tail using pi>3."""
    if type(q) is not int or q<2 or type(H) is not int or H<1:
        raise ValueError('q>=2,H>=1')
    return Q(2*q*q,9*H)


def finite_prefix_shadow_error(A:int,h:int)->Q:
    """Absolute epoch-AVERAGED phase transport to alpha_(2A)=U_(2A)/16^(2A).

    Source-only exact bound: 2*pi*|h|*T_(2A)/(15*A).
    The rational prefix itself is not claimed normal or equidistributed.
    """
    if type(A) is not int or A<1 or type(h) is not int:
        raise ValueError('A>=1,h integer')
    M=2*A
    return Q(44,7)*abs(h)*gamma_tail_cap(M)/Q(15*A)


def champernowne16_prefix(digits:int)->Q:
    """Terminating rational prefix of classical base16-normal Champernowne number.

    Its normality is an IMPORTED classical theorem, not established here.
    """
    if type(digits) is not int or not 1<=digits<=500:
        raise ValueError('declared finite prefix length 1..500')
    seq=''
    j=1
    while len(seq)<digits:
        x=j
        s=''
        while x:
            s='0123456789abcdef'[x%16]+s
            x//=16
        seq+=s
        j+=1
    return Q(int(seq[:digits],16),16**digits)


def triangle_energy(phases:tuple[Q,...],q:int)->Q:
    """Selected source triangular energy: exact rational, no surrogate Haar."""
    if not phases or type(q) is not int or q<2:
        raise ValueError('nonempty source phases, mesh>=2')
    N=len(phases)
    return Q(q,N*N)*sum((max(Q(0),1-q*min((x-y)%1,(y-x)%1))
                for x in phases for y in phases),Q(0))


def coherent_fixed_point(q:int,count:int=32)->Q:
    if type(count) is not int or count<1:raise ValueError('count>=1')
    return triangle_energy((Q(1,5),)*count,q)


# The following is an ANALYTIC OBSERVER TOOL. It is NOT source-based mixing.

def nb2_partial_mass(r:Q, last:int)->Q:
    """Sum of the first last negative-binomial Gamma(2) Abel weights.

    P(N=n)=(n+1)(1-r)^2 r^n, 0<=r<1, n>=0.
    """
    r=Q(r)
    if not Q(0)<=r<1 or type(last) is not int or last<0:
        raise ValueError('r in [0,1), last nonnegative integer')
    return sum(((n+1)*(1-r)**2*r**n for n in range(last)),Q(0))


def nb2_tail_mass(r:Q,last:int)->Q:
    """EXACT omitted Gamma(2)/negative-binomial mass after n=last-1."""
    r=Q(r)
    if not Q(0)<=r<1 or type(last) is not int or last<0:
        raise ValueError('r in [0,1), last nonnegative integer')
    return r**last*((last+1)-last*r)


def abel_cesaro_finite_identity(values:tuple[Q,...],r:Q)->dict:
    """Exact finite-input Abel=C(1) Gamma(2)-weighted prefix identity.

    Extend the declared finite a_n by 0 for n>=M. The NB2 mixture
    includes the INFINITE tail of its prefix means S_n/(n+1), with
    omitted part summed exactly; no random source assumption.
    """
    r=Q(r)
    if not values or not Q(0)<=r<1:
        raise ValueError('nonempty declared finite values and r in [0,1)')
    a=tuple(Q(x) for x in values)
    M=len(a)
    partial=Q(0)
    weighted=Q(0)
    for n,v in enumerate(a):
        partial+=v
        weighted+=(1-r)**2*r**n*partial
    future=(1-r)*r**M*partial
    abel=(1-r)*sum((v*r**n for n,v in enumerate(a)),Q(0))
    assert abel==weighted+future
    return {'abel_mean':abel,'finite_gamma_weighted_means':weighted,
            'exact_future_prefix_tail':future,
            'mixture_total':weighted+future,'finite_values_used':M}


def boundary_ghost(M:int,z:Q)->dict:
    """Analytic interior vanishing != boundary residue. F_M=z^M/(1-z)."""
    if type(M) is not int or M<0 or not Q(0)<=Q(z)<1:
        raise ValueError('M nonnegative, 0<=z<1')
    z=Q(z)
    f=z**M/(1-z)
    return {'function':f,'normalized_boundary_expression':(1-z)*f,
            'exact_equal_to_z_power_M':(1-z)*f==z**M,
            'first_M_Taylor_coefficients_zero':True,
            'fixed_M_boundary_residue':Q(1)}


def unit_phase_boundary_difference(M:int,z:Q)->Q:
    """Difference of valid ±1 Fourier character streams equal through M-1.

    First stream a_n=+1 all n. Second stream b_n=+1 n<M, -1 n>=M.
    Their generating-function difference b-a = -2 z^M/(1-z).
    """
    return -2*boundary_ghost(M,z)['function']


def gamma2_scaled_mean(r:Q)->Q:
    """For NB2 P(N=n)=(n+1)(1-r)^2 r^n, E[(1-r)(N+1)]=1+r."""
    r=Q(r)
    if not Q(0)<=r<1:raise ValueError('r in [0,1)')
    return 1+r


def gamma_tail_abel_boundary_upper(h:int,r:Q)->Q:
    """Rigorous source-only upper on |(1-r)(F_X-F_U)|.

    Uses |e(hX_n)-e(hU_n)|<=2*pi*|h|T_n,
    T_n<1/(64n^2), sum_(n>=1)1/n^2<2, pi<22/7.
    Does not bound (1-r)*F_U itself.
    """
    r=Q(r)
    if type(h) is not int or not Q(0)<=r<1:
        raise ValueError('integer harmonic, r in [0,1)')
    return (1-r)*Q(22,7)*Q(abs(h),16)


def analytic_ward_source_error_bound(h:int,r:Q)->Q:
    """Source-only rigorous upper on |r(1-r) E_h(r)|, via sum r(n)<4."""
    r=Q(r)
    if type(h) is not int or not Q(0)<=r<1:
        raise ValueError('h integer and r in [0,1)')
    return Q(22,7)*8*abs(h)*r*(1-r)
