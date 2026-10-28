"""Source-authenticated BBP Laplace/Mellin virtual-path transfer.

Research scope: exact rational source moments and two-time Hilbert overlaps;
classical limiting Gamma(2) law, a golden-selected first jet, and a signed
Frullani logarithmic chi-square representation.  The complex Mellin/Laplace
fields are diagnostics, NOT Weyl cancellation certificates.  No normality/RH.

Paper: research/2026-10-26/OILY_MACARONI_SOURCE_MELLIN_HILBERT.md.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb, factorial

# Actual Coherent Main X four-pole forcing: a_n=8n-7 and shifts (0,3,4,5).
SOURCE_POLES = ((0, 4), (3, -2), (4, -1), (5, -1))


def checked_n(n):
    if type(n) is not int or n < 1:
        raise ValueError("positive exact source index required")
    return n


def source_a(n):
    return 8 * checked_n(n) - 7


def r_at_a(a):
    """R(a)=Laplace[Q](a); EXACT for positive rational a."""
    if type(a) not in (int, F) or a <= 0:
        raise ValueError("positive rational Laplace parameter required")
    a = F(a)
    return sum((F(c, 1)/(a + d) for d,c in SOURCE_POLES), F())


def authentic_r(n):
    return r_at_a(source_a(n))


def source_taylor_moment(k):
    """Q^(k)(0) for Q(x)=sum_d c_d exp(-d*x); exact integer."""
    if type(k) is not int or k < 0:
        raise ValueError("nonnegative derivative order required")
    return sum(c * (-d)**k for d,c in SOURCE_POLES)


def source_moment(n, k):
    """E_(nu_n)[(a_n X)^k] exact rational, nu_n(dx)=e^-a_nx Q(x)dx/r(n)."""
    checked_n(n)
    if type(k) is not int or k < 0:
        raise ValueError("nonnegative moment order required")
    a=source_a(n)
    m=sum((F(c, 1)/(a+d)**(k+1) for d,c in SOURCE_POLES),F())
    return a**k * factorial(k) * m / authentic_r(n)


def fibonacci_ratio(m):
    """Finite SUCC ratio F_m/F_(m+1), chosen positive Laplace fixed point."""
    if type(m) is not int or m < 1:
        raise ValueError("positive Fibonacci depth")
    u,v=0,1
    for _ in range(m):
        u,v=v,u+v
    return F(u,v)


def finite_first_jet_bounds(n, m, log_terms=36):
    """Certified rational enclosure for d/dz log[E_n(lambda_m z) Gamma_n(1+z)] at z=0.

    E_n(w)=(1+w/n)^n, Gamma_n(1+z)=n! n^z / prod_(k=1)^n(k+z).
    The exact derivative is lambda_m+log(n)-H_n.  Only log(n) is enclosed.
    Uses the repository's already-authenticated rational logarithm module.
    """
    checked_n(n)
    from .euler_mascheroni_succ import rational_log_bounds
    lo,hi=rational_log_bounds(n,terms=log_terms)
    hn=sum((F(1,k) for k in range(1,n+1)),F())
    lam=fibonacci_ratio(m)
    return (lam+lo-hn,lam+hi-hn)



def green_tail_bounds(n, depth=20):
    """Authenticated future BBP Green tail, exact lower and upper Fractions.

    T_n = sum_(j>=1)16^(-j) r(n+j). r(n) decreases strictly.
    Tail beyond depth <= 16^-depth * r(n+depth+1) / 15.
    """
    checked_n(n)
    if type(depth) is not int or not 1 <= depth <= 2048:
        raise ValueError("finite positive green cutoff required")
    lower=sum((F(1,16**j)*authentic_r(n+j) for j in range(1,depth+1)),F())
    upper=lower+F(1,16**depth*15)*authentic_r(n+depth+1)
    return lower,upper


def frullani_square_log_weights(n):
    """Exact coefficients for chi²(nu_a || Gamma2) = sum coeff*log(1+s/a)-1.

    Because Q(0)=0, sum_(d,e)c_d*c_e=0, so log(a) cancels.
    Returns (constant=-1, tuple((s, rational_coeff),...)); coefficients
    include factor -1/(a² r(a)²).  Logs remain unevaluated, not certificates.
    """
    a=source_a(n)
    pref=-F(1,a*a)/authentic_r(n)**2
    by_shift={}
    for d,c in SOURCE_POLES:
        for e,k in SOURCE_POLES:
            by_shift[d+e]=by_shift.get(d+e,0)+c*k
    assert sum(by_shift.values()) == 0
    return F(-1),tuple(sorted((s,pref*v) for s,v in by_shift.items() if v))


def chi_square_limit_coefficient():
    """lim_(a->infinity) a² chi²(nu_a||Gamma2): 2*(59/30)^2."""
    return F(2*59*59,30*30)


def mutant_r(n, strength=F(1)):
    """CONTROL ONLY: alter Q by strength*e^-6x (1-e^-x)^3.

    Positive for nonnegative rational strength, same Q(0),Q'(0),Q''(0),
    but different all-time forcing.  Does not assert nonnormality.
    """
    checked_n(n)
    if type(strength) not in (int,F) or strength < 0:
        raise ValueError("nonnegative exact rational CONTROL strength required")
    a=source_a(n)
    perturb=sum(((-1)**k*comb(3,k)*F(1,a+6+k) for k in range(4)),F())
    return authentic_r(n)+F(strength)*perturb


def _mp():
    try:
        import mpmath as mp
    except ImportError as exc:
        raise RuntimeError("mpmath is optional, for analytic observations only") from exc
    return mp


def golden(mp):
    return (mp.sqrt(5)-1)/2


def _mpf(mp,r):
    r=F(r)
    return mp.mpf(r.numerator)/r.denominator


def complex_r_at(a):
    """Analytic Laplace extension, no gamma/normality input (mpmath observation)."""
    mp=_mp()
    return sum((mp.mpf(c)/(a+d) for d,c in SOURCE_POLES),mp.mpc(0))


def complex_joint_mellin(n,z,s=0,precision=70):
    """E_(nu_n)[(a_n X)^z exp(-s*a_n X)], Re(z)>-1, Re(1+s)>0.

    Exact mathematical formula: Gamma(1+z)*a^z/r(a) *
    sum_d c_d/(a*(1+s)+d)^(1+z). Analytic continuation exists further.
    Cancellation requires precision; value is a numerical observation.
    """
    mp=_mp()
    with mp.workdps(precision):
        a=source_a(n)
        z,s=mp.mpc(z),mp.mpc(s)
        if z.real<=-1 or (1+s).real<=0:
            raise ValueError("outside explicitly certified integral domain")
        raw=sum(mp.mpf(c)*mp.power(a*(1+s)+d,-1-z) for d,c in SOURCE_POLES)
        return +mp.gamma(1+z)*mp.power(a,z)*raw/_mpf(mp,authentic_r(n))


def source_oily_character(n,t,precision=75):
    """Complex CF E[e^(it(log(aX)-1+(lambda/2)aX))] of authentic nu_n.
    No U_n phases involved. OBSERVED, not an arithmetic Weyl estimate.
    """
    mp=_mp()
    with mp.workdps(precision):
        z=mp.j*mp.mpf(t)
        lam=golden(mp)
        return +mp.exp(-z)*complex_joint_mellin(n,z,s=-(lam/2)*z,precision=precision)


def gamma2_oily_character(t,precision=75):
    """Reference Gamma(2) law: e^-it Gamma(2+it)/(1-i lambda t/2)^(2+it)."""
    mp=_mp()
    with mp.workdps(precision):
        z=mp.j*mp.mpf(t)
        lam=golden(mp)
        return +mp.exp(-z)*mp.gamma(2+z)/mp.power(1-(lam/2)*z,2+z)


def first_complex_correction(n,t,precision=75):
    """First-order term to ADD to reference CF, -c*phi*it/(a*(1-it lambda/2))."""
    mp=_mp()
    with mp.workdps(precision):
        z=mp.j*mp.mpf(t)
        lam=golden(mp)
        ref=gamma2_oily_character(t,precision=precision)
        return -(_mpf(mp,F(59,30))*(1+lam)/source_a(n))*(z/(1-(lam/2)*z))*ref


def oily_defect_no_gamma(n,precision=75):
    """O_mac-E_n[Y] source-only calculation; gamma CANCELS exactly.

    Delta = 1+lambda + sum_d c_d log(1+d/a)/(a+d)/r(a)
                      -(lambda/2)*E_(nu_n)[aX].
    All source sums are rational except explicitly declared logs and lambda.
    """
    mp=_mp()
    with mp.workdps(precision):
        a=source_a(n)
        r=_mpf(mp,authentic_r(n))
        logsum=sum(mp.mpf(c)*mp.log1p(mp.mpf(d)/a)/(a+d) for d,c in SOURCE_POLES)
        mean=_mpf(mp,source_moment(n,1))
        lam=golden(mp)
        return +(1+lam+logsum/r-lam*mean/2)


def chi_square_observed(n,precision=90):
    """Exact signed Frullani log sum evaluated numerically; not rigorous interval."""
    mp=_mp()
    with mp.workdps(precision):
        a=source_a(n)
        const,terms=frullani_square_log_weights(n)
        return +(_mpf(mp,const)+sum(_mpf(mp,c)*mp.log1p(mp.mpf(s)/a) for s,c in terms))


def unweighted_overlap_square(n,m):
    """EXACT square of H_nm=R((a_n+a_m)/2)/sqrt(r(n)r(m))."""
    a,b=source_a(n),source_a(m)
    return r_at_a(F(a+b,2))**2/(authentic_r(n)*authentic_r(m))


def complex_time_kernel(n,m,h,t,precision=75):
    """Authentic two-time Hilbert overlap <e(hU_n)f_n,t,e(hU_m)f_m,t>.

    f_n,t(x)= exp(i*t*[log(a_n*x)-1+(lambda/2)*a_n*x])
              *exp(-a_n*x/2)*sqrt(Q(x)/r(n)).
    Gamma (-gamma) first jets cancel in relative f_n,t/f_m,t.
    Exact functional; this evaluation is numerical, NOT signed saving.
    """
    if type(h) is not int:
        raise ValueError("integer Fourier frequency required")
    mp=_mp()
    from .succ_internal_matrix_walk import original_state
    with mp.workdps(precision):
        a,b=source_a(n),source_a(m)
        lam=golden(mp)
        phase=_mpf(mp,original_state(n)-original_state(m))
        tilt=mp.mpf(a+b)/2-mp.j*(lam/2)*mp.mpf(t)*(a-b)
        num=complex_r_at(tilt)
        denom=mp.sqrt(_mpf(mp,authentic_r(n)*authentic_r(m)))
        return +(mp.exp(2*mp.pi*mp.j*h*phase)*mp.power(mp.mpf(a)/b,mp.j*t)*num/denom)


def limiting_log_scale_kernel(ratio,t,precision=75):
    """For a_n/a_m->ratio>0, n,m->inf; phase-free complex virtual kernel."""
    mp=_mp()
    with mp.workdps(precision):
        ratio=_mpf(mp,ratio)
        if ratio<=0: raise ValueError("positive ratio")
        lam=golden(mp)
        den=ratio+1-mp.j*lam*mp.mpf(t)*(ratio-1)
        return +mp.power(ratio,mp.j*t)*4*ratio/(den**2)



def local_hilbert_block_budget(start, count):
    """EXACT rational upper bound for an unweighted Fourier block read via source Hilbert states.

    Let B=[start,...,start+count-1], reference f_start normalized in common L²(dx),
    and H_(n,start)=<f_n,f_start> = R(mid)/sqrt(R_n R_start).
    For |z_n|=1 (in particular original e(hU_n)):

      |avg_B z_n - avg_B z_n*H_(n,start)| <= [8(count-1)/(8start-7)]².

    Proved from Q(x)<=15x, R(a)>=15/a²-59/a³ (a>=16),
    Var_mu_a(X)<=8/a², and the derivative of normalized source sqrt-density.
    No selected phase saving and NO pi-normality theorem.
    """
    checked_n(start)
    if start < 3 or type(count) is not int or count < 1:
        raise ValueError("start>=3 and positive block length required")
    return F(64*(count-1)**2,source_a(start)**2)


def multiscale_hilbert_transport_budget(N):
    """EXACT universal source-Hilbert projection error for the whole Weyl mean.

    Let k=floor(N^(1/3)), M=k²; discard times n<M and partition M..N
    into consecutive blocks of length <=k; in each block choose first-time
    source vector f_m as dual projector.  Then for ANY unit phases z_n:

      |N^-1 sum_(n<=N) z_n -
       N^-1 sum_B sum_(n in B) z_n*<f_n,f_(min B)>|
      <= (M-1)/N + [8(k-1)/(8M-7)]².

    This is O(N^-1/3), rigorous but it DOES NOT bound the projected sum.
    """
    if type(N) is not int or N < 27:
        raise ValueError("N>=27 for integer cube-root schedule")
    lo,hi=1,N+1
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**3<=N:lo=mid
        else:hi=mid
    k=lo;M=k*k
    upper=F(M-1,N)+local_hilbert_block_budget(M,k)
    return {"N":N,"block_length":k,"first_retained":M,
            "discarded":M-1,"error_upper_squared_not_used":False,
            "absolute_mean_error_upper":upper,
            "source_selected_saving_proved":False}



def positive_field_step(n):
    """Exact normalized Feynman-Kac / Boltzmann-Gibbs SUCC factor.

    mu_(n+1)(dx) = exp(-8x)*mu_n(dx)/Z_n,
    Z_n=E_mu_n[exp(-8X)] = r(n+1)/r(n), 0<Z_n<1.
    This reweights math paths; it is NOT a physical realization frequency.
    """
    checked_n(n)
    return authentic_r(n+1)/authentic_r(n)


def finite_field_free_energy_data(N):
    """Finite exact unnormalized free energy vs harmonic SUCC reference.

    Sum_(n=1)^(N-1)(-log Z_n - 2/n)
      = log(r(1)/r(N)) - 2 H_(N-1)
      --> log(3008/225) - 2*EulerGamma.
    Return rational source ratio, harmonic sum, and limiting rational constant
    inside logarithm.  No gamma/log values inserted as finite source inputs.
    """
    checked_n(N)
    harmonic=sum((F(2,k) for k in range(1,N)),F())
    return {"N":N,"source_ratio":authentic_r(1)/authentic_r(N),
            "harmonic_subtraction":harmonic,
            "finite_normalizer_constant":F(64)*authentic_r(1)/F(15),
            "pi_normality_proved":False}


def source_rank_and_claims():
    return {"source_poles":SOURCE_POLES,
            "gamma2_boundary": "PAPER-PROVED, classical Watson/Taylor",
            "laplace_mellin": "PAPER-PROVED exact analytic identity",
            "chi2_frullani": "PAPER-PROVED positive source log expression",
            "virtual_log_overlap": "PAPER-PROVED, true source Hilbert Gram",
            "golden_unique_for_bbp": False,
            "source_selected_weyl_saving": False,
            "pi_normality_proved": False,
            "RH_proved": False}
