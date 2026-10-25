"""Critical harmonic mixtures of positive Fejer/van der Corput correlations.

A source-authenticated *conditional* π normality instrument, NOT a signed
Fourier cancellation estimate. Ordinary N-time averages are preserved; only
lag/block lengths are mixed. Exact rational arithmetic throughout.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .harmonic_mirror_succ import harmonic


def _int(v: int, low: int) -> int:
    if type(v) is not int or v < low:
        raise ValueError(f"integer >= {low} required")
    return v


def mixture_weights(K: int, beta: int = 1) -> tuple[Q, ...]:
    """Distribution on block lengths 1..K: L^(-beta)/Z_beta(K)."""
    _int(K, 1);_int(beta, 0)
    unnormalized = tuple(Q(1, L**beta) for L in range(1,K+1))
    z = sum(unnormalized, Q())
    return tuple(w/z for w in unnormalized)


def lag_kernel(K: int, beta: int = 1) -> tuple[Q, ...]:
    """Nonnegative definite Gram/Fejer mixture c0..c_(K-1).

    c_k=sum_(L>k) q_L (L-k)/L^2, and c0=sum_L q_L/L.
    Kernel symbol c0+2*sum_(k>=1)c_k*cos(k*theta)>=0.
    """
    qs = mixture_weights(K,beta)
    return tuple(sum((q*Q(L-k,L*L)
                      for L,q in enumerate(qs, start=1) if L>k),Q())
                 for k in range(K))


def gaussian_correlations(values: tuple[tuple[int | Q,int | Q], ...],
                          upto: int) -> tuple[Q, ...]:
    """Re(C_k)=Re sum z_(n+k)*conj(z_n), including k=0."""
    _int(upto,1)
    N=len(values)
    if N==0 or upto>N:
        raise ValueError("1<=upto<=number of supplied Gaussian states")
    a=[]
    for x,y in values:
        if type(x) not in (int,Q) or type(y) not in (int,Q):
            raise ValueError("Gaussian coordinates must be exact")
        a.append((Q(x),Q(y)))
    return tuple(sum((a[j+k][0]*a[j][0]+a[j+k][1]*a[j][1]
                      for j in range(N-k)),Q()) for k in range(upto))


def exact_vdc_mixture(values: tuple[tuple[int|Q,int|Q],...], K: int,
                      beta: int = 1) -> tuple[Q, Q, Q]:
    """(true squared mean, raw nonnegative energy, valid upper certificate).

    The inequality holds for ALL finite complex sequences. The energy is the
    harmonic mixture of zero-padded block-square energies. The upper bound
    pays the shared maximal boundary multiplier 1+(K-1)/N.
    """
    N=len(values);_int(K,1)
    if not N or K>N:raise ValueError("1<=K<=N")
    corr=gaussian_correlations(values,K)
    coeffs=lag_kernel(K,beta)
    energy=(coeffs[0]*corr[0]+2*sum((coeffs[k]*corr[k]
                for k in range(1,K)),Q()))/N
    real=sum((Q(x) for x,_ in values),Q())
    imag=sum((Q(y) for _,y in values),Q())
    squared_mean=(real*real+imag*imag)/(N*N)
    rhs=energy*Q(N+K-1,N)
    if energy<0 or rhs<squared_mean:
        raise ArithmeticError("the positive Gram / vdc inequality failed")
    return squared_mean,energy,rhs


def harmonic_source_error_bound(N:int,K:int,h:int) -> Q:
    """Exact upper on (2/N)*sum_(k>=1) c_k E_(k,N,h).

    E_(k,N,h) <= (11*abs(h)/56)*16**k from the authentic BBP
    lag estimate of SUCC NLG. Elementary geometrically weighted cubic
    tail inequality gives <= (88*abs(h)/1575)*16**K/(N*H_K*K**3).
    This is an upper budget, NOT a Fourier bound itself.
    """
    _int(N,2);_int(K,2)
    if K>N:raise ValueError("K may not exceed N")
    if type(h) is not int or h==0:
        raise ValueError("nonzero integer Fourier mode required")
    return Q(88*abs(h)*16**K,1575*N*K**3)/harmonic(K)


def harmonic_exact_source_error_sum(N:int,K:int,h:int) -> Q:
    """Less-coarse rational error from NLG lag bound and exact c_k.

    E_k <= (44/7)/64 * |h| * (16**k-1) * sum_(n<=N-k) 1/n².
    """
    _int(N,2);_int(K,2)
    if K>N:raise ValueError("K may not exceed N")
    if type(h) is not int or h==0:raise ValueError("nonzero integer h required")
    ws=lag_kernel(K)
    total=Q()
    prefix=Q()
    for k in range(1,K):
        nsq=sum((Q(1,n*n) for n in range(1,N-k+1)),Q())
        total+=ws[k]*Q(44*abs(h)*(16**k-1),7*64)*nsq
    return 2*total/N


def conditional_bbp_fourier_upper(N:int,K:int,h:int,
            certified_special_sum_uppers:tuple[Q,...]) -> Q:
    """A valid implication IF externally SUPPLIED |W_k| uppers are sound.

    This function does NOT authenticate its input amplitudes. In particular
    passing zero without a proof does not certify pi normality.
    """
    _int(N,2);_int(K,2)
    if K>N or len(certified_special_sum_uppers)!=K-1:
        raise ValueError("one amplitude upper per lag, with 2<=K<=N")
    if type(h) is not int or h==0:raise ValueError("nonzero integer h")
    values=[]
    for v in certified_special_sum_uppers:
        if type(v) not in (int,Q) or not Q(0)<=v<=N:
            raise ValueError("amplitude uppers must be exact and in [0,N]")
        values.append(Q(v))
    w=lag_kernel(K)
    rhs = (w[0]+Q(2,N)*sum((w[k]*values[k-1]
                     for k in range(1,K)),Q())
           +harmonic_source_error_bound(N,K,h))
    return rhs*Q(N+K-1,N)


def integer_log_16(value:int) -> int:
    _int(value,1)
    j=0
    while 16**(j+1)<=value:
        j+=1
    return j


def critical_harmonic_lag_schedule(N:int) -> int:
    """K=b+3*floor(log_16 b), b=floor(log_16 N); N>=256.

    For N->infinity: K~log_16 N, 16**K <= N*b**3, and
    16**K/(N*K**3*H_K) <= 1/H_K ->0. No float logs.
    """
    _int(N,256)
    b=integer_log_16(N)
    return min(N,b+3*integer_log_16(b))


def naive_signed_harmonic_symbol_pi(K:int) -> Q:
    """Naive 1/k lag cosine kernel evaluated at angle pi.

    1+2*sum_(1<=k<K)(1-k/K)*(-1)**k/k can be NEGATIVE;
    it is not a universally positive Gram kernel. At K=4 gives -1/6.
    """
    _int(K,2)
    return 1+2*sum((Q((K-k)*(-1)**k,K*k) for k in range(1,K)),Q())


def alternating_spectral_symbol_pi(K:int) -> Q:
    """Actual harmonic-Fejer spectral symbol at theta=pi, always >=0."""
    _int(K,1)
    return sum((Q(1,j**3) for j in range(1,K+1,2)),Q())/harmonic(K)


def last_lag_weight_ratio(K:int) -> Q:
    """Harmonic c_(K-1) / pure length-K Fejer c_(K-1) = 1/(K*H_K)."""
    _int(K,2)
    w=lag_kernel(K)[-1]
    return w/Q(1,K*K)
